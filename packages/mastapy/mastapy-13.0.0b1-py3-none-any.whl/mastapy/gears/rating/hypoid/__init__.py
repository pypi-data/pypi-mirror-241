"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._436 import HypoidGearMeshRating
    from ._437 import HypoidGearRating
    from ._438 import HypoidGearSetRating
    from ._439 import HypoidRatingMethod
else:
    import_structure = {
        "_436": ["HypoidGearMeshRating"],
        "_437": ["HypoidGearRating"],
        "_438": ["HypoidGearSetRating"],
        "_439": ["HypoidRatingMethod"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "HypoidGearMeshRating",
    "HypoidGearRating",
    "HypoidGearSetRating",
    "HypoidRatingMethod",
)
