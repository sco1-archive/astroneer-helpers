from recipes.helpers import RecipeBase
from recipes.resources import NaturalResource, RefinedResource

SMALL_PRINTER_RECIPES = {
    "DRILL_STRENGTH_1": RecipeBase(components={"TUNGSTEN_CARBIDE": 1, RefinedResource.CERAMIC: 1},),
    "DRILL_STRENGTH_2": RecipeBase(components={"TUNGSTEN_CARBIDE": 1, "TITANIUM_ALLOY": 1},),
    "DRILL_STRENGTH_3": RecipeBase(components={"DIAMOND": 1, "TITANIUM_ALLOY": 1},),
    "MEDIUM_CANISTER": RecipeBase(components={"PLASTIC": 1, RefinedResource.GLASS: 1},),
    "MEDIUM_STORAGE": RecipeBase(components={NaturalResource.RESIN: 2}),
    "MEDIUM_STORAGE_SILO": RecipeBase(components={RefinedResource.TITANIUM: 2}),
    "PAVER": RecipeBase(components={"ALUMINUM_ALLOY": 1, "SILICONE": 1}),
    "ROVER_SEAT": RecipeBase(components={NaturalResource.COMPOUND: 2}),
    "RTG": RecipeBase(components={NaturalResource.LITHIUM: 1, "NANOCARBON_ALLOY": 1}),
}
