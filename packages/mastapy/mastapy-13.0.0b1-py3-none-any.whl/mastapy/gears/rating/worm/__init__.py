"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._370 import WormGearDutyCycleRating
    from ._371 import WormGearMeshRating
    from ._372 import WormGearRating
    from ._373 import WormGearSetDutyCycleRating
    from ._374 import WormGearSetRating
    from ._375 import WormMeshDutyCycleRating
else:
    import_structure = {
        "_370": ["WormGearDutyCycleRating"],
        "_371": ["WormGearMeshRating"],
        "_372": ["WormGearRating"],
        "_373": ["WormGearSetDutyCycleRating"],
        "_374": ["WormGearSetRating"],
        "_375": ["WormMeshDutyCycleRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "WormGearDutyCycleRating",
    "WormGearMeshRating",
    "WormGearRating",
    "WormGearSetDutyCycleRating",
    "WormGearSetRating",
    "WormMeshDutyCycleRating",
)
