"""Transaction data structs for compound transactions.

Compound transactions are transactions which contain other
transactions. They must only contain elementary transactions
(i.e. Those defined in transaction_data.py).

Warnings
--------
Vendors and clients should not develop scripts or applications against
this package. The contents may change at any time without warning.
"""
###############################################################################
#
# (C) Copyright 2023, Maptek Pty Ltd. All rights reserved.
#
###############################################################################
import typing

from .transaction_data import (
  TransactionData, CoordinateTransactionData, PrimitiveTransactionData)
from .qualifiers import Qualifiers

if typing.TYPE_CHECKING:
  from .transaction_manager import Transaction

class CoordinatePickTransactionData(TransactionData):
  """Transaction data for a coordinate pick.

  This causes the pick to be realised in the green bar at the
  bottom of the screen.
  """
  coordinate: CoordinateTransactionData

  def __init__(self) -> None:
    super().__init__()
    self.coordinate = CoordinateTransactionData()
    def confirm_parent(
        transaction: "Transaction", data: CoordinateTransactionData):
      parent_transaction = transaction.parent_transaction
      parent_data = CoordinatePickTransactionData()
      parent_data.coordinate = data
      # :HACK: This is bypassing confirm because confirm takes a
      # message handle, not the data.
      parent_transaction._value = parent_data
    self.coordinate.add_qualifier(
      Qualifiers.call_on_confirm(confirm_parent)
    )

  @staticmethod
  def transaction_name() -> str:
    return 'py::pyC_CoordinatePickTransaction'

  @staticmethod
  def data_type_name() -> str:
    return 'mdf::serC_DataGroup'

  @property
  def data(self) -> typing.Tuple[float, float, float]:
    """Get the data of this transaction."""
    coordinate = self.coordinate
    return (coordinate.x, coordinate.y, coordinate.z)

class PrimitivePickTransactionData(TransactionData):
  """Transaction data for a primitive pick.

  This causes the pick to be realised in the status bar at the
  bottom of the screen.
  """
  primitive: PrimitiveTransactionData

  def __init__(self) -> None:
    super().__init__()
    self.primitive = PrimitiveTransactionData()
    def confirm_parent(
        transaction: "Transaction", data: PrimitiveTransactionData):
      parent_transaction = transaction.parent_transaction
      parent_data = PrimitivePickTransactionData()
      parent_data.primitive = data
      # :HACK: This is bypassing confirm because confirm takes a
      # message handle, not the data.
      parent_transaction._value = parent_data
    self.primitive.add_qualifier(
      Qualifiers.call_on_confirm(confirm_parent)
    )

  @staticmethod
  def transaction_name() -> str:
    return 'py::pyC_PrimitivePickTransaction'

  @staticmethod
  def data_type_name() -> str:
    return 'mdf::serC_DataGroup'

  @property
  def data(self) -> typing.Tuple[int, int, int]:
    """Get the data of this transaction."""
    primitive = self.primitive
    return (primitive.owner, primitive.primitive_type, primitive.index)
