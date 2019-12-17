from __future__ import annotations

from enum import Enum, auto


class NaturalResource(Enum):
    ORGANIC = auto()
    COMPOUND = auto()
    RESIN = auto()
    CLAY = auto()
    QUARTZ = auto()
    AMMONIUM = auto()
    GRAPHITE = auto()
    LATERITE = auto()
    ASTRONIUM = auto()
    LITHIUM = auto()


class RefinedResource(Enum):
    CARBON = auto()
    CERAMIC = auto()
    GLASS = auto()
    ALUMINUM = auto()
    ZINC = auto()
    COPPER = auto()
    TUNGSTEN = auto()
    IRON = auto()
    TITANIUM = auto()
    HYDROGEN = auto()


class AtmosphericResource(Enum):
    ARGON = auto()
    METHANE = auto()
    NITROGEN = auto()
    SULFUR = auto()
    HELIUM = auto()
