"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1195 import GearFEModel
    from ._1196 import GearMeshFEModel
    from ._1197 import GearMeshingElementOptions
    from ._1198 import GearSetFEModel
else:
    import_structure = {
        "_1195": ["GearFEModel"],
        "_1196": ["GearMeshFEModel"],
        "_1197": ["GearMeshingElementOptions"],
        "_1198": ["GearSetFEModel"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "GearFEModel",
    "GearMeshFEModel",
    "GearMeshingElementOptions",
    "GearSetFEModel",
)
