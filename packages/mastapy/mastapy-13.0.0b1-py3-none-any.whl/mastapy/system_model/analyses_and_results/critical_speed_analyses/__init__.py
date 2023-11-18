"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6540 import AbstractAssemblyCriticalSpeedAnalysis
    from ._6541 import AbstractShaftCriticalSpeedAnalysis
    from ._6542 import AbstractShaftOrHousingCriticalSpeedAnalysis
    from ._6543 import AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis
    from ._6544 import AGMAGleasonConicalGearCriticalSpeedAnalysis
    from ._6545 import AGMAGleasonConicalGearMeshCriticalSpeedAnalysis
    from ._6546 import AGMAGleasonConicalGearSetCriticalSpeedAnalysis
    from ._6547 import AssemblyCriticalSpeedAnalysis
    from ._6548 import BearingCriticalSpeedAnalysis
    from ._6549 import BeltConnectionCriticalSpeedAnalysis
    from ._6550 import BeltDriveCriticalSpeedAnalysis
    from ._6551 import BevelDifferentialGearCriticalSpeedAnalysis
    from ._6552 import BevelDifferentialGearMeshCriticalSpeedAnalysis
    from ._6553 import BevelDifferentialGearSetCriticalSpeedAnalysis
    from ._6554 import BevelDifferentialPlanetGearCriticalSpeedAnalysis
    from ._6555 import BevelDifferentialSunGearCriticalSpeedAnalysis
    from ._6556 import BevelGearCriticalSpeedAnalysis
    from ._6557 import BevelGearMeshCriticalSpeedAnalysis
    from ._6558 import BevelGearSetCriticalSpeedAnalysis
    from ._6559 import BoltCriticalSpeedAnalysis
    from ._6560 import BoltedJointCriticalSpeedAnalysis
    from ._6561 import ClutchConnectionCriticalSpeedAnalysis
    from ._6562 import ClutchCriticalSpeedAnalysis
    from ._6563 import ClutchHalfCriticalSpeedAnalysis
    from ._6564 import CoaxialConnectionCriticalSpeedAnalysis
    from ._6565 import ComponentCriticalSpeedAnalysis
    from ._6566 import ConceptCouplingConnectionCriticalSpeedAnalysis
    from ._6567 import ConceptCouplingCriticalSpeedAnalysis
    from ._6568 import ConceptCouplingHalfCriticalSpeedAnalysis
    from ._6569 import ConceptGearCriticalSpeedAnalysis
    from ._6570 import ConceptGearMeshCriticalSpeedAnalysis
    from ._6571 import ConceptGearSetCriticalSpeedAnalysis
    from ._6572 import ConicalGearCriticalSpeedAnalysis
    from ._6573 import ConicalGearMeshCriticalSpeedAnalysis
    from ._6574 import ConicalGearSetCriticalSpeedAnalysis
    from ._6575 import ConnectionCriticalSpeedAnalysis
    from ._6576 import ConnectorCriticalSpeedAnalysis
    from ._6577 import CouplingConnectionCriticalSpeedAnalysis
    from ._6578 import CouplingCriticalSpeedAnalysis
    from ._6579 import CouplingHalfCriticalSpeedAnalysis
    from ._6580 import CriticalSpeedAnalysis
    from ._6581 import CriticalSpeedAnalysisDrawStyle
    from ._6582 import CriticalSpeedAnalysisOptions
    from ._6583 import CVTBeltConnectionCriticalSpeedAnalysis
    from ._6584 import CVTCriticalSpeedAnalysis
    from ._6585 import CVTPulleyCriticalSpeedAnalysis
    from ._6586 import CycloidalAssemblyCriticalSpeedAnalysis
    from ._6587 import CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis
    from ._6588 import CycloidalDiscCriticalSpeedAnalysis
    from ._6589 import CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis
    from ._6590 import CylindricalGearCriticalSpeedAnalysis
    from ._6591 import CylindricalGearMeshCriticalSpeedAnalysis
    from ._6592 import CylindricalGearSetCriticalSpeedAnalysis
    from ._6593 import CylindricalPlanetGearCriticalSpeedAnalysis
    from ._6594 import DatumCriticalSpeedAnalysis
    from ._6595 import ExternalCADModelCriticalSpeedAnalysis
    from ._6596 import FaceGearCriticalSpeedAnalysis
    from ._6597 import FaceGearMeshCriticalSpeedAnalysis
    from ._6598 import FaceGearSetCriticalSpeedAnalysis
    from ._6599 import FEPartCriticalSpeedAnalysis
    from ._6600 import FlexiblePinAssemblyCriticalSpeedAnalysis
    from ._6601 import GearCriticalSpeedAnalysis
    from ._6602 import GearMeshCriticalSpeedAnalysis
    from ._6603 import GearSetCriticalSpeedAnalysis
    from ._6604 import GuideDxfModelCriticalSpeedAnalysis
    from ._6605 import HypoidGearCriticalSpeedAnalysis
    from ._6606 import HypoidGearMeshCriticalSpeedAnalysis
    from ._6607 import HypoidGearSetCriticalSpeedAnalysis
    from ._6608 import InterMountableComponentConnectionCriticalSpeedAnalysis
    from ._6609 import KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis
    from ._6610 import KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis
    from ._6611 import KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis
    from ._6612 import KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis
    from ._6613 import KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis
    from ._6614 import KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis
    from ._6615 import KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis
    from ._6616 import KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis
    from ._6617 import KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis
    from ._6618 import MassDiscCriticalSpeedAnalysis
    from ._6619 import MeasurementComponentCriticalSpeedAnalysis
    from ._6620 import MountableComponentCriticalSpeedAnalysis
    from ._6621 import OilSealCriticalSpeedAnalysis
    from ._6622 import PartCriticalSpeedAnalysis
    from ._6623 import PartToPartShearCouplingConnectionCriticalSpeedAnalysis
    from ._6624 import PartToPartShearCouplingCriticalSpeedAnalysis
    from ._6625 import PartToPartShearCouplingHalfCriticalSpeedAnalysis
    from ._6626 import PlanetaryConnectionCriticalSpeedAnalysis
    from ._6627 import PlanetaryGearSetCriticalSpeedAnalysis
    from ._6628 import PlanetCarrierCriticalSpeedAnalysis
    from ._6629 import PointLoadCriticalSpeedAnalysis
    from ._6630 import PowerLoadCriticalSpeedAnalysis
    from ._6631 import PulleyCriticalSpeedAnalysis
    from ._6632 import RingPinsCriticalSpeedAnalysis
    from ._6633 import RingPinsToDiscConnectionCriticalSpeedAnalysis
    from ._6634 import RollingRingAssemblyCriticalSpeedAnalysis
    from ._6635 import RollingRingConnectionCriticalSpeedAnalysis
    from ._6636 import RollingRingCriticalSpeedAnalysis
    from ._6637 import RootAssemblyCriticalSpeedAnalysis
    from ._6638 import ShaftCriticalSpeedAnalysis
    from ._6639 import ShaftHubConnectionCriticalSpeedAnalysis
    from ._6640 import ShaftToMountableComponentConnectionCriticalSpeedAnalysis
    from ._6641 import SpecialisedAssemblyCriticalSpeedAnalysis
    from ._6642 import SpiralBevelGearCriticalSpeedAnalysis
    from ._6643 import SpiralBevelGearMeshCriticalSpeedAnalysis
    from ._6644 import SpiralBevelGearSetCriticalSpeedAnalysis
    from ._6645 import SpringDamperConnectionCriticalSpeedAnalysis
    from ._6646 import SpringDamperCriticalSpeedAnalysis
    from ._6647 import SpringDamperHalfCriticalSpeedAnalysis
    from ._6648 import StraightBevelDiffGearCriticalSpeedAnalysis
    from ._6649 import StraightBevelDiffGearMeshCriticalSpeedAnalysis
    from ._6650 import StraightBevelDiffGearSetCriticalSpeedAnalysis
    from ._6651 import StraightBevelGearCriticalSpeedAnalysis
    from ._6652 import StraightBevelGearMeshCriticalSpeedAnalysis
    from ._6653 import StraightBevelGearSetCriticalSpeedAnalysis
    from ._6654 import StraightBevelPlanetGearCriticalSpeedAnalysis
    from ._6655 import StraightBevelSunGearCriticalSpeedAnalysis
    from ._6656 import SynchroniserCriticalSpeedAnalysis
    from ._6657 import SynchroniserHalfCriticalSpeedAnalysis
    from ._6658 import SynchroniserPartCriticalSpeedAnalysis
    from ._6659 import SynchroniserSleeveCriticalSpeedAnalysis
    from ._6660 import TorqueConverterConnectionCriticalSpeedAnalysis
    from ._6661 import TorqueConverterCriticalSpeedAnalysis
    from ._6662 import TorqueConverterPumpCriticalSpeedAnalysis
    from ._6663 import TorqueConverterTurbineCriticalSpeedAnalysis
    from ._6664 import UnbalancedMassCriticalSpeedAnalysis
    from ._6665 import VirtualComponentCriticalSpeedAnalysis
    from ._6666 import WormGearCriticalSpeedAnalysis
    from ._6667 import WormGearMeshCriticalSpeedAnalysis
    from ._6668 import WormGearSetCriticalSpeedAnalysis
    from ._6669 import ZerolBevelGearCriticalSpeedAnalysis
    from ._6670 import ZerolBevelGearMeshCriticalSpeedAnalysis
    from ._6671 import ZerolBevelGearSetCriticalSpeedAnalysis
