"""Functions which create data for tests to use.

If a function which creates test data is only used in a single test file,
then it should be defined in that file and not here.

Use testdata_helpers.py to import test data generated in the application when:
* Generating the test data in Python is computationally prohibitive.
* It is not possible to generate the test data in Python (e.g. Due to testing
  against an old application).
* Because you have a good reason not to do it in Python.
"""
###############################################################################
#
# (C) Copyright 2023, Maptek Pty Ltd. All rights reserved.
#
###############################################################################

from __future__ import annotations

import ctypes

import numpy

from mapteksdk.data import PointSet, Polygon, ObjectID
from mapteksdk.geologycore import (
  DrillholeDatabase, DrillholeFieldType, DrillholeTableType)
from mapteksdk.project import Project

def grid_of_points(column_count=10, row_count=10):
  """"Create a uniform grid of points spaced every 1m in X and Y.

  The grid will be column_count across and row_count upwards."""
  x_values = numpy.arange(0, row_count)
  y_values = numpy.arange(0, column_count)
  z_value = 0
  indexing = "ij"
  return numpy.array(numpy.meshgrid(x_values,
                                    y_values,
                                    z_value,
                                    indexing=indexing),
                     dtype=ctypes.c_double).T.reshape(-1, 3)

def create_simple_loops(project, container_path):
  """Creates a set of equally spaced loop polygons.

  Parameters
  ----------
  project : Project
    Project to create the polygons in.
  container_path : str
    Path to the container to create the polygons in.

  """
  loop_radii = (6, 4, 3, 3, 6, 5, 4, 5, 4)
  loop_point_counts = (9, 16, 9, 28, 15, 17, 28, 29, 21)

  base_path = container_path + "/loop {0}"

  create_loop_objects(
    project, base_path, loop_radii, loop_point_counts, [0, 0, 0])

def create_scattered_loops(project, container_path):
  """Creates loops which cannot be easily connected.

  This creates three groups of four loops and a single isolated loop
  with no other loops nearby loops.

  Parameters
  ----------
  project : Project
    Project to create the polygons in.
  container_path : str
    Path to the container to create the polygons in.
  """
  loop_radii = ((6, 4, 5, 4), (3, 6, 5, 6), (4, 5, 4, 4), (6,))

  loop_point_counts = ((9, 16, 9, 12), (28, 15, 17, 20), (28, 29, 21, 24),
                       (14,))

  starts = [[-1, -3, -1], [6, -10, 4], [12, 8, -4], [20, 0, 5]]

  for i, (radii, counts, start) in enumerate(zip(
      loop_radii, loop_point_counts, starts)):
    base_path = container_path + f"/loop {i}" + " {0}"
    create_loop_objects(
      project, base_path, radii, counts, start)

def create_isolated_loops(project, container_path):
  """Creates loops which cannot be used to make a surface.

  Parameters
  ----------
  project : Project
    Project to create the polygons in.
  container_path : str
    Path to the container to create the polygons in.

  """
  radius = (4,)
  point_count = (16,)
  centres = [[-20, 0, 0], [-10, 0, 0], [10, 0, 0], [20, 0, 0]]

  for i, centre in enumerate(centres):
    base_path = container_path + f"/loop {i}" + " {0}"
    create_loop_objects(project, base_path, radius, point_count, centre)

