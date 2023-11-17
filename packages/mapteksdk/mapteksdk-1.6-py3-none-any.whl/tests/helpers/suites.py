"""Test suites which build on assertions.py.

These allow for common groups of tests to be put together.
"""
###############################################################################
#
# (C) Copyright 2023, Maptek Pty Ltd. All rights reserved.
#
###############################################################################
from __future__ import annotations

import typing
import unittest

import numpy as np

from mapteksdk.data.errors import ReadOnlyError
from mapteksdk.internal.lock import ObjectClosedError
from mapteksdk.project import Project

from . import assertions

if typing.TYPE_CHECKING:
  import numpy.typing as npt

T = typing.TypeVar("T")
"""Type for a parameter which can be any type."""

def object_attribute_standard_test_suite(
    owner: unittest.TestCase,
    test_parameters: assertions.PropertyTestTuple,
    good_value: T,
    happy_value: T,
    bad_values: dict[str, tuple[type[Exception], typing.Any]]):
  """Run standard tests for a property with one value for the whole object.

  This tests the following:
  * The property can be set in a Project.new() block.
  * The property can be set in a Project.edit() block.
  * It is an error to set the property in a Project.read() block.
  * It is an error to read the property after close() is called.
  * It is an error to edit the property after close() is called.
  * An error is raised if the property is set to any of the invalid
    values provided to the function.

  This only provides the most basic testing. Test suites should provide
  more detailed object specific tests in addition to this.

  Parameters
  ----------
  owner
    The unittest object which has called this function.
    This must have a `project` property assigned to a Project object.
  test_parameters
    Test parameters which define how to setup the object and read/edit
    the property under test.
  good_value
    A valid value for the property under test.
  happy_value
    A valid value for the property under test which is different from
    good_value.
  bad_values
    Dictionary where the keys are test case names and the values are
    tuples of expected exceptions and values. Assigning the value in
    the tuple to the property under test is expected to raise the
    expected exception.
  """
  project: Project = getattr(owner, "project")
  with owner.subTest(name="set in new"):
    assertions.assert_property_can_be_set_in_new(
      project=project,
      parameters=test_parameters,
      expected_value=good_value
    )
  with owner.subTest(name="set in edit"):
    assertions.assert_property_can_be_edited(
      project=project,
      parameters=test_parameters,
      original_value=good_value,
      expected_value=happy_value
    )
  with owner.subTest(name="Error for read-only"):
    assertions.assert_cannot_edit_read_only_property(
      project=project,
      parameters=test_parameters,
      assert_raises=owner.assertRaises,
      default_value=good_value,
      new_value=happy_value
    )
  with owner.subTest(name="Error read after close"):
    assertions.assert_cannot_read_property_after_close(
      project=project,
      parameters=test_parameters,
      assert_raises=owner.assertRaises,
      default_value=good_value
    )
  with owner.subTest(name="Error edit after close"):
    assertions.assert_cannot_edit_property_after_close(
      project=project,
      parameters=test_parameters,
      assert_raises=owner.assertRaises,
      default_value=good_value,
      new_value=happy_value
    )

  for name, (expected_exception, bad_value) in bad_values.items():
    with owner.subTest(name=name):
      assertions.assert_set_property_to_bad_value(
        project=project,
        parameters=test_parameters,
        assert_raises=owner.assertRaises,
        good_value=good_value,
        bad_value=bad_value,
        expected_exception=expected_exception
      )

  with owner.subTest(name="Default value"):
    def assert_property_has_default(data_object):
      test_parameters.assert_equal(
        test_parameters.read_property(data_object),
        test_parameters.default
      )

      assertions.assert_create_object(
        project=project,
        object_type=test_parameters.object_type,
        setup_function=test_parameters.setup_function,
        verify_function=assert_property_has_default
      )

