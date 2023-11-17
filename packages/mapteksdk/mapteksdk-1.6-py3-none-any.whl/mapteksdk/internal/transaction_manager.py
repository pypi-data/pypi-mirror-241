"""Request transactions without using the Workflows system.

This is an alternative to the classes defined in transactions.py.
Unlike RequestTransactionWithInputs, this requests the transaction the
same way as C++ code in the application would do it. This provides more
versatility than RequestTransactionWithInputs, however it is more difficult
to automate and read outputs.

Warnings
--------
Vendors and clients should not develop scripts or applications against
this package. The contents may change at any time without warning.
"""
###############################################################################
#
# (C) Copyright 2022, Maptek Pty Ltd. All rights reserved.
#
###############################################################################
import ctypes
from contextlib import AbstractContextManager
import itertools
import logging
import time
import typing

from .comms import Request, InlineMessage, Message, RepeatingField
from .serialisation import Context
from .transaction_data import TransactionData
from .transaction_request_data import (
  TransactionRequestData, TransactionRequestDataList)
from ..capi.mcp import Mcpd
from ..capi.types import T_MessageHandle
from .qualifiers import QualifierSet

LOG = logging.getLogger("mapteksdk.internal.transaction_manager")

NEXT_OPERATION_ID = itertools.count(start=1)

T = typing.TypeVar("T", bound=TransactionData)


# :NOTE: These errors are not intended to be user facing. They should be
# caught and converted into user-friendly errors by callers.
class TransactionFailedError(Exception):
  """Error raised when a transaction fails.

  This may indicate this operation is not supported by the application.
  """


class TransactionSetUpError(TransactionFailedError):
  """Exception thrown when failing to start a transaction.

  This indicates the server returned an error response to TransactionRequest.

  Parameters
  ----------
  transaction_name
    Name of the menu command which could not be created.
  """
  def __init__(self, transaction_name: str):
    self.transaction_name = transaction_name
    super().__init__(
      f"Failed to start menu command: {transaction_name}."
    )


class TransactionCancelledError(Exception):
  """Error raised when a menu command is cancelled.

  This indicates the user pressed "Cancel" or closed the window
  without confirming it.
  """
  def __init__(self, transaction_name: str):
    self.transaction_name = transaction_name
    super().__init__(
      f"The following command was cancelled: {transaction_name}."
    )


class TransactionTimeoutError(Exception):
  """Error raised when a transaction times out."""
  def __init__(self, transaction_name: str, timeout: int) -> None:
    super().__init__(
      f"{transaction_name} failed to return a response in {timeout}s."
    )


class TransactionCreate(Request):
  """A message requesting for a transaction to be created."""
  message_name = 'TransactionCreate'

  class Response(InlineMessage):
    """The response to a TransactionCreate message."""
    success: bool
    """True if the transaction was successfully started."""
    server_address: ctypes.c_uint64
    """The address of the transaction on the server."""

  response_type = Response

  transaction_manager_address: ctypes.c_uint64
  """Address of the transaction manager associated with the transaction.

  This is primarily used for undo/redo support, however the
  Python SDK doesn't support this so this isn't used for
  anything other than equality operations.
  """

  # Currently this class doesn't include the parent transaction address
  # because the Python SDK doesn't support it.
  # parent_transaction_address: typing.Optional[ctypes.c_uint64]

  request_data: TransactionRequestData
  """The data of the transaction to request."""

  initial_value: InlineMessage
  """Initial values to place into the panel.

  This is typically (but not required to be) a TransactionData subclass.
  """


class TransactionCreateCompound(Request):
  """A message requesting for a compound transaction to be created.

  As of writing, 2023-02-13, Python cannot handle optional fields in
  Requests. This means a different class is required to handle
  compound transactions because they contain the additional
  child_transactions field.
  """
  message_name = 'TransactionCreate'

  class Response(InlineMessage):
    """The response to a TransactionCreate message."""
    success: bool
    """True if the transaction was successfully started."""
    server_address: ctypes.c_uint64
    """The address of the transaction on the server."""

  response_type = Response

  transaction_manager_address: ctypes.c_uint64
  """Address of the transaction manager associated with the transaction.

  This is primarily used for undo/redo support, however the
  Python SDK doesn't support this so this isn't used for
  anything other than equality operations.
  """

  # Currently this class doesn't include the parent transaction address
  # because the Python SDK doesn't support it.
  # parent_transaction_address: typing.Optional[ctypes.c_uint64]

  request_data: TransactionRequestData
  """The data of the transaction to request."""

  child_transactions: TransactionRequestDataList
  """Child transactions of the request."""

  initial_value: InlineMessage
  """Initial values to place into the panel.

  This must be a TransactionData subclass.
  """


