"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1343 import BasicDynamicForceLoadCase
    from ._1344 import DynamicForceAnalysis
    from ._1345 import DynamicForceLoadCase
    from ._1346 import DynamicForcesOperatingPoint
    from ._1347 import EfficiencyMapAnalysis
    from ._1348 import EfficiencyMapLoadCase
    from ._1349 import ElectricMachineAnalysis
    from ._1350 import ElectricMachineBasicMechanicalLossSettings
    from ._1351 import ElectricMachineControlStrategy
    from ._1352 import ElectricMachineEfficiencyMapSettings
    from ._1353 import ElectricMachineFEAnalysis
    from ._1354 import ElectricMachineFEMechanicalAnalysis
    from ._1355 import ElectricMachineLoadCase
    from ._1356 import ElectricMachineLoadCaseBase
    from ._1357 import ElectricMachineLoadCaseGroup
    from ._1358 import ElectricMachineMechanicalLoadCase
    from ._1359 import EndWindingInductanceMethod
    from ._1360 import LeadingOrLagging
    from ._1361 import LoadCaseType
    from ._1362 import LoadCaseTypeSelector
    from ._1363 import MotoringOrGenerating
    from ._1364 import NonLinearDQModelMultipleOperatingPointsLoadCase
    from ._1365 import NumberOfStepsPerOperatingPointSpecificationMethod
    from ._1366 import OperatingPointsSpecificationMethod
    from ._1367 import SingleOperatingPointAnalysis
    from ._1368 import SlotDetailForAnalysis
    from ._1369 import SpecifyTorqueOrCurrent
    from ._1370 import SpeedPointsDistribution
    from ._1371 import SpeedTorqueCurveAnalysis
    from ._1372 import SpeedTorqueCurveLoadCase
    from ._1373 import SpeedTorqueLoadCase
    from ._1374 import Temperatures
else:
    import_structure = {
        "_1343": ["BasicDynamicForceLoadCase"],
        "_1344": ["DynamicForceAnalysis"],
        "_1345": ["DynamicForceLoadCase"],
        "_1346": ["DynamicForcesOperatingPoint"],
        "_1347": ["EfficiencyMapAnalysis"],
        "_1348": ["EfficiencyMapLoadCase"],
        "_1349": ["ElectricMachineAnalysis"],
        "_1350": ["ElectricMachineBasicMechanicalLossSettings"],
        "_1351": ["ElectricMachineControlStrategy"],
        "_1352": ["ElectricMachineEfficiencyMapSettings"],
        "_1353": ["ElectricMachineFEAnalysis"],
        "_1354": ["ElectricMachineFEMechanicalAnalysis"],
        "_1355": ["ElectricMachineLoadCase"],
        "_1356": ["ElectricMachineLoadCaseBase"],
        "_1357": ["ElectricMachineLoadCaseGroup"],
        "_1358": ["ElectricMachineMechanicalLoadCase"],
        "_1359": ["EndWindingInductanceMethod"],
        "_1360": ["LeadingOrLagging"],
        "_1361": ["LoadCaseType"],
        "_1362": ["LoadCaseTypeSelector"],
        "_1363": ["MotoringOrGenerating"],
        "_1364": ["NonLinearDQModelMultipleOperatingPointsLoadCase"],
        "_1365": ["NumberOfStepsPerOperatingPointSpecificationMethod"],
        "_1366": ["OperatingPointsSpecificationMethod"],
        "_1367": ["SingleOperatingPointAnalysis"],
        "_1368": ["SlotDetailForAnalysis"],
        "_1369": ["SpecifyTorqueOrCurrent"],
        "_1370": ["SpeedPointsDistribution"],
        "_1371": ["SpeedTorqueCurveAnalysis"],
        "_1372": ["SpeedTorqueCurveLoadCase"],
        "_1373": ["SpeedTorqueLoadCase"],
        "_1374": ["Temperatures"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BasicDynamicForceLoadCase",
    "DynamicForceAnalysis",
    "DynamicForceLoadCase",
    "DynamicForcesOperatingPoint",
    "EfficiencyMapAnalysis",
    "EfficiencyMapLoadCase",
    "ElectricMachineAnalysis",
    "ElectricMachineBasicMechanicalLossSettings",
    "ElectricMachineControlStrategy",
    "ElectricMachineEfficiencyMapSettings",
    "ElectricMachineFEAnalysis",
    "ElectricMachineFEMechanicalAnalysis",
    "ElectricMachineLoadCase",
    "ElectricMachineLoadCaseBase",
    "ElectricMachineLoadCaseGroup",
    "ElectricMachineMechanicalLoadCase",
    "EndWindingInductanceMethod",
    "LeadingOrLagging",
    "LoadCaseType",
    "LoadCaseTypeSelector",
    "MotoringOrGenerating",
    "NonLinearDQModelMultipleOperatingPointsLoadCase",
    "NumberOfStepsPerOperatingPointSpecificationMethod",
    "OperatingPointsSpecificationMethod",
    "SingleOperatingPointAnalysis",
    "SlotDetailForAnalysis",
    "SpecifyTorqueOrCurrent",
    "SpeedPointsDistribution",
    "SpeedTorqueCurveAnalysis",
    "SpeedTorqueCurveLoadCase",
    "SpeedTorqueLoadCase",
    "Temperatures",
)
