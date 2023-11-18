"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._637 import CutterProcessSimulation
    from ._638 import FormWheelGrindingProcessSimulation
    from ._639 import ShapingProcessSimulation
else:
    import_structure = {
        "_637": ["CutterProcessSimulation"],
        "_638": ["FormWheelGrindingProcessSimulation"],
        "_639": ["ShapingProcessSimulation"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CutterProcessSimulation",
    "FormWheelGrindingProcessSimulation",
    "ShapingProcessSimulation",
)