class TransactionDestroy(Message):
  """Destroy a transaction on the server."""
  message_name: typing.ClassVar[str] = "TransactionDestroy"

  parent_transaction_address: ctypes.c_uint64
  """The address of the parent transaction of the transaction to destroy."""

  transaction_address: ctypes.c_uint64
  """The address of the transaction to destroy."""


class TransactionConfirm(Message):
  """A message indicating a transaction has been confirmed.

  This does not parse the entire TransactionConfirm message. Instead
  it only parses the generic part of the message. This is used to identify
  which transaction was confirmed. The transaction then parses the remainder
  of the message (typically via a TransactionData subclass).

  This can never be sent by Python, only received.
  """
  message_name: str = "TransactionConfirm"

  transaction_address: ctypes.c_uint64
  """The address of the transaction which was confirmed.

  This will be the same as in the corresponding TransactionCreate
  message.
  """

  transaction_token: ctypes.c_uint64
  """The token of the transaction which was confirmed.

  This will be the same as in the corresponding TransactionCreate
  message
  """

  def send(self, destination):
    raise TypeError(
      "This type of message is a response only. It shouldn't be sent."
    )


class TransactionCancel(Message):
  """A message indicating a transaction has been cancelled.

  This does not parse the entire TransactionCancel message. Instead it
  only parses the generic part of the message. This is used to identify which
  transaction was cancelled.

  This can never be sent by Python, only received.
  """
  message_name: str = "TransactionCancel"

  top_level_transaction_address: ctypes.c_uint64
  """The address of the top-level transaction which was cancelled."""

  transaction_token: ctypes.c_uint64
  """The token of the transaction which was cancelled."""

  transaction_address: ctypes.c_uint64
  """The address of the transaction which was cancelled."""

  def send(self, destination):
    raise TypeError(
      "This type of message is a response only. It shouldn't be sent."
    )


