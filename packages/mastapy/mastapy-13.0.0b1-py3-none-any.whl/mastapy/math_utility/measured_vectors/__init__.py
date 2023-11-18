"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1557 import AbstractForceAndDisplacementResults
    from ._1558 import ForceAndDisplacementResults
    from ._1559 import ForceResults
    from ._1560 import NodeResults
    from ._1561 import OverridableDisplacementBoundaryCondition
    from ._1562 import VectorWithLinearAndAngularComponents
else:
    import_structure = {
        "_1557": ["AbstractForceAndDisplacementResults"],
        "_1558": ["ForceAndDisplacementResults"],
        "_1559": ["ForceResults"],
        "_1560": ["NodeResults"],
        "_1561": ["OverridableDisplacementBoundaryCondition"],
        "_1562": ["VectorWithLinearAndAngularComponents"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractForceAndDisplacementResults",
    "ForceAndDisplacementResults",
    "ForceResults",
    "NodeResults",
    "OverridableDisplacementBoundaryCondition",
    "VectorWithLinearAndAngularComponents",
)
