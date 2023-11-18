"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4440 import AbstractAssemblyCompoundParametricStudyTool
    from ._4441 import AbstractShaftCompoundParametricStudyTool
    from ._4442 import AbstractShaftOrHousingCompoundParametricStudyTool
    from ._4443 import (
        AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool,
    )
    from ._4444 import AGMAGleasonConicalGearCompoundParametricStudyTool
    from ._4445 import AGMAGleasonConicalGearMeshCompoundParametricStudyTool
    from ._4446 import AGMAGleasonConicalGearSetCompoundParametricStudyTool
    from ._4447 import AssemblyCompoundParametricStudyTool
    from ._4448 import BearingCompoundParametricStudyTool
    from ._4449 import BeltConnectionCompoundParametricStudyTool
    from ._4450 import BeltDriveCompoundParametricStudyTool
    from ._4451 import BevelDifferentialGearCompoundParametricStudyTool
    from ._4452 import BevelDifferentialGearMeshCompoundParametricStudyTool
    from ._4453 import BevelDifferentialGearSetCompoundParametricStudyTool
    from ._4454 import BevelDifferentialPlanetGearCompoundParametricStudyTool
    from ._4455 import BevelDifferentialSunGearCompoundParametricStudyTool
    from ._4456 import BevelGearCompoundParametricStudyTool
    from ._4457 import BevelGearMeshCompoundParametricStudyTool
    from ._4458 import BevelGearSetCompoundParametricStudyTool
    from ._4459 import BoltCompoundParametricStudyTool
    from ._4460 import BoltedJointCompoundParametricStudyTool
    from ._4461 import ClutchCompoundParametricStudyTool
    from ._4462 import ClutchConnectionCompoundParametricStudyTool
    from ._4463 import ClutchHalfCompoundParametricStudyTool
    from ._4464 import CoaxialConnectionCompoundParametricStudyTool
    from ._4465 import ComponentCompoundParametricStudyTool
    from ._4466 import ConceptCouplingCompoundParametricStudyTool
    from ._4467 import ConceptCouplingConnectionCompoundParametricStudyTool
    from ._4468 import ConceptCouplingHalfCompoundParametricStudyTool
    from ._4469 import ConceptGearCompoundParametricStudyTool
    from ._4470 import ConceptGearMeshCompoundParametricStudyTool
    from ._4471 import ConceptGearSetCompoundParametricStudyTool
    from ._4472 import ConicalGearCompoundParametricStudyTool
    from ._4473 import ConicalGearMeshCompoundParametricStudyTool
    from ._4474 import ConicalGearSetCompoundParametricStudyTool
    from ._4475 import ConnectionCompoundParametricStudyTool
    from ._4476 import ConnectorCompoundParametricStudyTool
    from ._4477 import CouplingCompoundParametricStudyTool
    from ._4478 import CouplingConnectionCompoundParametricStudyTool
    from ._4479 import CouplingHalfCompoundParametricStudyTool
    from ._4480 import CVTBeltConnectionCompoundParametricStudyTool
    from ._4481 import CVTCompoundParametricStudyTool
    from ._4482 import CVTPulleyCompoundParametricStudyTool
    from ._4483 import CycloidalAssemblyCompoundParametricStudyTool
    from ._4484 import CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool
    from ._4485 import CycloidalDiscCompoundParametricStudyTool
    from ._4486 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundParametricStudyTool,
    )
    from ._4487 import CylindricalGearCompoundParametricStudyTool
    from ._4488 import CylindricalGearMeshCompoundParametricStudyTool
    from ._4489 import CylindricalGearSetCompoundParametricStudyTool
    from ._4490 import CylindricalPlanetGearCompoundParametricStudyTool
    from ._4491 import DatumCompoundParametricStudyTool
    from ._4492 import ExternalCADModelCompoundParametricStudyTool
    from ._4493 import FaceGearCompoundParametricStudyTool
    from ._4494 import FaceGearMeshCompoundParametricStudyTool
    from ._4495 import FaceGearSetCompoundParametricStudyTool
    from ._4496 import FEPartCompoundParametricStudyTool
    from ._4497 import FlexiblePinAssemblyCompoundParametricStudyTool
    from ._4498 import GearCompoundParametricStudyTool
    from ._4499 import GearMeshCompoundParametricStudyTool
    from ._4500 import GearSetCompoundParametricStudyTool
    from ._4501 import GuideDxfModelCompoundParametricStudyTool
    from ._4502 import HypoidGearCompoundParametricStudyTool
    from ._4503 import HypoidGearMeshCompoundParametricStudyTool
    from ._4504 import HypoidGearSetCompoundParametricStudyTool
    from ._4505 import InterMountableComponentConnectionCompoundParametricStudyTool
    from ._4506 import KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool
    from ._4507 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool,
    )
    from ._4508 import KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool
    from ._4509 import KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool
    from ._4510 import KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool
    from ._4511 import KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool
    from ._4512 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool,
    )
    from ._4513 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool,
    )
    from ._4514 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool,
    )
    from ._4515 import MassDiscCompoundParametricStudyTool
    from ._4516 import MeasurementComponentCompoundParametricStudyTool
    from ._4517 import MountableComponentCompoundParametricStudyTool
    from ._4518 import OilSealCompoundParametricStudyTool
    from ._4519 import PartCompoundParametricStudyTool
    from ._4520 import PartToPartShearCouplingCompoundParametricStudyTool
    from ._4521 import PartToPartShearCouplingConnectionCompoundParametricStudyTool
    from ._4522 import PartToPartShearCouplingHalfCompoundParametricStudyTool
    from ._4523 import PlanetaryConnectionCompoundParametricStudyTool
    from ._4524 import PlanetaryGearSetCompoundParametricStudyTool
    from ._4525 import PlanetCarrierCompoundParametricStudyTool
    from ._4526 import PointLoadCompoundParametricStudyTool
    from ._4527 import PowerLoadCompoundParametricStudyTool
    from ._4528 import PulleyCompoundParametricStudyTool
    from ._4529 import RingPinsCompoundParametricStudyTool
    from ._4530 import RingPinsToDiscConnectionCompoundParametricStudyTool
    from ._4531 import RollingRingAssemblyCompoundParametricStudyTool
    from ._4532 import RollingRingCompoundParametricStudyTool
    from ._4533 import RollingRingConnectionCompoundParametricStudyTool
    from ._4534 import RootAssemblyCompoundParametricStudyTool
    from ._4535 import ShaftCompoundParametricStudyTool
    from ._4536 import ShaftHubConnectionCompoundParametricStudyTool
    from ._4537 import ShaftToMountableComponentConnectionCompoundParametricStudyTool
    from ._4538 import SpecialisedAssemblyCompoundParametricStudyTool
    from ._4539 import SpiralBevelGearCompoundParametricStudyTool
    from ._4540 import SpiralBevelGearMeshCompoundParametricStudyTool
    from ._4541 import SpiralBevelGearSetCompoundParametricStudyTool
    from ._4542 import SpringDamperCompoundParametricStudyTool
    from ._4543 import SpringDamperConnectionCompoundParametricStudyTool
    from ._4544 import SpringDamperHalfCompoundParametricStudyTool
    from ._4545 import StraightBevelDiffGearCompoundParametricStudyTool
    from ._4546 import StraightBevelDiffGearMeshCompoundParametricStudyTool
    from ._4547 import StraightBevelDiffGearSetCompoundParametricStudyTool
    from ._4548 import StraightBevelGearCompoundParametricStudyTool
    from ._4549 import StraightBevelGearMeshCompoundParametricStudyTool
    from ._4550 import StraightBevelGearSetCompoundParametricStudyTool
    from ._4551 import StraightBevelPlanetGearCompoundParametricStudyTool
    from ._4552 import StraightBevelSunGearCompoundParametricStudyTool
    from ._4553 import SynchroniserCompoundParametricStudyTool
    from ._4554 import SynchroniserHalfCompoundParametricStudyTool
    from ._4555 import SynchroniserPartCompoundParametricStudyTool
    from ._4556 import SynchroniserSleeveCompoundParametricStudyTool
    from ._4557 import TorqueConverterCompoundParametricStudyTool
    from ._4558 import TorqueConverterConnectionCompoundParametricStudyTool
    from ._4559 import TorqueConverterPumpCompoundParametricStudyTool
    from ._4560 import TorqueConverterTurbineCompoundParametricStudyTool
    from ._4561 import UnbalancedMassCompoundParametricStudyTool
    from ._4562 import VirtualComponentCompoundParametricStudyTool
    from ._4563 import WormGearCompoundParametricStudyTool
    from ._4564 import WormGearMeshCompoundParametricStudyTool
    from ._4565 import WormGearSetCompoundParametricStudyTool
    from ._4566 import ZerolBevelGearCompoundParametricStudyTool
    from ._4567 import ZerolBevelGearMeshCompoundParametricStudyTool
    from ._4568 import ZerolBevelGearSetCompoundParametricStudyTool
