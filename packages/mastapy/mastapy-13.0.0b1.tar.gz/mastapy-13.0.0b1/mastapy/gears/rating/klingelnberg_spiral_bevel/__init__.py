"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._403 import KlingelnbergCycloPalloidSpiralBevelGearMeshRating
    from ._404 import KlingelnbergCycloPalloidSpiralBevelGearRating
    from ._405 import KlingelnbergCycloPalloidSpiralBevelGearSetRating
else:
    import_structure = {
        "_403": ["KlingelnbergCycloPalloidSpiralBevelGearMeshRating"],
        "_404": ["KlingelnbergCycloPalloidSpiralBevelGearRating"],
        "_405": ["KlingelnbergCycloPalloidSpiralBevelGearSetRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KlingelnbergCycloPalloidSpiralBevelGearMeshRating",
    "KlingelnbergCycloPalloidSpiralBevelGearRating",
    "KlingelnbergCycloPalloidSpiralBevelGearSetRating",
)
