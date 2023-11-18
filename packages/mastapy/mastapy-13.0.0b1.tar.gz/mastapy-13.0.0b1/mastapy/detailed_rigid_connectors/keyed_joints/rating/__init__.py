"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1438 import KeywayHalfRating
    from ._1439 import KeywayRating
else:
    import_structure = {
        "_1438": ["KeywayHalfRating"],
        "_1439": ["KeywayRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KeywayHalfRating",
    "KeywayRating",
)
