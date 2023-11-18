"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._409 import KlingelnbergCycloPalloidConicalGearMeshRating
    from ._410 import KlingelnbergCycloPalloidConicalGearRating
    from ._411 import KlingelnbergCycloPalloidConicalGearSetRating
else:
    import_structure = {
        "_409": ["KlingelnbergCycloPalloidConicalGearMeshRating"],
        "_410": ["KlingelnbergCycloPalloidConicalGearRating"],
        "_411": ["KlingelnbergCycloPalloidConicalGearSetRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KlingelnbergCycloPalloidConicalGearMeshRating",
    "KlingelnbergCycloPalloidConicalGearRating",
    "KlingelnbergCycloPalloidConicalGearSetRating",
)
