"""ModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy._internal.python_net import python_net_import
from mastapy.system_model.analyses_and_results import _2618
from mastapy._internal.cast_exception import CastException

_SPRING_DAMPER_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SpringDamperConnectionLoadCase",
)
_TORQUE_CONVERTER_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "TorqueConverterConnectionLoadCase",
)
_WORM_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "WormGearLoadCase"
)
_WORM_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "WormGearSetLoadCase"
)
_ZEROL_BEVEL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ZerolBevelGearLoadCase"
)
_ZEROL_BEVEL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ZerolBevelGearSetLoadCase",
)
_CYCLOIDAL_ASSEMBLY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CycloidalAssemblyLoadCase",
)
_CYCLOIDAL_DISC_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "CycloidalDiscLoadCase"
)
_RING_PINS_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "RingPinsLoadCase"
)
_PART_TO_PART_SHEAR_COUPLING_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "PartToPartShearCouplingLoadCase",
)
_PART_TO_PART_SHEAR_COUPLING_HALF_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "PartToPartShearCouplingHalfLoadCase",
)
_BELT_DRIVE_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BeltDriveLoadCase"
)
_CLUTCH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ClutchLoadCase"
)
_CLUTCH_HALF_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ClutchHalfLoadCase"
)
_CONCEPT_COUPLING_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConceptCouplingLoadCase"
)
_CONCEPT_COUPLING_HALF_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ConceptCouplingHalfLoadCase",
)
_COUPLING_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "CouplingLoadCase"
)
_COUPLING_HALF_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "CouplingHalfLoadCase"
)
_CVT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "CVTLoadCase"
)
_CVT_PULLEY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "CVTPulleyLoadCase"
)
_PULLEY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "PulleyLoadCase"
)
_SHAFT_HUB_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ShaftHubConnectionLoadCase",
)
_ROLLING_RING_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "RollingRingLoadCase"
)
_ROLLING_RING_ASSEMBLY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "RollingRingAssemblyLoadCase",
)
_SPRING_DAMPER_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "SpringDamperLoadCase"
)
_SPRING_DAMPER_HALF_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SpringDamperHalfLoadCase",
)
_SYNCHRONISER_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "SynchroniserLoadCase"
)
_SYNCHRONISER_HALF_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SynchroniserHalfLoadCase",
)
_SYNCHRONISER_PART_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SynchroniserPartLoadCase",
)
_SYNCHRONISER_SLEEVE_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SynchroniserSleeveLoadCase",
)
_TORQUE_CONVERTER_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "TorqueConverterLoadCase"
)
_TORQUE_CONVERTER_PUMP_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "TorqueConverterPumpLoadCase",
)
_TORQUE_CONVERTER_TURBINE_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "TorqueConverterTurbineLoadCase",
)
_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ShaftToMountableComponentConnectionLoadCase",
)
_CVT_BELT_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CVTBeltConnectionLoadCase",
)
_BELT_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BeltConnectionLoadCase"
)
_COAXIAL_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CoaxialConnectionLoadCase",
)
_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConnectionLoadCase"
)
_INTER_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "InterMountableComponentConnectionLoadCase",
)
_PLANETARY_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "PlanetaryConnectionLoadCase",
)
_ROLLING_RING_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "RollingRingConnectionLoadCase",
)
_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "AbstractShaftToMountableComponentConnectionLoadCase",
)
_BEVEL_DIFFERENTIAL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "BevelDifferentialGearMeshLoadCase",
)
_CONCEPT_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConceptGearMeshLoadCase"
)
_FACE_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "FaceGearMeshLoadCase"
)
_STRAIGHT_BEVEL_DIFF_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelDiffGearMeshLoadCase",
)
_BEVEL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BevelGearMeshLoadCase"
)
_CONICAL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConicalGearMeshLoadCase"
)
_AGMA_GLEASON_CONICAL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "AGMAGleasonConicalGearMeshLoadCase",
)
_CYLINDRICAL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CylindricalGearMeshLoadCase",
)
_HYPOID_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "HypoidGearMeshLoadCase"
)
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidConicalGearMeshLoadCase",
)
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidHypoidGearMeshLoadCase",
)
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase",
)
_SPIRAL_BEVEL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SpiralBevelGearMeshLoadCase",
)
_STRAIGHT_BEVEL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelGearMeshLoadCase",
)
_WORM_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "WormGearMeshLoadCase"
)
_ZEROL_BEVEL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ZerolBevelGearMeshLoadCase",
)
_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "GearMeshLoadCase"
)
_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CycloidalDiscCentralBearingConnectionLoadCase",
)
_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CycloidalDiscPlanetaryBearingConnectionLoadCase",
)
_RING_PINS_TO_DISC_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "RingPinsToDiscConnectionLoadCase",
)
_PART_TO_PART_SHEAR_COUPLING_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "PartToPartShearCouplingConnectionLoadCase",
)
_CLUTCH_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ClutchConnectionLoadCase",
)
_CONCEPT_COUPLING_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ConceptCouplingConnectionLoadCase",
)
_COUPLING_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CouplingConnectionLoadCase",
)
_ABSTRACT_SHAFT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "AbstractShaftLoadCase"
)
_ABSTRACT_ASSEMBLY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "AbstractAssemblyLoadCase",
)
_ABSTRACT_SHAFT_OR_HOUSING_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "AbstractShaftOrHousingLoadCase",
)
_BEARING_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BearingLoadCase"
)
_BOLT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BoltLoadCase"
)
_BOLTED_JOINT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BoltedJointLoadCase"
)
_COMPONENT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ComponentLoadCase"
)
_CONNECTOR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConnectorLoadCase"
)
_DATUM_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "DatumLoadCase"
)
_EXTERNAL_CAD_MODEL_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ExternalCADModelLoadCase",
)
_FE_PART_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "FEPartLoadCase"
)
_FLEXIBLE_PIN_ASSEMBLY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "FlexiblePinAssemblyLoadCase",
)
_ASSEMBLY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "AssemblyLoadCase"
)
_GUIDE_DXF_MODEL_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "GuideDxfModelLoadCase"
)
_MASS_DISC_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "MassDiscLoadCase"
)
_MEASUREMENT_COMPONENT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "MeasurementComponentLoadCase",
)
_MOUNTABLE_COMPONENT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "MountableComponentLoadCase",
)
_OIL_SEAL_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "OilSealLoadCase"
)
_PART_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "PartLoadCase"
)
_PLANET_CARRIER_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "PlanetCarrierLoadCase"
)
_POINT_LOAD_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "PointLoadLoadCase"
)
_POWER_LOAD_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "PowerLoadLoadCase"
)
_ROOT_ASSEMBLY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "RootAssemblyLoadCase"
)
_SPECIALISED_ASSEMBLY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SpecialisedAssemblyLoadCase",
)
_UNBALANCED_MASS_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "UnbalancedMassLoadCase"
)
_VIRTUAL_COMPONENT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "VirtualComponentLoadCase",
)
_SHAFT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ShaftLoadCase"
)
_CONCEPT_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConceptGearLoadCase"
)
_CONCEPT_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConceptGearSetLoadCase"
)
_FACE_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "FaceGearLoadCase"
)
_FACE_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "FaceGearSetLoadCase"
)
_AGMA_GLEASON_CONICAL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "AGMAGleasonConicalGearLoadCase",
)
_AGMA_GLEASON_CONICAL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "AGMAGleasonConicalGearSetLoadCase",
)
_BEVEL_DIFFERENTIAL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "BevelDifferentialGearLoadCase",
)
_BEVEL_DIFFERENTIAL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "BevelDifferentialGearSetLoadCase",
)
_BEVEL_DIFFERENTIAL_PLANET_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "BevelDifferentialPlanetGearLoadCase",
)
_BEVEL_DIFFERENTIAL_SUN_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "BevelDifferentialSunGearLoadCase",
)
_BEVEL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BevelGearLoadCase"
)
_BEVEL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BevelGearSetLoadCase"
)
_CONICAL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConicalGearLoadCase"
)
_CONICAL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConicalGearSetLoadCase"
)
_CYLINDRICAL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "CylindricalGearLoadCase"
)
_CYLINDRICAL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CylindricalGearSetLoadCase",
)
_CYLINDRICAL_PLANET_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CylindricalPlanetGearLoadCase",
)
_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "GearLoadCase"
)
_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "GearSetLoadCase"
)
_HYPOID_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "HypoidGearLoadCase"
)
_HYPOID_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "HypoidGearSetLoadCase"
)
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidConicalGearLoadCase",
)
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidConicalGearSetLoadCase",
)
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidHypoidGearLoadCase",
)
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidHypoidGearSetLoadCase",
)
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidSpiralBevelGearLoadCase",
)
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
)
_PLANETARY_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "PlanetaryGearSetLoadCase",
)
_SPIRAL_BEVEL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "SpiralBevelGearLoadCase"
)
_SPIRAL_BEVEL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SpiralBevelGearSetLoadCase",
)
_STRAIGHT_BEVEL_DIFF_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelDiffGearLoadCase",
)
_STRAIGHT_BEVEL_DIFF_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelDiffGearSetLoadCase",
)
_STRAIGHT_BEVEL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelGearLoadCase",
)
_STRAIGHT_BEVEL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelGearSetLoadCase",
)
_STRAIGHT_BEVEL_PLANET_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelPlanetGearLoadCase",
)
_STRAIGHT_BEVEL_SUN_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelSunGearLoadCase",
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
_SPRING_DAMPER_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings", "SpringDamperConnection"
)
_WORM_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "WormGearSet"
)
_ZEROL_BEVEL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ZerolBevelGear"
)
_ZEROL_BEVEL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ZerolBevelGearSet"
)
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
_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults", "ModalAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6954,
        _6970,
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
        _6937,
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
    )
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4683,
        _4698,
        _4708,
        _4709,
        _4711,
        _4712,
        _4613,
        _4615,
        _4669,
        _4662,
        _4661,
        _4579,
        _4592,
        _4591,
        _4597,
        _4596,
        _4609,
        _4608,
        _4611,
        _4612,
        _4668,
        _4675,
        _4673,
        _4671,
        _4685,
        _4684,
        _4695,
        _4694,
        _4696,
        _4697,
        _4699,
        _4700,
        _4701,
        _4678,
        _4610,
        _4578,
        _4593,
        _4604,
        _4639,
        _4663,
        _4672,
        _4572,
        _4580,
        _4598,
        _4626,
        _4686,
        _4585,
        _4601,
        _4573,
        _4617,
        _4636,
        _4640,
        _4643,
        _4646,
        _4680,
        _4689,
        _4707,
        _4710,
        _4632,
        _4614,
        _4616,
        _4670,
        _4660,
        _4590,
        _4595,
        _4607,
        _4570,
        _4569,
        _4571,
        _4577,
        _4589,
        _4588,
        _4594,
        _4605,
        _4621,
        _4625,
        _4629,
        _4630,
        _4576,
        _4635,
        _4649,
        _4650,
        _4655,
        _4657,
        _4659,
        _4665,
        _4666,
        _4667,
        _4674,
        _4679,
        _4702,
        _4703,
        _4676,
        _4599,
        _4600,
        _4627,
        _4628,
        _4574,
        _4575,
        _4581,
        _4582,
        _4583,
        _4584,
        _4586,
        _4587,
        _4602,
        _4603,
        _4618,
        _4619,
        _4620,
        _4633,
        _4634,
        _4637,
        _4638,
        _4641,
        _4642,
        _4644,
        _4645,
        _4647,
        _4648,
        _4664,
        _4681,
        _4682,
        _4687,
        _4688,
        _4690,
        _4691,
        _4692,
        _4693,
    )
    from mastapy.system_model.connections_and_sockets.couplings import (
        _2350,
        _2346,
        _2340,
        _2342,
        _2344,
        _2348,
    )
    from mastapy.system_model.part_model.gears import (
        _2550,
        _2551,
        _2552,
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


__docformat__ = "restructuredtext en"
__all__ = ("ModalAnalysis",)


Self = TypeVar("Self", bound="ModalAnalysis")


class ModalAnalysis(_2618.SingleAnalysis):
    """ModalAnalysis

    This is a mastapy class.
    """

    TYPE = _MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ModalAnalysis")

    class _Cast_ModalAnalysis:
        """Special nested class for casting ModalAnalysis to subclasses."""

        def __init__(
            self: "ModalAnalysis._Cast_ModalAnalysis", parent: "ModalAnalysis"
        ):
            self._parent = parent

        @property
        def single_analysis(self: "ModalAnalysis._Cast_ModalAnalysis"):
            return self._parent._cast(_2618.SingleAnalysis)

        @property
        def marshal_by_ref_object_permanent(self: "ModalAnalysis._Cast_ModalAnalysis"):
            from mastapy import _7550

            return self._parent._cast(_7550.MarshalByRefObjectPermanent)

        @property
        def modal_analysis(
            self: "ModalAnalysis._Cast_ModalAnalysis",
        ) -> "ModalAnalysis":
            return self._parent

        def __getattr__(self: "ModalAnalysis._Cast_ModalAnalysis", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @enforce_parameter_types
    def results_for_spring_damper_connection_load_case(
        self: Self, design_entity_analysis: "_6954.SpringDamperConnectionLoadCase"
    ) -> "_4683.SpringDamperConnectionModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.SpringDamperConnectionModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _SPRING_DAMPER_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_torque_converter_connection(
        self: Self, design_entity: "_2350.TorqueConverterConnection"
    ) -> "_4698.TorqueConverterConnectionModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.TorqueConverterConnectionModalAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_torque_converter_connection_load_case(
        self: Self, design_entity_analysis: "_6970.TorqueConverterConnectionLoadCase"
    ) -> "_4698.TorqueConverterConnectionModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.TorqueConverterConnectionModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _TORQUE_CONVERTER_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_worm_gear_load_case(
        self: Self, design_entity_analysis: "_6980.WormGearLoadCase"
    ) -> "_4708.WormGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.WormGearModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_WORM_GEAR_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_worm_gear_set(
        self: Self, design_entity: "_2550.WormGearSet"
    ) -> "_4709.WormGearSetModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.WormGearSetModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_WORM_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_worm_gear_set_load_case(
        self: Self, design_entity_analysis: "_6982.WormGearSetLoadCase"
    ) -> "_4709.WormGearSetModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.WormGearSetModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_WORM_GEAR_SET_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_zerol_bevel_gear(
        self: Self, design_entity: "_2551.ZerolBevelGear"
    ) -> "_4711.ZerolBevelGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ZerolBevelGearModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_zerol_bevel_gear_load_case(
        self: Self, design_entity_analysis: "_6983.ZerolBevelGearLoadCase"
    ) -> "_4711.ZerolBevelGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ZerolBevelGearModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_zerol_bevel_gear_set(
        self: Self, design_entity: "_2552.ZerolBevelGearSet"
    ) -> "_4712.ZerolBevelGearSetModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ZerolBevelGearSetModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_zerol_bevel_gear_set_load_case(
        self: Self, design_entity_analysis: "_6985.ZerolBevelGearSetLoadCase"
    ) -> "_4712.ZerolBevelGearSetModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ZerolBevelGearSetModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _ZEROL_BEVEL_GEAR_SET_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cycloidal_assembly(
        self: Self, design_entity: "_2566.CycloidalAssembly"
    ) -> "_4613.CycloidalAssemblyModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.CycloidalAssemblyModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.cycloidal.CycloidalAssembly)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_ASSEMBLY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cycloidal_assembly_load_case(
        self: Self, design_entity_analysis: "_6855.CycloidalAssemblyLoadCase"
    ) -> "_4613.CycloidalAssemblyModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.CycloidalAssemblyModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CycloidalAssemblyLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _CYCLOIDAL_ASSEMBLY_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cycloidal_disc(
        self: Self, design_entity: "_2567.CycloidalDisc"
    ) -> "_4615.CycloidalDiscModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.CycloidalDiscModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.cycloidal.CycloidalDisc)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_DISC](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cycloidal_disc_load_case(
        self: Self, design_entity_analysis: "_6857.CycloidalDiscLoadCase"
    ) -> "_4615.CycloidalDiscModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.CycloidalDiscModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_DISC_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_ring_pins(
        self: Self, design_entity: "_2568.RingPins"
    ) -> "_4669.RingPinsModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.RingPinsModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.cycloidal.RingPins)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_RING_PINS](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_ring_pins_load_case(
        self: Self, design_entity_analysis: "_6941.RingPinsLoadCase"
    ) -> "_4669.RingPinsModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.RingPinsModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RingPinsLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_RING_PINS_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_part_to_part_shear_coupling(
        self: Self, design_entity: "_2586.PartToPartShearCoupling"
    ) -> "_4662.PartToPartShearCouplingModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.PartToPartShearCouplingModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCoupling)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_part_to_part_shear_coupling_load_case(
        self: Self, design_entity_analysis: "_6929.PartToPartShearCouplingLoadCase"
    ) -> "_4662.PartToPartShearCouplingModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.PartToPartShearCouplingModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _PART_TO_PART_SHEAR_COUPLING_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_part_to_part_shear_coupling_half(
        self: Self, design_entity: "_2587.PartToPartShearCouplingHalf"
    ) -> "_4661.PartToPartShearCouplingHalfModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.PartToPartShearCouplingHalfModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _PART_TO_PART_SHEAR_COUPLING_HALF
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_part_to_part_shear_coupling_half_load_case(
        self: Self, design_entity_analysis: "_6928.PartToPartShearCouplingHalfLoadCase"
    ) -> "_4661.PartToPartShearCouplingHalfModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.PartToPartShearCouplingHalfModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingHalfLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _PART_TO_PART_SHEAR_COUPLING_HALF_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_belt_drive(
        self: Self, design_entity: "_2574.BeltDrive"
    ) -> "_4579.BeltDriveModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.BeltDriveModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.BeltDrive)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BELT_DRIVE](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_belt_drive_load_case(
        self: Self, design_entity_analysis: "_6819.BeltDriveLoadCase"
    ) -> "_4579.BeltDriveModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.BeltDriveModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BeltDriveLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BELT_DRIVE_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_clutch(
        self: Self, design_entity: "_2576.Clutch"
    ) -> "_4592.ClutchModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ClutchModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Clutch)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CLUTCH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_clutch_load_case(
        self: Self, design_entity_analysis: "_6832.ClutchLoadCase"
    ) -> "_4592.ClutchModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ClutchModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CLUTCH_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_clutch_half(
        self: Self, design_entity: "_2577.ClutchHalf"
    ) -> "_4591.ClutchHalfModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ClutchHalfModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ClutchHalf)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CLUTCH_HALF](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_clutch_half_load_case(
        self: Self, design_entity_analysis: "_6831.ClutchHalfLoadCase"
    ) -> "_4591.ClutchHalfModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ClutchHalfModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchHalfLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CLUTCH_HALF_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_coupling(
        self: Self, design_entity: "_2579.ConceptCoupling"
    ) -> "_4597.ConceptCouplingModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ConceptCouplingModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCoupling)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_coupling_load_case(
        self: Self, design_entity_analysis: "_6838.ConceptCouplingLoadCase"
    ) -> "_4597.ConceptCouplingModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ConceptCouplingModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_coupling_half(
        self: Self, design_entity: "_2580.ConceptCouplingHalf"
    ) -> "_4596.ConceptCouplingHalfModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ConceptCouplingHalfModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCouplingHalf)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING_HALF](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_coupling_half_load_case(
        self: Self, design_entity_analysis: "_6837.ConceptCouplingHalfLoadCase"
    ) -> "_4596.ConceptCouplingHalfModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ConceptCouplingHalfModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingHalfLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _CONCEPT_COUPLING_HALF_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_coupling(
        self: Self, design_entity: "_2581.Coupling"
    ) -> "_4609.CouplingModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.CouplingModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Coupling)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_COUPLING](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_coupling_load_case(
        self: Self, design_entity_analysis: "_6851.CouplingLoadCase"
    ) -> "_4609.CouplingModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.CouplingModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_COUPLING_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_coupling_half(
        self: Self, design_entity: "_2582.CouplingHalf"
    ) -> "_4608.CouplingHalfModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.CouplingHalfModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CouplingHalf)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_COUPLING_HALF](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_coupling_half_load_case(
        self: Self, design_entity_analysis: "_6850.CouplingHalfLoadCase"
    ) -> "_4608.CouplingHalfModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.CouplingHalfModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingHalfLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_COUPLING_HALF_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cvt(
        self: Self, design_entity: "_2584.CVT"
    ) -> "_4611.CVTModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.CVTModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVT)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CVT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cvt_load_case(
        self: Self, design_entity_analysis: "_6853.CVTLoadCase"
    ) -> "_4611.CVTModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.CVTModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CVT_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cvt_pulley(
        self: Self, design_entity: "_2585.CVTPulley"
    ) -> "_4612.CVTPulleyModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.CVTPulleyModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVTPulley)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CVT_PULLEY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cvt_pulley_load_case(
        self: Self, design_entity_analysis: "_6854.CVTPulleyLoadCase"
    ) -> "_4612.CVTPulleyModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.CVTPulleyModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTPulleyLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CVT_PULLEY_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_pulley(
        self: Self, design_entity: "_2588.Pulley"
    ) -> "_4668.PulleyModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.PulleyModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Pulley)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_PULLEY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_pulley_load_case(
        self: Self, design_entity_analysis: "_6938.PulleyLoadCase"
    ) -> "_4668.PulleyModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.PulleyModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PulleyLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_PULLEY_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_shaft_hub_connection(
        self: Self, design_entity: "_2596.ShaftHubConnection"
    ) -> "_4675.ShaftHubConnectionModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ShaftHubConnectionModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ShaftHubConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SHAFT_HUB_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_shaft_hub_connection_load_case(
        self: Self, design_entity_analysis: "_6947.ShaftHubConnectionLoadCase"
    ) -> "_4675.ShaftHubConnectionModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ShaftHubConnectionModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftHubConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _SHAFT_HUB_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_rolling_ring(
        self: Self, design_entity: "_2594.RollingRing"
    ) -> "_4673.RollingRingModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.RollingRingModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRing)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ROLLING_RING](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_rolling_ring_load_case(
        self: Self, design_entity_analysis: "_6945.RollingRingLoadCase"
    ) -> "_4673.RollingRingModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.RollingRingModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ROLLING_RING_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_rolling_ring_assembly(
        self: Self, design_entity: "_2595.RollingRingAssembly"
    ) -> "_4671.RollingRingAssemblyModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.RollingRingAssemblyModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRingAssembly)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ROLLING_RING_ASSEMBLY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_rolling_ring_assembly_load_case(
        self: Self, design_entity_analysis: "_6943.RollingRingAssemblyLoadCase"
    ) -> "_4671.RollingRingAssemblyModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.RollingRingAssemblyModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingAssemblyLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _ROLLING_RING_ASSEMBLY_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spring_damper(
        self: Self, design_entity: "_2598.SpringDamper"
    ) -> "_4685.SpringDamperModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.SpringDamperModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamper)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spring_damper_load_case(
        self: Self, design_entity_analysis: "_6956.SpringDamperLoadCase"
    ) -> "_4685.SpringDamperModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.SpringDamperModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spring_damper_half(
        self: Self, design_entity: "_2599.SpringDamperHalf"
    ) -> "_4684.SpringDamperHalfModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.SpringDamperHalfModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamperHalf)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER_HALF](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spring_damper_half_load_case(
        self: Self, design_entity_analysis: "_6955.SpringDamperHalfLoadCase"
    ) -> "_4684.SpringDamperHalfModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.SpringDamperHalfModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperHalfLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _SPRING_DAMPER_HALF_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_synchroniser(
        self: Self, design_entity: "_2600.Synchroniser"
    ) -> "_4695.SynchroniserModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.SynchroniserModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Synchroniser)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SYNCHRONISER](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_synchroniser_load_case(
        self: Self, design_entity_analysis: "_6966.SynchroniserLoadCase"
    ) -> "_4695.SynchroniserModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.SynchroniserModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_synchroniser_half(
        self: Self, design_entity: "_2602.SynchroniserHalf"
    ) -> "_4694.SynchroniserHalfModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.SynchroniserHalfModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserHalf)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_HALF](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_synchroniser_half_load_case(
        self: Self, design_entity_analysis: "_6965.SynchroniserHalfLoadCase"
    ) -> "_4694.SynchroniserHalfModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.SynchroniserHalfModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserHalfLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_HALF_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_synchroniser_part(
        self: Self, design_entity: "_2603.SynchroniserPart"
    ) -> "_4696.SynchroniserPartModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.SynchroniserPartModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserPart)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_PART](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_synchroniser_part_load_case(
        self: Self, design_entity_analysis: "_6967.SynchroniserPartLoadCase"
    ) -> "_4696.SynchroniserPartModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.SynchroniserPartModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserPartLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_PART_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_synchroniser_sleeve(
        self: Self, design_entity: "_2604.SynchroniserSleeve"
    ) -> "_4697.SynchroniserSleeveModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.SynchroniserSleeveModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserSleeve)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_SLEEVE](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_synchroniser_sleeve_load_case(
        self: Self, design_entity_analysis: "_6968.SynchroniserSleeveLoadCase"
    ) -> "_4697.SynchroniserSleeveModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.SynchroniserSleeveModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _SYNCHRONISER_SLEEVE_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_torque_converter(
        self: Self, design_entity: "_2605.TorqueConverter"
    ) -> "_4699.TorqueConverterModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.TorqueConverterModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverter)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_torque_converter_load_case(
        self: Self, design_entity_analysis: "_6971.TorqueConverterLoadCase"
    ) -> "_4699.TorqueConverterModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.TorqueConverterModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_torque_converter_pump(
        self: Self, design_entity: "_2606.TorqueConverterPump"
    ) -> "_4700.TorqueConverterPumpModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.TorqueConverterPumpModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterPump)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_PUMP](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_torque_converter_pump_load_case(
        self: Self, design_entity_analysis: "_6972.TorqueConverterPumpLoadCase"
    ) -> "_4700.TorqueConverterPumpModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.TorqueConverterPumpModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterPumpLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _TORQUE_CONVERTER_PUMP_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_torque_converter_turbine(
        self: Self, design_entity: "_2608.TorqueConverterTurbine"
    ) -> "_4701.TorqueConverterTurbineModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.TorqueConverterTurbineModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterTurbine)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_TURBINE](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_torque_converter_turbine_load_case(
        self: Self, design_entity_analysis: "_6973.TorqueConverterTurbineLoadCase"
    ) -> "_4701.TorqueConverterTurbineModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.TorqueConverterTurbineModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterTurbineLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _TORQUE_CONVERTER_TURBINE_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_shaft_to_mountable_component_connection(
        self: Self, design_entity: "_2293.ShaftToMountableComponentConnection"
    ) -> "_4678.ShaftToMountableComponentConnectionModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ShaftToMountableComponentConnectionModalAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_shaft_to_mountable_component_connection_load_case(
        self: Self,
        design_entity_analysis: "_6949.ShaftToMountableComponentConnectionLoadCase",
    ) -> "_4678.ShaftToMountableComponentConnectionModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ShaftToMountableComponentConnectionModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftToMountableComponentConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cvt_belt_connection(
        self: Self, design_entity: "_2271.CVTBeltConnection"
    ) -> "_4610.CVTBeltConnectionModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.CVTBeltConnectionModalAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CVTBeltConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CVT_BELT_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cvt_belt_connection_load_case(
        self: Self, design_entity_analysis: "_6852.CVTBeltConnectionLoadCase"
    ) -> "_4610.CVTBeltConnectionModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.CVTBeltConnectionModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTBeltConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _CVT_BELT_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_belt_connection(
        self: Self, design_entity: "_2266.BeltConnection"
    ) -> "_4578.BeltConnectionModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.BeltConnectionModalAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.BeltConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BELT_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_belt_connection_load_case(
        self: Self, design_entity_analysis: "_6818.BeltConnectionLoadCase"
    ) -> "_4578.BeltConnectionModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.BeltConnectionModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BeltConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BELT_CONNECTION_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_coaxial_connection(
        self: Self, design_entity: "_2267.CoaxialConnection"
    ) -> "_4593.CoaxialConnectionModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.CoaxialConnectionModalAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CoaxialConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_COAXIAL_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_coaxial_connection_load_case(
        self: Self, design_entity_analysis: "_6834.CoaxialConnectionLoadCase"
    ) -> "_4593.CoaxialConnectionModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.CoaxialConnectionModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CoaxialConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _COAXIAL_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_connection(
        self: Self, design_entity: "_2270.Connection"
    ) -> "_4604.ConnectionModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ConnectionModalAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.Connection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_connection_load_case(
        self: Self, design_entity_analysis: "_6847.ConnectionLoadCase"
    ) -> "_4604.ConnectionModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ConnectionModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONNECTION_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_inter_mountable_component_connection(
        self: Self, design_entity: "_2279.InterMountableComponentConnection"
    ) -> "_4639.InterMountableComponentConnectionModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.InterMountableComponentConnectionModalAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.InterMountableComponentConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _INTER_MOUNTABLE_COMPONENT_CONNECTION
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_inter_mountable_component_connection_load_case(
        self: Self,
        design_entity_analysis: "_6909.InterMountableComponentConnectionLoadCase",
    ) -> "_4639.InterMountableComponentConnectionModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.InterMountableComponentConnectionModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.InterMountableComponentConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _INTER_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_planetary_connection(
        self: Self, design_entity: "_2285.PlanetaryConnection"
    ) -> "_4663.PlanetaryConnectionModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.PlanetaryConnectionModalAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.PlanetaryConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_PLANETARY_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_planetary_connection_load_case(
        self: Self, design_entity_analysis: "_6930.PlanetaryConnectionLoadCase"
    ) -> "_4663.PlanetaryConnectionModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.PlanetaryConnectionModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetaryConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _PLANETARY_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_rolling_ring_connection(
        self: Self, design_entity: "_2290.RollingRingConnection"
    ) -> "_4672.RollingRingConnectionModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.RollingRingConnectionModalAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.RollingRingConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ROLLING_RING_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_rolling_ring_connection_load_case(
        self: Self, design_entity_analysis: "_6944.RollingRingConnectionLoadCase"
    ) -> "_4672.RollingRingConnectionModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.RollingRingConnectionModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _ROLLING_RING_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_abstract_shaft_to_mountable_component_connection(
        self: Self, design_entity: "_2263.AbstractShaftToMountableComponentConnection"
    ) -> "_4572.AbstractShaftToMountableComponentConnectionModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.AbstractShaftToMountableComponentConnectionModalAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.AbstractShaftToMountableComponentConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_abstract_shaft_to_mountable_component_connection_load_case(
        self: Self,
        design_entity_analysis: "_6807.AbstractShaftToMountableComponentConnectionLoadCase",
    ) -> "_4572.AbstractShaftToMountableComponentConnectionModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.AbstractShaftToMountableComponentConnectionModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractShaftToMountableComponentConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_differential_gear_mesh(
        self: Self, design_entity: "_2299.BevelDifferentialGearMesh"
    ) -> "_4580.BevelDifferentialGearMeshModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialGearMeshModalAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _BEVEL_DIFFERENTIAL_GEAR_MESH
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_differential_gear_mesh_load_case(
        self: Self, design_entity_analysis: "_6821.BevelDifferentialGearMeshLoadCase"
    ) -> "_4580.BevelDifferentialGearMeshModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialGearMeshModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _BEVEL_DIFFERENTIAL_GEAR_MESH_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_gear_mesh(
        self: Self, design_entity: "_2303.ConceptGearMesh"
    ) -> "_4598.ConceptGearMeshModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ConceptGearMeshModalAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_gear_mesh_load_case(
        self: Self, design_entity_analysis: "_6840.ConceptGearMeshLoadCase"
    ) -> "_4598.ConceptGearMeshModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ConceptGearMeshModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_MESH_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_face_gear_mesh(
        self: Self, design_entity: "_2309.FaceGearMesh"
    ) -> "_4626.FaceGearMeshModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.FaceGearMeshModalAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.FaceGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_FACE_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_face_gear_mesh_load_case(
        self: Self, design_entity_analysis: "_6883.FaceGearMeshLoadCase"
    ) -> "_4626.FaceGearMeshModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.FaceGearMeshModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_FACE_GEAR_MESH_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_diff_gear_mesh(
        self: Self, design_entity: "_2323.StraightBevelDiffGearMesh"
    ) -> "_4686.StraightBevelDiffGearMeshModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelDiffGearMeshModalAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _STRAIGHT_BEVEL_DIFF_GEAR_MESH
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_diff_gear_mesh_load_case(
        self: Self, design_entity_analysis: "_6958.StraightBevelDiffGearMeshLoadCase"
    ) -> "_4686.StraightBevelDiffGearMeshModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelDiffGearMeshModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _STRAIGHT_BEVEL_DIFF_GEAR_MESH_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_gear_mesh(
        self: Self, design_entity: "_2301.BevelGearMesh"
    ) -> "_4585.BevelGearMeshModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.BevelGearMeshModalAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_gear_mesh_load_case(
        self: Self, design_entity_analysis: "_6826.BevelGearMeshLoadCase"
    ) -> "_4585.BevelGearMeshModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.BevelGearMeshModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_MESH_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_conical_gear_mesh(
        self: Self, design_entity: "_2305.ConicalGearMesh"
    ) -> "_4601.ConicalGearMeshModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ConicalGearMeshModalAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_conical_gear_mesh_load_case(
        self: Self, design_entity_analysis: "_6844.ConicalGearMeshLoadCase"
    ) -> "_4601.ConicalGearMeshModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ConicalGearMeshModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_MESH_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_agma_gleason_conical_gear_mesh(
        self: Self, design_entity: "_2297.AGMAGleasonConicalGearMesh"
    ) -> "_4573.AGMAGleasonConicalGearMeshModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.AGMAGleasonConicalGearMeshModalAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _AGMA_GLEASON_CONICAL_GEAR_MESH
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_agma_gleason_conical_gear_mesh_load_case(
        self: Self, design_entity_analysis: "_6812.AGMAGleasonConicalGearMeshLoadCase"
    ) -> "_4573.AGMAGleasonConicalGearMeshModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.AGMAGleasonConicalGearMeshModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _AGMA_GLEASON_CONICAL_GEAR_MESH_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cylindrical_gear_mesh(
        self: Self, design_entity: "_2307.CylindricalGearMesh"
    ) -> "_4617.CylindricalGearMeshModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.CylindricalGearMeshModalAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cylindrical_gear_mesh_load_case(
        self: Self, design_entity_analysis: "_6861.CylindricalGearMeshLoadCase"
    ) -> "_4617.CylindricalGearMeshModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.CylindricalGearMeshModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _CYLINDRICAL_GEAR_MESH_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_hypoid_gear_mesh(
        self: Self, design_entity: "_2313.HypoidGearMesh"
    ) -> "_4636.HypoidGearMeshModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.HypoidGearMeshModalAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_hypoid_gear_mesh_load_case(
        self: Self, design_entity_analysis: "_6904.HypoidGearMeshLoadCase"
    ) -> "_4636.HypoidGearMeshModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.HypoidGearMeshModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_MESH_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh(
        self: Self, design_entity: "_2316.KlingelnbergCycloPalloidConicalGearMesh"
    ) -> "_4640.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(
        self: Self,
        design_entity_analysis: "_6911.KlingelnbergCycloPalloidConicalGearMeshLoadCase",
    ) -> "_4640.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh(
        self: Self, design_entity: "_2317.KlingelnbergCycloPalloidHypoidGearMesh"
    ) -> "_4643.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(
        self: Self,
        design_entity_analysis: "_6914.KlingelnbergCycloPalloidHypoidGearMeshLoadCase",
    ) -> "_4643.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(
        self: Self, design_entity: "_2318.KlingelnbergCycloPalloidSpiralBevelGearMesh"
    ) -> "_4646.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_load_case(
        self: Self,
        design_entity_analysis: "_6917.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase",
    ) -> "_4646.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spiral_bevel_gear_mesh(
        self: Self, design_entity: "_2321.SpiralBevelGearMesh"
    ) -> "_4680.SpiralBevelGearMeshModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.SpiralBevelGearMeshModalAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spiral_bevel_gear_mesh_load_case(
        self: Self, design_entity_analysis: "_6952.SpiralBevelGearMeshLoadCase"
    ) -> "_4680.SpiralBevelGearMeshModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.SpiralBevelGearMeshModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _SPIRAL_BEVEL_GEAR_MESH_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_gear_mesh(
        self: Self, design_entity: "_2325.StraightBevelGearMesh"
    ) -> "_4689.StraightBevelGearMeshModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelGearMeshModalAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_gear_mesh_load_case(
        self: Self, design_entity_analysis: "_6961.StraightBevelGearMeshLoadCase"
    ) -> "_4689.StraightBevelGearMeshModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelGearMeshModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _STRAIGHT_BEVEL_GEAR_MESH_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_worm_gear_mesh(
        self: Self, design_entity: "_2327.WormGearMesh"
    ) -> "_4707.WormGearMeshModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.WormGearMeshModalAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.WormGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_WORM_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_worm_gear_mesh_load_case(
        self: Self, design_entity_analysis: "_6981.WormGearMeshLoadCase"
    ) -> "_4707.WormGearMeshModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.WormGearMeshModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_WORM_GEAR_MESH_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_zerol_bevel_gear_mesh(
        self: Self, design_entity: "_2329.ZerolBevelGearMesh"
    ) -> "_4710.ZerolBevelGearMeshModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ZerolBevelGearMeshModalAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_zerol_bevel_gear_mesh_load_case(
        self: Self, design_entity_analysis: "_6984.ZerolBevelGearMeshLoadCase"
    ) -> "_4710.ZerolBevelGearMeshModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ZerolBevelGearMeshModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _ZEROL_BEVEL_GEAR_MESH_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_gear_mesh(
        self: Self, design_entity: "_2311.GearMesh"
    ) -> "_4632.GearMeshModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.GearMeshModalAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.GearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_gear_mesh_load_case(
        self: Self, design_entity_analysis: "_6890.GearMeshLoadCase"
    ) -> "_4632.GearMeshModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.GearMeshModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_GEAR_MESH_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cycloidal_disc_central_bearing_connection(
        self: Self, design_entity: "_2333.CycloidalDiscCentralBearingConnection"
    ) -> "_4614.CycloidalDiscCentralBearingConnectionModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.CycloidalDiscCentralBearingConnectionModalAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscCentralBearingConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cycloidal_disc_central_bearing_connection_load_case(
        self: Self,
        design_entity_analysis: "_6856.CycloidalDiscCentralBearingConnectionLoadCase",
    ) -> "_4614.CycloidalDiscCentralBearingConnectionModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.CycloidalDiscCentralBearingConnectionModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscCentralBearingConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cycloidal_disc_planetary_bearing_connection(
        self: Self, design_entity: "_2336.CycloidalDiscPlanetaryBearingConnection"
    ) -> "_4616.CycloidalDiscPlanetaryBearingConnectionModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.CycloidalDiscPlanetaryBearingConnectionModalAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscPlanetaryBearingConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cycloidal_disc_planetary_bearing_connection_load_case(
        self: Self,
        design_entity_analysis: "_6858.CycloidalDiscPlanetaryBearingConnectionLoadCase",
    ) -> "_4616.CycloidalDiscPlanetaryBearingConnectionModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.CycloidalDiscPlanetaryBearingConnectionModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscPlanetaryBearingConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_ring_pins_to_disc_connection(
        self: Self, design_entity: "_2339.RingPinsToDiscConnection"
    ) -> "_4670.RingPinsToDiscConnectionModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.RingPinsToDiscConnectionModalAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _RING_PINS_TO_DISC_CONNECTION
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_ring_pins_to_disc_connection_load_case(
        self: Self, design_entity_analysis: "_6942.RingPinsToDiscConnectionLoadCase"
    ) -> "_4670.RingPinsToDiscConnectionModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.RingPinsToDiscConnectionModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RingPinsToDiscConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _RING_PINS_TO_DISC_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_part_to_part_shear_coupling_connection(
        self: Self, design_entity: "_2346.PartToPartShearCouplingConnection"
    ) -> "_4660.PartToPartShearCouplingConnectionModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.PartToPartShearCouplingConnectionModalAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _PART_TO_PART_SHEAR_COUPLING_CONNECTION
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_part_to_part_shear_coupling_connection_load_case(
        self: Self,
        design_entity_analysis: "_6927.PartToPartShearCouplingConnectionLoadCase",
    ) -> "_4660.PartToPartShearCouplingConnectionModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.PartToPartShearCouplingConnectionModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _PART_TO_PART_SHEAR_COUPLING_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_clutch_connection(
        self: Self, design_entity: "_2340.ClutchConnection"
    ) -> "_4590.ClutchConnectionModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ClutchConnectionModalAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ClutchConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CLUTCH_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_clutch_connection_load_case(
        self: Self, design_entity_analysis: "_6830.ClutchConnectionLoadCase"
    ) -> "_4590.ClutchConnectionModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ClutchConnectionModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CLUTCH_CONNECTION_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_coupling_connection(
        self: Self, design_entity: "_2342.ConceptCouplingConnection"
    ) -> "_4595.ConceptCouplingConnectionModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ConceptCouplingConnectionModalAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_coupling_connection_load_case(
        self: Self, design_entity_analysis: "_6836.ConceptCouplingConnectionLoadCase"
    ) -> "_4595.ConceptCouplingConnectionModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ConceptCouplingConnectionModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _CONCEPT_COUPLING_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_coupling_connection(
        self: Self, design_entity: "_2344.CouplingConnection"
    ) -> "_4607.CouplingConnectionModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.CouplingConnectionModalAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.CouplingConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_COUPLING_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_coupling_connection_load_case(
        self: Self, design_entity_analysis: "_6849.CouplingConnectionLoadCase"
    ) -> "_4607.CouplingConnectionModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.CouplingConnectionModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _COUPLING_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spring_damper_connection(
        self: Self, design_entity: "_2348.SpringDamperConnection"
    ) -> "_4683.SpringDamperConnectionModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.SpringDamperConnectionModalAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_abstract_shaft(
        self: Self, design_entity: "_2433.AbstractShaft"
    ) -> "_4570.AbstractShaftModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.AbstractShaftModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaft)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ABSTRACT_SHAFT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_abstract_shaft_load_case(
        self: Self, design_entity_analysis: "_6805.AbstractShaftLoadCase"
    ) -> "_4570.AbstractShaftModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.AbstractShaftModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractShaftLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ABSTRACT_SHAFT_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_abstract_assembly(
        self: Self, design_entity: "_2432.AbstractAssembly"
    ) -> "_4569.AbstractAssemblyModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.AbstractAssemblyModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.AbstractAssembly)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ABSTRACT_ASSEMBLY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_abstract_assembly_load_case(
        self: Self, design_entity_analysis: "_6804.AbstractAssemblyLoadCase"
    ) -> "_4569.AbstractAssemblyModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.AbstractAssemblyModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractAssemblyLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ABSTRACT_ASSEMBLY_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_abstract_shaft_or_housing(
        self: Self, design_entity: "_2434.AbstractShaftOrHousing"
    ) -> "_4571.AbstractShaftOrHousingModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.AbstractShaftOrHousingModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaftOrHousing)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ABSTRACT_SHAFT_OR_HOUSING](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_abstract_shaft_or_housing_load_case(
        self: Self, design_entity_analysis: "_6806.AbstractShaftOrHousingLoadCase"
    ) -> "_4571.AbstractShaftOrHousingModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.AbstractShaftOrHousingModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractShaftOrHousingLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _ABSTRACT_SHAFT_OR_HOUSING_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bearing(
        self: Self, design_entity: "_2437.Bearing"
    ) -> "_4577.BearingModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.BearingModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.Bearing)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BEARING](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bearing_load_case(
        self: Self, design_entity_analysis: "_6817.BearingLoadCase"
    ) -> "_4577.BearingModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.BearingModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BearingLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BEARING_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bolt(
        self: Self, design_entity: "_2440.Bolt"
    ) -> "_4589.BoltModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.BoltModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.Bolt)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BOLT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bolt_load_case(
        self: Self, design_entity_analysis: "_6829.BoltLoadCase"
    ) -> "_4589.BoltModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.BoltModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BoltLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BOLT_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bolted_joint(
        self: Self, design_entity: "_2441.BoltedJoint"
    ) -> "_4588.BoltedJointModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.BoltedJointModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.BoltedJoint)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BOLTED_JOINT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bolted_joint_load_case(
        self: Self, design_entity_analysis: "_6828.BoltedJointLoadCase"
    ) -> "_4588.BoltedJointModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.BoltedJointModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BoltedJointLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BOLTED_JOINT_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_component(
        self: Self, design_entity: "_2442.Component"
    ) -> "_4594.ComponentModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ComponentModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.Component)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_COMPONENT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_component_load_case(
        self: Self, design_entity_analysis: "_6835.ComponentLoadCase"
    ) -> "_4594.ComponentModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ComponentModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ComponentLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_COMPONENT_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_connector(
        self: Self, design_entity: "_2445.Connector"
    ) -> "_4605.ConnectorModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ConnectorModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.Connector)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONNECTOR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_connector_load_case(
        self: Self, design_entity_analysis: "_6848.ConnectorLoadCase"
    ) -> "_4605.ConnectorModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ConnectorModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConnectorLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONNECTOR_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_datum(
        self: Self, design_entity: "_2446.Datum"
    ) -> "_4621.DatumModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.DatumModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.Datum)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_DATUM](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_datum_load_case(
        self: Self, design_entity_analysis: "_6867.DatumLoadCase"
    ) -> "_4621.DatumModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.DatumModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.DatumLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_DATUM_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_external_cad_model(
        self: Self, design_entity: "_2450.ExternalCADModel"
    ) -> "_4625.ExternalCADModelModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ExternalCADModelModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.ExternalCADModel)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_EXTERNAL_CAD_MODEL](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_external_cad_model_load_case(
        self: Self, design_entity_analysis: "_6881.ExternalCADModelLoadCase"
    ) -> "_4625.ExternalCADModelModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ExternalCADModelModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ExternalCADModelLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _EXTERNAL_CAD_MODEL_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_fe_part(
        self: Self, design_entity: "_2451.FEPart"
    ) -> "_4629.FEPartModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.FEPartModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.FEPart)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_FE_PART](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_fe_part_load_case(
        self: Self, design_entity_analysis: "_6885.FEPartLoadCase"
    ) -> "_4629.FEPartModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.FEPartModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FEPartLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_FE_PART_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_flexible_pin_assembly(
        self: Self, design_entity: "_2452.FlexiblePinAssembly"
    ) -> "_4630.FlexiblePinAssemblyModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.FlexiblePinAssemblyModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.FlexiblePinAssembly)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_FLEXIBLE_PIN_ASSEMBLY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_flexible_pin_assembly_load_case(
        self: Self, design_entity_analysis: "_6886.FlexiblePinAssemblyLoadCase"
    ) -> "_4630.FlexiblePinAssemblyModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.FlexiblePinAssemblyModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FlexiblePinAssemblyLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _FLEXIBLE_PIN_ASSEMBLY_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_assembly(
        self: Self, design_entity: "_2431.Assembly"
    ) -> "_4576.AssemblyModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.AssemblyModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.Assembly)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ASSEMBLY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_assembly_load_case(
        self: Self, design_entity_analysis: "_6816.AssemblyLoadCase"
    ) -> "_4576.AssemblyModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.AssemblyModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AssemblyLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ASSEMBLY_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_guide_dxf_model(
        self: Self, design_entity: "_2453.GuideDxfModel"
    ) -> "_4635.GuideDxfModelModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.GuideDxfModelModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.GuideDxfModel)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_GUIDE_DXF_MODEL](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_guide_dxf_model_load_case(
        self: Self, design_entity_analysis: "_6894.GuideDxfModelLoadCase"
    ) -> "_4635.GuideDxfModelModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.GuideDxfModelModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GuideDxfModelLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_GUIDE_DXF_MODEL_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_mass_disc(
        self: Self, design_entity: "_2460.MassDisc"
    ) -> "_4649.MassDiscModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.MassDiscModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.MassDisc)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_MASS_DISC](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_mass_disc_load_case(
        self: Self, design_entity_analysis: "_6919.MassDiscLoadCase"
    ) -> "_4649.MassDiscModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.MassDiscModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MassDiscLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_MASS_DISC_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_measurement_component(
        self: Self, design_entity: "_2461.MeasurementComponent"
    ) -> "_4650.MeasurementComponentModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.MeasurementComponentModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.MeasurementComponent)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_MEASUREMENT_COMPONENT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_measurement_component_load_case(
        self: Self, design_entity_analysis: "_6920.MeasurementComponentLoadCase"
    ) -> "_4650.MeasurementComponentModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.MeasurementComponentModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MeasurementComponentLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _MEASUREMENT_COMPONENT_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_mountable_component(
        self: Self, design_entity: "_2462.MountableComponent"
    ) -> "_4655.MountableComponentModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.MountableComponentModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.MountableComponent)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_MOUNTABLE_COMPONENT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_mountable_component_load_case(
        self: Self, design_entity_analysis: "_6922.MountableComponentLoadCase"
    ) -> "_4655.MountableComponentModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.MountableComponentModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MountableComponentLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _MOUNTABLE_COMPONENT_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_oil_seal(
        self: Self, design_entity: "_2464.OilSeal"
    ) -> "_4657.OilSealModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.OilSealModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.OilSeal)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_OIL_SEAL](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_oil_seal_load_case(
        self: Self, design_entity_analysis: "_6924.OilSealLoadCase"
    ) -> "_4657.OilSealModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.OilSealModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.OilSealLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_OIL_SEAL_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_part(
        self: Self, design_entity: "_2466.Part"
    ) -> "_4659.PartModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.PartModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.Part)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_PART](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_part_load_case(
        self: Self, design_entity_analysis: "_6926.PartLoadCase"
    ) -> "_4659.PartModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.PartModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_PART_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_planet_carrier(
        self: Self, design_entity: "_2467.PlanetCarrier"
    ) -> "_4665.PlanetCarrierModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.PlanetCarrierModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.PlanetCarrier)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_PLANET_CARRIER](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_planet_carrier_load_case(
        self: Self, design_entity_analysis: "_6933.PlanetCarrierLoadCase"
    ) -> "_4665.PlanetCarrierModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.PlanetCarrierModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetCarrierLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_PLANET_CARRIER_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_point_load(
        self: Self, design_entity: "_2469.PointLoad"
    ) -> "_4666.PointLoadModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.PointLoadModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.PointLoad)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_POINT_LOAD](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_point_load_load_case(
        self: Self, design_entity_analysis: "_6936.PointLoadLoadCase"
    ) -> "_4666.PointLoadModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.PointLoadModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PointLoadLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_POINT_LOAD_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_power_load(
        self: Self, design_entity: "_2470.PowerLoad"
    ) -> "_4667.PowerLoadModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.PowerLoadModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.PowerLoad)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_POWER_LOAD](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_power_load_load_case(
        self: Self, design_entity_analysis: "_6937.PowerLoadLoadCase"
    ) -> "_4667.PowerLoadModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.PowerLoadModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PowerLoadLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_POWER_LOAD_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_root_assembly(
        self: Self, design_entity: "_2472.RootAssembly"
    ) -> "_4674.RootAssemblyModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.RootAssemblyModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.RootAssembly)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ROOT_ASSEMBLY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_root_assembly_load_case(
        self: Self, design_entity_analysis: "_6946.RootAssemblyLoadCase"
    ) -> "_4674.RootAssemblyModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.RootAssemblyModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RootAssemblyLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ROOT_ASSEMBLY_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_specialised_assembly(
        self: Self, design_entity: "_2474.SpecialisedAssembly"
    ) -> "_4679.SpecialisedAssemblyModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.SpecialisedAssemblyModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.SpecialisedAssembly)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SPECIALISED_ASSEMBLY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_specialised_assembly_load_case(
        self: Self, design_entity_analysis: "_6950.SpecialisedAssemblyLoadCase"
    ) -> "_4679.SpecialisedAssemblyModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.SpecialisedAssemblyModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpecialisedAssemblyLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _SPECIALISED_ASSEMBLY_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_unbalanced_mass(
        self: Self, design_entity: "_2475.UnbalancedMass"
    ) -> "_4702.UnbalancedMassModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.UnbalancedMassModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.UnbalancedMass)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_UNBALANCED_MASS](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_unbalanced_mass_load_case(
        self: Self, design_entity_analysis: "_6978.UnbalancedMassLoadCase"
    ) -> "_4702.UnbalancedMassModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.UnbalancedMassModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.UnbalancedMassLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_UNBALANCED_MASS_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_virtual_component(
        self: Self, design_entity: "_2477.VirtualComponent"
    ) -> "_4703.VirtualComponentModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.VirtualComponentModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.VirtualComponent)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_VIRTUAL_COMPONENT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_virtual_component_load_case(
        self: Self, design_entity_analysis: "_6979.VirtualComponentLoadCase"
    ) -> "_4703.VirtualComponentModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.VirtualComponentModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.VirtualComponentLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_VIRTUAL_COMPONENT_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_shaft(
        self: Self, design_entity: "_2480.Shaft"
    ) -> "_4676.ShaftModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ShaftModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.shaft_model.Shaft)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SHAFT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_shaft_load_case(
        self: Self, design_entity_analysis: "_6948.ShaftLoadCase"
    ) -> "_4676.ShaftModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ShaftModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SHAFT_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_gear(
        self: Self, design_entity: "_2519.ConceptGear"
    ) -> "_4599.ConceptGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ConceptGearModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_gear_load_case(
        self: Self, design_entity_analysis: "_6839.ConceptGearLoadCase"
    ) -> "_4599.ConceptGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ConceptGearModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_gear_set(
        self: Self, design_entity: "_2520.ConceptGearSet"
    ) -> "_4600.ConceptGearSetModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ConceptGearSetModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_gear_set_load_case(
        self: Self, design_entity_analysis: "_6841.ConceptGearSetLoadCase"
    ) -> "_4600.ConceptGearSetModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ConceptGearSetModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_SET_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_face_gear(
        self: Self, design_entity: "_2526.FaceGear"
    ) -> "_4627.FaceGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.FaceGearModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_FACE_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_face_gear_load_case(
        self: Self, design_entity_analysis: "_6882.FaceGearLoadCase"
    ) -> "_4627.FaceGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.FaceGearModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_FACE_GEAR_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_face_gear_set(
        self: Self, design_entity: "_2527.FaceGearSet"
    ) -> "_4628.FaceGearSetModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.FaceGearSetModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_FACE_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_face_gear_set_load_case(
        self: Self, design_entity_analysis: "_6884.FaceGearSetLoadCase"
    ) -> "_4628.FaceGearSetModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.FaceGearSetModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_FACE_GEAR_SET_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_agma_gleason_conical_gear(
        self: Self, design_entity: "_2511.AGMAGleasonConicalGear"
    ) -> "_4574.AGMAGleasonConicalGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.AGMAGleasonConicalGearModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_agma_gleason_conical_gear_load_case(
        self: Self, design_entity_analysis: "_6811.AGMAGleasonConicalGearLoadCase"
    ) -> "_4574.AGMAGleasonConicalGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.AGMAGleasonConicalGearModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _AGMA_GLEASON_CONICAL_GEAR_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_agma_gleason_conical_gear_set(
        self: Self, design_entity: "_2512.AGMAGleasonConicalGearSet"
    ) -> "_4575.AGMAGleasonConicalGearSetModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.AGMAGleasonConicalGearSetModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _AGMA_GLEASON_CONICAL_GEAR_SET
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_agma_gleason_conical_gear_set_load_case(
        self: Self, design_entity_analysis: "_6813.AGMAGleasonConicalGearSetLoadCase"
    ) -> "_4575.AGMAGleasonConicalGearSetModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.AGMAGleasonConicalGearSetModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _AGMA_GLEASON_CONICAL_GEAR_SET_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_differential_gear(
        self: Self, design_entity: "_2513.BevelDifferentialGear"
    ) -> "_4581.BevelDifferentialGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialGearModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_differential_gear_load_case(
        self: Self, design_entity_analysis: "_6820.BevelDifferentialGearLoadCase"
    ) -> "_4581.BevelDifferentialGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialGearModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _BEVEL_DIFFERENTIAL_GEAR_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_differential_gear_set(
        self: Self, design_entity: "_2514.BevelDifferentialGearSet"
    ) -> "_4582.BevelDifferentialGearSetModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialGearSetModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_differential_gear_set_load_case(
        self: Self, design_entity_analysis: "_6822.BevelDifferentialGearSetLoadCase"
    ) -> "_4582.BevelDifferentialGearSetModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialGearSetModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _BEVEL_DIFFERENTIAL_GEAR_SET_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_differential_planet_gear(
        self: Self, design_entity: "_2515.BevelDifferentialPlanetGear"
    ) -> "_4583.BevelDifferentialPlanetGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialPlanetGearModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _BEVEL_DIFFERENTIAL_PLANET_GEAR
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_differential_planet_gear_load_case(
        self: Self, design_entity_analysis: "_6823.BevelDifferentialPlanetGearLoadCase"
    ) -> "_4583.BevelDifferentialPlanetGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialPlanetGearModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialPlanetGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _BEVEL_DIFFERENTIAL_PLANET_GEAR_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_differential_sun_gear(
        self: Self, design_entity: "_2516.BevelDifferentialSunGear"
    ) -> "_4584.BevelDifferentialSunGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialSunGearModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialSunGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_SUN_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_differential_sun_gear_load_case(
        self: Self, design_entity_analysis: "_6824.BevelDifferentialSunGearLoadCase"
    ) -> "_4584.BevelDifferentialSunGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.BevelDifferentialSunGearModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialSunGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _BEVEL_DIFFERENTIAL_SUN_GEAR_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_gear(
        self: Self, design_entity: "_2517.BevelGear"
    ) -> "_4586.BevelGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.BevelGearModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_gear_load_case(
        self: Self, design_entity_analysis: "_6825.BevelGearLoadCase"
    ) -> "_4586.BevelGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.BevelGearModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_gear_set(
        self: Self, design_entity: "_2518.BevelGearSet"
    ) -> "_4587.BevelGearSetModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.BevelGearSetModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_gear_set_load_case(
        self: Self, design_entity_analysis: "_6827.BevelGearSetLoadCase"
    ) -> "_4587.BevelGearSetModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.BevelGearSetModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_SET_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_conical_gear(
        self: Self, design_entity: "_2521.ConicalGear"
    ) -> "_4602.ConicalGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ConicalGearModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_conical_gear_load_case(
        self: Self, design_entity_analysis: "_6842.ConicalGearLoadCase"
    ) -> "_4602.ConicalGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ConicalGearModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_conical_gear_set(
        self: Self, design_entity: "_2522.ConicalGearSet"
    ) -> "_4603.ConicalGearSetModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ConicalGearSetModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_conical_gear_set_load_case(
        self: Self, design_entity_analysis: "_6846.ConicalGearSetLoadCase"
    ) -> "_4603.ConicalGearSetModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ConicalGearSetModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_SET_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cylindrical_gear(
        self: Self, design_entity: "_2523.CylindricalGear"
    ) -> "_4618.CylindricalGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.CylindricalGearModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cylindrical_gear_load_case(
        self: Self, design_entity_analysis: "_6859.CylindricalGearLoadCase"
    ) -> "_4618.CylindricalGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.CylindricalGearModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cylindrical_gear_set(
        self: Self, design_entity: "_2524.CylindricalGearSet"
    ) -> "_4619.CylindricalGearSetModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.CylindricalGearSetModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cylindrical_gear_set_load_case(
        self: Self, design_entity_analysis: "_6863.CylindricalGearSetLoadCase"
    ) -> "_4619.CylindricalGearSetModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.CylindricalGearSetModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _CYLINDRICAL_GEAR_SET_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cylindrical_planet_gear(
        self: Self, design_entity: "_2525.CylindricalPlanetGear"
    ) -> "_4620.CylindricalPlanetGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.CylindricalPlanetGearModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalPlanetGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_PLANET_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cylindrical_planet_gear_load_case(
        self: Self, design_entity_analysis: "_6864.CylindricalPlanetGearLoadCase"
    ) -> "_4620.CylindricalPlanetGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.CylindricalPlanetGearModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalPlanetGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _CYLINDRICAL_PLANET_GEAR_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_gear(
        self: Self, design_entity: "_2528.Gear"
    ) -> "_4633.GearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.GearModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.Gear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_gear_load_case(
        self: Self, design_entity_analysis: "_6888.GearLoadCase"
    ) -> "_4633.GearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.GearModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_GEAR_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_gear_set(
        self: Self, design_entity: "_2530.GearSet"
    ) -> "_4634.GearSetModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.GearSetModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.GearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_gear_set_load_case(
        self: Self, design_entity_analysis: "_6893.GearSetLoadCase"
    ) -> "_4634.GearSetModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.GearSetModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_GEAR_SET_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_hypoid_gear(
        self: Self, design_entity: "_2532.HypoidGear"
    ) -> "_4637.HypoidGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.HypoidGearModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_hypoid_gear_load_case(
        self: Self, design_entity_analysis: "_6903.HypoidGearLoadCase"
    ) -> "_4637.HypoidGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.HypoidGearModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_hypoid_gear_set(
        self: Self, design_entity: "_2533.HypoidGearSet"
    ) -> "_4638.HypoidGearSetModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.HypoidGearSetModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_hypoid_gear_set_load_case(
        self: Self, design_entity_analysis: "_6905.HypoidGearSetLoadCase"
    ) -> "_4638.HypoidGearSetModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.HypoidGearSetModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_SET_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_conical_gear(
        self: Self, design_entity: "_2534.KlingelnbergCycloPalloidConicalGear"
    ) -> "_4641.KlingelnbergCycloPalloidConicalGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidConicalGearModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_conical_gear_load_case(
        self: Self,
        design_entity_analysis: "_6910.KlingelnbergCycloPalloidConicalGearLoadCase",
    ) -> "_4641.KlingelnbergCycloPalloidConicalGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidConicalGearModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_conical_gear_set(
        self: Self, design_entity: "_2535.KlingelnbergCycloPalloidConicalGearSet"
    ) -> "_4642.KlingelnbergCycloPalloidConicalGearSetModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidConicalGearSetModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_conical_gear_set_load_case(
        self: Self,
        design_entity_analysis: "_6912.KlingelnbergCycloPalloidConicalGearSetLoadCase",
    ) -> "_4642.KlingelnbergCycloPalloidConicalGearSetModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidConicalGearSetModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_hypoid_gear(
        self: Self, design_entity: "_2536.KlingelnbergCycloPalloidHypoidGear"
    ) -> "_4644.KlingelnbergCycloPalloidHypoidGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidHypoidGearModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_load_case(
        self: Self,
        design_entity_analysis: "_6913.KlingelnbergCycloPalloidHypoidGearLoadCase",
    ) -> "_4644.KlingelnbergCycloPalloidHypoidGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidHypoidGearModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set(
        self: Self, design_entity: "_2537.KlingelnbergCycloPalloidHypoidGearSet"
    ) -> "_4645.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(
        self: Self,
        design_entity_analysis: "_6915.KlingelnbergCycloPalloidHypoidGearSetLoadCase",
    ) -> "_4645.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear(
        self: Self, design_entity: "_2538.KlingelnbergCycloPalloidSpiralBevelGear"
    ) -> "_4647.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(
        self: Self,
        design_entity_analysis: "_6916.KlingelnbergCycloPalloidSpiralBevelGearLoadCase",
    ) -> "_4647.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(
        self: Self, design_entity: "_2539.KlingelnbergCycloPalloidSpiralBevelGearSet"
    ) -> "_4648.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(
        self: Self,
        design_entity_analysis: "_6918.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
    ) -> "_4648.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_planetary_gear_set(
        self: Self, design_entity: "_2540.PlanetaryGearSet"
    ) -> "_4664.PlanetaryGearSetModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.PlanetaryGearSetModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.PlanetaryGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_PLANETARY_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_planetary_gear_set_load_case(
        self: Self, design_entity_analysis: "_6931.PlanetaryGearSetLoadCase"
    ) -> "_4664.PlanetaryGearSetModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.PlanetaryGearSetModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetaryGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _PLANETARY_GEAR_SET_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spiral_bevel_gear(
        self: Self, design_entity: "_2541.SpiralBevelGear"
    ) -> "_4681.SpiralBevelGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.SpiralBevelGearModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spiral_bevel_gear_load_case(
        self: Self, design_entity_analysis: "_6951.SpiralBevelGearLoadCase"
    ) -> "_4681.SpiralBevelGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.SpiralBevelGearModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spiral_bevel_gear_set(
        self: Self, design_entity: "_2542.SpiralBevelGearSet"
    ) -> "_4682.SpiralBevelGearSetModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.SpiralBevelGearSetModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spiral_bevel_gear_set_load_case(
        self: Self, design_entity_analysis: "_6953.SpiralBevelGearSetLoadCase"
    ) -> "_4682.SpiralBevelGearSetModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.SpiralBevelGearSetModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _SPIRAL_BEVEL_GEAR_SET_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_diff_gear(
        self: Self, design_entity: "_2543.StraightBevelDiffGear"
    ) -> "_4687.StraightBevelDiffGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelDiffGearModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_diff_gear_load_case(
        self: Self, design_entity_analysis: "_6957.StraightBevelDiffGearLoadCase"
    ) -> "_4687.StraightBevelDiffGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelDiffGearModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _STRAIGHT_BEVEL_DIFF_GEAR_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_diff_gear_set(
        self: Self, design_entity: "_2544.StraightBevelDiffGearSet"
    ) -> "_4688.StraightBevelDiffGearSetModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelDiffGearSetModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _STRAIGHT_BEVEL_DIFF_GEAR_SET
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_diff_gear_set_load_case(
        self: Self, design_entity_analysis: "_6959.StraightBevelDiffGearSetLoadCase"
    ) -> "_4688.StraightBevelDiffGearSetModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelDiffGearSetModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _STRAIGHT_BEVEL_DIFF_GEAR_SET_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_gear(
        self: Self, design_entity: "_2545.StraightBevelGear"
    ) -> "_4690.StraightBevelGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelGearModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_gear_load_case(
        self: Self, design_entity_analysis: "_6960.StraightBevelGearLoadCase"
    ) -> "_4690.StraightBevelGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelGearModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _STRAIGHT_BEVEL_GEAR_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_gear_set(
        self: Self, design_entity: "_2546.StraightBevelGearSet"
    ) -> "_4691.StraightBevelGearSetModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelGearSetModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_gear_set_load_case(
        self: Self, design_entity_analysis: "_6962.StraightBevelGearSetLoadCase"
    ) -> "_4691.StraightBevelGearSetModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelGearSetModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _STRAIGHT_BEVEL_GEAR_SET_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_planet_gear(
        self: Self, design_entity: "_2547.StraightBevelPlanetGear"
    ) -> "_4692.StraightBevelPlanetGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelPlanetGearModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelPlanetGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_PLANET_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_planet_gear_load_case(
        self: Self, design_entity_analysis: "_6963.StraightBevelPlanetGearLoadCase"
    ) -> "_4692.StraightBevelPlanetGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelPlanetGearModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelPlanetGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _STRAIGHT_BEVEL_PLANET_GEAR_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_sun_gear(
        self: Self, design_entity: "_2548.StraightBevelSunGear"
    ) -> "_4693.StraightBevelSunGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelSunGearModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelSunGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_SUN_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_sun_gear_load_case(
        self: Self, design_entity_analysis: "_6964.StraightBevelSunGearLoadCase"
    ) -> "_4693.StraightBevelSunGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelSunGearModalAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelSunGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _STRAIGHT_BEVEL_SUN_GEAR_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_worm_gear(
        self: Self, design_entity: "_2549.WormGear"
    ) -> "_4708.WormGearModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.WormGearModalAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_WORM_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "ModalAnalysis._Cast_ModalAnalysis":
        return self._Cast_ModalAnalysis(self)
