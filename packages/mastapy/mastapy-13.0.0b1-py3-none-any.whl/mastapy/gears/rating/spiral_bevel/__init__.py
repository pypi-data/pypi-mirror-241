"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._400 import SpiralBevelGearMeshRating
    from ._401 import SpiralBevelGearRating
    from ._402 import SpiralBevelGearSetRating
else:
    import_structure = {
        "_400": ["SpiralBevelGearMeshRating"],
        "_401": ["SpiralBevelGearRating"],
        "_402": ["SpiralBevelGearSetRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "SpiralBevelGearMeshRating",
    "SpiralBevelGearRating",
    "SpiralBevelGearSetRating",
)
