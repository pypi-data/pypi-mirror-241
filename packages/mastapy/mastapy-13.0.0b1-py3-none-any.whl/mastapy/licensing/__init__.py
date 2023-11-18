"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1485 import LicenceServer
    from ._7569 import LicenceServerDetails
    from ._7570 import ModuleDetails
    from ._7571 import ModuleLicenceStatus
else:
    import_structure = {
        "_1485": ["LicenceServer"],
        "_7569": ["LicenceServerDetails"],
        "_7570": ["ModuleDetails"],
        "_7571": ["ModuleLicenceStatus"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "LicenceServer",
    "LicenceServerDetails",
    "ModuleDetails",
    "ModuleLicenceStatus",
)
