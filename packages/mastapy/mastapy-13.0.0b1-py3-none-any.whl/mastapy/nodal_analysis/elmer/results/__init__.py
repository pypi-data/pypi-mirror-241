"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._174 import Data
    from ._175 import Data1D
    from ._176 import Data3D
else:
    import_structure = {
        "_174": ["Data"],
        "_175": ["Data1D"],
        "_176": ["Data3D"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Data",
    "Data1D",
    "Data3D",
)
