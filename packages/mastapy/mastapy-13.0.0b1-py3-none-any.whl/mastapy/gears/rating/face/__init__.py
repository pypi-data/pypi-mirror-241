"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._443 import FaceGearDutyCycleRating
    from ._444 import FaceGearMeshDutyCycleRating
    from ._445 import FaceGearMeshRating
    from ._446 import FaceGearRating
    from ._447 import FaceGearSetDutyCycleRating
    from ._448 import FaceGearSetRating
else:
    import_structure = {
        "_443": ["FaceGearDutyCycleRating"],
        "_444": ["FaceGearMeshDutyCycleRating"],
        "_445": ["FaceGearMeshRating"],
        "_446": ["FaceGearRating"],
        "_447": ["FaceGearSetDutyCycleRating"],
        "_448": ["FaceGearSetRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "FaceGearDutyCycleRating",
    "FaceGearMeshDutyCycleRating",
    "FaceGearMeshRating",
    "FaceGearRating",
    "FaceGearSetDutyCycleRating",
    "FaceGearSetRating",
)
