"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2508 import ActiveCylindricalGearSetDesignSelection
    from ._2509 import ActiveGearSetDesignSelection
    from ._2510 import ActiveGearSetDesignSelectionGroup
    from ._2511 import AGMAGleasonConicalGear
    from ._2512 import AGMAGleasonConicalGearSet
    from ._2513 import BevelDifferentialGear
    from ._2514 import BevelDifferentialGearSet
    from ._2515 import BevelDifferentialPlanetGear
    from ._2516 import BevelDifferentialSunGear
    from ._2517 import BevelGear
    from ._2518 import BevelGearSet
    from ._2519 import ConceptGear
    from ._2520 import ConceptGearSet
    from ._2521 import ConicalGear
    from ._2522 import ConicalGearSet
    from ._2523 import CylindricalGear
    from ._2524 import CylindricalGearSet
    from ._2525 import CylindricalPlanetGear
    from ._2526 import FaceGear
    from ._2527 import FaceGearSet
    from ._2528 import Gear
    from ._2529 import GearOrientations
    from ._2530 import GearSet
    from ._2531 import GearSetConfiguration
    from ._2532 import HypoidGear
    from ._2533 import HypoidGearSet
    from ._2534 import KlingelnbergCycloPalloidConicalGear
    from ._2535 import KlingelnbergCycloPalloidConicalGearSet
    from ._2536 import KlingelnbergCycloPalloidHypoidGear
    from ._2537 import KlingelnbergCycloPalloidHypoidGearSet
    from ._2538 import KlingelnbergCycloPalloidSpiralBevelGear
    from ._2539 import KlingelnbergCycloPalloidSpiralBevelGearSet
    from ._2540 import PlanetaryGearSet
    from ._2541 import SpiralBevelGear
    from ._2542 import SpiralBevelGearSet
    from ._2543 import StraightBevelDiffGear
    from ._2544 import StraightBevelDiffGearSet
    from ._2545 import StraightBevelGear
    from ._2546 import StraightBevelGearSet
    from ._2547 import StraightBevelPlanetGear
    from ._2548 import StraightBevelSunGear
    from ._2549 import WormGear
    from ._2550 import WormGearSet
    from ._2551 import ZerolBevelGear
    from ._2552 import ZerolBevelGearSet
else:
    import_structure = {
        "_2508": ["ActiveCylindricalGearSetDesignSelection"],
        "_2509": ["ActiveGearSetDesignSelection"],
        "_2510": ["ActiveGearSetDesignSelectionGroup"],
        "_2511": ["AGMAGleasonConicalGear"],
        "_2512": ["AGMAGleasonConicalGearSet"],
        "_2513": ["BevelDifferentialGear"],
        "_2514": ["BevelDifferentialGearSet"],
        "_2515": ["BevelDifferentialPlanetGear"],
        "_2516": ["BevelDifferentialSunGear"],
        "_2517": ["BevelGear"],
        "_2518": ["BevelGearSet"],
        "_2519": ["ConceptGear"],
        "_2520": ["ConceptGearSet"],
        "_2521": ["ConicalGear"],
        "_2522": ["ConicalGearSet"],
        "_2523": ["CylindricalGear"],
        "_2524": ["CylindricalGearSet"],
        "_2525": ["CylindricalPlanetGear"],
        "_2526": ["FaceGear"],
        "_2527": ["FaceGearSet"],
        "_2528": ["Gear"],
        "_2529": ["GearOrientations"],
        "_2530": ["GearSet"],
        "_2531": ["GearSetConfiguration"],
        "_2532": ["HypoidGear"],
        "_2533": ["HypoidGearSet"],
        "_2534": ["KlingelnbergCycloPalloidConicalGear"],
        "_2535": ["KlingelnbergCycloPalloidConicalGearSet"],
        "_2536": ["KlingelnbergCycloPalloidHypoidGear"],
        "_2537": ["KlingelnbergCycloPalloidHypoidGearSet"],
        "_2538": ["KlingelnbergCycloPalloidSpiralBevelGear"],
        "_2539": ["KlingelnbergCycloPalloidSpiralBevelGearSet"],
        "_2540": ["PlanetaryGearSet"],
        "_2541": ["SpiralBevelGear"],
        "_2542": ["SpiralBevelGearSet"],
        "_2543": ["StraightBevelDiffGear"],
        "_2544": ["StraightBevelDiffGearSet"],
        "_2545": ["StraightBevelGear"],
        "_2546": ["StraightBevelGearSet"],
        "_2547": ["StraightBevelPlanetGear"],
        "_2548": ["StraightBevelSunGear"],
        "_2549": ["WormGear"],
        "_2550": ["WormGearSet"],
        "_2551": ["ZerolBevelGear"],
        "_2552": ["ZerolBevelGearSet"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ActiveCylindricalGearSetDesignSelection",
    "ActiveGearSetDesignSelection",
    "ActiveGearSetDesignSelectionGroup",
    "AGMAGleasonConicalGear",
    "AGMAGleasonConicalGearSet",
    "BevelDifferentialGear",
    "BevelDifferentialGearSet",
    "BevelDifferentialPlanetGear",
    "BevelDifferentialSunGear",
    "BevelGear",
    "BevelGearSet",
    "ConceptGear",
    "ConceptGearSet",
    "ConicalGear",
    "ConicalGearSet",
    "CylindricalGear",
    "CylindricalGearSet",
    "CylindricalPlanetGear",
    "FaceGear",
    "FaceGearSet",
    "Gear",
    "GearOrientations",
    "GearSet",
    "GearSetConfiguration",
    "HypoidGear",
    "HypoidGearSet",
    "KlingelnbergCycloPalloidConicalGear",
    "KlingelnbergCycloPalloidConicalGearSet",
    "KlingelnbergCycloPalloidHypoidGear",
    "KlingelnbergCycloPalloidHypoidGearSet",
    "KlingelnbergCycloPalloidSpiralBevelGear",
    "KlingelnbergCycloPalloidSpiralBevelGearSet",
    "PlanetaryGearSet",
    "SpiralBevelGear",
    "SpiralBevelGearSet",
    "StraightBevelDiffGear",
    "StraightBevelDiffGearSet",
    "StraightBevelGear",
    "StraightBevelGearSet",
    "StraightBevelPlanetGear",
    "StraightBevelSunGear",
    "WormGear",
    "WormGearSet",
    "ZerolBevelGear",
    "ZerolBevelGearSet",
)
