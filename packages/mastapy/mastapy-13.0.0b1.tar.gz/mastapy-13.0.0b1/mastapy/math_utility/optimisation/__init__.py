"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1536 import AbstractOptimisable
    from ._1537 import DesignSpaceSearchStrategyDatabase
    from ._1538 import InputSetter
    from ._1539 import MicroGeometryDesignSpaceSearchStrategyDatabase
    from ._1540 import Optimisable
    from ._1541 import OptimisationHistory
    from ._1542 import OptimizationInput
    from ._1543 import OptimizationVariable
    from ._1544 import ParetoOptimisationFilter
    from ._1545 import ParetoOptimisationInput
    from ._1546 import ParetoOptimisationOutput
    from ._1547 import ParetoOptimisationStrategy
    from ._1548 import ParetoOptimisationStrategyBars
    from ._1549 import ParetoOptimisationStrategyChartInformation
    from ._1550 import ParetoOptimisationStrategyDatabase
    from ._1551 import ParetoOptimisationVariable
    from ._1552 import ParetoOptimisationVariableBase
    from ._1553 import PropertyTargetForDominantCandidateSearch
    from ._1554 import ReportingOptimizationInput
    from ._1555 import SpecifyOptimisationInputAs
    from ._1556 import TargetingPropertyTo
else:
    import_structure = {
        "_1536": ["AbstractOptimisable"],
        "_1537": ["DesignSpaceSearchStrategyDatabase"],
        "_1538": ["InputSetter"],
        "_1539": ["MicroGeometryDesignSpaceSearchStrategyDatabase"],
        "_1540": ["Optimisable"],
        "_1541": ["OptimisationHistory"],
        "_1542": ["OptimizationInput"],
        "_1543": ["OptimizationVariable"],
        "_1544": ["ParetoOptimisationFilter"],
        "_1545": ["ParetoOptimisationInput"],
        "_1546": ["ParetoOptimisationOutput"],
        "_1547": ["ParetoOptimisationStrategy"],
        "_1548": ["ParetoOptimisationStrategyBars"],
        "_1549": ["ParetoOptimisationStrategyChartInformation"],
        "_1550": ["ParetoOptimisationStrategyDatabase"],
        "_1551": ["ParetoOptimisationVariable"],
        "_1552": ["ParetoOptimisationVariableBase"],
        "_1553": ["PropertyTargetForDominantCandidateSearch"],
        "_1554": ["ReportingOptimizationInput"],
        "_1555": ["SpecifyOptimisationInputAs"],
        "_1556": ["TargetingPropertyTo"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractOptimisable",
    "DesignSpaceSearchStrategyDatabase",
    "InputSetter",
    "MicroGeometryDesignSpaceSearchStrategyDatabase",
    "Optimisable",
    "OptimisationHistory",
    "OptimizationInput",
    "OptimizationVariable",
    "ParetoOptimisationFilter",
    "ParetoOptimisationInput",
    "ParetoOptimisationOutput",
    "ParetoOptimisationStrategy",
    "ParetoOptimisationStrategyBars",
    "ParetoOptimisationStrategyChartInformation",
    "ParetoOptimisationStrategyDatabase",
    "ParetoOptimisationVariable",
    "ParetoOptimisationVariableBase",
    "PropertyTargetForDominantCandidateSearch",
    "ReportingOptimizationInput",
    "SpecifyOptimisationInputAs",
    "TargetingPropertyTo",
)
