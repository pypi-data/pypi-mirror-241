"""The transaction request object.

Warnings
--------
Vendors and clients should not develop scripts or applications against
this package. The contents may change at any time without warning.
"""
import ctypes

from .comms import InlineMessage, SubMessage, RepeatingField
from .qualifiers import QualifierSet

class TransactionRequestData(InlineMessage):
  """Data required to request a transaction.

  This can be used either for top-level transactions, or for
  transactions which request other transactions.
  """
  class_name: str
  """The class name of the transaction to request.

  This should include the namespace.
  """

  data_type_name: str
  """The data type name for this transaction."""

  transaction_address: ctypes.c_uint64
  """The address of the transaction object.

  This is used, along with the transaction token, to uniquely
  identify the transaction.
  """

  transaction_token: ctypes.c_uint64
  """The transaction token.

  This is used, along with the transaction address, to uniquely
  identify the transaction. This should be different for every
  message sent within the same process.
  """

  qualifiers: QualifierSet
  """Qualifiers to apply to the transaction."""

class TransactionRequestDataList(SubMessage):
  """A repeating field of TransactionRequestData.

  This is used to represent the metadata of the child transactions of
  a compound transaction.
  """
  request_list: RepeatingField[TransactionRequestData]
