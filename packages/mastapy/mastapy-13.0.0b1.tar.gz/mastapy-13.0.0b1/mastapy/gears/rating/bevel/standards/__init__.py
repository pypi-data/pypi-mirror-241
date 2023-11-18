"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._555 import AGMASpiralBevelGearSingleFlankRating
    from ._556 import AGMASpiralBevelMeshSingleFlankRating
    from ._557 import GleasonSpiralBevelGearSingleFlankRating
    from ._558 import GleasonSpiralBevelMeshSingleFlankRating
    from ._559 import SpiralBevelGearSingleFlankRating
    from ._560 import SpiralBevelMeshSingleFlankRating
    from ._561 import SpiralBevelRateableGear
    from ._562 import SpiralBevelRateableMesh
else:
    import_structure = {
        "_555": ["AGMASpiralBevelGearSingleFlankRating"],
        "_556": ["AGMASpiralBevelMeshSingleFlankRating"],
        "_557": ["GleasonSpiralBevelGearSingleFlankRating"],
        "_558": ["GleasonSpiralBevelMeshSingleFlankRating"],
        "_559": ["SpiralBevelGearSingleFlankRating"],
        "_560": ["SpiralBevelMeshSingleFlankRating"],
        "_561": ["SpiralBevelRateableGear"],
        "_562": ["SpiralBevelRateableMesh"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMASpiralBevelGearSingleFlankRating",
    "AGMASpiralBevelMeshSingleFlankRating",
    "GleasonSpiralBevelGearSingleFlankRating",
    "GleasonSpiralBevelMeshSingleFlankRating",
    "SpiralBevelGearSingleFlankRating",
    "SpiralBevelMeshSingleFlankRating",
    "SpiralBevelRateableGear",
    "SpiralBevelRateableMesh",
)
