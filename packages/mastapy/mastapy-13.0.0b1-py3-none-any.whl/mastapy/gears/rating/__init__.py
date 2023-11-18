"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._351 import AbstractGearMeshRating
    from ._352 import AbstractGearRating
    from ._353 import AbstractGearSetRating
    from ._354 import BendingAndContactReportingObject
    from ._355 import FlankLoadingState
    from ._356 import GearDutyCycleRating
    from ._357 import GearFlankRating
    from ._358 import GearMeshRating
    from ._359 import GearRating
    from ._360 import GearSetDutyCycleRating
    from ._361 import GearSetRating
    from ._362 import GearSingleFlankRating
    from ._363 import MeshDutyCycleRating
    from ._364 import MeshSingleFlankRating
    from ._365 import RateableMesh
    from ._366 import SafetyFactorResults
else:
    import_structure = {
        "_351": ["AbstractGearMeshRating"],
        "_352": ["AbstractGearRating"],
        "_353": ["AbstractGearSetRating"],
        "_354": ["BendingAndContactReportingObject"],
        "_355": ["FlankLoadingState"],
        "_356": ["GearDutyCycleRating"],
        "_357": ["GearFlankRating"],
        "_358": ["GearMeshRating"],
        "_359": ["GearRating"],
        "_360": ["GearSetDutyCycleRating"],
        "_361": ["GearSetRating"],
        "_362": ["GearSingleFlankRating"],
        "_363": ["MeshDutyCycleRating"],
        "_364": ["MeshSingleFlankRating"],
        "_365": ["RateableMesh"],
        "_366": ["SafetyFactorResults"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractGearMeshRating",
    "AbstractGearRating",
    "AbstractGearSetRating",
    "BendingAndContactReportingObject",
    "FlankLoadingState",
    "GearDutyCycleRating",
    "GearFlankRating",
    "GearMeshRating",
    "GearRating",
    "GearSetDutyCycleRating",
    "GearSetRating",
    "GearSingleFlankRating",
    "MeshDutyCycleRating",
    "MeshSingleFlankRating",
    "RateableMesh",
    "SafetyFactorResults",
)
