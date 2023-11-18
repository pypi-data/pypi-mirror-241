"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2353 import AlignConnectedComponentOptions
    from ._2354 import AlignmentMethod
    from ._2355 import AlignmentMethodForRaceBearing
    from ._2356 import AlignmentUsingAxialNodePositions
    from ._2357 import AngleSource
    from ._2358 import BaseFEWithSelection
    from ._2359 import BatchOperations
    from ._2360 import BearingNodeAlignmentOption
    from ._2361 import BearingNodeOption
    from ._2362 import BearingRaceNodeLink
    from ._2363 import BearingRacePosition
    from ._2364 import ComponentOrientationOption
    from ._2365 import ContactPairWithSelection
    from ._2366 import CoordinateSystemWithSelection
    from ._2367 import CreateConnectedComponentOptions
    from ._2368 import DegreeOfFreedomBoundaryCondition
    from ._2369 import DegreeOfFreedomBoundaryConditionAngular
    from ._2370 import DegreeOfFreedomBoundaryConditionLinear
    from ._2371 import ElectricMachineDataSet
    from ._2372 import ElectricMachineDynamicLoadData
    from ._2373 import ElementFaceGroupWithSelection
    from ._2374 import ElementPropertiesWithSelection
    from ._2375 import FEEntityGroupWithSelection
    from ._2376 import FEExportSettings
    from ._2377 import FEPartDRIVASurfaceSelection
    from ._2378 import FEPartWithBatchOptions
    from ._2379 import FEStiffnessGeometry
    from ._2380 import FEStiffnessTester
    from ._2381 import FESubstructure
    from ._2382 import FESubstructureExportOptions
    from ._2383 import FESubstructureNode
    from ._2384 import FESubstructureNodeModeShape
    from ._2385 import FESubstructureNodeModeShapes
    from ._2386 import FESubstructureType
    from ._2387 import FESubstructureWithBatchOptions
    from ._2388 import FESubstructureWithSelection
    from ._2389 import FESubstructureWithSelectionComponents
    from ._2390 import FESubstructureWithSelectionForHarmonicAnalysis
    from ._2391 import FESubstructureWithSelectionForModalAnalysis
    from ._2392 import FESubstructureWithSelectionForStaticAnalysis
    from ._2393 import GearMeshingOptions
    from ._2394 import IndependentMASTACreatedCondensationNode
    from ._2395 import LinkComponentAxialPositionErrorReporter
    from ._2396 import LinkNodeSource
    from ._2397 import MaterialPropertiesWithSelection
    from ._2398 import NodeBoundaryConditionStaticAnalysis
    from ._2399 import NodeGroupWithSelection
    from ._2400 import NodeSelectionDepthOption
    from ._2401 import OptionsWhenExternalFEFileAlreadyExists
    from ._2402 import PerLinkExportOptions
    from ._2403 import PerNodeExportOptions
    from ._2404 import RaceBearingFE
    from ._2405 import RaceBearingFESystemDeflection
    from ._2406 import RaceBearingFEWithSelection
    from ._2407 import ReplacedShaftSelectionHelper
    from ._2408 import SystemDeflectionFEExportOptions
    from ._2409 import ThermalExpansionOption
