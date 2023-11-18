"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5520 import AbstractMeasuredDynamicResponseAtTime
    from ._5521 import DynamicForceResultAtTime
    from ._5522 import DynamicForceVector3DResult
    from ._5523 import DynamicTorqueResultAtTime
    from ._5524 import DynamicTorqueVector3DResult
else:
    import_structure = {
        "_5520": ["AbstractMeasuredDynamicResponseAtTime"],
        "_5521": ["DynamicForceResultAtTime"],
        "_5522": ["DynamicForceVector3DResult"],
        "_5523": ["DynamicTorqueResultAtTime"],
        "_5524": ["DynamicTorqueVector3DResult"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractMeasuredDynamicResponseAtTime",
    "DynamicForceResultAtTime",
    "DynamicForceVector3DResult",
    "DynamicTorqueResultAtTime",
    "DynamicTorqueVector3DResult",
)
