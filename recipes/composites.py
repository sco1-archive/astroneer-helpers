from recipes.helpers import RecipeBase
from recipes.resources import AtmosphericResource, NaturalResource, RefinedResource


COMPOSITE_RECIPES = {
    "ALUMINUM_ALLOY": RecipeBase(
        components={RefinedResource.ALUMINUM: 1, RefinedResource.COPPER: 1},
    ),
    "DIAMOND": RecipeBase(components={"GRAPHENE": 2}),
    "EXPLOSIVE_POWDER": RecipeBase(
        components={RefinedResource.CARBON: 2, AtmosphericResource.SULFUR: 1},
    ),
    "GRAPHENE": RecipeBase(components={NaturalResource.GRAPHITE: 1, "HYDRAZINE": 1}),
    "HYDRAZINE": RecipeBase(
        components={
            RefinedResource.TUNGSTEN: 1,
            RefinedResource.CARBON: 1,
            AtmosphericResource.HYDROGEN: 1,
        },
    ),
    "NANOCARBON_ALLOY": RecipeBase(
        components={"TITANIUM_ALLOY": 1, "STEEL": 1, AtmosphericResource.HELIUM: 1}
    ),
    "PLASTIC": RecipeBase(components={RefinedResource.CARBON: 1, NaturalResource.COMPOUND: 1},),
    "RUBBER": RecipeBase(components={NaturalResource.ORGANIC: 1, NaturalResource.RESIN: 1}),
    "SILICONE": RecipeBase(
        components={
            NaturalResource.RESIN: 1,
            NaturalResource.QUARTZ: 1,
            AtmosphericResource.METHANE: 1,
        },
    ),
    "STEEL": RecipeBase(
        components={
            RefinedResource.IRON: 1,
            RefinedResource.CARBON: 1,
            AtmosphericResource.ARGON: 1,
        },
    ),
    "TITANIUM_ALLOY": RecipeBase(
        components={RefinedResource.TITANIUM: 1, "GRAPHENE": 1, AtmosphericResource.NITROGEN: 1},
    ),
    "TUNGSTEN_CARBIDE": RecipeBase(
        components={RefinedResource.TUNGSTEN: 1, RefinedResource.CARBON: 1},
    ),
}