else:
    import_structure = {
        "_2353": ["AlignConnectedComponentOptions"],
        "_2354": ["AlignmentMethod"],
        "_2355": ["AlignmentMethodForRaceBearing"],
        "_2356": ["AlignmentUsingAxialNodePositions"],
        "_2357": ["AngleSource"],
        "_2358": ["BaseFEWithSelection"],
        "_2359": ["BatchOperations"],
        "_2360": ["BearingNodeAlignmentOption"],
        "_2361": ["BearingNodeOption"],
        "_2362": ["BearingRaceNodeLink"],
        "_2363": ["BearingRacePosition"],
        "_2364": ["ComponentOrientationOption"],
        "_2365": ["ContactPairWithSelection"],
        "_2366": ["CoordinateSystemWithSelection"],
        "_2367": ["CreateConnectedComponentOptions"],
        "_2368": ["DegreeOfFreedomBoundaryCondition"],
        "_2369": ["DegreeOfFreedomBoundaryConditionAngular"],
        "_2370": ["DegreeOfFreedomBoundaryConditionLinear"],
        "_2371": ["ElectricMachineDataSet"],
        "_2372": ["ElectricMachineDynamicLoadData"],
        "_2373": ["ElementFaceGroupWithSelection"],
        "_2374": ["ElementPropertiesWithSelection"],
        "_2375": ["FEEntityGroupWithSelection"],
        "_2376": ["FEExportSettings"],
        "_2377": ["FEPartDRIVASurfaceSelection"],
        "_2378": ["FEPartWithBatchOptions"],
        "_2379": ["FEStiffnessGeometry"],
        "_2380": ["FEStiffnessTester"],
        "_2381": ["FESubstructure"],
        "_2382": ["FESubstructureExportOptions"],
        "_2383": ["FESubstructureNode"],
        "_2384": ["FESubstructureNodeModeShape"],
        "_2385": ["FESubstructureNodeModeShapes"],
        "_2386": ["FESubstructureType"],
        "_2387": ["FESubstructureWithBatchOptions"],
        "_2388": ["FESubstructureWithSelection"],
        "_2389": ["FESubstructureWithSelectionComponents"],
        "_2390": ["FESubstructureWithSelectionForHarmonicAnalysis"],
        "_2391": ["FESubstructureWithSelectionForModalAnalysis"],
        "_2392": ["FESubstructureWithSelectionForStaticAnalysis"],
        "_2393": ["GearMeshingOptions"],
        "_2394": ["IndependentMASTACreatedCondensationNode"],
        "_2395": ["LinkComponentAxialPositionErrorReporter"],
        "_2396": ["LinkNodeSource"],
        "_2397": ["MaterialPropertiesWithSelection"],
        "_2398": ["NodeBoundaryConditionStaticAnalysis"],
        "_2399": ["NodeGroupWithSelection"],
        "_2400": ["NodeSelectionDepthOption"],
        "_2401": ["OptionsWhenExternalFEFileAlreadyExists"],
        "_2402": ["PerLinkExportOptions"],
        "_2403": ["PerNodeExportOptions"],
        "_2404": ["RaceBearingFE"],
        "_2405": ["RaceBearingFESystemDeflection"],
        "_2406": ["RaceBearingFEWithSelection"],
        "_2407": ["ReplacedShaftSelectionHelper"],
        "_2408": ["SystemDeflectionFEExportOptions"],
        "_2409": ["ThermalExpansionOption"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AlignConnectedComponentOptions",
    "AlignmentMethod",
    "AlignmentMethodForRaceBearing",
    "AlignmentUsingAxialNodePositions",
    "AngleSource",
    "BaseFEWithSelection",
    "BatchOperations",
    "BearingNodeAlignmentOption",
    "BearingNodeOption",
    "BearingRaceNodeLink",
    "BearingRacePosition",
    "ComponentOrientationOption",
    "ContactPairWithSelection",
    "CoordinateSystemWithSelection",
    "CreateConnectedComponentOptions",
    "DegreeOfFreedomBoundaryCondition",
    "DegreeOfFreedomBoundaryConditionAngular",
    "DegreeOfFreedomBoundaryConditionLinear",
    "ElectricMachineDataSet",
    "ElectricMachineDynamicLoadData",
    "ElementFaceGroupWithSelection",
    "ElementPropertiesWithSelection",
    "FEEntityGroupWithSelection",
    "FEExportSettings",
    "FEPartDRIVASurfaceSelection",
    "FEPartWithBatchOptions",
    "FEStiffnessGeometry",
    "FEStiffnessTester",
    "FESubstructure",
    "FESubstructureExportOptions",
    "FESubstructureNode",
    "FESubstructureNodeModeShape",
    "FESubstructureNodeModeShapes",
    "FESubstructureType",
    "FESubstructureWithBatchOptions",
    "FESubstructureWithSelection",
    "FESubstructureWithSelectionComponents",
    "FESubstructureWithSelectionForHarmonicAnalysis",
    "FESubstructureWithSelectionForModalAnalysis",
    "FESubstructureWithSelectionForStaticAnalysis",
    "GearMeshingOptions",
    "IndependentMASTACreatedCondensationNode",
    "LinkComponentAxialPositionErrorReporter",
    "LinkNodeSource",
    "MaterialPropertiesWithSelection",
    "NodeBoundaryConditionStaticAnalysis",
    "NodeGroupWithSelection",
    "NodeSelectionDepthOption",
    "OptionsWhenExternalFEFileAlreadyExists",
    "PerLinkExportOptions",
    "PerNodeExportOptions",
    "RaceBearingFE",
    "RaceBearingFESystemDeflection",
    "RaceBearingFEWithSelection",
    "ReplacedShaftSelectionHelper",
    "SystemDeflectionFEExportOptions",
    "ThermalExpansionOption",
)
