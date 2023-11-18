"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._376 import BevelVirtualCylindricalGearISO10300MethodB2
    from ._377 import BevelVirtualCylindricalGearSetISO10300MethodB1
    from ._378 import BevelVirtualCylindricalGearSetISO10300MethodB2
    from ._379 import HypoidVirtualCylindricalGearISO10300MethodB2
    from ._380 import HypoidVirtualCylindricalGearSetISO10300MethodB1
    from ._381 import HypoidVirtualCylindricalGearSetISO10300MethodB2
    from ._382 import KlingelnbergHypoidVirtualCylindricalGear
    from ._383 import KlingelnbergSpiralBevelVirtualCylindricalGear
    from ._384 import KlingelnbergVirtualCylindricalGear
    from ._385 import KlingelnbergVirtualCylindricalGearSet
    from ._386 import VirtualCylindricalGear
    from ._387 import VirtualCylindricalGearBasic
    from ._388 import VirtualCylindricalGearISO10300MethodB1
    from ._389 import VirtualCylindricalGearISO10300MethodB2
    from ._390 import VirtualCylindricalGearSet
    from ._391 import VirtualCylindricalGearSetISO10300MethodB1
    from ._392 import VirtualCylindricalGearSetISO10300MethodB2
else:
    import_structure = {
        "_376": ["BevelVirtualCylindricalGearISO10300MethodB2"],
        "_377": ["BevelVirtualCylindricalGearSetISO10300MethodB1"],
        "_378": ["BevelVirtualCylindricalGearSetISO10300MethodB2"],
        "_379": ["HypoidVirtualCylindricalGearISO10300MethodB2"],
        "_380": ["HypoidVirtualCylindricalGearSetISO10300MethodB1"],
        "_381": ["HypoidVirtualCylindricalGearSetISO10300MethodB2"],
        "_382": ["KlingelnbergHypoidVirtualCylindricalGear"],
        "_383": ["KlingelnbergSpiralBevelVirtualCylindricalGear"],
        "_384": ["KlingelnbergVirtualCylindricalGear"],
        "_385": ["KlingelnbergVirtualCylindricalGearSet"],
        "_386": ["VirtualCylindricalGear"],
        "_387": ["VirtualCylindricalGearBasic"],
        "_388": ["VirtualCylindricalGearISO10300MethodB1"],
        "_389": ["VirtualCylindricalGearISO10300MethodB2"],
        "_390": ["VirtualCylindricalGearSet"],
        "_391": ["VirtualCylindricalGearSetISO10300MethodB1"],
        "_392": ["VirtualCylindricalGearSetISO10300MethodB2"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BevelVirtualCylindricalGearISO10300MethodB2",
    "BevelVirtualCylindricalGearSetISO10300MethodB1",
    "BevelVirtualCylindricalGearSetISO10300MethodB2",
    "HypoidVirtualCylindricalGearISO10300MethodB2",
    "HypoidVirtualCylindricalGearSetISO10300MethodB1",
    "HypoidVirtualCylindricalGearSetISO10300MethodB2",
    "KlingelnbergHypoidVirtualCylindricalGear",
    "KlingelnbergSpiralBevelVirtualCylindricalGear",
    "KlingelnbergVirtualCylindricalGear",
    "KlingelnbergVirtualCylindricalGearSet",
    "VirtualCylindricalGear",
    "VirtualCylindricalGearBasic",
    "VirtualCylindricalGearISO10300MethodB1",
    "VirtualCylindricalGearISO10300MethodB2",
    "VirtualCylindricalGearSet",
    "VirtualCylindricalGearSetISO10300MethodB1",
    "VirtualCylindricalGearSetISO10300MethodB2",
)
