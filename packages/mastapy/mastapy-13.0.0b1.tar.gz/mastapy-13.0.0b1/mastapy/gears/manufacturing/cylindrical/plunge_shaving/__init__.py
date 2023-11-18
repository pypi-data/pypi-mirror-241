"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._640 import CalculationError
    from ._641 import ChartType
    from ._642 import GearPointCalculationError
    from ._643 import MicroGeometryDefinitionMethod
    from ._644 import MicroGeometryDefinitionType
    from ._645 import PlungeShaverCalculation
    from ._646 import PlungeShaverCalculationInputs
    from ._647 import PlungeShaverGeneration
    from ._648 import PlungeShaverInputsAndMicroGeometry
    from ._649 import PlungeShaverOutputs
    from ._650 import PlungeShaverSettings
    from ._651 import PointOfInterest
    from ._652 import RealPlungeShaverOutputs
    from ._653 import ShaverPointCalculationError
    from ._654 import ShaverPointOfInterest
    from ._655 import VirtualPlungeShaverOutputs
else:
    import_structure = {
        "_640": ["CalculationError"],
        "_641": ["ChartType"],
        "_642": ["GearPointCalculationError"],
        "_643": ["MicroGeometryDefinitionMethod"],
        "_644": ["MicroGeometryDefinitionType"],
        "_645": ["PlungeShaverCalculation"],
        "_646": ["PlungeShaverCalculationInputs"],
        "_647": ["PlungeShaverGeneration"],
        "_648": ["PlungeShaverInputsAndMicroGeometry"],
        "_649": ["PlungeShaverOutputs"],
        "_650": ["PlungeShaverSettings"],
        "_651": ["PointOfInterest"],
        "_652": ["RealPlungeShaverOutputs"],
        "_653": ["ShaverPointCalculationError"],
        "_654": ["ShaverPointOfInterest"],
        "_655": ["VirtualPlungeShaverOutputs"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CalculationError",
    "ChartType",
    "GearPointCalculationError",
    "MicroGeometryDefinitionMethod",
    "MicroGeometryDefinitionType",
    "PlungeShaverCalculation",
    "PlungeShaverCalculationInputs",
    "PlungeShaverGeneration",
    "PlungeShaverInputsAndMicroGeometry",
    "PlungeShaverOutputs",
    "PlungeShaverSettings",
    "PointOfInterest",
    "RealPlungeShaverOutputs",
    "ShaverPointCalculationError",
    "ShaverPointOfInterest",
    "VirtualPlungeShaverOutputs",
)
