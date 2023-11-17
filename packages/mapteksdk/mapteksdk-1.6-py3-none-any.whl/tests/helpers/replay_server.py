"""Server which can receive and reply to MCP messages."""
###############################################################################
#
# (C) Copyright 2023, Maptek Pty Ltd. All rights reserved.
#
###############################################################################

import dataclasses
import queue
import threading
import typing

from mapteksdk.internal import comms
from mapteksdk.internal.mcp import (ExistingMcpdInstance, McpDll,
                                    connect_to_mcpd)

from tests.helpers.errors import MessageSequenceError

MAX_RETRIES = 10
"""Maximum retries to wait for a message to arrive."""

MessageSubclass = typing.TypeVar("MessageSubclass", bound=comms.Message)
"""A subclass of the Message type."""

@dataclasses.dataclass
class ReceiveMessageData(typing.Generic[MessageSubclass]):
  """Indicates the next operation is to receive a message."""
  expected_message_type: typing.Type[MessageSubclass]
  """The type of message expected to be received."""
  verify_function: typing.Callable[[MessageSubclass], None]
  """Function which verifies the received message is correct.

  It accepts an instance of the MessageSubclass. If the MessageSubclass
  is not verified correctly, it should raise an exception.
  """
  generate_reply: typing.Optional[
    typing.Callable[[MessageSubclass], comms.Message]]
  """Function which generates the reply to the message.

  This is passed the message and should return the reply.
  If this is None, no reply will be sent.
  """


@dataclasses.dataclass
class SendMessageData(typing.Generic[MessageSubclass]):
  """Indicates the next operation is to send a message."""
  generate_message: typing.Callable[[], MessageSubclass]
  """Function which generates the message to send."""
  destination_name: str
  """The name of the server to send the message to."""


OperationSequence: "typing.TypeAlias" = typing.List[
  typing.Union[SendMessageData, ReceiveMessageData]]
"""A sequence of operations expected for a client or server.

A SendMessageData dataclass indicates that this client/server is expected to
send a message.
A ReceiveMessageData dataclass indicates that this client/server is expecting
to receive a message.
Each operation in the sequence is expected to occur in order.
"""


