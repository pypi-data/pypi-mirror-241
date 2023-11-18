"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._747 import ActiveProfileRangeCalculationSource
    from ._748 import AxialShaverRedressing
    from ._749 import ConventionalShavingDynamics
    from ._750 import ConventionalShavingDynamicsCalculationForDesignedGears
    from ._751 import ConventionalShavingDynamicsCalculationForHobbedGears
    from ._752 import ConventionalShavingDynamicsViewModel
    from ._753 import PlungeShaverDynamics
    from ._754 import PlungeShaverDynamicSettings
    from ._755 import PlungeShaverRedressing
    from ._756 import PlungeShavingDynamicsCalculationForDesignedGears
    from ._757 import PlungeShavingDynamicsCalculationForHobbedGears
    from ._758 import PlungeShavingDynamicsViewModel
    from ._759 import RedressingSettings
    from ._760 import RollAngleRangeRelativeToAccuracy
    from ._761 import RollAngleReportObject
    from ._762 import ShaverRedressing
    from ._763 import ShavingDynamics
    from ._764 import ShavingDynamicsCalculation
    from ._765 import ShavingDynamicsCalculationForDesignedGears
    from ._766 import ShavingDynamicsCalculationForHobbedGears
    from ._767 import ShavingDynamicsConfiguration
    from ._768 import ShavingDynamicsViewModel
    from ._769 import ShavingDynamicsViewModelBase
else:
    import_structure = {
        "_747": ["ActiveProfileRangeCalculationSource"],
        "_748": ["AxialShaverRedressing"],
        "_749": ["ConventionalShavingDynamics"],
        "_750": ["ConventionalShavingDynamicsCalculationForDesignedGears"],
        "_751": ["ConventionalShavingDynamicsCalculationForHobbedGears"],
        "_752": ["ConventionalShavingDynamicsViewModel"],
        "_753": ["PlungeShaverDynamics"],
        "_754": ["PlungeShaverDynamicSettings"],
        "_755": ["PlungeShaverRedressing"],
        "_756": ["PlungeShavingDynamicsCalculationForDesignedGears"],
        "_757": ["PlungeShavingDynamicsCalculationForHobbedGears"],
        "_758": ["PlungeShavingDynamicsViewModel"],
        "_759": ["RedressingSettings"],
        "_760": ["RollAngleRangeRelativeToAccuracy"],
        "_761": ["RollAngleReportObject"],
        "_762": ["ShaverRedressing"],
        "_763": ["ShavingDynamics"],
        "_764": ["ShavingDynamicsCalculation"],
        "_765": ["ShavingDynamicsCalculationForDesignedGears"],
        "_766": ["ShavingDynamicsCalculationForHobbedGears"],
        "_767": ["ShavingDynamicsConfiguration"],
        "_768": ["ShavingDynamicsViewModel"],
        "_769": ["ShavingDynamicsViewModelBase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ActiveProfileRangeCalculationSource",
    "AxialShaverRedressing",
    "ConventionalShavingDynamics",
    "ConventionalShavingDynamicsCalculationForDesignedGears",
    "ConventionalShavingDynamicsCalculationForHobbedGears",
    "ConventionalShavingDynamicsViewModel",
    "PlungeShaverDynamics",
    "PlungeShaverDynamicSettings",
    "PlungeShaverRedressing",
    "PlungeShavingDynamicsCalculationForDesignedGears",
    "PlungeShavingDynamicsCalculationForHobbedGears",
    "PlungeShavingDynamicsViewModel",
    "RedressingSettings",
    "RollAngleRangeRelativeToAccuracy",
    "RollAngleReportObject",
    "ShaverRedressing",
    "ShavingDynamics",
    "ShavingDynamicsCalculation",
    "ShavingDynamicsCalculationForDesignedGears",
    "ShavingDynamicsCalculationForHobbedGears",
    "ShavingDynamicsConfiguration",
    "ShavingDynamicsViewModel",
    "ShavingDynamicsViewModelBase",
)
