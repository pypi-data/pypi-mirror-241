"""File containing assertions designed for DataObject subclasses."""
###############################################################################
#
# (C) Copyright 2023, Maptek Pty Ltd. All rights reserved.
#
###############################################################################
from __future__ import annotations

import itertools
import typing

import numpy as np

from mapteksdk.data import ObjectID, DataObject, Container
from mapteksdk.data.errors import ReadOnlyError
from mapteksdk.internal.lock import ObjectClosedError
from mapteksdk.project import Project

DataObjectSubclass = typing.TypeVar("DataObjectSubclass", bound=DataObject)
"""Type for a parameter which must be a subclass of DataObject."""
T = typing.TypeVar("T")
"""Type for a parameter which can be any type."""
_PATH_COUNTER =itertools.count()
"""Counter used to generate the next path."""

def next_path() -> str:
  """Return a path for an object.

  This will not return the same path more than once within a single
  script.

  Returns
  -------
  str
    A valid path.
  """
  return f"object_{next(_PATH_COUNTER)}"

def default_setup_function(_: DataObject):
  """Default setup function.

  This does nothing.
  """


class PropertyTestTuple(typing.NamedTuple):
  """Named tuple containing functions required to test a property."""
  object_type: typing.Callable[
    [], DataObjectSubclass | type[DataObjectSubclass]]
  """Function which returns the type of the object to create.

  This is a function to support either giving the type:

  >>> object_type=lambda: Scan

  Or an instance of the type:

  >>> object_type=lambda: Scan(dimensions=(3, 3))

  Returns
  -------
  DataObject | type[DataObject]
    The created object or the type of the object to create.
  """
  edit_property: typing.Callable[[DataObjectSubclass, T], None]
  """Function for editing the property on the object to test.

  Parameters
  ----------
  data_object
    Open DataObject subclass to set the property for.
  value
    Value to assign to the property.
  """
  read_property: typing.Callable[[DataObjectSubclass], T]
  """Function for reading the property on the object to test.

  Parameters
  ----------
  data_object
    Open DataObject subclass to read the property from.

  Returns
  -------
  T
    The value read from the property.
  """
  assert_equal: typing.Callable[[T, T], None]
  """Function to assert if the property values are equal.

  Parameters
  ----------
  first
    The first value to check if they are equal.
  second
    The second value to check if they are equal.

  Raises
  ------
  AssertionError
    If the two properties are not equal.
  """
  default: typing.Any
  """Expected default value for the property.

  When the object is created, the array is expected to be
  filled with the default value.
  """
  setup_function: typing.Callable[
    [DataObjectSubclass], None] = default_setup_function
  """Function which sets up a newly created object.

  This must assign any properties which are required for the object to
  be saved.

  Parameters
  ----------
  data_object
    DataObject subclass to setup.

  Notes
  -----
  By default, this is a function which doesn't do anything.
  """


def assert_property_can_be_set_in_new(
    project: Project,
    parameters: PropertyTestTuple[DataObjectSubclass, T],
    expected_value: T):
  """Assert that the property's value can be set on a new object.

  Parameters
  ----------
  project
    Project to use to open the object.
  parameters
    Parameters to use to create the object and edit/read the property.
  expected_value
    The value to assign to the property.
  """
  with project.new(next_path(), parameters.object_type()) as new_object:
    oid: ObjectID[DataObjectSubclass] = new_object.id # type: ignore
    parameters.setup_function(new_object)
    parameters.edit_property(new_object, expected_value)
    parameters.assert_equal(
      parameters.read_property(new_object),
      expected_value)

  with project.read(oid) as read_object:
    parameters.assert_equal(
      parameters.read_property(read_object),
      expected_value)


