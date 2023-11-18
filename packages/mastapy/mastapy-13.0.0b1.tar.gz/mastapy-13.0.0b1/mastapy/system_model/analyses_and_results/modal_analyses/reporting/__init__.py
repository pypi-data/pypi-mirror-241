"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4713 import CalculateFullFEResultsForMode
    from ._4714 import CampbellDiagramReport
    from ._4715 import ComponentPerModeResult
    from ._4716 import DesignEntityModalAnalysisGroupResults
    from ._4717 import ModalCMSResultsForModeAndFE
    from ._4718 import PerModeResultsReport
    from ._4719 import RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis
    from ._4720 import RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis
    from ._4721 import RigidlyConnectedDesignEntityGroupModalAnalysis
    from ._4722 import ShaftPerModeResult
    from ._4723 import SingleExcitationResultsModalAnalysis
    from ._4724 import SingleModeResults
else:
    import_structure = {
        "_4713": ["CalculateFullFEResultsForMode"],
        "_4714": ["CampbellDiagramReport"],
        "_4715": ["ComponentPerModeResult"],
        "_4716": ["DesignEntityModalAnalysisGroupResults"],
        "_4717": ["ModalCMSResultsForModeAndFE"],
        "_4718": ["PerModeResultsReport"],
        "_4719": ["RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis"],
        "_4720": ["RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis"],
        "_4721": ["RigidlyConnectedDesignEntityGroupModalAnalysis"],
        "_4722": ["ShaftPerModeResult"],
        "_4723": ["SingleExcitationResultsModalAnalysis"],
        "_4724": ["SingleModeResults"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CalculateFullFEResultsForMode",
    "CampbellDiagramReport",
    "ComponentPerModeResult",
    "DesignEntityModalAnalysisGroupResults",
    "ModalCMSResultsForModeAndFE",
    "PerModeResultsReport",
    "RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis",
    "RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis",
    "RigidlyConnectedDesignEntityGroupModalAnalysis",
    "ShaftPerModeResult",
    "SingleExcitationResultsModalAnalysis",
    "SingleModeResults",
)
