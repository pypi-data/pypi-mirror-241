"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1318 import DynamicForceResults
    from ._1319 import EfficiencyResults
    from ._1320 import ElectricMachineDQModel
    from ._1321 import ElectricMachineMechanicalResults
    from ._1322 import ElectricMachineMechanicalResultsViewable
    from ._1323 import ElectricMachineResults
    from ._1324 import ElectricMachineResultsForConductorTurn
    from ._1325 import ElectricMachineResultsForConductorTurnAtTimeStep
    from ._1326 import ElectricMachineResultsForLineToLine
    from ._1327 import ElectricMachineResultsForOpenCircuitAndOnLoad
    from ._1328 import ElectricMachineResultsForPhase
    from ._1329 import ElectricMachineResultsForPhaseAtTimeStep
    from ._1330 import ElectricMachineResultsForStatorToothAtTimeStep
    from ._1331 import ElectricMachineResultsLineToLineAtTimeStep
    from ._1332 import ElectricMachineResultsTimeStep
    from ._1333 import ElectricMachineResultsTimeStepAtLocation
    from ._1334 import ElectricMachineResultsViewable
    from ._1335 import ElectricMachineForceViewOptions
    from ._1337 import LinearDQModel
    from ._1338 import MaximumTorqueResultsPoints
    from ._1339 import NonLinearDQModel
    from ._1340 import NonLinearDQModelGeneratorSettings
    from ._1341 import OnLoadElectricMachineResults
    from ._1342 import OpenCircuitElectricMachineResults
else:
    import_structure = {
        "_1318": ["DynamicForceResults"],
        "_1319": ["EfficiencyResults"],
        "_1320": ["ElectricMachineDQModel"],
        "_1321": ["ElectricMachineMechanicalResults"],
        "_1322": ["ElectricMachineMechanicalResultsViewable"],
        "_1323": ["ElectricMachineResults"],
        "_1324": ["ElectricMachineResultsForConductorTurn"],
        "_1325": ["ElectricMachineResultsForConductorTurnAtTimeStep"],
        "_1326": ["ElectricMachineResultsForLineToLine"],
        "_1327": ["ElectricMachineResultsForOpenCircuitAndOnLoad"],
        "_1328": ["ElectricMachineResultsForPhase"],
        "_1329": ["ElectricMachineResultsForPhaseAtTimeStep"],
        "_1330": ["ElectricMachineResultsForStatorToothAtTimeStep"],
        "_1331": ["ElectricMachineResultsLineToLineAtTimeStep"],
        "_1332": ["ElectricMachineResultsTimeStep"],
        "_1333": ["ElectricMachineResultsTimeStepAtLocation"],
        "_1334": ["ElectricMachineResultsViewable"],
        "_1335": ["ElectricMachineForceViewOptions"],
        "_1337": ["LinearDQModel"],
        "_1338": ["MaximumTorqueResultsPoints"],
        "_1339": ["NonLinearDQModel"],
        "_1340": ["NonLinearDQModelGeneratorSettings"],
        "_1341": ["OnLoadElectricMachineResults"],
        "_1342": ["OpenCircuitElectricMachineResults"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DynamicForceResults",
    "EfficiencyResults",
    "ElectricMachineDQModel",
    "ElectricMachineMechanicalResults",
    "ElectricMachineMechanicalResultsViewable",
    "ElectricMachineResults",
    "ElectricMachineResultsForConductorTurn",
    "ElectricMachineResultsForConductorTurnAtTimeStep",
    "ElectricMachineResultsForLineToLine",
    "ElectricMachineResultsForOpenCircuitAndOnLoad",
    "ElectricMachineResultsForPhase",
    "ElectricMachineResultsForPhaseAtTimeStep",
    "ElectricMachineResultsForStatorToothAtTimeStep",
    "ElectricMachineResultsLineToLineAtTimeStep",
    "ElectricMachineResultsTimeStep",
    "ElectricMachineResultsTimeStepAtLocation",
    "ElectricMachineResultsViewable",
    "ElectricMachineForceViewOptions",
    "LinearDQModel",
    "MaximumTorqueResultsPoints",
    "NonLinearDQModel",
    "NonLinearDQModelGeneratorSettings",
    "OnLoadElectricMachineResults",
    "OpenCircuitElectricMachineResults",
)
