"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._488 import MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating
    from ._489 import PlasticGearVDI2736AbstractGearSingleFlankRating
    from ._490 import PlasticGearVDI2736AbstractMeshSingleFlankRating
    from ._491 import PlasticGearVDI2736AbstractRateableMesh
    from ._492 import PlasticPlasticVDI2736MeshSingleFlankRating
    from ._493 import PlasticSNCurveForTheSpecifiedOperatingConditions
    from ._494 import (
        PlasticVDI2736GearSingleFlankRatingInAMetalPlasticOrAPlasticMetalMesh,
    )
    from ._495 import PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh
    from ._496 import VDI2736MetalPlasticRateableMesh
    from ._497 import VDI2736PlasticMetalRateableMesh
    from ._498 import VDI2736PlasticPlasticRateableMesh
else:
    import_structure = {
        "_488": ["MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating"],
        "_489": ["PlasticGearVDI2736AbstractGearSingleFlankRating"],
        "_490": ["PlasticGearVDI2736AbstractMeshSingleFlankRating"],
        "_491": ["PlasticGearVDI2736AbstractRateableMesh"],
        "_492": ["PlasticPlasticVDI2736MeshSingleFlankRating"],
        "_493": ["PlasticSNCurveForTheSpecifiedOperatingConditions"],
        "_494": [
            "PlasticVDI2736GearSingleFlankRatingInAMetalPlasticOrAPlasticMetalMesh"
        ],
        "_495": ["PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh"],
        "_496": ["VDI2736MetalPlasticRateableMesh"],
        "_497": ["VDI2736PlasticMetalRateableMesh"],
        "_498": ["VDI2736PlasticPlasticRateableMesh"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating",
    "PlasticGearVDI2736AbstractGearSingleFlankRating",
    "PlasticGearVDI2736AbstractMeshSingleFlankRating",
    "PlasticGearVDI2736AbstractRateableMesh",
    "PlasticPlasticVDI2736MeshSingleFlankRating",
    "PlasticSNCurveForTheSpecifiedOperatingConditions",
    "PlasticVDI2736GearSingleFlankRatingInAMetalPlasticOrAPlasticMetalMesh",
    "PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh",
    "VDI2736MetalPlasticRateableMesh",
    "VDI2736PlasticMetalRateableMesh",
    "VDI2736PlasticPlasticRateableMesh",
)
