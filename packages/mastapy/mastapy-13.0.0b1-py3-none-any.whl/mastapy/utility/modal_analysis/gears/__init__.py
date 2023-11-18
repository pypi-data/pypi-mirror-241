"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1795 import GearMeshForTE
    from ._1796 import GearOrderForTE
    from ._1797 import GearPositions
    from ._1798 import HarmonicOrderForTE
    from ._1799 import LabelOnlyOrder
    from ._1800 import OrderForTE
    from ._1801 import OrderSelector
    from ._1802 import OrderWithRadius
    from ._1803 import RollingBearingOrder
    from ._1804 import ShaftOrderForTE
    from ._1805 import UserDefinedOrderForTE
else:
    import_structure = {
        "_1795": ["GearMeshForTE"],
        "_1796": ["GearOrderForTE"],
        "_1797": ["GearPositions"],
        "_1798": ["HarmonicOrderForTE"],
        "_1799": ["LabelOnlyOrder"],
        "_1800": ["OrderForTE"],
        "_1801": ["OrderSelector"],
        "_1802": ["OrderWithRadius"],
        "_1803": ["RollingBearingOrder"],
        "_1804": ["ShaftOrderForTE"],
        "_1805": ["UserDefinedOrderForTE"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "GearMeshForTE",
    "GearOrderForTE",
    "GearPositions",
    "HarmonicOrderForTE",
    "LabelOnlyOrder",
    "OrderForTE",
    "OrderSelector",
    "OrderWithRadius",
    "RollingBearingOrder",
    "ShaftOrderForTE",
    "UserDefinedOrderForTE",
)
