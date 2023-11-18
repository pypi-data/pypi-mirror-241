"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4030 import AbstractAssemblyPowerFlow
    from ._4031 import AbstractShaftOrHousingPowerFlow
    from ._4032 import AbstractShaftPowerFlow
    from ._4033 import AbstractShaftToMountableComponentConnectionPowerFlow
    from ._4034 import AGMAGleasonConicalGearMeshPowerFlow
    from ._4035 import AGMAGleasonConicalGearPowerFlow
    from ._4036 import AGMAGleasonConicalGearSetPowerFlow
    from ._4037 import AssemblyPowerFlow
    from ._4038 import BearingPowerFlow
    from ._4039 import BeltConnectionPowerFlow
    from ._4040 import BeltDrivePowerFlow
    from ._4041 import BevelDifferentialGearMeshPowerFlow
    from ._4042 import BevelDifferentialGearPowerFlow
    from ._4043 import BevelDifferentialGearSetPowerFlow
    from ._4044 import BevelDifferentialPlanetGearPowerFlow
    from ._4045 import BevelDifferentialSunGearPowerFlow
    from ._4046 import BevelGearMeshPowerFlow
    from ._4047 import BevelGearPowerFlow
    from ._4048 import BevelGearSetPowerFlow
    from ._4049 import BoltedJointPowerFlow
    from ._4050 import BoltPowerFlow
    from ._4051 import ClutchConnectionPowerFlow
    from ._4052 import ClutchHalfPowerFlow
    from ._4053 import ClutchPowerFlow
    from ._4054 import CoaxialConnectionPowerFlow
    from ._4055 import ComponentPowerFlow
    from ._4056 import ConceptCouplingConnectionPowerFlow
    from ._4057 import ConceptCouplingHalfPowerFlow
    from ._4058 import ConceptCouplingPowerFlow
    from ._4059 import ConceptGearMeshPowerFlow
    from ._4060 import ConceptGearPowerFlow
    from ._4061 import ConceptGearSetPowerFlow
    from ._4062 import ConicalGearMeshPowerFlow
    from ._4063 import ConicalGearPowerFlow
    from ._4064 import ConicalGearSetPowerFlow
    from ._4065 import ConnectionPowerFlow
    from ._4066 import ConnectorPowerFlow
    from ._4067 import CouplingConnectionPowerFlow
    from ._4068 import CouplingHalfPowerFlow
    from ._4069 import CouplingPowerFlow
    from ._4070 import CVTBeltConnectionPowerFlow
    from ._4071 import CVTPowerFlow
    from ._4072 import CVTPulleyPowerFlow
    from ._4073 import CycloidalAssemblyPowerFlow
    from ._4074 import CycloidalDiscCentralBearingConnectionPowerFlow
    from ._4075 import CycloidalDiscPlanetaryBearingConnectionPowerFlow
    from ._4076 import CycloidalDiscPowerFlow
    from ._4077 import CylindricalGearGeometricEntityDrawStyle
    from ._4078 import CylindricalGearMeshPowerFlow
    from ._4079 import CylindricalGearPowerFlow
    from ._4080 import CylindricalGearSetPowerFlow
    from ._4081 import CylindricalPlanetGearPowerFlow
    from ._4082 import DatumPowerFlow
    from ._4083 import ExternalCADModelPowerFlow
    from ._4084 import FaceGearMeshPowerFlow
    from ._4085 import FaceGearPowerFlow
    from ._4086 import FaceGearSetPowerFlow
    from ._4087 import FastPowerFlowSolution
    from ._4088 import FEPartPowerFlow
    from ._4089 import FlexiblePinAssemblyPowerFlow
    from ._4090 import GearMeshPowerFlow
    from ._4091 import GearPowerFlow
    from ._4092 import GearSetPowerFlow
    from ._4093 import GuideDxfModelPowerFlow
    from ._4094 import HypoidGearMeshPowerFlow
    from ._4095 import HypoidGearPowerFlow
    from ._4096 import HypoidGearSetPowerFlow
    from ._4097 import InterMountableComponentConnectionPowerFlow
    from ._4098 import KlingelnbergCycloPalloidConicalGearMeshPowerFlow
    from ._4099 import KlingelnbergCycloPalloidConicalGearPowerFlow
    from ._4100 import KlingelnbergCycloPalloidConicalGearSetPowerFlow
    from ._4101 import KlingelnbergCycloPalloidHypoidGearMeshPowerFlow
    from ._4102 import KlingelnbergCycloPalloidHypoidGearPowerFlow
    from ._4103 import KlingelnbergCycloPalloidHypoidGearSetPowerFlow
    from ._4104 import KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow
    from ._4105 import KlingelnbergCycloPalloidSpiralBevelGearPowerFlow
    from ._4106 import KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow
    from ._4107 import MassDiscPowerFlow
    from ._4108 import MeasurementComponentPowerFlow
    from ._4109 import MountableComponentPowerFlow
    from ._4110 import OilSealPowerFlow
    from ._4111 import PartPowerFlow
    from ._4112 import PartToPartShearCouplingConnectionPowerFlow
    from ._4113 import PartToPartShearCouplingHalfPowerFlow
    from ._4114 import PartToPartShearCouplingPowerFlow
    from ._4115 import PlanetaryConnectionPowerFlow
    from ._4116 import PlanetaryGearSetPowerFlow
    from ._4117 import PlanetCarrierPowerFlow
    from ._4118 import PointLoadPowerFlow
    from ._4119 import PowerFlow
    from ._4120 import PowerFlowDrawStyle
    from ._4121 import PowerLoadPowerFlow
    from ._4122 import PulleyPowerFlow
    from ._4123 import RingPinsPowerFlow
    from ._4124 import RingPinsToDiscConnectionPowerFlow
    from ._4125 import RollingRingAssemblyPowerFlow
    from ._4126 import RollingRingConnectionPowerFlow
    from ._4127 import RollingRingPowerFlow
    from ._4128 import RootAssemblyPowerFlow
    from ._4129 import ShaftHubConnectionPowerFlow
    from ._4130 import ShaftPowerFlow
    from ._4131 import ShaftToMountableComponentConnectionPowerFlow
    from ._4132 import SpecialisedAssemblyPowerFlow
    from ._4133 import SpiralBevelGearMeshPowerFlow
    from ._4134 import SpiralBevelGearPowerFlow
    from ._4135 import SpiralBevelGearSetPowerFlow
    from ._4136 import SpringDamperConnectionPowerFlow
    from ._4137 import SpringDamperHalfPowerFlow
    from ._4138 import SpringDamperPowerFlow
    from ._4139 import StraightBevelDiffGearMeshPowerFlow
    from ._4140 import StraightBevelDiffGearPowerFlow
    from ._4141 import StraightBevelDiffGearSetPowerFlow
    from ._4142 import StraightBevelGearMeshPowerFlow
    from ._4143 import StraightBevelGearPowerFlow
    from ._4144 import StraightBevelGearSetPowerFlow
    from ._4145 import StraightBevelPlanetGearPowerFlow
    from ._4146 import StraightBevelSunGearPowerFlow
    from ._4147 import SynchroniserHalfPowerFlow
    from ._4148 import SynchroniserPartPowerFlow
    from ._4149 import SynchroniserPowerFlow
    from ._4150 import SynchroniserSleevePowerFlow
    from ._4151 import ToothPassingHarmonic
    from ._4152 import TorqueConverterConnectionPowerFlow
    from ._4153 import TorqueConverterPowerFlow
    from ._4154 import TorqueConverterPumpPowerFlow
    from ._4155 import TorqueConverterTurbinePowerFlow
    from ._4156 import UnbalancedMassPowerFlow
    from ._4157 import VirtualComponentPowerFlow
    from ._4158 import WormGearMeshPowerFlow
    from ._4159 import WormGearPowerFlow
    from ._4160 import WormGearSetPowerFlow
    from ._4161 import ZerolBevelGearMeshPowerFlow
    from ._4162 import ZerolBevelGearPowerFlow
    from ._4163 import ZerolBevelGearSetPowerFlow
