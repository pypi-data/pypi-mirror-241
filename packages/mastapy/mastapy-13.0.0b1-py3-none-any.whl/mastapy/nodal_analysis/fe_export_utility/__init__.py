"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._165 import BoundaryConditionType
    from ._166 import FEExportFormat
else:
    import_structure = {
        "_165": ["BoundaryConditionType"],
        "_166": ["FEExportFormat"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BoundaryConditionType",
    "FEExportFormat",
)
