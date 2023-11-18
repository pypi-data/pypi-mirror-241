"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._396 import StraightBevelDiffGearMeshRating
    from ._397 import StraightBevelDiffGearRating
    from ._398 import StraightBevelDiffGearSetRating
    from ._399 import StraightBevelDiffMeshedGearRating
else:
    import_structure = {
        "_396": ["StraightBevelDiffGearMeshRating"],
        "_397": ["StraightBevelDiffGearRating"],
        "_398": ["StraightBevelDiffGearSetRating"],
        "_399": ["StraightBevelDiffMeshedGearRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "StraightBevelDiffGearMeshRating",
    "StraightBevelDiffGearRating",
    "StraightBevelDiffGearSetRating",
    "StraightBevelDiffMeshedGearRating",
)