else:
    import_structure = {
        "_4440": ["AbstractAssemblyCompoundParametricStudyTool"],
        "_4441": ["AbstractShaftCompoundParametricStudyTool"],
        "_4442": ["AbstractShaftOrHousingCompoundParametricStudyTool"],
        "_4443": [
            "AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool"
        ],
        "_4444": ["AGMAGleasonConicalGearCompoundParametricStudyTool"],
        "_4445": ["AGMAGleasonConicalGearMeshCompoundParametricStudyTool"],
        "_4446": ["AGMAGleasonConicalGearSetCompoundParametricStudyTool"],
        "_4447": ["AssemblyCompoundParametricStudyTool"],
        "_4448": ["BearingCompoundParametricStudyTool"],
        "_4449": ["BeltConnectionCompoundParametricStudyTool"],
        "_4450": ["BeltDriveCompoundParametricStudyTool"],
        "_4451": ["BevelDifferentialGearCompoundParametricStudyTool"],
        "_4452": ["BevelDifferentialGearMeshCompoundParametricStudyTool"],
        "_4453": ["BevelDifferentialGearSetCompoundParametricStudyTool"],
        "_4454": ["BevelDifferentialPlanetGearCompoundParametricStudyTool"],
        "_4455": ["BevelDifferentialSunGearCompoundParametricStudyTool"],
        "_4456": ["BevelGearCompoundParametricStudyTool"],
        "_4457": ["BevelGearMeshCompoundParametricStudyTool"],
        "_4458": ["BevelGearSetCompoundParametricStudyTool"],
        "_4459": ["BoltCompoundParametricStudyTool"],
        "_4460": ["BoltedJointCompoundParametricStudyTool"],
        "_4461": ["ClutchCompoundParametricStudyTool"],
        "_4462": ["ClutchConnectionCompoundParametricStudyTool"],
        "_4463": ["ClutchHalfCompoundParametricStudyTool"],
        "_4464": ["CoaxialConnectionCompoundParametricStudyTool"],
        "_4465": ["ComponentCompoundParametricStudyTool"],
        "_4466": ["ConceptCouplingCompoundParametricStudyTool"],
        "_4467": ["ConceptCouplingConnectionCompoundParametricStudyTool"],
        "_4468": ["ConceptCouplingHalfCompoundParametricStudyTool"],
        "_4469": ["ConceptGearCompoundParametricStudyTool"],
        "_4470": ["ConceptGearMeshCompoundParametricStudyTool"],
        "_4471": ["ConceptGearSetCompoundParametricStudyTool"],
        "_4472": ["ConicalGearCompoundParametricStudyTool"],
        "_4473": ["ConicalGearMeshCompoundParametricStudyTool"],
        "_4474": ["ConicalGearSetCompoundParametricStudyTool"],
        "_4475": ["ConnectionCompoundParametricStudyTool"],
        "_4476": ["ConnectorCompoundParametricStudyTool"],
        "_4477": ["CouplingCompoundParametricStudyTool"],
        "_4478": ["CouplingConnectionCompoundParametricStudyTool"],
        "_4479": ["CouplingHalfCompoundParametricStudyTool"],
        "_4480": ["CVTBeltConnectionCompoundParametricStudyTool"],
        "_4481": ["CVTCompoundParametricStudyTool"],
        "_4482": ["CVTPulleyCompoundParametricStudyTool"],
        "_4483": ["CycloidalAssemblyCompoundParametricStudyTool"],
        "_4484": ["CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool"],
        "_4485": ["CycloidalDiscCompoundParametricStudyTool"],
        "_4486": ["CycloidalDiscPlanetaryBearingConnectionCompoundParametricStudyTool"],
        "_4487": ["CylindricalGearCompoundParametricStudyTool"],
        "_4488": ["CylindricalGearMeshCompoundParametricStudyTool"],
        "_4489": ["CylindricalGearSetCompoundParametricStudyTool"],
        "_4490": ["CylindricalPlanetGearCompoundParametricStudyTool"],
        "_4491": ["DatumCompoundParametricStudyTool"],
        "_4492": ["ExternalCADModelCompoundParametricStudyTool"],
        "_4493": ["FaceGearCompoundParametricStudyTool"],
        "_4494": ["FaceGearMeshCompoundParametricStudyTool"],
        "_4495": ["FaceGearSetCompoundParametricStudyTool"],
        "_4496": ["FEPartCompoundParametricStudyTool"],
        "_4497": ["FlexiblePinAssemblyCompoundParametricStudyTool"],
        "_4498": ["GearCompoundParametricStudyTool"],
        "_4499": ["GearMeshCompoundParametricStudyTool"],
        "_4500": ["GearSetCompoundParametricStudyTool"],
        "_4501": ["GuideDxfModelCompoundParametricStudyTool"],
        "_4502": ["HypoidGearCompoundParametricStudyTool"],
        "_4503": ["HypoidGearMeshCompoundParametricStudyTool"],
        "_4504": ["HypoidGearSetCompoundParametricStudyTool"],
        "_4505": ["InterMountableComponentConnectionCompoundParametricStudyTool"],
        "_4506": ["KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool"],
        "_4507": ["KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool"],
        "_4508": ["KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool"],
        "_4509": ["KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool"],
        "_4510": ["KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool"],
        "_4511": ["KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool"],
        "_4512": ["KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool"],
        "_4513": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool"
        ],
        "_4514": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool"
        ],
        "_4515": ["MassDiscCompoundParametricStudyTool"],
        "_4516": ["MeasurementComponentCompoundParametricStudyTool"],
        "_4517": ["MountableComponentCompoundParametricStudyTool"],
        "_4518": ["OilSealCompoundParametricStudyTool"],
        "_4519": ["PartCompoundParametricStudyTool"],
        "_4520": ["PartToPartShearCouplingCompoundParametricStudyTool"],
        "_4521": ["PartToPartShearCouplingConnectionCompoundParametricStudyTool"],
        "_4522": ["PartToPartShearCouplingHalfCompoundParametricStudyTool"],
        "_4523": ["PlanetaryConnectionCompoundParametricStudyTool"],
        "_4524": ["PlanetaryGearSetCompoundParametricStudyTool"],
        "_4525": ["PlanetCarrierCompoundParametricStudyTool"],
        "_4526": ["PointLoadCompoundParametricStudyTool"],
        "_4527": ["PowerLoadCompoundParametricStudyTool"],
        "_4528": ["PulleyCompoundParametricStudyTool"],
        "_4529": ["RingPinsCompoundParametricStudyTool"],
        "_4530": ["RingPinsToDiscConnectionCompoundParametricStudyTool"],
        "_4531": ["RollingRingAssemblyCompoundParametricStudyTool"],
        "_4532": ["RollingRingCompoundParametricStudyTool"],
        "_4533": ["RollingRingConnectionCompoundParametricStudyTool"],
        "_4534": ["RootAssemblyCompoundParametricStudyTool"],
        "_4535": ["ShaftCompoundParametricStudyTool"],
        "_4536": ["ShaftHubConnectionCompoundParametricStudyTool"],
        "_4537": ["ShaftToMountableComponentConnectionCompoundParametricStudyTool"],
        "_4538": ["SpecialisedAssemblyCompoundParametricStudyTool"],
        "_4539": ["SpiralBevelGearCompoundParametricStudyTool"],
        "_4540": ["SpiralBevelGearMeshCompoundParametricStudyTool"],
        "_4541": ["SpiralBevelGearSetCompoundParametricStudyTool"],
        "_4542": ["SpringDamperCompoundParametricStudyTool"],
        "_4543": ["SpringDamperConnectionCompoundParametricStudyTool"],
        "_4544": ["SpringDamperHalfCompoundParametricStudyTool"],
        "_4545": ["StraightBevelDiffGearCompoundParametricStudyTool"],
        "_4546": ["StraightBevelDiffGearMeshCompoundParametricStudyTool"],
        "_4547": ["StraightBevelDiffGearSetCompoundParametricStudyTool"],
        "_4548": ["StraightBevelGearCompoundParametricStudyTool"],
        "_4549": ["StraightBevelGearMeshCompoundParametricStudyTool"],
        "_4550": ["StraightBevelGearSetCompoundParametricStudyTool"],
        "_4551": ["StraightBevelPlanetGearCompoundParametricStudyTool"],
        "_4552": ["StraightBevelSunGearCompoundParametricStudyTool"],
        "_4553": ["SynchroniserCompoundParametricStudyTool"],
        "_4554": ["SynchroniserHalfCompoundParametricStudyTool"],
        "_4555": ["SynchroniserPartCompoundParametricStudyTool"],
        "_4556": ["SynchroniserSleeveCompoundParametricStudyTool"],
        "_4557": ["TorqueConverterCompoundParametricStudyTool"],
        "_4558": ["TorqueConverterConnectionCompoundParametricStudyTool"],
        "_4559": ["TorqueConverterPumpCompoundParametricStudyTool"],
        "_4560": ["TorqueConverterTurbineCompoundParametricStudyTool"],
        "_4561": ["UnbalancedMassCompoundParametricStudyTool"],
        "_4562": ["VirtualComponentCompoundParametricStudyTool"],
        "_4563": ["WormGearCompoundParametricStudyTool"],
        "_4564": ["WormGearMeshCompoundParametricStudyTool"],
        "_4565": ["WormGearSetCompoundParametricStudyTool"],
        "_4566": ["ZerolBevelGearCompoundParametricStudyTool"],
        "_4567": ["ZerolBevelGearMeshCompoundParametricStudyTool"],
        "_4568": ["ZerolBevelGearSetCompoundParametricStudyTool"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundParametricStudyTool",
    "AbstractShaftCompoundParametricStudyTool",
    "AbstractShaftOrHousingCompoundParametricStudyTool",
    "AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool",
    "AGMAGleasonConicalGearCompoundParametricStudyTool",
    "AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
    "AGMAGleasonConicalGearSetCompoundParametricStudyTool",
    "AssemblyCompoundParametricStudyTool",
    "BearingCompoundParametricStudyTool",
    "BeltConnectionCompoundParametricStudyTool",
    "BeltDriveCompoundParametricStudyTool",
    "BevelDifferentialGearCompoundParametricStudyTool",
    "BevelDifferentialGearMeshCompoundParametricStudyTool",
    "BevelDifferentialGearSetCompoundParametricStudyTool",
    "BevelDifferentialPlanetGearCompoundParametricStudyTool",
    "BevelDifferentialSunGearCompoundParametricStudyTool",
    "BevelGearCompoundParametricStudyTool",
    "BevelGearMeshCompoundParametricStudyTool",
    "BevelGearSetCompoundParametricStudyTool",
    "BoltCompoundParametricStudyTool",
    "BoltedJointCompoundParametricStudyTool",
    "ClutchCompoundParametricStudyTool",
    "ClutchConnectionCompoundParametricStudyTool",
    "ClutchHalfCompoundParametricStudyTool",
    "CoaxialConnectionCompoundParametricStudyTool",
    "ComponentCompoundParametricStudyTool",
    "ConceptCouplingCompoundParametricStudyTool",
    "ConceptCouplingConnectionCompoundParametricStudyTool",
    "ConceptCouplingHalfCompoundParametricStudyTool",
    "ConceptGearCompoundParametricStudyTool",
    "ConceptGearMeshCompoundParametricStudyTool",
    "ConceptGearSetCompoundParametricStudyTool",
    "ConicalGearCompoundParametricStudyTool",
    "ConicalGearMeshCompoundParametricStudyTool",
    "ConicalGearSetCompoundParametricStudyTool",
    "ConnectionCompoundParametricStudyTool",
    "ConnectorCompoundParametricStudyTool",
    "CouplingCompoundParametricStudyTool",
    "CouplingConnectionCompoundParametricStudyTool",
    "CouplingHalfCompoundParametricStudyTool",
    "CVTBeltConnectionCompoundParametricStudyTool",
    "CVTCompoundParametricStudyTool",
    "CVTPulleyCompoundParametricStudyTool",
    "CycloidalAssemblyCompoundParametricStudyTool",
    "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
    "CycloidalDiscCompoundParametricStudyTool",
    "CycloidalDiscPlanetaryBearingConnectionCompoundParametricStudyTool",
    "CylindricalGearCompoundParametricStudyTool",
    "CylindricalGearMeshCompoundParametricStudyTool",
    "CylindricalGearSetCompoundParametricStudyTool",
    "CylindricalPlanetGearCompoundParametricStudyTool",
    "DatumCompoundParametricStudyTool",
    "ExternalCADModelCompoundParametricStudyTool",
    "FaceGearCompoundParametricStudyTool",
    "FaceGearMeshCompoundParametricStudyTool",
    "FaceGearSetCompoundParametricStudyTool",
    "FEPartCompoundParametricStudyTool",
    "FlexiblePinAssemblyCompoundParametricStudyTool",
    "GearCompoundParametricStudyTool",
    "GearMeshCompoundParametricStudyTool",
    "GearSetCompoundParametricStudyTool",
    "GuideDxfModelCompoundParametricStudyTool",
    "HypoidGearCompoundParametricStudyTool",
    "HypoidGearMeshCompoundParametricStudyTool",
    "HypoidGearSetCompoundParametricStudyTool",
    "InterMountableComponentConnectionCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool",
    "MassDiscCompoundParametricStudyTool",
    "MeasurementComponentCompoundParametricStudyTool",
    "MountableComponentCompoundParametricStudyTool",
    "OilSealCompoundParametricStudyTool",
    "PartCompoundParametricStudyTool",
    "PartToPartShearCouplingCompoundParametricStudyTool",
    "PartToPartShearCouplingConnectionCompoundParametricStudyTool",
    "PartToPartShearCouplingHalfCompoundParametricStudyTool",
    "PlanetaryConnectionCompoundParametricStudyTool",
    "PlanetaryGearSetCompoundParametricStudyTool",
    "PlanetCarrierCompoundParametricStudyTool",
    "PointLoadCompoundParametricStudyTool",
    "PowerLoadCompoundParametricStudyTool",
    "PulleyCompoundParametricStudyTool",
    "RingPinsCompoundParametricStudyTool",
    "RingPinsToDiscConnectionCompoundParametricStudyTool",
    "RollingRingAssemblyCompoundParametricStudyTool",
    "RollingRingCompoundParametricStudyTool",
    "RollingRingConnectionCompoundParametricStudyTool",
    "RootAssemblyCompoundParametricStudyTool",
    "ShaftCompoundParametricStudyTool",
    "ShaftHubConnectionCompoundParametricStudyTool",
    "ShaftToMountableComponentConnectionCompoundParametricStudyTool",
    "SpecialisedAssemblyCompoundParametricStudyTool",
    "SpiralBevelGearCompoundParametricStudyTool",
    "SpiralBevelGearMeshCompoundParametricStudyTool",
    "SpiralBevelGearSetCompoundParametricStudyTool",
    "SpringDamperCompoundParametricStudyTool",
    "SpringDamperConnectionCompoundParametricStudyTool",
    "SpringDamperHalfCompoundParametricStudyTool",
    "StraightBevelDiffGearCompoundParametricStudyTool",
    "StraightBevelDiffGearMeshCompoundParametricStudyTool",
    "StraightBevelDiffGearSetCompoundParametricStudyTool",
    "StraightBevelGearCompoundParametricStudyTool",
    "StraightBevelGearMeshCompoundParametricStudyTool",
    "StraightBevelGearSetCompoundParametricStudyTool",
    "StraightBevelPlanetGearCompoundParametricStudyTool",
    "StraightBevelSunGearCompoundParametricStudyTool",
    "SynchroniserCompoundParametricStudyTool",
    "SynchroniserHalfCompoundParametricStudyTool",
    "SynchroniserPartCompoundParametricStudyTool",
    "SynchroniserSleeveCompoundParametricStudyTool",
    "TorqueConverterCompoundParametricStudyTool",
    "TorqueConverterConnectionCompoundParametricStudyTool",
    "TorqueConverterPumpCompoundParametricStudyTool",
    "TorqueConverterTurbineCompoundParametricStudyTool",
    "UnbalancedMassCompoundParametricStudyTool",
    "VirtualComponentCompoundParametricStudyTool",
    "WormGearCompoundParametricStudyTool",
    "WormGearMeshCompoundParametricStudyTool",
    "WormGearSetCompoundParametricStudyTool",
    "ZerolBevelGearCompoundParametricStudyTool",
    "ZerolBevelGearMeshCompoundParametricStudyTool",
    "ZerolBevelGearSetCompoundParametricStudyTool",
)