class Transaction(typing.Generic[T], AbstractContextManager):
  """Class representing a Transaction managed by the TransactionManager.

  Parameters
  ----------
  transaction_manager
    Transaction manager responsible for managing this transaction.
  transaction_data
    The TransactionData subclass indicating which transaction to
    request.
  qualifiers
    Qualifiers to apply to the transaction.
  initial_value
    Instance of the type transaction_data containing the initial values
    for the transaction.
  server_name
    The name of the server which will host the transaction.
  """
  def __init__(
      self,
      transaction_manager: "TransactionManager",
      transaction_data: typing.Type[T],
      initial_value: T,
      server_name: str,
      parent_transaction: typing.Optional["Transaction"]=None):
    self.__transaction_manager = transaction_manager
    self.__transaction_data = transaction_data
    self.__initial_value = initial_value
    self.__token = next(NEXT_OPERATION_ID)
    self._value = None
    self.__is_cancelled = False
    self.__error: typing.Optional[Exception] = None
    """The error this transaction has encountered.

    If this is falsy, the transaction has not encountered an error.
    This error will be raised if wait_for_value() is called.
    """
    self.__server_address = None
    """The address of the server-side representation of the transaction.

    This is required to destruct the server-side representation of this
    transaction.
    """
    self.__server_name = server_name
    """The name of the server which will host the transaction."""
    self.__confirm_callbacks: typing.List[
      typing.Callable[["Transaction"], None]] = []
    self.parent_transaction = parent_transaction
    """The transactions parent, if it has one.

    If the Transaction is a top-level transaction, then this will be None.
    """
    self.__child_transactions = self._register_child_transactions(initial_value)
    if self.parent_transaction and self.__child_transactions:
      raise NotImplementedError(
        "Compound transactions which contain other compound transactions "
        "is not yet implemented."
      )

  def name(self) -> str:
    """The name of the transaction, including the namespace."""
    return self.__transaction_data.transaction_name()

  def key(self) -> typing.Tuple[ctypes.c_uint64, ctypes.c_uint64]:
    """Key which uniquely identifies this transaction (within this process).

    This is used by the transaction manager to determine which transaction
    an event is relevant to.

    Returns
    -------
    tuple
      A tuple containing the id of this Python object and the token
      assigned to this object.
    """
    return (id(self), self.__token)

  def is_compound(self) -> bool:
    """If this is a compound transaction.

    A compound transaction is a transaction which contains other transactions.
    """
    return len(self.__child_transactions) != 0

  def generate_request_data(self) -> TransactionRequestData:
    """Generate request data for this object.

    Returns
    -------
    TransactionRequestData
      Header information required to request the transaction.
    """
    request_data = TransactionRequestData()
    request_data.class_name = self.__transaction_data.transaction_name()
    request_data.data_type_name = self.__transaction_data.data_type_name()
    request_data.transaction_address = id(self)
    request_data.transaction_token = self.__token
    # The qualifiers field starts with an underscore so that it isn't
    # included in the body of the request. Include the qualifiers in
    # the header.
    # pylint: disable=protected-access
    client_qualifiers = self.__initial_value._qualifiers
    server_qualifiers = []
    for qualifier in client_qualifiers.values:
      # Handle qualifiers which the server doesn't need to know about.
      if qualifier.key == "CallOnConfirm":
        self.__confirm_callbacks.append(qualifier.parameters.values[0])
        continue
      server_qualifiers.append(qualifier)

    request_data.qualifiers = QualifierSet()
    request_data.qualifiers.values = server_qualifiers
    return request_data

  def _register_child_transactions(
      self,
      transaction_data: TransactionData
      ) -> typing.List["Transaction"]:
    """Register the child transactions with the TransactionManager.

    Parameters
    ----------
    transaction_data
      TransactionData to register child transactions for.

    Returns
    -------
    list[Transaction]
      List of child transactions for the transaction_data.
      This will be empty if transaction_data was not a compound transaction.
    """
    child_transactions = []
    # Determine the list of fields of the message from the annotations.
    annotations = getattr(transaction_data, '__annotations__', {})
    # Ignore repeating fields and class variables.
    def ignore_annotation(field_type):
      origin = getattr(field_type, '__origin__', type(None))
      return origin is typing.ClassVar or issubclass(origin, RepeatingField)

    fields = list(
      (field_name, field_type)
      for field_name, field_type in annotations.items()
      if not ignore_annotation(field_type))

    for field in fields:
      field_name, field_type = field
      if field_name.startswith("_"):
        continue
      # If the field is a subclass of TransactionData, then this has
      # found a child transaction.
      if issubclass(field_type, TransactionData):
        field_value = getattr(transaction_data, field_name)
        child = self.__transaction_manager.create_transaction(
          field_type,
          field_value,
          self.__server_name,
          self
        )
        child_transactions.append(child)
      else:
        # It is not a compound transaction.
        break

    return child_transactions

  def send(self):
    """Send the transaction to the relevant server.

    Raises
    ------
    TransactionSetUpError
      If the menu command could not be created on the relevant server.
    """
    if self.is_compound():
      request = TransactionCreateCompound()
      request.child_transactions = TransactionRequestDataList()
      request.child_transactions.request_list = [
        child.generate_request_data() for child in self.__child_transactions
      ]
    else:
      request = TransactionCreate()

    request.transaction_manager_address = id(self.__transaction_manager)
    request.request_data = self.generate_request_data()

    request.initial_value = self.__initial_value
    response = request.send(self.__server_name)
    # pylint: disable=no-member
    # Pylint can't figure out that response is of ResponseType.
    if not response.success:
      raise TransactionSetUpError(self.name())
    self.__server_address = response.server_address

  def confirm_received(self, confirm_message):
    """Handle a TransactionConfirm message for this transaction.

    Parameters
    ----------
    message_handle
      Message handle for the confirm message. This assumes that the
      transaction address and token have already been extracted
      from the message.
    """
    # This doesn't currently use the context. Read it and discard it
    # so that the next part of the message can be read.
    _ = Context.from_handle(confirm_message)

    data = self._read_transaction_data(confirm_message)

    # Handle callbacks for the confirm.
    try:
      for callback in self.__confirm_callbacks:
        callback(self, data)
    except Exception as error:
      # The error will be re-raised by wait_for_value().
      self.__error = error
      return

    self._value = data

  def cancel(self):
    """Cancel this transaction.

    This will destroy the server-side representation as if the user
    had cancelled the transaction in the user interface.
    """
    self.__is_cancelled = True
    self._delete_server_side()

  def cancel_received(self, cancel_message):
    """Handle a TransactionCancel message for this transaction.

    Parameters
    ----------
    message_handle
      Message handle for the cancel message. This assumes the transaction
      address and token have already been extracted from the message.
    """
    self.cancel()

    # :NOTE: This could read the context and transaction data,
    # but it isn't used.

  def _delete_server_side(self):
    """Delete the transactions server-side representation.

    This should be called immediately after receiving a response from
    the server to ensure that any UI the server created for the request
    is disposed of quickly.

    It is safe to call this function multiple times.
    """
    if self.__server_address is None:
      return
    destroy_request = TransactionDestroy()
    # We don't currently support parent transactions, so the parent
    # address is the same as the transaction address.
    destroy_request.parent_transaction_address = self.__server_address
    destroy_request.transaction_address = self.__server_address
    destroy_request.send(self.__server_name)
    self.__server_address = None

  def wait_for_value(self, timeout: typing.Optional[float]=None) -> T:
    """Wait for the transaction to be confirmed and return a value.

    Returns
    -------
    T
      The response type for this transaction.
    timeout
      Time in seconds to wait for a value. If a value is not
      returned in this time, a TransactionTimeoutError will be raised.

    Raises
    ------
    TransactionCancelledError
      If the transaction is cancelled. This includes if the MCP
      is shut down.
    TransactionFailedError
      If an error occurs.
    TransactionTimeoutError
      If timeout is specified and no value was received after the
      timeout had elapsed.
    """
    if timeout is None:
      timeout = TransactionManager.default_timeout
    if timeout:
      start_time = time.perf_counter()
    try:
      while True:
        result = Mcpd().dll.McpServicePendingEvents()
        if not result:
          raise TransactionCancelledError(self.name())
        if self._value is not None:
          break
        if self.__is_cancelled:
          break
        if self.__error:
          raise self.__error
        if timeout:
          duration = time.perf_counter() - start_time
          if duration > timeout:
            raise TransactionTimeoutError(self.name(), timeout)
    except OSError as error:
      LOG.exception(error)
      raise
    if self.__is_cancelled:
      raise TransactionCancelledError(self.name())

    assert self._value is not None
    return self._value

  def _read_transaction_data(self, message_handle: T_MessageHandle) -> T:
    """Read the transaction data from a message.

    Parameters
    ----------
    message_handle
      Message handle to read the transaction data from.
      This message handle should already have been partially
      read via TransactionConfirm.from_handle(). This reads the remaining
      data from the message and assigns it to this object so that it
      will be returned by wait_for_value().
    """
    try:
      return self.__transaction_data.from_handle(message_handle)
    except:
      self.__error = TransactionFailedError(
        "Failed to read result of operation."
      )
      raise

  def __exit__(self, __exc_type, __exc_value, __traceback):
    for child in self.__child_transactions:
      self.__transaction_manager._remove_transaction(child)
      child._delete_server_side()
    self.__transaction_manager._remove_transaction(self)
    self._delete_server_side()

