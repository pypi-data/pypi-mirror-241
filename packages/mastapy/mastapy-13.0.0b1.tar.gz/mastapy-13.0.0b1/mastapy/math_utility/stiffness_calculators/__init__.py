"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1534 import IndividualContactPosition
    from ._1535 import SurfaceToSurfaceContact
else:
    import_structure = {
        "_1534": ["IndividualContactPosition"],
        "_1535": ["SurfaceToSurfaceContact"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "IndividualContactPosition",
    "SurfaceToSurfaceContact",
)
