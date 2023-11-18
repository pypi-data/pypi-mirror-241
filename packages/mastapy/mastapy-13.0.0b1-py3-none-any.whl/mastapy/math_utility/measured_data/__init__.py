"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1563 import GriddedSurfaceAccessor
    from ._1564 import LookupTableBase
    from ._1565 import OnedimensionalFunctionLookupTable
    from ._1566 import TwodimensionalFunctionLookupTable
else:
    import_structure = {
        "_1563": ["GriddedSurfaceAccessor"],
        "_1564": ["LookupTableBase"],
        "_1565": ["OnedimensionalFunctionLookupTable"],
        "_1566": ["TwodimensionalFunctionLookupTable"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "GriddedSurfaceAccessor",
    "LookupTableBase",
    "OnedimensionalFunctionLookupTable",
    "TwodimensionalFunctionLookupTable",
)
