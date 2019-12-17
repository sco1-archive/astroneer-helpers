from typing import NamedTuple

from recipes.resources import AtmosphericResource, NaturalResource, RefinedResource


class CompositeResource(NamedTuple):
    components: dict


RUBBER = CompositeResource(components={NaturalResource.ORGANIC: 1, NaturalResource.RESIN: 1})

PLASTIC = CompositeResource(components={RefinedResource.CARBON: 1, NaturalResource.COMPOUND: 1})

ALUMINUM_ALLOY = CompositeResource(
    components={RefinedResource.ALUMINUM: 1, RefinedResource.COPPER: 1},
)

TUNGSTEN_CARBIDE = CompositeResource(
    components={RefinedResource.TUNGSTEN: 1, RefinedResource.CARBON: 1},
)

HYDRAZINE = CompositeResource(
    components={
        RefinedResource.TUNGSTEN: 1,
        RefinedResource.CARBON: 1,
        AtmosphericResource.HYDROGEN: 1,
    },
)

GRAPHENE = CompositeResource(components={NaturalResource.GRAPHITE: 1, HYDRAZINE: 1})

DIAMOND = CompositeResource(components={GRAPHENE: 2})

SILICONE = CompositeResource(
    components={
        NaturalResource.RESIN: 1,
        NaturalResource.QUARTZ: 1,
        AtmosphericResource.METHANE: 1,
    },
)

EXPLOSIVE_POWDER = CompositeResource(
    components={RefinedResource.CARBON: 2, AtmosphericResource.SULFUR: 1}
)

STEEL = CompositeResource(
    components={RefinedResource.IRON: 1, RefinedResource.CARBON: 1, AtmosphericResource.ARGON: 1}
)

TITANIUM_ALLOY = CompositeResource(
    components={RefinedResource.TITANIUM: 1, GRAPHENE: 1, AtmosphericResource.NITROGEN: 1}
)

NANOCARBON_ALLOY = CompositeResource(
    components={TITANIUM_ALLOY: 1, STEEL: 1, AtmosphericResource.HELIUM: 1}
)
