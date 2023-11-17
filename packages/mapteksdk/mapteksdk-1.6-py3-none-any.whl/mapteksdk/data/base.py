"""The base classes of all objects in a Project.

The basic unit of data in a Project is an object. All objects in a Project
are subclasses of DataObject and thus can access the properties and
functions defined by DataObject.

Objects which are intended to be visualised, such as Surface, Polyline
or Polygon, inherit from the Topology class.

Objects which are not intended to be visualised on their own, such
as colour maps and rasters, inherit directly from the DataObject class.

For objects which contain other objects, see mapteksdk.data.containers.

"""
###############################################################################
#
# (C) Copyright 2020, Maptek Pty Ltd. All rights reserved.
#
###############################################################################
from __future__ import annotations

import ctypes
import datetime
import dataclasses
import functools
import logging
import typing

import numpy as np
from pyproj.enums import WktVersion

from ..capi import DataEngine, Modelling
from ..capi.util import CApiFunctionNotSupportedError
from ..internal.colour_map_information import ColourMapInformation
from ..internal.lock import ReadLock, WriteLock, LockType
from ..internal.singular_data_property_read_only import (
  SingularDataPropertyReadOnly)
from .change_reasons import ChangeReasons
from ..internal.singular_data_property_read_write import (
  SingularDataPropertyReadWrite)
from .coordinate_systems import CoordinateSystem, LocalTransform
from .errors import (
  CannotSaveInReadOnlyModeError, ReadOnlyError, AlreadyAssociatedError,
  NonOrphanRasterError)
from .objectid import ObjectID
from .primitive_type import PrimitiveType

if typing.TYPE_CHECKING:
  import sys

  from .images import Raster
  from .colourmaps import ColourMap
  from .primitives.attribute_key import AttributeKey

  if sys.version_info >= (3, 11):
    from typing import Self
  else:
    Self = typing.Any

# pylint: disable=too-many-lines
# pylint: disable=too-many-instance-attributes
log = logging.getLogger("mapteksdk.data")

try:
  final = typing.final
except AttributeError:
  # :TODO: SDK-506 typing.final was added to the typing module in
  # Python 3.8. When dropping support for Python 3.7, this try
  # catch can be removed.
  # pylint: disable=invalid-name
  def final(f):
    """Empty decorator to replace final in Python 3.7."""
    return f

_NO_COORDINATE_SYSTEM: typing.Literal[
  "NO_COORDINATE_SYSTEM"] = "NO_COORDINATE_SYSTEM"
"""Placeholder representing the absence of a coordinate system."""

ObjectAttributeTypes = typing.Union[
  None, typing.Type[None], ctypes.c_bool, ctypes.c_int8, ctypes.c_uint8,
  ctypes.c_int16, ctypes.c_uint16, ctypes.c_int32, ctypes.c_uint32,
  ctypes.c_int64, ctypes.c_uint64, ctypes.c_float, ctypes.c_double,
  ctypes.c_char_p, datetime.datetime, datetime.date]
"""Alias for the union of valid ctypes types for object attributes."""

ObjectAttributeTypesWithAlias = typing.Union[
  ObjectAttributeTypes, bool, str, int, float]
"""Object attribute types plus Python types which alias common types.

For convenience some functions treat certain Python types as aliases
for C types. The aliases are displayed in the following tables.

+-------------+-----------------+
| Python type | C type          |
+=============+=================+
| bool        | ctypes.c_bool   |
+-------------+-----------------+
| str         | ctypes.c_char_p |
+-------------+-----------------+
| int         | ctypes.c_int16  |
+-------------+-----------------+
| float       | ctypes.c_double |
+-------------+-----------------+

Notes
-----
The above table only applies for object-level attributes.
"""

ObjectAttributeDataTypes = typing.Union[
  None, typing.Type[None], typing.Type[ctypes.c_bool],
  typing.Type[ctypes.c_int8], typing.Type[ctypes.c_uint8],
  typing.Type[ctypes.c_int16], typing.Type[ctypes.c_uint16],
  typing.Type[ctypes.c_int32], typing.Type[ctypes.c_uint32],
  typing.Type[ctypes.c_int64], typing.Type[ctypes.c_uint64],
  typing.Type[ctypes.c_float], typing.Type[ctypes.c_double],
  typing.Type[ctypes.c_char_p], typing.Type[datetime.datetime],
  typing.Type[datetime.date]]
"""Alias for the union of valid data types for object attributes."""

class AlreadyOpenedError(RuntimeError):
  """Error raised when attempting to open an object multiple times."""

class Extent:
  """A multidimensional, axially-aligned "intervals" or "extents".

  This extent is bound to a volume in 3D space.

  This is also known as a Axis-Aligned Bounding Box (AABB).

  Attributes
  ----------
  minimum
    Point representing minimum values in the form [x, y, z].
  maximum
    Point representing maximum values in the form [x, y, z].
  """
  def __init__(
      self,
      minimum: tuple[float, float, float],
      maximum: tuple[float, float, float]):
    self.minimum = minimum
    self.maximum = maximum

    if not all(lower <= upper for lower, upper in zip(minimum, maximum)):
      # This raises an error to inform the caller that they made a mistake.
      #
      # It may seem tempting to automatically fix the values by taking the min
      # and max of the pairs. However, if such a mistake was made it is
      # possible that another was made as well. For example, one of the inputs
      # may have came from the wrong source (property/variable).
      raise ValueError('minimum must be less than or equal to maximum.')

    assert len(self.minimum) == len(self.maximum)

  def __contains__(self, value: tuple[float, float, float] | Extent):
    """Return true if value is contained within the extent.

    An extent is contained within another extent if:

    - Its lower bound is greater than or equal to the other extent's lower
      bound.
    - Its upper bound is less than or equal to the other extent's upper bound.
    """
    if isinstance(value, Extent):
      def within_1d_extent(value, lower, upper):
        """Return True if value is within lower and upper or is lower or upper.
        """
        return lower <= value <= upper

      return all([
        # Check along the X-axis.
        within_1d_extent(value.minimum[0], self.minimum[0], self.maximum[0]),
        within_1d_extent(value.maximum[0], self.minimum[0], self.maximum[0]),

        # Check along the Y-axis.
        within_1d_extent(value.minimum[1], self.minimum[1], self.maximum[1]),
        within_1d_extent(value.maximum[1], self.minimum[1], self.maximum[1]),

        # Check along the Z-axis.
        within_1d_extent(value.minimum[2], self.minimum[2], self.maximum[2]),
        within_1d_extent(value.maximum[2], self.minimum[2], self.maximum[2]),
      ])

    return all(a >= b for a, b in zip(value, self.minimum)) and \
        all(a <= b for a, b in zip(value, self.maximum))

  @property
  def centre(self) -> tuple[float, float, float]:
    """Returns the center of the extent.

    Returns
    -------
    point
      Point representing the center of the extent.
    """
    assert len(self.minimum) == len(self.maximum)
    midpoints = [
      (minimum + maximum) / 2.0
      for minimum, maximum in zip(self.minimum, self.maximum)
    ]

    # The temporary conversion to a list causes mypy to think this tuple
    # is of type tuple[float, ...] (i.e. It forgets how long the tuple is).
    return tuple(midpoints) # type: ignore

  @property
  def length(self) -> float:
    """The length is the maximum of the X, Y or Z dimension.

    Returns
    -------
    float
      Maximum width of the extent.
    """
    assert len(self.minimum) == len(self.maximum)
    lengths = [
      maximum - minimum
      for minimum, maximum in zip(self.minimum, self.maximum)
    ]
    return max(lengths)

  @property
  def span(self) -> tuple[float, float, float]:
    """The span of the extent in each direction."""
    return tuple(max - min for max, min in zip(self.maximum, self.minimum))

  def as_numpy(self) -> np.ndarray:
    """Returns the extent as a numpy array.

    Returns
    -------
    np.array
      The extent representing as a numpy array.
    """
    return np.array(self.minimum + self.maximum)

  def overlaps(self, other: Extent) -> bool:
    """Return True if this extent and the other overlap.

    The extents overlap if they share space which includes if:

    - They extend over each other and partially cover the same space.
    - One extent overlaps another by being inside of the other.
    - The two extents come into contact with one another at a single point.
    - The two extents come into contact with one another along a line.
    - The two extents come into contact in a two dimensional rectangular area,
      similar to two boxes placed next to each other. No part of either extent
      is inside of the other extent, but both extents are touching.

    Parameters
    ----------
    other
      The extent to check if it overlaps with this extent.
    """

    return all([
      # Check the overlap for the X-axis.
      self.minimum[0] <= other.maximum[0],
      self.maximum[0] >= other.minimum[0],

      # Check the overlap for the Y-axis.
      self.minimum[1] <= other.maximum[1],
      self.maximum[1] >= other.minimum[1],

      # Check the overlap for the Z-axis.
      self.minimum[2] <= other.maximum[2],
      self.maximum[2] >= other.minimum[2],
    ])


