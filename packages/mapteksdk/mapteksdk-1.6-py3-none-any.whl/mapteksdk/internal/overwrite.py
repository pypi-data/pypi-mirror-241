"""Helper functions for overwriting objects."""
###############################################################################
#
# (C) Copyright 2023, Maptek Pty Ltd. All rights reserved.
#
###############################################################################
from __future__ import annotations
import typing

from ..capi import DataEngine
from ..data import ObjectID
from ..internal.lock import WriteLock
from ..internal.path_helpers import check_path_component_validity
from ..overwrite_modes import OverwriteMode

def _unique_name(object_name: str, container_lock: WriteLock) -> str:
  """Get a unique unused name for the object.

  Parameters
  ----------
  object_name
    The name to use as a base.
  container_lock
    Lock on the container to generate the unique name for.

  Returns
  -------
  str
    object_name with the smallest possible integer appended such
    that there is no object in the container with that name.
  """
  name_template = f"{object_name} %i"
  i = 1
  new_name = name_template % i
  while DataEngine().ContainerFind(
      container_lock.lock, new_name.encode("utf-8")):
    i += 1
    new_name = name_template % i
  return new_name


def _add_to_container_with_override(
    container_lock: WriteLock,
    object_name: str,
    object_id: ObjectID,
    allow_hidden_objects: bool,
    overwrite: OverwriteMode):
  """Add a single object to an open container.

  Parameters
  ----------
  container_lock
    Write lock on the container to add the object to.
  object_name
    The name to add the object with.
  object_id
    ObjectID of the object to add.
  allow_hidden_objects
    If True, object_name can be the name for a hidden object.
    If False, an error will be raised if object_name is for
    a hidden object.
  overwrite
    Enum indicating what behaviour to use if there is already an object with
    the given name in the container.
  """
  check_path_component_validity(object_name, allow_hidden_objects)
  existing_object = DataEngine().ContainerFind(
      container_lock.lock, object_name.encode("utf-8"))
  if existing_object:
    if existing_object.value == object_id.handle.value:
      # The object has already been added to the container
      # with the specified name.
      return

    if overwrite is OverwriteMode.ERROR:
      raise ValueError(
        f"There is already an object in the container "
        f"called: '{object_name}'")
    if overwrite is OverwriteMode.OVERWRITE:
      DataEngine().ContainerRemoveObject(
        container_lock.lock, existing_object, False)
    elif overwrite is OverwriteMode.UNIQUE_NAME:
      new_name = _unique_name(object_name, container_lock)
      object_name = new_name

  DataEngine().ContainerAppend(
    container_lock.lock,
    object_name.encode("utf8"),
    object_id.handle,
    True)


def add_objects_with_overwrite(
    container_lock: WriteLock,
    objects_to_add: typing.Iterable[tuple[str, ObjectID]],
    allow_hidden_objects: bool,
    overwrite: OverwriteMode):
  """Add objects to the container with overwrite support.

  Parameters
  ----------
  container_lock
    Write lock on the container to add objects to.
  objects_to_add
    An iterable of tuples containing the name to add each object at
    and the object ID of each object to add.
  allow_hidden_objects
    If true, allows adding hidden objects to the container.
    If false, an error will be raised if an object_to_add would be
    a hidden object.
  overwrite
    Enum indicating what behaviour to use if there is already an object with
    the given names in the container.

  Raises
  ------
  ValueError
    If overwrite is OverwriteMode.ERROR and there is already an object
    with the specified name in the container.
  ValueError
    If this would add a hidden object and adding hidden objects
    is disallowed.
  """
  for object_name, object_id in objects_to_add:
    _add_to_container_with_override(
      container_lock, object_name, object_id, allow_hidden_objects, overwrite)
