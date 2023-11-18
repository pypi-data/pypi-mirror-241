"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6265 import CombinationAnalysis
    from ._6266 import FlexiblePinAnalysis
    from ._6267 import FlexiblePinAnalysisConceptLevel
    from ._6268 import FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass
    from ._6269 import FlexiblePinAnalysisGearAndBearingRating
    from ._6270 import FlexiblePinAnalysisManufactureLevel
    from ._6271 import FlexiblePinAnalysisOptions
    from ._6272 import FlexiblePinAnalysisStopStartAnalysis
    from ._6273 import WindTurbineCertificationReport
else:
    import_structure = {
        "_6265": ["CombinationAnalysis"],
        "_6266": ["FlexiblePinAnalysis"],
        "_6267": ["FlexiblePinAnalysisConceptLevel"],
        "_6268": ["FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass"],
        "_6269": ["FlexiblePinAnalysisGearAndBearingRating"],
        "_6270": ["FlexiblePinAnalysisManufactureLevel"],
        "_6271": ["FlexiblePinAnalysisOptions"],
        "_6272": ["FlexiblePinAnalysisStopStartAnalysis"],
        "_6273": ["WindTurbineCertificationReport"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CombinationAnalysis",
    "FlexiblePinAnalysis",
    "FlexiblePinAnalysisConceptLevel",
    "FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass",
    "FlexiblePinAnalysisGearAndBearingRating",
    "FlexiblePinAnalysisManufactureLevel",
    "FlexiblePinAnalysisOptions",
    "FlexiblePinAnalysisStopStartAnalysis",
    "WindTurbineCertificationReport",
)
