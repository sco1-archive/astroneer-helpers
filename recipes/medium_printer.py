from recipes.helpers import RecipeBase
from recipes.resources import RefinedResource


MEDIUM_PRINTER_RECIPES = {
    "CRANE": RecipeBase(components={"STEEL": 1, "SILICONE": 1, RefinedResource.TITANIUM: 1},),
    "LARGE_STORAGE": RecipeBase(components={RefinedResource.CERAMIC: 3}),
}
