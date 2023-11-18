"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._959 import StraightBevelGearDesign
    from ._960 import StraightBevelGearMeshDesign
    from ._961 import StraightBevelGearSetDesign
    from ._962 import StraightBevelMeshedGearDesign
else:
    import_structure = {
        "_959": ["StraightBevelGearDesign"],
        "_960": ["StraightBevelGearMeshDesign"],
        "_961": ["StraightBevelGearSetDesign"],
        "_962": ["StraightBevelMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "StraightBevelGearDesign",
    "StraightBevelGearMeshDesign",
    "StraightBevelGearSetDesign",
    "StraightBevelMeshedGearDesign",
)