class ReplayServer:
  """A server which replays messages recorded from an application server.

  Implements the context management protocol to enable the server to be
  shutdown in the event of an exception while dealing with the result.

  Parameters
  ----------
  mcpd_connection
    Connection to the MCPD to use to send messages.
  server_name
    The name of the server to start. Other servers can send messages to
    this server by sending messages to this name.

  Warnings
  --------
  This class assumes that the messages are sent and received in a specific
  order. If this is not the case, tests which use it will encounter random
  test fails based on the order that messages are sent / received.

  """

  def __init__(
      self,
      mcpd_connection,
      server_name,
      expected_operations: OperationSequence):
    message_set: typing.Set[comms.Message] = set()
    for operation in expected_operations:
      if isinstance(operation, ReceiveMessageData):
        message_set.add(operation.expected_message_type)

    self.cancellation_event = threading.Event()
    self.server_running = threading.Event()
    self.mcpd_connection = mcpd_connection
    self.__expected_operations = expected_operations
    self.__message_buffer: queue.Queue[
      typing.Tuple[type[comms.Message], typing.Any]] = queue.Queue()
    """Buffer used to store MCP messages before they are processed.

    Each item is a tuple containing the type of the received message and the
    handle to use to read the message.
    This class assumes that MCP messages always arrive in order and thus
    it makes sense for them to be stored in a queue.
    """
    self.error: typing.Optional[Exception] = None
    self.finished_event = threading.Event()

    def _safe_run(*args):
      # This prevents the test running forever if there is a bug when starting
      # the server in _run().
      try:
        self._run(*args)
      except Exception as error:
        self.cancellation_event.set()
        mcpd_connection.log.info("Stopping server.")
        self.error = error
        raise

    self.server_thread = threading.Thread(
      target=_safe_run, args=(mcpd_connection, server_name, message_set))

    self._callback_functions = []  # "C functions" (McpDll().dll.Callback)
    self._callback_handles = []  # Handles after registering the callbacks.

    self.server_thread.start()

    mcpd_connection.log.info('Waiting for %s to connect.', server_name)
    self.server_running.wait()

  def send_message(self, message_data: SendMessageData[comms.Message]):
    """Send a message.

    Parameters
    ----------
    message_data
      MessageData containing the message to send to the client.
    """
    message = message_data.generate_message()
    self.mcpd_connection.log.info(
      f"sending message '{message.message_name}' "
      f"to {message_data.destination_name}"
    )
    # This doesn't read the response. Handling responses could be
    # added in the future if required.
    message.send(message_data.destination_name)

  def receive_message(self, expected_data: ReceiveMessageData[comms.Message]):
    """Assert that the next message received is correct.

    Parameters
    ----------
    expected_data
      Expected data for the next message.
    """
    McpDll().dll.McpServicePendingEvents()
    retries = 0
    while retries < MAX_RETRIES:
      try:
        message_type, message_handle = self.__message_buffer.get(timeout=0.01)
        if message_type != expected_data.expected_message_type:
          expected_name = expected_data.expected_message_type.message_name
          actual_name = message_type.message_name
          raise MessageSequenceError(
            f"Expected message of type: {expected_name}, "
            f"not a message of type: {actual_name}"
          )
        message = message_type.from_handle(
          message_handle)
        break
      except queue.Empty:
        # The queue was empty after the timeout. Service pending MCP events
        # so that the message can arrive.
        McpDll().dll.McpServicePendingEvents()
        retries += 1
    else:
      # This is run if the max retry count is reached.
      expected_name = expected_data.expected_message_type.message_name
      raise TimeoutError(
        f"Timed out waiting for {expected_name} to arrive."
      )

    expected_data.verify_function(message)

    if expected_data.generate_reply is not None:
      # The way this reply stuff is set-up needs some work. Possibly a dedicated
      # Response type with a reply() function taking the source message handle.
      reply = McpDll().BeginReply(message_handle)
      # pylint: disable=protected-access; Sending replies are not encapsulated at
      # this time.
      comms._add_content_to_message(
        reply, expected_data.generate_reply(message))
      McpDll().Send(reply)

  def stop_server(self):
    """Stop the server.

    This uses out-of-band communication (i.e not the MCP).
    """
    self.cancellation_event.set()
    self.server_thread.join()

  def __enter__(self):
    return self

  def __exit__(self, exception_type, value, traceback):
    before_error = self.error
    if before_error:
      raise before_error
    self.finished_event.wait(10.0)
    self.stop_server()
    after_error = self.error
    if after_error:
      raise after_error

  def _on_message_received(self, request_type, message):
    """Callback when a message is received.

    This adds the message to the message buffer, queueing it to be processed.
    """
    self.__message_buffer.put((request_type, message))

  def _run(
      self,
      mcpd_connection,
      server_name: str,
      message_types: typing.Set[comms.Message]):

    # The connection to the mcpd for this thread (the _run function is called
    # on a new thread).
    replay_connection = connect_to_mcpd(
      specific_mcpd=ExistingMcpdInstance(self.mcpd_connection.mcpd_pid, None,
                                         self.mcpd_connection.socket_path),
      # Reuse the licence of the initial connection to the mcpd as it should
      # still be valid (i.e. should't have expired yet).
      sdk_licence=self.mcpd_connection.licence,
      name=server_name)

    try:
      # Register each message type that this is expected to handle.
      for request_type in message_types:
        self._callback_functions.append(
          McpDll().dll.Callback(
            lambda event, req_type=request_type:
              self._on_message_received(req_type, event)))

        callback_handle = McpDll().dll.McpAddCallbackOnMessage(
          request_type.message_name.encode('utf-8'),
          self._callback_functions[-1])

        self._callback_handles.append(callback_handle)

      # Inform the creator that the server has been started and should be
      # connected to the mcpd.
      self.server_running.set()

      # Wait for the message on the server to be received and in the meantime
      # service any events that we may receive.
      while not self.cancellation_event.is_set():
        if len(self.__expected_operations) == 0:
          mcpd_connection.log.info(
            "All operations expected completed. Closing down server.")
          break
        next_operation = self.__expected_operations.pop(0)
        if isinstance(next_operation, SendMessageData):
          self.send_message(next_operation)
        else:
          mcpd_connection.log.info(
            "Server waiting for: " +
            next_operation.expected_message_type.message_name)
          self.receive_message(next_operation)
    finally:
      self.finished_event.set()
      replay_connection.disconnect()