else:
    import_structure = {
        "_6540": ["AbstractAssemblyCriticalSpeedAnalysis"],
        "_6541": ["AbstractShaftCriticalSpeedAnalysis"],
        "_6542": ["AbstractShaftOrHousingCriticalSpeedAnalysis"],
        "_6543": ["AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis"],
        "_6544": ["AGMAGleasonConicalGearCriticalSpeedAnalysis"],
        "_6545": ["AGMAGleasonConicalGearMeshCriticalSpeedAnalysis"],
        "_6546": ["AGMAGleasonConicalGearSetCriticalSpeedAnalysis"],
        "_6547": ["AssemblyCriticalSpeedAnalysis"],
        "_6548": ["BearingCriticalSpeedAnalysis"],
        "_6549": ["BeltConnectionCriticalSpeedAnalysis"],
        "_6550": ["BeltDriveCriticalSpeedAnalysis"],
        "_6551": ["BevelDifferentialGearCriticalSpeedAnalysis"],
        "_6552": ["BevelDifferentialGearMeshCriticalSpeedAnalysis"],
        "_6553": ["BevelDifferentialGearSetCriticalSpeedAnalysis"],
        "_6554": ["BevelDifferentialPlanetGearCriticalSpeedAnalysis"],
        "_6555": ["BevelDifferentialSunGearCriticalSpeedAnalysis"],
        "_6556": ["BevelGearCriticalSpeedAnalysis"],
        "_6557": ["BevelGearMeshCriticalSpeedAnalysis"],
        "_6558": ["BevelGearSetCriticalSpeedAnalysis"],
        "_6559": ["BoltCriticalSpeedAnalysis"],
        "_6560": ["BoltedJointCriticalSpeedAnalysis"],
        "_6561": ["ClutchConnectionCriticalSpeedAnalysis"],
        "_6562": ["ClutchCriticalSpeedAnalysis"],
        "_6563": ["ClutchHalfCriticalSpeedAnalysis"],
        "_6564": ["CoaxialConnectionCriticalSpeedAnalysis"],
        "_6565": ["ComponentCriticalSpeedAnalysis"],
        "_6566": ["ConceptCouplingConnectionCriticalSpeedAnalysis"],
        "_6567": ["ConceptCouplingCriticalSpeedAnalysis"],
        "_6568": ["ConceptCouplingHalfCriticalSpeedAnalysis"],
        "_6569": ["ConceptGearCriticalSpeedAnalysis"],
        "_6570": ["ConceptGearMeshCriticalSpeedAnalysis"],
        "_6571": ["ConceptGearSetCriticalSpeedAnalysis"],
        "_6572": ["ConicalGearCriticalSpeedAnalysis"],
        "_6573": ["ConicalGearMeshCriticalSpeedAnalysis"],
        "_6574": ["ConicalGearSetCriticalSpeedAnalysis"],
        "_6575": ["ConnectionCriticalSpeedAnalysis"],
        "_6576": ["ConnectorCriticalSpeedAnalysis"],
        "_6577": ["CouplingConnectionCriticalSpeedAnalysis"],
        "_6578": ["CouplingCriticalSpeedAnalysis"],
        "_6579": ["CouplingHalfCriticalSpeedAnalysis"],
        "_6580": ["CriticalSpeedAnalysis"],
        "_6581": ["CriticalSpeedAnalysisDrawStyle"],
        "_6582": ["CriticalSpeedAnalysisOptions"],
        "_6583": ["CVTBeltConnectionCriticalSpeedAnalysis"],
        "_6584": ["CVTCriticalSpeedAnalysis"],
        "_6585": ["CVTPulleyCriticalSpeedAnalysis"],
        "_6586": ["CycloidalAssemblyCriticalSpeedAnalysis"],
        "_6587": ["CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis"],
        "_6588": ["CycloidalDiscCriticalSpeedAnalysis"],
        "_6589": ["CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis"],
        "_6590": ["CylindricalGearCriticalSpeedAnalysis"],
        "_6591": ["CylindricalGearMeshCriticalSpeedAnalysis"],
        "_6592": ["CylindricalGearSetCriticalSpeedAnalysis"],
        "_6593": ["CylindricalPlanetGearCriticalSpeedAnalysis"],
        "_6594": ["DatumCriticalSpeedAnalysis"],
        "_6595": ["ExternalCADModelCriticalSpeedAnalysis"],
        "_6596": ["FaceGearCriticalSpeedAnalysis"],
        "_6597": ["FaceGearMeshCriticalSpeedAnalysis"],
        "_6598": ["FaceGearSetCriticalSpeedAnalysis"],
        "_6599": ["FEPartCriticalSpeedAnalysis"],
        "_6600": ["FlexiblePinAssemblyCriticalSpeedAnalysis"],
        "_6601": ["GearCriticalSpeedAnalysis"],
        "_6602": ["GearMeshCriticalSpeedAnalysis"],
        "_6603": ["GearSetCriticalSpeedAnalysis"],
        "_6604": ["GuideDxfModelCriticalSpeedAnalysis"],
        "_6605": ["HypoidGearCriticalSpeedAnalysis"],
        "_6606": ["HypoidGearMeshCriticalSpeedAnalysis"],
        "_6607": ["HypoidGearSetCriticalSpeedAnalysis"],
        "_6608": ["InterMountableComponentConnectionCriticalSpeedAnalysis"],
        "_6609": ["KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis"],
        "_6610": ["KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis"],
        "_6611": ["KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis"],
        "_6612": ["KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis"],
        "_6613": ["KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis"],
        "_6614": ["KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis"],
        "_6615": ["KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis"],
        "_6616": ["KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis"],
        "_6617": ["KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis"],
        "_6618": ["MassDiscCriticalSpeedAnalysis"],
        "_6619": ["MeasurementComponentCriticalSpeedAnalysis"],
        "_6620": ["MountableComponentCriticalSpeedAnalysis"],
        "_6621": ["OilSealCriticalSpeedAnalysis"],
        "_6622": ["PartCriticalSpeedAnalysis"],
        "_6623": ["PartToPartShearCouplingConnectionCriticalSpeedAnalysis"],
        "_6624": ["PartToPartShearCouplingCriticalSpeedAnalysis"],
        "_6625": ["PartToPartShearCouplingHalfCriticalSpeedAnalysis"],
        "_6626": ["PlanetaryConnectionCriticalSpeedAnalysis"],
        "_6627": ["PlanetaryGearSetCriticalSpeedAnalysis"],
        "_6628": ["PlanetCarrierCriticalSpeedAnalysis"],
        "_6629": ["PointLoadCriticalSpeedAnalysis"],
        "_6630": ["PowerLoadCriticalSpeedAnalysis"],
        "_6631": ["PulleyCriticalSpeedAnalysis"],
        "_6632": ["RingPinsCriticalSpeedAnalysis"],
        "_6633": ["RingPinsToDiscConnectionCriticalSpeedAnalysis"],
        "_6634": ["RollingRingAssemblyCriticalSpeedAnalysis"],
        "_6635": ["RollingRingConnectionCriticalSpeedAnalysis"],
        "_6636": ["RollingRingCriticalSpeedAnalysis"],
        "_6637": ["RootAssemblyCriticalSpeedAnalysis"],
        "_6638": ["ShaftCriticalSpeedAnalysis"],
        "_6639": ["ShaftHubConnectionCriticalSpeedAnalysis"],
        "_6640": ["ShaftToMountableComponentConnectionCriticalSpeedAnalysis"],
        "_6641": ["SpecialisedAssemblyCriticalSpeedAnalysis"],
        "_6642": ["SpiralBevelGearCriticalSpeedAnalysis"],
        "_6643": ["SpiralBevelGearMeshCriticalSpeedAnalysis"],
        "_6644": ["SpiralBevelGearSetCriticalSpeedAnalysis"],
        "_6645": ["SpringDamperConnectionCriticalSpeedAnalysis"],
        "_6646": ["SpringDamperCriticalSpeedAnalysis"],
        "_6647": ["SpringDamperHalfCriticalSpeedAnalysis"],
        "_6648": ["StraightBevelDiffGearCriticalSpeedAnalysis"],
        "_6649": ["StraightBevelDiffGearMeshCriticalSpeedAnalysis"],
        "_6650": ["StraightBevelDiffGearSetCriticalSpeedAnalysis"],
        "_6651": ["StraightBevelGearCriticalSpeedAnalysis"],
        "_6652": ["StraightBevelGearMeshCriticalSpeedAnalysis"],
        "_6653": ["StraightBevelGearSetCriticalSpeedAnalysis"],
        "_6654": ["StraightBevelPlanetGearCriticalSpeedAnalysis"],
        "_6655": ["StraightBevelSunGearCriticalSpeedAnalysis"],
        "_6656": ["SynchroniserCriticalSpeedAnalysis"],
        "_6657": ["SynchroniserHalfCriticalSpeedAnalysis"],
        "_6658": ["SynchroniserPartCriticalSpeedAnalysis"],
        "_6659": ["SynchroniserSleeveCriticalSpeedAnalysis"],
        "_6660": ["TorqueConverterConnectionCriticalSpeedAnalysis"],
        "_6661": ["TorqueConverterCriticalSpeedAnalysis"],
        "_6662": ["TorqueConverterPumpCriticalSpeedAnalysis"],
        "_6663": ["TorqueConverterTurbineCriticalSpeedAnalysis"],
        "_6664": ["UnbalancedMassCriticalSpeedAnalysis"],
        "_6665": ["VirtualComponentCriticalSpeedAnalysis"],
        "_6666": ["WormGearCriticalSpeedAnalysis"],
        "_6667": ["WormGearMeshCriticalSpeedAnalysis"],
        "_6668": ["WormGearSetCriticalSpeedAnalysis"],
        "_6669": ["ZerolBevelGearCriticalSpeedAnalysis"],
        "_6670": ["ZerolBevelGearMeshCriticalSpeedAnalysis"],
        "_6671": ["ZerolBevelGearSetCriticalSpeedAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCriticalSpeedAnalysis",
    "AbstractShaftCriticalSpeedAnalysis",
    "AbstractShaftOrHousingCriticalSpeedAnalysis",
    "AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis",
    "AGMAGleasonConicalGearCriticalSpeedAnalysis",
    "AGMAGleasonConicalGearMeshCriticalSpeedAnalysis",
    "AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
    "AssemblyCriticalSpeedAnalysis",
    "BearingCriticalSpeedAnalysis",
    "BeltConnectionCriticalSpeedAnalysis",
    "BeltDriveCriticalSpeedAnalysis",
    "BevelDifferentialGearCriticalSpeedAnalysis",
    "BevelDifferentialGearMeshCriticalSpeedAnalysis",
    "BevelDifferentialGearSetCriticalSpeedAnalysis",
    "BevelDifferentialPlanetGearCriticalSpeedAnalysis",
    "BevelDifferentialSunGearCriticalSpeedAnalysis",
    "BevelGearCriticalSpeedAnalysis",
    "BevelGearMeshCriticalSpeedAnalysis",
    "BevelGearSetCriticalSpeedAnalysis",
    "BoltCriticalSpeedAnalysis",
    "BoltedJointCriticalSpeedAnalysis",
    "ClutchConnectionCriticalSpeedAnalysis",
    "ClutchCriticalSpeedAnalysis",
    "ClutchHalfCriticalSpeedAnalysis",
    "CoaxialConnectionCriticalSpeedAnalysis",
    "ComponentCriticalSpeedAnalysis",
    "ConceptCouplingConnectionCriticalSpeedAnalysis",
    "ConceptCouplingCriticalSpeedAnalysis",
    "ConceptCouplingHalfCriticalSpeedAnalysis",
    "ConceptGearCriticalSpeedAnalysis",
    "ConceptGearMeshCriticalSpeedAnalysis",
    "ConceptGearSetCriticalSpeedAnalysis",
    "ConicalGearCriticalSpeedAnalysis",
    "ConicalGearMeshCriticalSpeedAnalysis",
    "ConicalGearSetCriticalSpeedAnalysis",
    "ConnectionCriticalSpeedAnalysis",
    "ConnectorCriticalSpeedAnalysis",
    "CouplingConnectionCriticalSpeedAnalysis",
    "CouplingCriticalSpeedAnalysis",
    "CouplingHalfCriticalSpeedAnalysis",
    "CriticalSpeedAnalysis",
    "CriticalSpeedAnalysisDrawStyle",
    "CriticalSpeedAnalysisOptions",
    "CVTBeltConnectionCriticalSpeedAnalysis",
    "CVTCriticalSpeedAnalysis",
    "CVTPulleyCriticalSpeedAnalysis",
    "CycloidalAssemblyCriticalSpeedAnalysis",
    "CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis",
    "CycloidalDiscCriticalSpeedAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis",
    "CylindricalGearCriticalSpeedAnalysis",
    "CylindricalGearMeshCriticalSpeedAnalysis",
    "CylindricalGearSetCriticalSpeedAnalysis",
    "CylindricalPlanetGearCriticalSpeedAnalysis",
    "DatumCriticalSpeedAnalysis",
    "ExternalCADModelCriticalSpeedAnalysis",
    "FaceGearCriticalSpeedAnalysis",
    "FaceGearMeshCriticalSpeedAnalysis",
    "FaceGearSetCriticalSpeedAnalysis",
    "FEPartCriticalSpeedAnalysis",
    "FlexiblePinAssemblyCriticalSpeedAnalysis",
    "GearCriticalSpeedAnalysis",
    "GearMeshCriticalSpeedAnalysis",
    "GearSetCriticalSpeedAnalysis",
    "GuideDxfModelCriticalSpeedAnalysis",
    "HypoidGearCriticalSpeedAnalysis",
    "HypoidGearMeshCriticalSpeedAnalysis",
    "HypoidGearSetCriticalSpeedAnalysis",
    "InterMountableComponentConnectionCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis",
    "MassDiscCriticalSpeedAnalysis",
    "MeasurementComponentCriticalSpeedAnalysis",
    "MountableComponentCriticalSpeedAnalysis",
    "OilSealCriticalSpeedAnalysis",
    "PartCriticalSpeedAnalysis",
    "PartToPartShearCouplingConnectionCriticalSpeedAnalysis",
    "PartToPartShearCouplingCriticalSpeedAnalysis",
    "PartToPartShearCouplingHalfCriticalSpeedAnalysis",
    "PlanetaryConnectionCriticalSpeedAnalysis",
    "PlanetaryGearSetCriticalSpeedAnalysis",
    "PlanetCarrierCriticalSpeedAnalysis",
    "PointLoadCriticalSpeedAnalysis",
    "PowerLoadCriticalSpeedAnalysis",
    "PulleyCriticalSpeedAnalysis",
    "RingPinsCriticalSpeedAnalysis",
    "RingPinsToDiscConnectionCriticalSpeedAnalysis",
    "RollingRingAssemblyCriticalSpeedAnalysis",
    "RollingRingConnectionCriticalSpeedAnalysis",
    "RollingRingCriticalSpeedAnalysis",
    "RootAssemblyCriticalSpeedAnalysis",
    "ShaftCriticalSpeedAnalysis",
    "ShaftHubConnectionCriticalSpeedAnalysis",
    "ShaftToMountableComponentConnectionCriticalSpeedAnalysis",
    "SpecialisedAssemblyCriticalSpeedAnalysis",
    "SpiralBevelGearCriticalSpeedAnalysis",
    "SpiralBevelGearMeshCriticalSpeedAnalysis",
    "SpiralBevelGearSetCriticalSpeedAnalysis",
    "SpringDamperConnectionCriticalSpeedAnalysis",
    "SpringDamperCriticalSpeedAnalysis",
    "SpringDamperHalfCriticalSpeedAnalysis",
    "StraightBevelDiffGearCriticalSpeedAnalysis",
    "StraightBevelDiffGearMeshCriticalSpeedAnalysis",
    "StraightBevelDiffGearSetCriticalSpeedAnalysis",
    "StraightBevelGearCriticalSpeedAnalysis",
    "StraightBevelGearMeshCriticalSpeedAnalysis",
    "StraightBevelGearSetCriticalSpeedAnalysis",
    "StraightBevelPlanetGearCriticalSpeedAnalysis",
    "StraightBevelSunGearCriticalSpeedAnalysis",
    "SynchroniserCriticalSpeedAnalysis",
    "SynchroniserHalfCriticalSpeedAnalysis",
    "SynchroniserPartCriticalSpeedAnalysis",
    "SynchroniserSleeveCriticalSpeedAnalysis",
    "TorqueConverterConnectionCriticalSpeedAnalysis",
    "TorqueConverterCriticalSpeedAnalysis",
    "TorqueConverterPumpCriticalSpeedAnalysis",
    "TorqueConverterTurbineCriticalSpeedAnalysis",
    "UnbalancedMassCriticalSpeedAnalysis",
    "VirtualComponentCriticalSpeedAnalysis",
    "WormGearCriticalSpeedAnalysis",
    "WormGearMeshCriticalSpeedAnalysis",
    "WormGearSetCriticalSpeedAnalysis",
    "ZerolBevelGearCriticalSpeedAnalysis",
    "ZerolBevelGearMeshCriticalSpeedAnalysis",
    "ZerolBevelGearSetCriticalSpeedAnalysis",
)
