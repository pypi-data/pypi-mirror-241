"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._849 import CylindricalGearBendingStiffness
    from ._850 import CylindricalGearBendingStiffnessNode
    from ._851 import CylindricalGearContactStiffness
    from ._852 import CylindricalGearContactStiffnessNode
    from ._853 import CylindricalGearFESettings
    from ._854 import CylindricalGearLoadDistributionAnalysis
    from ._855 import CylindricalGearMeshLoadDistributionAnalysis
    from ._856 import CylindricalGearMeshLoadedContactLine
    from ._857 import CylindricalGearMeshLoadedContactPoint
    from ._858 import CylindricalGearSetLoadDistributionAnalysis
    from ._859 import CylindricalMeshLoadDistributionAtRotation
    from ._860 import FaceGearSetLoadDistributionAnalysis
else:
    import_structure = {
        "_849": ["CylindricalGearBendingStiffness"],
        "_850": ["CylindricalGearBendingStiffnessNode"],
        "_851": ["CylindricalGearContactStiffness"],
        "_852": ["CylindricalGearContactStiffnessNode"],
        "_853": ["CylindricalGearFESettings"],
        "_854": ["CylindricalGearLoadDistributionAnalysis"],
        "_855": ["CylindricalGearMeshLoadDistributionAnalysis"],
        "_856": ["CylindricalGearMeshLoadedContactLine"],
        "_857": ["CylindricalGearMeshLoadedContactPoint"],
        "_858": ["CylindricalGearSetLoadDistributionAnalysis"],
        "_859": ["CylindricalMeshLoadDistributionAtRotation"],
        "_860": ["FaceGearSetLoadDistributionAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearBendingStiffness",
    "CylindricalGearBendingStiffnessNode",
    "CylindricalGearContactStiffness",
    "CylindricalGearContactStiffnessNode",
    "CylindricalGearFESettings",
    "CylindricalGearLoadDistributionAnalysis",
    "CylindricalGearMeshLoadDistributionAnalysis",
    "CylindricalGearMeshLoadedContactLine",
    "CylindricalGearMeshLoadedContactPoint",
    "CylindricalGearSetLoadDistributionAnalysis",
    "CylindricalMeshLoadDistributionAtRotation",
    "FaceGearSetLoadDistributionAnalysis",
)
