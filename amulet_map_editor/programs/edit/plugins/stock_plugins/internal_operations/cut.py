from typing import TYPE_CHECKING

from amulet.api.structure import structure_cache
from amulet.api.data_types import Dimension, OperationReturnType
from amulet.api.selection import SelectionGroup
from amulet_map_editor.programs.edit.plugins.stock_plugins.internal_operations.delete import (
    delete,
)
from amulet_map_editor.programs.edit.plugins.api.errors import OperationError

if TYPE_CHECKING:
    from amulet.api.level import World


def cut(
    world: "World", dimension: Dimension, selection: SelectionGroup
) -> OperationReturnType:
    if selection:
        structure = world.extract_structure(selection, dimension)
        structure_cache.add_structure(structure, structure.dimensions[0])
        yield from delete(
            world,
            dimension,
            selection,
        )
    else:
        raise OperationError(
            "At least one selection is required for the copy operation."
        )
