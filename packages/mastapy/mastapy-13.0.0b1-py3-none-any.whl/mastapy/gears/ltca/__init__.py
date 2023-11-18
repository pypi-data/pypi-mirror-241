"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._823 import ConicalGearFilletStressResults
    from ._824 import ConicalGearRootFilletStressResults
    from ._825 import ContactResultType
    from ._826 import CylindricalGearFilletNodeStressResults
    from ._827 import CylindricalGearFilletNodeStressResultsColumn
    from ._828 import CylindricalGearFilletNodeStressResultsRow
    from ._829 import CylindricalGearRootFilletStressResults
    from ._830 import CylindricalMeshedGearLoadDistributionAnalysis
    from ._831 import GearBendingStiffness
    from ._832 import GearBendingStiffnessNode
    from ._833 import GearContactStiffness
    from ._834 import GearContactStiffnessNode
    from ._835 import GearFilletNodeStressResults
    from ._836 import GearFilletNodeStressResultsColumn
    from ._837 import GearFilletNodeStressResultsRow
    from ._838 import GearLoadDistributionAnalysis
    from ._839 import GearMeshLoadDistributionAnalysis
    from ._840 import GearMeshLoadDistributionAtRotation
    from ._841 import GearMeshLoadedContactLine
    from ._842 import GearMeshLoadedContactPoint
    from ._843 import GearRootFilletStressResults
    from ._844 import GearSetLoadDistributionAnalysis
    from ._845 import GearStiffness
    from ._846 import GearStiffnessNode
    from ._847 import MeshedGearLoadDistributionAnalysisAtRotation
    from ._848 import UseAdvancedLTCAOptions
else:
    import_structure = {
        "_823": ["ConicalGearFilletStressResults"],
        "_824": ["ConicalGearRootFilletStressResults"],
        "_825": ["ContactResultType"],
        "_826": ["CylindricalGearFilletNodeStressResults"],
        "_827": ["CylindricalGearFilletNodeStressResultsColumn"],
        "_828": ["CylindricalGearFilletNodeStressResultsRow"],
        "_829": ["CylindricalGearRootFilletStressResults"],
        "_830": ["CylindricalMeshedGearLoadDistributionAnalysis"],
        "_831": ["GearBendingStiffness"],
        "_832": ["GearBendingStiffnessNode"],
        "_833": ["GearContactStiffness"],
        "_834": ["GearContactStiffnessNode"],
        "_835": ["GearFilletNodeStressResults"],
        "_836": ["GearFilletNodeStressResultsColumn"],
        "_837": ["GearFilletNodeStressResultsRow"],
        "_838": ["GearLoadDistributionAnalysis"],
        "_839": ["GearMeshLoadDistributionAnalysis"],
        "_840": ["GearMeshLoadDistributionAtRotation"],
        "_841": ["GearMeshLoadedContactLine"],
        "_842": ["GearMeshLoadedContactPoint"],
        "_843": ["GearRootFilletStressResults"],
        "_844": ["GearSetLoadDistributionAnalysis"],
        "_845": ["GearStiffness"],
        "_846": ["GearStiffnessNode"],
        "_847": ["MeshedGearLoadDistributionAnalysisAtRotation"],
        "_848": ["UseAdvancedLTCAOptions"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConicalGearFilletStressResults",
    "ConicalGearRootFilletStressResults",
    "ContactResultType",
    "CylindricalGearFilletNodeStressResults",
    "CylindricalGearFilletNodeStressResultsColumn",
    "CylindricalGearFilletNodeStressResultsRow",
    "CylindricalGearRootFilletStressResults",
    "CylindricalMeshedGearLoadDistributionAnalysis",
    "GearBendingStiffness",
    "GearBendingStiffnessNode",
    "GearContactStiffness",
    "GearContactStiffnessNode",
    "GearFilletNodeStressResults",
    "GearFilletNodeStressResultsColumn",
    "GearFilletNodeStressResultsRow",
    "GearLoadDistributionAnalysis",
    "GearMeshLoadDistributionAnalysis",
    "GearMeshLoadDistributionAtRotation",
    "GearMeshLoadedContactLine",
    "GearMeshLoadedContactPoint",
    "GearRootFilletStressResults",
    "GearSetLoadDistributionAnalysis",
    "GearStiffness",
    "GearStiffnessNode",
    "MeshedGearLoadDistributionAnalysisAtRotation",
    "UseAdvancedLTCAOptions",
)
