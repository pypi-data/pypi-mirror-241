"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2840 import CylindricalGearMeshMisalignmentValue
    from ._2841 import FlexibleGearChart
    from ._2842 import GearInMeshDeflectionResults
    from ._2843 import MeshDeflectionResults
    from ._2844 import PlanetCarrierWindup
    from ._2845 import PlanetPinWindup
    from ._2846 import RigidlyConnectedComponentGroupSystemDeflection
    from ._2847 import ShaftSystemDeflectionSectionsReport
    from ._2848 import SplineFlankContactReporting
else:
    import_structure = {
        "_2840": ["CylindricalGearMeshMisalignmentValue"],
        "_2841": ["FlexibleGearChart"],
        "_2842": ["GearInMeshDeflectionResults"],
        "_2843": ["MeshDeflectionResults"],
        "_2844": ["PlanetCarrierWindup"],
        "_2845": ["PlanetPinWindup"],
        "_2846": ["RigidlyConnectedComponentGroupSystemDeflection"],
        "_2847": ["ShaftSystemDeflectionSectionsReport"],
        "_2848": ["SplineFlankContactReporting"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearMeshMisalignmentValue",
    "FlexibleGearChart",
    "GearInMeshDeflectionResults",
    "MeshDeflectionResults",
    "PlanetCarrierWindup",
    "PlanetPinWindup",
    "RigidlyConnectedComponentGroupSystemDeflection",
    "ShaftSystemDeflectionSectionsReport",
    "SplineFlankContactReporting",
)
