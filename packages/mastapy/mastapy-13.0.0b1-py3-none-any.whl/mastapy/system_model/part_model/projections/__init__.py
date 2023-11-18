"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2482 import SpecifiedConcentricPartGroupDrawingOrder
    from ._2483 import SpecifiedParallelPartGroupDrawingOrder
else:
    import_structure = {
        "_2482": ["SpecifiedConcentricPartGroupDrawingOrder"],
        "_2483": ["SpecifiedParallelPartGroupDrawingOrder"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "SpecifiedConcentricPartGroupDrawingOrder",
    "SpecifiedParallelPartGroupDrawingOrder",
)
