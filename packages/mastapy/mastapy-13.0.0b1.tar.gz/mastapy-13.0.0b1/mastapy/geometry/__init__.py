"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._304 import ClippingPlane
    from ._305 import DrawStyle
    from ._306 import DrawStyleBase
    from ._307 import PackagingLimits
else:
    import_structure = {
        "_304": ["ClippingPlane"],
        "_305": ["DrawStyle"],
        "_306": ["DrawStyleBase"],
        "_307": ["PackagingLimits"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ClippingPlane",
    "DrawStyle",
    "DrawStyleBase",
    "PackagingLimits",
)
