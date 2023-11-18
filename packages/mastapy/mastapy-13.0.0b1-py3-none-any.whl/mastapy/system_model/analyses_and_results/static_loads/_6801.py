"""LoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable, enum_with_selected_value
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.bearings.bearing_results.rolling import _1970
from mastapy.system_model import _2212
from mastapy.gears import _335
from mastapy.nodal_analysis.nodal_entities import _130
from mastapy.bearings.bearing_results.rolling.iso_rating_results import _2107
from mastapy._internal.python_net import python_net_import
from mastapy.system_model.analyses_and_results import _2648
from mastapy._internal.cast_exception import CastException

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
_SPRING_DAMPER_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings", "SpringDamperConnection"
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
_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "LoadCase"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _1965, _2067
    from mastapy.system_model import _2208, _2222
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6808,
        _6937,
        _6976,
        _6970,
        _6805,
        _6804,
        _6806,
        _6817,
        _6829,
        _6828,
        _6835,
        _6848,
        _6867,
        _6881,
        _6885,
        _6886,
        _6816,
        _6894,
        _6919,
        _6920,
        _6922,
        _6924,
        _6926,
        _6933,
        _6936,
        _6946,
        _6950,
        _6978,
        _6979,
        _6948,
        _6839,
        _6841,
        _6882,
        _6884,
        _6811,
        _6813,
        _6820,
        _6822,
        _6823,
        _6824,
        _6825,
        _6827,
        _6842,
        _6846,
        _6859,
        _6863,
        _6864,
        _6888,
        _6893,
        _6903,
        _6905,
        _6910,
        _6912,
        _6913,
        _6915,
        _6916,
        _6918,
        _6931,
        _6951,
        _6953,
        _6957,
        _6959,
        _6960,
        _6962,
        _6963,
        _6964,
        _6980,
        _6982,
        _6983,
        _6985,
        _6855,
        _6857,
        _6941,
        _6929,
        _6928,
        _6819,
        _6832,
        _6831,
        _6838,
        _6837,
        _6851,
        _6850,
        _6853,
        _6854,
        _6938,
        _6947,
        _6945,
        _6943,
        _6956,
        _6955,
        _6966,
        _6965,
        _6967,
        _6968,
        _6971,
        _6972,
        _6973,
        _6949,
        _6852,
        _6818,
        _6834,
        _6847,
        _6909,
        _6930,
        _6944,
        _6807,
        _6821,
        _6840,
        _6883,
        _6958,
        _6826,
        _6844,
        _6812,
        _6861,
        _6904,
        _6911,
        _6914,
        _6917,
        _6952,
        _6961,
        _6981,
        _6984,
        _6890,
        _6856,
        _6858,
        _6942,
        _6927,
        _6830,
        _6836,
        _6849,
        _6954,
    )
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4386
    from mastapy.system_model.connections_and_sockets.couplings import (
        _2350,
        _2346,
        _2340,
        _2342,
        _2344,
        _2348,
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
__all__ = ("LoadCase",)


Self = TypeVar("Self", bound="LoadCase")


class LoadCase(_2648.Context):
    """LoadCase

    This is a mastapy class.
    """

    TYPE = _LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadCase")

    class _Cast_LoadCase:
        """Special nested class for casting LoadCase to subclasses."""

        def __init__(self: "LoadCase._Cast_LoadCase", parent: "LoadCase"):
            self._parent = parent

        @property
        def context(self: "LoadCase._Cast_LoadCase"):
            return self._parent._cast(_2648.Context)

        @property
        def parametric_study_static_load(self: "LoadCase._Cast_LoadCase"):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4384,
            )

            return self._parent._cast(_4384.ParametricStudyStaticLoad)

        @property
        def harmonic_analysis_with_varying_stiffness_static_load_case(
            self: "LoadCase._Cast_LoadCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5767,
            )

            return self._parent._cast(
                _5767.HarmonicAnalysisWithVaryingStiffnessStaticLoadCase
            )

        @property
        def static_load_case(self: "LoadCase._Cast_LoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6802

            return self._parent._cast(_6802.StaticLoadCase)

        @property
        def time_series_load_case(self: "LoadCase._Cast_LoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6803

            return self._parent._cast(_6803.TimeSeriesLoadCase)

        @property
        def advanced_time_stepping_analysis_for_modulation_static_load_case(
            self: "LoadCase._Cast_LoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6809

            return self._parent._cast(
                _6809.AdvancedTimeSteppingAnalysisForModulationStaticLoadCase
            )

        @property
        def load_case(self: "LoadCase._Cast_LoadCase") -> "LoadCase":
            return self._parent

        def __getattr__(self: "LoadCase._Cast_LoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def air_density(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.AirDensity

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @air_density.setter
    @enforce_parameter_types
    def air_density(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.AirDensity = value

    @property
    def ball_bearing_contact_calculation(
        self: Self,
    ) -> "_1965.BallBearingContactCalculation":
        """mastapy.bearings.bearing_results.rolling.BallBearingContactCalculation"""
        temp = self.wrapped.BallBearingContactCalculation

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Bearings.BearingResults.Rolling.BallBearingContactCalculation",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.bearings.bearing_results.rolling._1965",
            "BallBearingContactCalculation",
        )(value)

    @ball_bearing_contact_calculation.setter
    @enforce_parameter_types
    def ball_bearing_contact_calculation(
        self: Self, value: "_1965.BallBearingContactCalculation"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Bearings.BearingResults.Rolling.BallBearingContactCalculation",
        )
        self.wrapped.BallBearingContactCalculation = value

    @property
    def ball_bearing_friction_model_for_gyroscopic_moment(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_FrictionModelForGyroscopicMoment":
        """EnumWithSelectedValue[mastapy.bearings.bearing_results.rolling.FrictionModelForGyroscopicMoment]"""
        temp = self.wrapped.BallBearingFrictionModelForGyroscopicMoment

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_FrictionModelForGyroscopicMoment.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @ball_bearing_friction_model_for_gyroscopic_moment.setter
    @enforce_parameter_types
    def ball_bearing_friction_model_for_gyroscopic_moment(
        self: Self, value: "_1970.FrictionModelForGyroscopicMoment"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_FrictionModelForGyroscopicMoment.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.BallBearingFrictionModelForGyroscopicMoment = value

    @property
    def characteristic_specific_acoustic_impedance(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.CharacteristicSpecificAcousticImpedance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @characteristic_specific_acoustic_impedance.setter
    @enforce_parameter_types
    def characteristic_specific_acoustic_impedance(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.CharacteristicSpecificAcousticImpedance = value

    @property
    def energy_convergence_absolute_tolerance(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.EnergyConvergenceAbsoluteTolerance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @energy_convergence_absolute_tolerance.setter
    @enforce_parameter_types
    def energy_convergence_absolute_tolerance(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.EnergyConvergenceAbsoluteTolerance = value

    @property
    def expand_grounded_nodes_for_thermal_effects(
        self: Self,
    ) -> "overridable.Overridable_bool":
        """Overridable[bool]"""
        temp = self.wrapped.ExpandGroundedNodesForThermalEffects

        if temp is None:
            return False

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_bool"
        )(temp)

    @expand_grounded_nodes_for_thermal_effects.setter
    @enforce_parameter_types
    def expand_grounded_nodes_for_thermal_effects(
        self: Self, value: "Union[bool, Tuple[bool, bool]]"
    ):
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else False, is_overridden
        )
        self.wrapped.ExpandGroundedNodesForThermalEffects = value

    @property
    def force_multiple_mesh_nodes_for_unloaded_cylindrical_gear_meshes(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = self.wrapped.ForceMultipleMeshNodesForUnloadedCylindricalGearMeshes

        if temp is None:
            return False

        return temp

    @force_multiple_mesh_nodes_for_unloaded_cylindrical_gear_meshes.setter
    @enforce_parameter_types
    def force_multiple_mesh_nodes_for_unloaded_cylindrical_gear_meshes(
        self: Self, value: "bool"
    ):
        self.wrapped.ForceMultipleMeshNodesForUnloadedCylindricalGearMeshes = (
            bool(value) if value is not None else False
        )

    @property
    def gear_mesh_nodes_per_unit_length_to_diameter_ratio(self: Self) -> "float":
        """float"""
        temp = self.wrapped.GearMeshNodesPerUnitLengthToDiameterRatio

        if temp is None:
            return 0.0

        return temp

    @gear_mesh_nodes_per_unit_length_to_diameter_ratio.setter
    @enforce_parameter_types
    def gear_mesh_nodes_per_unit_length_to_diameter_ratio(self: Self, value: "float"):
        self.wrapped.GearMeshNodesPerUnitLengthToDiameterRatio = (
            float(value) if value is not None else 0.0
        )

    @property
    def grid_refinement_factor_contact_width(
        self: Self,
    ) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.GridRefinementFactorContactWidth

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @grid_refinement_factor_contact_width.setter
    @enforce_parameter_types
    def grid_refinement_factor_contact_width(
        self: Self, value: "Union[int, Tuple[int, bool]]"
    ):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.GridRefinementFactorContactWidth = value

    @property
    def grid_refinement_factor_rib_height(self: Self) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.GridRefinementFactorRibHeight

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @grid_refinement_factor_rib_height.setter
    @enforce_parameter_types
    def grid_refinement_factor_rib_height(
        self: Self, value: "Union[int, Tuple[int, bool]]"
    ):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.GridRefinementFactorRibHeight = value

    @property
    def hypoid_gear_wind_up_removal_method_for_misalignments(
        self: Self,
    ) -> "_2208.HypoidWindUpRemovalMethod":
        """mastapy.system_model.HypoidWindUpRemovalMethod"""
        temp = self.wrapped.HypoidGearWindUpRemovalMethodForMisalignments

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.SystemModel.HypoidWindUpRemovalMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model._2208", "HypoidWindUpRemovalMethod"
        )(value)

    @hypoid_gear_wind_up_removal_method_for_misalignments.setter
    @enforce_parameter_types
    def hypoid_gear_wind_up_removal_method_for_misalignments(
        self: Self, value: "_2208.HypoidWindUpRemovalMethod"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.SystemModel.HypoidWindUpRemovalMethod"
        )
        self.wrapped.HypoidGearWindUpRemovalMethodForMisalignments = value

    @property
    def include_bearing_centrifugal_ring_expansion(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeBearingCentrifugalRingExpansion

        if temp is None:
            return False

        return temp

    @include_bearing_centrifugal_ring_expansion.setter
    @enforce_parameter_types
    def include_bearing_centrifugal_ring_expansion(self: Self, value: "bool"):
        self.wrapped.IncludeBearingCentrifugalRingExpansion = (
            bool(value) if value is not None else False
        )

    @property
    def include_bearing_centrifugal(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeBearingCentrifugal

        if temp is None:
            return False

        return temp

    @include_bearing_centrifugal.setter
    @enforce_parameter_types
    def include_bearing_centrifugal(self: Self, value: "bool"):
        self.wrapped.IncludeBearingCentrifugal = (
            bool(value) if value is not None else False
        )

    @property
    def include_fitting_effects(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeFittingEffects

        if temp is None:
            return False

        return temp

    @include_fitting_effects.setter
    @enforce_parameter_types
    def include_fitting_effects(self: Self, value: "bool"):
        self.wrapped.IncludeFittingEffects = bool(value) if value is not None else False

    @property
    def include_gear_blank_elastic_distortion(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeGearBlankElasticDistortion

        if temp is None:
            return False

        return temp

    @include_gear_blank_elastic_distortion.setter
    @enforce_parameter_types
    def include_gear_blank_elastic_distortion(self: Self, value: "bool"):
        self.wrapped.IncludeGearBlankElasticDistortion = (
            bool(value) if value is not None else False
        )

    @property
    def include_gravity(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeGravity

        if temp is None:
            return False

        return temp

    @include_gravity.setter
    @enforce_parameter_types
    def include_gravity(self: Self, value: "bool"):
        self.wrapped.IncludeGravity = bool(value) if value is not None else False

    @property
    def include_inner_race_distortion_for_flexible_pin_spindle(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeInnerRaceDistortionForFlexiblePinSpindle

        if temp is None:
            return False

        return temp

    @include_inner_race_distortion_for_flexible_pin_spindle.setter
    @enforce_parameter_types
    def include_inner_race_distortion_for_flexible_pin_spindle(
        self: Self, value: "bool"
    ):
        self.wrapped.IncludeInnerRaceDistortionForFlexiblePinSpindle = (
            bool(value) if value is not None else False
        )

    @property
    def include_planetary_centrifugal(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludePlanetaryCentrifugal

        if temp is None:
            return False

        return temp

    @include_planetary_centrifugal.setter
    @enforce_parameter_types
    def include_planetary_centrifugal(self: Self, value: "bool"):
        self.wrapped.IncludePlanetaryCentrifugal = (
            bool(value) if value is not None else False
        )

    @property
    def include_profile_modifications_and_manufacturing_errors_during_cycloidal_analysis(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = (
            self.wrapped.IncludeProfileModificationsAndManufacturingErrorsDuringCycloidalAnalysis
        )

        if temp is None:
            return False

        return temp

    @include_profile_modifications_and_manufacturing_errors_during_cycloidal_analysis.setter
    @enforce_parameter_types
    def include_profile_modifications_and_manufacturing_errors_during_cycloidal_analysis(
        self: Self, value: "bool"
    ):
        self.wrapped.IncludeProfileModificationsAndManufacturingErrorsDuringCycloidalAnalysis = (
            bool(value) if value is not None else False
        )

    @property
    def include_rib_contact_analysis(self: Self) -> "overridable.Overridable_bool":
        """Overridable[bool]"""
        temp = self.wrapped.IncludeRibContactAnalysis

        if temp is None:
            return False

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_bool"
        )(temp)

    @include_rib_contact_analysis.setter
    @enforce_parameter_types
    def include_rib_contact_analysis(
        self: Self, value: "Union[bool, Tuple[bool, bool]]"
    ):
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else False, is_overridden
        )
        self.wrapped.IncludeRibContactAnalysis = value

    @property
    def include_ring_ovality(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeRingOvality

        if temp is None:
            return False

        return temp

    @include_ring_ovality.setter
    @enforce_parameter_types
    def include_ring_ovality(self: Self, value: "bool"):
        self.wrapped.IncludeRingOvality = bool(value) if value is not None else False

    @property
    def include_thermal_expansion_effects(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeThermalExpansionEffects

        if temp is None:
            return False

        return temp

    @include_thermal_expansion_effects.setter
    @enforce_parameter_types
    def include_thermal_expansion_effects(self: Self, value: "bool"):
        self.wrapped.IncludeThermalExpansionEffects = (
            bool(value) if value is not None else False
        )

    @property
    def include_tilt_stiffness_for_bevel_hypoid_gears(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeTiltStiffnessForBevelHypoidGears

        if temp is None:
            return False

        return temp

    @include_tilt_stiffness_for_bevel_hypoid_gears.setter
    @enforce_parameter_types
    def include_tilt_stiffness_for_bevel_hypoid_gears(self: Self, value: "bool"):
        self.wrapped.IncludeTiltStiffnessForBevelHypoidGears = (
            bool(value) if value is not None else False
        )

    @property
    def maximum_shaft_section_cross_sectional_area_ratio(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumShaftSectionCrossSectionalAreaRatio

        if temp is None:
            return 0.0

        return temp

    @maximum_shaft_section_cross_sectional_area_ratio.setter
    @enforce_parameter_types
    def maximum_shaft_section_cross_sectional_area_ratio(self: Self, value: "float"):
        self.wrapped.MaximumShaftSectionCrossSectionalAreaRatio = (
            float(value) if value is not None else 0.0
        )

    @property
    def maximum_shaft_section_length_to_diameter_ratio(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumShaftSectionLengthToDiameterRatio

        if temp is None:
            return 0.0

        return temp

    @maximum_shaft_section_length_to_diameter_ratio.setter
    @enforce_parameter_types
    def maximum_shaft_section_length_to_diameter_ratio(self: Self, value: "float"):
        self.wrapped.MaximumShaftSectionLengthToDiameterRatio = (
            float(value) if value is not None else 0.0
        )

    @property
    def maximum_shaft_section_polar_area_moment_of_inertia_ratio(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumShaftSectionPolarAreaMomentOfInertiaRatio

        if temp is None:
            return 0.0

        return temp

    @maximum_shaft_section_polar_area_moment_of_inertia_ratio.setter
    @enforce_parameter_types
    def maximum_shaft_section_polar_area_moment_of_inertia_ratio(
        self: Self, value: "float"
    ):
        self.wrapped.MaximumShaftSectionPolarAreaMomentOfInertiaRatio = (
            float(value) if value is not None else 0.0
        )

    @property
    def maximum_translation_per_solver_step(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MaximumTranslationPerSolverStep

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @maximum_translation_per_solver_step.setter
    @enforce_parameter_types
    def maximum_translation_per_solver_step(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MaximumTranslationPerSolverStep = value

    @property
    def mesh_stiffness_model(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_MeshStiffnessModel":
        """EnumWithSelectedValue[mastapy.system_model.MeshStiffnessModel]"""
        temp = self.wrapped.MeshStiffnessModel

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_MeshStiffnessModel.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @mesh_stiffness_model.setter
    @enforce_parameter_types
    def mesh_stiffness_model(self: Self, value: "_2212.MeshStiffnessModel"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_MeshStiffnessModel.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.MeshStiffnessModel = value

    @property
    def micro_geometry_model_in_system_deflection(
        self: Self,
    ) -> "overridable.Overridable_MicroGeometryModel":
        """Overridable[mastapy.gears.MicroGeometryModel]"""
        temp = self.wrapped.MicroGeometryModelInSystemDeflection

        if temp is None:
            return None

        value = overridable.Overridable_MicroGeometryModel.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value)

    @micro_geometry_model_in_system_deflection.setter
    @enforce_parameter_types
    def micro_geometry_model_in_system_deflection(
        self: Self,
        value: "Union[_335.MicroGeometryModel, Tuple[_335.MicroGeometryModel, bool]]",
    ):
        wrapper_type = overridable.Overridable_MicroGeometryModel.wrapper_type()
        enclosed_type = overridable.Overridable_MicroGeometryModel.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](
            value if value is not None else None, is_overridden
        )
        self.wrapped.MicroGeometryModelInSystemDeflection = value

    @property
    def minimum_force_for_bearing_to_be_considered_loaded(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MinimumForceForBearingToBeConsideredLoaded

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minimum_force_for_bearing_to_be_considered_loaded.setter
    @enforce_parameter_types
    def minimum_force_for_bearing_to_be_considered_loaded(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MinimumForceForBearingToBeConsideredLoaded = value

    @property
    def minimum_moment_for_bearing_to_be_considered_loaded(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MinimumMomentForBearingToBeConsideredLoaded

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minimum_moment_for_bearing_to_be_considered_loaded.setter
    @enforce_parameter_types
    def minimum_moment_for_bearing_to_be_considered_loaded(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MinimumMomentForBearingToBeConsideredLoaded = value

    @property
    def minimum_number_of_gear_mesh_nodes(self: Self) -> "int":
        """int"""
        temp = self.wrapped.MinimumNumberOfGearMeshNodes

        if temp is None:
            return 0

        return temp

    @minimum_number_of_gear_mesh_nodes.setter
    @enforce_parameter_types
    def minimum_number_of_gear_mesh_nodes(self: Self, value: "int"):
        self.wrapped.MinimumNumberOfGearMeshNodes = (
            int(value) if value is not None else 0
        )

    @property
    def minimum_power_for_gear_mesh_to_be_loaded(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MinimumPowerForGearMeshToBeLoaded

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minimum_power_for_gear_mesh_to_be_loaded.setter
    @enforce_parameter_types
    def minimum_power_for_gear_mesh_to_be_loaded(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MinimumPowerForGearMeshToBeLoaded = value

    @property
    def minimum_torque_for_gear_mesh_to_be_loaded(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MinimumTorqueForGearMeshToBeLoaded

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minimum_torque_for_gear_mesh_to_be_loaded.setter
    @enforce_parameter_types
    def minimum_torque_for_gear_mesh_to_be_loaded(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MinimumTorqueForGearMeshToBeLoaded = value

    @property
    def model_bearing_mounting_clearances_automatically(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ModelBearingMountingClearancesAutomatically

        if temp is None:
            return False

        return temp

    @model_bearing_mounting_clearances_automatically.setter
    @enforce_parameter_types
    def model_bearing_mounting_clearances_automatically(self: Self, value: "bool"):
        self.wrapped.ModelBearingMountingClearancesAutomatically = (
            bool(value) if value is not None else False
        )

    @property
    def number_of_grid_points_across_rib_contact_width(
        self: Self,
    ) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.NumberOfGridPointsAcrossRibContactWidth

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @number_of_grid_points_across_rib_contact_width.setter
    @enforce_parameter_types
    def number_of_grid_points_across_rib_contact_width(
        self: Self, value: "Union[int, Tuple[int, bool]]"
    ):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.NumberOfGridPointsAcrossRibContactWidth = value

    @property
    def number_of_grid_points_across_rib_height(
        self: Self,
    ) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.NumberOfGridPointsAcrossRibHeight

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @number_of_grid_points_across_rib_height.setter
    @enforce_parameter_types
    def number_of_grid_points_across_rib_height(
        self: Self, value: "Union[int, Tuple[int, bool]]"
    ):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.NumberOfGridPointsAcrossRibHeight = value

    @property
    def number_of_strips_for_roller_calculation(
        self: Self,
    ) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.NumberOfStripsForRollerCalculation

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @number_of_strips_for_roller_calculation.setter
    @enforce_parameter_types
    def number_of_strips_for_roller_calculation(
        self: Self, value: "Union[int, Tuple[int, bool]]"
    ):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.NumberOfStripsForRollerCalculation = value

    @property
    def peak_load_factor_for_shafts(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PeakLoadFactorForShafts

        if temp is None:
            return 0.0

        return temp

    @peak_load_factor_for_shafts.setter
    @enforce_parameter_types
    def peak_load_factor_for_shafts(self: Self, value: "float"):
        self.wrapped.PeakLoadFactorForShafts = (
            float(value) if value is not None else 0.0
        )

    @property
    def refine_grid_around_contact_point(self: Self) -> "overridable.Overridable_bool":
        """Overridable[bool]"""
        temp = self.wrapped.RefineGridAroundContactPoint

        if temp is None:
            return False

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_bool"
        )(temp)

    @refine_grid_around_contact_point.setter
    @enforce_parameter_types
    def refine_grid_around_contact_point(
        self: Self, value: "Union[bool, Tuple[bool, bool]]"
    ):
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else False, is_overridden
        )
        self.wrapped.RefineGridAroundContactPoint = value

    @property
    def relative_tolerance_for_convergence(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RelativeToleranceForConvergence

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @relative_tolerance_for_convergence.setter
    @enforce_parameter_types
    def relative_tolerance_for_convergence(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RelativeToleranceForConvergence = value

    @property
    def ring_ovality_scaling(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RingOvalityScaling

        if temp is None:
            return 0.0

        return temp

    @ring_ovality_scaling.setter
    @enforce_parameter_types
    def ring_ovality_scaling(self: Self, value: "float"):
        self.wrapped.RingOvalityScaling = float(value) if value is not None else 0.0

    @property
    def roller_analysis_method(self: Self) -> "_2067.RollerAnalysisMethod":
        """mastapy.bearings.bearing_results.rolling.RollerAnalysisMethod"""
        temp = self.wrapped.RollerAnalysisMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Bearings.BearingResults.Rolling.RollerAnalysisMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.bearings.bearing_results.rolling._2067", "RollerAnalysisMethod"
        )(value)

    @roller_analysis_method.setter
    @enforce_parameter_types
    def roller_analysis_method(self: Self, value: "_2067.RollerAnalysisMethod"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Bearings.BearingResults.Rolling.RollerAnalysisMethod"
        )
        self.wrapped.RollerAnalysisMethod = value

    @property
    def set_first_element_angle_to_load_direction(
        self: Self,
    ) -> "overridable.Overridable_bool":
        """Overridable[bool]"""
        temp = self.wrapped.SetFirstElementAngleToLoadDirection

        if temp is None:
            return False

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_bool"
        )(temp)

    @set_first_element_angle_to_load_direction.setter
    @enforce_parameter_types
    def set_first_element_angle_to_load_direction(
        self: Self, value: "Union[bool, Tuple[bool, bool]]"
    ):
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else False, is_overridden
        )
        self.wrapped.SetFirstElementAngleToLoadDirection = value

    @property
    def shear_area_factor_method(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ShearAreaFactorMethod":
        """EnumWithSelectedValue[mastapy.nodal_analysis.nodal_entities.ShearAreaFactorMethod]"""
        temp = self.wrapped.ShearAreaFactorMethod

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ShearAreaFactorMethod.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @shear_area_factor_method.setter
    @enforce_parameter_types
    def shear_area_factor_method(self: Self, value: "_130.ShearAreaFactorMethod"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ShearAreaFactorMethod.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ShearAreaFactorMethod = value

    @property
    def speed_of_sound(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.SpeedOfSound

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @speed_of_sound.setter
    @enforce_parameter_types
    def speed_of_sound(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.SpeedOfSound = value

    @property
    def spline_rigid_bond_detailed_connection_nodes_per_unit_length_to_diameter_ratio(
        self: Self,
    ) -> "float":
        """float"""
        temp = (
            self.wrapped.SplineRigidBondDetailedConnectionNodesPerUnitLengthToDiameterRatio
        )

        if temp is None:
            return 0.0

        return temp

    @spline_rigid_bond_detailed_connection_nodes_per_unit_length_to_diameter_ratio.setter
    @enforce_parameter_types
    def spline_rigid_bond_detailed_connection_nodes_per_unit_length_to_diameter_ratio(
        self: Self, value: "float"
    ):
        self.wrapped.SplineRigidBondDetailedConnectionNodesPerUnitLengthToDiameterRatio = (
            float(value) if value is not None else 0.0
        )

    @property
    def stress_concentration_method_for_rating(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_StressConcentrationMethod":
        """EnumWithSelectedValue[mastapy.bearings.bearing_results.rolling.iso_rating_results.StressConcentrationMethod]"""
        temp = self.wrapped.StressConcentrationMethodForRating

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_StressConcentrationMethod.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @stress_concentration_method_for_rating.setter
    @enforce_parameter_types
    def stress_concentration_method_for_rating(
        self: Self, value: "_2107.StressConcentrationMethod"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_StressConcentrationMethod.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.StressConcentrationMethodForRating = value

    @property
    def tolerance_factor_for_axial_internal_clearances(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ToleranceFactorForAxialInternalClearances

        if temp is None:
            return 0.0

        return temp

    @tolerance_factor_for_axial_internal_clearances.setter
    @enforce_parameter_types
    def tolerance_factor_for_axial_internal_clearances(self: Self, value: "float"):
        self.wrapped.ToleranceFactorForAxialInternalClearances = (
            float(value) if value is not None else 0.0
        )

    @property
    def tolerance_factor_for_inner_fit(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ToleranceFactorForInnerFit

        if temp is None:
            return 0.0

        return temp

    @tolerance_factor_for_inner_fit.setter
    @enforce_parameter_types
    def tolerance_factor_for_inner_fit(self: Self, value: "float"):
        self.wrapped.ToleranceFactorForInnerFit = (
            float(value) if value is not None else 0.0
        )

    @property
    def tolerance_factor_for_inner_mounting_sleeve_bore(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ToleranceFactorForInnerMountingSleeveBore

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @tolerance_factor_for_inner_mounting_sleeve_bore.setter
    @enforce_parameter_types
    def tolerance_factor_for_inner_mounting_sleeve_bore(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ToleranceFactorForInnerMountingSleeveBore = value

    @property
    def tolerance_factor_for_inner_mounting_sleeve_outer_diameter(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ToleranceFactorForInnerMountingSleeveOuterDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @tolerance_factor_for_inner_mounting_sleeve_outer_diameter.setter
    @enforce_parameter_types
    def tolerance_factor_for_inner_mounting_sleeve_outer_diameter(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ToleranceFactorForInnerMountingSleeveOuterDiameter = value

    @property
    def tolerance_factor_for_inner_ring(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ToleranceFactorForInnerRing

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @tolerance_factor_for_inner_ring.setter
    @enforce_parameter_types
    def tolerance_factor_for_inner_ring(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ToleranceFactorForInnerRing = value

    @property
    def tolerance_factor_for_inner_support(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ToleranceFactorForInnerSupport

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @tolerance_factor_for_inner_support.setter
    @enforce_parameter_types
    def tolerance_factor_for_inner_support(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ToleranceFactorForInnerSupport = value

    @property
    def tolerance_factor_for_outer_fit(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ToleranceFactorForOuterFit

        if temp is None:
            return 0.0

        return temp

    @tolerance_factor_for_outer_fit.setter
    @enforce_parameter_types
    def tolerance_factor_for_outer_fit(self: Self, value: "float"):
        self.wrapped.ToleranceFactorForOuterFit = (
            float(value) if value is not None else 0.0
        )

    @property
    def tolerance_factor_for_outer_mounting_sleeve_bore(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ToleranceFactorForOuterMountingSleeveBore

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @tolerance_factor_for_outer_mounting_sleeve_bore.setter
    @enforce_parameter_types
    def tolerance_factor_for_outer_mounting_sleeve_bore(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ToleranceFactorForOuterMountingSleeveBore = value

    @property
    def tolerance_factor_for_outer_mounting_sleeve_outer_diameter(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ToleranceFactorForOuterMountingSleeveOuterDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @tolerance_factor_for_outer_mounting_sleeve_outer_diameter.setter
    @enforce_parameter_types
    def tolerance_factor_for_outer_mounting_sleeve_outer_diameter(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ToleranceFactorForOuterMountingSleeveOuterDiameter = value

    @property
    def tolerance_factor_for_outer_ring(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ToleranceFactorForOuterRing

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @tolerance_factor_for_outer_ring.setter
    @enforce_parameter_types
    def tolerance_factor_for_outer_ring(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ToleranceFactorForOuterRing = value

    @property
    def tolerance_factor_for_outer_support(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ToleranceFactorForOuterSupport

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @tolerance_factor_for_outer_support.setter
    @enforce_parameter_types
    def tolerance_factor_for_outer_support(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ToleranceFactorForOuterSupport = value

    @property
    def tolerance_factor_for_radial_internal_clearances(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ToleranceFactorForRadialInternalClearances

        if temp is None:
            return 0.0

        return temp

    @tolerance_factor_for_radial_internal_clearances.setter
    @enforce_parameter_types
    def tolerance_factor_for_radial_internal_clearances(self: Self, value: "float"):
        self.wrapped.ToleranceFactorForRadialInternalClearances = (
            float(value) if value is not None else 0.0
        )

    @property
    def use_default_temperatures(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseDefaultTemperatures

        if temp is None:
            return False

        return temp

    @use_default_temperatures.setter
    @enforce_parameter_types
    def use_default_temperatures(self: Self, value: "bool"):
        self.wrapped.UseDefaultTemperatures = (
            bool(value) if value is not None else False
        )

    @property
    def use_node_per_bearing_row_inner(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseNodePerBearingRowInner

        if temp is None:
            return False

        return temp

    @use_node_per_bearing_row_inner.setter
    @enforce_parameter_types
    def use_node_per_bearing_row_inner(self: Self, value: "bool"):
        self.wrapped.UseNodePerBearingRowInner = (
            bool(value) if value is not None else False
        )

    @property
    def use_node_per_bearing_row_outer(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseNodePerBearingRowOuter

        if temp is None:
            return False

        return temp

    @use_node_per_bearing_row_outer.setter
    @enforce_parameter_types
    def use_node_per_bearing_row_outer(self: Self, value: "bool"):
        self.wrapped.UseNodePerBearingRowOuter = (
            bool(value) if value is not None else False
        )

    @property
    def use_single_node_for_cylindrical_gear_meshes(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseSingleNodeForCylindricalGearMeshes

        if temp is None:
            return False

        return temp

    @use_single_node_for_cylindrical_gear_meshes.setter
    @enforce_parameter_types
    def use_single_node_for_cylindrical_gear_meshes(self: Self, value: "bool"):
        self.wrapped.UseSingleNodeForCylindricalGearMeshes = (
            bool(value) if value is not None else False
        )

    @property
    def use_single_node_for_spline_rigid_bond_detailed_connection_connections(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = self.wrapped.UseSingleNodeForSplineRigidBondDetailedConnectionConnections

        if temp is None:
            return False

        return temp

    @use_single_node_for_spline_rigid_bond_detailed_connection_connections.setter
    @enforce_parameter_types
    def use_single_node_for_spline_rigid_bond_detailed_connection_connections(
        self: Self, value: "bool"
    ):
        self.wrapped.UseSingleNodeForSplineRigidBondDetailedConnectionConnections = (
            bool(value) if value is not None else False
        )

    @property
    def additional_acceleration(self: Self) -> "_6808.AdditionalAccelerationOptions":
        """mastapy.system_model.analyses_and_results.static_loads.AdditionalAccelerationOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AdditionalAcceleration

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def input_power_load(self: Self) -> "_6937.PowerLoadLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PowerLoadLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InputPowerLoad

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def output_power_load(self: Self) -> "_6937.PowerLoadLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PowerLoadLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OutputPowerLoad

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def parametric_study_tool_options(self: Self) -> "_4386.ParametricStudyToolOptions":
        """mastapy.system_model.analyses_and_results.parametric_study_tools.ParametricStudyToolOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParametricStudyToolOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def temperatures(self: Self) -> "_2222.TransmissionTemperatureSet":
        """mastapy.system_model.TransmissionTemperatureSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Temperatures

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def transmission_efficiency_settings(
        self: Self,
    ) -> "_6976.TransmissionEfficiencySettings":
        """mastapy.system_model.analyses_and_results.static_loads.TransmissionEfficiencySettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransmissionEfficiencySettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_loads(self: Self) -> "List[_6937.PowerLoadLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.PowerLoadLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def delete(self: Self):
        """Method does not return."""
        self.wrapped.Delete()

    @enforce_parameter_types
    def inputs_for_torque_converter_connection(
        self: Self, design_entity: "_2350.TorqueConverterConnection"
    ) -> "_6970.TorqueConverterConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterConnectionLoadCase

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection)
        """
        method_result = self.wrapped.InputsFor.Overloads[_TORQUE_CONVERTER_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_abstract_shaft(
        self: Self, design_entity: "_2433.AbstractShaft"
    ) -> "_6805.AbstractShaftLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.AbstractShaftLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaft)
        """
        method_result = self.wrapped.InputsFor.Overloads[_ABSTRACT_SHAFT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_abstract_assembly(
        self: Self, design_entity: "_2432.AbstractAssembly"
    ) -> "_6804.AbstractAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.AbstractAssemblyLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.AbstractAssembly)
        """
        method_result = self.wrapped.InputsFor.Overloads[_ABSTRACT_ASSEMBLY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_abstract_shaft_or_housing(
        self: Self, design_entity: "_2434.AbstractShaftOrHousing"
    ) -> "_6806.AbstractShaftOrHousingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.AbstractShaftOrHousingLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaftOrHousing)
        """
        method_result = self.wrapped.InputsFor.Overloads[_ABSTRACT_SHAFT_OR_HOUSING](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_bearing(
        self: Self, design_entity: "_2437.Bearing"
    ) -> "_6817.BearingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BearingLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.Bearing)
        """
        method_result = self.wrapped.InputsFor.Overloads[_BEARING](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_bolt(
        self: Self, design_entity: "_2440.Bolt"
    ) -> "_6829.BoltLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BoltLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.Bolt)
        """
        method_result = self.wrapped.InputsFor.Overloads[_BOLT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_bolted_joint(
        self: Self, design_entity: "_2441.BoltedJoint"
    ) -> "_6828.BoltedJointLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BoltedJointLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.BoltedJoint)
        """
        method_result = self.wrapped.InputsFor.Overloads[_BOLTED_JOINT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_component(
        self: Self, design_entity: "_2442.Component"
    ) -> "_6835.ComponentLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ComponentLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.Component)
        """
        method_result = self.wrapped.InputsFor.Overloads[_COMPONENT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_connector(
        self: Self, design_entity: "_2445.Connector"
    ) -> "_6848.ConnectorLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConnectorLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.Connector)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CONNECTOR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_datum(
        self: Self, design_entity: "_2446.Datum"
    ) -> "_6867.DatumLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.DatumLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.Datum)
        """
        method_result = self.wrapped.InputsFor.Overloads[_DATUM](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_external_cad_model(
        self: Self, design_entity: "_2450.ExternalCADModel"
    ) -> "_6881.ExternalCADModelLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ExternalCADModelLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.ExternalCADModel)
        """
        method_result = self.wrapped.InputsFor.Overloads[_EXTERNAL_CAD_MODEL](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_fe_part(
        self: Self, design_entity: "_2451.FEPart"
    ) -> "_6885.FEPartLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FEPartLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.FEPart)
        """
        method_result = self.wrapped.InputsFor.Overloads[_FE_PART](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_flexible_pin_assembly(
        self: Self, design_entity: "_2452.FlexiblePinAssembly"
    ) -> "_6886.FlexiblePinAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FlexiblePinAssemblyLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.FlexiblePinAssembly)
        """
        method_result = self.wrapped.InputsFor.Overloads[_FLEXIBLE_PIN_ASSEMBLY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_assembly(
        self: Self, design_entity: "_2431.Assembly"
    ) -> "_6816.AssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.AssemblyLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.Assembly)
        """
        method_result = self.wrapped.InputsFor.Overloads[_ASSEMBLY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_guide_dxf_model(
        self: Self, design_entity: "_2453.GuideDxfModel"
    ) -> "_6894.GuideDxfModelLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.GuideDxfModelLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.GuideDxfModel)
        """
        method_result = self.wrapped.InputsFor.Overloads[_GUIDE_DXF_MODEL](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_mass_disc(
        self: Self, design_entity: "_2460.MassDisc"
    ) -> "_6919.MassDiscLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.MassDiscLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.MassDisc)
        """
        method_result = self.wrapped.InputsFor.Overloads[_MASS_DISC](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_measurement_component(
        self: Self, design_entity: "_2461.MeasurementComponent"
    ) -> "_6920.MeasurementComponentLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.MeasurementComponentLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.MeasurementComponent)
        """
        method_result = self.wrapped.InputsFor.Overloads[_MEASUREMENT_COMPONENT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_mountable_component(
        self: Self, design_entity: "_2462.MountableComponent"
    ) -> "_6922.MountableComponentLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.MountableComponentLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.MountableComponent)
        """
        method_result = self.wrapped.InputsFor.Overloads[_MOUNTABLE_COMPONENT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_oil_seal(
        self: Self, design_entity: "_2464.OilSeal"
    ) -> "_6924.OilSealLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.OilSealLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.OilSeal)
        """
        method_result = self.wrapped.InputsFor.Overloads[_OIL_SEAL](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_part(
        self: Self, design_entity: "_2466.Part"
    ) -> "_6926.PartLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.Part)
        """
        method_result = self.wrapped.InputsFor.Overloads[_PART](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_planet_carrier(
        self: Self, design_entity: "_2467.PlanetCarrier"
    ) -> "_6933.PlanetCarrierLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PlanetCarrierLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.PlanetCarrier)
        """
        method_result = self.wrapped.InputsFor.Overloads[_PLANET_CARRIER](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_point_load(
        self: Self, design_entity: "_2469.PointLoad"
    ) -> "_6936.PointLoadLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PointLoadLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.PointLoad)
        """
        method_result = self.wrapped.InputsFor.Overloads[_POINT_LOAD](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_power_load(
        self: Self, design_entity: "_2470.PowerLoad"
    ) -> "_6937.PowerLoadLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PowerLoadLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.PowerLoad)
        """
        method_result = self.wrapped.InputsFor.Overloads[_POWER_LOAD](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_root_assembly(
        self: Self, design_entity: "_2472.RootAssembly"
    ) -> "_6946.RootAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RootAssemblyLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.RootAssembly)
        """
        method_result = self.wrapped.InputsFor.Overloads[_ROOT_ASSEMBLY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_specialised_assembly(
        self: Self, design_entity: "_2474.SpecialisedAssembly"
    ) -> "_6950.SpecialisedAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpecialisedAssemblyLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.SpecialisedAssembly)
        """
        method_result = self.wrapped.InputsFor.Overloads[_SPECIALISED_ASSEMBLY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_unbalanced_mass(
        self: Self, design_entity: "_2475.UnbalancedMass"
    ) -> "_6978.UnbalancedMassLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.UnbalancedMassLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.UnbalancedMass)
        """
        method_result = self.wrapped.InputsFor.Overloads[_UNBALANCED_MASS](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_virtual_component(
        self: Self, design_entity: "_2477.VirtualComponent"
    ) -> "_6979.VirtualComponentLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.VirtualComponentLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.VirtualComponent)
        """
        method_result = self.wrapped.InputsFor.Overloads[_VIRTUAL_COMPONENT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_shaft(
        self: Self, design_entity: "_2480.Shaft"
    ) -> "_6948.ShaftLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ShaftLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.shaft_model.Shaft)
        """
        method_result = self.wrapped.InputsFor.Overloads[_SHAFT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_concept_gear(
        self: Self, design_entity: "_2519.ConceptGear"
    ) -> "_6839.ConceptGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptGearLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CONCEPT_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_concept_gear_set(
        self: Self, design_entity: "_2520.ConceptGearSet"
    ) -> "_6841.ConceptGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptGearSetLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGearSet)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CONCEPT_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_face_gear(
        self: Self, design_entity: "_2526.FaceGear"
    ) -> "_6882.FaceGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FaceGearLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[_FACE_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_face_gear_set(
        self: Self, design_entity: "_2527.FaceGearSet"
    ) -> "_6884.FaceGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FaceGearSetLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGearSet)
        """
        method_result = self.wrapped.InputsFor.Overloads[_FACE_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_agma_gleason_conical_gear(
        self: Self, design_entity: "_2511.AGMAGleasonConicalGear"
    ) -> "_6811.AGMAGleasonConicalGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_agma_gleason_conical_gear_set(
        self: Self, design_entity: "_2512.AGMAGleasonConicalGearSet"
    ) -> "_6813.AGMAGleasonConicalGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearSetLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet)
        """
        method_result = self.wrapped.InputsFor.Overloads[
            _AGMA_GLEASON_CONICAL_GEAR_SET
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_bevel_differential_gear(
        self: Self, design_entity: "_2513.BevelDifferentialGear"
    ) -> "_6820.BevelDifferentialGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_bevel_differential_gear_set(
        self: Self, design_entity: "_2514.BevelDifferentialGearSet"
    ) -> "_6822.BevelDifferentialGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearSetLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGearSet)
        """
        method_result = self.wrapped.InputsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_bevel_differential_planet_gear(
        self: Self, design_entity: "_2515.BevelDifferentialPlanetGear"
    ) -> "_6823.BevelDifferentialPlanetGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialPlanetGearLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[
            _BEVEL_DIFFERENTIAL_PLANET_GEAR
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_bevel_differential_sun_gear(
        self: Self, design_entity: "_2516.BevelDifferentialSunGear"
    ) -> "_6824.BevelDifferentialSunGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialSunGearLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialSunGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[_BEVEL_DIFFERENTIAL_SUN_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_bevel_gear(
        self: Self, design_entity: "_2517.BevelGear"
    ) -> "_6825.BevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelGearLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[_BEVEL_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_bevel_gear_set(
        self: Self, design_entity: "_2518.BevelGearSet"
    ) -> "_6827.BevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelGearSetLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGearSet)
        """
        method_result = self.wrapped.InputsFor.Overloads[_BEVEL_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_conical_gear(
        self: Self, design_entity: "_2521.ConicalGear"
    ) -> "_6842.ConicalGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConicalGearLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CONICAL_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_conical_gear_set(
        self: Self, design_entity: "_2522.ConicalGearSet"
    ) -> "_6846.ConicalGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConicalGearSetLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGearSet)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CONICAL_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_cylindrical_gear(
        self: Self, design_entity: "_2523.CylindricalGear"
    ) -> "_6859.CylindricalGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CYLINDRICAL_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_cylindrical_gear_set(
        self: Self, design_entity: "_2524.CylindricalGearSet"
    ) -> "_6863.CylindricalGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearSetLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGearSet)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CYLINDRICAL_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_cylindrical_planet_gear(
        self: Self, design_entity: "_2525.CylindricalPlanetGear"
    ) -> "_6864.CylindricalPlanetGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalPlanetGearLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalPlanetGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CYLINDRICAL_PLANET_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_gear(
        self: Self, design_entity: "_2528.Gear"
    ) -> "_6888.GearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.GearLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.gears.Gear)
        """
        method_result = self.wrapped.InputsFor.Overloads[_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_gear_set(
        self: Self, design_entity: "_2530.GearSet"
    ) -> "_6893.GearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.GearSetLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.gears.GearSet)
        """
        method_result = self.wrapped.InputsFor.Overloads[_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_hypoid_gear(
        self: Self, design_entity: "_2532.HypoidGear"
    ) -> "_6903.HypoidGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[_HYPOID_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_hypoid_gear_set(
        self: Self, design_entity: "_2533.HypoidGearSet"
    ) -> "_6905.HypoidGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearSetLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGearSet)
        """
        method_result = self.wrapped.InputsFor.Overloads[_HYPOID_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_klingelnberg_cyclo_palloid_conical_gear(
        self: Self, design_entity: "_2534.KlingelnbergCycloPalloidConicalGear"
    ) -> "_6910.KlingelnbergCycloPalloidConicalGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_klingelnberg_cyclo_palloid_conical_gear_set(
        self: Self, design_entity: "_2535.KlingelnbergCycloPalloidConicalGearSet"
    ) -> "_6912.KlingelnbergCycloPalloidConicalGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearSetLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet)
        """
        method_result = self.wrapped.InputsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_klingelnberg_cyclo_palloid_hypoid_gear(
        self: Self, design_entity: "_2536.KlingelnbergCycloPalloidHypoidGear"
    ) -> "_6913.KlingelnbergCycloPalloidHypoidGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_klingelnberg_cyclo_palloid_hypoid_gear_set(
        self: Self, design_entity: "_2537.KlingelnbergCycloPalloidHypoidGearSet"
    ) -> "_6915.KlingelnbergCycloPalloidHypoidGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearSetLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet)
        """
        method_result = self.wrapped.InputsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_klingelnberg_cyclo_palloid_spiral_bevel_gear(
        self: Self, design_entity: "_2538.KlingelnbergCycloPalloidSpiralBevelGear"
    ) -> "_6916.KlingelnbergCycloPalloidSpiralBevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(
        self: Self, design_entity: "_2539.KlingelnbergCycloPalloidSpiralBevelGearSet"
    ) -> "_6918.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet)
        """
        method_result = self.wrapped.InputsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_planetary_gear_set(
        self: Self, design_entity: "_2540.PlanetaryGearSet"
    ) -> "_6931.PlanetaryGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PlanetaryGearSetLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.gears.PlanetaryGearSet)
        """
        method_result = self.wrapped.InputsFor.Overloads[_PLANETARY_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_spiral_bevel_gear(
        self: Self, design_entity: "_2541.SpiralBevelGear"
    ) -> "_6951.SpiralBevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[_SPIRAL_BEVEL_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_spiral_bevel_gear_set(
        self: Self, design_entity: "_2542.SpiralBevelGearSet"
    ) -> "_6953.SpiralBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearSetLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGearSet)
        """
        method_result = self.wrapped.InputsFor.Overloads[_SPIRAL_BEVEL_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_straight_bevel_diff_gear(
        self: Self, design_entity: "_2543.StraightBevelDiffGear"
    ) -> "_6957.StraightBevelDiffGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_straight_bevel_diff_gear_set(
        self: Self, design_entity: "_2544.StraightBevelDiffGearSet"
    ) -> "_6959.StraightBevelDiffGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearSetLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGearSet)
        """
        method_result = self.wrapped.InputsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_straight_bevel_gear(
        self: Self, design_entity: "_2545.StraightBevelGear"
    ) -> "_6960.StraightBevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[_STRAIGHT_BEVEL_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_straight_bevel_gear_set(
        self: Self, design_entity: "_2546.StraightBevelGearSet"
    ) -> "_6962.StraightBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearSetLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGearSet)
        """
        method_result = self.wrapped.InputsFor.Overloads[_STRAIGHT_BEVEL_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_straight_bevel_planet_gear(
        self: Self, design_entity: "_2547.StraightBevelPlanetGear"
    ) -> "_6963.StraightBevelPlanetGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelPlanetGearLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelPlanetGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[_STRAIGHT_BEVEL_PLANET_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_straight_bevel_sun_gear(
        self: Self, design_entity: "_2548.StraightBevelSunGear"
    ) -> "_6964.StraightBevelSunGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelSunGearLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelSunGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[_STRAIGHT_BEVEL_SUN_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_worm_gear(
        self: Self, design_entity: "_2549.WormGear"
    ) -> "_6980.WormGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.WormGearLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[_WORM_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_worm_gear_set(
        self: Self, design_entity: "_2550.WormGearSet"
    ) -> "_6982.WormGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.WormGearSetLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGearSet)
        """
        method_result = self.wrapped.InputsFor.Overloads[_WORM_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_zerol_bevel_gear(
        self: Self, design_entity: "_2551.ZerolBevelGear"
    ) -> "_6983.ZerolBevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGear)
        """
        method_result = self.wrapped.InputsFor.Overloads[_ZEROL_BEVEL_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_zerol_bevel_gear_set(
        self: Self, design_entity: "_2552.ZerolBevelGearSet"
    ) -> "_6985.ZerolBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearSetLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGearSet)
        """
        method_result = self.wrapped.InputsFor.Overloads[_ZEROL_BEVEL_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_cycloidal_assembly(
        self: Self, design_entity: "_2566.CycloidalAssembly"
    ) -> "_6855.CycloidalAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalAssemblyLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.cycloidal.CycloidalAssembly)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CYCLOIDAL_ASSEMBLY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_cycloidal_disc(
        self: Self, design_entity: "_2567.CycloidalDisc"
    ) -> "_6857.CycloidalDiscLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.cycloidal.CycloidalDisc)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CYCLOIDAL_DISC](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_ring_pins(
        self: Self, design_entity: "_2568.RingPins"
    ) -> "_6941.RingPinsLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RingPinsLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.cycloidal.RingPins)
        """
        method_result = self.wrapped.InputsFor.Overloads[_RING_PINS](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_part_to_part_shear_coupling(
        self: Self, design_entity: "_2586.PartToPartShearCoupling"
    ) -> "_6929.PartToPartShearCouplingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCoupling)
        """
        method_result = self.wrapped.InputsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_part_to_part_shear_coupling_half(
        self: Self, design_entity: "_2587.PartToPartShearCouplingHalf"
    ) -> "_6928.PartToPartShearCouplingHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingHalfLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf)
        """
        method_result = self.wrapped.InputsFor.Overloads[
            _PART_TO_PART_SHEAR_COUPLING_HALF
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_belt_drive(
        self: Self, design_entity: "_2574.BeltDrive"
    ) -> "_6819.BeltDriveLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BeltDriveLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.couplings.BeltDrive)
        """
        method_result = self.wrapped.InputsFor.Overloads[_BELT_DRIVE](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_clutch(
        self: Self, design_entity: "_2576.Clutch"
    ) -> "_6832.ClutchLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ClutchLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Clutch)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CLUTCH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_clutch_half(
        self: Self, design_entity: "_2577.ClutchHalf"
    ) -> "_6831.ClutchHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ClutchHalfLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ClutchHalf)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CLUTCH_HALF](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_concept_coupling(
        self: Self, design_entity: "_2579.ConceptCoupling"
    ) -> "_6838.ConceptCouplingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCoupling)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CONCEPT_COUPLING](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_concept_coupling_half(
        self: Self, design_entity: "_2580.ConceptCouplingHalf"
    ) -> "_6837.ConceptCouplingHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingHalfLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCouplingHalf)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CONCEPT_COUPLING_HALF](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_coupling(
        self: Self, design_entity: "_2581.Coupling"
    ) -> "_6851.CouplingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CouplingLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Coupling)
        """
        method_result = self.wrapped.InputsFor.Overloads[_COUPLING](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_coupling_half(
        self: Self, design_entity: "_2582.CouplingHalf"
    ) -> "_6850.CouplingHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CouplingHalfLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CouplingHalf)
        """
        method_result = self.wrapped.InputsFor.Overloads[_COUPLING_HALF](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_cvt(self: Self, design_entity: "_2584.CVT") -> "_6853.CVTLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CVTLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVT)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CVT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_cvt_pulley(
        self: Self, design_entity: "_2585.CVTPulley"
    ) -> "_6854.CVTPulleyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CVTPulleyLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVTPulley)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CVT_PULLEY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_pulley(
        self: Self, design_entity: "_2588.Pulley"
    ) -> "_6938.PulleyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PulleyLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Pulley)
        """
        method_result = self.wrapped.InputsFor.Overloads[_PULLEY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_shaft_hub_connection(
        self: Self, design_entity: "_2596.ShaftHubConnection"
    ) -> "_6947.ShaftHubConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ShaftHubConnectionLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ShaftHubConnection)
        """
        method_result = self.wrapped.InputsFor.Overloads[_SHAFT_HUB_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_rolling_ring(
        self: Self, design_entity: "_2594.RollingRing"
    ) -> "_6945.RollingRingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RollingRingLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRing)
        """
        method_result = self.wrapped.InputsFor.Overloads[_ROLLING_RING](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_rolling_ring_assembly(
        self: Self, design_entity: "_2595.RollingRingAssembly"
    ) -> "_6943.RollingRingAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RollingRingAssemblyLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRingAssembly)
        """
        method_result = self.wrapped.InputsFor.Overloads[_ROLLING_RING_ASSEMBLY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_spring_damper(
        self: Self, design_entity: "_2598.SpringDamper"
    ) -> "_6956.SpringDamperLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpringDamperLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamper)
        """
        method_result = self.wrapped.InputsFor.Overloads[_SPRING_DAMPER](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_spring_damper_half(
        self: Self, design_entity: "_2599.SpringDamperHalf"
    ) -> "_6955.SpringDamperHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpringDamperHalfLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamperHalf)
        """
        method_result = self.wrapped.InputsFor.Overloads[_SPRING_DAMPER_HALF](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_synchroniser(
        self: Self, design_entity: "_2600.Synchroniser"
    ) -> "_6966.SynchroniserLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Synchroniser)
        """
        method_result = self.wrapped.InputsFor.Overloads[_SYNCHRONISER](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_synchroniser_half(
        self: Self, design_entity: "_2602.SynchroniserHalf"
    ) -> "_6965.SynchroniserHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserHalfLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserHalf)
        """
        method_result = self.wrapped.InputsFor.Overloads[_SYNCHRONISER_HALF](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_synchroniser_part(
        self: Self, design_entity: "_2603.SynchroniserPart"
    ) -> "_6967.SynchroniserPartLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserPartLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserPart)
        """
        method_result = self.wrapped.InputsFor.Overloads[_SYNCHRONISER_PART](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_synchroniser_sleeve(
        self: Self, design_entity: "_2604.SynchroniserSleeve"
    ) -> "_6968.SynchroniserSleeveLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserSleeve)
        """
        method_result = self.wrapped.InputsFor.Overloads[_SYNCHRONISER_SLEEVE](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_torque_converter(
        self: Self, design_entity: "_2605.TorqueConverter"
    ) -> "_6971.TorqueConverterLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverter)
        """
        method_result = self.wrapped.InputsFor.Overloads[_TORQUE_CONVERTER](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_torque_converter_pump(
        self: Self, design_entity: "_2606.TorqueConverterPump"
    ) -> "_6972.TorqueConverterPumpLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterPumpLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterPump)
        """
        method_result = self.wrapped.InputsFor.Overloads[_TORQUE_CONVERTER_PUMP](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_torque_converter_turbine(
        self: Self, design_entity: "_2608.TorqueConverterTurbine"
    ) -> "_6973.TorqueConverterTurbineLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterTurbineLoadCase

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterTurbine)
        """
        method_result = self.wrapped.InputsFor.Overloads[_TORQUE_CONVERTER_TURBINE](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_shaft_to_mountable_component_connection(
        self: Self, design_entity: "_2293.ShaftToMountableComponentConnection"
    ) -> "_6949.ShaftToMountableComponentConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ShaftToMountableComponentConnectionLoadCase

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection)
        """
        method_result = self.wrapped.InputsFor.Overloads[
            _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_cvt_belt_connection(
        self: Self, design_entity: "_2271.CVTBeltConnection"
    ) -> "_6852.CVTBeltConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CVTBeltConnectionLoadCase

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CVTBeltConnection)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CVT_BELT_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_belt_connection(
        self: Self, design_entity: "_2266.BeltConnection"
    ) -> "_6818.BeltConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BeltConnectionLoadCase

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.BeltConnection)
        """
        method_result = self.wrapped.InputsFor.Overloads[_BELT_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_coaxial_connection(
        self: Self, design_entity: "_2267.CoaxialConnection"
    ) -> "_6834.CoaxialConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CoaxialConnectionLoadCase

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CoaxialConnection)
        """
        method_result = self.wrapped.InputsFor.Overloads[_COAXIAL_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_connection(
        self: Self, design_entity: "_2270.Connection"
    ) -> "_6847.ConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConnectionLoadCase

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.Connection)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_inter_mountable_component_connection(
        self: Self, design_entity: "_2279.InterMountableComponentConnection"
    ) -> "_6909.InterMountableComponentConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.InterMountableComponentConnectionLoadCase

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.InterMountableComponentConnection)
        """
        method_result = self.wrapped.InputsFor.Overloads[
            _INTER_MOUNTABLE_COMPONENT_CONNECTION
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_planetary_connection(
        self: Self, design_entity: "_2285.PlanetaryConnection"
    ) -> "_6930.PlanetaryConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PlanetaryConnectionLoadCase

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.PlanetaryConnection)
        """
        method_result = self.wrapped.InputsFor.Overloads[_PLANETARY_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_rolling_ring_connection(
        self: Self, design_entity: "_2290.RollingRingConnection"
    ) -> "_6944.RollingRingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RollingRingConnectionLoadCase

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.RollingRingConnection)
        """
        method_result = self.wrapped.InputsFor.Overloads[_ROLLING_RING_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_abstract_shaft_to_mountable_component_connection(
        self: Self, design_entity: "_2263.AbstractShaftToMountableComponentConnection"
    ) -> "_6807.AbstractShaftToMountableComponentConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.AbstractShaftToMountableComponentConnectionLoadCase

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.AbstractShaftToMountableComponentConnection)
        """
        method_result = self.wrapped.InputsFor.Overloads[
            _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_bevel_differential_gear_mesh(
        self: Self, design_entity: "_2299.BevelDifferentialGearMesh"
    ) -> "_6821.BevelDifferentialGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearMeshLoadCase

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh)
        """
        method_result = self.wrapped.InputsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_concept_gear_mesh(
        self: Self, design_entity: "_2303.ConceptGearMesh"
    ) -> "_6840.ConceptGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptGearMeshLoadCase

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CONCEPT_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_face_gear_mesh(
        self: Self, design_entity: "_2309.FaceGearMesh"
    ) -> "_6883.FaceGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FaceGearMeshLoadCase

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.FaceGearMesh)
        """
        method_result = self.wrapped.InputsFor.Overloads[_FACE_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_straight_bevel_diff_gear_mesh(
        self: Self, design_entity: "_2323.StraightBevelDiffGearMesh"
    ) -> "_6958.StraightBevelDiffGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearMeshLoadCase

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh)
        """
        method_result = self.wrapped.InputsFor.Overloads[
            _STRAIGHT_BEVEL_DIFF_GEAR_MESH
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_bevel_gear_mesh(
        self: Self, design_entity: "_2301.BevelGearMesh"
    ) -> "_6826.BevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelGearMeshLoadCase

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelGearMesh)
        """
        method_result = self.wrapped.InputsFor.Overloads[_BEVEL_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_conical_gear_mesh(
        self: Self, design_entity: "_2305.ConicalGearMesh"
    ) -> "_6844.ConicalGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConicalGearMeshLoadCase

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CONICAL_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_agma_gleason_conical_gear_mesh(
        self: Self, design_entity: "_2297.AGMAGleasonConicalGearMesh"
    ) -> "_6812.AGMAGleasonConicalGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearMeshLoadCase

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh)
        """
        method_result = self.wrapped.InputsFor.Overloads[
            _AGMA_GLEASON_CONICAL_GEAR_MESH
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_cylindrical_gear_mesh(
        self: Self, design_entity: "_2307.CylindricalGearMesh"
    ) -> "_6861.CylindricalGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearMeshLoadCase

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CYLINDRICAL_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_hypoid_gear_mesh(
        self: Self, design_entity: "_2313.HypoidGearMesh"
    ) -> "_6904.HypoidGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh)
        """
        method_result = self.wrapped.InputsFor.Overloads[_HYPOID_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_klingelnberg_cyclo_palloid_conical_gear_mesh(
        self: Self, design_entity: "_2316.KlingelnbergCycloPalloidConicalGearMesh"
    ) -> "_6911.KlingelnbergCycloPalloidConicalGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearMeshLoadCase

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh)
        """
        method_result = self.wrapped.InputsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh(
        self: Self, design_entity: "_2317.KlingelnbergCycloPalloidHypoidGearMesh"
    ) -> "_6914.KlingelnbergCycloPalloidHypoidGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearMeshLoadCase

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh)
        """
        method_result = self.wrapped.InputsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(
        self: Self, design_entity: "_2318.KlingelnbergCycloPalloidSpiralBevelGearMesh"
    ) -> "_6917.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh)
        """
        method_result = self.wrapped.InputsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_spiral_bevel_gear_mesh(
        self: Self, design_entity: "_2321.SpiralBevelGearMesh"
    ) -> "_6952.SpiralBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh)
        """
        method_result = self.wrapped.InputsFor.Overloads[_SPIRAL_BEVEL_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_straight_bevel_gear_mesh(
        self: Self, design_entity: "_2325.StraightBevelGearMesh"
    ) -> "_6961.StraightBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearMeshLoadCase

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh)
        """
        method_result = self.wrapped.InputsFor.Overloads[_STRAIGHT_BEVEL_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_worm_gear_mesh(
        self: Self, design_entity: "_2327.WormGearMesh"
    ) -> "_6981.WormGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.WormGearMeshLoadCase

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.WormGearMesh)
        """
        method_result = self.wrapped.InputsFor.Overloads[_WORM_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_zerol_bevel_gear_mesh(
        self: Self, design_entity: "_2329.ZerolBevelGearMesh"
    ) -> "_6984.ZerolBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearMeshLoadCase

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh)
        """
        method_result = self.wrapped.InputsFor.Overloads[_ZEROL_BEVEL_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_gear_mesh(
        self: Self, design_entity: "_2311.GearMesh"
    ) -> "_6890.GearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.GearMeshLoadCase

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.GearMesh)
        """
        method_result = self.wrapped.InputsFor.Overloads[_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_cycloidal_disc_central_bearing_connection(
        self: Self, design_entity: "_2333.CycloidalDiscCentralBearingConnection"
    ) -> "_6856.CycloidalDiscCentralBearingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscCentralBearingConnectionLoadCase

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscCentralBearingConnection)
        """
        method_result = self.wrapped.InputsFor.Overloads[
            _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_cycloidal_disc_planetary_bearing_connection(
        self: Self, design_entity: "_2336.CycloidalDiscPlanetaryBearingConnection"
    ) -> "_6858.CycloidalDiscPlanetaryBearingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscPlanetaryBearingConnectionLoadCase

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscPlanetaryBearingConnection)
        """
        method_result = self.wrapped.InputsFor.Overloads[
            _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_ring_pins_to_disc_connection(
        self: Self, design_entity: "_2339.RingPinsToDiscConnection"
    ) -> "_6942.RingPinsToDiscConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RingPinsToDiscConnectionLoadCase

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection)
        """
        method_result = self.wrapped.InputsFor.Overloads[_RING_PINS_TO_DISC_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_part_to_part_shear_coupling_connection(
        self: Self, design_entity: "_2346.PartToPartShearCouplingConnection"
    ) -> "_6927.PartToPartShearCouplingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingConnectionLoadCase

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection)
        """
        method_result = self.wrapped.InputsFor.Overloads[
            _PART_TO_PART_SHEAR_COUPLING_CONNECTION
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_clutch_connection(
        self: Self, design_entity: "_2340.ClutchConnection"
    ) -> "_6830.ClutchConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ClutchConnectionLoadCase

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ClutchConnection)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CLUTCH_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_concept_coupling_connection(
        self: Self, design_entity: "_2342.ConceptCouplingConnection"
    ) -> "_6836.ConceptCouplingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingConnectionLoadCase

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection)
        """
        method_result = self.wrapped.InputsFor.Overloads[_CONCEPT_COUPLING_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_coupling_connection(
        self: Self, design_entity: "_2344.CouplingConnection"
    ) -> "_6849.CouplingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CouplingConnectionLoadCase

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.CouplingConnection)
        """
        method_result = self.wrapped.InputsFor.Overloads[_COUPLING_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def inputs_for_spring_damper_connection(
        self: Self, design_entity: "_2348.SpringDamperConnection"
    ) -> "_6954.SpringDamperConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpringDamperConnectionLoadCase

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection)
        """
        method_result = self.wrapped.InputsFor.Overloads[_SPRING_DAMPER_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "LoadCase._Cast_LoadCase":
        return self._Cast_LoadCase(self)
