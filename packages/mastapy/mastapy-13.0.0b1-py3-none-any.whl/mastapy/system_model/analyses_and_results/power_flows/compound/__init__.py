"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4164 import AbstractAssemblyCompoundPowerFlow
    from ._4165 import AbstractShaftCompoundPowerFlow
    from ._4166 import AbstractShaftOrHousingCompoundPowerFlow
    from ._4167 import AbstractShaftToMountableComponentConnectionCompoundPowerFlow
    from ._4168 import AGMAGleasonConicalGearCompoundPowerFlow
    from ._4169 import AGMAGleasonConicalGearMeshCompoundPowerFlow
    from ._4170 import AGMAGleasonConicalGearSetCompoundPowerFlow
    from ._4171 import AssemblyCompoundPowerFlow
    from ._4172 import BearingCompoundPowerFlow
    from ._4173 import BeltConnectionCompoundPowerFlow
    from ._4174 import BeltDriveCompoundPowerFlow
    from ._4175 import BevelDifferentialGearCompoundPowerFlow
    from ._4176 import BevelDifferentialGearMeshCompoundPowerFlow
    from ._4177 import BevelDifferentialGearSetCompoundPowerFlow
    from ._4178 import BevelDifferentialPlanetGearCompoundPowerFlow
    from ._4179 import BevelDifferentialSunGearCompoundPowerFlow
    from ._4180 import BevelGearCompoundPowerFlow
    from ._4181 import BevelGearMeshCompoundPowerFlow
    from ._4182 import BevelGearSetCompoundPowerFlow
    from ._4183 import BoltCompoundPowerFlow
    from ._4184 import BoltedJointCompoundPowerFlow
    from ._4185 import ClutchCompoundPowerFlow
    from ._4186 import ClutchConnectionCompoundPowerFlow
    from ._4187 import ClutchHalfCompoundPowerFlow
    from ._4188 import CoaxialConnectionCompoundPowerFlow
    from ._4189 import ComponentCompoundPowerFlow
    from ._4190 import ConceptCouplingCompoundPowerFlow
    from ._4191 import ConceptCouplingConnectionCompoundPowerFlow
    from ._4192 import ConceptCouplingHalfCompoundPowerFlow
    from ._4193 import ConceptGearCompoundPowerFlow
    from ._4194 import ConceptGearMeshCompoundPowerFlow
    from ._4195 import ConceptGearSetCompoundPowerFlow
    from ._4196 import ConicalGearCompoundPowerFlow
    from ._4197 import ConicalGearMeshCompoundPowerFlow
    from ._4198 import ConicalGearSetCompoundPowerFlow
    from ._4199 import ConnectionCompoundPowerFlow
    from ._4200 import ConnectorCompoundPowerFlow
    from ._4201 import CouplingCompoundPowerFlow
    from ._4202 import CouplingConnectionCompoundPowerFlow
    from ._4203 import CouplingHalfCompoundPowerFlow
    from ._4204 import CVTBeltConnectionCompoundPowerFlow
    from ._4205 import CVTCompoundPowerFlow
    from ._4206 import CVTPulleyCompoundPowerFlow
    from ._4207 import CycloidalAssemblyCompoundPowerFlow
    from ._4208 import CycloidalDiscCentralBearingConnectionCompoundPowerFlow
    from ._4209 import CycloidalDiscCompoundPowerFlow
    from ._4210 import CycloidalDiscPlanetaryBearingConnectionCompoundPowerFlow
    from ._4211 import CylindricalGearCompoundPowerFlow
    from ._4212 import CylindricalGearMeshCompoundPowerFlow
    from ._4213 import CylindricalGearSetCompoundPowerFlow
    from ._4214 import CylindricalPlanetGearCompoundPowerFlow
    from ._4215 import DatumCompoundPowerFlow
    from ._4216 import ExternalCADModelCompoundPowerFlow
    from ._4217 import FaceGearCompoundPowerFlow
    from ._4218 import FaceGearMeshCompoundPowerFlow
    from ._4219 import FaceGearSetCompoundPowerFlow
    from ._4220 import FEPartCompoundPowerFlow
    from ._4221 import FlexiblePinAssemblyCompoundPowerFlow
    from ._4222 import GearCompoundPowerFlow
    from ._4223 import GearMeshCompoundPowerFlow
    from ._4224 import GearSetCompoundPowerFlow
    from ._4225 import GuideDxfModelCompoundPowerFlow
    from ._4226 import HypoidGearCompoundPowerFlow
    from ._4227 import HypoidGearMeshCompoundPowerFlow
    from ._4228 import HypoidGearSetCompoundPowerFlow
    from ._4229 import InterMountableComponentConnectionCompoundPowerFlow
    from ._4230 import KlingelnbergCycloPalloidConicalGearCompoundPowerFlow
    from ._4231 import KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow
    from ._4232 import KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow
    from ._4233 import KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow
    from ._4234 import KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow
    from ._4235 import KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow
    from ._4236 import KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow
    from ._4237 import KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow
    from ._4238 import KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow
    from ._4239 import MassDiscCompoundPowerFlow
    from ._4240 import MeasurementComponentCompoundPowerFlow
    from ._4241 import MountableComponentCompoundPowerFlow
    from ._4242 import OilSealCompoundPowerFlow
    from ._4243 import PartCompoundPowerFlow
    from ._4244 import PartToPartShearCouplingCompoundPowerFlow
    from ._4245 import PartToPartShearCouplingConnectionCompoundPowerFlow
    from ._4246 import PartToPartShearCouplingHalfCompoundPowerFlow
    from ._4247 import PlanetaryConnectionCompoundPowerFlow
    from ._4248 import PlanetaryGearSetCompoundPowerFlow
    from ._4249 import PlanetCarrierCompoundPowerFlow
    from ._4250 import PointLoadCompoundPowerFlow
    from ._4251 import PowerLoadCompoundPowerFlow
    from ._4252 import PulleyCompoundPowerFlow
    from ._4253 import RingPinsCompoundPowerFlow
    from ._4254 import RingPinsToDiscConnectionCompoundPowerFlow
    from ._4255 import RollingRingAssemblyCompoundPowerFlow
    from ._4256 import RollingRingCompoundPowerFlow
    from ._4257 import RollingRingConnectionCompoundPowerFlow
    from ._4258 import RootAssemblyCompoundPowerFlow
    from ._4259 import ShaftCompoundPowerFlow
    from ._4260 import ShaftHubConnectionCompoundPowerFlow
    from ._4261 import ShaftToMountableComponentConnectionCompoundPowerFlow
    from ._4262 import SpecialisedAssemblyCompoundPowerFlow
    from ._4263 import SpiralBevelGearCompoundPowerFlow
    from ._4264 import SpiralBevelGearMeshCompoundPowerFlow
    from ._4265 import SpiralBevelGearSetCompoundPowerFlow
    from ._4266 import SpringDamperCompoundPowerFlow
    from ._4267 import SpringDamperConnectionCompoundPowerFlow
    from ._4268 import SpringDamperHalfCompoundPowerFlow
    from ._4269 import StraightBevelDiffGearCompoundPowerFlow
    from ._4270 import StraightBevelDiffGearMeshCompoundPowerFlow
    from ._4271 import StraightBevelDiffGearSetCompoundPowerFlow
    from ._4272 import StraightBevelGearCompoundPowerFlow
    from ._4273 import StraightBevelGearMeshCompoundPowerFlow
    from ._4274 import StraightBevelGearSetCompoundPowerFlow
    from ._4275 import StraightBevelPlanetGearCompoundPowerFlow
    from ._4276 import StraightBevelSunGearCompoundPowerFlow
    from ._4277 import SynchroniserCompoundPowerFlow
    from ._4278 import SynchroniserHalfCompoundPowerFlow
    from ._4279 import SynchroniserPartCompoundPowerFlow
    from ._4280 import SynchroniserSleeveCompoundPowerFlow
    from ._4281 import TorqueConverterCompoundPowerFlow
    from ._4282 import TorqueConverterConnectionCompoundPowerFlow
    from ._4283 import TorqueConverterPumpCompoundPowerFlow
    from ._4284 import TorqueConverterTurbineCompoundPowerFlow
    from ._4285 import UnbalancedMassCompoundPowerFlow
    from ._4286 import VirtualComponentCompoundPowerFlow
    from ._4287 import WormGearCompoundPowerFlow
    from ._4288 import WormGearMeshCompoundPowerFlow
    from ._4289 import WormGearSetCompoundPowerFlow
    from ._4290 import ZerolBevelGearCompoundPowerFlow
    from ._4291 import ZerolBevelGearMeshCompoundPowerFlow
    from ._4292 import ZerolBevelGearSetCompoundPowerFlow
