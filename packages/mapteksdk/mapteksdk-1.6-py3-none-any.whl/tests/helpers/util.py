"""Helpers functions for tests which don't go anywhere else."""
###############################################################################
#
# (C) Copyright 2023, Maptek Pty Ltd. All rights reserved.
#
###############################################################################
from __future__ import annotations
import typing

import contextlib
import numpy

from mapteksdk.data import PointSet

if typing.TYPE_CHECKING:
  from mapteksdk.project import Project
  from mapteksdk.data import Surface, ObjectID

def z_extent(project: Project, surface: ObjectID[Surface]):
  """Read the surface and return its Z extent."""
  with project.read(surface) as readable_surface:
    min_z = readable_surface.extent.minimum[2]
    max_z = readable_surface.extent.maximum[2]
    return min_z, max_z


def z_extents(project: Project, surfaces: typing.Iterable[ObjectID[Surface]]):
  """Read the surfaces and return the total Z extent of the surfaces."""
  # This creates a surface_count x 2 array with the first column the
  # extent minimums and the second column the extent maximums.
  extents = numpy.array([z_extent(project, surface) for surface in surfaces])
  return numpy.min(extents[:, 0]), numpy.max(extents[:, 1])


def convert_surface_to_pointset(
    project: Project,
    surface_id: ObjectID[Surface],
    destination_path: str):
  """Create a PointSet from the given Surface object."""
  with project.new_or_edit(destination_path, PointSet) as new_object:
    with project.read(surface_id) as old_object:
      new_object.points = old_object.points
      point_count = old_object.point_count

  return new_object.id, point_count

@contextlib.contextmanager
def enable_nep50_overflow():
  """Context manager to disable NEP 50 warning and enable overflow exception.

  If/when a future version of numpy stops providing a way to control this
  behaviour then tests will fail and this function should not throw
  NotImplementedError if the version is so new that it doesn't have the
  function as the NEP 50 behaviour is the default.
  """
  # pylint: disable=protected-access

  get_promotion_state = getattr(numpy, '_get_promotion_state', None)

  if not get_promotion_state:
    raise NotImplementedError(
      "numpy doesn't support the NEP 50 promotion state.\n"
      "This means overflow won't be detected by numpy and it will will resort "
      "to wrapping numbers around the bounds.")

  state_before = numpy._get_promotion_state()
  try:
    # This enables the overflow exception and disables the warning.
    #
    # Essentially, this lets us test against the behaviour of future numpy
    # version.
    numpy._set_promotion_state("weak")
    yield
  finally:
    numpy._set_promotion_state(state_before)
