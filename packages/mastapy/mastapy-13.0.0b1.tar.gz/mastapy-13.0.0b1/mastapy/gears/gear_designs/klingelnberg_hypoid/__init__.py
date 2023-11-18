"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._975 import KlingelnbergCycloPalloidHypoidGearDesign
    from ._976 import KlingelnbergCycloPalloidHypoidGearMeshDesign
    from ._977 import KlingelnbergCycloPalloidHypoidGearSetDesign
    from ._978 import KlingelnbergCycloPalloidHypoidMeshedGearDesign
else:
    import_structure = {
        "_975": ["KlingelnbergCycloPalloidHypoidGearDesign"],
        "_976": ["KlingelnbergCycloPalloidHypoidGearMeshDesign"],
        "_977": ["KlingelnbergCycloPalloidHypoidGearSetDesign"],
        "_978": ["KlingelnbergCycloPalloidHypoidMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KlingelnbergCycloPalloidHypoidGearDesign",
    "KlingelnbergCycloPalloidHypoidGearMeshDesign",
    "KlingelnbergCycloPalloidHypoidGearSetDesign",
    "KlingelnbergCycloPalloidHypoidMeshedGearDesign",
)
