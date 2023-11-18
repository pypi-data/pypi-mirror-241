"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1206 import CylindricalGearLTCAContactChartDataAsTextFile
    from ._1207 import CylindricalGearLTCAContactCharts
    from ._1208 import CylindricalGearWorstLTCAContactChartDataAsTextFile
    from ._1209 import CylindricalGearWorstLTCAContactCharts
    from ._1210 import GearLTCAContactChartDataAsTextFile
    from ._1211 import GearLTCAContactCharts
    from ._1212 import PointsWithWorstResults
else:
    import_structure = {
        "_1206": ["CylindricalGearLTCAContactChartDataAsTextFile"],
        "_1207": ["CylindricalGearLTCAContactCharts"],
        "_1208": ["CylindricalGearWorstLTCAContactChartDataAsTextFile"],
        "_1209": ["CylindricalGearWorstLTCAContactCharts"],
        "_1210": ["GearLTCAContactChartDataAsTextFile"],
        "_1211": ["GearLTCAContactCharts"],
        "_1212": ["PointsWithWorstResults"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearLTCAContactChartDataAsTextFile",
    "CylindricalGearLTCAContactCharts",
    "CylindricalGearWorstLTCAContactChartDataAsTextFile",
    "CylindricalGearWorstLTCAContactCharts",
    "GearLTCAContactChartDataAsTextFile",
    "GearLTCAContactCharts",
    "PointsWithWorstResults",
)
