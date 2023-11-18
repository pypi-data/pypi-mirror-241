"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5244 import AbstractAssemblyCompoundModalAnalysisAtASpeed
    from ._5245 import AbstractShaftCompoundModalAnalysisAtASpeed
    from ._5246 import AbstractShaftOrHousingCompoundModalAnalysisAtASpeed
    from ._5247 import (
        AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed,
    )
    from ._5248 import AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed
    from ._5249 import AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed
    from ._5250 import AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed
    from ._5251 import AssemblyCompoundModalAnalysisAtASpeed
    from ._5252 import BearingCompoundModalAnalysisAtASpeed
    from ._5253 import BeltConnectionCompoundModalAnalysisAtASpeed
    from ._5254 import BeltDriveCompoundModalAnalysisAtASpeed
    from ._5255 import BevelDifferentialGearCompoundModalAnalysisAtASpeed
    from ._5256 import BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed
    from ._5257 import BevelDifferentialGearSetCompoundModalAnalysisAtASpeed
    from ._5258 import BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed
    from ._5259 import BevelDifferentialSunGearCompoundModalAnalysisAtASpeed
    from ._5260 import BevelGearCompoundModalAnalysisAtASpeed
    from ._5261 import BevelGearMeshCompoundModalAnalysisAtASpeed
    from ._5262 import BevelGearSetCompoundModalAnalysisAtASpeed
    from ._5263 import BoltCompoundModalAnalysisAtASpeed
    from ._5264 import BoltedJointCompoundModalAnalysisAtASpeed
    from ._5265 import ClutchCompoundModalAnalysisAtASpeed
    from ._5266 import ClutchConnectionCompoundModalAnalysisAtASpeed
    from ._5267 import ClutchHalfCompoundModalAnalysisAtASpeed
    from ._5268 import CoaxialConnectionCompoundModalAnalysisAtASpeed
    from ._5269 import ComponentCompoundModalAnalysisAtASpeed
    from ._5270 import ConceptCouplingCompoundModalAnalysisAtASpeed
    from ._5271 import ConceptCouplingConnectionCompoundModalAnalysisAtASpeed
    from ._5272 import ConceptCouplingHalfCompoundModalAnalysisAtASpeed
    from ._5273 import ConceptGearCompoundModalAnalysisAtASpeed
    from ._5274 import ConceptGearMeshCompoundModalAnalysisAtASpeed
    from ._5275 import ConceptGearSetCompoundModalAnalysisAtASpeed
    from ._5276 import ConicalGearCompoundModalAnalysisAtASpeed
    from ._5277 import ConicalGearMeshCompoundModalAnalysisAtASpeed
    from ._5278 import ConicalGearSetCompoundModalAnalysisAtASpeed
    from ._5279 import ConnectionCompoundModalAnalysisAtASpeed
    from ._5280 import ConnectorCompoundModalAnalysisAtASpeed
    from ._5281 import CouplingCompoundModalAnalysisAtASpeed
    from ._5282 import CouplingConnectionCompoundModalAnalysisAtASpeed
    from ._5283 import CouplingHalfCompoundModalAnalysisAtASpeed
    from ._5284 import CVTBeltConnectionCompoundModalAnalysisAtASpeed
    from ._5285 import CVTCompoundModalAnalysisAtASpeed
    from ._5286 import CVTPulleyCompoundModalAnalysisAtASpeed
    from ._5287 import CycloidalAssemblyCompoundModalAnalysisAtASpeed
    from ._5288 import (
        CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed,
    )
    from ._5289 import CycloidalDiscCompoundModalAnalysisAtASpeed
    from ._5290 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed,
    )
    from ._5291 import CylindricalGearCompoundModalAnalysisAtASpeed
    from ._5292 import CylindricalGearMeshCompoundModalAnalysisAtASpeed
    from ._5293 import CylindricalGearSetCompoundModalAnalysisAtASpeed
    from ._5294 import CylindricalPlanetGearCompoundModalAnalysisAtASpeed
    from ._5295 import DatumCompoundModalAnalysisAtASpeed
    from ._5296 import ExternalCADModelCompoundModalAnalysisAtASpeed
    from ._5297 import FaceGearCompoundModalAnalysisAtASpeed
    from ._5298 import FaceGearMeshCompoundModalAnalysisAtASpeed
    from ._5299 import FaceGearSetCompoundModalAnalysisAtASpeed
    from ._5300 import FEPartCompoundModalAnalysisAtASpeed
    from ._5301 import FlexiblePinAssemblyCompoundModalAnalysisAtASpeed
    from ._5302 import GearCompoundModalAnalysisAtASpeed
    from ._5303 import GearMeshCompoundModalAnalysisAtASpeed
    from ._5304 import GearSetCompoundModalAnalysisAtASpeed
    from ._5305 import GuideDxfModelCompoundModalAnalysisAtASpeed
    from ._5306 import HypoidGearCompoundModalAnalysisAtASpeed
    from ._5307 import HypoidGearMeshCompoundModalAnalysisAtASpeed
    from ._5308 import HypoidGearSetCompoundModalAnalysisAtASpeed
    from ._5309 import InterMountableComponentConnectionCompoundModalAnalysisAtASpeed
    from ._5310 import KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed
    from ._5311 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed,
    )
    from ._5312 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed,
    )
    from ._5313 import KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed
    from ._5314 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed,
    )
    from ._5315 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed,
    )
    from ._5316 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed,
    )
    from ._5317 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed,
    )
    from ._5318 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed,
    )
    from ._5319 import MassDiscCompoundModalAnalysisAtASpeed
    from ._5320 import MeasurementComponentCompoundModalAnalysisAtASpeed
    from ._5321 import MountableComponentCompoundModalAnalysisAtASpeed
    from ._5322 import OilSealCompoundModalAnalysisAtASpeed
    from ._5323 import PartCompoundModalAnalysisAtASpeed
    from ._5324 import PartToPartShearCouplingCompoundModalAnalysisAtASpeed
    from ._5325 import PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed
    from ._5326 import PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed
    from ._5327 import PlanetaryConnectionCompoundModalAnalysisAtASpeed
    from ._5328 import PlanetaryGearSetCompoundModalAnalysisAtASpeed
    from ._5329 import PlanetCarrierCompoundModalAnalysisAtASpeed
    from ._5330 import PointLoadCompoundModalAnalysisAtASpeed
    from ._5331 import PowerLoadCompoundModalAnalysisAtASpeed
    from ._5332 import PulleyCompoundModalAnalysisAtASpeed
    from ._5333 import RingPinsCompoundModalAnalysisAtASpeed
    from ._5334 import RingPinsToDiscConnectionCompoundModalAnalysisAtASpeed
    from ._5335 import RollingRingAssemblyCompoundModalAnalysisAtASpeed
    from ._5336 import RollingRingCompoundModalAnalysisAtASpeed
    from ._5337 import RollingRingConnectionCompoundModalAnalysisAtASpeed
    from ._5338 import RootAssemblyCompoundModalAnalysisAtASpeed
    from ._5339 import ShaftCompoundModalAnalysisAtASpeed
    from ._5340 import ShaftHubConnectionCompoundModalAnalysisAtASpeed
    from ._5341 import ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed
    from ._5342 import SpecialisedAssemblyCompoundModalAnalysisAtASpeed
    from ._5343 import SpiralBevelGearCompoundModalAnalysisAtASpeed
    from ._5344 import SpiralBevelGearMeshCompoundModalAnalysisAtASpeed
    from ._5345 import SpiralBevelGearSetCompoundModalAnalysisAtASpeed
    from ._5346 import SpringDamperCompoundModalAnalysisAtASpeed
    from ._5347 import SpringDamperConnectionCompoundModalAnalysisAtASpeed
    from ._5348 import SpringDamperHalfCompoundModalAnalysisAtASpeed
    from ._5349 import StraightBevelDiffGearCompoundModalAnalysisAtASpeed
    from ._5350 import StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed
    from ._5351 import StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed
    from ._5352 import StraightBevelGearCompoundModalAnalysisAtASpeed
    from ._5353 import StraightBevelGearMeshCompoundModalAnalysisAtASpeed
    from ._5354 import StraightBevelGearSetCompoundModalAnalysisAtASpeed
    from ._5355 import StraightBevelPlanetGearCompoundModalAnalysisAtASpeed
    from ._5356 import StraightBevelSunGearCompoundModalAnalysisAtASpeed
    from ._5357 import SynchroniserCompoundModalAnalysisAtASpeed
    from ._5358 import SynchroniserHalfCompoundModalAnalysisAtASpeed
    from ._5359 import SynchroniserPartCompoundModalAnalysisAtASpeed
    from ._5360 import SynchroniserSleeveCompoundModalAnalysisAtASpeed
    from ._5361 import TorqueConverterCompoundModalAnalysisAtASpeed
    from ._5362 import TorqueConverterConnectionCompoundModalAnalysisAtASpeed
    from ._5363 import TorqueConverterPumpCompoundModalAnalysisAtASpeed
    from ._5364 import TorqueConverterTurbineCompoundModalAnalysisAtASpeed
    from ._5365 import UnbalancedMassCompoundModalAnalysisAtASpeed
    from ._5366 import VirtualComponentCompoundModalAnalysisAtASpeed
    from ._5367 import WormGearCompoundModalAnalysisAtASpeed
    from ._5368 import WormGearMeshCompoundModalAnalysisAtASpeed
    from ._5369 import WormGearSetCompoundModalAnalysisAtASpeed
    from ._5370 import ZerolBevelGearCompoundModalAnalysisAtASpeed
    from ._5371 import ZerolBevelGearMeshCompoundModalAnalysisAtASpeed
    from ._5372 import ZerolBevelGearSetCompoundModalAnalysisAtASpeed
