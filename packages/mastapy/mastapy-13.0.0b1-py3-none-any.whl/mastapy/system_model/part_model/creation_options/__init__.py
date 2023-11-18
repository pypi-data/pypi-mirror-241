"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2569 import BeltCreationOptions
    from ._2570 import CycloidalAssemblyCreationOptions
    from ._2571 import CylindricalGearLinearTrainCreationOptions
    from ._2572 import PlanetCarrierCreationOptions
    from ._2573 import ShaftCreationOptions
else:
    import_structure = {
        "_2569": ["BeltCreationOptions"],
        "_2570": ["CycloidalAssemblyCreationOptions"],
        "_2571": ["CylindricalGearLinearTrainCreationOptions"],
        "_2572": ["PlanetCarrierCreationOptions"],
        "_2573": ["ShaftCreationOptions"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BeltCreationOptions",
    "CycloidalAssemblyCreationOptions",
    "CylindricalGearLinearTrainCreationOptions",
    "PlanetCarrierCreationOptions",
    "ShaftCreationOptions",
)
