"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7267 import AbstractAssemblyAdvancedSystemDeflection
    from ._7268 import AbstractShaftAdvancedSystemDeflection
    from ._7269 import AbstractShaftOrHousingAdvancedSystemDeflection
    from ._7270 import (
        AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection,
    )
    from ._7271 import AdvancedSystemDeflection
    from ._7272 import AdvancedSystemDeflectionOptions
    from ._7273 import AdvancedSystemDeflectionSubAnalysis
    from ._7274 import AGMAGleasonConicalGearAdvancedSystemDeflection
    from ._7275 import AGMAGleasonConicalGearMeshAdvancedSystemDeflection
    from ._7276 import AGMAGleasonConicalGearSetAdvancedSystemDeflection
    from ._7277 import AssemblyAdvancedSystemDeflection
    from ._7278 import BearingAdvancedSystemDeflection
    from ._7279 import BeltConnectionAdvancedSystemDeflection
    from ._7280 import BeltDriveAdvancedSystemDeflection
    from ._7281 import BevelDifferentialGearAdvancedSystemDeflection
    from ._7282 import BevelDifferentialGearMeshAdvancedSystemDeflection
    from ._7283 import BevelDifferentialGearSetAdvancedSystemDeflection
    from ._7284 import BevelDifferentialPlanetGearAdvancedSystemDeflection
    from ._7285 import BevelDifferentialSunGearAdvancedSystemDeflection
    from ._7286 import BevelGearAdvancedSystemDeflection
    from ._7287 import BevelGearMeshAdvancedSystemDeflection
    from ._7288 import BevelGearSetAdvancedSystemDeflection
    from ._7289 import BoltAdvancedSystemDeflection
    from ._7290 import BoltedJointAdvancedSystemDeflection
    from ._7291 import ClutchAdvancedSystemDeflection
    from ._7292 import ClutchConnectionAdvancedSystemDeflection
    from ._7293 import ClutchHalfAdvancedSystemDeflection
    from ._7294 import CoaxialConnectionAdvancedSystemDeflection
    from ._7295 import ComponentAdvancedSystemDeflection
    from ._7296 import ConceptCouplingAdvancedSystemDeflection
    from ._7297 import ConceptCouplingConnectionAdvancedSystemDeflection
    from ._7298 import ConceptCouplingHalfAdvancedSystemDeflection
    from ._7299 import ConceptGearAdvancedSystemDeflection
    from ._7300 import ConceptGearMeshAdvancedSystemDeflection
    from ._7301 import ConceptGearSetAdvancedSystemDeflection
    from ._7302 import ConicalGearAdvancedSystemDeflection
    from ._7303 import ConicalGearMeshAdvancedSystemDeflection
    from ._7304 import ConicalGearSetAdvancedSystemDeflection
    from ._7305 import ConnectionAdvancedSystemDeflection
    from ._7306 import ConnectorAdvancedSystemDeflection
    from ._7307 import ContactChartPerToothPass
    from ._7308 import CouplingAdvancedSystemDeflection
    from ._7309 import CouplingConnectionAdvancedSystemDeflection
    from ._7310 import CouplingHalfAdvancedSystemDeflection
    from ._7311 import CVTAdvancedSystemDeflection
    from ._7312 import CVTBeltConnectionAdvancedSystemDeflection
    from ._7313 import CVTPulleyAdvancedSystemDeflection
    from ._7314 import CycloidalAssemblyAdvancedSystemDeflection
    from ._7315 import CycloidalDiscAdvancedSystemDeflection
    from ._7316 import CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection
    from ._7317 import CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection
    from ._7318 import CylindricalGearAdvancedSystemDeflection
    from ._7319 import CylindricalGearMeshAdvancedSystemDeflection
    from ._7320 import CylindricalGearSetAdvancedSystemDeflection
    from ._7321 import CylindricalMeshedGearAdvancedSystemDeflection
    from ._7322 import CylindricalPlanetGearAdvancedSystemDeflection
    from ._7323 import DatumAdvancedSystemDeflection
    from ._7324 import ExternalCADModelAdvancedSystemDeflection
    from ._7325 import FaceGearAdvancedSystemDeflection
    from ._7326 import FaceGearMeshAdvancedSystemDeflection
    from ._7327 import FaceGearSetAdvancedSystemDeflection
    from ._7328 import FEPartAdvancedSystemDeflection
    from ._7329 import FlexiblePinAssemblyAdvancedSystemDeflection
    from ._7330 import GearAdvancedSystemDeflection
    from ._7331 import GearMeshAdvancedSystemDeflection
    from ._7332 import GearSetAdvancedSystemDeflection
    from ._7333 import GuideDxfModelAdvancedSystemDeflection
    from ._7334 import HypoidGearAdvancedSystemDeflection
    from ._7335 import HypoidGearMeshAdvancedSystemDeflection
    from ._7336 import HypoidGearSetAdvancedSystemDeflection
    from ._7337 import InterMountableComponentConnectionAdvancedSystemDeflection
    from ._7338 import KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection
    from ._7339 import KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection
    from ._7340 import KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection
    from ._7341 import KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection
    from ._7342 import KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection
    from ._7343 import KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection
    from ._7344 import KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection
    from ._7345 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection,
    )
    from ._7346 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection,
    )
    from ._7347 import UseLtcaInAsdOption
    from ._7348 import MassDiscAdvancedSystemDeflection
    from ._7349 import MeasurementComponentAdvancedSystemDeflection
    from ._7350 import MountableComponentAdvancedSystemDeflection
    from ._7351 import OilSealAdvancedSystemDeflection
    from ._7352 import PartAdvancedSystemDeflection
    from ._7353 import PartToPartShearCouplingAdvancedSystemDeflection
    from ._7354 import PartToPartShearCouplingConnectionAdvancedSystemDeflection
    from ._7355 import PartToPartShearCouplingHalfAdvancedSystemDeflection
    from ._7356 import PlanetaryConnectionAdvancedSystemDeflection
    from ._7357 import PlanetaryGearSetAdvancedSystemDeflection
    from ._7358 import PlanetCarrierAdvancedSystemDeflection
    from ._7359 import PointLoadAdvancedSystemDeflection
    from ._7360 import PowerLoadAdvancedSystemDeflection
    from ._7361 import PulleyAdvancedSystemDeflection
    from ._7362 import RingPinsAdvancedSystemDeflection
    from ._7363 import RingPinsToDiscConnectionAdvancedSystemDeflection
    from ._7364 import RollingRingAdvancedSystemDeflection
    from ._7365 import RollingRingAssemblyAdvancedSystemDeflection
    from ._7366 import RollingRingConnectionAdvancedSystemDeflection
    from ._7367 import RootAssemblyAdvancedSystemDeflection
    from ._7368 import ShaftAdvancedSystemDeflection
    from ._7369 import ShaftHubConnectionAdvancedSystemDeflection
    from ._7370 import ShaftToMountableComponentConnectionAdvancedSystemDeflection
    from ._7371 import SpecialisedAssemblyAdvancedSystemDeflection
    from ._7372 import SpiralBevelGearAdvancedSystemDeflection
    from ._7373 import SpiralBevelGearMeshAdvancedSystemDeflection
    from ._7374 import SpiralBevelGearSetAdvancedSystemDeflection
    from ._7375 import SpringDamperAdvancedSystemDeflection
    from ._7376 import SpringDamperConnectionAdvancedSystemDeflection
    from ._7377 import SpringDamperHalfAdvancedSystemDeflection
    from ._7378 import StraightBevelDiffGearAdvancedSystemDeflection
    from ._7379 import StraightBevelDiffGearMeshAdvancedSystemDeflection
    from ._7380 import StraightBevelDiffGearSetAdvancedSystemDeflection
    from ._7381 import StraightBevelGearAdvancedSystemDeflection
    from ._7382 import StraightBevelGearMeshAdvancedSystemDeflection
    from ._7383 import StraightBevelGearSetAdvancedSystemDeflection
    from ._7384 import StraightBevelPlanetGearAdvancedSystemDeflection
    from ._7385 import StraightBevelSunGearAdvancedSystemDeflection
    from ._7386 import SynchroniserAdvancedSystemDeflection
    from ._7387 import SynchroniserHalfAdvancedSystemDeflection
    from ._7388 import SynchroniserPartAdvancedSystemDeflection
    from ._7389 import SynchroniserSleeveAdvancedSystemDeflection
    from ._7390 import TorqueConverterAdvancedSystemDeflection
    from ._7391 import TorqueConverterConnectionAdvancedSystemDeflection
    from ._7392 import TorqueConverterPumpAdvancedSystemDeflection
    from ._7393 import TorqueConverterTurbineAdvancedSystemDeflection
    from ._7394 import TransmissionErrorToOtherPowerLoad
    from ._7395 import UnbalancedMassAdvancedSystemDeflection
    from ._7396 import VirtualComponentAdvancedSystemDeflection
    from ._7397 import WormGearAdvancedSystemDeflection
    from ._7398 import WormGearMeshAdvancedSystemDeflection
    from ._7399 import WormGearSetAdvancedSystemDeflection
    from ._7400 import ZerolBevelGearAdvancedSystemDeflection
    from ._7401 import ZerolBevelGearMeshAdvancedSystemDeflection
    from ._7402 import ZerolBevelGearSetAdvancedSystemDeflection
