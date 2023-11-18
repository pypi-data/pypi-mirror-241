"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2480 import Shaft
    from ._2481 import ShaftBow
else:
    import_structure = {
        "_2480": ["Shaft"],
        "_2481": ["ShaftBow"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Shaft",
    "ShaftBow",
)
