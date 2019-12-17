from enum import Enum, auto


class ResourceBase(Enum):
    """Unified resource base class for easier isinstance check."""


class NaturalResource(ResourceBase):
    """Hashable name mapping for natural resources."""

    AMMONIUM = auto()
    ASTRONIUM = auto()
    CLAY = auto()
    COMPOUND = auto()
    GRAPHITE = auto()
    LATERITE = auto()
    LITHIUM = auto()
    ORGANIC = auto()
    QUARTZ = auto()
    RESIN = auto()


class RefinedResource(ResourceBase):
    """Hashable name mapping for refined resources."""

    ALUMINUM = auto()
    CARBON = auto()
    CERAMIC = auto()
    COPPER = auto()
    GLASS = auto()
    HYDROGEN = auto()
    IRON = auto()
    TITANIUM = auto()
    TUNGSTEN = auto()
    ZINC = auto()


class AtmosphericResource(ResourceBase):
    """Hashable name mapping for atmospheric resources."""

    ARGON = auto()
    HELIUM = auto()
    HYDROGEN = auto()
    METHANE = auto()
    NITROGEN = auto()
    SULFUR = auto()
