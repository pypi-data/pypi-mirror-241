"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2108 import InnerRingFittingThermalResults
    from ._2109 import InterferenceComponents
    from ._2110 import OuterRingFittingThermalResults
    from ._2111 import RingFittingThermalResults
else:
    import_structure = {
        "_2108": ["InnerRingFittingThermalResults"],
        "_2109": ["InterferenceComponents"],
        "_2110": ["OuterRingFittingThermalResults"],
        "_2111": ["RingFittingThermalResults"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "InnerRingFittingThermalResults",
    "InterferenceComponents",
    "OuterRingFittingThermalResults",
    "RingFittingThermalResults",
)
