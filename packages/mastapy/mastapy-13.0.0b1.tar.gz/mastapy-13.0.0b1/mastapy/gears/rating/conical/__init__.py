"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._536 import ConicalGearDutyCycleRating
    from ._537 import ConicalGearMeshRating
    from ._538 import ConicalGearRating
    from ._539 import ConicalGearSetDutyCycleRating
    from ._540 import ConicalGearSetRating
    from ._541 import ConicalGearSingleFlankRating
    from ._542 import ConicalMeshDutyCycleRating
    from ._543 import ConicalMeshedGearRating
    from ._544 import ConicalMeshSingleFlankRating
    from ._545 import ConicalRateableMesh
else:
    import_structure = {
        "_536": ["ConicalGearDutyCycleRating"],
        "_537": ["ConicalGearMeshRating"],
        "_538": ["ConicalGearRating"],
        "_539": ["ConicalGearSetDutyCycleRating"],
        "_540": ["ConicalGearSetRating"],
        "_541": ["ConicalGearSingleFlankRating"],
        "_542": ["ConicalMeshDutyCycleRating"],
        "_543": ["ConicalMeshedGearRating"],
        "_544": ["ConicalMeshSingleFlankRating"],
        "_545": ["ConicalRateableMesh"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConicalGearDutyCycleRating",
    "ConicalGearMeshRating",
    "ConicalGearRating",
    "ConicalGearSetDutyCycleRating",
    "ConicalGearSetRating",
    "ConicalGearSingleFlankRating",
    "ConicalMeshDutyCycleRating",
    "ConicalMeshedGearRating",
    "ConicalMeshSingleFlankRating",
    "ConicalRateableMesh",
)
