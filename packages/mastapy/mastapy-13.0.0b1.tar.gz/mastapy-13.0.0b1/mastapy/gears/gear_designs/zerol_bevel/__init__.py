"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._950 import ZerolBevelGearDesign
    from ._951 import ZerolBevelGearMeshDesign
    from ._952 import ZerolBevelGearSetDesign
    from ._953 import ZerolBevelMeshedGearDesign
else:
    import_structure = {
        "_950": ["ZerolBevelGearDesign"],
        "_951": ["ZerolBevelGearMeshDesign"],
        "_952": ["ZerolBevelGearSetDesign"],
        "_953": ["ZerolBevelMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ZerolBevelGearDesign",
    "ZerolBevelGearMeshDesign",
    "ZerolBevelGearSetDesign",
    "ZerolBevelMeshedGearDesign",
)
