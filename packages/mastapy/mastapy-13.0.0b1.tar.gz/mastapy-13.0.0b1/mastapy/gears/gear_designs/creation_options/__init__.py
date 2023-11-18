"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1144 import CylindricalGearPairCreationOptions
    from ._1145 import GearSetCreationOptions
    from ._1146 import HypoidGearSetCreationOptions
    from ._1147 import SpiralBevelGearSetCreationOptions
else:
    import_structure = {
        "_1144": ["CylindricalGearPairCreationOptions"],
        "_1145": ["GearSetCreationOptions"],
        "_1146": ["HypoidGearSetCreationOptions"],
        "_1147": ["SpiralBevelGearSetCreationOptions"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearPairCreationOptions",
    "GearSetCreationOptions",
    "HypoidGearSetCreationOptions",
    "SpiralBevelGearSetCreationOptions",
)