else:
    import_structure = {
        "_7267": ["AbstractAssemblyAdvancedSystemDeflection"],
        "_7268": ["AbstractShaftAdvancedSystemDeflection"],
        "_7269": ["AbstractShaftOrHousingAdvancedSystemDeflection"],
        "_7270": [
            "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection"
        ],
        "_7271": ["AdvancedSystemDeflection"],
        "_7272": ["AdvancedSystemDeflectionOptions"],
        "_7273": ["AdvancedSystemDeflectionSubAnalysis"],
        "_7274": ["AGMAGleasonConicalGearAdvancedSystemDeflection"],
        "_7275": ["AGMAGleasonConicalGearMeshAdvancedSystemDeflection"],
        "_7276": ["AGMAGleasonConicalGearSetAdvancedSystemDeflection"],
        "_7277": ["AssemblyAdvancedSystemDeflection"],
        "_7278": ["BearingAdvancedSystemDeflection"],
        "_7279": ["BeltConnectionAdvancedSystemDeflection"],
        "_7280": ["BeltDriveAdvancedSystemDeflection"],
        "_7281": ["BevelDifferentialGearAdvancedSystemDeflection"],
        "_7282": ["BevelDifferentialGearMeshAdvancedSystemDeflection"],
        "_7283": ["BevelDifferentialGearSetAdvancedSystemDeflection"],
        "_7284": ["BevelDifferentialPlanetGearAdvancedSystemDeflection"],
        "_7285": ["BevelDifferentialSunGearAdvancedSystemDeflection"],
        "_7286": ["BevelGearAdvancedSystemDeflection"],
        "_7287": ["BevelGearMeshAdvancedSystemDeflection"],
        "_7288": ["BevelGearSetAdvancedSystemDeflection"],
        "_7289": ["BoltAdvancedSystemDeflection"],
        "_7290": ["BoltedJointAdvancedSystemDeflection"],
        "_7291": ["ClutchAdvancedSystemDeflection"],
        "_7292": ["ClutchConnectionAdvancedSystemDeflection"],
        "_7293": ["ClutchHalfAdvancedSystemDeflection"],
        "_7294": ["CoaxialConnectionAdvancedSystemDeflection"],
        "_7295": ["ComponentAdvancedSystemDeflection"],
        "_7296": ["ConceptCouplingAdvancedSystemDeflection"],
        "_7297": ["ConceptCouplingConnectionAdvancedSystemDeflection"],
        "_7298": ["ConceptCouplingHalfAdvancedSystemDeflection"],
        "_7299": ["ConceptGearAdvancedSystemDeflection"],
        "_7300": ["ConceptGearMeshAdvancedSystemDeflection"],
        "_7301": ["ConceptGearSetAdvancedSystemDeflection"],
        "_7302": ["ConicalGearAdvancedSystemDeflection"],
        "_7303": ["ConicalGearMeshAdvancedSystemDeflection"],
        "_7304": ["ConicalGearSetAdvancedSystemDeflection"],
        "_7305": ["ConnectionAdvancedSystemDeflection"],
        "_7306": ["ConnectorAdvancedSystemDeflection"],
        "_7307": ["ContactChartPerToothPass"],
        "_7308": ["CouplingAdvancedSystemDeflection"],
        "_7309": ["CouplingConnectionAdvancedSystemDeflection"],
        "_7310": ["CouplingHalfAdvancedSystemDeflection"],
        "_7311": ["CVTAdvancedSystemDeflection"],
        "_7312": ["CVTBeltConnectionAdvancedSystemDeflection"],
        "_7313": ["CVTPulleyAdvancedSystemDeflection"],
        "_7314": ["CycloidalAssemblyAdvancedSystemDeflection"],
        "_7315": ["CycloidalDiscAdvancedSystemDeflection"],
        "_7316": ["CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection"],
        "_7317": ["CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection"],
        "_7318": ["CylindricalGearAdvancedSystemDeflection"],
        "_7319": ["CylindricalGearMeshAdvancedSystemDeflection"],
        "_7320": ["CylindricalGearSetAdvancedSystemDeflection"],
        "_7321": ["CylindricalMeshedGearAdvancedSystemDeflection"],
        "_7322": ["CylindricalPlanetGearAdvancedSystemDeflection"],
        "_7323": ["DatumAdvancedSystemDeflection"],
        "_7324": ["ExternalCADModelAdvancedSystemDeflection"],
        "_7325": ["FaceGearAdvancedSystemDeflection"],
        "_7326": ["FaceGearMeshAdvancedSystemDeflection"],
        "_7327": ["FaceGearSetAdvancedSystemDeflection"],
        "_7328": ["FEPartAdvancedSystemDeflection"],
        "_7329": ["FlexiblePinAssemblyAdvancedSystemDeflection"],
        "_7330": ["GearAdvancedSystemDeflection"],
        "_7331": ["GearMeshAdvancedSystemDeflection"],
        "_7332": ["GearSetAdvancedSystemDeflection"],
        "_7333": ["GuideDxfModelAdvancedSystemDeflection"],
        "_7334": ["HypoidGearAdvancedSystemDeflection"],
        "_7335": ["HypoidGearMeshAdvancedSystemDeflection"],
        "_7336": ["HypoidGearSetAdvancedSystemDeflection"],
        "_7337": ["InterMountableComponentConnectionAdvancedSystemDeflection"],
        "_7338": ["KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection"],
        "_7339": ["KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection"],
        "_7340": ["KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection"],
        "_7341": ["KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection"],
        "_7342": ["KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection"],
        "_7343": ["KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection"],
        "_7344": ["KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection"],
        "_7345": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection"
        ],
        "_7346": ["KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection"],
        "_7347": ["UseLtcaInAsdOption"],
        "_7348": ["MassDiscAdvancedSystemDeflection"],
        "_7349": ["MeasurementComponentAdvancedSystemDeflection"],
        "_7350": ["MountableComponentAdvancedSystemDeflection"],
        "_7351": ["OilSealAdvancedSystemDeflection"],
        "_7352": ["PartAdvancedSystemDeflection"],
        "_7353": ["PartToPartShearCouplingAdvancedSystemDeflection"],
        "_7354": ["PartToPartShearCouplingConnectionAdvancedSystemDeflection"],
        "_7355": ["PartToPartShearCouplingHalfAdvancedSystemDeflection"],
        "_7356": ["PlanetaryConnectionAdvancedSystemDeflection"],
        "_7357": ["PlanetaryGearSetAdvancedSystemDeflection"],
        "_7358": ["PlanetCarrierAdvancedSystemDeflection"],
        "_7359": ["PointLoadAdvancedSystemDeflection"],
        "_7360": ["PowerLoadAdvancedSystemDeflection"],
        "_7361": ["PulleyAdvancedSystemDeflection"],
        "_7362": ["RingPinsAdvancedSystemDeflection"],
        "_7363": ["RingPinsToDiscConnectionAdvancedSystemDeflection"],
        "_7364": ["RollingRingAdvancedSystemDeflection"],
        "_7365": ["RollingRingAssemblyAdvancedSystemDeflection"],
        "_7366": ["RollingRingConnectionAdvancedSystemDeflection"],
        "_7367": ["RootAssemblyAdvancedSystemDeflection"],
        "_7368": ["ShaftAdvancedSystemDeflection"],
        "_7369": ["ShaftHubConnectionAdvancedSystemDeflection"],
        "_7370": ["ShaftToMountableComponentConnectionAdvancedSystemDeflection"],
        "_7371": ["SpecialisedAssemblyAdvancedSystemDeflection"],
        "_7372": ["SpiralBevelGearAdvancedSystemDeflection"],
        "_7373": ["SpiralBevelGearMeshAdvancedSystemDeflection"],
        "_7374": ["SpiralBevelGearSetAdvancedSystemDeflection"],
        "_7375": ["SpringDamperAdvancedSystemDeflection"],
        "_7376": ["SpringDamperConnectionAdvancedSystemDeflection"],
        "_7377": ["SpringDamperHalfAdvancedSystemDeflection"],
        "_7378": ["StraightBevelDiffGearAdvancedSystemDeflection"],
        "_7379": ["StraightBevelDiffGearMeshAdvancedSystemDeflection"],
        "_7380": ["StraightBevelDiffGearSetAdvancedSystemDeflection"],
        "_7381": ["StraightBevelGearAdvancedSystemDeflection"],
        "_7382": ["StraightBevelGearMeshAdvancedSystemDeflection"],
        "_7383": ["StraightBevelGearSetAdvancedSystemDeflection"],
        "_7384": ["StraightBevelPlanetGearAdvancedSystemDeflection"],
        "_7385": ["StraightBevelSunGearAdvancedSystemDeflection"],
        "_7386": ["SynchroniserAdvancedSystemDeflection"],
        "_7387": ["SynchroniserHalfAdvancedSystemDeflection"],
        "_7388": ["SynchroniserPartAdvancedSystemDeflection"],
        "_7389": ["SynchroniserSleeveAdvancedSystemDeflection"],
        "_7390": ["TorqueConverterAdvancedSystemDeflection"],
        "_7391": ["TorqueConverterConnectionAdvancedSystemDeflection"],
        "_7392": ["TorqueConverterPumpAdvancedSystemDeflection"],
        "_7393": ["TorqueConverterTurbineAdvancedSystemDeflection"],
        "_7394": ["TransmissionErrorToOtherPowerLoad"],
        "_7395": ["UnbalancedMassAdvancedSystemDeflection"],
        "_7396": ["VirtualComponentAdvancedSystemDeflection"],
        "_7397": ["WormGearAdvancedSystemDeflection"],
        "_7398": ["WormGearMeshAdvancedSystemDeflection"],
        "_7399": ["WormGearSetAdvancedSystemDeflection"],
        "_7400": ["ZerolBevelGearAdvancedSystemDeflection"],
        "_7401": ["ZerolBevelGearMeshAdvancedSystemDeflection"],
        "_7402": ["ZerolBevelGearSetAdvancedSystemDeflection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyAdvancedSystemDeflection",
    "AbstractShaftAdvancedSystemDeflection",
    "AbstractShaftOrHousingAdvancedSystemDeflection",
    "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",
    "AdvancedSystemDeflection",
    "AdvancedSystemDeflectionOptions",
    "AdvancedSystemDeflectionSubAnalysis",
    "AGMAGleasonConicalGearAdvancedSystemDeflection",
    "AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
    "AGMAGleasonConicalGearSetAdvancedSystemDeflection",
    "AssemblyAdvancedSystemDeflection",
    "BearingAdvancedSystemDeflection",
    "BeltConnectionAdvancedSystemDeflection",
    "BeltDriveAdvancedSystemDeflection",
    "BevelDifferentialGearAdvancedSystemDeflection",
    "BevelDifferentialGearMeshAdvancedSystemDeflection",
    "BevelDifferentialGearSetAdvancedSystemDeflection",
    "BevelDifferentialPlanetGearAdvancedSystemDeflection",
    "BevelDifferentialSunGearAdvancedSystemDeflection",
    "BevelGearAdvancedSystemDeflection",
    "BevelGearMeshAdvancedSystemDeflection",
    "BevelGearSetAdvancedSystemDeflection",
    "BoltAdvancedSystemDeflection",
    "BoltedJointAdvancedSystemDeflection",
    "ClutchAdvancedSystemDeflection",
    "ClutchConnectionAdvancedSystemDeflection",
    "ClutchHalfAdvancedSystemDeflection",
    "CoaxialConnectionAdvancedSystemDeflection",
    "ComponentAdvancedSystemDeflection",
    "ConceptCouplingAdvancedSystemDeflection",
    "ConceptCouplingConnectionAdvancedSystemDeflection",
    "ConceptCouplingHalfAdvancedSystemDeflection",
    "ConceptGearAdvancedSystemDeflection",
    "ConceptGearMeshAdvancedSystemDeflection",
    "ConceptGearSetAdvancedSystemDeflection",
    "ConicalGearAdvancedSystemDeflection",
    "ConicalGearMeshAdvancedSystemDeflection",
    "ConicalGearSetAdvancedSystemDeflection",
    "ConnectionAdvancedSystemDeflection",
    "ConnectorAdvancedSystemDeflection",
    "ContactChartPerToothPass",
    "CouplingAdvancedSystemDeflection",
    "CouplingConnectionAdvancedSystemDeflection",
    "CouplingHalfAdvancedSystemDeflection",
    "CVTAdvancedSystemDeflection",
    "CVTBeltConnectionAdvancedSystemDeflection",
    "CVTPulleyAdvancedSystemDeflection",
    "CycloidalAssemblyAdvancedSystemDeflection",
    "CycloidalDiscAdvancedSystemDeflection",
    "CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection",
    "CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection",
    "CylindricalGearAdvancedSystemDeflection",
    "CylindricalGearMeshAdvancedSystemDeflection",
    "CylindricalGearSetAdvancedSystemDeflection",
    "CylindricalMeshedGearAdvancedSystemDeflection",
    "CylindricalPlanetGearAdvancedSystemDeflection",
    "DatumAdvancedSystemDeflection",
    "ExternalCADModelAdvancedSystemDeflection",
    "FaceGearAdvancedSystemDeflection",
    "FaceGearMeshAdvancedSystemDeflection",
    "FaceGearSetAdvancedSystemDeflection",
    "FEPartAdvancedSystemDeflection",
    "FlexiblePinAssemblyAdvancedSystemDeflection",
    "GearAdvancedSystemDeflection",
    "GearMeshAdvancedSystemDeflection",
    "GearSetAdvancedSystemDeflection",
    "GuideDxfModelAdvancedSystemDeflection",
    "HypoidGearAdvancedSystemDeflection",
    "HypoidGearMeshAdvancedSystemDeflection",
    "HypoidGearSetAdvancedSystemDeflection",
    "InterMountableComponentConnectionAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection",
    "UseLtcaInAsdOption",
    "MassDiscAdvancedSystemDeflection",
    "MeasurementComponentAdvancedSystemDeflection",
    "MountableComponentAdvancedSystemDeflection",
    "OilSealAdvancedSystemDeflection",
    "PartAdvancedSystemDeflection",
    "PartToPartShearCouplingAdvancedSystemDeflection",
    "PartToPartShearCouplingConnectionAdvancedSystemDeflection",
    "PartToPartShearCouplingHalfAdvancedSystemDeflection",
    "PlanetaryConnectionAdvancedSystemDeflection",
    "PlanetaryGearSetAdvancedSystemDeflection",
    "PlanetCarrierAdvancedSystemDeflection",
    "PointLoadAdvancedSystemDeflection",
    "PowerLoadAdvancedSystemDeflection",
    "PulleyAdvancedSystemDeflection",
    "RingPinsAdvancedSystemDeflection",
    "RingPinsToDiscConnectionAdvancedSystemDeflection",
    "RollingRingAdvancedSystemDeflection",
    "RollingRingAssemblyAdvancedSystemDeflection",
    "RollingRingConnectionAdvancedSystemDeflection",
    "RootAssemblyAdvancedSystemDeflection",
    "ShaftAdvancedSystemDeflection",
    "ShaftHubConnectionAdvancedSystemDeflection",
    "ShaftToMountableComponentConnectionAdvancedSystemDeflection",
    "SpecialisedAssemblyAdvancedSystemDeflection",
    "SpiralBevelGearAdvancedSystemDeflection",
    "SpiralBevelGearMeshAdvancedSystemDeflection",
    "SpiralBevelGearSetAdvancedSystemDeflection",
    "SpringDamperAdvancedSystemDeflection",
    "SpringDamperConnectionAdvancedSystemDeflection",
    "SpringDamperHalfAdvancedSystemDeflection",
    "StraightBevelDiffGearAdvancedSystemDeflection",
    "StraightBevelDiffGearMeshAdvancedSystemDeflection",
    "StraightBevelDiffGearSetAdvancedSystemDeflection",
    "StraightBevelGearAdvancedSystemDeflection",
    "StraightBevelGearMeshAdvancedSystemDeflection",
    "StraightBevelGearSetAdvancedSystemDeflection",
    "StraightBevelPlanetGearAdvancedSystemDeflection",
    "StraightBevelSunGearAdvancedSystemDeflection",
    "SynchroniserAdvancedSystemDeflection",
    "SynchroniserHalfAdvancedSystemDeflection",
    "SynchroniserPartAdvancedSystemDeflection",
    "SynchroniserSleeveAdvancedSystemDeflection",
    "TorqueConverterAdvancedSystemDeflection",
    "TorqueConverterConnectionAdvancedSystemDeflection",
    "TorqueConverterPumpAdvancedSystemDeflection",
    "TorqueConverterTurbineAdvancedSystemDeflection",
    "TransmissionErrorToOtherPowerLoad",
    "UnbalancedMassAdvancedSystemDeflection",
    "VirtualComponentAdvancedSystemDeflection",
    "WormGearAdvancedSystemDeflection",
    "WormGearMeshAdvancedSystemDeflection",
    "WormGearSetAdvancedSystemDeflection",
    "ZerolBevelGearAdvancedSystemDeflection",
    "ZerolBevelGearMeshAdvancedSystemDeflection",
    "ZerolBevelGearSetAdvancedSystemDeflection",
)
