"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7403 import AbstractAssemblyCompoundAdvancedSystemDeflection
    from ._7404 import AbstractShaftCompoundAdvancedSystemDeflection
    from ._7405 import AbstractShaftOrHousingCompoundAdvancedSystemDeflection
    from ._7406 import (
        AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection,
    )
    from ._7407 import AGMAGleasonConicalGearCompoundAdvancedSystemDeflection
    from ._7408 import AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection
    from ._7409 import AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection
    from ._7410 import AssemblyCompoundAdvancedSystemDeflection
    from ._7411 import BearingCompoundAdvancedSystemDeflection
    from ._7412 import BeltConnectionCompoundAdvancedSystemDeflection
    from ._7413 import BeltDriveCompoundAdvancedSystemDeflection
    from ._7414 import BevelDifferentialGearCompoundAdvancedSystemDeflection
    from ._7415 import BevelDifferentialGearMeshCompoundAdvancedSystemDeflection
    from ._7416 import BevelDifferentialGearSetCompoundAdvancedSystemDeflection
    from ._7417 import BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection
    from ._7418 import BevelDifferentialSunGearCompoundAdvancedSystemDeflection
    from ._7419 import BevelGearCompoundAdvancedSystemDeflection
    from ._7420 import BevelGearMeshCompoundAdvancedSystemDeflection
    from ._7421 import BevelGearSetCompoundAdvancedSystemDeflection
    from ._7422 import BoltCompoundAdvancedSystemDeflection
    from ._7423 import BoltedJointCompoundAdvancedSystemDeflection
    from ._7424 import ClutchCompoundAdvancedSystemDeflection
    from ._7425 import ClutchConnectionCompoundAdvancedSystemDeflection
    from ._7426 import ClutchHalfCompoundAdvancedSystemDeflection
    from ._7427 import CoaxialConnectionCompoundAdvancedSystemDeflection
    from ._7428 import ComponentCompoundAdvancedSystemDeflection
    from ._7429 import ConceptCouplingCompoundAdvancedSystemDeflection
    from ._7430 import ConceptCouplingConnectionCompoundAdvancedSystemDeflection
    from ._7431 import ConceptCouplingHalfCompoundAdvancedSystemDeflection
    from ._7432 import ConceptGearCompoundAdvancedSystemDeflection
    from ._7433 import ConceptGearMeshCompoundAdvancedSystemDeflection
    from ._7434 import ConceptGearSetCompoundAdvancedSystemDeflection
    from ._7435 import ConicalGearCompoundAdvancedSystemDeflection
    from ._7436 import ConicalGearMeshCompoundAdvancedSystemDeflection
    from ._7437 import ConicalGearSetCompoundAdvancedSystemDeflection
    from ._7438 import ConnectionCompoundAdvancedSystemDeflection
    from ._7439 import ConnectorCompoundAdvancedSystemDeflection
    from ._7440 import CouplingCompoundAdvancedSystemDeflection
    from ._7441 import CouplingConnectionCompoundAdvancedSystemDeflection
    from ._7442 import CouplingHalfCompoundAdvancedSystemDeflection
    from ._7443 import CVTBeltConnectionCompoundAdvancedSystemDeflection
    from ._7444 import CVTCompoundAdvancedSystemDeflection
    from ._7445 import CVTPulleyCompoundAdvancedSystemDeflection
    from ._7446 import CycloidalAssemblyCompoundAdvancedSystemDeflection
    from ._7447 import (
        CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection,
    )
    from ._7448 import CycloidalDiscCompoundAdvancedSystemDeflection
    from ._7449 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection,
    )
    from ._7450 import CylindricalGearCompoundAdvancedSystemDeflection
    from ._7451 import CylindricalGearMeshCompoundAdvancedSystemDeflection
    from ._7452 import CylindricalGearSetCompoundAdvancedSystemDeflection
    from ._7453 import CylindricalPlanetGearCompoundAdvancedSystemDeflection
    from ._7454 import DatumCompoundAdvancedSystemDeflection
    from ._7455 import ExternalCADModelCompoundAdvancedSystemDeflection
    from ._7456 import FaceGearCompoundAdvancedSystemDeflection
    from ._7457 import FaceGearMeshCompoundAdvancedSystemDeflection
    from ._7458 import FaceGearSetCompoundAdvancedSystemDeflection
    from ._7459 import FEPartCompoundAdvancedSystemDeflection
    from ._7460 import FlexiblePinAssemblyCompoundAdvancedSystemDeflection
    from ._7461 import GearCompoundAdvancedSystemDeflection
    from ._7462 import GearMeshCompoundAdvancedSystemDeflection
    from ._7463 import GearSetCompoundAdvancedSystemDeflection
    from ._7464 import GuideDxfModelCompoundAdvancedSystemDeflection
    from ._7465 import HypoidGearCompoundAdvancedSystemDeflection
    from ._7466 import HypoidGearMeshCompoundAdvancedSystemDeflection
    from ._7467 import HypoidGearSetCompoundAdvancedSystemDeflection
    from ._7468 import InterMountableComponentConnectionCompoundAdvancedSystemDeflection
    from ._7469 import (
        KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection,
    )
    from ._7470 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection,
    )
    from ._7471 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection,
    )
    from ._7472 import (
        KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection,
    )
    from ._7473 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection,
    )
    from ._7474 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection,
    )
    from ._7475 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection,
    )
    from ._7476 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection,
    )
    from ._7477 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection,
    )
    from ._7478 import MassDiscCompoundAdvancedSystemDeflection
    from ._7479 import MeasurementComponentCompoundAdvancedSystemDeflection
    from ._7480 import MountableComponentCompoundAdvancedSystemDeflection
    from ._7481 import OilSealCompoundAdvancedSystemDeflection
    from ._7482 import PartCompoundAdvancedSystemDeflection
    from ._7483 import PartToPartShearCouplingCompoundAdvancedSystemDeflection
    from ._7484 import PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection
    from ._7485 import PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection
    from ._7486 import PlanetaryConnectionCompoundAdvancedSystemDeflection
    from ._7487 import PlanetaryGearSetCompoundAdvancedSystemDeflection
    from ._7488 import PlanetCarrierCompoundAdvancedSystemDeflection
    from ._7489 import PointLoadCompoundAdvancedSystemDeflection
    from ._7490 import PowerLoadCompoundAdvancedSystemDeflection
    from ._7491 import PulleyCompoundAdvancedSystemDeflection
    from ._7492 import RingPinsCompoundAdvancedSystemDeflection
    from ._7493 import RingPinsToDiscConnectionCompoundAdvancedSystemDeflection
    from ._7494 import RollingRingAssemblyCompoundAdvancedSystemDeflection
    from ._7495 import RollingRingCompoundAdvancedSystemDeflection
    from ._7496 import RollingRingConnectionCompoundAdvancedSystemDeflection
    from ._7497 import RootAssemblyCompoundAdvancedSystemDeflection
    from ._7498 import ShaftCompoundAdvancedSystemDeflection
    from ._7499 import ShaftHubConnectionCompoundAdvancedSystemDeflection
    from ._7500 import (
        ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection,
    )
    from ._7501 import SpecialisedAssemblyCompoundAdvancedSystemDeflection
    from ._7502 import SpiralBevelGearCompoundAdvancedSystemDeflection
    from ._7503 import SpiralBevelGearMeshCompoundAdvancedSystemDeflection
    from ._7504 import SpiralBevelGearSetCompoundAdvancedSystemDeflection
    from ._7505 import SpringDamperCompoundAdvancedSystemDeflection
    from ._7506 import SpringDamperConnectionCompoundAdvancedSystemDeflection
    from ._7507 import SpringDamperHalfCompoundAdvancedSystemDeflection
    from ._7508 import StraightBevelDiffGearCompoundAdvancedSystemDeflection
    from ._7509 import StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection
    from ._7510 import StraightBevelDiffGearSetCompoundAdvancedSystemDeflection
    from ._7511 import StraightBevelGearCompoundAdvancedSystemDeflection
    from ._7512 import StraightBevelGearMeshCompoundAdvancedSystemDeflection
    from ._7513 import StraightBevelGearSetCompoundAdvancedSystemDeflection
    from ._7514 import StraightBevelPlanetGearCompoundAdvancedSystemDeflection
    from ._7515 import StraightBevelSunGearCompoundAdvancedSystemDeflection
    from ._7516 import SynchroniserCompoundAdvancedSystemDeflection
    from ._7517 import SynchroniserHalfCompoundAdvancedSystemDeflection
    from ._7518 import SynchroniserPartCompoundAdvancedSystemDeflection
    from ._7519 import SynchroniserSleeveCompoundAdvancedSystemDeflection
    from ._7520 import TorqueConverterCompoundAdvancedSystemDeflection
    from ._7521 import TorqueConverterConnectionCompoundAdvancedSystemDeflection
    from ._7522 import TorqueConverterPumpCompoundAdvancedSystemDeflection
    from ._7523 import TorqueConverterTurbineCompoundAdvancedSystemDeflection
    from ._7524 import UnbalancedMassCompoundAdvancedSystemDeflection
    from ._7525 import VirtualComponentCompoundAdvancedSystemDeflection
    from ._7526 import WormGearCompoundAdvancedSystemDeflection
    from ._7527 import WormGearMeshCompoundAdvancedSystemDeflection
    from ._7528 import WormGearSetCompoundAdvancedSystemDeflection
    from ._7529 import ZerolBevelGearCompoundAdvancedSystemDeflection
    from ._7530 import ZerolBevelGearMeshCompoundAdvancedSystemDeflection
    from ._7531 import ZerolBevelGearSetCompoundAdvancedSystemDeflection
