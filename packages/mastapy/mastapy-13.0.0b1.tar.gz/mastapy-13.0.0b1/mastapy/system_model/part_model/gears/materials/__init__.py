"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2564 import GearMaterialExpertSystemMaterialDetails
    from ._2565 import GearMaterialExpertSystemMaterialOptions
else:
    import_structure = {
        "_2564": ["GearMaterialExpertSystemMaterialDetails"],
        "_2565": ["GearMaterialExpertSystemMaterialOptions"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "GearMaterialExpertSystemMaterialDetails",
    "GearMaterialExpertSystemMaterialOptions",
)
