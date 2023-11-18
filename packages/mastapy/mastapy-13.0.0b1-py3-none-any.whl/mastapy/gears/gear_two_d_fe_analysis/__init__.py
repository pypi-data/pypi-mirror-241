"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._892 import CylindricalGearMeshTIFFAnalysis
    from ._893 import CylindricalGearMeshTIFFAnalysisDutyCycle
    from ._894 import CylindricalGearSetTIFFAnalysis
    from ._895 import CylindricalGearSetTIFFAnalysisDutyCycle
    from ._896 import CylindricalGearTIFFAnalysis
    from ._897 import CylindricalGearTIFFAnalysisDutyCycle
    from ._898 import CylindricalGearTwoDimensionalFEAnalysis
    from ._899 import FindleyCriticalPlaneAnalysis
else:
    import_structure = {
        "_892": ["CylindricalGearMeshTIFFAnalysis"],
        "_893": ["CylindricalGearMeshTIFFAnalysisDutyCycle"],
        "_894": ["CylindricalGearSetTIFFAnalysis"],
        "_895": ["CylindricalGearSetTIFFAnalysisDutyCycle"],
        "_896": ["CylindricalGearTIFFAnalysis"],
        "_897": ["CylindricalGearTIFFAnalysisDutyCycle"],
        "_898": ["CylindricalGearTwoDimensionalFEAnalysis"],
        "_899": ["FindleyCriticalPlaneAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearMeshTIFFAnalysis",
    "CylindricalGearMeshTIFFAnalysisDutyCycle",
    "CylindricalGearSetTIFFAnalysis",
    "CylindricalGearSetTIFFAnalysisDutyCycle",
    "CylindricalGearTIFFAnalysis",
    "CylindricalGearTIFFAnalysisDutyCycle",
    "CylindricalGearTwoDimensionalFEAnalysis",
    "FindleyCriticalPlaneAnalysis",
)