else:
    import_structure = {
        "_7403": ["AbstractAssemblyCompoundAdvancedSystemDeflection"],
        "_7404": ["AbstractShaftCompoundAdvancedSystemDeflection"],
        "_7405": ["AbstractShaftOrHousingCompoundAdvancedSystemDeflection"],
        "_7406": [
            "AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection"
        ],
        "_7407": ["AGMAGleasonConicalGearCompoundAdvancedSystemDeflection"],
        "_7408": ["AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection"],
        "_7409": ["AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection"],
        "_7410": ["AssemblyCompoundAdvancedSystemDeflection"],
        "_7411": ["BearingCompoundAdvancedSystemDeflection"],
        "_7412": ["BeltConnectionCompoundAdvancedSystemDeflection"],
        "_7413": ["BeltDriveCompoundAdvancedSystemDeflection"],
        "_7414": ["BevelDifferentialGearCompoundAdvancedSystemDeflection"],
        "_7415": ["BevelDifferentialGearMeshCompoundAdvancedSystemDeflection"],
        "_7416": ["BevelDifferentialGearSetCompoundAdvancedSystemDeflection"],
        "_7417": ["BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection"],
        "_7418": ["BevelDifferentialSunGearCompoundAdvancedSystemDeflection"],
        "_7419": ["BevelGearCompoundAdvancedSystemDeflection"],
        "_7420": ["BevelGearMeshCompoundAdvancedSystemDeflection"],
        "_7421": ["BevelGearSetCompoundAdvancedSystemDeflection"],
        "_7422": ["BoltCompoundAdvancedSystemDeflection"],
        "_7423": ["BoltedJointCompoundAdvancedSystemDeflection"],
        "_7424": ["ClutchCompoundAdvancedSystemDeflection"],
        "_7425": ["ClutchConnectionCompoundAdvancedSystemDeflection"],
        "_7426": ["ClutchHalfCompoundAdvancedSystemDeflection"],
        "_7427": ["CoaxialConnectionCompoundAdvancedSystemDeflection"],
        "_7428": ["ComponentCompoundAdvancedSystemDeflection"],
        "_7429": ["ConceptCouplingCompoundAdvancedSystemDeflection"],
        "_7430": ["ConceptCouplingConnectionCompoundAdvancedSystemDeflection"],
        "_7431": ["ConceptCouplingHalfCompoundAdvancedSystemDeflection"],
        "_7432": ["ConceptGearCompoundAdvancedSystemDeflection"],
        "_7433": ["ConceptGearMeshCompoundAdvancedSystemDeflection"],
        "_7434": ["ConceptGearSetCompoundAdvancedSystemDeflection"],
        "_7435": ["ConicalGearCompoundAdvancedSystemDeflection"],
        "_7436": ["ConicalGearMeshCompoundAdvancedSystemDeflection"],
        "_7437": ["ConicalGearSetCompoundAdvancedSystemDeflection"],
        "_7438": ["ConnectionCompoundAdvancedSystemDeflection"],
        "_7439": ["ConnectorCompoundAdvancedSystemDeflection"],
        "_7440": ["CouplingCompoundAdvancedSystemDeflection"],
        "_7441": ["CouplingConnectionCompoundAdvancedSystemDeflection"],
        "_7442": ["CouplingHalfCompoundAdvancedSystemDeflection"],
        "_7443": ["CVTBeltConnectionCompoundAdvancedSystemDeflection"],
        "_7444": ["CVTCompoundAdvancedSystemDeflection"],
        "_7445": ["CVTPulleyCompoundAdvancedSystemDeflection"],
        "_7446": ["CycloidalAssemblyCompoundAdvancedSystemDeflection"],
        "_7447": [
            "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection"
        ],
        "_7448": ["CycloidalDiscCompoundAdvancedSystemDeflection"],
        "_7449": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection"
        ],
        "_7450": ["CylindricalGearCompoundAdvancedSystemDeflection"],
        "_7451": ["CylindricalGearMeshCompoundAdvancedSystemDeflection"],
        "_7452": ["CylindricalGearSetCompoundAdvancedSystemDeflection"],
        "_7453": ["CylindricalPlanetGearCompoundAdvancedSystemDeflection"],
        "_7454": ["DatumCompoundAdvancedSystemDeflection"],
        "_7455": ["ExternalCADModelCompoundAdvancedSystemDeflection"],
        "_7456": ["FaceGearCompoundAdvancedSystemDeflection"],
        "_7457": ["FaceGearMeshCompoundAdvancedSystemDeflection"],
        "_7458": ["FaceGearSetCompoundAdvancedSystemDeflection"],
        "_7459": ["FEPartCompoundAdvancedSystemDeflection"],
        "_7460": ["FlexiblePinAssemblyCompoundAdvancedSystemDeflection"],
        "_7461": ["GearCompoundAdvancedSystemDeflection"],
        "_7462": ["GearMeshCompoundAdvancedSystemDeflection"],
        "_7463": ["GearSetCompoundAdvancedSystemDeflection"],
        "_7464": ["GuideDxfModelCompoundAdvancedSystemDeflection"],
        "_7465": ["HypoidGearCompoundAdvancedSystemDeflection"],
        "_7466": ["HypoidGearMeshCompoundAdvancedSystemDeflection"],
        "_7467": ["HypoidGearSetCompoundAdvancedSystemDeflection"],
        "_7468": ["InterMountableComponentConnectionCompoundAdvancedSystemDeflection"],
        "_7469": [
            "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection"
        ],
        "_7470": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection"
        ],
        "_7471": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection"
        ],
        "_7472": ["KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection"],
        "_7473": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection"
        ],
        "_7474": [
            "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection"
        ],
        "_7475": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection"
        ],
        "_7476": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection"
        ],
        "_7477": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection"
        ],
        "_7478": ["MassDiscCompoundAdvancedSystemDeflection"],
        "_7479": ["MeasurementComponentCompoundAdvancedSystemDeflection"],
        "_7480": ["MountableComponentCompoundAdvancedSystemDeflection"],
        "_7481": ["OilSealCompoundAdvancedSystemDeflection"],
        "_7482": ["PartCompoundAdvancedSystemDeflection"],
        "_7483": ["PartToPartShearCouplingCompoundAdvancedSystemDeflection"],
        "_7484": ["PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection"],
        "_7485": ["PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection"],
        "_7486": ["PlanetaryConnectionCompoundAdvancedSystemDeflection"],
        "_7487": ["PlanetaryGearSetCompoundAdvancedSystemDeflection"],
        "_7488": ["PlanetCarrierCompoundAdvancedSystemDeflection"],
        "_7489": ["PointLoadCompoundAdvancedSystemDeflection"],
        "_7490": ["PowerLoadCompoundAdvancedSystemDeflection"],
        "_7491": ["PulleyCompoundAdvancedSystemDeflection"],
        "_7492": ["RingPinsCompoundAdvancedSystemDeflection"],
        "_7493": ["RingPinsToDiscConnectionCompoundAdvancedSystemDeflection"],
        "_7494": ["RollingRingAssemblyCompoundAdvancedSystemDeflection"],
        "_7495": ["RollingRingCompoundAdvancedSystemDeflection"],
        "_7496": ["RollingRingConnectionCompoundAdvancedSystemDeflection"],
        "_7497": ["RootAssemblyCompoundAdvancedSystemDeflection"],
        "_7498": ["ShaftCompoundAdvancedSystemDeflection"],
        "_7499": ["ShaftHubConnectionCompoundAdvancedSystemDeflection"],
        "_7500": [
            "ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection"
        ],
        "_7501": ["SpecialisedAssemblyCompoundAdvancedSystemDeflection"],
        "_7502": ["SpiralBevelGearCompoundAdvancedSystemDeflection"],
        "_7503": ["SpiralBevelGearMeshCompoundAdvancedSystemDeflection"],
        "_7504": ["SpiralBevelGearSetCompoundAdvancedSystemDeflection"],
        "_7505": ["SpringDamperCompoundAdvancedSystemDeflection"],
        "_7506": ["SpringDamperConnectionCompoundAdvancedSystemDeflection"],
        "_7507": ["SpringDamperHalfCompoundAdvancedSystemDeflection"],
        "_7508": ["StraightBevelDiffGearCompoundAdvancedSystemDeflection"],
        "_7509": ["StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection"],
        "_7510": ["StraightBevelDiffGearSetCompoundAdvancedSystemDeflection"],
        "_7511": ["StraightBevelGearCompoundAdvancedSystemDeflection"],
        "_7512": ["StraightBevelGearMeshCompoundAdvancedSystemDeflection"],
        "_7513": ["StraightBevelGearSetCompoundAdvancedSystemDeflection"],
        "_7514": ["StraightBevelPlanetGearCompoundAdvancedSystemDeflection"],
        "_7515": ["StraightBevelSunGearCompoundAdvancedSystemDeflection"],
        "_7516": ["SynchroniserCompoundAdvancedSystemDeflection"],
        "_7517": ["SynchroniserHalfCompoundAdvancedSystemDeflection"],
        "_7518": ["SynchroniserPartCompoundAdvancedSystemDeflection"],
        "_7519": ["SynchroniserSleeveCompoundAdvancedSystemDeflection"],
        "_7520": ["TorqueConverterCompoundAdvancedSystemDeflection"],
        "_7521": ["TorqueConverterConnectionCompoundAdvancedSystemDeflection"],
        "_7522": ["TorqueConverterPumpCompoundAdvancedSystemDeflection"],
        "_7523": ["TorqueConverterTurbineCompoundAdvancedSystemDeflection"],
        "_7524": ["UnbalancedMassCompoundAdvancedSystemDeflection"],
        "_7525": ["VirtualComponentCompoundAdvancedSystemDeflection"],
        "_7526": ["WormGearCompoundAdvancedSystemDeflection"],
        "_7527": ["WormGearMeshCompoundAdvancedSystemDeflection"],
        "_7528": ["WormGearSetCompoundAdvancedSystemDeflection"],
        "_7529": ["ZerolBevelGearCompoundAdvancedSystemDeflection"],
        "_7530": ["ZerolBevelGearMeshCompoundAdvancedSystemDeflection"],
        "_7531": ["ZerolBevelGearSetCompoundAdvancedSystemDeflection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundAdvancedSystemDeflection",
    "AbstractShaftCompoundAdvancedSystemDeflection",
    "AbstractShaftOrHousingCompoundAdvancedSystemDeflection",
    "AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
    "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
    "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
    "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
    "AssemblyCompoundAdvancedSystemDeflection",
    "BearingCompoundAdvancedSystemDeflection",
    "BeltConnectionCompoundAdvancedSystemDeflection",
    "BeltDriveCompoundAdvancedSystemDeflection",
    "BevelDifferentialGearCompoundAdvancedSystemDeflection",
    "BevelDifferentialGearMeshCompoundAdvancedSystemDeflection",
    "BevelDifferentialGearSetCompoundAdvancedSystemDeflection",
    "BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection",
    "BevelDifferentialSunGearCompoundAdvancedSystemDeflection",
    "BevelGearCompoundAdvancedSystemDeflection",
    "BevelGearMeshCompoundAdvancedSystemDeflection",
    "BevelGearSetCompoundAdvancedSystemDeflection",
    "BoltCompoundAdvancedSystemDeflection",
    "BoltedJointCompoundAdvancedSystemDeflection",
    "ClutchCompoundAdvancedSystemDeflection",
    "ClutchConnectionCompoundAdvancedSystemDeflection",
    "ClutchHalfCompoundAdvancedSystemDeflection",
    "CoaxialConnectionCompoundAdvancedSystemDeflection",
    "ComponentCompoundAdvancedSystemDeflection",
    "ConceptCouplingCompoundAdvancedSystemDeflection",
    "ConceptCouplingConnectionCompoundAdvancedSystemDeflection",
    "ConceptCouplingHalfCompoundAdvancedSystemDeflection",
    "ConceptGearCompoundAdvancedSystemDeflection",
    "ConceptGearMeshCompoundAdvancedSystemDeflection",
    "ConceptGearSetCompoundAdvancedSystemDeflection",
    "ConicalGearCompoundAdvancedSystemDeflection",
    "ConicalGearMeshCompoundAdvancedSystemDeflection",
    "ConicalGearSetCompoundAdvancedSystemDeflection",
    "ConnectionCompoundAdvancedSystemDeflection",
    "ConnectorCompoundAdvancedSystemDeflection",
    "CouplingCompoundAdvancedSystemDeflection",
    "CouplingConnectionCompoundAdvancedSystemDeflection",
    "CouplingHalfCompoundAdvancedSystemDeflection",
    "CVTBeltConnectionCompoundAdvancedSystemDeflection",
    "CVTCompoundAdvancedSystemDeflection",
    "CVTPulleyCompoundAdvancedSystemDeflection",
    "CycloidalAssemblyCompoundAdvancedSystemDeflection",
    "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection",
    "CycloidalDiscCompoundAdvancedSystemDeflection",
    "CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection",
    "CylindricalGearCompoundAdvancedSystemDeflection",
    "CylindricalGearMeshCompoundAdvancedSystemDeflection",
    "CylindricalGearSetCompoundAdvancedSystemDeflection",
    "CylindricalPlanetGearCompoundAdvancedSystemDeflection",
    "DatumCompoundAdvancedSystemDeflection",
    "ExternalCADModelCompoundAdvancedSystemDeflection",
    "FaceGearCompoundAdvancedSystemDeflection",
    "FaceGearMeshCompoundAdvancedSystemDeflection",
    "FaceGearSetCompoundAdvancedSystemDeflection",
    "FEPartCompoundAdvancedSystemDeflection",
    "FlexiblePinAssemblyCompoundAdvancedSystemDeflection",
    "GearCompoundAdvancedSystemDeflection",
    "GearMeshCompoundAdvancedSystemDeflection",
    "GearSetCompoundAdvancedSystemDeflection",
    "GuideDxfModelCompoundAdvancedSystemDeflection",
    "HypoidGearCompoundAdvancedSystemDeflection",
    "HypoidGearMeshCompoundAdvancedSystemDeflection",
    "HypoidGearSetCompoundAdvancedSystemDeflection",
    "InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection",
    "MassDiscCompoundAdvancedSystemDeflection",
    "MeasurementComponentCompoundAdvancedSystemDeflection",
    "MountableComponentCompoundAdvancedSystemDeflection",
    "OilSealCompoundAdvancedSystemDeflection",
    "PartCompoundAdvancedSystemDeflection",
    "PartToPartShearCouplingCompoundAdvancedSystemDeflection",
    "PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection",
    "PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection",
    "PlanetaryConnectionCompoundAdvancedSystemDeflection",
    "PlanetaryGearSetCompoundAdvancedSystemDeflection",
    "PlanetCarrierCompoundAdvancedSystemDeflection",
    "PointLoadCompoundAdvancedSystemDeflection",
    "PowerLoadCompoundAdvancedSystemDeflection",
    "PulleyCompoundAdvancedSystemDeflection",
    "RingPinsCompoundAdvancedSystemDeflection",
    "RingPinsToDiscConnectionCompoundAdvancedSystemDeflection",
    "RollingRingAssemblyCompoundAdvancedSystemDeflection",
    "RollingRingCompoundAdvancedSystemDeflection",
    "RollingRingConnectionCompoundAdvancedSystemDeflection",
    "RootAssemblyCompoundAdvancedSystemDeflection",
    "ShaftCompoundAdvancedSystemDeflection",
    "ShaftHubConnectionCompoundAdvancedSystemDeflection",
    "ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
    "SpecialisedAssemblyCompoundAdvancedSystemDeflection",
    "SpiralBevelGearCompoundAdvancedSystemDeflection",
    "SpiralBevelGearMeshCompoundAdvancedSystemDeflection",
    "SpiralBevelGearSetCompoundAdvancedSystemDeflection",
    "SpringDamperCompoundAdvancedSystemDeflection",
    "SpringDamperConnectionCompoundAdvancedSystemDeflection",
    "SpringDamperHalfCompoundAdvancedSystemDeflection",
    "StraightBevelDiffGearCompoundAdvancedSystemDeflection",
    "StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection",
    "StraightBevelDiffGearSetCompoundAdvancedSystemDeflection",
    "StraightBevelGearCompoundAdvancedSystemDeflection",
    "StraightBevelGearMeshCompoundAdvancedSystemDeflection",
    "StraightBevelGearSetCompoundAdvancedSystemDeflection",
    "StraightBevelPlanetGearCompoundAdvancedSystemDeflection",
    "StraightBevelSunGearCompoundAdvancedSystemDeflection",
    "SynchroniserCompoundAdvancedSystemDeflection",
    "SynchroniserHalfCompoundAdvancedSystemDeflection",
    "SynchroniserPartCompoundAdvancedSystemDeflection",
    "SynchroniserSleeveCompoundAdvancedSystemDeflection",
    "TorqueConverterCompoundAdvancedSystemDeflection",
    "TorqueConverterConnectionCompoundAdvancedSystemDeflection",
    "TorqueConverterPumpCompoundAdvancedSystemDeflection",
    "TorqueConverterTurbineCompoundAdvancedSystemDeflection",
    "UnbalancedMassCompoundAdvancedSystemDeflection",
    "VirtualComponentCompoundAdvancedSystemDeflection",
    "WormGearCompoundAdvancedSystemDeflection",
    "WormGearMeshCompoundAdvancedSystemDeflection",
    "WormGearSetCompoundAdvancedSystemDeflection",
    "ZerolBevelGearCompoundAdvancedSystemDeflection",
    "ZerolBevelGearMeshCompoundAdvancedSystemDeflection",
    "ZerolBevelGearSetCompoundAdvancedSystemDeflection",
)
