"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._811 import PinionFinishCutter
    from ._812 import PinionRoughCutter
    from ._813 import WheelFinishCutter
    from ._814 import WheelRoughCutter
else:
    import_structure = {
        "_811": ["PinionFinishCutter"],
        "_812": ["PinionRoughCutter"],
        "_813": ["WheelFinishCutter"],
        "_814": ["WheelRoughCutter"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "PinionFinishCutter",
    "PinionRoughCutter",
    "WheelFinishCutter",
    "WheelRoughCutter",
)
