"""MCP messages intended to be used in tests.

These messages are expected to not be appropriate for use in the actual SDK,
and thus should only be used for testing.
"""
###############################################################################
#
# (C) Copyright 2023, Maptek Pty Ltd. All rights reserved.
#
###############################################################################

import typing
import ctypes

from mapteksdk.internal import comms
from mapteksdk.internal.serialisation import Context
from mapteksdk.internal.transaction_data import PathTransactionData
from mapteksdk.internal.transaction_request_data import TransactionRequestData
from mapteksdk.internal.writable_selection import WritableSelection

T = typing.TypeVar("T")


class TransactionConfirmHeader(comms.InlineMessage):
  """The header for a TransactionConfirm message."""
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
  context: Context

  def __init__(
      self,
      transaction_address: typing.Union[ctypes.c_uint64, int],
      transaction_token: typing.Union[ctypes.c_uint64, int]) -> None:
    if not isinstance(transaction_address, ctypes.c_uint64):
      transaction_address = ctypes.c_uint64(transaction_address)
    if not isinstance(transaction_token, ctypes.c_uint64):
      transaction_token = ctypes.c_uint64(transaction_token)

    self.transaction_address = transaction_address
    self.transaction_token = transaction_token
    self.context = Context.default_context()


class TransactionCreateHeader(comms.InlineMessage):
  """A message requesting for a transaction to be created."""
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


class TransactionCancelHeader(comms.InlineMessage):
  """The header for a TransactionCancel message.

  This is more detailed than the TransactionCancel class available in
  the Python SDK because the Python SDK only reads the first few fields
  of the message. As this needs to be sent, it contains the entire header
  of the message.
  """
  top_level_transaction_address: ctypes.c_uint64
  """The address of the top-level transaction which was cancelled."""

  transaction_token: ctypes.c_uint64
  """The token of the transaction which was cancelled."""

  transaction_address: ctypes.c_uint64
  """The address of the transaction which was cancelled."""

  context: Context
  """The context of the cancelled transaction.

  As of 2023-06-06 this is not read by the Python SDK. It is included
  here so that the send message matches what would be send by an
  application.
  """
  def __init__(
      self,
      top_level_transaction_address: ctypes.c_uint64,
      transaction_token: ctypes.c_uint64,
      transaction_address: ctypes.c_uint64) -> None:
    self.top_level_transaction_address = top_level_transaction_address
    self.transaction_token = transaction_token
    self.transaction_address = transaction_address
    self.context = Context.default_context()


if typing.TYPE_CHECKING:
  class TransactionCreateProtocol(typing.Protocol[T]):
    """Protocol which represents a transaction create message."""
    header: TransactionCreateHeader
    """The header of the TransactionCreate message.

    This is the same for all TransactionCreate messages.
    """
    body: T
    """The body of the TransactionCreate message.

    This differs depending on what transaction is being created.
    """


  class TransactionConfirmProtocol(typing.Protocol[T]):
    """Protocol which represents a transaction confirm message."""
    header: TransactionConfirmHeader
    """The header of the TransactionConfirm message.

    This is the same for all TransactionConfirm messages.
    """

    body: T
    """The body of the TransactionConfirm message.

    This differs depending on the transaction which was confirmed.
    """

  class TransactionCancelProtocol(typing.Protocol[T]):
    """Protocol which represents a transaction cancel message."""
    header: TransactionCancelHeader
    """Header for the TransactionCancel message.

    This is the same for all TransactionCancel messages.
    """
    body: T
    """The body of the TransactionCancel message.

    This differs depending on the transaction which was cancelled.
    """

class DoubleTransactionCreate(comms.Message):
  """Transaction create for requesting a double.

  This allows for a Transaction create message for a double
  to be received.
  """
  message_name: str = "TransactionCreate"
  header: TransactionCreateHeader
  body: ctypes.c_double

class DoubleTransactionConfirm(comms.Message):
  """Transaction confirm for requesting a double."""
  message_name: str = "TransactionConfirm"

  header: TransactionConfirmHeader
  body: ctypes.c_double

class DoubleTransactionCancel(comms.Message):
  """Transaction cancel for requesting a double."""
  message_name: str = "TransactionCancel"

  header: TransactionCancelHeader
  body: ctypes.c_double

class PathTransactionCreate(comms.Message):
  """Transaction create for requesting a path."""
  message_name: str = "TransactionCreate"
  header: TransactionCreateHeader
  body: PathTransactionData

class PathTransactionConfirm(comms.Message):
  """Transaction confirm for requesting a path."""
  message_name: str = "TransactionConfirm"

  header: TransactionConfirmHeader
  body: PathTransactionData

class PathTransactionCancel(comms.Message):
  """Transaction cancel for requesting a path."""
  message_name: str = "TransactionCancel"

  header: TransactionCancelHeader
  body: PathTransactionData


class WritableSelectionCreate(comms.Message):
  """TransactionCreate for requesting a WritableSelection."""
  message_name: str = "TransactionCreate"
  header: TransactionCreateHeader
  body: WritableSelection


class WritableSelectionConfirm(comms.Message):
  """TransactionConfirm for requesting a WritableSelection."""
  message_name: str = "TransactionConfirm"
  header: TransactionConfirmHeader
  body: WritableSelection


class WritableSelectionCancel(comms.Message):
  """TransactionCancel for requesting a WritableSelection."""
  message_name: str = "TransactionCancel"
  header: TransactionCancelHeader
  body: WritableSelection
