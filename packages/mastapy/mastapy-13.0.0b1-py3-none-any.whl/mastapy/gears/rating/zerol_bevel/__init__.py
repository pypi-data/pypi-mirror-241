"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._367 import ZerolBevelGearMeshRating
    from ._368 import ZerolBevelGearRating
    from ._369 import ZerolBevelGearSetRating
else:
    import_structure = {
        "_367": ["ZerolBevelGearMeshRating"],
        "_368": ["ZerolBevelGearRating"],
        "_369": ["ZerolBevelGearSetRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ZerolBevelGearMeshRating",
    "ZerolBevelGearRating",
    "ZerolBevelGearSetRating",
)
