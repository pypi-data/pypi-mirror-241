"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._954 import WormDesign
    from ._955 import WormGearDesign
    from ._956 import WormGearMeshDesign
    from ._957 import WormGearSetDesign
    from ._958 import WormWheelDesign
else:
    import_structure = {
        "_954": ["WormDesign"],
        "_955": ["WormGearDesign"],
        "_956": ["WormGearMeshDesign"],
        "_957": ["WormGearSetDesign"],
        "_958": ["WormWheelDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "WormDesign",
    "WormGearDesign",
    "WormGearMeshDesign",
    "WormGearSetDesign",
    "WormWheelDesign",
)
