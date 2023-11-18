"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._393 import StraightBevelGearMeshRating
    from ._394 import StraightBevelGearRating
    from ._395 import StraightBevelGearSetRating
else:
    import_structure = {
        "_393": ["StraightBevelGearMeshRating"],
        "_394": ["StraightBevelGearRating"],
        "_395": ["StraightBevelGearSetRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "StraightBevelGearMeshRating",
    "StraightBevelGearRating",
    "StraightBevelGearSetRating",
)
