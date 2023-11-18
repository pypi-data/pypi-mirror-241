"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._967 import SpiralBevelGearDesign
    from ._968 import SpiralBevelGearMeshDesign
    from ._969 import SpiralBevelGearSetDesign
    from ._970 import SpiralBevelMeshedGearDesign
else:
    import_structure = {
        "_967": ["SpiralBevelGearDesign"],
        "_968": ["SpiralBevelGearMeshDesign"],
        "_969": ["SpiralBevelGearSetDesign"],
        "_970": ["SpiralBevelMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "SpiralBevelGearDesign",
    "SpiralBevelGearMeshDesign",
    "SpiralBevelGearSetDesign",
    "SpiralBevelMeshedGearDesign",
)
