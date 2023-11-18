"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._971 import KlingelnbergCycloPalloidSpiralBevelGearDesign
    from ._972 import KlingelnbergCycloPalloidSpiralBevelGearMeshDesign
    from ._973 import KlingelnbergCycloPalloidSpiralBevelGearSetDesign
    from ._974 import KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign
else:
    import_structure = {
        "_971": ["KlingelnbergCycloPalloidSpiralBevelGearDesign"],
        "_972": ["KlingelnbergCycloPalloidSpiralBevelGearMeshDesign"],
        "_973": ["KlingelnbergCycloPalloidSpiralBevelGearSetDesign"],
        "_974": ["KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KlingelnbergCycloPalloidSpiralBevelGearDesign",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshDesign",
    "KlingelnbergCycloPalloidSpiralBevelGearSetDesign",
    "KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign",
)
