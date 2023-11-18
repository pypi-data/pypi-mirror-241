"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2235 import DesignStateTargetRatio
    from ._2236 import PlanetGearOptions
    from ._2237 import SystemOptimiser
    from ._2238 import SystemOptimiserDetails
    from ._2239 import ToothNumberFinder
else:
    import_structure = {
        "_2235": ["DesignStateTargetRatio"],
        "_2236": ["PlanetGearOptions"],
        "_2237": ["SystemOptimiser"],
        "_2238": ["SystemOptimiserDetails"],
        "_2239": ["ToothNumberFinder"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DesignStateTargetRatio",
    "PlanetGearOptions",
    "SystemOptimiser",
    "SystemOptimiserDetails",
    "ToothNumberFinder",
)
