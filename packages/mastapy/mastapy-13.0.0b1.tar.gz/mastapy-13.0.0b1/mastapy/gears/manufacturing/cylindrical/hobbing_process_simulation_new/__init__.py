"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._656 import ActiveProcessMethod
    from ._657 import AnalysisMethod
    from ._658 import CalculateLeadDeviationAccuracy
    from ._659 import CalculatePitchDeviationAccuracy
    from ._660 import CalculateProfileDeviationAccuracy
    from ._661 import CentreDistanceOffsetMethod
    from ._662 import CutterHeadSlideError
    from ._663 import GearMountingError
    from ._664 import HobbingProcessCalculation
    from ._665 import HobbingProcessGearShape
    from ._666 import HobbingProcessLeadCalculation
    from ._667 import HobbingProcessMarkOnShaft
    from ._668 import HobbingProcessPitchCalculation
    from ._669 import HobbingProcessProfileCalculation
    from ._670 import HobbingProcessSimulationInput
    from ._671 import HobbingProcessSimulationNew
    from ._672 import HobbingProcessSimulationViewModel
    from ._673 import HobbingProcessTotalModificationCalculation
    from ._674 import HobManufactureError
    from ._675 import HobResharpeningError
    from ._676 import ManufacturedQualityGrade
    from ._677 import MountingError
    from ._678 import ProcessCalculation
    from ._679 import ProcessGearShape
    from ._680 import ProcessLeadCalculation
    from ._681 import ProcessPitchCalculation
    from ._682 import ProcessProfileCalculation
    from ._683 import ProcessSimulationInput
    from ._684 import ProcessSimulationNew
    from ._685 import ProcessSimulationViewModel
    from ._686 import ProcessTotalModificationCalculation
    from ._687 import RackManufactureError
    from ._688 import RackMountingError
    from ._689 import WormGrinderManufactureError
    from ._690 import WormGrindingCutterCalculation
    from ._691 import WormGrindingLeadCalculation
    from ._692 import WormGrindingProcessCalculation
    from ._693 import WormGrindingProcessGearShape
    from ._694 import WormGrindingProcessMarkOnShaft
    from ._695 import WormGrindingProcessPitchCalculation
    from ._696 import WormGrindingProcessProfileCalculation
    from ._697 import WormGrindingProcessSimulationInput
    from ._698 import WormGrindingProcessSimulationNew
    from ._699 import WormGrindingProcessSimulationViewModel
    from ._700 import WormGrindingProcessTotalModificationCalculation
else:
    import_structure = {
        "_656": ["ActiveProcessMethod"],
        "_657": ["AnalysisMethod"],
        "_658": ["CalculateLeadDeviationAccuracy"],
        "_659": ["CalculatePitchDeviationAccuracy"],
        "_660": ["CalculateProfileDeviationAccuracy"],
        "_661": ["CentreDistanceOffsetMethod"],
        "_662": ["CutterHeadSlideError"],
        "_663": ["GearMountingError"],
        "_664": ["HobbingProcessCalculation"],
        "_665": ["HobbingProcessGearShape"],
        "_666": ["HobbingProcessLeadCalculation"],
        "_667": ["HobbingProcessMarkOnShaft"],
        "_668": ["HobbingProcessPitchCalculation"],
        "_669": ["HobbingProcessProfileCalculation"],
        "_670": ["HobbingProcessSimulationInput"],
        "_671": ["HobbingProcessSimulationNew"],
        "_672": ["HobbingProcessSimulationViewModel"],
        "_673": ["HobbingProcessTotalModificationCalculation"],
        "_674": ["HobManufactureError"],
        "_675": ["HobResharpeningError"],
        "_676": ["ManufacturedQualityGrade"],
        "_677": ["MountingError"],
        "_678": ["ProcessCalculation"],
        "_679": ["ProcessGearShape"],
        "_680": ["ProcessLeadCalculation"],
        "_681": ["ProcessPitchCalculation"],
        "_682": ["ProcessProfileCalculation"],
        "_683": ["ProcessSimulationInput"],
        "_684": ["ProcessSimulationNew"],
        "_685": ["ProcessSimulationViewModel"],
        "_686": ["ProcessTotalModificationCalculation"],
        "_687": ["RackManufactureError"],
        "_688": ["RackMountingError"],
        "_689": ["WormGrinderManufactureError"],
        "_690": ["WormGrindingCutterCalculation"],
        "_691": ["WormGrindingLeadCalculation"],
        "_692": ["WormGrindingProcessCalculation"],
        "_693": ["WormGrindingProcessGearShape"],
        "_694": ["WormGrindingProcessMarkOnShaft"],
        "_695": ["WormGrindingProcessPitchCalculation"],
        "_696": ["WormGrindingProcessProfileCalculation"],
        "_697": ["WormGrindingProcessSimulationInput"],
        "_698": ["WormGrindingProcessSimulationNew"],
        "_699": ["WormGrindingProcessSimulationViewModel"],
        "_700": ["WormGrindingProcessTotalModificationCalculation"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ActiveProcessMethod",
    "AnalysisMethod",
    "CalculateLeadDeviationAccuracy",
    "CalculatePitchDeviationAccuracy",
    "CalculateProfileDeviationAccuracy",
    "CentreDistanceOffsetMethod",
    "CutterHeadSlideError",
    "GearMountingError",
    "HobbingProcessCalculation",
    "HobbingProcessGearShape",
    "HobbingProcessLeadCalculation",
    "HobbingProcessMarkOnShaft",
    "HobbingProcessPitchCalculation",
    "HobbingProcessProfileCalculation",
    "HobbingProcessSimulationInput",
    "HobbingProcessSimulationNew",
    "HobbingProcessSimulationViewModel",
    "HobbingProcessTotalModificationCalculation",
    "HobManufactureError",
    "HobResharpeningError",
    "ManufacturedQualityGrade",
    "MountingError",
    "ProcessCalculation",
    "ProcessGearShape",
    "ProcessLeadCalculation",
    "ProcessPitchCalculation",
    "ProcessProfileCalculation",
    "ProcessSimulationInput",
    "ProcessSimulationNew",
    "ProcessSimulationViewModel",
    "ProcessTotalModificationCalculation",
    "RackManufactureError",
    "RackMountingError",
    "WormGrinderManufactureError",
    "WormGrindingCutterCalculation",
    "WormGrindingLeadCalculation",
    "WormGrindingProcessCalculation",
    "WormGrindingProcessGearShape",
    "WormGrindingProcessMarkOnShaft",
    "WormGrindingProcessPitchCalculation",
    "WormGrindingProcessProfileCalculation",
    "WormGrindingProcessSimulationInput",
    "WormGrindingProcessSimulationNew",
    "WormGrindingProcessSimulationViewModel",
    "WormGrindingProcessTotalModificationCalculation",
)