else:
    import_structure = {
        "_4030": ["AbstractAssemblyPowerFlow"],
        "_4031": ["AbstractShaftOrHousingPowerFlow"],
        "_4032": ["AbstractShaftPowerFlow"],
        "_4033": ["AbstractShaftToMountableComponentConnectionPowerFlow"],
        "_4034": ["AGMAGleasonConicalGearMeshPowerFlow"],
        "_4035": ["AGMAGleasonConicalGearPowerFlow"],
        "_4036": ["AGMAGleasonConicalGearSetPowerFlow"],
        "_4037": ["AssemblyPowerFlow"],
        "_4038": ["BearingPowerFlow"],
        "_4039": ["BeltConnectionPowerFlow"],
        "_4040": ["BeltDrivePowerFlow"],
        "_4041": ["BevelDifferentialGearMeshPowerFlow"],
        "_4042": ["BevelDifferentialGearPowerFlow"],
        "_4043": ["BevelDifferentialGearSetPowerFlow"],
        "_4044": ["BevelDifferentialPlanetGearPowerFlow"],
        "_4045": ["BevelDifferentialSunGearPowerFlow"],
        "_4046": ["BevelGearMeshPowerFlow"],
        "_4047": ["BevelGearPowerFlow"],
        "_4048": ["BevelGearSetPowerFlow"],
        "_4049": ["BoltedJointPowerFlow"],
        "_4050": ["BoltPowerFlow"],
        "_4051": ["ClutchConnectionPowerFlow"],
        "_4052": ["ClutchHalfPowerFlow"],
        "_4053": ["ClutchPowerFlow"],
        "_4054": ["CoaxialConnectionPowerFlow"],
        "_4055": ["ComponentPowerFlow"],
        "_4056": ["ConceptCouplingConnectionPowerFlow"],
        "_4057": ["ConceptCouplingHalfPowerFlow"],
        "_4058": ["ConceptCouplingPowerFlow"],
        "_4059": ["ConceptGearMeshPowerFlow"],
        "_4060": ["ConceptGearPowerFlow"],
        "_4061": ["ConceptGearSetPowerFlow"],
        "_4062": ["ConicalGearMeshPowerFlow"],
        "_4063": ["ConicalGearPowerFlow"],
        "_4064": ["ConicalGearSetPowerFlow"],
        "_4065": ["ConnectionPowerFlow"],
        "_4066": ["ConnectorPowerFlow"],
        "_4067": ["CouplingConnectionPowerFlow"],
        "_4068": ["CouplingHalfPowerFlow"],
        "_4069": ["CouplingPowerFlow"],
        "_4070": ["CVTBeltConnectionPowerFlow"],
        "_4071": ["CVTPowerFlow"],
        "_4072": ["CVTPulleyPowerFlow"],
        "_4073": ["CycloidalAssemblyPowerFlow"],
        "_4074": ["CycloidalDiscCentralBearingConnectionPowerFlow"],
        "_4075": ["CycloidalDiscPlanetaryBearingConnectionPowerFlow"],
        "_4076": ["CycloidalDiscPowerFlow"],
        "_4077": ["CylindricalGearGeometricEntityDrawStyle"],
        "_4078": ["CylindricalGearMeshPowerFlow"],
        "_4079": ["CylindricalGearPowerFlow"],
        "_4080": ["CylindricalGearSetPowerFlow"],
        "_4081": ["CylindricalPlanetGearPowerFlow"],
        "_4082": ["DatumPowerFlow"],
        "_4083": ["ExternalCADModelPowerFlow"],
        "_4084": ["FaceGearMeshPowerFlow"],
        "_4085": ["FaceGearPowerFlow"],
        "_4086": ["FaceGearSetPowerFlow"],
        "_4087": ["FastPowerFlowSolution"],
        "_4088": ["FEPartPowerFlow"],
        "_4089": ["FlexiblePinAssemblyPowerFlow"],
        "_4090": ["GearMeshPowerFlow"],
        "_4091": ["GearPowerFlow"],
        "_4092": ["GearSetPowerFlow"],
        "_4093": ["GuideDxfModelPowerFlow"],
        "_4094": ["HypoidGearMeshPowerFlow"],
        "_4095": ["HypoidGearPowerFlow"],
        "_4096": ["HypoidGearSetPowerFlow"],
        "_4097": ["InterMountableComponentConnectionPowerFlow"],
        "_4098": ["KlingelnbergCycloPalloidConicalGearMeshPowerFlow"],
        "_4099": ["KlingelnbergCycloPalloidConicalGearPowerFlow"],
        "_4100": ["KlingelnbergCycloPalloidConicalGearSetPowerFlow"],
        "_4101": ["KlingelnbergCycloPalloidHypoidGearMeshPowerFlow"],
        "_4102": ["KlingelnbergCycloPalloidHypoidGearPowerFlow"],
        "_4103": ["KlingelnbergCycloPalloidHypoidGearSetPowerFlow"],
        "_4104": ["KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow"],
        "_4105": ["KlingelnbergCycloPalloidSpiralBevelGearPowerFlow"],
        "_4106": ["KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow"],
        "_4107": ["MassDiscPowerFlow"],
        "_4108": ["MeasurementComponentPowerFlow"],
        "_4109": ["MountableComponentPowerFlow"],
        "_4110": ["OilSealPowerFlow"],
        "_4111": ["PartPowerFlow"],
        "_4112": ["PartToPartShearCouplingConnectionPowerFlow"],
        "_4113": ["PartToPartShearCouplingHalfPowerFlow"],
        "_4114": ["PartToPartShearCouplingPowerFlow"],
        "_4115": ["PlanetaryConnectionPowerFlow"],
        "_4116": ["PlanetaryGearSetPowerFlow"],
        "_4117": ["PlanetCarrierPowerFlow"],
        "_4118": ["PointLoadPowerFlow"],
        "_4119": ["PowerFlow"],
        "_4120": ["PowerFlowDrawStyle"],
        "_4121": ["PowerLoadPowerFlow"],
        "_4122": ["PulleyPowerFlow"],
        "_4123": ["RingPinsPowerFlow"],
        "_4124": ["RingPinsToDiscConnectionPowerFlow"],
        "_4125": ["RollingRingAssemblyPowerFlow"],
        "_4126": ["RollingRingConnectionPowerFlow"],
        "_4127": ["RollingRingPowerFlow"],
        "_4128": ["RootAssemblyPowerFlow"],
        "_4129": ["ShaftHubConnectionPowerFlow"],
        "_4130": ["ShaftPowerFlow"],
        "_4131": ["ShaftToMountableComponentConnectionPowerFlow"],
        "_4132": ["SpecialisedAssemblyPowerFlow"],
        "_4133": ["SpiralBevelGearMeshPowerFlow"],
        "_4134": ["SpiralBevelGearPowerFlow"],
        "_4135": ["SpiralBevelGearSetPowerFlow"],
        "_4136": ["SpringDamperConnectionPowerFlow"],
        "_4137": ["SpringDamperHalfPowerFlow"],
        "_4138": ["SpringDamperPowerFlow"],
        "_4139": ["StraightBevelDiffGearMeshPowerFlow"],
        "_4140": ["StraightBevelDiffGearPowerFlow"],
        "_4141": ["StraightBevelDiffGearSetPowerFlow"],
        "_4142": ["StraightBevelGearMeshPowerFlow"],
        "_4143": ["StraightBevelGearPowerFlow"],
        "_4144": ["StraightBevelGearSetPowerFlow"],
        "_4145": ["StraightBevelPlanetGearPowerFlow"],
        "_4146": ["StraightBevelSunGearPowerFlow"],
        "_4147": ["SynchroniserHalfPowerFlow"],
        "_4148": ["SynchroniserPartPowerFlow"],
        "_4149": ["SynchroniserPowerFlow"],
        "_4150": ["SynchroniserSleevePowerFlow"],
        "_4151": ["ToothPassingHarmonic"],
        "_4152": ["TorqueConverterConnectionPowerFlow"],
        "_4153": ["TorqueConverterPowerFlow"],
        "_4154": ["TorqueConverterPumpPowerFlow"],
        "_4155": ["TorqueConverterTurbinePowerFlow"],
        "_4156": ["UnbalancedMassPowerFlow"],
        "_4157": ["VirtualComponentPowerFlow"],
        "_4158": ["WormGearMeshPowerFlow"],
        "_4159": ["WormGearPowerFlow"],
        "_4160": ["WormGearSetPowerFlow"],
        "_4161": ["ZerolBevelGearMeshPowerFlow"],
        "_4162": ["ZerolBevelGearPowerFlow"],
        "_4163": ["ZerolBevelGearSetPowerFlow"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyPowerFlow",
    "AbstractShaftOrHousingPowerFlow",
    "AbstractShaftPowerFlow",
    "AbstractShaftToMountableComponentConnectionPowerFlow",
    "AGMAGleasonConicalGearMeshPowerFlow",
    "AGMAGleasonConicalGearPowerFlow",
    "AGMAGleasonConicalGearSetPowerFlow",
    "AssemblyPowerFlow",
    "BearingPowerFlow",
    "BeltConnectionPowerFlow",
    "BeltDrivePowerFlow",
    "BevelDifferentialGearMeshPowerFlow",
    "BevelDifferentialGearPowerFlow",
    "BevelDifferentialGearSetPowerFlow",
    "BevelDifferentialPlanetGearPowerFlow",
    "BevelDifferentialSunGearPowerFlow",
    "BevelGearMeshPowerFlow",
    "BevelGearPowerFlow",
    "BevelGearSetPowerFlow",
    "BoltedJointPowerFlow",
    "BoltPowerFlow",
    "ClutchConnectionPowerFlow",
    "ClutchHalfPowerFlow",
    "ClutchPowerFlow",
    "CoaxialConnectionPowerFlow",
    "ComponentPowerFlow",
    "ConceptCouplingConnectionPowerFlow",
    "ConceptCouplingHalfPowerFlow",
    "ConceptCouplingPowerFlow",
    "ConceptGearMeshPowerFlow",
    "ConceptGearPowerFlow",
    "ConceptGearSetPowerFlow",
    "ConicalGearMeshPowerFlow",
    "ConicalGearPowerFlow",
    "ConicalGearSetPowerFlow",
    "ConnectionPowerFlow",
    "ConnectorPowerFlow",
    "CouplingConnectionPowerFlow",
    "CouplingHalfPowerFlow",
    "CouplingPowerFlow",
    "CVTBeltConnectionPowerFlow",
    "CVTPowerFlow",
    "CVTPulleyPowerFlow",
    "CycloidalAssemblyPowerFlow",
    "CycloidalDiscCentralBearingConnectionPowerFlow",
    "CycloidalDiscPlanetaryBearingConnectionPowerFlow",
    "CycloidalDiscPowerFlow",
    "CylindricalGearGeometricEntityDrawStyle",
    "CylindricalGearMeshPowerFlow",
    "CylindricalGearPowerFlow",
    "CylindricalGearSetPowerFlow",
    "CylindricalPlanetGearPowerFlow",
    "DatumPowerFlow",
    "ExternalCADModelPowerFlow",
    "FaceGearMeshPowerFlow",
    "FaceGearPowerFlow",
    "FaceGearSetPowerFlow",
    "FastPowerFlowSolution",
    "FEPartPowerFlow",
    "FlexiblePinAssemblyPowerFlow",
    "GearMeshPowerFlow",
    "GearPowerFlow",
    "GearSetPowerFlow",
    "GuideDxfModelPowerFlow",
    "HypoidGearMeshPowerFlow",
    "HypoidGearPowerFlow",
    "HypoidGearSetPowerFlow",
    "InterMountableComponentConnectionPowerFlow",
    "KlingelnbergCycloPalloidConicalGearMeshPowerFlow",
    "KlingelnbergCycloPalloidConicalGearPowerFlow",
    "KlingelnbergCycloPalloidConicalGearSetPowerFlow",
    "KlingelnbergCycloPalloidHypoidGearMeshPowerFlow",
    "KlingelnbergCycloPalloidHypoidGearPowerFlow",
    "KlingelnbergCycloPalloidHypoidGearSetPowerFlow",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow",
    "KlingelnbergCycloPalloidSpiralBevelGearPowerFlow",
    "KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow",
    "MassDiscPowerFlow",
    "MeasurementComponentPowerFlow",
    "MountableComponentPowerFlow",
    "OilSealPowerFlow",
    "PartPowerFlow",
    "PartToPartShearCouplingConnectionPowerFlow",
    "PartToPartShearCouplingHalfPowerFlow",
    "PartToPartShearCouplingPowerFlow",
    "PlanetaryConnectionPowerFlow",
    "PlanetaryGearSetPowerFlow",
    "PlanetCarrierPowerFlow",
    "PointLoadPowerFlow",
    "PowerFlow",
    "PowerFlowDrawStyle",
    "PowerLoadPowerFlow",
    "PulleyPowerFlow",
    "RingPinsPowerFlow",
    "RingPinsToDiscConnectionPowerFlow",
    "RollingRingAssemblyPowerFlow",
    "RollingRingConnectionPowerFlow",
    "RollingRingPowerFlow",
    "RootAssemblyPowerFlow",
    "ShaftHubConnectionPowerFlow",
    "ShaftPowerFlow",
    "ShaftToMountableComponentConnectionPowerFlow",
    "SpecialisedAssemblyPowerFlow",
    "SpiralBevelGearMeshPowerFlow",
    "SpiralBevelGearPowerFlow",
    "SpiralBevelGearSetPowerFlow",
    "SpringDamperConnectionPowerFlow",
    "SpringDamperHalfPowerFlow",
    "SpringDamperPowerFlow",
    "StraightBevelDiffGearMeshPowerFlow",
    "StraightBevelDiffGearPowerFlow",
    "StraightBevelDiffGearSetPowerFlow",
    "StraightBevelGearMeshPowerFlow",
    "StraightBevelGearPowerFlow",
    "StraightBevelGearSetPowerFlow",
    "StraightBevelPlanetGearPowerFlow",
    "StraightBevelSunGearPowerFlow",
    "SynchroniserHalfPowerFlow",
    "SynchroniserPartPowerFlow",
    "SynchroniserPowerFlow",
    "SynchroniserSleevePowerFlow",
    "ToothPassingHarmonic",
    "TorqueConverterConnectionPowerFlow",
    "TorqueConverterPowerFlow",
    "TorqueConverterPumpPowerFlow",
    "TorqueConverterTurbinePowerFlow",
    "UnbalancedMassPowerFlow",
    "VirtualComponentPowerFlow",
    "WormGearMeshPowerFlow",
    "WormGearPowerFlow",
    "WormGearSetPowerFlow",
    "ZerolBevelGearMeshPowerFlow",
    "ZerolBevelGearPowerFlow",
    "ZerolBevelGearSetPowerFlow",
)
