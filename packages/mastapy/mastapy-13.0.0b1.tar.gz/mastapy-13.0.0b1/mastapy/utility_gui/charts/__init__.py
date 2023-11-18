"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1850 import BubbleChartDefinition
    from ._1851 import ConstantLine
    from ._1852 import CustomLineChart
    from ._1853 import CustomTableAndChart
    from ._1854 import LegacyChartMathChartDefinition
    from ._1855 import MatrixVisualisationDefinition
    from ._1856 import ModeConstantLine
    from ._1857 import NDChartDefinition
    from ._1858 import ParallelCoordinatesChartDefinition
    from ._1859 import PointsForSurface
    from ._1860 import ScatterChartDefinition
    from ._1861 import Series2D
    from ._1862 import SMTAxis
    from ._1863 import ThreeDChartDefinition
    from ._1864 import ThreeDVectorChartDefinition
    from ._1865 import TwoDChartDefinition
else:
    import_structure = {
        "_1850": ["BubbleChartDefinition"],
        "_1851": ["ConstantLine"],
        "_1852": ["CustomLineChart"],
        "_1853": ["CustomTableAndChart"],
        "_1854": ["LegacyChartMathChartDefinition"],
        "_1855": ["MatrixVisualisationDefinition"],
        "_1856": ["ModeConstantLine"],
        "_1857": ["NDChartDefinition"],
        "_1858": ["ParallelCoordinatesChartDefinition"],
        "_1859": ["PointsForSurface"],
        "_1860": ["ScatterChartDefinition"],
        "_1861": ["Series2D"],
        "_1862": ["SMTAxis"],
        "_1863": ["ThreeDChartDefinition"],
        "_1864": ["ThreeDVectorChartDefinition"],
        "_1865": ["TwoDChartDefinition"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BubbleChartDefinition",
    "ConstantLine",
    "CustomLineChart",
    "CustomTableAndChart",
    "LegacyChartMathChartDefinition",
    "MatrixVisualisationDefinition",
    "ModeConstantLine",
    "NDChartDefinition",
    "ParallelCoordinatesChartDefinition",
    "PointsForSurface",
    "ScatterChartDefinition",
    "Series2D",
    "SMTAxis",
    "ThreeDChartDefinition",
    "ThreeDVectorChartDefinition",
    "TwoDChartDefinition",
)