def assert_property_can_be_edited(
    project: Project,
    parameters: PropertyTestTuple[DataObjectSubclass, T],
    original_value: T,
    expected_value: T):
  """Assert that the property's value can be edited once set.

  Essentially, this sets the property to `original_value` and then
  tests that it can then be edited to `expected_value`.

  Parameters
  ----------
  project
    Project to use to open the object.
  parameters
    Parameters to use to create the object and edit/read the property.
  original_value
    A valid value to assign to the property.
  expected_value
    Another valid value to assign to the property.
  """
  with project.new(next_path(), parameters.object_type()) as new_object:
    oid: ObjectID[DataObjectSubclass] = new_object.id # type: ignore
    parameters.setup_function(new_object)
    parameters.edit_property(new_object, original_value)

  with project.edit(oid) as edit_object:
    parameters.edit_property(edit_object, expected_value)
    parameters.assert_equal(
      parameters.read_property(edit_object),
      expected_value)

  with project.read(oid) as read_object:
    parameters.assert_equal(
      parameters.read_property(read_object),
      expected_value)


def assert_array_property_supports_broadcast(
    project: Project,
    parameters: PropertyTestTuple[DataObjectSubclass, typing.Sequence[T]],
    single_value: T):
  """Assert that an array property supports NumPy broadcasting.

  This tests some non-standard behaviour of the SDK, for example:

  >>> surface.point_colours = [255, 0, 0, 255]

  Will make all of the point colours red (Normally, this would raise
  an error and to broadcast would require [:] after point_colours).

  Parameters
  ----------
  project
    Project to use to create objects.
  parameters
    Parameters to use to create the object and read /edit the property
    under test.
  single_value
    A single value to broadcast the array to.
  """
  # As this behaviour is non-standard, the type checker cannot handle it.
  with project.new(next_path(), parameters.object_type()) as new_object:
    parameters.setup_function(new_object)
    parameters.edit_property(new_object, single_value) # type:ignore
    for item in parameters.read_property(new_object):
      parameters.assert_equal(item, single_value) # type: ignore

  with project.read(new_object.id) as read_object:
    for item in parameters.read_property(read_object):
      parameters.assert_equal(item, single_value) # type: ignore


def assert_cannot_edit_read_only_property(
    project: Project,
    parameters: PropertyTestTuple[DataObjectSubclass, T],
    assert_raises: typing.Callable[
      [type[Exception]], typing.ContextManager],
    default_value: T,
    new_value: T):
  """Assert that the property cannot be edited on a read-only object.

  This sets the property to `default_value` and then checks that:
  1: When the object is open for reading, it cannot set the property
     to `new_value`.
  2: That the property value is still `default_value` after that error
     has occurred.

  Parameters
  ----------
  project
    Project to use to open the object.
  parameters
    Parameters to use to create the object and read the property.
  default_value
    A valid value for the property.
  new_value
    A valid value for the property which is not the same as default_value.
  """
  with project.new(next_path(), parameters.object_type()) as new_object:
    oid: ObjectID[DataObjectSubclass] = new_object.id # type: ignore
    parameters.setup_function(new_object)
    parameters.edit_property(new_object, default_value)

  with assert_raises(ReadOnlyError):
    with project.read(oid) as read_object:
      parameters.edit_property(read_object, new_value)

  with project.read(oid) as final_object:
    parameters.assert_equal(
      parameters.read_property(final_object),
      default_value
    )

def assert_cannot_read_property_after_close(
    project: Project,
    parameters: PropertyTestTuple[DataObjectSubclass, T],
    assert_raises: typing.Callable[
      [type[Exception]], typing.ContextManager],
    default_value: T):
  """Asserts that a property cannot be read after the object is closed."""
  with project.new(next_path(), parameters.object_type()) as new_object:
    parameters.setup_function(new_object)
    parameters.edit_property(new_object, default_value)

  with assert_raises(ObjectClosedError):
    parameters.read_property(new_object)

  with project.read(new_object.id) as read_object:
    parameters.assert_equal(
      parameters.read_property(read_object),
      default_value
    )

def assert_cannot_edit_property_after_close(
    project: Project,
    parameters: PropertyTestTuple[DataObjectSubclass, T],
    assert_raises: typing.Callable[
      [type[Exception]], typing.ContextManager],
    default_value: T,
    new_value: T):
  """Asserts that a property cannot be edited after the object is closed."""
  with project.new(next_path(), parameters.object_type()) as new_object:
    parameters.setup_function(new_object)
    parameters.edit_property(new_object, default_value)

  with assert_raises(ObjectClosedError):
    parameters.edit_property(new_object, new_value)

  with project.read(new_object.id) as read_object:
    parameters.assert_equal(
      parameters.read_property(read_object),
      default_value
    )

