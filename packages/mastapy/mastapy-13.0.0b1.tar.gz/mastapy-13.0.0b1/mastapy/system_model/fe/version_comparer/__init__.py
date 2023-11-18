"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2410 import DesignResults
    from ._2411 import FESubstructureResults
    from ._2412 import FESubstructureVersionComparer
    from ._2413 import LoadCaseResults
    from ._2414 import LoadCasesToRun
    from ._2415 import NodeComparisonResult
else:
    import_structure = {
        "_2410": ["DesignResults"],
        "_2411": ["FESubstructureResults"],
        "_2412": ["FESubstructureVersionComparer"],
        "_2413": ["LoadCaseResults"],
        "_2414": ["LoadCasesToRun"],
        "_2415": ["NodeComparisonResult"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DesignResults",
    "FESubstructureResults",
    "FESubstructureVersionComparer",
    "LoadCaseResults",
    "LoadCasesToRun",
    "NodeComparisonResult",
)