def per_primitive_secondary_attribute_standard_test_suite(
    owner: unittest.TestCase,
    test_parameters: assertions.PropertyTestTuple,
    good_value: typing.Sequence[T],
    happy_value: typing.Sequence[T],
    expanded_happy_value: typing.Sequence[T],
    shrunk_happy_value: typing.Sequence[T],
    bad_values: dict[str, tuple[type[Exception], typing.Any]],
    expand_primary_property: typing.Callable[
      [assertions.DataObjectSubclass], None],
    shrink_primary_property: typing.Callable[
      [assertions.DataObjectSubclass], None]):
  """Run standard tests for a property with one value per primitive.

  This tests the following:
  * The property can be set in a Project.new() block.
  * The property can be set in a Project.edit() block.
  * It is an error to set the property in a Project.read() block.
  * Adding a primitive expands the array.
  * Removing a primitive shrinks the array.
  * It is an error to read the property after close() is called.
  * It is an error to edit the property after close() is called.
  * An error is raised if the property is set to any of the invalid
    values provided to the function.

  This only provides the most basic testing. Test suites should provide
  more detailed object specific tests in addition to this.

  Parameters
  ----------
  owner
    The unittest object which has called this function.
    This must have a `project` property assigned to a Project object.
  test_parameters
    Test parameters which define how to setup the object and read/edit
    the property under test.
  good_value
    A valid value for the property under test.
  happy_value
    A valid value for the property under test which is different from
    good_value.
  expanded_happy_value
    The expected value of good_value after `expand_primary_property` has
    been run.
  shrunk_happy_value
    The expected value of good_value after `shrink_primary_property` has
    been run.
  bad_values
    Dictionary where the keys are test case names and the values are
    tuples of expected exceptions and values. Assigning the value in
    the tuple to the property under test is expected to raise the
    expected exception.
  expand_primary_property
    A function which will expand the primary property which defines the
    length of the secondary property. This does not need to be callable
    more than once.
  """
  project: Project = getattr(owner, "project")

  with owner.subTest(name="set in new"):
    assertions.assert_property_can_be_set_in_new(
      project=project,
      parameters=test_parameters,
      expected_value=good_value
    )
  with owner.subTest(name="set in edit"):
    assertions.assert_property_can_be_edited(
      project=project,
      parameters=test_parameters,
      original_value=good_value,
      expected_value=happy_value
    )
  with owner.subTest(name="Add primitive expands array"):
    assertions.assert_resize_primary_resizes_secondary(
      project=project,
      parameters=test_parameters,
      resize_primary_property=expand_primary_property,
      original_value=happy_value,
      expected_value=expanded_happy_value
    )
  with owner.subTest(name="Remove primitive shrinks array"):
    assertions.assert_resize_primary_resizes_secondary(
      project=project,
      parameters=test_parameters,
      resize_primary_property=shrink_primary_property,
      original_value=happy_value,
      expected_value=shrunk_happy_value
    )
  with owner.subTest(name="broadcast"):
    assertions.assert_array_property_supports_broadcast(
      project=project,
      parameters=test_parameters,
      single_value=good_value[0]
    )
  with owner.subTest(name="Error for read-only"):
    assertions.assert_cannot_edit_read_only_property(
      project=project,
      parameters=test_parameters,
      assert_raises=owner.assertRaises,
      default_value=good_value,
      new_value=happy_value
    )
  with owner.subTest(name="Error read after close"):
    assertions.assert_cannot_read_property_after_close(
      project=project,
      parameters=test_parameters,
      assert_raises=owner.assertRaises,
      default_value=good_value
    )
  with owner.subTest(name="Error edit after close"):
    assertions.assert_cannot_edit_property_after_close(
      project=project,
      parameters=test_parameters,
      assert_raises=owner.assertRaises,
      default_value=good_value,
      new_value=happy_value
    )

  for name, (expected_exception, bad_value) in bad_values.items():
    with owner.subTest(name=name):
      assertions.assert_set_property_to_bad_value(
        project=project,
        parameters=test_parameters,
        assert_raises=owner.assertRaises,
        good_value=happy_value,
        bad_value=bad_value,
        expected_exception=expected_exception
      )

  with owner.subTest(name="Default value"):
    def assert_property_has_default(data_object):
      owner.assertTrue(
        np.all(
          test_parameters.read_property(data_object) == test_parameters.default)
      )

      assertions.assert_create_object(
        project=project,
        object_type=test_parameters.object_type,
        setup_function=test_parameters.setup_function,
        verify_function=assert_property_has_default
      )

