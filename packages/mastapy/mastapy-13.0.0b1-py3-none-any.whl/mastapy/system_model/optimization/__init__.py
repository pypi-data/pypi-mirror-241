"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2224 import ConicalGearOptimisationStrategy
    from ._2225 import ConicalGearOptimizationStep
    from ._2226 import ConicalGearOptimizationStrategyDatabase
    from ._2227 import CylindricalGearOptimisationStrategy
    from ._2228 import CylindricalGearOptimizationStep
    from ._2229 import MeasuredAndFactorViewModel
    from ._2230 import MicroGeometryOptimisationTarget
    from ._2231 import OptimizationStep
    from ._2232 import OptimizationStrategy
    from ._2233 import OptimizationStrategyBase
    from ._2234 import OptimizationStrategyDatabase
else:
    import_structure = {
        "_2224": ["ConicalGearOptimisationStrategy"],
        "_2225": ["ConicalGearOptimizationStep"],
        "_2226": ["ConicalGearOptimizationStrategyDatabase"],
        "_2227": ["CylindricalGearOptimisationStrategy"],
        "_2228": ["CylindricalGearOptimizationStep"],
        "_2229": ["MeasuredAndFactorViewModel"],
        "_2230": ["MicroGeometryOptimisationTarget"],
        "_2231": ["OptimizationStep"],
        "_2232": ["OptimizationStrategy"],
        "_2233": ["OptimizationStrategyBase"],
        "_2234": ["OptimizationStrategyDatabase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConicalGearOptimisationStrategy",
    "ConicalGearOptimizationStep",
    "ConicalGearOptimizationStrategyDatabase",
    "CylindricalGearOptimisationStrategy",
    "CylindricalGearOptimizationStep",
    "MeasuredAndFactorViewModel",
    "MicroGeometryOptimisationTarget",
    "OptimizationStep",
    "OptimizationStrategy",
    "OptimizationStrategyBase",
    "OptimizationStrategyDatabase",
)
