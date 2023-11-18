"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2259 import AdvancedTimeSteppingAnalysisForModulationModeViewOptions
    from ._2260 import ExcitationAnalysisViewOption
    from ._2261 import ModalContributionViewOptions
else:
    import_structure = {
        "_2259": ["AdvancedTimeSteppingAnalysisForModulationModeViewOptions"],
        "_2260": ["ExcitationAnalysisViewOption"],
        "_2261": ["ModalContributionViewOptions"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AdvancedTimeSteppingAnalysisForModulationModeViewOptions",
    "ExcitationAnalysisViewOption",
    "ModalContributionViewOptions",
)
