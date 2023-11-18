"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1170 import ConicalGearBiasModification
    from ._1171 import ConicalGearFlankMicroGeometry
    from ._1172 import ConicalGearLeadModification
    from ._1173 import ConicalGearProfileModification
else:
    import_structure = {
        "_1170": ["ConicalGearBiasModification"],
        "_1171": ["ConicalGearFlankMicroGeometry"],
        "_1172": ["ConicalGearLeadModification"],
        "_1173": ["ConicalGearProfileModification"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConicalGearBiasModification",
    "ConicalGearFlankMicroGeometry",
    "ConicalGearLeadModification",
    "ConicalGearProfileModification",
)
