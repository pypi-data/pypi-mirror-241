"""Geometry types used in the Python SDK.

This does not cover the common geometry types of points, vectors and
facets which are represented with numpy arrays rather than distinct
types/classes.
"""
###############################################################################
#
# (C) Copyright 2023, Maptek Pty Ltd. All rights reserved.
#
###############################################################################

from __future__ import annotations

import numpy as np
import typing

if typing.TYPE_CHECKING:
  # This requires numpy 1.20 or later to be used.
  import numpy.typing as npt


class Plane:
  """A plane in 3D defined by the equation Ax + By + Cz + D = 0.
  """

  # pylint: disable=invalid-name;reason=Names are common to the domain and
  # would be unnecessarily wordy otherwise.
  def __init__(self, a: float, b: float, c: float, d: float):
    self.coefficient_a = a
    self.coefficient_b = b
    self.coefficient_c = c
    self.coefficient_d = d

  def __eq__(self, other):
    return (
    self.coefficient_a == other.coefficient_a and
    self.coefficient_b == other.coefficient_b and
    self.coefficient_c == other.coefficient_c and
    self.coefficient_d == other.coefficient_d)

  def __repr__(self) -> str:
    return f'Plane({self.coefficient_a}, {self.coefficient_b}, ' + \
      f'{self.coefficient_c}, {self.coefficient_d})'

  @property
  def normal(self) -> npt.ArrayLike:
    """The normal of the plane.

    This is not normalised (i.e. its length is not guaranteed to be 1).
    """
    return (self.coefficient_a, self.coefficient_b, self.coefficient_c)

  def translated(self, vector: npt.ArrayLike) -> Plane:
    """Return a new Plane translated by the given vector.

    Parameters
    ----------
    vector
      The vector by which the plane will be translated.

    Returns
    -------
    Plane
      A new plane that has been translated from the current plane by vector.

    Warnings
    --------
    Vector must not contain NaNs.
    Vector must be a 3D vector (consist of 3 components).
    """
    point = self._closest_point_on_plane_to((0.0, 0.0, 0.0))
    return self.from_normal_and_point(self.normal, point + vector)

  def _closest_point_on_plane_to(self, point: npt.ArrayLike) -> npt.ArrayLike:
    """Find the point on the plane closest to a specified point.

    Parameters
    ----------
    point
      The specified point.

    Returns
    -------
    npt.ArrayLike
      The closest point on the plane to the specified point.
    """
    # The closest point is calculated as:
    #    closest_point = specified_point + t * normal
    # Where
    #    t = -F ( specified_point ) / ( || normal || ^2)
    # And
    #    F(point) = A * point.x + B * point.y + C * point.z + D
    # With
    #    A, B, C, D being the coefficients of hte plane.
    f = (self.coefficient_a * point[0] + self.coefficient_b * point[1] +
         self.coefficient_c * point[2] + self.coefficient_d)

    normal = np.asarray(self.normal)
    t = -f / (normal  * normal ).sum()
    return np.asarray(point) + normal * t

  @classmethod
  def from_normal_and_point(cls, normal: npt.ArrayLike, point: npt.ArrayLike):
    """Construct a plane using a normal vector and point on the plane.

    Parameters
    ----------
    normal
      The normal vector of the plane.
      The magnitude (also known as length) of this vector must be non-zero.
    point
      A point on the plane.

    Warnings
    --------
    The length of the normal vector must not be zero.
    The normal or point must not contain NaNs.
    The point must be 3D point (consist of 3 components).
    """
    normal = np.asarray(normal)
    normalised_normal = normal / np.linalg.norm(normal)

    return cls(normalised_normal[0],
               normalised_normal[1],
               normalised_normal[2],
               -np.dot(normalised_normal, point))

  @classmethod
  def from_three_points(cls,
                        point1: npt.ArrayLike,
                        point2: npt.ArrayLike,
                        point3: npt.ArrayLike):
    """Construct a plane using three points and the right-hand rule.

    The plane normal is in the direction of Cross(point2 - point1,
    point3 - point1) and normal's magnitude (also known as length) must be
    non-zero.

    Parameters
    ----------
    point1
      The first point.
    point2
      The second point.
    point3
      The third point.

    Warnings
    --------
    The given points must be 3D points (consist of 3 components).
    The given points must not contain NaNs.
    The given points must not all be colinear.
    The length of the normal vector produced from the points must not be zero.
    """
    # Convert points to numpy arrays.
    point1 = np.asarray(point1)
    point2 = np.asarray(point2)
    point3 = np.asarray(point3)

    normal = np.cross(point2 - point1, point3 - point1)
    normalised_normal = normal / np.linalg.norm(normal)

    return cls(normalised_normal[0],
               normalised_normal[1],
               normalised_normal[2],
               -np.dot(normalised_normal, point1))

  @classmethod
  def xy(cls, z: float = 0):
    """Return a plane whose normal lines along the axis Z.

    The plane passes through (0, 0, z).

    Parameters
    ----------
    z
      The z-coordinate of the plane.

    Warnings
    --------
    The z should not be NaN.
    """
    return cls(0, 0, 1, -z)

  @classmethod
  def yz(cls, x: float = 0):
    """Return a plane whose normal lines along the axis X.

    The plane passes through (0, 0, 0).

    Parameters
    ----------
    x
      The x-coordinate of the plane.

    Warnings
    --------
    The x should not be NaN.
    """
    return cls(1, 0, 0, -x)

  @classmethod
  def xz(cls, y: float = 0):
    """Return a plane whose normal lines along the axis Y.

    The plane passes through (0, 0, 0).

    Parameters
    ----------
    y
      The y-coordinate of the plane.

    Warnings
    --------
    The y should not be NaN.
    """
    return cls(0, -1, 0, y)