@dataclasses.dataclass
class _ObjectAttribute:
  """Holds data for an object attribute."""
  name : str
  """The name of the object attribute."""
  id : int
  """The ID of the object attribute."""
  dtype : ObjectAttributeDataTypes
  """The data type of the object attribute."""
  value : typing.Any
  """The data stored in this attribute.

  This is None by default.
  """

class DataObject:
  """The basic unit of data in a Project.

  Each object can be referenced (opened/loaded) from its ID, see `ObjectID`,
  `Project.read()` and `Project.edit()`.
  """

  # This corresponds to C++ type called mdf::deC_Object.

  _object_attribute_table: dict[int, ObjectAttributeDataTypes] = {
    0: None, 1: type(None), 2: ctypes.c_bool, 3: ctypes.c_int8,
    4: ctypes.c_uint8, 5: ctypes.c_int16, 6: ctypes.c_uint16,
    7: ctypes.c_int32, 8: ctypes.c_uint32, 9: ctypes.c_int64,
    10: ctypes.c_uint64, 11: ctypes.c_float, 12: ctypes.c_double,
    13: ctypes.c_char_p, 14: datetime.datetime, 15: datetime.date,
  }
  """Dictionary which maps object attribute type ids to Python types."""

  def __init__(self, object_id: ObjectID, lock_type: LockType, *,
               rollback_on_error: bool = False):
    """Opens the object for read or read-write.

    It is recommended to go through `Project.read()` and `Project.edit()`
    instead of constructing this object directly.

    Parameters
    ----------
    object_id
      The ID of the object to open for read or read-write.
    lock_type
      Specify read/write operation intended for the
      lifespan of this object instance.
    rollback_on_error
      When true, changes should be rolled back if there is an error.
    """
    assert object_id
    self.__id: ObjectID = object_id
    self.__lock_type: LockType = lock_type
    self.__object_attributes: dict[
      str, _ObjectAttribute] | None = None
    self.__lock_opened = False
    self._lock: ReadLock | WriteLock = self.__begin_lock(rollback_on_error)

  @classmethod
  def static_type(cls):
    """Return this type as stored in a Project."""
    raise NotImplementedError(
      "Static type must be implemented on child classes.")

  @property
  def id(self) -> ObjectID[DataObject]:
    """Object ID that uniquely references this object in the project.

    Returns
    -------
    ObjectID
      The unique id of this object.
    """
    return self.__id

  @property
  def closed(self) -> bool:
    """If this object has been closed.

    Attempting to read or edit a closed object will raise an ObjectClosedError.
    Such an error typically indicates an error in the script and should not
    be caught.

    Examples
    --------
    If the object was opened with the Project.new(), Project.edit() or
    Project.read() in a "with" block, this will be True until the with
    block is closed and False afterwards.

    >>> with self.project.new("cad/point_set", PointSet) as point_set:
    >>>     point_set.points = [[1, 2, 3], [4, 5, 6]]
    >>>     print("closed?", point_set.closed)
    >>> print("closed?", point_set.closed)
    closed? False
    closed? True
    """
    return self._lock.is_closed

  @property
  def is_read_only(self) -> bool:
    """If this object is read-only.

    This will return True if the object was open with Project.read()
    and False if it was open with Project.edit() or Project.new().
    Attempting to edit a read-only object will raise an error.
    """
    return self.lock_type is not LockType.READWRITE

  @property
  def lock_type(self) -> LockType:
    """Indicates whether operating in read-only or read-write mode.

    Use the is_read_only property instead for checking if an object
    is open for reading or editing.

    Returns
    -------
    LockType
      The type of lock on this object. This will be LockType.ReadWrite
      if the object is open for editing and LockType.Read if the object
      is open for reading.
    """
    return self.__lock_type

  def _invalidate_properties(self):
    """Invalidates the properties of the object.

    The next time a property is requested, its values will be loaded from the
    project.
    """
    self._extra_invalidate_properties()

  def _extra_invalidate_properties(self):
    """Invalidate properties defined by the child class.

    This is called during _invalidate_properties() and should never
    be called directly.
    Child classes must implement this to invalidate the properties
    they define. They must not overwrite _invalidate_properties().
    """
    raise NotImplementedError(
      "_extra_invalidate_properties must be implemented on child classes"
    )

  # Child classes should place their child-specific function in _save()
  # instead of overwriting or overriding save().
  @final
  def save(self) -> ChangeReasons:
    """Save the changes made to the object.

    Generally a user does not need to call this function, because it is called
    automatically at the end of a with block using Project.new() or
    Project.edit().

    Returns
    -------
    ChangeReasons
      The change reasons for the operation. This depends on what changes
      to the object were saved.
      If the api_version is less than 1.9, this always returns
      ChangeReasons.NO_CHANGE.
    """
    self._raise_if_save_in_read_only()
    self._save()
    self._invalidate_properties()
    return self._checkpoint()

  def _save(self):
    """Save the properties defined by the child class.

    This is called during save() and should never be called directly.
    Child classes must implement this to save the properties they define.
    They must not overwrite save().
    """
    raise NotImplementedError("_save() must be implemented on child classes")

  def close(self):
    """Closes the object.

    This should be called as soon as you are finished working with an object.
    To avoid needing to remember to call this function, open the object using
    a with block and project.read(), project.new() or project.edit().
    Those functions automatically call this function at the end of the with
    block.

    A closed object cannot be used for further reading or writing. The ID of
    a closed object may be queried and this can then be used to re-open the
    object.
    """
    self.__end_lock()

  def _checkpoint(self) -> ChangeReasons:
    """Checkpoint the saved changes to the object.

    This makes the changes to the object saved by save() visible to
    readers of the lock.
    """
    self._raise_if_read_only("Save changes")
    return ChangeReasons(DataEngine().Checkpoint(self._lock.lock))

  def _raise_if_read_only(self, operation: str):
    """Raise a ReadOnlyError if this object is open for read-only.

    The message is: "Cannot {operation} in read-only mode".

    Parameters
    ----------
    operation
      The operation which cannot be done in read-only mode.
      This should not start with a capital letter and should describe
      what operation cannot be performed in read-only mode.

    Raises
    ------
    ReadOnlyError
      If this object is open for read-only.
    """
    if self.is_read_only:
      raise ReadOnlyError(f"Cannot {operation} in read-only mode.")

  def _raise_if_save_in_read_only(self):
    """Raise a CannotSaveInReadOnlyModeError if open for read-only.

    This should be called in the save() function of child classes.

    Raises
    ------
    CannotSaveInReadOnlyModeError
      If this object is open for read-only.
    """
    if self.is_read_only:
      error = CannotSaveInReadOnlyModeError()
      log.error(error)
      raise error

  def __begin_lock(self, rollback_on_error: bool) -> ReadLock | WriteLock:
    if self.__lock_opened:
      raise AlreadyOpenedError(
        "This object has already been opened. After closing the object, you "
        "should start a new context manager using the with statement.")
    self.__lock_opened = True
    lock: ReadLock | WriteLock
    if self.__lock_type is LockType.READWRITE:
      lock = WriteLock(self.__id.handle, rollback_on_error=rollback_on_error)
      log.debug("Opened object for writing: %s of type %s",
                self.__id, self.__derived_type_name)
    else:
      lock = ReadLock(self.__id.handle)
      log.debug("Opened object for reading: %s of type %s",
                self.__id, self.__derived_type_name)
    return lock

  def __end_lock(self):
    if not self.closed:
      self._lock.close()
      if self.__lock_type is LockType.READWRITE:
        log.debug("Closed object for writing: %s of type %s",
                  self.__id, self.__derived_type_name)
      else:
        log.debug("Closed object for reading: %s of type %s",
                  self.__id, self.__derived_type_name)

  def __enter__(self) -> Self:
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    """Close the object. See close()"""
    self.close()

  @property
  def __derived_type_name(self) -> str:
    """Return qualified name of the derived object type."""
    return type(self).__qualname__

  def __repr__(self) -> str:
    return f'{self.__derived_type_name}({self.__id})'

  # =========================================================================
  # Properties of the underlying object in the project.
  # =========================================================================

  @property
  def created_date(self) -> datetime.datetime:
    """The date and time (in UTC) of when this object was created.

    Returns
    -------
    datetime.datetime:
      The date and time the object was created.
      0:0:0 1/1/1970 if the operation failed.
    """
    value = ctypes.c_int64() # value provided in microseconds
    success = DataEngine().GetObjectCreationDateTime(
      self._lock.lock, ctypes.byref(value))
    if success:
      try:
        return datetime.datetime.fromtimestamp(float(value.value) / 1000000,
                                               datetime.timezone.utc).replace(
                                                 tzinfo=None)
      except (OSError, OverflowError) as error:
        message = str(error)
    else:
      message = DataEngine().ErrorMessage().decode('utf-8')

    log.warning(
      'Failed to determine the creation date of object %s because %s',
      self.id, message)
    return datetime.datetime.fromtimestamp(0, datetime.timezone.utc).replace(
      tzinfo=None)

  @property
  def modified_date(self) -> datetime.datetime:
    """The date and time (in UTC) of when this object was last modified.

    Returns
    -------
    datetime.datetime
      The date and time this object was last modified.
      0:0:0 1/1/1970 if the operation failed.
    """
    value = ctypes.c_int64() # value provided in microseconds
    success = DataEngine().GetObjectModificationDateTime(
      self._lock.lock, ctypes.byref(value))
    if success:
      return datetime.datetime.fromtimestamp(float(value.value) / 1000000,
                                             datetime.timezone.utc).replace(
                                               tzinfo=None)

    message = DataEngine().ErrorMessage().decode('utf-8')
    log.warning(
      'Failed to determine the last modified date of object %s because %s',
      self.id, message)
    return datetime.datetime.fromtimestamp(0, datetime.timezone.utc).replace(
      tzinfo=None)

  @property
  def _revision_number(self) -> int:
    """The revision number of the object.

    This is incremented when save() is called or when the object is closed
    by project.edit() (assuming a change was made).

    If the application is too old to support this, the revision number
    will always be zero.

    Warnings
    --------
    The revision number is not stored persistently. If a maptekdb is
    closed and reopened, the revision number for each object will reset
    to one.
    """
    return DataEngine().GetObjectRevisionNumber(self._lock.lock) or 0

  @property
  def _object_attributes(self) -> dict[str, _ObjectAttribute]:
    """Property for accessing the object attributes.

    When first called, the names of all object attributes are cached.
    """
    if self.__object_attributes is None:
      self.__object_attributes = self.__construct_attribute_dictionary()
    return self.__object_attributes

  @typing.overload
  def set_attribute(
      self,
      name: str,
      dtype: typing.Type[datetime.date],
      data: datetime.date | tuple[float]):
    ...

  @typing.overload
  def set_attribute(
      self,
      name: str,
      dtype: typing.Type[datetime.datetime],
      data: datetime.datetime | str):
    ...

  @typing.overload
  def set_attribute(
      self,
      name: str,
      dtype: type[int],
      data: int):
    ...

  @typing.overload
  def set_attribute(
      self,
      name: str,
      dtype: type[float],
      data: float):
    ...

  @typing.overload
  def set_attribute(
      self,
      name: str,
      dtype: type[bool],
      data: bool):
    ...

  @typing.overload
  def set_attribute(
      self,
      name: str,
      dtype: type[str],
      data: str):
    ...

  @typing.overload
  def set_attribute(
      self,
      name: str,
      dtype: ObjectAttributeDataTypes,
      data: ObjectAttributeTypesWithAlias):
    ...

  def set_attribute(
      self,
      name: str,
      dtype: type[
        ObjectAttributeTypes | datetime.datetime | datetime.date | bool |
        int | float | str] | None,
      data: typing.Any):
    """Sets the value for the object attribute with the specified name.

    This will overwrite any existing attribute with the specified name.

    Parameters
    ----------
    name
      The name of the object attribute for which the value should be set.
    dtype
      The type of data to assign to the attribute. This should be
      a type from the ctypes module or datetime.datetime or datetime.date.
      Passing bool is equivalent to passing ctypes.c_bool.
      Passing str is equivalent to passing ctypes.c_char_p.
      Passing int is equivalent to passing ctypes.c_int16.
      Passing float is equivalent to passing ctypes.c_double.
    data
      The value to assign to object attribute `name`.
      For `dtype` = datetime.datetime this can either be a datetime
      object or timestamp which will be passed directly to
      datetime.fromtimestamp().
      For `dtype` = datetime.date this can either be a date object or a
      tuple of the form: (year, month, day).

    Raises
    ------
    ValueError
      If `dtype` is an unsupported type.
    TypeError
      If `value` is an inappropriate type for object attribute `name`.
    ValueError
      If `name` starts or ends with whitespace or is empty.
    RuntimeError
      If a different error occurs.

    Notes
    -----
    If an error occurs after adding a new object attribute or editing
    an existing object attribute resulting in save() not being called,
    the changes to the object attributes can only be undone if
    the application's API version is 1.6 or greater.

    Prior to mapteksdk 1.6:
    Adding new object attributes, or editing the values of object
    attributes, will not be undone if an error occurs.

    Examples
    --------
    Create an object attribute on an object at "target" and then read its
    value.

    >>> import ctypes
    >>> from mapteksdk.project import Project
    >>> project = Project()
    >>> with project.edit("target") as edit_object:
    ...     edit_object.set_attribute("count", ctypes.c_int16, 0)
    ... with project.read("target") as read_object:
    ...     print(read_object.get_attribute("count"))
    0
    """
    self._raise_if_read_only("set object attributes")
    if name.strip() != name:
      raise ValueError(
        "Attribute names must not contain leading or trailing whitespace. "
        f"Invalid attribute name: '{name}'."
      )
    if name == "":
      raise ValueError(
        "Attribute name must not be empty."
      )
    attribute_id = DataEngine().GetAttributeId(name.encode("utf-8"))

    if dtype == bool:
      dtype = ctypes.c_bool
    elif dtype == str:
      dtype = ctypes.c_char_p
    elif dtype == int:
      dtype = ctypes.c_int16
    elif dtype == float:
      dtype = ctypes.c_double

    if dtype is datetime.datetime and not isinstance(data, datetime.datetime):
      data = datetime.datetime.fromtimestamp(data, datetime.timezone.utc)
      data = data.replace(tzinfo=None)  # Remove timezone awareness.

    if dtype is datetime.date and not isinstance(data, datetime.date):
      data = datetime.date(data[0], data[1], data[2])

    try:
      result = self.__save_attribute(attribute_id,
                                     dtype,
                                     data)
    except ctypes.ArgumentError as exception:
      raise TypeError(f"Cannot convert {data} of type {type(data)} to "
                      f"type: {dtype}.") from exception
    except AttributeError as exception:
      raise TypeError(f"Cannot convert {data} of type {type(data)} to "
                      f"type: {dtype}.") from exception

    if not result:
      message = DataEngine().ErrorMessage().decode('utf-8')
      raise RuntimeError(f"Failed to save attribute: '{name}' on object "
                         f"'{self.id}'. {message}")

    if name in self._object_attributes:
      self._object_attributes[name].value = data
      self._object_attributes[name].dtype = dtype
      self._object_attributes[name].id = attribute_id
    else:
      self._object_attributes[name] = _ObjectAttribute(name, attribute_id,
                                                       dtype, data)

  def attribute_names(self) -> list[str]:
    """Returns a list containing the names of all object-level attributes.

    Use this to iterate over the object attributes.

    Returns
    -------
    list
      List containing the attribute names.

    Examples
    --------
    Iterate over all object attributes of the object stared at "target"
    and print their values.

    >>> from mapteksdk.project import Project
    >>> project = Project()
    >>> with project.read("target") as read_object:
    ...     for name in read_object.attribute_names():
    ...         print(name, ":", read_object.get_attribute(name))
    """
    return list(self._object_attributes.keys())

  def get_attribute(self, name: str) -> ObjectAttributeTypes:
    """Returns the value for the attribute with the specified name.

    Parameters
    ----------
    name
      The name of the object attribute to get the value for.

    Returns
    -------
    ObjectAttributeTypes
      The value of the object attribute `name`.
      For `dtype` = datetime.datetime this is an integer representing
      the number of milliseconds since 1st Jan 1970.
      For `dtype` = datetime.date this is a tuple of the form:
      (year, month, day).

    Raises
    ------
    KeyError
      If there is no object attribute called `name`.

    Warnings
    --------
    In the future this function may be changed to return datetime.datetime
    and datetime.date objects instead of the current representation for
    object attributes of type datetime.datetime or datetime.date.
    """
    attribute = self._object_attributes[name]
    # If value is None and the type is not NoneType, the value will
    # need to be loaded from the DataEngine.
    if attribute.value is None and attribute.dtype is not type(None):
      attribute.value = self.__load_attribute_value(attribute.id,
                                                    attribute.dtype)
    return attribute.value

  def get_attribute_type(self, name: str) -> ObjectAttributeDataTypes:
    """Returns the type of the attribute with the specified name.

    Parameters
    ----------
    name
      Name of the attribute whose type should be returned.

    Returns
    -------
    ObjectAttributeDataTypes
      The type of the object attribute `name`.

    Raises
    ------
    KeyError
      If there is no object attribute called `name`.
    """
    return self._object_attributes[name].dtype

  def delete_all_attributes(self):
    """Delete all object attributes attached to an object.

    This only deletes object attributes and has no effect
    on PrimitiveAttributes.

    Raises
    ------
    RuntimeError
      If all attributes cannot be deleted.
    """
    result = DataEngine().DeleteAllAttributes(self._lock.lock)

    if not result:
      message = DataEngine().ErrorMessage().decode('utf-8')
      raise RuntimeError(f"Failed to delete all attributes on object: "
                         f"'{self.id}'. {message}")

    self.__object_attributes = None

  def delete_attribute(self, attribute: str) -> bool:
    """Deletes a single object-level attribute.

    Deleting a non-existent object attribute will not raise an error.

    Parameters
    ----------
    attribute : str
      Name of attribute to delete.

    Returns
    -------
    bool
      True if the object attribute existed and was deleted;
      False if the object attribute did not exist.

    Raises
    ------
    RuntimeError
      If the attribute cannot be deleted.
    """
    # Get the attribute id from the attribute name
    if attribute not in self._object_attributes:
      # If the attribute doesn't exist, no need to delete it.
      return False
    attribute_id = self._object_attributes[attribute].id
    result = DataEngine().DeleteAttribute(self._lock.lock, attribute_id)

    if not result:
      message = DataEngine().ErrorMessage().decode('utf-8')
      raise RuntimeError(f"Failed to delete attribute '{attribute}' on "
                         f"object '{self.id}'. {message}.")

    self._object_attributes.pop(attribute)
    return result

  def __construct_attribute_dictionary(self) -> dict[
      str, _ObjectAttribute]:
    """Constructs the object attribute dictionary.

    This constructs a blank dictionary containing the name, id and type
    of every object attribute on this object.

    Returns
    -------
    dict
      Dictionary of object attributes. Key is the name, value is
      a __ObjectAttribute containing the name, id, type and a None
      value for the object attribute.

    """
    attributes: dict[str, _ObjectAttribute] = {}
    # Get the attribute id list
    # Get size of list
    attr_list_size = DataEngine().GetAttributeList(
      self._lock.lock,
      None,
      0)
    id_buf = (ctypes.c_uint32 * attr_list_size) # Create buffer type
    attribute_buffer = id_buf() # Create buffer
    # Get the list of attributes
    DataEngine().GetAttributeList(self._lock.lock,
                                  attribute_buffer,
                                  attr_list_size)

    for attribute in attribute_buffer:
      # Get the attribute name
      char_sz = DataEngine().GetAttributeName(attribute, None, 0)
      # Create string buffer to hold path
      str_buffer = ctypes.create_string_buffer(char_sz)
      DataEngine().GetAttributeName(attribute, str_buffer, char_sz)
      name = str_buffer.value.decode("utf-8")

      # Get the attribute data type
      dtype_id = DataEngine().GetAttributeValueType(
        self._lock.lock,
        attribute)

      dtype = self._object_attribute_table[dtype_id.value]

      attributes[name] = _ObjectAttribute(name, attribute, dtype, None)

    return attributes

  def __save_attribute(
      self,
      attribute_id: int,
      dtype: ObjectAttributeDataTypes,
      data: ObjectAttributeTypes) -> bool:
    """Saves an attribute to the project.

    Parameters
    ----------
    attribute_id
      Attribute ID for the object attribute the value should be set for.
    dtype
      The data type of the object attribute.
    data
      The value to assign to the object attribute. This can be any type
      which can be trivially converted to dtype.
    """
    result = False
    if dtype is None:
      pass
    elif dtype is type(None):
      result = DataEngine().SetAttributeNull(
        self._lock.lock,
        attribute_id)
    elif dtype is ctypes.c_char_p or dtype is str:
      result = DataEngine().SetAttributeString(
        self._lock.lock,
        attribute_id,
        data.encode("utf-8"))
    elif dtype is datetime.datetime:
      assert isinstance(data, datetime.datetime)
      data = data.replace(tzinfo=datetime.timezone.utc)
      result = DataEngine().SetAttributeDateTime(
        self._lock.lock,
        attribute_id,
        int(data.timestamp() * 1000000))
    elif dtype is datetime.date:
      assert isinstance(data, datetime.date)
      result = DataEngine().SetAttributeDate(
        self._lock.lock,
        attribute_id,
        data.year,
        data.month,
        data.day)
    else:
      if isinstance(dtype, str):
        raise TypeError(f"Invalid dtype \"{dtype}\". Pass the type directly, "
                         "not a string containing the name of the type.")
      try:
        # Try to handle the 'easy' data types. The data types in the
        # dictionary don't require any extra handling on the Python side.
        # :TRICKY: This dictionary can't be a property of the class because
        # DataEngine() will raise an error if there is no connected
        # application.
        dtype_to_c_api_function: dict[
            type, typing.Callable] = {
          ctypes.c_bool : DataEngine().SetAttributeBool,
          bool : DataEngine().SetAttributeBool,
          ctypes.c_int8 : DataEngine().SetAttributeInt8s,
          ctypes.c_uint8 : DataEngine().SetAttributeInt8u,
          ctypes.c_int16 : DataEngine().SetAttributeInt16s,
          ctypes.c_uint16 : DataEngine().SetAttributeInt16u,
          ctypes.c_int32 : DataEngine().SetAttributeInt32s,
          ctypes.c_uint32 : DataEngine().SetAttributeInt32u,
          ctypes.c_int64 : DataEngine().SetAttributeInt64s,
          ctypes.c_uint64 : DataEngine().SetAttributeInt64u,
          ctypes.c_float : DataEngine().SetAttributeFloat32,
          ctypes.c_double : DataEngine().SetAttributeFloat64,
        }
        result = dtype_to_c_api_function[dtype](
          self._lock.lock, attribute_id, data)
      except KeyError:
        raise TypeError(f"Unsupported dtype: \"{dtype}\".") from None

    return result

  def __load_attribute_value(
      self, attribute_id: int, dtype: ObjectAttributeDataTypes
      ) -> ObjectAttributeTypes:
    """Loads the value of an object attribute.

    This loads the value of the object attribute with the specified
    id and type from the Project.

    Parameters
    ----------
    attribute_id
      ID of the attribute to load.
    dtype
      The type of the attribute to load.

    Returns
    -------
    ObjectAttributeTypes
      The value of the attribute.
    """
    if dtype is None:
      raise KeyError(f"Object attribute: {attribute_id} does not exist.")
    if dtype is type(None):
      # The type was null so there is no data here but there is still an
      # attribute.
      return None

    type_to_function: dict[type, typing.Callable] = {
      ctypes.c_bool: DataEngine().GetAttributeValueBool,
      ctypes.c_int8: DataEngine().GetAttributeValueInt8s,
      ctypes.c_uint8: DataEngine().GetAttributeValueInt8u,
      ctypes.c_int16: DataEngine().GetAttributeValueInt16s,
      ctypes.c_uint16: DataEngine().GetAttributeValueInt16u,
      ctypes.c_int32: DataEngine().GetAttributeValueInt32s,
      ctypes.c_uint32: DataEngine().GetAttributeValueInt32u,
      ctypes.c_int64: DataEngine().GetAttributeValueInt64s,
      ctypes.c_uint64: DataEngine().GetAttributeValueInt64u,
      ctypes.c_float: DataEngine().GetAttributeValueFloat32,
      ctypes.c_double: DataEngine().GetAttributeValueFloat64,

      # The following types need special handling.
      ctypes.c_char_p: DataEngine().GetAttributeValueString,
      datetime.datetime: DataEngine().GetAttributeValueDateTime,
      datetime.date: DataEngine().GetAttributeValueDate,
    }

    function = type_to_function.get(dtype)
    if function is None:
      raise ValueError(
        f'The type of the attribute ({dtype}) is an unsupported type.')

    value: typing.Any
    if dtype is datetime.datetime:
      # Convert timestamp from the project to a datetime object.
      c_value = ctypes.c_int64()
      got_result = function(
        self._lock.lock, attribute_id, ctypes.byref(c_value))
      value = datetime.datetime.fromtimestamp(c_value.value / 1000000,
                                              datetime.timezone.utc)
      value = value.replace(tzinfo=None)  # Remove timezone awareness.
    elif dtype is datetime.date:
      # Convert date tuple from the project to a date object.
      year = ctypes.c_int32()
      month = ctypes.c_uint8()
      day = ctypes.c_uint8()
      got_result = function(
        self._lock.lock,
        attribute_id,
        ctypes.byref(year),
        ctypes.byref(month),
        ctypes.byref(day)
        )
      value = datetime.date(year.value, month.value, day.value)
    elif dtype is ctypes.c_char_p:
      # Get attribute value as text string
      value_sz = function(self._lock.lock, attribute_id, None, 0)

      # Create string buffer to hold path
      value_buffer = ctypes.create_string_buffer(value_sz)
      got_result = function(self._lock.lock, attribute_id, value_buffer,
                            value_sz)
      value = value_buffer.value.decode("utf-8")
    else:
      # Define a value of the given type.
      # mypy cannot determine that dtype cannot possibly be None, date or
      # datetime in this branch so ignore type checking.
      value = dtype() # type: ignore
      got_result = function(self._lock.lock, attribute_id, ctypes.byref(value))
      value = value.value

    if not got_result:
      raise KeyError(f"Object attribute: {attribute_id} does not exist.")

    return value

