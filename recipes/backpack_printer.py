from recipes.helpers import RecipeBase
from recipes.resources import RefinedResource

BACKPACK_PRINTER_RECIPES = {
    "FLOODLIGHT": RecipeBase(components={RefinedResource.TUNGSTEN: 2}),
}
