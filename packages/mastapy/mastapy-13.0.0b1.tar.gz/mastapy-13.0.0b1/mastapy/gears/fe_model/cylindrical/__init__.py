"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1199 import CylindricalGearFEModel
    from ._1200 import CylindricalGearMeshFEModel
    from ._1201 import CylindricalGearSetFEModel
else:
    import_structure = {
        "_1199": ["CylindricalGearFEModel"],
        "_1200": ["CylindricalGearMeshFEModel"],
        "_1201": ["CylindricalGearSetFEModel"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearFEModel",
    "CylindricalGearMeshFEModel",
    "CylindricalGearSetFEModel",
)
