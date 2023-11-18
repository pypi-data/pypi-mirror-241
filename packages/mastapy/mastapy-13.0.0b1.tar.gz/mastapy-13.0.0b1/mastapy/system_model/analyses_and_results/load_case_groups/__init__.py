"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5655 import AbstractDesignStateLoadCaseGroup
    from ._5656 import AbstractLoadCaseGroup
    from ._5657 import AbstractStaticLoadCaseGroup
    from ._5658 import ClutchEngagementStatus
    from ._5659 import ConceptSynchroGearEngagementStatus
    from ._5660 import DesignState
    from ._5661 import DutyCycle
    from ._5662 import GenericClutchEngagementStatus
    from ._5663 import LoadCaseGroupHistograms
    from ._5664 import SubGroupInSingleDesignState
    from ._5665 import SystemOptimisationGearSet
    from ._5666 import SystemOptimiserGearSetOptimisation
    from ._5667 import SystemOptimiserTargets
    from ._5668 import TimeSeriesLoadCaseGroup
else:
    import_structure = {
        "_5655": ["AbstractDesignStateLoadCaseGroup"],
        "_5656": ["AbstractLoadCaseGroup"],
        "_5657": ["AbstractStaticLoadCaseGroup"],
        "_5658": ["ClutchEngagementStatus"],
        "_5659": ["ConceptSynchroGearEngagementStatus"],
        "_5660": ["DesignState"],
        "_5661": ["DutyCycle"],
        "_5662": ["GenericClutchEngagementStatus"],
        "_5663": ["LoadCaseGroupHistograms"],
        "_5664": ["SubGroupInSingleDesignState"],
        "_5665": ["SystemOptimisationGearSet"],
        "_5666": ["SystemOptimiserGearSetOptimisation"],
        "_5667": ["SystemOptimiserTargets"],
        "_5668": ["TimeSeriesLoadCaseGroup"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractDesignStateLoadCaseGroup",
    "AbstractLoadCaseGroup",
    "AbstractStaticLoadCaseGroup",
    "ClutchEngagementStatus",
    "ConceptSynchroGearEngagementStatus",
    "DesignState",
    "DutyCycle",
    "GenericClutchEngagementStatus",
    "LoadCaseGroupHistograms",
    "SubGroupInSingleDesignState",
    "SystemOptimisationGearSet",
    "SystemOptimiserGearSetOptimisation",
    "SystemOptimiserTargets",
    "TimeSeriesLoadCaseGroup",
)
