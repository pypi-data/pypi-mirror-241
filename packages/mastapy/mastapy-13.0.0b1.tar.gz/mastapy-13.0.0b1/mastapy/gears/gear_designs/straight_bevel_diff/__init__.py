"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._963 import StraightBevelDiffGearDesign
    from ._964 import StraightBevelDiffGearMeshDesign
    from ._965 import StraightBevelDiffGearSetDesign
    from ._966 import StraightBevelDiffMeshedGearDesign
else:
    import_structure = {
        "_963": ["StraightBevelDiffGearDesign"],
        "_964": ["StraightBevelDiffGearMeshDesign"],
        "_965": ["StraightBevelDiffGearSetDesign"],
        "_966": ["StraightBevelDiffMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "StraightBevelDiffGearDesign",
    "StraightBevelDiffGearMeshDesign",
    "StraightBevelDiffGearSetDesign",
    "StraightBevelDiffMeshedGearDesign",
)
