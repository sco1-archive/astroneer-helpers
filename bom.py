from collections import defaultdict
from typing import Union

from recipes.backpack_printer import BACKPACK_PRINTER_RECIPES
from recipes.composites import COMPOSITE_RECIPES
from recipes.large_printer import LARGE_PRINTER_RECIPES
from recipes.medium_printer import MEDIUM_PRINTER_RECIPES
from recipes.resources import ResourceBase
from recipes.small_printer import SMALL_PRINTER_RECIPES


# Merge all recipes into a super recipe book
ALL_RECIPES = {}
for d in (
    COMPOSITE_RECIPES,
    BACKPACK_PRINTER_RECIPES,
    SMALL_PRINTER_RECIPES,
    MEDIUM_PRINTER_RECIPES,
    LARGE_PRINTER_RECIPES,
):
    ALL_RECIPES.update(d)


def build_bom(build_spec: defaultdict) -> defaultdict:
    """Reduce the provided build specification into the base resources required for construction."""
    while any(
        (iter_part := part)
        for part, quantity in build_spec.items()
        if not isinstance(part, ResourceBase) and quantity > 0
    ):
        part_quantity = build_spec[iter_part]
        for subcomponent, subcomponent_quantity in ALL_RECIPES[iter_part].components.items():
            build_spec[subcomponent] += part_quantity * subcomponent_quantity

        build_spec[iter_part] = 0

    return build_spec


def build_table(build_spec: defaultdict) -> str:
    """Prettyprint the output bill of materials."""
    deconstructed_build = build_bom(build_spec)
    required_materials = sorted(
        [
            (resource.name, quantity)
            for resource, quantity in deconstructed_build.items()
            if quantity > 0
        ],
        key=lambda x: x[0],
    )

    return "\n".join([f"{resource:9}{quantity:>3}" for resource, quantity in required_materials])
