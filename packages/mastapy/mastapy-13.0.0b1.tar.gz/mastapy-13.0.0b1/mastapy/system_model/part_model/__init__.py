"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2431 import Assembly
    from ._2432 import AbstractAssembly
    from ._2433 import AbstractShaft
    from ._2434 import AbstractShaftOrHousing
    from ._2435 import AGMALoadSharingTableApplicationLevel
    from ._2436 import AxialInternalClearanceTolerance
    from ._2437 import Bearing
    from ._2438 import BearingF0InputMethod
    from ._2439 import BearingRaceMountingOptions
    from ._2440 import Bolt
    from ._2441 import BoltedJoint
    from ._2442 import Component
    from ._2443 import ComponentsConnectedResult
    from ._2444 import ConnectedSockets
    from ._2445 import Connector
    from ._2446 import Datum
    from ._2447 import ElectricMachineSearchRegionSpecificationMethod
    from ._2448 import EnginePartLoad
    from ._2449 import EngineSpeed
    from ._2450 import ExternalCADModel
    from ._2451 import FEPart
    from ._2452 import FlexiblePinAssembly
    from ._2453 import GuideDxfModel
    from ._2454 import GuideImage
    from ._2455 import GuideModelUsage
    from ._2456 import InnerBearingRaceMountingOptions
    from ._2457 import InternalClearanceTolerance
    from ._2458 import LoadSharingModes
    from ._2459 import LoadSharingSettings
    from ._2460 import MassDisc
    from ._2461 import MeasurementComponent
    from ._2462 import MountableComponent
    from ._2463 import OilLevelSpecification
    from ._2464 import OilSeal
    from ._2465 import OuterBearingRaceMountingOptions
    from ._2466 import Part
    from ._2467 import PlanetCarrier
    from ._2468 import PlanetCarrierSettings
    from ._2469 import PointLoad
    from ._2470 import PowerLoad
    from ._2471 import RadialInternalClearanceTolerance
    from ._2472 import RootAssembly
    from ._2473 import ShaftDiameterModificationDueToRollingBearingRing
    from ._2474 import SpecialisedAssembly
    from ._2475 import UnbalancedMass
    from ._2476 import UnbalancedMassInclusionOption
    from ._2477 import VirtualComponent
    from ._2478 import WindTurbineBladeModeDetails
    from ._2479 import WindTurbineSingleBladeDetails
else:
    import_structure = {
        "_2431": ["Assembly"],
        "_2432": ["AbstractAssembly"],
        "_2433": ["AbstractShaft"],
        "_2434": ["AbstractShaftOrHousing"],
        "_2435": ["AGMALoadSharingTableApplicationLevel"],
        "_2436": ["AxialInternalClearanceTolerance"],
        "_2437": ["Bearing"],
        "_2438": ["BearingF0InputMethod"],
        "_2439": ["BearingRaceMountingOptions"],
        "_2440": ["Bolt"],
        "_2441": ["BoltedJoint"],
        "_2442": ["Component"],
        "_2443": ["ComponentsConnectedResult"],
        "_2444": ["ConnectedSockets"],
        "_2445": ["Connector"],
        "_2446": ["Datum"],
        "_2447": ["ElectricMachineSearchRegionSpecificationMethod"],
        "_2448": ["EnginePartLoad"],
        "_2449": ["EngineSpeed"],
        "_2450": ["ExternalCADModel"],
        "_2451": ["FEPart"],
        "_2452": ["FlexiblePinAssembly"],
        "_2453": ["GuideDxfModel"],
        "_2454": ["GuideImage"],
        "_2455": ["GuideModelUsage"],
        "_2456": ["InnerBearingRaceMountingOptions"],
        "_2457": ["InternalClearanceTolerance"],
        "_2458": ["LoadSharingModes"],
        "_2459": ["LoadSharingSettings"],
        "_2460": ["MassDisc"],
        "_2461": ["MeasurementComponent"],
        "_2462": ["MountableComponent"],
        "_2463": ["OilLevelSpecification"],
        "_2464": ["OilSeal"],
        "_2465": ["OuterBearingRaceMountingOptions"],
        "_2466": ["Part"],
        "_2467": ["PlanetCarrier"],
        "_2468": ["PlanetCarrierSettings"],
        "_2469": ["PointLoad"],
        "_2470": ["PowerLoad"],
        "_2471": ["RadialInternalClearanceTolerance"],
        "_2472": ["RootAssembly"],
        "_2473": ["ShaftDiameterModificationDueToRollingBearingRing"],
        "_2474": ["SpecialisedAssembly"],
        "_2475": ["UnbalancedMass"],
        "_2476": ["UnbalancedMassInclusionOption"],
        "_2477": ["VirtualComponent"],
        "_2478": ["WindTurbineBladeModeDetails"],
        "_2479": ["WindTurbineSingleBladeDetails"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Assembly",
    "AbstractAssembly",
    "AbstractShaft",
    "AbstractShaftOrHousing",
    "AGMALoadSharingTableApplicationLevel",
    "AxialInternalClearanceTolerance",
    "Bearing",
    "BearingF0InputMethod",
    "BearingRaceMountingOptions",
    "Bolt",
    "BoltedJoint",
    "Component",
    "ComponentsConnectedResult",
    "ConnectedSockets",
    "Connector",
    "Datum",
    "ElectricMachineSearchRegionSpecificationMethod",
    "EnginePartLoad",
    "EngineSpeed",
    "ExternalCADModel",
    "FEPart",
    "FlexiblePinAssembly",
    "GuideDxfModel",
    "GuideImage",
    "GuideModelUsage",
    "InnerBearingRaceMountingOptions",
    "InternalClearanceTolerance",
    "LoadSharingModes",
    "LoadSharingSettings",
    "MassDisc",
    "MeasurementComponent",
    "MountableComponent",
    "OilLevelSpecification",
    "OilSeal",
    "OuterBearingRaceMountingOptions",
    "Part",
    "PlanetCarrier",
    "PlanetCarrierSettings",
    "PointLoad",
    "PowerLoad",
    "RadialInternalClearanceTolerance",
    "RootAssembly",
    "ShaftDiameterModificationDueToRollingBearingRing",
    "SpecialisedAssembly",
    "UnbalancedMass",
    "UnbalancedMassInclusionOption",
    "VirtualComponent",
    "WindTurbineBladeModeDetails",
    "WindTurbineSingleBladeDetails",
)
