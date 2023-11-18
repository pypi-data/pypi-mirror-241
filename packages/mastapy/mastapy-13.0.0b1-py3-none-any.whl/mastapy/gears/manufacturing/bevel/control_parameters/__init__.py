"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._815 import ConicalGearManufacturingControlParameters
    from ._816 import ConicalManufacturingSGMControlParameters
    from ._817 import ConicalManufacturingSGTControlParameters
    from ._818 import ConicalManufacturingSMTControlParameters
else:
    import_structure = {
        "_815": ["ConicalGearManufacturingControlParameters"],
        "_816": ["ConicalManufacturingSGMControlParameters"],
        "_817": ["ConicalManufacturingSGTControlParameters"],
        "_818": ["ConicalManufacturingSMTControlParameters"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConicalGearManufacturingControlParameters",
    "ConicalManufacturingSGMControlParameters",
    "ConicalManufacturingSGTControlParameters",
    "ConicalManufacturingSMTControlParameters",
)
