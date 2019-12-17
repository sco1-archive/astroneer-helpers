from recipes import composites
from recipes.helpers import RecipeBase
from recipes.resources import NaturalResource, RefinedResource


MEDIUM_STORAGE_SILO = RecipeBase(components={RefinedResource.TITANIUM: 2})

ROVER_SEAT = RecipeBase(components={NaturalResource.COMPOUND: 2})

MEDIUM_STORAGE = RecipeBase(components={NaturalResource.RESIN: 2})

DRILL_STRENGTH_1 = RecipeBase(
    components={composites.TUNGSTEN_CARBIDE: 1, RefinedResource.CERAMIC: 1}
)

DRILL_STRENGTH_2 = RecipeBase(
    components={composites.TUNGSTEN_CARBIDE: 1, composites.TITANIUM_ALLOY: 1}
)

DRILL_STRENGTH_3 = RecipeBase(components={composites.DIAMOND: 1, composites.TITANIUM_ALLOY: 1})

RTG = RecipeBase(components={NaturalResource.LITHIUM: 1, composites.NANOCARBON_ALLOY: 1})

MEDIUM_CANISTER = RecipeBase(components={composites.PLASTIC: 1, RefinedResource.GLASS: 1})

PAVER = RecipeBase(components={composites.ALUMINUM_ALLOY: 1, composites.SILICONE: 1})