def create_loop_objects(project, base_path, radii, point_counts, start):
  """Function which creates a single group of loops.

  This is used by the above functions to create the loops. The number
  of loops created is based on the length of radii and point_counts.

  Parameters
  ----------
  project : Project
    Project to create the polygons in.
  base_path : str
    Base path to create the polygons with. This must contain a formatting {0}.
  radii : iterable
    Iterable of radii for each loop to create. This should have the same
    length as point_counts.
  point_counts : iterable
    Iterable of points for each loop to create. This should have the same
    length as radii.
  start : list
    List containing three elements. This is added to the coordinates of
    every loop.

  """
  two_pi = 2 * numpy.pi
  for i, (radius, point_count) in enumerate(zip(radii, point_counts)):
    points = numpy.empty((point_count, 3))
    initial_values = numpy.arange(0, two_pi, two_pi / point_count)

    # Set the x values to:
    # sin((2 * pi) * (index / point_count)) * radius
    points[:, 0] = initial_values
    numpy.sin(points[:, 0], out=points[:, 0])
    points[:, 0] *= radius

    # The y coordinate is the same for the entire loop.
    points[:, 1] = 1.5 * i

    # Set the y values to:
    # cos((2 * pi) * (index / point_count)) * radius
    points[:, 2] = initial_values
    numpy.cos(points[:, 2], out=points[:, 2])
    points[:, 2] *= radius

    # Adjust the points based on start.
    points += start

    with project.new(base_path.format(i), Polygon, overwrite=True
        ) as loop:
      loop.points = points


def generate_simple_point_set(
    project: Project,
    path: str,
    centre: tuple[float, float, float]) -> ObjectID[PointSet]:
  """Generate a simple point set.

  This point set contains eight points arranged like so:
  *   *
   * *
   * *
  *   *

  The inner points have a z of 0 and the outer points have a z of 1.

  Parameters
  ----------
  project
    Project to create the point set in.
  path
    Path to create the points at.
  centre
    Centre point for the point set.

  Returns
  -------
  ObjectID[Surface]
    Object ID of the surface.
  """
  base_points = [
    [-1, -1, 0], [-1, 1, 0], [1, 1, 0], [1, -1, 0],
    [-2, -2, 1], [-2, 2, 1], [2, 2, 1], [2, -2, 1],
  ]

  with project.new(path, PointSet, overwrite=True) as point_set:
    point_set.points = base_points
    point_set.points += centre
  return point_set.id

def get_test_database_all_tables_minimal(project: Project
    ) -> ObjectID[DrillholeDatabase]:
  """Creates a drillhole database with all tables with minimal fields.

  The database contains a table of each table type. These tables contain
  the minimal fields required for the table to be valid.

  Parameters
  ----------
  project : Project
    Test project to create the database in.

  Returns
  -------
  ObjectID
    Object ID of the DrillholeDatabase. If this is called multiple times
    in the same test, the same ObjectID will be returned each time.
  """
  # It should be fine to use the same path for every test because
  # the maptekdb should be cleared between tests.
  database_path = "drillholes/all_tables"

  # If a previous call has created the database, return it instead of creating
  # another one.
  existing_oid = project.find_object(database_path)
  if existing_oid:
    return existing_oid

  # The collar table is created automatically when the database is created
  # so it does not need to be included here.
  tables_to_add = (
    DrillholeTableType.ASSAY, DrillholeTableType.SURVEY,
    DrillholeTableType.GEOLOGY, DrillholeTableType.DOWNHOLE,
    DrillholeTableType.QUALITY, DrillholeTableType.OTHER)

  with project.new(database_path, DrillholeDatabase
      ) as database:
    for table_type in tables_to_add:
      _ = database.add_table(table_type.name, table_type)
    # The other table starts empty, so add a field to avoid an error.
    other_table = database.tables_by_type(DrillholeTableType.OTHER)[0]
    other_table.add_field("Other", int, "At least one field is needed")
  return database.id

