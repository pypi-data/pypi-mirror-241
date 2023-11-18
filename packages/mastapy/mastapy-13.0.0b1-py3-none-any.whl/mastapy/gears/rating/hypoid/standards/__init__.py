"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._440 import GleasonHypoidGearSingleFlankRating
    from ._441 import GleasonHypoidMeshSingleFlankRating
    from ._442 import HypoidRateableMesh
else:
    import_structure = {
        "_440": ["GleasonHypoidGearSingleFlankRating"],
        "_441": ["GleasonHypoidMeshSingleFlankRating"],
        "_442": ["HypoidRateableMesh"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "GleasonHypoidGearSingleFlankRating",
    "GleasonHypoidMeshSingleFlankRating",
    "HypoidRateableMesh",
)
