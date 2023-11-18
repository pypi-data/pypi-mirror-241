"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._979 import KlingelnbergConicalGearDesign
    from ._980 import KlingelnbergConicalGearMeshDesign
    from ._981 import KlingelnbergConicalGearSetDesign
    from ._982 import KlingelnbergConicalMeshedGearDesign
else:
    import_structure = {
        "_979": ["KlingelnbergConicalGearDesign"],
        "_980": ["KlingelnbergConicalGearMeshDesign"],
        "_981": ["KlingelnbergConicalGearSetDesign"],
        "_982": ["KlingelnbergConicalMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KlingelnbergConicalGearDesign",
    "KlingelnbergConicalGearMeshDesign",
    "KlingelnbergConicalGearSetDesign",
    "KlingelnbergConicalMeshedGearDesign",
)
