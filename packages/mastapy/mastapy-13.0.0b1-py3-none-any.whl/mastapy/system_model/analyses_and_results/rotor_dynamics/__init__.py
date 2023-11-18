"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4024 import RotorDynamicsDrawStyle
    from ._4025 import ShaftComplexShape
    from ._4026 import ShaftForcedComplexShape
    from ._4027 import ShaftModalComplexShape
    from ._4028 import ShaftModalComplexShapeAtSpeeds
    from ._4029 import ShaftModalComplexShapeAtStiffness
else:
    import_structure = {
        "_4024": ["RotorDynamicsDrawStyle"],
        "_4025": ["ShaftComplexShape"],
        "_4026": ["ShaftForcedComplexShape"],
        "_4027": ["ShaftModalComplexShape"],
        "_4028": ["ShaftModalComplexShapeAtSpeeds"],
        "_4029": ["ShaftModalComplexShapeAtStiffness"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "RotorDynamicsDrawStyle",
    "ShaftComplexShape",
    "ShaftForcedComplexShape",
    "ShaftModalComplexShape",
    "ShaftModalComplexShapeAtSpeeds",
    "ShaftModalComplexShapeAtStiffness",
)
