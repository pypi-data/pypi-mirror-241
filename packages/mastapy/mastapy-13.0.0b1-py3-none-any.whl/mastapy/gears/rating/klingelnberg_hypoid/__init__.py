"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._406 import KlingelnbergCycloPalloidHypoidGearMeshRating
    from ._407 import KlingelnbergCycloPalloidHypoidGearRating
    from ._408 import KlingelnbergCycloPalloidHypoidGearSetRating
else:
    import_structure = {
        "_406": ["KlingelnbergCycloPalloidHypoidGearMeshRating"],
        "_407": ["KlingelnbergCycloPalloidHypoidGearRating"],
        "_408": ["KlingelnbergCycloPalloidHypoidGearSetRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KlingelnbergCycloPalloidHypoidGearMeshRating",
    "KlingelnbergCycloPalloidHypoidGearRating",
    "KlingelnbergCycloPalloidHypoidGearSetRating",
)
