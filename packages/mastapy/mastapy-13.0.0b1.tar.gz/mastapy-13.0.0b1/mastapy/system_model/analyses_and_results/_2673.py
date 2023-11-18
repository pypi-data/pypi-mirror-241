"""CompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Iterable

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy._internal.python_net import python_net_import
from mastapy.system_model.analyses_and_results import _2617
from mastapy._internal.cast_exception import CastException

_SPRING_DAMPER_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings", "SpringDamperConnection"
)
_TORQUE_CONVERTER_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings",
    "TorqueConverterConnection",
)
_PART_TO_PART_SHEAR_COUPLING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings",
    "PartToPartShearCouplingConnection",
)
_CLUTCH_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings", "ClutchConnection"
)
_CONCEPT_COUPLING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings",
    "ConceptCouplingConnection",
)
_COUPLING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings", "CouplingConnection"
)
_ABSTRACT_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "AbstractShaft"
)
_ABSTRACT_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "AbstractAssembly"
)
_ABSTRACT_SHAFT_OR_HOUSING = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "AbstractShaftOrHousing"
)
_BEARING = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Bearing")
_BOLT = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Bolt")
_BOLTED_JOINT = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "BoltedJoint")
_COMPONENT = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Component")
_CONNECTOR = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Connector")
_DATUM = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Datum")
_EXTERNAL_CAD_MODEL = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "ExternalCADModel"
)
_FE_PART = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "FEPart")
_FLEXIBLE_PIN_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "FlexiblePinAssembly"
)
_ASSEMBLY = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Assembly")
_GUIDE_DXF_MODEL = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "GuideDxfModel"
)
_MASS_DISC = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "MassDisc")
_MEASUREMENT_COMPONENT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "MeasurementComponent"
)
_MOUNTABLE_COMPONENT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "MountableComponent"
)
_OIL_SEAL = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "OilSeal")
_PART = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Part")
_PLANET_CARRIER = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "PlanetCarrier"
)
_POINT_LOAD = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "PointLoad")
_POWER_LOAD = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "PowerLoad")
_ROOT_ASSEMBLY = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "RootAssembly")
_SPECIALISED_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "SpecialisedAssembly"
)
_UNBALANCED_MASS = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "UnbalancedMass"
)
_VIRTUAL_COMPONENT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "VirtualComponent"
)
_SHAFT = python_net_import("SMT.MastaAPI.SystemModel.PartModel.ShaftModel", "Shaft")
_CONCEPT_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ConceptGear"
)
_CONCEPT_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ConceptGearSet"
)
_FACE_GEAR = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Gears", "FaceGear")
_FACE_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "FaceGearSet"
)
_AGMA_GLEASON_CONICAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "AGMAGleasonConicalGear"
)
_AGMA_GLEASON_CONICAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "AGMAGleasonConicalGearSet"
)
_BEVEL_DIFFERENTIAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelDifferentialGear"
)
_BEVEL_DIFFERENTIAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelDifferentialGearSet"
)
_BEVEL_DIFFERENTIAL_PLANET_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelDifferentialPlanetGear"
)
_BEVEL_DIFFERENTIAL_SUN_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelDifferentialSunGear"
)
_BEVEL_GEAR = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelGear")
_BEVEL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelGearSet"
)
_CONICAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ConicalGear"
)
_CONICAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ConicalGearSet"
)
_CYLINDRICAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "CylindricalGear"
)
_CYLINDRICAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "CylindricalGearSet"
)
_CYLINDRICAL_PLANET_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "CylindricalPlanetGear"
)
_GEAR = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Gears", "Gear")
_GEAR_SET = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Gears", "GearSet")
_HYPOID_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "HypoidGear"
)
_HYPOID_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "HypoidGearSet"
)
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "KlingelnbergCycloPalloidConicalGear"
)
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "KlingelnbergCycloPalloidConicalGearSet"
)
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "KlingelnbergCycloPalloidHypoidGear"
)
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "KlingelnbergCycloPalloidHypoidGearSet"
)
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears",
    "KlingelnbergCycloPalloidSpiralBevelGear",
)
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears",
    "KlingelnbergCycloPalloidSpiralBevelGearSet",
)
_PLANETARY_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "PlanetaryGearSet"
)
_SPIRAL_BEVEL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "SpiralBevelGear"
)
_SPIRAL_BEVEL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "SpiralBevelGearSet"
)
_STRAIGHT_BEVEL_DIFF_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelDiffGear"
)
_STRAIGHT_BEVEL_DIFF_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelDiffGearSet"
)
_STRAIGHT_BEVEL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelGear"
)
_STRAIGHT_BEVEL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelGearSet"
)
_STRAIGHT_BEVEL_PLANET_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelPlanetGear"
)
_STRAIGHT_BEVEL_SUN_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelSunGear"
)
_WORM_GEAR = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Gears", "WormGear")
_WORM_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "WormGearSet"
)
_ZEROL_BEVEL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ZerolBevelGear"
)
_ZEROL_BEVEL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ZerolBevelGearSet"
)
_CYCLOIDAL_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Cycloidal", "CycloidalAssembly"
)
_CYCLOIDAL_DISC = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Cycloidal", "CycloidalDisc"
)
_RING_PINS = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Cycloidal", "RingPins"
)
_PART_TO_PART_SHEAR_COUPLING = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "PartToPartShearCoupling"
)
_PART_TO_PART_SHEAR_COUPLING_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "PartToPartShearCouplingHalf"
)
_BELT_DRIVE = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "BeltDrive"
)
_CLUTCH = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Couplings", "Clutch")
_CLUTCH_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "ClutchHalf"
)
_CONCEPT_COUPLING = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "ConceptCoupling"
)
_CONCEPT_COUPLING_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "ConceptCouplingHalf"
)
_COUPLING = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "Coupling"
)
_COUPLING_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "CouplingHalf"
)
_CVT = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Couplings", "CVT")
_CVT_PULLEY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "CVTPulley"
)
_PULLEY = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Couplings", "Pulley")
_SHAFT_HUB_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "ShaftHubConnection"
)
_ROLLING_RING = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "RollingRing"
)
_ROLLING_RING_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "RollingRingAssembly"
)
_SPRING_DAMPER = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SpringDamper"
)
_SPRING_DAMPER_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SpringDamperHalf"
)
_SYNCHRONISER = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "Synchroniser"
)
_SYNCHRONISER_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SynchroniserHalf"
)
_SYNCHRONISER_PART = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SynchroniserPart"
)
_SYNCHRONISER_SLEEVE = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SynchroniserSleeve"
)
_TORQUE_CONVERTER = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "TorqueConverter"
)
_TORQUE_CONVERTER_PUMP = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "TorqueConverterPump"
)
_TORQUE_CONVERTER_TURBINE = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "TorqueConverterTurbine"
)
_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets",
    "ShaftToMountableComponentConnection",
)
_CVT_BELT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "CVTBeltConnection"
)
_BELT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "BeltConnection"
)
_COAXIAL_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "CoaxialConnection"
)
_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "Connection"
)
_INTER_MOUNTABLE_COMPONENT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets",
    "InterMountableComponentConnection",
)
_PLANETARY_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "PlanetaryConnection"
)
_ROLLING_RING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "RollingRingConnection"
)
_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets",
    "AbstractShaftToMountableComponentConnection",
)
_BEVEL_DIFFERENTIAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "BevelDifferentialGearMesh"
)
_CONCEPT_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "ConceptGearMesh"
)
_FACE_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "FaceGearMesh"
)
_STRAIGHT_BEVEL_DIFF_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "StraightBevelDiffGearMesh"
)
_BEVEL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "BevelGearMesh"
)
_CONICAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "ConicalGearMesh"
)
_AGMA_GLEASON_CONICAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "AGMAGleasonConicalGearMesh"
)
_CYLINDRICAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "CylindricalGearMesh"
)
_HYPOID_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "HypoidGearMesh"
)
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears",
    "KlingelnbergCycloPalloidConicalGearMesh",
)
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears",
    "KlingelnbergCycloPalloidHypoidGearMesh",
)
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears",
    "KlingelnbergCycloPalloidSpiralBevelGearMesh",
)
_SPIRAL_BEVEL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "SpiralBevelGearMesh"
)
_STRAIGHT_BEVEL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "StraightBevelGearMesh"
)
_WORM_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "WormGearMesh"
)
_ZEROL_BEVEL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "ZerolBevelGearMesh"
)
_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "GearMesh"
)
_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal",
    "CycloidalDiscCentralBearingConnection",
)
_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal",
    "CycloidalDiscPlanetaryBearingConnection",
)
_RING_PINS_TO_DISC_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal",
    "RingPinsToDiscConnection",
)
_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults", "CompoundMultibodyDynamicsAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import (
        _2348,
        _2350,
        _2346,
        _2340,
        _2342,
        _2344,
    )
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5629,
        _5644,
        _5527,
        _5526,
        _5528,
        _5534,
        _5545,
        _5546,
        _5551,
        _5562,
        _5577,
        _5578,
        _5582,
        _5583,
        _5533,
        _5587,
        _5601,
        _5602,
        _5603,
        _5604,
        _5605,
        _5611,
        _5612,
        _5613,
        _5620,
        _5624,
        _5647,
        _5648,
        _5621,
        _5555,
        _5557,
        _5579,
        _5581,
        _5530,
        _5532,
        _5537,
        _5539,
        _5540,
        _5541,
        _5542,
        _5544,
        _5558,
        _5560,
        _5573,
        _5575,
        _5576,
        _5584,
        _5586,
        _5588,
        _5590,
        _5592,
        _5594,
        _5595,
        _5597,
        _5598,
        _5600,
        _5610,
        _5625,
        _5627,
        _5631,
        _5633,
        _5634,
        _5636,
        _5637,
        _5638,
        _5649,
        _5651,
        _5652,
        _5654,
        _5569,
        _5571,
        _5615,
        _5606,
        _5608,
        _5536,
        _5547,
        _5549,
        _5552,
        _5554,
        _5563,
        _5565,
        _5567,
        _5568,
        _5614,
        _5622,
        _5618,
        _5617,
        _5628,
        _5630,
        _5639,
        _5640,
        _5641,
        _5642,
        _5643,
        _5645,
        _5646,
        _5623,
        _5566,
        _5535,
        _5550,
        _5561,
        _5591,
        _5609,
        _5619,
        _5529,
        _5538,
        _5556,
        _5580,
        _5632,
        _5543,
        _5559,
        _5531,
        _5574,
        _5589,
        _5593,
        _5596,
        _5599,
        _5626,
        _5635,
        _5650,
        _5653,
        _5585,
        _5570,
        _5572,
        _5616,
        _5607,
        _5548,
        _5553,
        _5564,
    )
    from mastapy.system_model.part_model import (
        _2433,
        _2432,
        _2434,
        _2437,
        _2440,
        _2441,
        _2442,
        _2445,
        _2446,
        _2450,
        _2451,
        _2452,
        _2431,
        _2453,
        _2460,
        _2461,
        _2462,
        _2464,
        _2466,
        _2467,
        _2469,
        _2470,
        _2472,
        _2474,
        _2475,
        _2477,
    )
    from mastapy.system_model.part_model.shaft_model import _2480
    from mastapy.system_model.part_model.gears import (
        _2519,
        _2520,
        _2526,
        _2527,
        _2511,
        _2512,
        _2513,
        _2514,
        _2515,
        _2516,
        _2517,
        _2518,
        _2521,
        _2522,
        _2523,
        _2524,
        _2525,
        _2528,
        _2530,
        _2532,
        _2533,
        _2534,
        _2535,
        _2536,
        _2537,
        _2538,
        _2539,
        _2540,
        _2541,
        _2542,
        _2543,
        _2544,
        _2545,
        _2546,
        _2547,
        _2548,
        _2549,
        _2550,
        _2551,
        _2552,
    )
    from mastapy.system_model.part_model.cycloidal import _2566, _2567, _2568
    from mastapy.system_model.part_model.couplings import (
        _2586,
        _2587,
        _2574,
        _2576,
        _2577,
        _2579,
        _2580,
        _2581,
        _2582,
        _2584,
        _2585,
        _2588,
        _2596,
        _2594,
        _2595,
        _2598,
        _2599,
        _2600,
        _2602,
        _2603,
        _2604,
        _2605,
        _2606,
        _2608,
    )
    from mastapy.system_model.connections_and_sockets import (
        _2293,
        _2271,
        _2266,
        _2267,
        _2270,
        _2279,
        _2285,
        _2290,
        _2263,
    )
    from mastapy.system_model.connections_and_sockets.gears import (
        _2299,
        _2303,
        _2309,
        _2323,
        _2301,
        _2305,
        _2297,
        _2307,
        _2313,
        _2316,
        _2317,
        _2318,
        _2321,
        _2325,
        _2327,
        _2329,
        _2311,
    )
    from mastapy.system_model.connections_and_sockets.cycloidal import (
        _2333,
        _2336,
        _2339,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="CompoundMultibodyDynamicsAnalysis")


class CompoundMultibodyDynamicsAnalysis(_2617.CompoundAnalysis):
    """CompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CompoundMultibodyDynamicsAnalysis")

    class _Cast_CompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting CompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "CompoundMultibodyDynamicsAnalysis._Cast_CompoundMultibodyDynamicsAnalysis",
            parent: "CompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def compound_analysis(
            self: "CompoundMultibodyDynamicsAnalysis._Cast_CompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_2617.CompoundAnalysis)

        @property
        def marshal_by_ref_object_permanent(
            self: "CompoundMultibodyDynamicsAnalysis._Cast_CompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy import _7550

            return self._parent._cast(_7550.MarshalByRefObjectPermanent)

        @property
        def compound_multibody_dynamics_analysis(
            self: "CompoundMultibodyDynamicsAnalysis._Cast_CompoundMultibodyDynamicsAnalysis",
        ) -> "CompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "CompoundMultibodyDynamicsAnalysis._Cast_CompoundMultibodyDynamicsAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "CompoundMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @enforce_parameter_types
    def results_for_spring_damper_connection(
        self: Self, design_entity: "_2348.SpringDamperConnection"
    ) -> "Iterable[_5629.SpringDamperConnectionCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.SpringDamperConnectionCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_torque_converter_connection(
        self: Self, design_entity: "_2350.TorqueConverterConnection"
    ) -> "Iterable[_5644.TorqueConverterConnectionCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.TorqueConverterConnectionCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_abstract_shaft(
        self: Self, design_entity: "_2433.AbstractShaft"
    ) -> "Iterable[_5527.AbstractShaftCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.AbstractShaftCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaft)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ABSTRACT_SHAFT](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_abstract_assembly(
        self: Self, design_entity: "_2432.AbstractAssembly"
    ) -> "Iterable[_5526.AbstractAssemblyCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.AbstractAssemblyCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.AbstractAssembly)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ABSTRACT_ASSEMBLY](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_abstract_shaft_or_housing(
        self: Self, design_entity: "_2434.AbstractShaftOrHousing"
    ) -> "Iterable[_5528.AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaftOrHousing)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ABSTRACT_SHAFT_OR_HOUSING](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_bearing(
        self: Self, design_entity: "_2437.Bearing"
    ) -> "Iterable[_5534.BearingCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.BearingCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.Bearing)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BEARING](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_bolt(
        self: Self, design_entity: "_2440.Bolt"
    ) -> "Iterable[_5545.BoltCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.BoltCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.Bolt)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BOLT](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_bolted_joint(
        self: Self, design_entity: "_2441.BoltedJoint"
    ) -> "Iterable[_5546.BoltedJointCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.BoltedJointCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.BoltedJoint)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BOLTED_JOINT](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_component(
        self: Self, design_entity: "_2442.Component"
    ) -> "Iterable[_5551.ComponentCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ComponentCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.Component)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_COMPONENT](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_connector(
        self: Self, design_entity: "_2445.Connector"
    ) -> "Iterable[_5562.ConnectorCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ConnectorCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.Connector)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONNECTOR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_datum(
        self: Self, design_entity: "_2446.Datum"
    ) -> "Iterable[_5577.DatumCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.DatumCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.Datum)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_DATUM](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_external_cad_model(
        self: Self, design_entity: "_2450.ExternalCADModel"
    ) -> "Iterable[_5578.ExternalCADModelCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ExternalCADModelCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.ExternalCADModel)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_EXTERNAL_CAD_MODEL](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_fe_part(
        self: Self, design_entity: "_2451.FEPart"
    ) -> "Iterable[_5582.FEPartCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.FEPartCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.FEPart)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_FE_PART](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_flexible_pin_assembly(
        self: Self, design_entity: "_2452.FlexiblePinAssembly"
    ) -> "Iterable[_5583.FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.FlexiblePinAssembly)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_FLEXIBLE_PIN_ASSEMBLY](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_assembly(
        self: Self, design_entity: "_2431.Assembly"
    ) -> "Iterable[_5533.AssemblyCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.AssemblyCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.Assembly)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ASSEMBLY](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_guide_dxf_model(
        self: Self, design_entity: "_2453.GuideDxfModel"
    ) -> "Iterable[_5587.GuideDxfModelCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.GuideDxfModelCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.GuideDxfModel)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_GUIDE_DXF_MODEL](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_mass_disc(
        self: Self, design_entity: "_2460.MassDisc"
    ) -> "Iterable[_5601.MassDiscCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.MassDiscCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.MassDisc)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_MASS_DISC](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_measurement_component(
        self: Self, design_entity: "_2461.MeasurementComponent"
    ) -> "Iterable[_5602.MeasurementComponentCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.MeasurementComponentCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.MeasurementComponent)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_MEASUREMENT_COMPONENT](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_mountable_component(
        self: Self, design_entity: "_2462.MountableComponent"
    ) -> "Iterable[_5603.MountableComponentCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.MountableComponentCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.MountableComponent)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_MOUNTABLE_COMPONENT](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_oil_seal(
        self: Self, design_entity: "_2464.OilSeal"
    ) -> "Iterable[_5604.OilSealCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.OilSealCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.OilSeal)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_OIL_SEAL](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_part(
        self: Self, design_entity: "_2466.Part"
    ) -> "Iterable[_5605.PartCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.PartCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.Part)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_PART](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_planet_carrier(
        self: Self, design_entity: "_2467.PlanetCarrier"
    ) -> "Iterable[_5611.PlanetCarrierCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.PlanetCarrierCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.PlanetCarrier)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_PLANET_CARRIER](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_point_load(
        self: Self, design_entity: "_2469.PointLoad"
    ) -> "Iterable[_5612.PointLoadCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.PointLoadCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.PointLoad)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_POINT_LOAD](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_power_load(
        self: Self, design_entity: "_2470.PowerLoad"
    ) -> "Iterable[_5613.PowerLoadCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.PowerLoadCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.PowerLoad)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_POWER_LOAD](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_root_assembly(
        self: Self, design_entity: "_2472.RootAssembly"
    ) -> "Iterable[_5620.RootAssemblyCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.RootAssemblyCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.RootAssembly)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ROOT_ASSEMBLY](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_specialised_assembly(
        self: Self, design_entity: "_2474.SpecialisedAssembly"
    ) -> "Iterable[_5624.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.SpecialisedAssembly)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SPECIALISED_ASSEMBLY](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_unbalanced_mass(
        self: Self, design_entity: "_2475.UnbalancedMass"
    ) -> "Iterable[_5647.UnbalancedMassCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.UnbalancedMassCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.UnbalancedMass)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_UNBALANCED_MASS](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_virtual_component(
        self: Self, design_entity: "_2477.VirtualComponent"
    ) -> "Iterable[_5648.VirtualComponentCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.VirtualComponentCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.VirtualComponent)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_VIRTUAL_COMPONENT](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_shaft(
        self: Self, design_entity: "_2480.Shaft"
    ) -> "Iterable[_5621.ShaftCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ShaftCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.shaft_model.Shaft)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SHAFT](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_concept_gear(
        self: Self, design_entity: "_2519.ConceptGear"
    ) -> "Iterable[_5555.ConceptGearCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ConceptGearCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_concept_gear_set(
        self: Self, design_entity: "_2520.ConceptGearSet"
    ) -> "Iterable[_5557.ConceptGearSetCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ConceptGearSetCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_face_gear(
        self: Self, design_entity: "_2526.FaceGear"
    ) -> "Iterable[_5579.FaceGearCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.FaceGearCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_FACE_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_face_gear_set(
        self: Self, design_entity: "_2527.FaceGearSet"
    ) -> "Iterable[_5581.FaceGearSetCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.FaceGearSetCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_FACE_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_agma_gleason_conical_gear(
        self: Self, design_entity: "_2511.AGMAGleasonConicalGear"
    ) -> "Iterable[_5530.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_agma_gleason_conical_gear_set(
        self: Self, design_entity: "_2512.AGMAGleasonConicalGearSet"
    ) -> "Iterable[_5532.AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_bevel_differential_gear(
        self: Self, design_entity: "_2513.BevelDifferentialGear"
    ) -> "Iterable[_5537.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_bevel_differential_gear_set(
        self: Self, design_entity: "_2514.BevelDifferentialGearSet"
    ) -> "Iterable[_5539.BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_bevel_differential_planet_gear(
        self: Self, design_entity: "_2515.BevelDifferentialPlanetGear"
    ) -> "Iterable[_5540.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_PLANET_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_bevel_differential_sun_gear(
        self: Self, design_entity: "_2516.BevelDifferentialSunGear"
    ) -> "Iterable[_5541.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialSunGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_SUN_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_bevel_gear(
        self: Self, design_entity: "_2517.BevelGear"
    ) -> "Iterable[_5542.BevelGearCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.BevelGearCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_bevel_gear_set(
        self: Self, design_entity: "_2518.BevelGearSet"
    ) -> "Iterable[_5544.BevelGearSetCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.BevelGearSetCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_conical_gear(
        self: Self, design_entity: "_2521.ConicalGear"
    ) -> "Iterable[_5558.ConicalGearCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ConicalGearCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_conical_gear_set(
        self: Self, design_entity: "_2522.ConicalGearSet"
    ) -> "Iterable[_5560.ConicalGearSetCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ConicalGearSetCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_cylindrical_gear(
        self: Self, design_entity: "_2523.CylindricalGear"
    ) -> "Iterable[_5573.CylindricalGearCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CylindricalGearCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_cylindrical_gear_set(
        self: Self, design_entity: "_2524.CylindricalGearSet"
    ) -> "Iterable[_5575.CylindricalGearSetCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CylindricalGearSetCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_cylindrical_planet_gear(
        self: Self, design_entity: "_2525.CylindricalPlanetGear"
    ) -> "Iterable[_5576.CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalPlanetGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_PLANET_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_gear(
        self: Self, design_entity: "_2528.Gear"
    ) -> "Iterable[_5584.GearCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.GearCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.Gear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_gear_set(
        self: Self, design_entity: "_2530.GearSet"
    ) -> "Iterable[_5586.GearSetCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.GearSetCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.GearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_hypoid_gear(
        self: Self, design_entity: "_2532.HypoidGear"
    ) -> "Iterable[_5588.HypoidGearCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.HypoidGearCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_hypoid_gear_set(
        self: Self, design_entity: "_2533.HypoidGearSet"
    ) -> "Iterable[_5590.HypoidGearSetCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.HypoidGearSetCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_conical_gear(
        self: Self, design_entity: "_2534.KlingelnbergCycloPalloidConicalGear"
    ) -> "Iterable[_5592.KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_conical_gear_set(
        self: Self, design_entity: "_2535.KlingelnbergCycloPalloidConicalGearSet"
    ) -> "Iterable[_5594.KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[
                _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET
            ](design_entity.wrapped if design_entity else None)
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_hypoid_gear(
        self: Self, design_entity: "_2536.KlingelnbergCycloPalloidHypoidGear"
    ) -> "Iterable[_5595.KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set(
        self: Self, design_entity: "_2537.KlingelnbergCycloPalloidHypoidGearSet"
    ) -> "Iterable[_5597.KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[
                _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET
            ](design_entity.wrapped if design_entity else None)
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear(
        self: Self, design_entity: "_2538.KlingelnbergCycloPalloidSpiralBevelGear"
    ) -> "Iterable[_5598.KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[
                _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR
            ](design_entity.wrapped if design_entity else None)
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(
        self: Self, design_entity: "_2539.KlingelnbergCycloPalloidSpiralBevelGearSet"
    ) -> "Iterable[_5600.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[
                _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET
            ](design_entity.wrapped if design_entity else None)
        )

    @enforce_parameter_types
    def results_for_planetary_gear_set(
        self: Self, design_entity: "_2540.PlanetaryGearSet"
    ) -> "Iterable[_5610.PlanetaryGearSetCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.PlanetaryGearSetCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.PlanetaryGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_PLANETARY_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_spiral_bevel_gear(
        self: Self, design_entity: "_2541.SpiralBevelGear"
    ) -> "Iterable[_5625.SpiralBevelGearCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.SpiralBevelGearCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_spiral_bevel_gear_set(
        self: Self, design_entity: "_2542.SpiralBevelGearSet"
    ) -> "Iterable[_5627.SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_straight_bevel_diff_gear(
        self: Self, design_entity: "_2543.StraightBevelDiffGear"
    ) -> "Iterable[_5631.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_straight_bevel_diff_gear_set(
        self: Self, design_entity: "_2544.StraightBevelDiffGearSet"
    ) -> "Iterable[_5633.StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_straight_bevel_gear(
        self: Self, design_entity: "_2545.StraightBevelGear"
    ) -> "Iterable[_5634.StraightBevelGearCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.StraightBevelGearCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_straight_bevel_gear_set(
        self: Self, design_entity: "_2546.StraightBevelGearSet"
    ) -> "Iterable[_5636.StraightBevelGearSetCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.StraightBevelGearSetCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_straight_bevel_planet_gear(
        self: Self, design_entity: "_2547.StraightBevelPlanetGear"
    ) -> "Iterable[_5637.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelPlanetGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_PLANET_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_straight_bevel_sun_gear(
        self: Self, design_entity: "_2548.StraightBevelSunGear"
    ) -> "Iterable[_5638.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelSunGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_SUN_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_worm_gear(
        self: Self, design_entity: "_2549.WormGear"
    ) -> "Iterable[_5649.WormGearCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.WormGearCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_WORM_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_worm_gear_set(
        self: Self, design_entity: "_2550.WormGearSet"
    ) -> "Iterable[_5651.WormGearSetCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.WormGearSetCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_WORM_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_zerol_bevel_gear(
        self: Self, design_entity: "_2551.ZerolBevelGear"
    ) -> "Iterable[_5652.ZerolBevelGearCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ZerolBevelGearCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGear)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_zerol_bevel_gear_set(
        self: Self, design_entity: "_2552.ZerolBevelGearSet"
    ) -> "Iterable[_5654.ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGearSet)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR_SET](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_cycloidal_assembly(
        self: Self, design_entity: "_2566.CycloidalAssembly"
    ) -> "Iterable[_5569.CycloidalAssemblyCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CycloidalAssemblyCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.cycloidal.CycloidalAssembly)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_ASSEMBLY](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_cycloidal_disc(
        self: Self, design_entity: "_2567.CycloidalDisc"
    ) -> "Iterable[_5571.CycloidalDiscCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CycloidalDiscCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.cycloidal.CycloidalDisc)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_DISC](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_ring_pins(
        self: Self, design_entity: "_2568.RingPins"
    ) -> "Iterable[_5615.RingPinsCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.RingPinsCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.cycloidal.RingPins)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_RING_PINS](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_part_to_part_shear_coupling(
        self: Self, design_entity: "_2586.PartToPartShearCoupling"
    ) -> "Iterable[_5606.PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCoupling)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_part_to_part_shear_coupling_half(
        self: Self, design_entity: "_2587.PartToPartShearCouplingHalf"
    ) -> "Iterable[_5608.PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING_HALF](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_belt_drive(
        self: Self, design_entity: "_2574.BeltDrive"
    ) -> "Iterable[_5536.BeltDriveCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.BeltDriveCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.BeltDrive)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BELT_DRIVE](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_clutch(
        self: Self, design_entity: "_2576.Clutch"
    ) -> "Iterable[_5547.ClutchCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ClutchCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Clutch)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CLUTCH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_clutch_half(
        self: Self, design_entity: "_2577.ClutchHalf"
    ) -> "Iterable[_5549.ClutchHalfCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ClutchHalfCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ClutchHalf)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CLUTCH_HALF](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_concept_coupling(
        self: Self, design_entity: "_2579.ConceptCoupling"
    ) -> "Iterable[_5552.ConceptCouplingCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ConceptCouplingCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCoupling)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_concept_coupling_half(
        self: Self, design_entity: "_2580.ConceptCouplingHalf"
    ) -> "Iterable[_5554.ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCouplingHalf)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING_HALF](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_coupling(
        self: Self, design_entity: "_2581.Coupling"
    ) -> "Iterable[_5563.CouplingCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CouplingCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Coupling)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_COUPLING](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_coupling_half(
        self: Self, design_entity: "_2582.CouplingHalf"
    ) -> "Iterable[_5565.CouplingHalfCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CouplingHalfCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CouplingHalf)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_COUPLING_HALF](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_cvt(
        self: Self, design_entity: "_2584.CVT"
    ) -> "Iterable[_5567.CVTCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CVTCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVT)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CVT](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_cvt_pulley(
        self: Self, design_entity: "_2585.CVTPulley"
    ) -> "Iterable[_5568.CVTPulleyCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CVTPulleyCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVTPulley)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CVT_PULLEY](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_pulley(
        self: Self, design_entity: "_2588.Pulley"
    ) -> "Iterable[_5614.PulleyCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.PulleyCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Pulley)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_PULLEY](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_shaft_hub_connection(
        self: Self, design_entity: "_2596.ShaftHubConnection"
    ) -> "Iterable[_5622.ShaftHubConnectionCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ShaftHubConnectionCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ShaftHubConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SHAFT_HUB_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_rolling_ring(
        self: Self, design_entity: "_2594.RollingRing"
    ) -> "Iterable[_5618.RollingRingCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.RollingRingCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRing)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ROLLING_RING](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_rolling_ring_assembly(
        self: Self, design_entity: "_2595.RollingRingAssembly"
    ) -> "Iterable[_5617.RollingRingAssemblyCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.RollingRingAssemblyCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRingAssembly)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ROLLING_RING_ASSEMBLY](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_spring_damper(
        self: Self, design_entity: "_2598.SpringDamper"
    ) -> "Iterable[_5628.SpringDamperCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.SpringDamperCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamper)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_spring_damper_half(
        self: Self, design_entity: "_2599.SpringDamperHalf"
    ) -> "Iterable[_5630.SpringDamperHalfCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.SpringDamperHalfCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamperHalf)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER_HALF](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_synchroniser(
        self: Self, design_entity: "_2600.Synchroniser"
    ) -> "Iterable[_5639.SynchroniserCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.SynchroniserCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Synchroniser)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SYNCHRONISER](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_synchroniser_half(
        self: Self, design_entity: "_2602.SynchroniserHalf"
    ) -> "Iterable[_5640.SynchroniserHalfCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.SynchroniserHalfCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserHalf)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_HALF](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_synchroniser_part(
        self: Self, design_entity: "_2603.SynchroniserPart"
    ) -> "Iterable[_5641.SynchroniserPartCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.SynchroniserPartCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserPart)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_PART](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_synchroniser_sleeve(
        self: Self, design_entity: "_2604.SynchroniserSleeve"
    ) -> "Iterable[_5642.SynchroniserSleeveCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.SynchroniserSleeveCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserSleeve)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_SLEEVE](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_torque_converter(
        self: Self, design_entity: "_2605.TorqueConverter"
    ) -> "Iterable[_5643.TorqueConverterCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.TorqueConverterCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverter)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_torque_converter_pump(
        self: Self, design_entity: "_2606.TorqueConverterPump"
    ) -> "Iterable[_5645.TorqueConverterPumpCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.TorqueConverterPumpCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterPump)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_PUMP](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_torque_converter_turbine(
        self: Self, design_entity: "_2608.TorqueConverterTurbine"
    ) -> "Iterable[_5646.TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterTurbine)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_TURBINE](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_shaft_to_mountable_component_connection(
        self: Self, design_entity: "_2293.ShaftToMountableComponentConnection"
    ) -> "Iterable[_5623.ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_cvt_belt_connection(
        self: Self, design_entity: "_2271.CVTBeltConnection"
    ) -> "Iterable[_5566.CVTBeltConnectionCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CVTBeltConnectionCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CVTBeltConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CVT_BELT_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_belt_connection(
        self: Self, design_entity: "_2266.BeltConnection"
    ) -> "Iterable[_5535.BeltConnectionCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.BeltConnectionCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.BeltConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BELT_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_coaxial_connection(
        self: Self, design_entity: "_2267.CoaxialConnection"
    ) -> "Iterable[_5550.CoaxialConnectionCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CoaxialConnectionCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CoaxialConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_COAXIAL_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_connection(
        self: Self, design_entity: "_2270.Connection"
    ) -> "Iterable[_5561.ConnectionCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ConnectionCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.Connection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_inter_mountable_component_connection(
        self: Self, design_entity: "_2279.InterMountableComponentConnection"
    ) -> "Iterable[_5591.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.InterMountableComponentConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_INTER_MOUNTABLE_COMPONENT_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_planetary_connection(
        self: Self, design_entity: "_2285.PlanetaryConnection"
    ) -> "Iterable[_5609.PlanetaryConnectionCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.PlanetaryConnectionCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.PlanetaryConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_PLANETARY_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_rolling_ring_connection(
        self: Self, design_entity: "_2290.RollingRingConnection"
    ) -> "Iterable[_5619.RollingRingConnectionCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.RollingRingConnectionCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.RollingRingConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ROLLING_RING_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_abstract_shaft_to_mountable_component_connection(
        self: Self, design_entity: "_2263.AbstractShaftToMountableComponentConnection"
    ) -> "Iterable[_5529.AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.AbstractShaftToMountableComponentConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[
                _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION
            ](design_entity.wrapped if design_entity else None)
        )

    @enforce_parameter_types
    def results_for_bevel_differential_gear_mesh(
        self: Self, design_entity: "_2299.BevelDifferentialGearMesh"
    ) -> "Iterable[_5538.BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_concept_gear_mesh(
        self: Self, design_entity: "_2303.ConceptGearMesh"
    ) -> "Iterable[_5556.ConceptGearMeshCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ConceptGearMeshCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_face_gear_mesh(
        self: Self, design_entity: "_2309.FaceGearMesh"
    ) -> "Iterable[_5580.FaceGearMeshCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.FaceGearMeshCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.FaceGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_FACE_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_straight_bevel_diff_gear_mesh(
        self: Self, design_entity: "_2323.StraightBevelDiffGearMesh"
    ) -> "Iterable[_5632.StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_bevel_gear_mesh(
        self: Self, design_entity: "_2301.BevelGearMesh"
    ) -> "Iterable[_5543.BevelGearMeshCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.BevelGearMeshCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_conical_gear_mesh(
        self: Self, design_entity: "_2305.ConicalGearMesh"
    ) -> "Iterable[_5559.ConicalGearMeshCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ConicalGearMeshCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_agma_gleason_conical_gear_mesh(
        self: Self, design_entity: "_2297.AGMAGleasonConicalGearMesh"
    ) -> "Iterable[_5531.AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_cylindrical_gear_mesh(
        self: Self, design_entity: "_2307.CylindricalGearMesh"
    ) -> "Iterable[_5574.CylindricalGearMeshCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CylindricalGearMeshCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_hypoid_gear_mesh(
        self: Self, design_entity: "_2313.HypoidGearMesh"
    ) -> "Iterable[_5589.HypoidGearMeshCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.HypoidGearMeshCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh(
        self: Self, design_entity: "_2316.KlingelnbergCycloPalloidConicalGearMesh"
    ) -> "Iterable[_5593.KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[
                _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH
            ](design_entity.wrapped if design_entity else None)
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh(
        self: Self, design_entity: "_2317.KlingelnbergCycloPalloidHypoidGearMesh"
    ) -> "Iterable[_5596.KlingelnbergCycloPalloidHypoidGearMeshCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.KlingelnbergCycloPalloidHypoidGearMeshCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[
                _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH
            ](design_entity.wrapped if design_entity else None)
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(
        self: Self, design_entity: "_2318.KlingelnbergCycloPalloidSpiralBevelGearMesh"
    ) -> "Iterable[_5599.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[
                _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH
            ](design_entity.wrapped if design_entity else None)
        )

    @enforce_parameter_types
    def results_for_spiral_bevel_gear_mesh(
        self: Self, design_entity: "_2321.SpiralBevelGearMesh"
    ) -> "Iterable[_5626.SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_straight_bevel_gear_mesh(
        self: Self, design_entity: "_2325.StraightBevelGearMesh"
    ) -> "Iterable[_5635.StraightBevelGearMeshCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.StraightBevelGearMeshCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_worm_gear_mesh(
        self: Self, design_entity: "_2327.WormGearMesh"
    ) -> "Iterable[_5650.WormGearMeshCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.WormGearMeshCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.WormGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_WORM_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_zerol_bevel_gear_mesh(
        self: Self, design_entity: "_2329.ZerolBevelGearMesh"
    ) -> "Iterable[_5653.ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_gear_mesh(
        self: Self, design_entity: "_2311.GearMesh"
    ) -> "Iterable[_5585.GearMeshCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.GearMeshCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.GearMesh)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_GEAR_MESH](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_cycloidal_disc_central_bearing_connection(
        self: Self, design_entity: "_2333.CycloidalDiscCentralBearingConnection"
    ) -> "Iterable[_5570.CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscCentralBearingConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[
                _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION
            ](design_entity.wrapped if design_entity else None)
        )

    @enforce_parameter_types
    def results_for_cycloidal_disc_planetary_bearing_connection(
        self: Self, design_entity: "_2336.CycloidalDiscPlanetaryBearingConnection"
    ) -> "Iterable[_5572.CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscPlanetaryBearingConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[
                _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION
            ](design_entity.wrapped if design_entity else None)
        )

    @enforce_parameter_types
    def results_for_ring_pins_to_disc_connection(
        self: Self, design_entity: "_2339.RingPinsToDiscConnection"
    ) -> "Iterable[_5616.RingPinsToDiscConnectionCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.RingPinsToDiscConnectionCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_RING_PINS_TO_DISC_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_part_to_part_shear_coupling_connection(
        self: Self, design_entity: "_2346.PartToPartShearCouplingConnection"
    ) -> "Iterable[_5607.PartToPartShearCouplingConnectionCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.PartToPartShearCouplingConnectionCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_clutch_connection(
        self: Self, design_entity: "_2340.ClutchConnection"
    ) -> "Iterable[_5548.ClutchConnectionCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ClutchConnectionCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ClutchConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CLUTCH_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_concept_coupling_connection(
        self: Self, design_entity: "_2342.ConceptCouplingConnection"
    ) -> "Iterable[_5553.ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @enforce_parameter_types
    def results_for_coupling_connection(
        self: Self, design_entity: "_2344.CouplingConnection"
    ) -> "Iterable[_5564.CouplingConnectionCompoundMultibodyDynamicsAnalysis]":
        """Iterable[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CouplingConnectionCompoundMultibodyDynamicsAnalysis]

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.CouplingConnection)
        """
        return conversion.pn_to_mp_objects_in_iterable(
            self.wrapped.ResultsFor.Overloads[_COUPLING_CONNECTION](
                design_entity.wrapped if design_entity else None
            )
        )

    @property
    def cast_to(
        self: Self,
    ) -> "CompoundMultibodyDynamicsAnalysis._Cast_CompoundMultibodyDynamicsAnalysis":
        return self._Cast_CompoundMultibodyDynamicsAnalysis(self)
