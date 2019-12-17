from recipes import composites
from recipes.helpers import RecipeBase
from recipes.resources import RefinedResource


CRANE = RecipeBase(
    components={composites.STEEL: 1, composites.SILICONE: 1, RefinedResource.TITANIUM: 1}
)


LARGE_STORAGE = RecipeBase(components={RefinedResource.CERAMIC: 3})
