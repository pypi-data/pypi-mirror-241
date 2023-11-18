"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2566 import CycloidalAssembly
    from ._2567 import CycloidalDisc
    from ._2568 import RingPins
else:
    import_structure = {
        "_2566": ["CycloidalAssembly"],
        "_2567": ["CycloidalDisc"],
        "_2568": ["RingPins"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CycloidalAssembly",
    "CycloidalDisc",
    "RingPins",
)
