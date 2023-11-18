"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1845 import ColumnInputOptions
    from ._1846 import DataInputFileOptions
    from ._1847 import DataLoggerItem
    from ._1848 import DataLoggerWithCharts
    from ._1849 import ScalingDrawStyle
else:
    import_structure = {
        "_1845": ["ColumnInputOptions"],
        "_1846": ["DataInputFileOptions"],
        "_1847": ["DataLoggerItem"],
        "_1848": ["DataLoggerWithCharts"],
        "_1849": ["ScalingDrawStyle"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ColumnInputOptions",
    "DataInputFileOptions",
    "DataLoggerItem",
    "DataLoggerWithCharts",
    "ScalingDrawStyle",
)