class TransactionManager:
  """Manages MCP messages related to transactions.

  This class maintains a list of all of the transactions it has started.
  When an MCP event arrives which is relevant to one of these transactions,
  it parses enough of the message to identify which transaction the message
  is for. It then passes the remainder of that message to the transaction
  for handling.
  """
  default_timeout: typing.ClassVar[typing.Optional[float]]=None
  """The default time out for operations.

  This is None by default, indicating operations should only time out if the
  caller specifies a timeout.
  """

  def __init__(self):
    self.__callback_handles: typing.List[
      typing.Tuple[typing.Any, typing.Callable[[typing.Any], None]], str] = []
    """List of callbacks created by this object.

    Each element of the list is a tuple containing:

    * The callback handle.
    * The callback function.
    * The name of the message which will trigger the callback.

    Both the handle and the function need to be kept until this object is
    destructed to avoid undefined behaviour caused by attempting to call a
    callback which has been disposed of.

    This is also used to ensure all of the callbacks are disposed when
    this object is disposed.
    """

    self.__transactions: typing.Dict[
      typing.Tuple[ctypes.c_uint64, ctypes.c_uint64], Transaction] = {}
    """Dictionary of transactions this object is keeping track of.

    The keys are a tuple of the transaction address and transaction token,
    and the values are the actual Transaction objects.
    """

  def __enter__(self):
    def _on_transaction_confirm(message_handle):
      """Callback run when a TransactionConfirm message arrives."""
      # This reads the generic parts of the TransactionConfirm.
      # It doesn't read to the end of the message, only the
      # generic part at the beginning.
      event = TransactionConfirm.from_handle(message_handle)
      try:
        # pylint: disable=no-member
        # Pylint incorrectly deduces the type of event as Message
        # instead of TransactionConfirm.
        # See: https://github.com/PyCQA/pylint/issues/981
        transaction = self.__transactions[
            (event.transaction_address, event.transaction_token)
          ]
        transaction.confirm_received(message_handle)
      except KeyError:
        # pylint: disable=no-member
        # Same issue as in the try block.
        LOG.info(
          "Received TransactionConfirm for: "
          "transaction_address: %s "
          "transaction token: %s "
          "But it was not found in the transaction list",
          event.transaction_address, event.transaction_token)

    def _on_transaction_cancel(message_handle):
      """Callback run when a TransactionCancel message arrives."""
      event = TransactionCancel.from_handle(message_handle)

      try:
        # pylint: disable=no-member
        transaction = self.__transactions[
          (event.transaction_address, event.transaction_token)
        ]
        transaction.cancel_received(message_handle)

      except KeyError:
        # pylint: disable=no-member
        LOG.info(
          "Received TransactionCancel for: "
          "transaction_address: %s "
          "transaction token: %s "
          "But it was not found in the transaction list",
          event.transaction_address, event.transaction_token)

    self.__register_callback(
      "TransactionConfirm",
      _on_transaction_confirm
    )
    self.__register_callback(
      "TransactionCancel",
      _on_transaction_cancel
    )
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    for transaction in list(self.__transactions.values()):
      self._remove_transaction(transaction)
    for callback_handle, _, message_name in self.__callback_handles:
      Mcpd().dll.McpRemoveCallbackOnMessage(
        message_name.encode("utf-8"), callback_handle)

  def __register_callback(self, event_name: str, callback):
    """Register a callback to be called for the given MCP event.

    This handles registering the callback to be removed when this
    object is disposed.

    Parameters
    ----------
    event_name
      The name of the event which should call the callback.
    callback
      Function which accepts a message handle and returns no value
      to be called when the event arrives.
    """
    callback_handle = Mcpd().dll.Callback(callback)
    # :TRICKY: Include the callback handle in the tuple to ensure
    # it is not garbage collected before it is called.
    self.__callback_handles.append(
      (Mcpd().dll.McpAddCallbackOnMessage(
        event_name.encode("utf-8"),
        callback_handle
      ), callback_handle, event_name)
    )

  def create_transaction(
      self,
      data_type: typing.Type[T],
      initial_value: T,
      server_name: str,
      parent_transaction: typing.Optional[Transaction]=None
      ) -> Transaction[T]:
    """Create a new transaction managed by this object.

    This transaction is not sent to the server.

    Parameters
    ----------
    data_type
      The data type of the transaction.
    qualifiers
      The qualifiers of the transaction.
    initial_values
      The initial values of the transaction.
    server_name
      The name of the server which will host the transaction.

    Returns
    -------
    Transaction
      The newly created Transaction.
    """
    if not isinstance(initial_value, data_type):
      raise TypeError(
        f"Initial value should be type '{data_type.__name__}', "
        f"not {type(initial_value).__name__}"
      )
    transaction = Transaction(
      self,
      data_type,
      initial_value,
      server_name,
      parent_transaction
    )
    key = transaction.key()
    self.__transactions[key] = transaction
    return transaction

  def _remove_transaction(self, transaction: Transaction):
    """Remove the transaction from the transaction manager.

    This will cause MCP events intended for this transaction to be
    ignored. This will do nothing if the transaction has already been
    removed, or was never added to this object.

    Parameters
    ----------
    transaction
      The transaction to remove.
    """
    try:
      del self.__transactions[transaction.key()]
    except KeyError:
      pass
