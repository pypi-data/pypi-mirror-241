"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._412 import KlingelnbergConicalMeshSingleFlankRating
    from ._413 import KlingelnbergConicalRateableMesh
    from ._414 import KlingelnbergCycloPalloidConicalGearSingleFlankRating
    from ._415 import KlingelnbergCycloPalloidHypoidGearSingleFlankRating
    from ._416 import KlingelnbergCycloPalloidHypoidMeshSingleFlankRating
    from ._417 import KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating
else:
    import_structure = {
        "_412": ["KlingelnbergConicalMeshSingleFlankRating"],
        "_413": ["KlingelnbergConicalRateableMesh"],
        "_414": ["KlingelnbergCycloPalloidConicalGearSingleFlankRating"],
        "_415": ["KlingelnbergCycloPalloidHypoidGearSingleFlankRating"],
        "_416": ["KlingelnbergCycloPalloidHypoidMeshSingleFlankRating"],
        "_417": ["KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KlingelnbergConicalMeshSingleFlankRating",
    "KlingelnbergConicalRateableMesh",
    "KlingelnbergCycloPalloidConicalGearSingleFlankRating",
    "KlingelnbergCycloPalloidHypoidGearSingleFlankRating",
    "KlingelnbergCycloPalloidHypoidMeshSingleFlankRating",
    "KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating",
)