def get_test_database_all_tables_maximal(project: Project
    ) -> ObjectID[DrillholeDatabase]:
  """Creates a drillhole database with all table and field types.

  The returned drillhole database contains every table type and each
  table contains one of each of the field types it supports.

  Parameters
  ----------
  project : Project
    Test project to create the database in.

  Returns
  -------
  ObjectID
    Object ID of the DrillholeDatabase. If this is called multiple times
    in the same test, the same ObjectID will be returned each time.
  """
  # It should be fine to use the same path for every test because
  # the maptekdb should be cleared between tests.
  database_path = "drillholes/max_tables"

  # If a previous call has created the database, return it instead of creating
  # another one.
  existing_oid = project.find_object(database_path)
  if existing_oid:
    return existing_oid

  # The collar table is created automatically when the database is created
  # so it does not need to be included here.
  tables_to_add = (
    DrillholeTableType.ASSAY, DrillholeTableType.SURVEY,
    DrillholeTableType.GEOLOGY, DrillholeTableType.DOWNHOLE,
    DrillholeTableType.QUALITY, DrillholeTableType.OTHER)

  # The fields to add to the tables of each type.
  # Note that the required fields are added automatically when the table is
  # created.
  fields_to_add = {
    DrillholeTableType.COLLAR : [
      {
        "name" : "elevation",
        "data_type" : float,
        "description" : "Height above sea level",
        "field_type" : DrillholeFieldType.ELEVATION,
      },
      {
        "name" : "total_depth",
        "data_type" : float,
        "description" : "Total depth of drillhole",
        "field_type" : DrillholeFieldType.TOTAL_DEPTH,
      },
      {
        "name" : "AZ",
        "data_type" : float,
        "description" : "Azimuth of collar point",
        "field_type" : DrillholeFieldType.AZIMUTH,
      },
      {
        "name" : "dip",
        "data_type" : float,
        "description" : "Dip of collar point",
        "field_type" : DrillholeFieldType.DIP,
      },
      {
        "name" : "underground",
        "data_type" : bool,
        "description" : "If the drillhole is below ground",
      },
    ],
    DrillholeTableType.SURVEY : [
      {
        "name" : "accuracy",
        "data_type" : numpy.float32,
        "description" : "Accuracy of measurement."
      },
    ],
    DrillholeTableType.GEOLOGY : [
      {
        "name" : "thickness",
        "data_type" : float,
        "description" : "Thickness of the interval",
        "field_type" : DrillholeFieldType.THICKNESS,
      },
      {
        "name" : "rock_type",
        "data_type" : str,
        "description" : "Type of rock in the interval",
        "field_type" : DrillholeFieldType.ROCK_TYPE,
      },
      {
        "name" : "horizon",
        "data_type" : str,
        "description" : "For completeness",
        "field_type" : DrillholeFieldType.HORIZON
      },
      {
        "name" : "notes",
        "data_type" : str,
        "description" : "Additional notes on the rock type",
      },
    ],
    DrillholeTableType.ASSAY : [
      {
        "name" : "thickness",
        "data_type" : float,
        "description" : "Thickness of the interval",
        "field_type" : DrillholeFieldType.THICKNESS,
      },
      {
        "name" : "CU",
        "data_type" : float,
        "description" : "Copper in interval",
      }
    ],
    DrillholeTableType.DOWNHOLE: [
      {
        "name" : "thickness",
        "data_type" : float,
        "description" : "Thickness of the interval",
        "field_type" : DrillholeFieldType.THICKNESS,
      },
      {
        "name" : "colour",
        "data_type" : str,
        "description" : "Colour of the interval"
      },
    ],
    DrillholeTableType.QUALITY : [
      {
        "name" : "thickness",
        "data_type" : float,
        "description" : "Thickness of the interval",
        "field_type" : DrillholeFieldType.THICKNESS,
      },
      {
        "name" : "verified",
        "data_type" : bool,
        "description" : "If quality has been verified",
      },
    ],
    DrillholeTableType.OTHER : [
      {
        "name" : "drill_rig",
        "data_type" : str,
        "description" : "ID of the drill rig used."
      }
    ]
  }
  # It should be fine to use the same path for every test because
  # the maptekdb should be cleared between tests.
  with project.new(database_path, DrillholeDatabase
      ) as database:
    for table_type, fields in fields_to_add.items():
      if table_type is DrillholeTableType.COLLAR:
        table = database.collar_table
      else:
        table = database.add_table(table_type.name, table_type)
      for field in fields:
        table.add_field(**field)
  return database.id
