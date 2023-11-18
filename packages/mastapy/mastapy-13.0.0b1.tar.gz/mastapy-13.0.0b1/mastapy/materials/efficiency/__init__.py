"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._290 import BearingEfficiencyRatingMethod
    from ._291 import CombinedResistiveTorque
    from ._292 import EfficiencyRatingMethod
    from ._293 import IndependentPowerLoss
    from ._294 import IndependentResistiveTorque
    from ._295 import LoadAndSpeedCombinedPowerLoss
    from ._296 import OilPumpDetail
    from ._297 import OilPumpDriveType
    from ._298 import OilSealLossCalculationMethod
    from ._299 import OilSealMaterialType
    from ._300 import PowerLoss
    from ._301 import ResistiveTorque
else:
    import_structure = {
        "_290": ["BearingEfficiencyRatingMethod"],
        "_291": ["CombinedResistiveTorque"],
        "_292": ["EfficiencyRatingMethod"],
        "_293": ["IndependentPowerLoss"],
        "_294": ["IndependentResistiveTorque"],
        "_295": ["LoadAndSpeedCombinedPowerLoss"],
        "_296": ["OilPumpDetail"],
        "_297": ["OilPumpDriveType"],
        "_298": ["OilSealLossCalculationMethod"],
        "_299": ["OilSealMaterialType"],
        "_300": ["PowerLoss"],
        "_301": ["ResistiveTorque"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BearingEfficiencyRatingMethod",
    "CombinedResistiveTorque",
    "EfficiencyRatingMethod",
    "IndependentPowerLoss",
    "IndependentResistiveTorque",
    "LoadAndSpeedCombinedPowerLoss",
    "OilPumpDetail",
    "OilPumpDriveType",
    "OilSealLossCalculationMethod",
    "OilSealMaterialType",
    "PowerLoss",
    "ResistiveTorque",
)