def assert_set_property_to_bad_value(
    project: Project,
    parameters: PropertyTestTuple[DataObjectSubclass, T],
    assert_raises: typing.Callable[
      [type[Exception]], typing.ContextManager],
    good_value: T,
    bad_value: typing.Any,
    expected_exception: type[Exception]
    ):
  """Tests that an error is raised when providing a bad value.

  This also tests that the current value of the property is not
  changed by the error.

  Parameters
  ----------
  project
    Project to create the object in.
  parameters
    Parameters to use to create the object and edit/read the property.
  assert_raises
    Function which returns a context manager which will raise an
    AssertionError if an exception is not raised.
  good_value
    A valid value for the property. This is used to detect that the
    property is not changed when an error occurs.
  bad_value
    A value which the property should raise an error if it is assigned to.
  expected_exception
    The exception expected to be raised.
  """
  with project.new(next_path(), parameters.object_type()) as new_object:
    oid: ObjectID[DataObjectSubclass] = new_object.id # type: ignore
    parameters.setup_function(new_object)
    parameters.edit_property(new_object, good_value)

  with project.edit(oid) as bad_object:
    with assert_raises(expected_exception):
      parameters.edit_property(bad_object, bad_value)
    # Make sure the property wasn't edited when an error occurred.
    parameters.assert_equal(
      parameters.read_property(bad_object),
      good_value
    )

  with project.read(oid) as read_object:
    # The property should not have been edited after closing
    # and re-opening the object.
    parameters.assert_equal(
      parameters.read_property(read_object),
      good_value
    )

def assert_resize_primary_resizes_secondary(
    project: Project,
    parameters: PropertyTestTuple[DataObjectSubclass, T],
    resize_primary_property: typing.Callable[[DataObjectSubclass], None],
    original_value: T,
    expected_value: T,
    ):
  """Assert that resizing the primary property expands the secondary property.

  For example, this could be used to assert that when points are added/removed
  to/from a point set, the point colours array expands/shrinks.

  Parameters
  ----------
  project
    The Project to use to create, edit and read objects.
  parameters
    ProjectTestTuple for reading and editing the property under test.
  resize_primary_property
    A function which accepts the object open for editing. It must
    change the length of the primary property array.
  original_value
    The original value to assign to the property.
  expected_value
    The expected value after resize_primary_property() has been called.
  """
  with project.new(next_path(), parameters.object_type()) as new_object:
    oid: ObjectID[DataObjectSubclass] = new_object.id # type: ignore
    parameters.setup_function(new_object)
    parameters.edit_property(new_object, original_value)

  with project.edit(oid) as edit_object:
    resize_primary_property(edit_object)
    parameters.assert_equal(
      parameters.read_property(edit_object),
      expected_value
    )

  with project.read(oid) as read_object:
    parameters.assert_equal(
      parameters.read_property(read_object),
      expected_value
    )

def assert_create_object(
    project: Project,
    object_type: typing.Callable[
      [], DataObjectSubclass | type[DataObjectSubclass]],
    setup_function: typing.Callable[[DataObjectSubclass], None],
    verify_function: typing.Callable[[DataObjectSubclass], None]):
  """Assert that running the setup function puts the object in a valid state.

  This:
  * Creates an object of the specified type.
  * Runs the setup function on it.
  * Runs the verify function.
  * Closes the object.
  * Opens the object for reading.
  * Runs the verification function again.

  Parameters
  ----------
  project
    Project to use to create objects.
  object_type
    The type of object to create.
  setup_function
    Function to run on the newly created object. The test will fail if
    this does not place the object into a valid, savable state.
  verify_function
    Function which verifies that the created object is in the expected state
    after the setup function was run.

  """
  with project.new(next_path(), object_type()) as new_object:
    setup_function(new_object)
    verify_function(new_object)

  with project.read(new_object.id) as read_object:
    verify_function(read_object)

