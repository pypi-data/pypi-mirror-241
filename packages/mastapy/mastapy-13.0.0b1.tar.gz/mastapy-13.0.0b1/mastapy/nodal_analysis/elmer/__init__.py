"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._167 import ContactType
    from ._168 import ElectricMachineAnalysisPeriod
    from ._169 import ElmerResults
    from ._170 import ElmerResultsFromElectroMagneticAnalysis
    from ._171 import ElmerResultsViewable
    from ._172 import ElmerResultType
    from ._173 import MechanicalContactSpecification
else:
    import_structure = {
        "_167": ["ContactType"],
        "_168": ["ElectricMachineAnalysisPeriod"],
        "_169": ["ElmerResults"],
        "_170": ["ElmerResultsFromElectroMagneticAnalysis"],
        "_171": ["ElmerResultsViewable"],
        "_172": ["ElmerResultType"],
        "_173": ["MechanicalContactSpecification"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ContactType",
    "ElectricMachineAnalysisPeriod",
    "ElmerResults",
    "ElmerResultsFromElectroMagneticAnalysis",
    "ElmerResultsViewable",
    "ElmerResultType",
    "MechanicalContactSpecification",
)
