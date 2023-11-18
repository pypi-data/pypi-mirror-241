"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5525 import DynamicExternalInterfaceOptions
else:
    import_structure = {
        "_5525": ["DynamicExternalInterfaceOptions"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = ("DynamicExternalInterfaceOptions",)
