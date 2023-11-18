"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._729 import CutterSimulationCalc
    from ._730 import CylindricalCutterSimulatableGear
    from ._731 import CylindricalGearSpecification
    from ._732 import CylindricalManufacturedRealGearInMesh
    from ._733 import CylindricalManufacturedVirtualGearInMesh
    from ._734 import FinishCutterSimulation
    from ._735 import FinishStockPoint
    from ._736 import FormWheelGrindingSimulationCalculator
    from ._737 import GearCutterSimulation
    from ._738 import HobSimulationCalculator
    from ._739 import ManufacturingOperationConstraints
    from ._740 import ManufacturingProcessControls
    from ._741 import RackSimulationCalculator
    from ._742 import RoughCutterSimulation
    from ._743 import ShaperSimulationCalculator
    from ._744 import ShavingSimulationCalculator
    from ._745 import VirtualSimulationCalculator
    from ._746 import WormGrinderSimulationCalculator
else:
    import_structure = {
        "_729": ["CutterSimulationCalc"],
        "_730": ["CylindricalCutterSimulatableGear"],
        "_731": ["CylindricalGearSpecification"],
        "_732": ["CylindricalManufacturedRealGearInMesh"],
        "_733": ["CylindricalManufacturedVirtualGearInMesh"],
        "_734": ["FinishCutterSimulation"],
        "_735": ["FinishStockPoint"],
        "_736": ["FormWheelGrindingSimulationCalculator"],
        "_737": ["GearCutterSimulation"],
        "_738": ["HobSimulationCalculator"],
        "_739": ["ManufacturingOperationConstraints"],
        "_740": ["ManufacturingProcessControls"],
        "_741": ["RackSimulationCalculator"],
        "_742": ["RoughCutterSimulation"],
        "_743": ["ShaperSimulationCalculator"],
        "_744": ["ShavingSimulationCalculator"],
        "_745": ["VirtualSimulationCalculator"],
        "_746": ["WormGrinderSimulationCalculator"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CutterSimulationCalc",
    "CylindricalCutterSimulatableGear",
    "CylindricalGearSpecification",
    "CylindricalManufacturedRealGearInMesh",
    "CylindricalManufacturedVirtualGearInMesh",
    "FinishCutterSimulation",
    "FinishStockPoint",
    "FormWheelGrindingSimulationCalculator",
    "GearCutterSimulation",
    "HobSimulationCalculator",
    "ManufacturingOperationConstraints",
    "ManufacturingProcessControls",
    "RackSimulationCalculator",
    "RoughCutterSimulation",
    "ShaperSimulationCalculator",
    "ShavingSimulationCalculator",
    "VirtualSimulationCalculator",
    "WormGrinderSimulationCalculator",
)
