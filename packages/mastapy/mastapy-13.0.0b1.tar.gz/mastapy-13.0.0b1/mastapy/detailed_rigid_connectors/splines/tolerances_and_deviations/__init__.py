"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1418 import FitAndTolerance
    from ._1419 import SAESplineTolerances
else:
    import_structure = {
        "_1418": ["FitAndTolerance"],
        "_1419": ["SAESplineTolerances"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "FitAndTolerance",
    "SAESplineTolerances",
)
