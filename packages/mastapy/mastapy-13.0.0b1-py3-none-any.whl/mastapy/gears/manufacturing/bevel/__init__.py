"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._770 import AbstractTCA
    from ._771 import BevelMachineSettingOptimizationResult
    from ._772 import ConicalFlankDeviationsData
    from ._773 import ConicalGearManufacturingAnalysis
    from ._774 import ConicalGearManufacturingConfig
    from ._775 import ConicalGearMicroGeometryConfig
    from ._776 import ConicalGearMicroGeometryConfigBase
    from ._777 import ConicalMeshedGearManufacturingAnalysis
    from ._778 import ConicalMeshedWheelFlankManufacturingConfig
    from ._779 import ConicalMeshFlankManufacturingConfig
    from ._780 import ConicalMeshFlankMicroGeometryConfig
    from ._781 import ConicalMeshFlankNURBSMicroGeometryConfig
    from ._782 import ConicalMeshManufacturingAnalysis
    from ._783 import ConicalMeshManufacturingConfig
    from ._784 import ConicalMeshMicroGeometryConfig
    from ._785 import ConicalMeshMicroGeometryConfigBase
    from ._786 import ConicalPinionManufacturingConfig
    from ._787 import ConicalPinionMicroGeometryConfig
    from ._788 import ConicalSetManufacturingAnalysis
    from ._789 import ConicalSetManufacturingConfig
    from ._790 import ConicalSetMicroGeometryConfig
    from ._791 import ConicalSetMicroGeometryConfigBase
    from ._792 import ConicalWheelManufacturingConfig
    from ._793 import EaseOffBasedTCA
    from ._794 import FlankMeasurementBorder
    from ._795 import HypoidAdvancedLibrary
    from ._796 import MachineTypes
    from ._797 import ManufacturingMachine
    from ._798 import ManufacturingMachineDatabase
    from ._799 import PinionBevelGeneratingModifiedRollMachineSettings
    from ._800 import PinionBevelGeneratingTiltMachineSettings
    from ._801 import PinionConcave
    from ._802 import PinionConicalMachineSettingsSpecified
    from ._803 import PinionConvex
    from ._804 import PinionFinishMachineSettings
    from ._805 import PinionHypoidFormateTiltMachineSettings
    from ._806 import PinionHypoidGeneratingTiltMachineSettings
    from ._807 import PinionMachineSettingsSMT
    from ._808 import PinionRoughMachineSetting
    from ._809 import Wheel
    from ._810 import WheelFormatMachineTypes
else:
    import_structure = {
        "_770": ["AbstractTCA"],
        "_771": ["BevelMachineSettingOptimizationResult"],
        "_772": ["ConicalFlankDeviationsData"],
        "_773": ["ConicalGearManufacturingAnalysis"],
        "_774": ["ConicalGearManufacturingConfig"],
        "_775": ["ConicalGearMicroGeometryConfig"],
        "_776": ["ConicalGearMicroGeometryConfigBase"],
        "_777": ["ConicalMeshedGearManufacturingAnalysis"],
        "_778": ["ConicalMeshedWheelFlankManufacturingConfig"],
        "_779": ["ConicalMeshFlankManufacturingConfig"],
        "_780": ["ConicalMeshFlankMicroGeometryConfig"],
        "_781": ["ConicalMeshFlankNURBSMicroGeometryConfig"],
        "_782": ["ConicalMeshManufacturingAnalysis"],
        "_783": ["ConicalMeshManufacturingConfig"],
        "_784": ["ConicalMeshMicroGeometryConfig"],
        "_785": ["ConicalMeshMicroGeometryConfigBase"],
        "_786": ["ConicalPinionManufacturingConfig"],
        "_787": ["ConicalPinionMicroGeometryConfig"],
        "_788": ["ConicalSetManufacturingAnalysis"],
        "_789": ["ConicalSetManufacturingConfig"],
        "_790": ["ConicalSetMicroGeometryConfig"],
        "_791": ["ConicalSetMicroGeometryConfigBase"],
        "_792": ["ConicalWheelManufacturingConfig"],
        "_793": ["EaseOffBasedTCA"],
        "_794": ["FlankMeasurementBorder"],
        "_795": ["HypoidAdvancedLibrary"],
        "_796": ["MachineTypes"],
        "_797": ["ManufacturingMachine"],
        "_798": ["ManufacturingMachineDatabase"],
        "_799": ["PinionBevelGeneratingModifiedRollMachineSettings"],
        "_800": ["PinionBevelGeneratingTiltMachineSettings"],
        "_801": ["PinionConcave"],
        "_802": ["PinionConicalMachineSettingsSpecified"],
        "_803": ["PinionConvex"],
        "_804": ["PinionFinishMachineSettings"],
        "_805": ["PinionHypoidFormateTiltMachineSettings"],
        "_806": ["PinionHypoidGeneratingTiltMachineSettings"],
        "_807": ["PinionMachineSettingsSMT"],
        "_808": ["PinionRoughMachineSetting"],
        "_809": ["Wheel"],
        "_810": ["WheelFormatMachineTypes"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractTCA",
    "BevelMachineSettingOptimizationResult",
    "ConicalFlankDeviationsData",
    "ConicalGearManufacturingAnalysis",
    "ConicalGearManufacturingConfig",
    "ConicalGearMicroGeometryConfig",
    "ConicalGearMicroGeometryConfigBase",
    "ConicalMeshedGearManufacturingAnalysis",
    "ConicalMeshedWheelFlankManufacturingConfig",
    "ConicalMeshFlankManufacturingConfig",
    "ConicalMeshFlankMicroGeometryConfig",
    "ConicalMeshFlankNURBSMicroGeometryConfig",
    "ConicalMeshManufacturingAnalysis",
    "ConicalMeshManufacturingConfig",
    "ConicalMeshMicroGeometryConfig",
    "ConicalMeshMicroGeometryConfigBase",
    "ConicalPinionManufacturingConfig",
    "ConicalPinionMicroGeometryConfig",
    "ConicalSetManufacturingAnalysis",
    "ConicalSetManufacturingConfig",
    "ConicalSetMicroGeometryConfig",
    "ConicalSetMicroGeometryConfigBase",
    "ConicalWheelManufacturingConfig",
    "EaseOffBasedTCA",
    "FlankMeasurementBorder",
    "HypoidAdvancedLibrary",
    "MachineTypes",
    "ManufacturingMachine",
    "ManufacturingMachineDatabase",
    "PinionBevelGeneratingModifiedRollMachineSettings",
    "PinionBevelGeneratingTiltMachineSettings",
    "PinionConcave",
    "PinionConicalMachineSettingsSpecified",
    "PinionConvex",
    "PinionFinishMachineSettings",
    "PinionHypoidFormateTiltMachineSettings",
    "PinionHypoidGeneratingTiltMachineSettings",
    "PinionMachineSettingsSMT",
    "PinionRoughMachineSetting",
    "Wheel",
    "WheelFormatMachineTypes",
)
