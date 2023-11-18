"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1202 import ConicalGearFEModel
    from ._1203 import ConicalMeshFEModel
    from ._1204 import ConicalSetFEModel
    from ._1205 import FlankDataSource
else:
    import_structure = {
        "_1202": ["ConicalGearFEModel"],
        "_1203": ["ConicalMeshFEModel"],
        "_1204": ["ConicalSetFEModel"],
        "_1205": ["FlankDataSource"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConicalGearFEModel",
    "ConicalMeshFEModel",
    "ConicalSetFEModel",
    "FlankDataSource",
)
