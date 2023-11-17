"""Tuple representing colour map information."""
###############################################################################
#
# (C) Copyright 2022, Maptek Pty Ltd. All rights reserved.
#
###############################################################################
from __future__ import annotations

import dataclasses
import typing

from ..data.objectid import ObjectID

if typing.TYPE_CHECKING:
  from ..data.colourmaps import ColourMap
  from ..data.primitive_type import PrimitiveType
  from ..data.primitives import AttributeKey

@dataclasses.dataclass
class ColourMapInformation:
  """Named tuple containing colour map information for a Topology object."""
  attribute_name: str
  """The name of the attribute the object is coloured by.

  To represent no colour map, this should be the empty string.
  """
  attribute_key: typing.Optional[AttributeKey]
  """The attribute key of the attribute.

  This will be None when loading the colour map information because only the
  name is provided by the C API in that case.
  """
  primitive_type: PrimitiveType
  """The primitive type of the attribute the object is coloured by."""
  colour_map_id: ObjectID[ColourMap]
  """Object ID of the colour map used to colour this object.

  To represent no colour map, this should be the null Object ID.
  """
  def is_valid(self) -> bool:
    """True if the colour map association is valid.

    If this is False, then the colour map association is invalid
    and no colour map is associated with the object.
    """
    return bool(self.attribute_name) and bool(self.colour_map_id)

  # :TODO: SDK-506 Self is not available in Python 3.7, so the type hint must
  # be in quotes.
  @classmethod
  def no_colour_map(cls, primitive_type: PrimitiveType) -> "typing.Self":
    """Construct ColourMapInformation indicating no colour map exists.

    Parameters
    ----------
    primitive_type
      PrimitiveType to indicate has no colour map associated with it.
    """
    return cls(
      "",
      None,
      primitive_type,
      ObjectID()
    )

  @classmethod
  def from_attribute_key(
      cls,
      key: AttributeKey,
      primitive_type: PrimitiveType,
      colour_map_id: ObjectID[ColourMap]) -> "typing.Self":
    """Construct colour map information using an AttributeKey.

    This is preferable to using the constructor directly, because it ensures
    the name field matches the name of the AttributeKey.

    Parameters
    ----------
    key
      AttributeKey of the attribute to associate with the colour map.
    primitive_type
      The primitive type of the attribute to associate with the colour map.
    colour_map_id
      ObjectID of the colour map to associate with the attribute.
    """
    return cls(
      key.name,
      key,
      primitive_type,
      colour_map_id
    )

  @classmethod
  def from_name(
      cls,
      name: str,
      primitive_type: PrimitiveType,
      colour_map_id: ObjectID[ColourMap]) -> "typing.Self":
    """Construct colour map information using only the name.

    This is preferable to using the constructor directly, because it ensures
    the name attribute key is correctly set to Nonne.

    Parameters
    ----------
    name
      The name of the attribute the colour map is associated with. This will
      later be used to look up the AttributeKey of the attribute.
    primitive_type
      The primitive type of the attribute to associate with the colour map.
    colour_map_id
      ObjectID of the colour map to associate with the attribute.
    """
    return cls(
      name,
      None,
      primitive_type,
      colour_map_id
    )
