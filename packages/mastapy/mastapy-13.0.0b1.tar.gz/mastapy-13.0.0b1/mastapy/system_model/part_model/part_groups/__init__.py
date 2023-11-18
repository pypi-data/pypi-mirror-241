"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2484 import ConcentricOrParallelPartGroup
    from ._2485 import ConcentricPartGroup
    from ._2486 import ConcentricPartGroupParallelToThis
    from ._2487 import DesignMeasurements
    from ._2488 import ParallelPartGroup
    from ._2489 import ParallelPartGroupSelection
    from ._2490 import PartGroup
else:
    import_structure = {
        "_2484": ["ConcentricOrParallelPartGroup"],
        "_2485": ["ConcentricPartGroup"],
        "_2486": ["ConcentricPartGroupParallelToThis"],
        "_2487": ["DesignMeasurements"],
        "_2488": ["ParallelPartGroup"],
        "_2489": ["ParallelPartGroupSelection"],
        "_2490": ["PartGroup"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConcentricOrParallelPartGroup",
    "ConcentricPartGroup",
    "ConcentricPartGroupParallelToThis",
    "DesignMeasurements",
    "ParallelPartGroup",
    "ParallelPartGroupSelection",
    "PartGroup",
)
