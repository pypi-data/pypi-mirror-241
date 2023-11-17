"""Utility function for normalising a selection.

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
from __future__ import annotations

import typing

from ..data import DataObject, ObjectID
from .util import default_type_error_message

def normalise_selection(
    selection: typing.Iterable[str | DataObject | ObjectID[DataObject]]
    ) -> typing.Iterable[ObjectID]:
  """Normalises an iterable of objects to an iterable of ObjectID.

  The selection iterable can contain a mix of the following:
  * Object path strings.
  * DataObject subclasses.
  * ObjectIDs.

  This function handles converting each to an ObjectID.

  Parameters
  ----------
  selection
    An iterable containing strings, DataObject subclasses or ObjectIDs.

  Returns
  -------
  Iterable[ObjectID]
    Iterable of ObjectID corresponding to each object in the input
    selection.

  Raises
  ------
  TypeError
    If any item in selection is not a string, DataObject or ObjectID.
  ValueError
    If any item in selection is a string, but there was no object at the
    specified path.
  """
  def to_object_id(item: str | DataObject | ObjectID[DataObject]
      ) -> ObjectID[DataObject]:
    if isinstance(item, ObjectID):
      return item
    if isinstance(item, DataObject):
      return item.id
    if isinstance(item, str):
      return ObjectID.from_path(item)
    raise TypeError(default_type_error_message("selection",
                                              item,
                                              (ObjectID, DataObject, str)))
  return [to_object_id(item) for item in selection]

def normalise_selection_to_paths(
    selection: typing.Iterable[str | DataObject | ObjectID[DataObject]]
    ) -> typing.Iterable[str]:
  """Normalises an iterable of objects to an iterable of object paths.

  The selection iterable can contain a mix of the following:
  * Object path strings.
  * DataObject subclasses.
  * ObjectIDs.

  This function handles converting each to the corresponding object paths.

  Parameters
  ----------
  selection
    An iterable containing strings, DataObject subclasses or ObjectIDs.

  Returns
  -------
  Iterable[str]
    Iterable of object paths corresponding to each object in the input
    selection.

  Raises
  ------
  TypeError
    If any item in selection is not a string, DataObject or ObjectID.
  ValueError
    If any item in selection is a string, but there was no object at the
    specified path.
  """
  def to_path(item: str | DataObject | ObjectID[DataObject]
      ) -> str:
    if isinstance(item, ObjectID):
      return item.path
    if isinstance(item, DataObject):
      return item.id.path
    if isinstance(item, str):
      # Converting the path to an ObjectID and back ensures the path
      # consistently points to an existent object and starts with
      # a slash.
      return ObjectID.from_path(item).path
    raise TypeError(default_type_error_message("selection",
                                              item,
                                              (ObjectID, DataObject, str)))
  return [to_path(item) for item in selection]
