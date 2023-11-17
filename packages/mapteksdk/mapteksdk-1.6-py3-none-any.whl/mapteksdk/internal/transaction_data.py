"""Transaction data structs for elemental transactions.

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
import pathlib
import typing

from .comms import InlineMessage
from .writable_selection import WritableSelection
from .qualifiers import QualifierSet, Qualifier

DATA_GROUP = "mdf::serC_DataGroup"

class TransactionData(InlineMessage):
  """Abstract base class for TransactionData classes.

  Classes which implement this can be used to set the initial values
  displayed in a panel when requesting a transaction or to read the values
  which the user entered into the panel.

  A TransactionData subclass can either be an elementary transaction
  or a compound transaction. An elementary transaction cannot
  contain other TransactionData subclasses. A compoundTransaction
  only contains TransactionData for elementary transactions.

  Warnings
  --------
  The TransactionData for a compound transaction must only contain
  TransactionData subclasses which are elementary transactions.

  Examples
  --------
  Imagine a simplified version of the panel for creating 2D text which accepts
  only a single string and a single point. The inputs are represented as
  type hinted variables on the class (A point is represented as three floats).
  Then the inheriting class needs to determine the name of the transaction.

  >>> class SimpleLabelTransactionData(TransactionData):
  ...     message: str
  ...     X: ctypes.c_float64
  ...     Y: ctypes.c_float64
  ...     Z: ctypes.c_float64
  ...     @classmethod
  ...     def transaction_name():
  ...         return "mdf::cadC_SimpleLabelTransaction"
  """
  def __init__(self) -> None:
    super().__init__()
    self._qualifiers: QualifierSet = QualifierSet()
    self._qualifiers.values = []

  @staticmethod
  def transaction_name() -> str:
    """The name of the transaction this data is for.

    This includes the namespace.
    """
    raise NotImplementedError("Must be implemented in child classes.")

  @staticmethod
  def data_type_name() -> str:
    """The name of the data type this transaction accepts.

    This is "mdf::serC_DataGroup" by default, which is what most montages
    use, however child classes may overwrite this if they use a different type.
    """
    return DATA_GROUP

  def add_qualifier(self, qualifier: Qualifier):
    """Add a qualifier to the TransactionData.

    This qualifier will be sent with the data.
    """
    self._qualifiers.values.append(qualifier)

  def add_qualifiers(self, qualifiers: typing.Iterable[Qualifier]):
    """Add an iterable of qualifiers to the TransactionData."""
    self._qualifiers.values.extend(qualifiers)

class StringTransactionData(TransactionData):
  """TransactionData for a simple request of a string.

  This is realised as a panel with a single text box the user can type a string
  into.
  """
  data: str

  @staticmethod
  def transaction_name() -> str:
    return "mdf::uiC_ElementalTransaction<mdf::Tstring>"

  @staticmethod
  def data_type_name() -> str:
    return "mdf::Tstring"


class DoubleTransactionData(TransactionData):
  """TransactionData for a simple request of a 64 bit float.

  By default this is realised as a panel with a single text box the user
  can type a number into.
  """
  data: ctypes.c_double

  @staticmethod
  def transaction_name() -> str:
    return "mdf::uiC_ElementalTransaction<double>"

  @staticmethod
  def data_type_name() -> str:
    return "::Tfloat64"


class BooleanTransactionData(TransactionData):
  """TransactionData for a simple request of a boolean.

  If this is a top-level request, it is realised as a panel with a "Yes" and
  a "No" button.
  """
  data: bool

  @staticmethod
  def transaction_name() -> str:
    return "mdf::uiC_ElementalTransaction<bool>"

  @staticmethod
  def data_type_name() -> str:
    return "::Tbool"

class CoordinateTransactionData(TransactionData):
  """TransactionData for a simple request of a point.

  If this is a top-level request, it is realised by the view entering
  pick mode.

  Warnings
  --------
  If this is used as a top-level request, it will not be possible
  to cancel the pick.
  """
  x: ctypes.c_double
  y: ctypes.c_double
  z: ctypes.c_double

  @staticmethod
  def transaction_name() -> str:
    return "mdf::uiC_ElementalTransaction<geoS_Point>"

  @staticmethod
  def data_type_name() -> str:
    return "mdf::geoS_Point"

class PrimitiveTransactionData(TransactionData):
  """TransactionData for a simple request of a primitive."""
  owner: ctypes.c_uint64
  primitive_type: ctypes.c_int32
  index: ctypes.c_uint32

  @staticmethod
  def transaction_name() -> str:
    return "mdf::uiC_ElementalTransaction<mdf::mdlC_Primitive>"

  @staticmethod
  def data_type_name() -> str:
    return "mdf::mdlC_Primitive"


class PathTransactionData(TransactionData):
  """TransactionData for a Path request."""
  path_string: str
  contains_environment_variables: bool
  is_valid: bool
  is_absolute: bool
  is_network: bool
  end_of_root: ctypes.c_uint32

  @staticmethod
  def transaction_name() -> str:
    return "mdf::uiC_ElementalTransaction<mdf::sysC_Path>"

  @staticmethod
  def data_type_name() -> str:
    return "mdf::sysC_Path"

  @classmethod
  def construct_from_pathlib(cls, path: pathlib.Path) -> "PathTransactionData":
    """Construct this object from a pathlib.Path object.

    This will make the path absolute.
    """
    absolute_path = path.absolute()
    result = cls()
    result.path_string = str(absolute_path)
    result.is_valid = True

    # Pathlib paths can't have environment variables in them.
    result.contains_environment_variables = False

    # This always makes the path absolute.
    result.is_absolute = True

    drive = absolute_path.drive
    # A network drive path is of the form:
    # \\<machine name>\<share>
    # If the absolute path starts with \\ then it must be a network share.
    result.is_network = drive.startswith("\\\\")

    # The C++ code considers the drive to be "C:/", whereas pathlib
    # considers it to be "C:". Add an extra character to get the correct
    # length.
    result.end_of_root = ctypes.c_uint32(len(drive) + 1)

    return result

  @classmethod
  def invalid_path(cls) -> "PathTransactionData":
    """Get the representation for an invalid path."""
    result = cls()
    result.path_string = ""
    result.contains_environment_variables = False
    result.is_valid = False
    result.is_absolute = False
    result.is_network = False
    result.end_of_root = 0
    return result

  def __eq__(self, __value: object) -> bool:
    if not isinstance(__value, PathTransactionData):
      return False
    # Two invalid paths are always equal regardless of other properties.
    if (not self.is_valid) and (not __value.is_valid):
      return True
    return (
      self.path_string == __value.path_string
      and self.contains_environment_variables
        == __value.contains_environment_variables
      and self.is_valid == __value.is_valid
      and self.is_absolute == __value.is_absolute
      and self.is_network == __value.is_network
      and self.end_of_root == __value.end_of_root
    )

  def __str__(self) -> str:
    if not self.is_valid:
      return "***Invalid Path***"
    return f"PathTransactionData('{self.path_string}')"

  @property
  def data(self) -> pathlib.Path:
    """Return the data stored in the object.

    This returns the path string.
    """
    if not self.is_valid:
      raise RuntimeError(
        "Cannot convert invalid path to pathlib Path."
      )
    if self.contains_environment_variables:
      raise NotImplementedError(
        "Handling of paths containing environment variables is not implemented."
      )
    return pathlib.Path(self.path_string)

class WritableSelectionTransactionData(TransactionData):
  """Transaction data for requesting a change of the active selection."""
  data: WritableSelection
  @staticmethod
  def transaction_name() -> str:
    return "mdf::uiC_WritableSelectionTransaction"

  @staticmethod
  def data_type_name() -> str:
    return "mdf::selC_WritableSelection"
