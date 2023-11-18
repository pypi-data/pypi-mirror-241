"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._499 import CylindricalGearSetRatingOptimisationHelper
    from ._500 import OptimisationResultsPair
    from ._501 import SafetyFactorOptimisationResults
    from ._502 import SafetyFactorOptimisationStepResult
    from ._503 import SafetyFactorOptimisationStepResultAngle
    from ._504 import SafetyFactorOptimisationStepResultNumber
    from ._505 import SafetyFactorOptimisationStepResultShortLength
else:
    import_structure = {
        "_499": ["CylindricalGearSetRatingOptimisationHelper"],
        "_500": ["OptimisationResultsPair"],
        "_501": ["SafetyFactorOptimisationResults"],
        "_502": ["SafetyFactorOptimisationStepResult"],
        "_503": ["SafetyFactorOptimisationStepResultAngle"],
        "_504": ["SafetyFactorOptimisationStepResultNumber"],
        "_505": ["SafetyFactorOptimisationStepResultShortLength"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearSetRatingOptimisationHelper",
    "OptimisationResultsPair",
    "SafetyFactorOptimisationResults",
    "SafetyFactorOptimisationStepResult",
    "SafetyFactorOptimisationStepResultAngle",
    "SafetyFactorOptimisationStepResultNumber",
    "SafetyFactorOptimisationStepResultShortLength",
)
