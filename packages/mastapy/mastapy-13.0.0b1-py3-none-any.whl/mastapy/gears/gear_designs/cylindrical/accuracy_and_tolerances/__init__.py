"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1130 import AGMA2000A88AccuracyGrader
    from ._1131 import AGMA20151A01AccuracyGrader
    from ._1132 import AGMA20151AccuracyGrades
    from ._1133 import AGMAISO13281B14AccuracyGrader
    from ._1134 import CylindricalAccuracyGrader
    from ._1135 import CylindricalAccuracyGraderWithProfileFormAndSlope
    from ._1136 import CylindricalAccuracyGrades
    from ._1137 import CylindricalGearAccuracyTolerances
    from ._1138 import DIN3967SystemOfGearFits
    from ._1139 import ISO132811995AccuracyGrader
    from ._1140 import ISO132812013AccuracyGrader
    from ._1141 import ISO1328AccuracyGraderCommon
    from ._1142 import ISO1328AccuracyGrades
    from ._1143 import OverridableTolerance
else:
    import_structure = {
        "_1130": ["AGMA2000A88AccuracyGrader"],
        "_1131": ["AGMA20151A01AccuracyGrader"],
        "_1132": ["AGMA20151AccuracyGrades"],
        "_1133": ["AGMAISO13281B14AccuracyGrader"],
        "_1134": ["CylindricalAccuracyGrader"],
        "_1135": ["CylindricalAccuracyGraderWithProfileFormAndSlope"],
        "_1136": ["CylindricalAccuracyGrades"],
        "_1137": ["CylindricalGearAccuracyTolerances"],
        "_1138": ["DIN3967SystemOfGearFits"],
        "_1139": ["ISO132811995AccuracyGrader"],
        "_1140": ["ISO132812013AccuracyGrader"],
        "_1141": ["ISO1328AccuracyGraderCommon"],
        "_1142": ["ISO1328AccuracyGrades"],
        "_1143": ["OverridableTolerance"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMA2000A88AccuracyGrader",
    "AGMA20151A01AccuracyGrader",
    "AGMA20151AccuracyGrades",
    "AGMAISO13281B14AccuracyGrader",
    "CylindricalAccuracyGrader",
    "CylindricalAccuracyGraderWithProfileFormAndSlope",
    "CylindricalAccuracyGrades",
    "CylindricalGearAccuracyTolerances",
    "DIN3967SystemOfGearFits",
    "ISO132811995AccuracyGrader",
    "ISO132812013AccuracyGrader",
    "ISO1328AccuracyGraderCommon",
    "ISO1328AccuracyGrades",
    "OverridableTolerance",
)
