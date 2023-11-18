"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._861 import ConicalGearBendingStiffness
    from ._862 import ConicalGearBendingStiffnessNode
    from ._863 import ConicalGearContactStiffness
    from ._864 import ConicalGearContactStiffnessNode
    from ._865 import ConicalGearLoadDistributionAnalysis
    from ._866 import ConicalGearSetLoadDistributionAnalysis
    from ._867 import ConicalMeshedGearLoadDistributionAnalysis
    from ._868 import ConicalMeshLoadDistributionAnalysis
    from ._869 import ConicalMeshLoadDistributionAtRotation
    from ._870 import ConicalMeshLoadedContactLine
else:
    import_structure = {
        "_861": ["ConicalGearBendingStiffness"],
        "_862": ["ConicalGearBendingStiffnessNode"],
        "_863": ["ConicalGearContactStiffness"],
        "_864": ["ConicalGearContactStiffnessNode"],
        "_865": ["ConicalGearLoadDistributionAnalysis"],
        "_866": ["ConicalGearSetLoadDistributionAnalysis"],
        "_867": ["ConicalMeshedGearLoadDistributionAnalysis"],
        "_868": ["ConicalMeshLoadDistributionAnalysis"],
        "_869": ["ConicalMeshLoadDistributionAtRotation"],
        "_870": ["ConicalMeshLoadedContactLine"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConicalGearBendingStiffness",
    "ConicalGearBendingStiffnessNode",
    "ConicalGearContactStiffness",
    "ConicalGearContactStiffnessNode",
    "ConicalGearLoadDistributionAnalysis",
    "ConicalGearSetLoadDistributionAnalysis",
    "ConicalMeshedGearLoadDistributionAnalysis",
    "ConicalMeshLoadDistributionAnalysis",
    "ConicalMeshLoadDistributionAtRotation",
    "ConicalMeshLoadedContactLine",
)