else:
    import_structure = {
        "_4164": ["AbstractAssemblyCompoundPowerFlow"],
        "_4165": ["AbstractShaftCompoundPowerFlow"],
        "_4166": ["AbstractShaftOrHousingCompoundPowerFlow"],
        "_4167": ["AbstractShaftToMountableComponentConnectionCompoundPowerFlow"],
        "_4168": ["AGMAGleasonConicalGearCompoundPowerFlow"],
        "_4169": ["AGMAGleasonConicalGearMeshCompoundPowerFlow"],
        "_4170": ["AGMAGleasonConicalGearSetCompoundPowerFlow"],
        "_4171": ["AssemblyCompoundPowerFlow"],
        "_4172": ["BearingCompoundPowerFlow"],
        "_4173": ["BeltConnectionCompoundPowerFlow"],
        "_4174": ["BeltDriveCompoundPowerFlow"],
        "_4175": ["BevelDifferentialGearCompoundPowerFlow"],
        "_4176": ["BevelDifferentialGearMeshCompoundPowerFlow"],
        "_4177": ["BevelDifferentialGearSetCompoundPowerFlow"],
        "_4178": ["BevelDifferentialPlanetGearCompoundPowerFlow"],
        "_4179": ["BevelDifferentialSunGearCompoundPowerFlow"],
        "_4180": ["BevelGearCompoundPowerFlow"],
        "_4181": ["BevelGearMeshCompoundPowerFlow"],
        "_4182": ["BevelGearSetCompoundPowerFlow"],
        "_4183": ["BoltCompoundPowerFlow"],
        "_4184": ["BoltedJointCompoundPowerFlow"],
        "_4185": ["ClutchCompoundPowerFlow"],
        "_4186": ["ClutchConnectionCompoundPowerFlow"],
        "_4187": ["ClutchHalfCompoundPowerFlow"],
        "_4188": ["CoaxialConnectionCompoundPowerFlow"],
        "_4189": ["ComponentCompoundPowerFlow"],
        "_4190": ["ConceptCouplingCompoundPowerFlow"],
        "_4191": ["ConceptCouplingConnectionCompoundPowerFlow"],
        "_4192": ["ConceptCouplingHalfCompoundPowerFlow"],
        "_4193": ["ConceptGearCompoundPowerFlow"],
        "_4194": ["ConceptGearMeshCompoundPowerFlow"],
        "_4195": ["ConceptGearSetCompoundPowerFlow"],
        "_4196": ["ConicalGearCompoundPowerFlow"],
        "_4197": ["ConicalGearMeshCompoundPowerFlow"],
        "_4198": ["ConicalGearSetCompoundPowerFlow"],
        "_4199": ["ConnectionCompoundPowerFlow"],
        "_4200": ["ConnectorCompoundPowerFlow"],
        "_4201": ["CouplingCompoundPowerFlow"],
        "_4202": ["CouplingConnectionCompoundPowerFlow"],
        "_4203": ["CouplingHalfCompoundPowerFlow"],
        "_4204": ["CVTBeltConnectionCompoundPowerFlow"],
        "_4205": ["CVTCompoundPowerFlow"],
        "_4206": ["CVTPulleyCompoundPowerFlow"],
        "_4207": ["CycloidalAssemblyCompoundPowerFlow"],
        "_4208": ["CycloidalDiscCentralBearingConnectionCompoundPowerFlow"],
        "_4209": ["CycloidalDiscCompoundPowerFlow"],
        "_4210": ["CycloidalDiscPlanetaryBearingConnectionCompoundPowerFlow"],
        "_4211": ["CylindricalGearCompoundPowerFlow"],
        "_4212": ["CylindricalGearMeshCompoundPowerFlow"],
        "_4213": ["CylindricalGearSetCompoundPowerFlow"],
        "_4214": ["CylindricalPlanetGearCompoundPowerFlow"],
        "_4215": ["DatumCompoundPowerFlow"],
        "_4216": ["ExternalCADModelCompoundPowerFlow"],
        "_4217": ["FaceGearCompoundPowerFlow"],
        "_4218": ["FaceGearMeshCompoundPowerFlow"],
        "_4219": ["FaceGearSetCompoundPowerFlow"],
        "_4220": ["FEPartCompoundPowerFlow"],
        "_4221": ["FlexiblePinAssemblyCompoundPowerFlow"],
        "_4222": ["GearCompoundPowerFlow"],
        "_4223": ["GearMeshCompoundPowerFlow"],
        "_4224": ["GearSetCompoundPowerFlow"],
        "_4225": ["GuideDxfModelCompoundPowerFlow"],
        "_4226": ["HypoidGearCompoundPowerFlow"],
        "_4227": ["HypoidGearMeshCompoundPowerFlow"],
        "_4228": ["HypoidGearSetCompoundPowerFlow"],
        "_4229": ["InterMountableComponentConnectionCompoundPowerFlow"],
        "_4230": ["KlingelnbergCycloPalloidConicalGearCompoundPowerFlow"],
        "_4231": ["KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow"],
        "_4232": ["KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow"],
        "_4233": ["KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow"],
        "_4234": ["KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow"],
        "_4235": ["KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow"],
        "_4236": ["KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow"],
        "_4237": ["KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow"],
        "_4238": ["KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow"],
        "_4239": ["MassDiscCompoundPowerFlow"],
        "_4240": ["MeasurementComponentCompoundPowerFlow"],
        "_4241": ["MountableComponentCompoundPowerFlow"],
        "_4242": ["OilSealCompoundPowerFlow"],
        "_4243": ["PartCompoundPowerFlow"],
        "_4244": ["PartToPartShearCouplingCompoundPowerFlow"],
        "_4245": ["PartToPartShearCouplingConnectionCompoundPowerFlow"],
        "_4246": ["PartToPartShearCouplingHalfCompoundPowerFlow"],
        "_4247": ["PlanetaryConnectionCompoundPowerFlow"],
        "_4248": ["PlanetaryGearSetCompoundPowerFlow"],
        "_4249": ["PlanetCarrierCompoundPowerFlow"],
        "_4250": ["PointLoadCompoundPowerFlow"],
        "_4251": ["PowerLoadCompoundPowerFlow"],
        "_4252": ["PulleyCompoundPowerFlow"],
        "_4253": ["RingPinsCompoundPowerFlow"],
        "_4254": ["RingPinsToDiscConnectionCompoundPowerFlow"],
        "_4255": ["RollingRingAssemblyCompoundPowerFlow"],
        "_4256": ["RollingRingCompoundPowerFlow"],
        "_4257": ["RollingRingConnectionCompoundPowerFlow"],
        "_4258": ["RootAssemblyCompoundPowerFlow"],
        "_4259": ["ShaftCompoundPowerFlow"],
        "_4260": ["ShaftHubConnectionCompoundPowerFlow"],
        "_4261": ["ShaftToMountableComponentConnectionCompoundPowerFlow"],
        "_4262": ["SpecialisedAssemblyCompoundPowerFlow"],
        "_4263": ["SpiralBevelGearCompoundPowerFlow"],
        "_4264": ["SpiralBevelGearMeshCompoundPowerFlow"],
        "_4265": ["SpiralBevelGearSetCompoundPowerFlow"],
        "_4266": ["SpringDamperCompoundPowerFlow"],
        "_4267": ["SpringDamperConnectionCompoundPowerFlow"],
        "_4268": ["SpringDamperHalfCompoundPowerFlow"],
        "_4269": ["StraightBevelDiffGearCompoundPowerFlow"],
        "_4270": ["StraightBevelDiffGearMeshCompoundPowerFlow"],
        "_4271": ["StraightBevelDiffGearSetCompoundPowerFlow"],
        "_4272": ["StraightBevelGearCompoundPowerFlow"],
        "_4273": ["StraightBevelGearMeshCompoundPowerFlow"],
        "_4274": ["StraightBevelGearSetCompoundPowerFlow"],
        "_4275": ["StraightBevelPlanetGearCompoundPowerFlow"],
        "_4276": ["StraightBevelSunGearCompoundPowerFlow"],
        "_4277": ["SynchroniserCompoundPowerFlow"],
        "_4278": ["SynchroniserHalfCompoundPowerFlow"],
        "_4279": ["SynchroniserPartCompoundPowerFlow"],
        "_4280": ["SynchroniserSleeveCompoundPowerFlow"],
        "_4281": ["TorqueConverterCompoundPowerFlow"],
        "_4282": ["TorqueConverterConnectionCompoundPowerFlow"],
        "_4283": ["TorqueConverterPumpCompoundPowerFlow"],
        "_4284": ["TorqueConverterTurbineCompoundPowerFlow"],
        "_4285": ["UnbalancedMassCompoundPowerFlow"],
        "_4286": ["VirtualComponentCompoundPowerFlow"],
        "_4287": ["WormGearCompoundPowerFlow"],
        "_4288": ["WormGearMeshCompoundPowerFlow"],
        "_4289": ["WormGearSetCompoundPowerFlow"],
        "_4290": ["ZerolBevelGearCompoundPowerFlow"],
        "_4291": ["ZerolBevelGearMeshCompoundPowerFlow"],
        "_4292": ["ZerolBevelGearSetCompoundPowerFlow"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundPowerFlow",
    "AbstractShaftCompoundPowerFlow",
    "AbstractShaftOrHousingCompoundPowerFlow",
    "AbstractShaftToMountableComponentConnectionCompoundPowerFlow",
    "AGMAGleasonConicalGearCompoundPowerFlow",
    "AGMAGleasonConicalGearMeshCompoundPowerFlow",
    "AGMAGleasonConicalGearSetCompoundPowerFlow",
    "AssemblyCompoundPowerFlow",
    "BearingCompoundPowerFlow",
    "BeltConnectionCompoundPowerFlow",
    "BeltDriveCompoundPowerFlow",
    "BevelDifferentialGearCompoundPowerFlow",
    "BevelDifferentialGearMeshCompoundPowerFlow",
    "BevelDifferentialGearSetCompoundPowerFlow",
    "BevelDifferentialPlanetGearCompoundPowerFlow",
    "BevelDifferentialSunGearCompoundPowerFlow",
    "BevelGearCompoundPowerFlow",
    "BevelGearMeshCompoundPowerFlow",
    "BevelGearSetCompoundPowerFlow",
    "BoltCompoundPowerFlow",
    "BoltedJointCompoundPowerFlow",
    "ClutchCompoundPowerFlow",
    "ClutchConnectionCompoundPowerFlow",
    "ClutchHalfCompoundPowerFlow",
    "CoaxialConnectionCompoundPowerFlow",
    "ComponentCompoundPowerFlow",
    "ConceptCouplingCompoundPowerFlow",
    "ConceptCouplingConnectionCompoundPowerFlow",
    "ConceptCouplingHalfCompoundPowerFlow",
    "ConceptGearCompoundPowerFlow",
    "ConceptGearMeshCompoundPowerFlow",
    "ConceptGearSetCompoundPowerFlow",
    "ConicalGearCompoundPowerFlow",
    "ConicalGearMeshCompoundPowerFlow",
    "ConicalGearSetCompoundPowerFlow",
    "ConnectionCompoundPowerFlow",
    "ConnectorCompoundPowerFlow",
    "CouplingCompoundPowerFlow",
    "CouplingConnectionCompoundPowerFlow",
    "CouplingHalfCompoundPowerFlow",
    "CVTBeltConnectionCompoundPowerFlow",
    "CVTCompoundPowerFlow",
    "CVTPulleyCompoundPowerFlow",
    "CycloidalAssemblyCompoundPowerFlow",
    "CycloidalDiscCentralBearingConnectionCompoundPowerFlow",
    "CycloidalDiscCompoundPowerFlow",
    "CycloidalDiscPlanetaryBearingConnectionCompoundPowerFlow",
    "CylindricalGearCompoundPowerFlow",
    "CylindricalGearMeshCompoundPowerFlow",
    "CylindricalGearSetCompoundPowerFlow",
    "CylindricalPlanetGearCompoundPowerFlow",
    "DatumCompoundPowerFlow",
    "ExternalCADModelCompoundPowerFlow",
    "FaceGearCompoundPowerFlow",
    "FaceGearMeshCompoundPowerFlow",
    "FaceGearSetCompoundPowerFlow",
    "FEPartCompoundPowerFlow",
    "FlexiblePinAssemblyCompoundPowerFlow",
    "GearCompoundPowerFlow",
    "GearMeshCompoundPowerFlow",
    "GearSetCompoundPowerFlow",
    "GuideDxfModelCompoundPowerFlow",
    "HypoidGearCompoundPowerFlow",
    "HypoidGearMeshCompoundPowerFlow",
    "HypoidGearSetCompoundPowerFlow",
    "InterMountableComponentConnectionCompoundPowerFlow",
    "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow",
    "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow",
    "KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow",
    "MassDiscCompoundPowerFlow",
    "MeasurementComponentCompoundPowerFlow",
    "MountableComponentCompoundPowerFlow",
    "OilSealCompoundPowerFlow",
    "PartCompoundPowerFlow",
    "PartToPartShearCouplingCompoundPowerFlow",
    "PartToPartShearCouplingConnectionCompoundPowerFlow",
    "PartToPartShearCouplingHalfCompoundPowerFlow",
    "PlanetaryConnectionCompoundPowerFlow",
    "PlanetaryGearSetCompoundPowerFlow",
    "PlanetCarrierCompoundPowerFlow",
    "PointLoadCompoundPowerFlow",
    "PowerLoadCompoundPowerFlow",
    "PulleyCompoundPowerFlow",
    "RingPinsCompoundPowerFlow",
    "RingPinsToDiscConnectionCompoundPowerFlow",
    "RollingRingAssemblyCompoundPowerFlow",
    "RollingRingCompoundPowerFlow",
    "RollingRingConnectionCompoundPowerFlow",
    "RootAssemblyCompoundPowerFlow",
    "ShaftCompoundPowerFlow",
    "ShaftHubConnectionCompoundPowerFlow",
    "ShaftToMountableComponentConnectionCompoundPowerFlow",
    "SpecialisedAssemblyCompoundPowerFlow",
    "SpiralBevelGearCompoundPowerFlow",
    "SpiralBevelGearMeshCompoundPowerFlow",
    "SpiralBevelGearSetCompoundPowerFlow",
    "SpringDamperCompoundPowerFlow",
    "SpringDamperConnectionCompoundPowerFlow",
    "SpringDamperHalfCompoundPowerFlow",
    "StraightBevelDiffGearCompoundPowerFlow",
    "StraightBevelDiffGearMeshCompoundPowerFlow",
    "StraightBevelDiffGearSetCompoundPowerFlow",
    "StraightBevelGearCompoundPowerFlow",
    "StraightBevelGearMeshCompoundPowerFlow",
    "StraightBevelGearSetCompoundPowerFlow",
    "StraightBevelPlanetGearCompoundPowerFlow",
    "StraightBevelSunGearCompoundPowerFlow",
    "SynchroniserCompoundPowerFlow",
    "SynchroniserHalfCompoundPowerFlow",
    "SynchroniserPartCompoundPowerFlow",
    "SynchroniserSleeveCompoundPowerFlow",
    "TorqueConverterCompoundPowerFlow",
    "TorqueConverterConnectionCompoundPowerFlow",
    "TorqueConverterPumpCompoundPowerFlow",
    "TorqueConverterTurbineCompoundPowerFlow",
    "UnbalancedMassCompoundPowerFlow",
    "VirtualComponentCompoundPowerFlow",
    "WormGearCompoundPowerFlow",
    "WormGearMeshCompoundPowerFlow",
    "WormGearSetCompoundPowerFlow",
    "ZerolBevelGearCompoundPowerFlow",
    "ZerolBevelGearMeshCompoundPowerFlow",
    "ZerolBevelGearSetCompoundPowerFlow",
)
