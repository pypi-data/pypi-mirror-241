"""Classes designed to be serialised in MCP messages.

The classes declared in this file must not depend on
the data subpackage.

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
import json
import typing

from mapteksdk.internal.comms import InlineMessage, SubMessage
from mapteksdk.internal.qualifiers import QualifierSet

class Icon:
  """This type should be used in the definition of a message where an icon is
  expected.
  """
  storage_type = str

  def __init__(self, name=''):
    self.name = name

  @classmethod
  def convert_from(cls, storage_value):
    """Convert from the underlying value to this type."""
    assert isinstance(storage_value, cls.storage_type)
    return cls(storage_value)

  @classmethod
  def convert_to(cls, value):
    """Convert the icon name to a value of the storage type (str).

    Returns
    -------
      A str which is the name of the icon.

    Raises
    ------
    TypeError
      If value is not a Icon or str, i.e the value is not an icon.
    """
    if isinstance(value, cls):
      return value.name
    if isinstance(value, str):
      return value

    raise TypeError('The value for a Icon should be either an Icon or str.')


class JsonValue:
  """This type should be used in the definition of a Message where JSON is
  expected.
  """

  storage_type = str

  def __init__(self, value):
    self.value = value

  def __str__(self):
    return str(self.value)

  @classmethod
  def convert_from(cls, storage_value):
    """Convert from the underlying value to this type."""
    assert isinstance(storage_value, cls.storage_type)
    return cls(json.loads(storage_value))

  @classmethod
  def convert_to(cls, value):
    """Convert the value to the storage type.

    Returns
    -------
      The serialised value to a JSON formatted str.

    Raises
    ------
    TypeError
      If value is not a JsonValue or not suitable for seralisation to JSON
      with Python's default JSON encoder.
    """
    if isinstance(value, cls):
      return json.dumps(value.value)

    return json.dumps(value)

class KeyBinding(InlineMessage):
  """A key binding for a transaction."""
  is_valid: bool
  is_hold_and_click: bool
  key: ctypes.c_uint32 # keyE
  modifiers: ctypes.c_uint32 # keyE_Modifier

class Context(SubMessage):
  """Transaction context object."""
  active_view_id: ctypes.c_uint64
  active_view_name: str
  associated_view_ids: typing.Set[ctypes.c_uint64]
  workspace_views: typing.Set[ctypes.c_uint64]
  finish_hint: ctypes.c_uint8 # uiC_Outcome (Enum)
  selection_contains_objects: bool
  selection_type: ctypes.c_int32 # picE_SelectionType
  # A datetime is represented as two floats - a day number and seconds
  # since midnight.
  # Converting these to/from a Python datetime is non-trivial, so just
  # pretend it is two floats.
  selection_last_change_time_day_number: ctypes.c_double
  selection_last_change_time_seconds_since_midnight: ctypes.c_double
  key_modifiers: ctypes.c_uint32 # keyE_Modifiers
  key_binding: KeyBinding
  scones: QualifierSet
  cookies: QualifierSet

  @classmethod
  def default_context(cls) -> "Context":
    """Return a context filled with default values."""
    context = cls()

    default_key_binding = KeyBinding()
    default_key_binding.is_valid = False
    default_key_binding.is_hold_and_click = False
    default_key_binding.key = 0
    default_key_binding.modifiers = 0

    scones = QualifierSet()
    scones.values = []

    cookies = QualifierSet()
    cookies.values = []

    context.active_view_id = 0
    context.active_view_name = ""
    context.associated_view_ids = set()
    context.workspace_views = set()
    context.finish_hint = 43 # "Success"
    context.selection_contains_objects = False
    context.selection_type = 0
    context.selection_last_change_time_day_number = 0.0
    context.selection_last_change_time_seconds_since_midnight = 0.0
    context.key_modifiers = 0
    context.key_binding = default_key_binding
    context.scones = scones
    context.cookies = cookies

    return context


class FixedInteger16Mixin:
  """A base-type for use with an enumeration that is a 16-bit integer.

  This class exists because ctypes.c_int16 can't be used as the base
  type of the enumerations due to having its own metaclass.

  To define an enumeration using this type:
  >>> import enum
  >>> class Example(FixedInteger16Mixin, enum.IntEnum)
  ...   PRIMARY = 1
  ...   SECONDARY = 2
  ...   TERTIARY = 3
  """
  storage_type: typing.ClassVar = ctypes.c_int16

  @classmethod
  def convert_from(cls, value):
    """Converts the underlying value to the enumeration type."""
    return cls(value)

  def convert_to(self) -> ctypes.c_int16:
    """Convert the enumeration to the value that serialised."""
    return ctypes.c_int16(self.value)


class FixedInteger32Mixin:
  """A base-type for use with an enumeration that is a 32-bit integer.

  This class exists because ctypes.c_int132 can't be used as the base
  type of the enumerations due to having its own metaclass.

  To define an enumeration using this type:
  >>> import enum
  >>> class Example(FixedInteger32Mixin, enum.IntEnum)
  ...   PRIMARY = 1
  ...   SECONDARY = 2
  ...   TERTIARY = 3
  """
  storage_type: typing.ClassVar = ctypes.c_int32

  @classmethod
  def convert_from(cls, value):
    """Converts the underlying value to the enumeration type."""
    return cls(value)

  def convert_to(self) -> ctypes.c_int32:
    """Convert the enumeration to the value that serialised."""
    return ctypes.c_int32(self.value)
