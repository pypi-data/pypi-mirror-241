"""Module containing operations shared by multiple applications.

The operations included here are shared by multiple applications and use
almost identical implementations for each application, but they
are not general enough to be included in the general operations module.
"""
###############################################################################
#
# (C) Copyright 2021, Maptek Pty Ltd. All rights reserved.
#
###############################################################################

from mapteksdk.internal.transaction import (request_transaction,
                                            RequestTransactionWithInputs)
from mapteksdk.operations import _decode_selection

def _loop_surface_straight(selection, command_prefix, destination=None):
  """Create a Surface from a series of loops using "straight loop ordering".

  This creates a single Surface with the loops connected based on
  their orientation.

  Parameters
  ----------
  selection : list
    List of Surfaces or Polygons to use to generate the loop surface.
    Each must contain loops.
  command_prefix : string
    Command prefix for the application to run the operation.
  destination : str
    Path to place the destination object. If not specified,
    this will use the default destination of the menu item.

  Returns
  -------
  WorkflowSelection
    Selection containing the created Surface.

  """
  inputs = [
    ('selection', RequestTransactionWithInputs.format_selection(selection)),
    ('straightLoopOrdering', 'true'),
    ('iterativeLoopOrdering', 'false'),
  ]

  if destination:
    inputs.append(('destination', destination))

  outputs = request_transaction(
    server='sdpServer',
    transaction='mtp::sdpS_TriangulateLoopSetTransaction',
    command_name=f'{command_prefix}.TriangulateLoopSet',
    inputs=inputs,
    )

  return _decode_selection(outputs)


def _loop_surface_iterative(selection, command_prefix, destination=None):
  """Creates Surfaces from a series of loops using "iterative loop ordering".

  This joins nearby loops with similar orientations. This can create
  multiple surfaces and may wrap around corners if needed.

  Unlike loop_surface_straight, this may ignore loops if they are not
  sufficiently close to another loop.

  Parameters
  ----------
  selection : list
    List of Surfaces or Polygons to use to generate the loop surfaces.
    Each must contain loops.
  command_prefix : string
    Command prefix for the application to run the operation.
  destination : str
    Path to place the destination object. If not specified,
    this will use the default destination of the menu item.

  Returns
  -------
  WorkflowSelection
    Selection containing the created Surface(s).

  """
  inputs = [
    ('selection', RequestTransactionWithInputs.format_selection(selection)),
    ('straightLoopOrdering', 'false'),
    ('iterativeLoopOrdering', 'true'),
  ]

  if destination:
    inputs.append(('destination', destination))

  outputs = request_transaction(
    server='sdpServer',
    transaction='mtp::sdpS_TriangulateLoopSetTransaction',
    command_name=f'{command_prefix}.TriangulateLoopSet',
    inputs=inputs,
    )

  return _decode_selection(outputs)

def _fix_surface(surfaces, command_prefix):
  """Automates the fixing of common issues with surfaces (triangulation).

  The fixes it performs are:
  - Self intersections - Fixes cases where the surface intersects itself

  - Trifurcations - Fixes cases where the surface meets itself, creating a
    T-junction.

  - Facet normals - Orient facet normals to point in the same direction.
    This will be up for surfaces/topography and out for solids.

  - Vertical facets - Remove vertical facets and close the hole this produces
    by moving the points along the top down, adding points as necessary to
    neighbouring non-vertical facets to maintain a consistent surface.

  Parameters
  ----------
  surfaces : list
    The list of surfaces to fix.
  command_prefix : string
    Command prefix for the application to run the operation.

  Returns
  ----------
  list
    The list of surfaces.
  """

  inputs = [
    ('selection', RequestTransactionWithInputs.format_selection(surfaces)),
    ('isFixingSelfIntersections', 'true'),
    ('isFixingTrifurcations', 'true'),
    ('isFixingFacetNormals', 'true'),
    ('collapseVerticalFacet', 'Down'),  # Up is the other option.
  ]

  outputs = request_transaction(
    server='sdpServer',
    transaction='mtp::sdpS_FixFacetNetworkTransaction',
    command_name=f'{command_prefix}.FixSurface',
    inputs=inputs,
    )

  return _decode_selection(outputs)