def append_primitive_test_suite(
    owner: unittest.TestCase,
    append_primitive: typing.Callable[
      [assertions.DataObjectSubclass, npt.ArrayLike], None],
    get_primitives: typing.Callable[
      [assertions.DataObjectSubclass], np.ndarray],
    setup_function: typing.Callable[[assertions.DataObjectSubclass], None],
    object_type: typing.Callable[
      [], assertions.DataObjectSubclass | type[assertions.DataObjectSubclass]],
    primitive_a: npt.ArrayLike,
    primitive_b: npt.ArrayLike,
    primitive_c: npt.ArrayLike,
    extra_setup: typing.Callable[
      [assertions.DataObjectSubclass], None]=assertions.default_setup_function
    ):
  """Check that primitives can be appended to a DataObject.

  This is intended to be used to test the append_point(), append_edge() and
  append_facet() function.

  This asserts that:
  * A single primitive can be appended to an object.
    e.g. surface.append_facets([0, 1, 2])
  * Multiple primitives can be appended to an object.
    e.g. surface.append_facets([0, 1, 2], [1, 2, 3])
  * An iterable containing one of more primitives can be appended to an object.
    e.g. surface.append_facets([[0, 1, 2], [1, 2, 3]])
  * A mix of iterables of primitives and primitives can be appended to an
    object.
    e.g. surface.append_facets([[0, 1, 2], [1, 2, 3]], [0, 1, 4])
  * A single primitive can be appended to an empty object.
  * Many primitives can be appended to an empty object.
  * Cannot append primitives on a read-only object.
  * Cannot append primitives after closing the object.

  This suite does NOT include:
  * Any tests for invalid input to the append function.
  * The return value of the append function.
  * Anything not listed above.

  Parameters
  ----------
  owner
    Unittest class which is running the test.
  append_primitive
    Function which appends the primitives. It should accept the object to
    append primitives to and *args containing the primitives to append.
  get_primitives
    Function which gets the primitives. This is used to assert that primitives
    were appended.
  setup_function
    Function to place objects into a valid state before running tests.
  object_type
    Callable returning the object type to pass to Project.new().
  primitive_a
    A primitive. This should be different to primitive_b and primitive_c.
  primitive_b
    A primitive. This should be different to primitive_a and primitive_c.
  primitive_c
    A primitive. This should be different to primitive_a and primitive_b.
  extra_setup
    Any extra setup which needs to be run after adding primitives to the object
    via append_primitive.
    This is run in test cases which do not call setup_function to test appending
    primitives to a blank object.
    This allows for appending other primitives required to place the object into
    a valid, savable state.
  """
  project: Project = getattr(owner, "project")

  def assert_primitive_a_appended(data_object: assertions.DataObjectSubclass):
    np.testing.assert_array_almost_equal(
      get_primitives(data_object)[-1],
      primitive_a
    )

  def assert_primitive_a_appended_at_start(
      data_object: assertions.DataObjectSubclass):
    np.testing.assert_array_almost_equal(
      get_primitives(data_object)[0],
      primitive_a
    )

  def assert_primitives_a_and_b_appended(
      data_object: assertions.DataObjectSubclass):
    np.testing.assert_array_almost_equal(
      get_primitives(data_object)[-1],
      primitive_b
    )
    np.testing.assert_array_almost_equal(
      get_primitives(data_object)[-2],
      primitive_a
    )

  def assert_primitives_a_b_and_c_appended(
      data_object: assertions.DataObjectSubclass):
    np.testing.assert_array_almost_equal(
      get_primitives(data_object)[-1],
      primitive_c
    )
    np.testing.assert_array_almost_equal(
      get_primitives(data_object)[-2],
      primitive_b
    )
    np.testing.assert_array_almost_equal(
      get_primitives(data_object)[-3],
      primitive_a
    )

  def assert_primitives_a_and_b_appended_at_start(
      data_object: assertions.DataObjectSubclass):
    np.testing.assert_array_almost_equal(
      get_primitives(data_object)[1],
      primitive_b
    )
    np.testing.assert_array_almost_equal(
      get_primitives(data_object)[0],
      primitive_a
    )

  with owner.subTest("Append single primitive"):
    def append_primitive_a(data_object: assertions.DataObjectSubclass):
      append_primitive(data_object, primitive_a)

    assertions.assert_edit_object(
      project=project,
      object_type=object_type,
      setup_function=setup_function,
      edit_function=append_primitive_a,
      verify_function=assert_primitive_a_appended,
    )

  with owner.subTest("Append many primitives"):
    def append_many_primitives(data_object: assertions.DataObjectSubclass):
      append_primitive(data_object, primitive_a, primitive_b)

    assertions.assert_edit_object(
      project=project,
      object_type=object_type,
      setup_function=setup_function,
      edit_function=append_many_primitives,
      verify_function=assert_primitives_a_and_b_appended,
    )

  with owner.subTest("Append iterable containing one primitive"):
    def append_length_one_iterable_primitives(
        data_object: assertions.DataObjectSubclass):
      append_primitive(data_object, (primitive_a,))
    assertions.assert_edit_object(
      project=project,
      object_type=object_type,
      setup_function=setup_function,
      edit_function=append_length_one_iterable_primitives,
      verify_function=assert_primitive_a_appended,
    )

  with owner.subTest("Append iterable containing many primitives"):
    def append_iterable_primitives(data_object: assertions.DataObjectSubclass):
      append_primitive(data_object, (primitive_a, primitive_b))
    assertions.assert_edit_object(
      project=project,
      object_type=object_type,
      setup_function=setup_function,
      edit_function=append_iterable_primitives,
      verify_function=assert_primitives_a_and_b_appended,
    )

  with owner.subTest("Append iterable and single primitive"):
    def append_iterable_and_single_primitive(
        data_object: assertions.DataObjectSubclass):
      append_primitive(data_object, (primitive_a, primitive_b), primitive_c)
    assertions.assert_edit_object(
      project=project,
      object_type=object_type,
      setup_function=setup_function,
      edit_function=append_iterable_and_single_primitive,
      verify_function=assert_primitives_a_b_and_c_appended,
    )

  with owner.subTest("Append single primitive to empty object"):
    # extra_setup() may append extra primitives after primitive_a to
    # handle cases where one primitive is not sufficient to create a
    # valid object.
    # e.g. A Polyline must contain one edge, which requires at least
    #      two points. Therefore, extra_setup() must append an extra
    #      point to make the object valid.
    # To allow for the above, this asserts that primitive_a is at the
    # start of the array rather than the end. This should be the case,
    # because primitive_a is appended to the array when the array has
    # a length of zero, so it should be at index 0.
    def append_primitive_a_with_extra_setup(
        data_object: assertions.DataObjectSubclass):
      append_primitive_a(data_object)
      extra_setup(data_object)
    assertions.assert_create_object(
      project=project,
      object_type=object_type,
      setup_function=append_primitive_a_with_extra_setup,
      verify_function=assert_primitive_a_appended_at_start
    )

  with owner.subTest("Append many primitives to empty object"):
    # This checks for the primitives being at the start of the array
    # rather than the end for similar reasons to the above test.
    def append_many_primitives_with_extra_setup(
        data_object: assertions.DataObjectSubclass):
      append_many_primitives(data_object)
      extra_setup(data_object)
    assertions.assert_create_object(
      project=project,
      object_type=object_type,
      setup_function=append_many_primitives_with_extra_setup,
      verify_function=assert_primitives_a_and_b_appended_at_start
    )

  with owner.subTest("Cannot append primitive in read"):
    with project.new(assertions.next_path(), object_type()) as new_object:
      setup_function(new_object)
      expected_primitives = get_primitives(new_object).copy()

    with project.read(new_object.id) as read_object:
      with owner.assertRaises(ReadOnlyError):
        append_primitive(read_object, primitive_a)
      np.testing.assert_array_almost_equal(
        get_primitives(read_object), expected_primitives)

    with project.read(new_object.id) as final_object:
      np.testing.assert_array_almost_equal(
        get_primitives(final_object), expected_primitives)

  with owner.subTest("Cannot append primitive on closed object"):
    with project.new(assertions.next_path(), object_type()) as new_object:
      setup_function(new_object)
      expected_primitives = get_primitives(new_object).copy()

    with owner.assertRaises(ObjectClosedError):
      append_primitive(new_object, primitive_a)

    with project.read(new_object.id) as read_object:
      np.testing.assert_array_almost_equal(
        get_primitives(read_object), expected_primitives)
