"""Representation of the objects within a Project.

Many of the types within this package can be used to create a new object
of that type through Project.new(). Classes defined in this module are yielded
when opening an object via Project.read() and Project.edit().

See Also
--------
:documentation:`data-types` : Documentation of data types.

"""
###############################################################################
#
# (C) Copyright 2020, Maptek Pty Ltd. All rights reserved.
#
###############################################################################

from .points import PointSet
from .edges import EdgeNetwork, Polygon, Polyline
from .ribbons import RibbonChain, RibbonLoop
from .facets import Surface
from .geotechnical import Discontinuity, Polarity
from .blocks import DenseBlockModel, SubblockedBlockModel, SparseBlockModel
from .cells import GridSurface
from .scans import Scan
from .annotations import (Text2D, Text3D, Marker, VerticalAlignment,
                          HorizontalAlignment, FontStyle)
from .images import Raster
from .image_registration import (
  RasterRegistrationTwoPoint,
  RasterRegistrationNone,
  RasterRegistrationUnsupported,
  RasterRegistrationMultiPoint,
  RasterRegistrationOverride
)
from .base import DataObject, Topology
from .colourmaps import (NumericColourMap, StringColourMap, UnsortedRangesError,
                         CaseInsensitiveDuplicateKeyError)
from .containers import Container, VisualContainer, StandardContainer
from .objectid import ObjectID
from .units import DistanceUnit, AngleUnit, UnsupportedUnit, Axis
from .errors import (CannotSaveInReadOnlyModeError, DegenerateTopologyError,
                     InvalidColourMapError)
from .coordinate_systems import (CoordinateSystem, LocalTransform,
                                 LocalTransformNotSupportedError)
from .ellipsoid import Ellipsoid
from .change_reasons import ChangeReasons
from .filled_polygon import FilledPolygon
from .primitives import AttributeKey
