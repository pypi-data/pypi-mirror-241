"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2297 import AGMAGleasonConicalGearMesh
    from ._2298 import AGMAGleasonConicalGearTeethSocket
    from ._2299 import BevelDifferentialGearMesh
    from ._2300 import BevelDifferentialGearTeethSocket
    from ._2301 import BevelGearMesh
    from ._2302 import BevelGearTeethSocket
    from ._2303 import ConceptGearMesh
    from ._2304 import ConceptGearTeethSocket
    from ._2305 import ConicalGearMesh
    from ._2306 import ConicalGearTeethSocket
    from ._2307 import CylindricalGearMesh
    from ._2308 import CylindricalGearTeethSocket
    from ._2309 import FaceGearMesh
    from ._2310 import FaceGearTeethSocket
    from ._2311 import GearMesh
    from ._2312 import GearTeethSocket
    from ._2313 import HypoidGearMesh
    from ._2314 import HypoidGearTeethSocket
    from ._2315 import KlingelnbergConicalGearTeethSocket
    from ._2316 import KlingelnbergCycloPalloidConicalGearMesh
    from ._2317 import KlingelnbergCycloPalloidHypoidGearMesh
    from ._2318 import KlingelnbergCycloPalloidSpiralBevelGearMesh
    from ._2319 import KlingelnbergHypoidGearTeethSocket
    from ._2320 import KlingelnbergSpiralBevelGearTeethSocket
    from ._2321 import SpiralBevelGearMesh
    from ._2322 import SpiralBevelGearTeethSocket
    from ._2323 import StraightBevelDiffGearMesh
    from ._2324 import StraightBevelDiffGearTeethSocket
    from ._2325 import StraightBevelGearMesh
    from ._2326 import StraightBevelGearTeethSocket
    from ._2327 import WormGearMesh
    from ._2328 import WormGearTeethSocket
    from ._2329 import ZerolBevelGearMesh
    from ._2330 import ZerolBevelGearTeethSocket
else:
    import_structure = {
        "_2297": ["AGMAGleasonConicalGearMesh"],
        "_2298": ["AGMAGleasonConicalGearTeethSocket"],
        "_2299": ["BevelDifferentialGearMesh"],
        "_2300": ["BevelDifferentialGearTeethSocket"],
        "_2301": ["BevelGearMesh"],
        "_2302": ["BevelGearTeethSocket"],
        "_2303": ["ConceptGearMesh"],
        "_2304": ["ConceptGearTeethSocket"],
        "_2305": ["ConicalGearMesh"],
        "_2306": ["ConicalGearTeethSocket"],
        "_2307": ["CylindricalGearMesh"],
        "_2308": ["CylindricalGearTeethSocket"],
        "_2309": ["FaceGearMesh"],
        "_2310": ["FaceGearTeethSocket"],
        "_2311": ["GearMesh"],
        "_2312": ["GearTeethSocket"],
        "_2313": ["HypoidGearMesh"],
        "_2314": ["HypoidGearTeethSocket"],
        "_2315": ["KlingelnbergConicalGearTeethSocket"],
        "_2316": ["KlingelnbergCycloPalloidConicalGearMesh"],
        "_2317": ["KlingelnbergCycloPalloidHypoidGearMesh"],
        "_2318": ["KlingelnbergCycloPalloidSpiralBevelGearMesh"],
        "_2319": ["KlingelnbergHypoidGearTeethSocket"],
        "_2320": ["KlingelnbergSpiralBevelGearTeethSocket"],
        "_2321": ["SpiralBevelGearMesh"],
        "_2322": ["SpiralBevelGearTeethSocket"],
        "_2323": ["StraightBevelDiffGearMesh"],
        "_2324": ["StraightBevelDiffGearTeethSocket"],
        "_2325": ["StraightBevelGearMesh"],
        "_2326": ["StraightBevelGearTeethSocket"],
        "_2327": ["WormGearMesh"],
        "_2328": ["WormGearTeethSocket"],
        "_2329": ["ZerolBevelGearMesh"],
        "_2330": ["ZerolBevelGearTeethSocket"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMAGleasonConicalGearMesh",
    "AGMAGleasonConicalGearTeethSocket",
    "BevelDifferentialGearMesh",
    "BevelDifferentialGearTeethSocket",
    "BevelGearMesh",
    "BevelGearTeethSocket",
    "ConceptGearMesh",
    "ConceptGearTeethSocket",
    "ConicalGearMesh",
    "ConicalGearTeethSocket",
    "CylindricalGearMesh",
    "CylindricalGearTeethSocket",
    "FaceGearMesh",
    "FaceGearTeethSocket",
    "GearMesh",
    "GearTeethSocket",
    "HypoidGearMesh",
    "HypoidGearTeethSocket",
    "KlingelnbergConicalGearTeethSocket",
    "KlingelnbergCycloPalloidConicalGearMesh",
    "KlingelnbergCycloPalloidHypoidGearMesh",
    "KlingelnbergCycloPalloidSpiralBevelGearMesh",
    "KlingelnbergHypoidGearTeethSocket",
    "KlingelnbergSpiralBevelGearTeethSocket",
    "SpiralBevelGearMesh",
    "SpiralBevelGearTeethSocket",
    "StraightBevelDiffGearMesh",
    "StraightBevelDiffGearTeethSocket",
    "StraightBevelGearMesh",
    "StraightBevelGearTeethSocket",
    "WormGearMesh",
    "WormGearTeethSocket",
    "ZerolBevelGearMesh",
    "ZerolBevelGearTeethSocket",
)
