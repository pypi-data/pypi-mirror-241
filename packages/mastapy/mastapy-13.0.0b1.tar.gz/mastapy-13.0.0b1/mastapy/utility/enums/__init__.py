"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1817 import BearingForceArrowOption
    from ._1818 import TableAndChartOptions
    from ._1819 import ThreeDViewContourOption
    from ._1820 import ThreeDViewContourOptionFirstSelection
    from ._1821 import ThreeDViewContourOptionSecondSelection
else:
    import_structure = {
        "_1817": ["BearingForceArrowOption"],
        "_1818": ["TableAndChartOptions"],
        "_1819": ["ThreeDViewContourOption"],
        "_1820": ["ThreeDViewContourOptionFirstSelection"],
        "_1821": ["ThreeDViewContourOptionSecondSelection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BearingForceArrowOption",
    "TableAndChartOptions",
    "ThreeDViewContourOption",
    "ThreeDViewContourOptionFirstSelection",
    "ThreeDViewContourOptionSecondSelection",
)
