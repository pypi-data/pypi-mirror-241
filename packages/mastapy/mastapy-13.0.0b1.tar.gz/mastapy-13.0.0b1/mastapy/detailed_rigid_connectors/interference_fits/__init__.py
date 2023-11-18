"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1440 import AssemblyMethods
    from ._1441 import CalculationMethods
    from ._1442 import InterferenceFitDesign
    from ._1443 import InterferenceFitHalfDesign
    from ._1444 import StressRegions
    from ._1445 import Table4JointInterfaceTypes
else:
    import_structure = {
        "_1440": ["AssemblyMethods"],
        "_1441": ["CalculationMethods"],
        "_1442": ["InterferenceFitDesign"],
        "_1443": ["InterferenceFitHalfDesign"],
        "_1444": ["StressRegions"],
        "_1445": ["Table4JointInterfaceTypes"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AssemblyMethods",
    "CalculationMethods",
    "InterferenceFitDesign",
    "InterferenceFitHalfDesign",
    "StressRegions",
    "Table4JointInterfaceTypes",
)