else:
    import_structure = {
        "_5244": ["AbstractAssemblyCompoundModalAnalysisAtASpeed"],
        "_5245": ["AbstractShaftCompoundModalAnalysisAtASpeed"],
        "_5246": ["AbstractShaftOrHousingCompoundModalAnalysisAtASpeed"],
        "_5247": [
            "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed"
        ],
        "_5248": ["AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed"],
        "_5249": ["AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed"],
        "_5250": ["AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed"],
        "_5251": ["AssemblyCompoundModalAnalysisAtASpeed"],
        "_5252": ["BearingCompoundModalAnalysisAtASpeed"],
        "_5253": ["BeltConnectionCompoundModalAnalysisAtASpeed"],
        "_5254": ["BeltDriveCompoundModalAnalysisAtASpeed"],
        "_5255": ["BevelDifferentialGearCompoundModalAnalysisAtASpeed"],
        "_5256": ["BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed"],
        "_5257": ["BevelDifferentialGearSetCompoundModalAnalysisAtASpeed"],
        "_5258": ["BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed"],
        "_5259": ["BevelDifferentialSunGearCompoundModalAnalysisAtASpeed"],
        "_5260": ["BevelGearCompoundModalAnalysisAtASpeed"],
        "_5261": ["BevelGearMeshCompoundModalAnalysisAtASpeed"],
        "_5262": ["BevelGearSetCompoundModalAnalysisAtASpeed"],
        "_5263": ["BoltCompoundModalAnalysisAtASpeed"],
        "_5264": ["BoltedJointCompoundModalAnalysisAtASpeed"],
        "_5265": ["ClutchCompoundModalAnalysisAtASpeed"],
        "_5266": ["ClutchConnectionCompoundModalAnalysisAtASpeed"],
        "_5267": ["ClutchHalfCompoundModalAnalysisAtASpeed"],
        "_5268": ["CoaxialConnectionCompoundModalAnalysisAtASpeed"],
        "_5269": ["ComponentCompoundModalAnalysisAtASpeed"],
        "_5270": ["ConceptCouplingCompoundModalAnalysisAtASpeed"],
        "_5271": ["ConceptCouplingConnectionCompoundModalAnalysisAtASpeed"],
        "_5272": ["ConceptCouplingHalfCompoundModalAnalysisAtASpeed"],
        "_5273": ["ConceptGearCompoundModalAnalysisAtASpeed"],
        "_5274": ["ConceptGearMeshCompoundModalAnalysisAtASpeed"],
        "_5275": ["ConceptGearSetCompoundModalAnalysisAtASpeed"],
        "_5276": ["ConicalGearCompoundModalAnalysisAtASpeed"],
        "_5277": ["ConicalGearMeshCompoundModalAnalysisAtASpeed"],
        "_5278": ["ConicalGearSetCompoundModalAnalysisAtASpeed"],
        "_5279": ["ConnectionCompoundModalAnalysisAtASpeed"],
        "_5280": ["ConnectorCompoundModalAnalysisAtASpeed"],
        "_5281": ["CouplingCompoundModalAnalysisAtASpeed"],
        "_5282": ["CouplingConnectionCompoundModalAnalysisAtASpeed"],
        "_5283": ["CouplingHalfCompoundModalAnalysisAtASpeed"],
        "_5284": ["CVTBeltConnectionCompoundModalAnalysisAtASpeed"],
        "_5285": ["CVTCompoundModalAnalysisAtASpeed"],
        "_5286": ["CVTPulleyCompoundModalAnalysisAtASpeed"],
        "_5287": ["CycloidalAssemblyCompoundModalAnalysisAtASpeed"],
        "_5288": ["CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed"],
        "_5289": ["CycloidalDiscCompoundModalAnalysisAtASpeed"],
        "_5290": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed"
        ],
        "_5291": ["CylindricalGearCompoundModalAnalysisAtASpeed"],
        "_5292": ["CylindricalGearMeshCompoundModalAnalysisAtASpeed"],
        "_5293": ["CylindricalGearSetCompoundModalAnalysisAtASpeed"],
        "_5294": ["CylindricalPlanetGearCompoundModalAnalysisAtASpeed"],
        "_5295": ["DatumCompoundModalAnalysisAtASpeed"],
        "_5296": ["ExternalCADModelCompoundModalAnalysisAtASpeed"],
        "_5297": ["FaceGearCompoundModalAnalysisAtASpeed"],
        "_5298": ["FaceGearMeshCompoundModalAnalysisAtASpeed"],
        "_5299": ["FaceGearSetCompoundModalAnalysisAtASpeed"],
        "_5300": ["FEPartCompoundModalAnalysisAtASpeed"],
        "_5301": ["FlexiblePinAssemblyCompoundModalAnalysisAtASpeed"],
        "_5302": ["GearCompoundModalAnalysisAtASpeed"],
        "_5303": ["GearMeshCompoundModalAnalysisAtASpeed"],
        "_5304": ["GearSetCompoundModalAnalysisAtASpeed"],
        "_5305": ["GuideDxfModelCompoundModalAnalysisAtASpeed"],
        "_5306": ["HypoidGearCompoundModalAnalysisAtASpeed"],
        "_5307": ["HypoidGearMeshCompoundModalAnalysisAtASpeed"],
        "_5308": ["HypoidGearSetCompoundModalAnalysisAtASpeed"],
        "_5309": ["InterMountableComponentConnectionCompoundModalAnalysisAtASpeed"],
        "_5310": ["KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed"],
        "_5311": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed"
        ],
        "_5312": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed"
        ],
        "_5313": ["KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed"],
        "_5314": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed"
        ],
        "_5315": ["KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed"],
        "_5316": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed"
        ],
        "_5317": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed"
        ],
        "_5318": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed"
        ],
        "_5319": ["MassDiscCompoundModalAnalysisAtASpeed"],
        "_5320": ["MeasurementComponentCompoundModalAnalysisAtASpeed"],
        "_5321": ["MountableComponentCompoundModalAnalysisAtASpeed"],
        "_5322": ["OilSealCompoundModalAnalysisAtASpeed"],
        "_5323": ["PartCompoundModalAnalysisAtASpeed"],
        "_5324": ["PartToPartShearCouplingCompoundModalAnalysisAtASpeed"],
        "_5325": ["PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed"],
        "_5326": ["PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed"],
        "_5327": ["PlanetaryConnectionCompoundModalAnalysisAtASpeed"],
        "_5328": ["PlanetaryGearSetCompoundModalAnalysisAtASpeed"],
        "_5329": ["PlanetCarrierCompoundModalAnalysisAtASpeed"],
        "_5330": ["PointLoadCompoundModalAnalysisAtASpeed"],
        "_5331": ["PowerLoadCompoundModalAnalysisAtASpeed"],
        "_5332": ["PulleyCompoundModalAnalysisAtASpeed"],
        "_5333": ["RingPinsCompoundModalAnalysisAtASpeed"],
        "_5334": ["RingPinsToDiscConnectionCompoundModalAnalysisAtASpeed"],
        "_5335": ["RollingRingAssemblyCompoundModalAnalysisAtASpeed"],
        "_5336": ["RollingRingCompoundModalAnalysisAtASpeed"],
        "_5337": ["RollingRingConnectionCompoundModalAnalysisAtASpeed"],
        "_5338": ["RootAssemblyCompoundModalAnalysisAtASpeed"],
        "_5339": ["ShaftCompoundModalAnalysisAtASpeed"],
        "_5340": ["ShaftHubConnectionCompoundModalAnalysisAtASpeed"],
        "_5341": ["ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed"],
        "_5342": ["SpecialisedAssemblyCompoundModalAnalysisAtASpeed"],
        "_5343": ["SpiralBevelGearCompoundModalAnalysisAtASpeed"],
        "_5344": ["SpiralBevelGearMeshCompoundModalAnalysisAtASpeed"],
        "_5345": ["SpiralBevelGearSetCompoundModalAnalysisAtASpeed"],
        "_5346": ["SpringDamperCompoundModalAnalysisAtASpeed"],
        "_5347": ["SpringDamperConnectionCompoundModalAnalysisAtASpeed"],
        "_5348": ["SpringDamperHalfCompoundModalAnalysisAtASpeed"],
        "_5349": ["StraightBevelDiffGearCompoundModalAnalysisAtASpeed"],
        "_5350": ["StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed"],
        "_5351": ["StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed"],
        "_5352": ["StraightBevelGearCompoundModalAnalysisAtASpeed"],
        "_5353": ["StraightBevelGearMeshCompoundModalAnalysisAtASpeed"],
        "_5354": ["StraightBevelGearSetCompoundModalAnalysisAtASpeed"],
        "_5355": ["StraightBevelPlanetGearCompoundModalAnalysisAtASpeed"],
        "_5356": ["StraightBevelSunGearCompoundModalAnalysisAtASpeed"],
        "_5357": ["SynchroniserCompoundModalAnalysisAtASpeed"],
        "_5358": ["SynchroniserHalfCompoundModalAnalysisAtASpeed"],
        "_5359": ["SynchroniserPartCompoundModalAnalysisAtASpeed"],
        "_5360": ["SynchroniserSleeveCompoundModalAnalysisAtASpeed"],
        "_5361": ["TorqueConverterCompoundModalAnalysisAtASpeed"],
        "_5362": ["TorqueConverterConnectionCompoundModalAnalysisAtASpeed"],
        "_5363": ["TorqueConverterPumpCompoundModalAnalysisAtASpeed"],
        "_5364": ["TorqueConverterTurbineCompoundModalAnalysisAtASpeed"],
        "_5365": ["UnbalancedMassCompoundModalAnalysisAtASpeed"],
        "_5366": ["VirtualComponentCompoundModalAnalysisAtASpeed"],
        "_5367": ["WormGearCompoundModalAnalysisAtASpeed"],
        "_5368": ["WormGearMeshCompoundModalAnalysisAtASpeed"],
        "_5369": ["WormGearSetCompoundModalAnalysisAtASpeed"],
        "_5370": ["ZerolBevelGearCompoundModalAnalysisAtASpeed"],
        "_5371": ["ZerolBevelGearMeshCompoundModalAnalysisAtASpeed"],
        "_5372": ["ZerolBevelGearSetCompoundModalAnalysisAtASpeed"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundModalAnalysisAtASpeed",
    "AbstractShaftCompoundModalAnalysisAtASpeed",
    "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
    "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
    "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
    "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
    "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
    "AssemblyCompoundModalAnalysisAtASpeed",
    "BearingCompoundModalAnalysisAtASpeed",
    "BeltConnectionCompoundModalAnalysisAtASpeed",
    "BeltDriveCompoundModalAnalysisAtASpeed",
    "BevelDifferentialGearCompoundModalAnalysisAtASpeed",
    "BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed",
    "BevelDifferentialGearSetCompoundModalAnalysisAtASpeed",
    "BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed",
    "BevelDifferentialSunGearCompoundModalAnalysisAtASpeed",
    "BevelGearCompoundModalAnalysisAtASpeed",
    "BevelGearMeshCompoundModalAnalysisAtASpeed",
    "BevelGearSetCompoundModalAnalysisAtASpeed",
    "BoltCompoundModalAnalysisAtASpeed",
    "BoltedJointCompoundModalAnalysisAtASpeed",
    "ClutchCompoundModalAnalysisAtASpeed",
    "ClutchConnectionCompoundModalAnalysisAtASpeed",
    "ClutchHalfCompoundModalAnalysisAtASpeed",
    "CoaxialConnectionCompoundModalAnalysisAtASpeed",
    "ComponentCompoundModalAnalysisAtASpeed",
    "ConceptCouplingCompoundModalAnalysisAtASpeed",
    "ConceptCouplingConnectionCompoundModalAnalysisAtASpeed",
    "ConceptCouplingHalfCompoundModalAnalysisAtASpeed",
    "ConceptGearCompoundModalAnalysisAtASpeed",
    "ConceptGearMeshCompoundModalAnalysisAtASpeed",
    "ConceptGearSetCompoundModalAnalysisAtASpeed",
    "ConicalGearCompoundModalAnalysisAtASpeed",
    "ConicalGearMeshCompoundModalAnalysisAtASpeed",
    "ConicalGearSetCompoundModalAnalysisAtASpeed",
    "ConnectionCompoundModalAnalysisAtASpeed",
    "ConnectorCompoundModalAnalysisAtASpeed",
    "CouplingCompoundModalAnalysisAtASpeed",
    "CouplingConnectionCompoundModalAnalysisAtASpeed",
    "CouplingHalfCompoundModalAnalysisAtASpeed",
    "CVTBeltConnectionCompoundModalAnalysisAtASpeed",
    "CVTCompoundModalAnalysisAtASpeed",
    "CVTPulleyCompoundModalAnalysisAtASpeed",
    "CycloidalAssemblyCompoundModalAnalysisAtASpeed",
    "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed",
    "CycloidalDiscCompoundModalAnalysisAtASpeed",
    "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed",
    "CylindricalGearCompoundModalAnalysisAtASpeed",
    "CylindricalGearMeshCompoundModalAnalysisAtASpeed",
    "CylindricalGearSetCompoundModalAnalysisAtASpeed",
    "CylindricalPlanetGearCompoundModalAnalysisAtASpeed",
    "DatumCompoundModalAnalysisAtASpeed",
    "ExternalCADModelCompoundModalAnalysisAtASpeed",
    "FaceGearCompoundModalAnalysisAtASpeed",
    "FaceGearMeshCompoundModalAnalysisAtASpeed",
    "FaceGearSetCompoundModalAnalysisAtASpeed",
    "FEPartCompoundModalAnalysisAtASpeed",
    "FlexiblePinAssemblyCompoundModalAnalysisAtASpeed",
    "GearCompoundModalAnalysisAtASpeed",
    "GearMeshCompoundModalAnalysisAtASpeed",
    "GearSetCompoundModalAnalysisAtASpeed",
    "GuideDxfModelCompoundModalAnalysisAtASpeed",
    "HypoidGearCompoundModalAnalysisAtASpeed",
    "HypoidGearMeshCompoundModalAnalysisAtASpeed",
    "HypoidGearSetCompoundModalAnalysisAtASpeed",
    "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed",
    "MassDiscCompoundModalAnalysisAtASpeed",
    "MeasurementComponentCompoundModalAnalysisAtASpeed",
    "MountableComponentCompoundModalAnalysisAtASpeed",
    "OilSealCompoundModalAnalysisAtASpeed",
    "PartCompoundModalAnalysisAtASpeed",
    "PartToPartShearCouplingCompoundModalAnalysisAtASpeed",
    "PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed",
    "PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed",
    "PlanetaryConnectionCompoundModalAnalysisAtASpeed",
    "PlanetaryGearSetCompoundModalAnalysisAtASpeed",
    "PlanetCarrierCompoundModalAnalysisAtASpeed",
    "PointLoadCompoundModalAnalysisAtASpeed",
    "PowerLoadCompoundModalAnalysisAtASpeed",
    "PulleyCompoundModalAnalysisAtASpeed",
    "RingPinsCompoundModalAnalysisAtASpeed",
    "RingPinsToDiscConnectionCompoundModalAnalysisAtASpeed",
    "RollingRingAssemblyCompoundModalAnalysisAtASpeed",
    "RollingRingCompoundModalAnalysisAtASpeed",
    "RollingRingConnectionCompoundModalAnalysisAtASpeed",
    "RootAssemblyCompoundModalAnalysisAtASpeed",
    "ShaftCompoundModalAnalysisAtASpeed",
    "ShaftHubConnectionCompoundModalAnalysisAtASpeed",
    "ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
    "SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
    "SpiralBevelGearCompoundModalAnalysisAtASpeed",
    "SpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
    "SpiralBevelGearSetCompoundModalAnalysisAtASpeed",
    "SpringDamperCompoundModalAnalysisAtASpeed",
    "SpringDamperConnectionCompoundModalAnalysisAtASpeed",
    "SpringDamperHalfCompoundModalAnalysisAtASpeed",
    "StraightBevelDiffGearCompoundModalAnalysisAtASpeed",
    "StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed",
    "StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed",
    "StraightBevelGearCompoundModalAnalysisAtASpeed",
    "StraightBevelGearMeshCompoundModalAnalysisAtASpeed",
    "StraightBevelGearSetCompoundModalAnalysisAtASpeed",
    "StraightBevelPlanetGearCompoundModalAnalysisAtASpeed",
    "StraightBevelSunGearCompoundModalAnalysisAtASpeed",
    "SynchroniserCompoundModalAnalysisAtASpeed",
    "SynchroniserHalfCompoundModalAnalysisAtASpeed",
    "SynchroniserPartCompoundModalAnalysisAtASpeed",
    "SynchroniserSleeveCompoundModalAnalysisAtASpeed",
    "TorqueConverterCompoundModalAnalysisAtASpeed",
    "TorqueConverterConnectionCompoundModalAnalysisAtASpeed",
    "TorqueConverterPumpCompoundModalAnalysisAtASpeed",
    "TorqueConverterTurbineCompoundModalAnalysisAtASpeed",
    "UnbalancedMassCompoundModalAnalysisAtASpeed",
    "VirtualComponentCompoundModalAnalysisAtASpeed",
    "WormGearCompoundModalAnalysisAtASpeed",
    "WormGearMeshCompoundModalAnalysisAtASpeed",
    "WormGearSetCompoundModalAnalysisAtASpeed",
    "ZerolBevelGearCompoundModalAnalysisAtASpeed",
    "ZerolBevelGearMeshCompoundModalAnalysisAtASpeed",
    "ZerolBevelGearSetCompoundModalAnalysisAtASpeed",
)