def assert_edit_object(
    project: Project,
    object_type: typing.Callable[
      [], DataObjectSubclass | type[DataObjectSubclass]],
    setup_function: typing.Callable[[DataObjectSubclass], None],
    edit_function: typing.Callable[[DataObjectSubclass], None],
    verify_function: typing.Callable[[DataObjectSubclass], None]):
  """Assert that editing the object places it in a specific state.

  Parameters
  ----------
  project
    Project to use to create objects.
  object_type
    Function which returns the type of object to create, or an instance
    of the object to create.
  setup_function
    Function to setup the state of the object. This should place the object
    in a valid, savable state.
  edit_function
    Function which edits the object to place it in the desired state.
  verify_function
    Function which verifies that the object was placed into the desired
    state.
  """
  with project.new(next_path(), object_type()) as new_object:
    setup_function(new_object)

  with project.edit(new_object.id) as edit_object:
    edit_function(edit_object)
    verify_function(edit_object)

  with project.read(new_object.id) as read_object:
    verify_function(read_object)

def assert_function_raises_error(
    project: Project,
    object_type: typing.Callable[
      [], DataObjectSubclass | type[DataObjectSubclass]],
    expected_error: type[Exception],
    setup_function: typing.Callable[[DataObjectSubclass], None],
    error_function: typing.Callable[[DataObjectSubclass], None],
    verify_function: typing.Callable[[DataObjectSubclass], None],
    assert_raises: typing.Callable[
      [type[Exception]], typing.ContextManager]):
  """Assert that calling error_function on the DataObject raises an error.

  Parameters
  ----------
  project
    Project to use to create, read and edit objects.
  object_type
    The type of object to create.
  expected_error
    Exception expected to be raised.
  setup_function
    Function which sets up the object.
  error_function
    Function which is expected to raise an error.
  verify_function
    Function which verifies that the object is unchanged.
  """
  with project.new(next_path(), object_type()) as new_object:
    setup_function(new_object)

  with project.edit(new_object.id) as edit_object:
    with assert_raises(expected_error):
      error_function(edit_object)
    verify_function(edit_object)

  with project.read(new_object.id) as read_object:
    verify_function(read_object)


def assert_masked_array_equal(x: np.ma.MaskedArray, y: np.ma.MaskedArray):
  """Asserts that two masked arrays have equal values and masks.

  Parameters
  ----------
  x : np.ma.MaskedArray
    The first masked array.
  y : np.ma.MaskedArray
    The second masked array.
  """
  np.testing.assert_array_equal(
    x.mask, y.mask, err_msg="Masks were not equal.")
  if x.dtype.kind in ("U", "S") or y.dtype.kind in ("U", "S"):
    np.testing.assert_array_equal(
      x, y, err_msg="Values were not equal.")
  else:
    np.testing.assert_array_almost_equal(
      x, y, err_msg="Values were not equal.")

def assert_two_surfaces_equal_basic(project, actual_surface, expected_surface):
  """Asserts that the points and facets of the two surfaces are equal.

  Parameters
  ----------
  actual_surface : ObjectID
      The actual surface to check.
  equal : ObjectID
      The expected surface to check against.

  Raises
  ------
  AssertionError
    If actual and expected objects are not equal.
  """
  with project.read(actual_surface) as actual:
    with project.read(expected_surface) as expected:
      np.testing.assert_array_equal(actual.points, expected.points)
      np.testing.assert_array_equal(actual.facets, expected.facets)

def assert_container_children(
    project: Project,
    container_path_or_id: str | ObjectID[Container],
    children: typing.Sequence[typing.Tuple[str, ObjectID]]):
  """Assert that the container contains the given children.

  Parameters
  ----------
  container
    Path to the container or the ObjectID of the container to check the
    children of.
  children
    An iterable of tuples containing the name of the expected child
    and its ObjectID.
  """
  with project.edit(container_path_or_id) as container:
    assert isinstance(container, Container)
    if len(container) != len(children):
      raise AssertionError(
        f"Expected {len(children)} items in container, but there were "
        f"{len(container)} items.")
    for i, (actual, expected) in enumerate(zip(container, children)):
      if actual != expected:
        raise AssertionError(
          f"Container item {i} differed from expected. "
          f"Expected: {expected}, Actual: {actual}")
