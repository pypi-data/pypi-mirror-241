"""A request response server for use in tests."""
###############################################################################
#
# (C) Copyright 2023, Maptek Pty Ltd. All rights reserved.
#
###############################################################################

import threading

from mapteksdk.internal import comms
from mapteksdk.internal.mcp import (McpDll, ExistingMcpdInstance,
                                    connect_to_mcpd)

class RequestResponseServer:
  """A server which can accept a request and send a response.

  Implements the context management protocol to enable the server to be
  shutdown in the event of an exception while dealing with the result.

  Parameters
  ----------
  mcpd_connection
    Connection to the MCPD to use to send messages.
  server_name
    The name of the server to start. Other servers can send messages to
    this server by sending servers to this name.
  messages
    List of tuples of the form (message_type, response_type) which this
    server can respond to.
    The response_type should be None if no response should be sent.
  """

  def __init__(self, mcpd_connection, server_name, messages=None):
    if messages is None:
      messages = []
    # Validate the message list.
    assert all(len(message) for message in messages)
    self.cancellation_event = threading.Event()
    self.server_running = threading.Event()

    def _safe_run(*args):
      # This prevents the test running forever if there is a bug when starting
      # the server in _run().
      try:
        self._run(*args)
      except:
        if not self.server_running.is_set():
          self.server_running.set()
        self.cancellation_event.set()
        print("Stopping server.")
        raise

    self.server_thread = threading.Thread(
      target=_safe_run, args=(mcpd_connection, server_name, messages))

    self._callback_functions = []  # "C functions" (McpDll().dll.Callback)
    self._callback_handles = []  # Handles after registering the callbacks.

    self.server_thread.start()

    mcpd_connection.log.info('Waiting for %s to connect.', server_name)
    self.server_running.wait()
    mcpd_connection.log.info('Now %s is connected.', server_name)

  def stop_server(self):
    """Stop the server.

    This uses out-of-band communication (i.e not the MCP).
    """
    self.cancellation_event.set()
    self.server_thread.join()

  def on_message_received(self, request, response_type):
    """Derived classes should override this function."""
    raise NotImplementedError('Derived classes should override this function. '
                              'The return value should be the response')

  def __enter__(self):
    return self

  def __exit__(self, exception_type, value, traceback):
    self.stop_server()

  def _on_message_received(self, request_type, response_type, message):
    request = request_type.from_handle(message)

    # The response_type should be derivable from request_type by convention.
    response = self.on_message_received(request, response_type)

    if response is not None:
      # The way this reply stuff is set-up needs some work. Possibly a dedicated
      # Response type with a reply() function taking the source message handle.
      reply = McpDll().BeginReply(message)
      # pylint: disable=protected-access; Sending replies are not encapsulated at
      # this time.
      comms._add_content_to_message(reply, response)
      McpDll().Send(reply)

  def _run(self, mcpd_connection, server_name, messages):
    mcpd_connection.log.info(
      "Connect to mcpd as %s: %s", server_name,
      mcpd_connection.socket_path)

    # The connection to the mcpd for this thread (the _run function is called
    # on a new thread).
    our_connection = connect_to_mcpd(
      specific_mcpd=ExistingMcpdInstance(mcpd_connection.mcpd_pid, None,
                                         mcpd_connection.socket_path),
      # Reuse the licence of the initial connection to the mcpd as it should
      # still be valid (i.e. wouldn't have expired yet).
      sdk_licence=mcpd_connection.licence,
      name=server_name)

    try:

      # Register each message type that this is expected to handle.
      for request_type, response_type in messages:
        self._callback_functions.append(
          McpDll().dll.Callback(
            lambda event, req_type=request_type, resp_type=response_type:
              self._on_message_received(req_type, resp_type, event)))

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
        McpDll().dll.McpServicePendingEvents()
    finally:
      our_connection.disconnect()
