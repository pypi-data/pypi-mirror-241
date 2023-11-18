"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._532 import AGMA2101GearSingleFlankRating
    from ._533 import AGMA2101MeshSingleFlankRating
    from ._534 import AGMA2101RateableMesh
    from ._535 import ThermalReductionFactorFactorsAndExponents
else:
    import_structure = {
        "_532": ["AGMA2101GearSingleFlankRating"],
        "_533": ["AGMA2101MeshSingleFlankRating"],
        "_534": ["AGMA2101RateableMesh"],
        "_535": ["ThermalReductionFactorFactorsAndExponents"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMA2101GearSingleFlankRating",
    "AGMA2101MeshSingleFlankRating",
    "AGMA2101RateableMesh",
    "ThermalReductionFactorFactorsAndExponents",
)