class Topology(DataObject):
  """Base class for "geometric objects" in a Project.

  This object is best thought of as the union of the following:

    - An arrangement of topological "primitives" including their location in
      space (known as their geometry).
    - The connectivity relationships between them (known as their topology).
    - The properties applied to them.

  A given geometric object may contain any number of any of the six basic
  primitives: points, edges, facets (triangles), tetras (4 sided polyhedra),
  cells (quadrilaterals) and blocks (cubes or rectangular boxes).
  However, derived classes typically enforce constraints on the type and number
  of each primitive allowed in objects of their type. For example an edge
  chain will have points and edges but not facets.
  """
  def __init__(self, object_id: ObjectID, lock_type: LockType, *,
               rollback_on_error: bool = False):
    super().__init__(
      object_id,
      lock_type,
      rollback_on_error=rollback_on_error)
    self.__extent: SingularDataPropertyReadOnly[
        Extent] = SingularDataPropertyReadOnly(
      "extent",
      lambda: [self._lock.lock],
      self.__load_extent
    )
    self.__colour_map_information: SingularDataPropertyReadWrite[
      ColourMapInformation] = SingularDataPropertyReadWrite(
        "colour_map",
        lambda: [self._lock.lock],
        self.is_read_only,
        # The partial function allows the setter to accept an extra
        # argument compared to the getter.
        self.__get_colour_map_information,
        functools.partial(
          self.__save_colour_map_information,
          reconcile_changes=self._reconcile_changes)
        )
    self.__coordinate_system: SingularDataPropertyReadWrite[
        CoordinateSystem | typing.Literal["NO_COORDINATE_SYSTEM"]
        ] = SingularDataPropertyReadWrite(
      name="coordinate_system",
      load_parameters=lambda: [self._lock.lock],
      read_only=self.is_read_only,
      load_function=self.__load_coordinate_system,
      save_function=self.__save_coordinate_system
    )

  def close(self):
    """Closes the object and saves the changes to the Project.

    Attempting to read or edit properties of an object after closing it will
    raise a ReadOnlyError.
    """
    self._invalidate_properties()
    DataObject.close(self)

  def cancel(self):
    """Cancel any pending changes to the object.

    This undoes all changes made to the object since it was opened
    (including any changes saved by save()) and then closes the object.

    After this is called, attempting to read or edit any of the properties
    on this object (other than the id) will raise an ObjectClosedError.

    Raises
    ------
    ReadOnlyError
      If the object was open for read only (i.e not for editing).
      It is not necessary to call this for a read only object as there will be
      no pending changes.
    ObjectClosedError
      If called on a closed object.
    """
    self._raise_if_read_only("cancel changes")

    assert isinstance(self._lock, WriteLock)
    self._lock.cancel()
    self._lock.close()
    self._invalidate_properties()

  @classmethod
  def static_type(cls):
    """Return the type of a topology as stored in a Project.

    This can be used for determining if the type of an object is topology.
    """
    return Modelling().TopologyType()

  def _extra_invalidate_properties(self):
    self.__colour_map_information.invalidate()
    self.__coordinate_system.invalidate()
    self._invalidate_colour_map()

  def _save_topology(self):
    """Save the topology of the object.

    This should save any properties defined on the implementing
    child class. This is called during _save(), which in turn is called
    during save().
    """
    raise NotImplementedError

  # Child classes of topology should implement _save_topology()
  # instead of overwriting or overriding _save_topology().
  @final
  def _save(self):
    self._save_topology()
    self.__coordinate_system.save()
    # :TRICKY: Saving the colour map information must be done after saving
    # all of the topology because it may require a call to reconcile changes,
    # which could discard unsaved changes (e.g. If the colour map was saved
    # with the primitive attributes, then for Surfaces it would result in a
    # call to reconcile changes between saving the points and facets,
    # resulting in new facets and points being discarded).
    self.__colour_map_information.save()
    self._reconcile_changes()

  def _reconcile_changes(self):
    """Request reconciliation of flagged changes.

    All properties need to be re-loaded after calling.
    """
    try:
      Modelling().ReconcileChanges(self._lock.lock)
    except:
      log.exception("Unexpected error when trying to save changes.")
      raise

  @property
  def extent(self) -> Extent:
    """The axes aligned bounding extent of the object."""
    return self.__extent.value

  def get_colour_map(self) -> ObjectID[ColourMap]:
    """Return the ID of the colour map object associated with this object.

    Returns
    -------
    ObjectID
      The ID of the colour map object or null object ID if there is
      no colour map.
    """
    return self.__colour_map_information.value.colour_map_id

  def _set_colour_map(
      self,
      attribute_key: AttributeKey,
      primitive_type: PrimitiveType,
      colour_map: ObjectID[ColourMap]):
    """Set the colour map for this object.

    This allows for derived classes and PrimitiveAttributes to set the
    colour map information.

    Parameters
    ----------
    attribute_name
      The name of the attribute to associate to the colour map.
    primitive_type
      The type of primitive the attribute has values for.
    colour_map
      The ObjectID of the colour map to use to colour by the attribute.

    Warnings
    --------
    This performs no safety checks. The caller is expected to perform
    such checks.
    """
    map_information =  ColourMapInformation.from_attribute_key(
      attribute_key,
      primitive_type,
      colour_map
    )
    self.__colour_map_information.value = map_information

  def _colour_map_information(self) -> ColourMapInformation:
    """Get the colour map information for this object.

    This allows for derived classes and PrimitiveAttributes to access the
    colour map information.

    Returns
    -------
    ColourMapInformation
      A named tuple containing the colour map information for this object.
      This will contain a null Object ID if there is no colour map
      associated with the object.
    """
    return self.__colour_map_information.value

  def _invalidate_colour_map(self):
    """Invalidates the colour map.

    It is loaded from the Project the next time it is accessed.
    """
    self.__colour_map_information.invalidate()

  def _associate_raster(self, raster_id: ObjectID[Raster], desired_index: int):
    """Associate a raster with this object.

    This should not be called directly.

    Parameters
    ----------
    raster_id
      Object ID of the raster to associate.
    desired_index
      The index to associate the raster at.

    Raises
    ------
    RuntimeError
      If the raster could not be associated with the object.
    TypeError
      If raster_id is not the ObjectID of a raster.
    AlreadyAssociatedError
      If the raster is already associated with an object.
    NonOrphanRasterError
      If the raster is not an orphan.
    """
    if not raster_id.is_a(Modelling().ImageType()):
      raise TypeError(f"Cannot associate Raster of type {raster_id.type_name} "
                     "because it is not a Raster.")
    desired_index = int(desired_index)
    if desired_index < 1 or desired_index > 255:
      message = (f"Invalid raster index ({desired_index}). Raster index must "
                 "be greater than 0 and less than 255.")
      raise ValueError(message)
    if raster_id in self.rasters.values():
      message = (
        "The Raster is already associated with this Surface. To edit "
        "the registration information, edit the registration property "
        "of the Raster directly. To change the raster index, the "
        "raster must be dissociated via dissociate_raster() "
        "before calling this function.")
      raise AlreadyAssociatedError(message)
    if not raster_id.is_orphan:
      # :TRICKY: 2021-09-27 SDK-542. AssociateRaster will
      # make a clone of the Raster if it is not an orphan. This won't clone
      # the registration information, resulting in the clone being
      # associated with the Surface with no registration information.
      # Raise an error to avoid this.
      # Note that if a Raster is created with a path in project.new
      # then it is an orphan until the object is closed and no error will
      # be raised.
      parent_id = raster_id.parent
      # Use the C API functions to avoid a circular dependency with
      # containers.py.
      if parent_id.is_a((
          Modelling().VisualContainerType(),
          Modelling().StandardContainerType())):
        raise NonOrphanRasterError(
          "Cannot associate a raster with a Project path. "
          "Call Project.copy_object() with a destination path of None and "
          "associate the copy instead.")
      raise AlreadyAssociatedError(
        "Cannot associate Raster because it is already associated with the "
        f"{parent_id.type_name} with path: '{parent_id.path}'. "
        "To associate the Raster with this object, first dissociate it from "
        "the other object and close the other object before calling this "
        "function. Alternatively create a copy by calling "
        "Project.copy_object() with a destination path of None.")
    result = Modelling().AssociateRaster(self._lock.lock,
                                         raster_id.handle,
                                         desired_index)
    result = result.value
    if result == 0:
      raise RuntimeError("Failed to associate raster.")
    return result

  @property
  def rasters(self) -> dict[int, ObjectID[Raster]]:
    """The raster associated with this object.

    This is a dictionary of raster indices and Object IDs of the raster images
    currently associated with this object.

    The keys are the raster ids and the values are the Object IDs of the
    associated rasters. Note that all raster ids are integers however they
    may not be consecutive - for example, an object may have raster ids
    0, 1, 5 and 200.

    Notes
    -----
    Rasters with higher indices appear on top of rasters with lower indices.
    The maximum possible raster id is 255.

    Removing a raster from this dictionary will not remove the raster
    association from the object. Use dissociate_raster to do this.

    Examples
    --------
    Iterate over all rasters on an object and invert the colours. Note
    that this will fail if there is no object at the path "target" and
    it will do nothing if no rasters are associated with the target.

    >>> from mapteksdk.project import Project
    >>> project = Project()
    >>> with project.read("target") as read_object:
    ...     for raster in read_object.rasters.values():
    ...         with project.edit(raster) as edit_raster:
    ...             edit_raster.pixels[:, :3] = 255 - edit_raster.pixels[:, :3]
    """
    rasters = Modelling().GetAssociatedRasters(self._lock.lock)
    final_rasters: dict[int, ObjectID[Raster]] = {}
    for key, value in rasters.items():
      final_rasters[key] = ObjectID(value)
    return final_rasters

  def dissociate_raster(self, raster: Raster | ObjectID[Raster]):
    """Removes the raster from the object.

    If an error occurs after dissociating a raster resulting in save()
    not being called, the dissociation of the raster can only be undone if
    the application's API version is 1.6 or greater.

    Prior to mapteksdk 1.6:
    Dissociating a raster will not be undone if an error occurs.

    Parameters
    ----------
    raster
      The raster to dissociate.

    Returns
    -------
    bool
      True if the raster was successfully dissociated from the object,
      False if the raster was not associated with the object.

    Raises
    ------
    TypeError
      If raster is not a Raster.
    ReadOnlyError
      If this object is open for read-only.

    Notes
    -----
    This only removes the association between the Raster and the object,
    it does not clear the registration information from the Raster.

    Examples
    --------
    Dissociate the first raster found on a picked object.

    >>> from mapteksdk.project import Project
    >>> from mapteksdk import operations
    >>> project = Project()
    >>> oid = operations.object_pick(
    ...     support_label="Pick an object to remove a raster from.")
    ... with project.edit(oid) as data_object:
    ...     report = f"There were no raster to remove from {oid.path}"
    ...     for index in data_object.rasters:
    ...         data_object.dissociate_raster(data_object.rasters[index])
    ...         report = f"Removed raster {index} from {oid.path}"
    ...         break
    ... # Now that the raster is dissociated and the object is closed,
    ... # the raster can be associated with a different object.
    ... operations.write_report("Remove Raster", report)
    """
    self._raise_if_read_only("dissociate raster")

    # :TODO: 2021-04-16 SDK-471: It might be useful to cache this information
    # and do it during save.
    if not isinstance(raster, ObjectID):
      try:
        raster = raster.id
      except AttributeError as error:
        raise TypeError("raster must be a ObjectID or DataObject, "
                        f"not '{raster}' of type {type(raster)}.") from error

    # :NOTE: 2021-04-16 We can't call Raster.static_type() because importing
    # images.py into this file would result in a circular dependency.
    if not raster.is_a(Modelling().ImageType()):
      raise TypeError('raster must be an object of type Raster.')

    return Modelling().DissociateRaster(self._lock.lock, raster.handle)

  @property
  def coordinate_system(self) -> CoordinateSystem | None:
    """The coordinate system the points of this object are in.

    If the object has no coordinate system, this will be None.

    Raises
    ------
    ReadOnlyError
      If set on an object open for read-only.

    Warning
    -------
    Setting this property does not change the points.
    This is only a label stating the coordinate system the points are in.

    Examples
    --------
    Creating an edge network and setting the coordinate system to be
    WGS84. Note that setting the coordinate system does not change the points.
    It is only stating which coordinate system the points are in.

    >>> from pyproj import CRS
    >>> from mapteksdk.project import Project
    >>> from mapteksdk.data import Polygon
    >>> project = Project()
    >>> with project.new("cad/rectangle", Polygon) as new_edges:
    ...     # Coordinates are in the form [longitude, latitude]
    ...     new_edges.points = [[112, 9], [112, 44], [154, 44], [154, 9]]
    ...     new_edges.coordinate_system = CRS.from_epsg(4326)

    Often a standard map projection is not convenient or accurate for
    a given application. In such cases a local transform can be provided
    to allow coordinates to be specified in a more convenient system.
    The below example defines a local transform where the origin is
    translated 1.2 degrees north and 2.1 degree east, points are scaled to be
    twice as far from the horizontal origin and the coordinates are rotated
    45 degrees clockwise about the horizontal_origin. Note that the points
    of the polygon are specified in the coordinate system after the local
    transform has been applied.

    >>> import math
    >>> from pyproj import CRS
    >>> from mapteksdk.project import Project
    >>> from mapteksdk.data import Polygon, CoordinateSystem, LocalTransform
    >>> project = Project()
    >>> transform = LocalTransform(
    ...     horizontal_origin = [1.2, 2.1],
    ...     horizontal_scale_factor = 2,
    ...     horizontal_rotation = math.pi / 4)
    >>> system = CoordinateSystem(CRS.from_epsg(20249), transform)
    >>> with project.new("cad/rectangle_transform", Polygon) as new_edges:
    ...     new_edges.points = [[112, 9], [112, 44], [154, 44], [154, 9]]
    ...     new_edges.coordinate_system = system

    See Also
    --------
    mapteksdk.data.coordinate_systems.CoordinateSystem : Allows for a
      coordinate system to be defined with an optional local transform.
    """
    # This returns None for no coordinate system for backwards
    # compatibility.
    if self.__coordinate_system.value == _NO_COORDINATE_SYSTEM:
      return None
    return self.__coordinate_system.value

  @coordinate_system.setter
  def coordinate_system(self, value: CoordinateSystem | None):
    if value is None:
      # This handles the case where a user does:
      # left_object.coordinate_system = right_object.coordinate_system
      # when right_object doesn't have a coordinate system.
      self.remove_coordinate_system()
      return

    if not isinstance(value, CoordinateSystem):
      value = CoordinateSystem(value)
    self.__coordinate_system.value = value

  def remove_coordinate_system(self):
    """Remove the coordinate system from the object.

    This does not change the geometry of the object. It only clears
    the label which states what coordinate system the object is in.

    This has no effect if the object does not have a coordinate system.
    """
    self._raise_if_read_only("Remove coordinate system.")
    self.__coordinate_system.value = _NO_COORDINATE_SYSTEM

  @staticmethod
  def __get_colour_map_information(lock) -> ColourMapInformation:
    """Get the colour map information for an object.

    Parameters
    ----------
    lock
      Lock on the object to get the colour map information for.

    Returns
    -------
    ColourMapInformation
      The colour map information for this object.
      If there is no colour map associated with this object,
      this will contain a null ObjectID.
    """
    read_type = Modelling().GetDisplayedAttributeType(lock)

    try:
      actual_type = PrimitiveType(read_type)
    except ValueError:
      return ColourMapInformation.no_colour_map(
        PrimitiveType.POINT)

    length = Modelling().GetDisplayedAttribute(
      lock,
      None,
      0)
    str_buffer = ctypes.create_string_buffer(length)
    Modelling().GetDisplayedAttribute(
      lock,
      str_buffer,
      length)

    name = str_buffer.value.decode("utf-8")

    if not name:
      return ColourMapInformation.no_colour_map(actual_type)

    colour_map_handle = Modelling().GetDisplayedColourMap(lock)
    colour_map_id = ObjectID(colour_map_handle)

    return ColourMapInformation.from_name(
      name, actual_type, colour_map_id
    )

  @staticmethod
  def __save_colour_map_information(
      lock,
      colour_map_info: ColourMapInformation,
      reconcile_changes: typing.Callable[[], None]):
    """Save the colour map information for an object.

    This does nothing if the colour map information contains a null
    object ID.

    This includes an implicit call to _reconcile_changes() to ensure
    the colour map is saved correctly.

    Parameters
    ----------
    lock
      Lock on the object to save the colour map for.
    colour_map_info
      Colour map information to save for this object.
    """
    if not colour_map_info.colour_map_id:
      # There is no colour map information to save.
      return
    if not colour_map_info.attribute_key:
      # The AttributeKey was never looked up, so it must not have been edited.
      return
    # If you set the colour map and colours at the same time, the
    # colour map is not set. To avoid this, reconcile changes before
    # saving the colour map.
    reconcile_changes()

    save_functions = {
      PrimitiveType.POINT : Modelling().SetDisplayedPointAttribute,
      PrimitiveType.EDGE : Modelling().SetDisplayedEdgeAttribute,
      PrimitiveType.FACET : Modelling().SetDisplayedFacetAttribute,
      PrimitiveType.BLOCK : Modelling().SetDisplayedBlockAttribute,
      PrimitiveType.CELL : Modelling().SetDisplayedBlockAttribute
    }

    save_function = save_functions[colour_map_info.primitive_type]
    save_function(
      lock,
      colour_map_info.attribute_key.to_json().encode("utf-8"),
      colour_map_info.colour_map_id.handle
    )

  @staticmethod
  def __load_extent(lock) -> Extent:
    """Load the extent of the object from the Project.

    Parameters
    ----------
    lock
      Lock on the object to load the extent of.

    Returns
    -------
    Extent
      The Extent of the object.
    """
    extents = (ctypes.c_double * 6)()
    Modelling().ReadExtent(lock, extents)
    return Extent(
      minimum=(extents[0], extents[1], extents[2]),
      maximum=(extents[3], extents[4], extents[5]))

  @staticmethod
  def __load_coordinate_system(lock
      ) -> CoordinateSystem | typing.Literal["NO_COORDINATE_SYSTEM"]:
    """Load the coordinate system information from the application.

    Returns
    -------
    CoordinateSystem
      The coordinate system information for this object.
    """
    wkt, c_local_transform = Modelling().GetCoordinateSystem(lock)
    if wkt != "":
      local_transform = np.empty((11,), dtype=ctypes.c_double)
      local_transform[:] = c_local_transform
      return CoordinateSystem(wkt, LocalTransform(local_transform))
    return _NO_COORDINATE_SYSTEM

  @staticmethod
  def __save_coordinate_system(
      lock,
      coordinate_system: CoordinateSystem | typing.Literal[
        "NO_COORDINATE_SYSTEM"]):
    """Save the coordinate system information to the application.

    Parameters
    ----------
    lock
      Lock on the object to save the coordinate system information.
    coordinate_system
      The coordinate system to save for the object.
      If this is NO_COORDINATE_SYSTEM, this clears the coordinate system.
    """
    if coordinate_system == _NO_COORDINATE_SYSTEM:
      try:
        Modelling().ClearCoordinateSystem(lock)
      except (CApiFunctionNotSupportedError, AttributeError):
        # Clear coordinate system is not supported by the C API.
        # If this object currently doesn't have a coordinate system,
        # suppress the error - the object is in the correct state.
        # This case will be hit if the script reads that there is no
        # coordinate system but doesn't set a coordinate system.
        if Topology.__load_coordinate_system(lock) != _NO_COORDINATE_SYSTEM:
          raise
      return
    wkt_string = coordinate_system.crs.to_wkt(WktVersion.WKT2_2019)
    local_transform = coordinate_system.local_transform.to_numpy()

    Modelling().SetCoordinateSystem(lock,
                                    wkt_string,
                                    local_transform)

  # =========================================================================
  #
  #                      TEXT / ANNOTATION SUPPORT
  #
  # =========================================================================
  def _get_text(self) -> str:
    """Get text string.

    Returns
    -------
    str
      Annotation text string.

    Notes
    -----
    C API: Supports marker text and 2d text.
    """
    buf_size = Modelling().GetAnnotationText(self._lock.lock, None, 0)
    str_buf = ctypes.create_string_buffer(buf_size)
    Modelling().GetAnnotationText(self._lock.lock, str_buf, buf_size)
    text = str_buf.value.decode("utf-8")
    return text

  def _get_text_size(self) -> float:
    """Get text size.

    Returns
    -------
    Double
      Text size.

    Notes
    -----
    C API: Supports marker text and 2d text.
    """
    return Modelling().GetAnnotationSize(self._lock.lock)

  def _get_text_colour(self) -> list[int]:
    """Get text colour.

    Returns
    -------
    array
      1D array of [R,G,B,A] uint8.

    Notes
    -----
      C API: Support marker text and 2d text.
    """
    col = (ctypes.c_uint8*4)
    buffer = col()
    Modelling().GetAnnotationTextColour(self._lock.lock,
                                        ctypes.byref(buffer))
    return [buffer[0], buffer[1], buffer[2], buffer[3]]

  def _save_annotation_text(self, text: str):
    """Save text for Marker or 2DText annotations.

    Parameters
    ----------
    text
      Text to write to the annotation object.
    """
    if text is not None:
      Modelling().SetAnnotationText(self._lock.lock, text.encode("utf-8"))

  def _save_annotation_text_size(self, text_size: float):
    """Save text for Marker or 2DText annotations.

    Parameters
    ----------
    text_size
      Text size to write to the annotation object.
    """
    if text_size is not None:
      Modelling().SetAnnotationSize(self._lock.lock, text_size)

  def _save_annotation_text_colour(self, text_colour: np.ndarray):
    """Save text for Marker or 2DText annotations.

    Parameters
    ----------
    text_colour
      [r,g,b,a] 1D array of uint8.
    """
    if text_colour is not None:
      rgba_colour = (ctypes.c_uint8 * len(text_colour))\
        (*text_colour.astype(ctypes.c_uint8))
      # .astype is used in case padding accidentally added new data as floats
      Modelling().SetAnnotationTextColour(self._lock.lock, rgba_colour)
