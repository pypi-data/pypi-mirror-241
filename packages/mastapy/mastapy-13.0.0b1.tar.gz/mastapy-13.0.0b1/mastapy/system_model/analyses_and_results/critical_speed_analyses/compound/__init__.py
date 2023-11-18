"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6672 import AbstractAssemblyCompoundCriticalSpeedAnalysis
    from ._6673 import AbstractShaftCompoundCriticalSpeedAnalysis
    from ._6674 import AbstractShaftOrHousingCompoundCriticalSpeedAnalysis
    from ._6675 import (
        AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis,
    )
    from ._6676 import AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis
    from ._6677 import AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis
    from ._6678 import AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis
    from ._6679 import AssemblyCompoundCriticalSpeedAnalysis
    from ._6680 import BearingCompoundCriticalSpeedAnalysis
    from ._6681 import BeltConnectionCompoundCriticalSpeedAnalysis
    from ._6682 import BeltDriveCompoundCriticalSpeedAnalysis
    from ._6683 import BevelDifferentialGearCompoundCriticalSpeedAnalysis
    from ._6684 import BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis
    from ._6685 import BevelDifferentialGearSetCompoundCriticalSpeedAnalysis
    from ._6686 import BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis
    from ._6687 import BevelDifferentialSunGearCompoundCriticalSpeedAnalysis
    from ._6688 import BevelGearCompoundCriticalSpeedAnalysis
    from ._6689 import BevelGearMeshCompoundCriticalSpeedAnalysis
    from ._6690 import BevelGearSetCompoundCriticalSpeedAnalysis
    from ._6691 import BoltCompoundCriticalSpeedAnalysis
    from ._6692 import BoltedJointCompoundCriticalSpeedAnalysis
    from ._6693 import ClutchCompoundCriticalSpeedAnalysis
    from ._6694 import ClutchConnectionCompoundCriticalSpeedAnalysis
    from ._6695 import ClutchHalfCompoundCriticalSpeedAnalysis
    from ._6696 import CoaxialConnectionCompoundCriticalSpeedAnalysis
    from ._6697 import ComponentCompoundCriticalSpeedAnalysis
    from ._6698 import ConceptCouplingCompoundCriticalSpeedAnalysis
    from ._6699 import ConceptCouplingConnectionCompoundCriticalSpeedAnalysis
    from ._6700 import ConceptCouplingHalfCompoundCriticalSpeedAnalysis
    from ._6701 import ConceptGearCompoundCriticalSpeedAnalysis
    from ._6702 import ConceptGearMeshCompoundCriticalSpeedAnalysis
    from ._6703 import ConceptGearSetCompoundCriticalSpeedAnalysis
    from ._6704 import ConicalGearCompoundCriticalSpeedAnalysis
    from ._6705 import ConicalGearMeshCompoundCriticalSpeedAnalysis
    from ._6706 import ConicalGearSetCompoundCriticalSpeedAnalysis
    from ._6707 import ConnectionCompoundCriticalSpeedAnalysis
    from ._6708 import ConnectorCompoundCriticalSpeedAnalysis
    from ._6709 import CouplingCompoundCriticalSpeedAnalysis
    from ._6710 import CouplingConnectionCompoundCriticalSpeedAnalysis
    from ._6711 import CouplingHalfCompoundCriticalSpeedAnalysis
    from ._6712 import CVTBeltConnectionCompoundCriticalSpeedAnalysis
    from ._6713 import CVTCompoundCriticalSpeedAnalysis
    from ._6714 import CVTPulleyCompoundCriticalSpeedAnalysis
    from ._6715 import CycloidalAssemblyCompoundCriticalSpeedAnalysis
    from ._6716 import (
        CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis,
    )
    from ._6717 import CycloidalDiscCompoundCriticalSpeedAnalysis
    from ._6718 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundCriticalSpeedAnalysis,
    )
    from ._6719 import CylindricalGearCompoundCriticalSpeedAnalysis
    from ._6720 import CylindricalGearMeshCompoundCriticalSpeedAnalysis
    from ._6721 import CylindricalGearSetCompoundCriticalSpeedAnalysis
    from ._6722 import CylindricalPlanetGearCompoundCriticalSpeedAnalysis
    from ._6723 import DatumCompoundCriticalSpeedAnalysis
    from ._6724 import ExternalCADModelCompoundCriticalSpeedAnalysis
    from ._6725 import FaceGearCompoundCriticalSpeedAnalysis
    from ._6726 import FaceGearMeshCompoundCriticalSpeedAnalysis
    from ._6727 import FaceGearSetCompoundCriticalSpeedAnalysis
    from ._6728 import FEPartCompoundCriticalSpeedAnalysis
    from ._6729 import FlexiblePinAssemblyCompoundCriticalSpeedAnalysis
    from ._6730 import GearCompoundCriticalSpeedAnalysis
    from ._6731 import GearMeshCompoundCriticalSpeedAnalysis
    from ._6732 import GearSetCompoundCriticalSpeedAnalysis
    from ._6733 import GuideDxfModelCompoundCriticalSpeedAnalysis
    from ._6734 import HypoidGearCompoundCriticalSpeedAnalysis
    from ._6735 import HypoidGearMeshCompoundCriticalSpeedAnalysis
    from ._6736 import HypoidGearSetCompoundCriticalSpeedAnalysis
    from ._6737 import InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
    from ._6738 import KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis
    from ._6739 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis,
    )
    from ._6740 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis,
    )
    from ._6741 import KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis
    from ._6742 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis,
    )
    from ._6743 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis,
    )
    from ._6744 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis,
    )
    from ._6745 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis,
    )
    from ._6746 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis,
    )
    from ._6747 import MassDiscCompoundCriticalSpeedAnalysis
    from ._6748 import MeasurementComponentCompoundCriticalSpeedAnalysis
    from ._6749 import MountableComponentCompoundCriticalSpeedAnalysis
    from ._6750 import OilSealCompoundCriticalSpeedAnalysis
    from ._6751 import PartCompoundCriticalSpeedAnalysis
    from ._6752 import PartToPartShearCouplingCompoundCriticalSpeedAnalysis
    from ._6753 import PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis
    from ._6754 import PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis
    from ._6755 import PlanetaryConnectionCompoundCriticalSpeedAnalysis
    from ._6756 import PlanetaryGearSetCompoundCriticalSpeedAnalysis
    from ._6757 import PlanetCarrierCompoundCriticalSpeedAnalysis
    from ._6758 import PointLoadCompoundCriticalSpeedAnalysis
    from ._6759 import PowerLoadCompoundCriticalSpeedAnalysis
    from ._6760 import PulleyCompoundCriticalSpeedAnalysis
    from ._6761 import RingPinsCompoundCriticalSpeedAnalysis
    from ._6762 import RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis
    from ._6763 import RollingRingAssemblyCompoundCriticalSpeedAnalysis
    from ._6764 import RollingRingCompoundCriticalSpeedAnalysis
    from ._6765 import RollingRingConnectionCompoundCriticalSpeedAnalysis
    from ._6766 import RootAssemblyCompoundCriticalSpeedAnalysis
    from ._6767 import ShaftCompoundCriticalSpeedAnalysis
    from ._6768 import ShaftHubConnectionCompoundCriticalSpeedAnalysis
    from ._6769 import ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis
    from ._6770 import SpecialisedAssemblyCompoundCriticalSpeedAnalysis
    from ._6771 import SpiralBevelGearCompoundCriticalSpeedAnalysis
    from ._6772 import SpiralBevelGearMeshCompoundCriticalSpeedAnalysis
    from ._6773 import SpiralBevelGearSetCompoundCriticalSpeedAnalysis
    from ._6774 import SpringDamperCompoundCriticalSpeedAnalysis
    from ._6775 import SpringDamperConnectionCompoundCriticalSpeedAnalysis
    from ._6776 import SpringDamperHalfCompoundCriticalSpeedAnalysis
    from ._6777 import StraightBevelDiffGearCompoundCriticalSpeedAnalysis
    from ._6778 import StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis
    from ._6779 import StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis
    from ._6780 import StraightBevelGearCompoundCriticalSpeedAnalysis
    from ._6781 import StraightBevelGearMeshCompoundCriticalSpeedAnalysis
    from ._6782 import StraightBevelGearSetCompoundCriticalSpeedAnalysis
    from ._6783 import StraightBevelPlanetGearCompoundCriticalSpeedAnalysis
    from ._6784 import StraightBevelSunGearCompoundCriticalSpeedAnalysis
    from ._6785 import SynchroniserCompoundCriticalSpeedAnalysis
    from ._6786 import SynchroniserHalfCompoundCriticalSpeedAnalysis
    from ._6787 import SynchroniserPartCompoundCriticalSpeedAnalysis
    from ._6788 import SynchroniserSleeveCompoundCriticalSpeedAnalysis
    from ._6789 import TorqueConverterCompoundCriticalSpeedAnalysis
    from ._6790 import TorqueConverterConnectionCompoundCriticalSpeedAnalysis
    from ._6791 import TorqueConverterPumpCompoundCriticalSpeedAnalysis
    from ._6792 import TorqueConverterTurbineCompoundCriticalSpeedAnalysis
    from ._6793 import UnbalancedMassCompoundCriticalSpeedAnalysis
    from ._6794 import VirtualComponentCompoundCriticalSpeedAnalysis
    from ._6795 import WormGearCompoundCriticalSpeedAnalysis
    from ._6796 import WormGearMeshCompoundCriticalSpeedAnalysis
    from ._6797 import WormGearSetCompoundCriticalSpeedAnalysis
    from ._6798 import ZerolBevelGearCompoundCriticalSpeedAnalysis
    from ._6799 import ZerolBevelGearMeshCompoundCriticalSpeedAnalysis
    from ._6800 import ZerolBevelGearSetCompoundCriticalSpeedAnalysis
else:
    import_structure = {
        "_6672": ["AbstractAssemblyCompoundCriticalSpeedAnalysis"],
        "_6673": ["AbstractShaftCompoundCriticalSpeedAnalysis"],
        "_6674": ["AbstractShaftOrHousingCompoundCriticalSpeedAnalysis"],
        "_6675": [
            "AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis"
        ],
        "_6676": ["AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis"],
        "_6677": ["AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis"],
        "_6678": ["AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis"],
        "_6679": ["AssemblyCompoundCriticalSpeedAnalysis"],
        "_6680": ["BearingCompoundCriticalSpeedAnalysis"],
        "_6681": ["BeltConnectionCompoundCriticalSpeedAnalysis"],
        "_6682": ["BeltDriveCompoundCriticalSpeedAnalysis"],
        "_6683": ["BevelDifferentialGearCompoundCriticalSpeedAnalysis"],
        "_6684": ["BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis"],
        "_6685": ["BevelDifferentialGearSetCompoundCriticalSpeedAnalysis"],
        "_6686": ["BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis"],
        "_6687": ["BevelDifferentialSunGearCompoundCriticalSpeedAnalysis"],
        "_6688": ["BevelGearCompoundCriticalSpeedAnalysis"],
        "_6689": ["BevelGearMeshCompoundCriticalSpeedAnalysis"],
        "_6690": ["BevelGearSetCompoundCriticalSpeedAnalysis"],
        "_6691": ["BoltCompoundCriticalSpeedAnalysis"],
        "_6692": ["BoltedJointCompoundCriticalSpeedAnalysis"],
        "_6693": ["ClutchCompoundCriticalSpeedAnalysis"],
        "_6694": ["ClutchConnectionCompoundCriticalSpeedAnalysis"],
        "_6695": ["ClutchHalfCompoundCriticalSpeedAnalysis"],
        "_6696": ["CoaxialConnectionCompoundCriticalSpeedAnalysis"],
        "_6697": ["ComponentCompoundCriticalSpeedAnalysis"],
        "_6698": ["ConceptCouplingCompoundCriticalSpeedAnalysis"],
        "_6699": ["ConceptCouplingConnectionCompoundCriticalSpeedAnalysis"],
        "_6700": ["ConceptCouplingHalfCompoundCriticalSpeedAnalysis"],
        "_6701": ["ConceptGearCompoundCriticalSpeedAnalysis"],
        "_6702": ["ConceptGearMeshCompoundCriticalSpeedAnalysis"],
        "_6703": ["ConceptGearSetCompoundCriticalSpeedAnalysis"],
        "_6704": ["ConicalGearCompoundCriticalSpeedAnalysis"],
        "_6705": ["ConicalGearMeshCompoundCriticalSpeedAnalysis"],
        "_6706": ["ConicalGearSetCompoundCriticalSpeedAnalysis"],
        "_6707": ["ConnectionCompoundCriticalSpeedAnalysis"],
        "_6708": ["ConnectorCompoundCriticalSpeedAnalysis"],
        "_6709": ["CouplingCompoundCriticalSpeedAnalysis"],
        "_6710": ["CouplingConnectionCompoundCriticalSpeedAnalysis"],
        "_6711": ["CouplingHalfCompoundCriticalSpeedAnalysis"],
        "_6712": ["CVTBeltConnectionCompoundCriticalSpeedAnalysis"],
        "_6713": ["CVTCompoundCriticalSpeedAnalysis"],
        "_6714": ["CVTPulleyCompoundCriticalSpeedAnalysis"],
        "_6715": ["CycloidalAssemblyCompoundCriticalSpeedAnalysis"],
        "_6716": ["CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis"],
        "_6717": ["CycloidalDiscCompoundCriticalSpeedAnalysis"],
        "_6718": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundCriticalSpeedAnalysis"
        ],
        "_6719": ["CylindricalGearCompoundCriticalSpeedAnalysis"],
        "_6720": ["CylindricalGearMeshCompoundCriticalSpeedAnalysis"],
        "_6721": ["CylindricalGearSetCompoundCriticalSpeedAnalysis"],
        "_6722": ["CylindricalPlanetGearCompoundCriticalSpeedAnalysis"],
        "_6723": ["DatumCompoundCriticalSpeedAnalysis"],
        "_6724": ["ExternalCADModelCompoundCriticalSpeedAnalysis"],
        "_6725": ["FaceGearCompoundCriticalSpeedAnalysis"],
        "_6726": ["FaceGearMeshCompoundCriticalSpeedAnalysis"],
        "_6727": ["FaceGearSetCompoundCriticalSpeedAnalysis"],
        "_6728": ["FEPartCompoundCriticalSpeedAnalysis"],
        "_6729": ["FlexiblePinAssemblyCompoundCriticalSpeedAnalysis"],
        "_6730": ["GearCompoundCriticalSpeedAnalysis"],
        "_6731": ["GearMeshCompoundCriticalSpeedAnalysis"],
        "_6732": ["GearSetCompoundCriticalSpeedAnalysis"],
        "_6733": ["GuideDxfModelCompoundCriticalSpeedAnalysis"],
        "_6734": ["HypoidGearCompoundCriticalSpeedAnalysis"],
        "_6735": ["HypoidGearMeshCompoundCriticalSpeedAnalysis"],
        "_6736": ["HypoidGearSetCompoundCriticalSpeedAnalysis"],
        "_6737": ["InterMountableComponentConnectionCompoundCriticalSpeedAnalysis"],
        "_6738": ["KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis"],
        "_6739": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis"
        ],
        "_6740": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis"
        ],
        "_6741": ["KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis"],
        "_6742": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis"
        ],
        "_6743": ["KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis"],
        "_6744": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis"
        ],
        "_6745": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis"
        ],
        "_6746": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis"
        ],
        "_6747": ["MassDiscCompoundCriticalSpeedAnalysis"],
        "_6748": ["MeasurementComponentCompoundCriticalSpeedAnalysis"],
        "_6749": ["MountableComponentCompoundCriticalSpeedAnalysis"],
        "_6750": ["OilSealCompoundCriticalSpeedAnalysis"],
        "_6751": ["PartCompoundCriticalSpeedAnalysis"],
        "_6752": ["PartToPartShearCouplingCompoundCriticalSpeedAnalysis"],
        "_6753": ["PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis"],
        "_6754": ["PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis"],
        "_6755": ["PlanetaryConnectionCompoundCriticalSpeedAnalysis"],
        "_6756": ["PlanetaryGearSetCompoundCriticalSpeedAnalysis"],
        "_6757": ["PlanetCarrierCompoundCriticalSpeedAnalysis"],
        "_6758": ["PointLoadCompoundCriticalSpeedAnalysis"],
        "_6759": ["PowerLoadCompoundCriticalSpeedAnalysis"],
        "_6760": ["PulleyCompoundCriticalSpeedAnalysis"],
        "_6761": ["RingPinsCompoundCriticalSpeedAnalysis"],
        "_6762": ["RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis"],
        "_6763": ["RollingRingAssemblyCompoundCriticalSpeedAnalysis"],
        "_6764": ["RollingRingCompoundCriticalSpeedAnalysis"],
        "_6765": ["RollingRingConnectionCompoundCriticalSpeedAnalysis"],
        "_6766": ["RootAssemblyCompoundCriticalSpeedAnalysis"],
        "_6767": ["ShaftCompoundCriticalSpeedAnalysis"],
        "_6768": ["ShaftHubConnectionCompoundCriticalSpeedAnalysis"],
        "_6769": ["ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis"],
        "_6770": ["SpecialisedAssemblyCompoundCriticalSpeedAnalysis"],
        "_6771": ["SpiralBevelGearCompoundCriticalSpeedAnalysis"],
        "_6772": ["SpiralBevelGearMeshCompoundCriticalSpeedAnalysis"],
        "_6773": ["SpiralBevelGearSetCompoundCriticalSpeedAnalysis"],
        "_6774": ["SpringDamperCompoundCriticalSpeedAnalysis"],
        "_6775": ["SpringDamperConnectionCompoundCriticalSpeedAnalysis"],
        "_6776": ["SpringDamperHalfCompoundCriticalSpeedAnalysis"],
        "_6777": ["StraightBevelDiffGearCompoundCriticalSpeedAnalysis"],
        "_6778": ["StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis"],
        "_6779": ["StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis"],
        "_6780": ["StraightBevelGearCompoundCriticalSpeedAnalysis"],
        "_6781": ["StraightBevelGearMeshCompoundCriticalSpeedAnalysis"],
        "_6782": ["StraightBevelGearSetCompoundCriticalSpeedAnalysis"],
        "_6783": ["StraightBevelPlanetGearCompoundCriticalSpeedAnalysis"],
        "_6784": ["StraightBevelSunGearCompoundCriticalSpeedAnalysis"],
        "_6785": ["SynchroniserCompoundCriticalSpeedAnalysis"],
        "_6786": ["SynchroniserHalfCompoundCriticalSpeedAnalysis"],
        "_6787": ["SynchroniserPartCompoundCriticalSpeedAnalysis"],
        "_6788": ["SynchroniserSleeveCompoundCriticalSpeedAnalysis"],
        "_6789": ["TorqueConverterCompoundCriticalSpeedAnalysis"],
        "_6790": ["TorqueConverterConnectionCompoundCriticalSpeedAnalysis"],
        "_6791": ["TorqueConverterPumpCompoundCriticalSpeedAnalysis"],
        "_6792": ["TorqueConverterTurbineCompoundCriticalSpeedAnalysis"],
        "_6793": ["UnbalancedMassCompoundCriticalSpeedAnalysis"],
        "_6794": ["VirtualComponentCompoundCriticalSpeedAnalysis"],
        "_6795": ["WormGearCompoundCriticalSpeedAnalysis"],
        "_6796": ["WormGearMeshCompoundCriticalSpeedAnalysis"],
        "_6797": ["WormGearSetCompoundCriticalSpeedAnalysis"],
        "_6798": ["ZerolBevelGearCompoundCriticalSpeedAnalysis"],
        "_6799": ["ZerolBevelGearMeshCompoundCriticalSpeedAnalysis"],
        "_6800": ["ZerolBevelGearSetCompoundCriticalSpeedAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundCriticalSpeedAnalysis",
    "AbstractShaftCompoundCriticalSpeedAnalysis",
    "AbstractShaftOrHousingCompoundCriticalSpeedAnalysis",
    "AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
    "AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis",
    "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
    "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
    "AssemblyCompoundCriticalSpeedAnalysis",
    "BearingCompoundCriticalSpeedAnalysis",
    "BeltConnectionCompoundCriticalSpeedAnalysis",
    "BeltDriveCompoundCriticalSpeedAnalysis",
    "BevelDifferentialGearCompoundCriticalSpeedAnalysis",
    "BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis",
    "BevelDifferentialGearSetCompoundCriticalSpeedAnalysis",
    "BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis",
    "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis",
    "BevelGearCompoundCriticalSpeedAnalysis",
    "BevelGearMeshCompoundCriticalSpeedAnalysis",
    "BevelGearSetCompoundCriticalSpeedAnalysis",
    "BoltCompoundCriticalSpeedAnalysis",
    "BoltedJointCompoundCriticalSpeedAnalysis",
    "ClutchCompoundCriticalSpeedAnalysis",
    "ClutchConnectionCompoundCriticalSpeedAnalysis",
    "ClutchHalfCompoundCriticalSpeedAnalysis",
    "CoaxialConnectionCompoundCriticalSpeedAnalysis",
    "ComponentCompoundCriticalSpeedAnalysis",
    "ConceptCouplingCompoundCriticalSpeedAnalysis",
    "ConceptCouplingConnectionCompoundCriticalSpeedAnalysis",
    "ConceptCouplingHalfCompoundCriticalSpeedAnalysis",
    "ConceptGearCompoundCriticalSpeedAnalysis",
    "ConceptGearMeshCompoundCriticalSpeedAnalysis",
    "ConceptGearSetCompoundCriticalSpeedAnalysis",
    "ConicalGearCompoundCriticalSpeedAnalysis",
    "ConicalGearMeshCompoundCriticalSpeedAnalysis",
    "ConicalGearSetCompoundCriticalSpeedAnalysis",
    "ConnectionCompoundCriticalSpeedAnalysis",
    "ConnectorCompoundCriticalSpeedAnalysis",
    "CouplingCompoundCriticalSpeedAnalysis",
    "CouplingConnectionCompoundCriticalSpeedAnalysis",
    "CouplingHalfCompoundCriticalSpeedAnalysis",
    "CVTBeltConnectionCompoundCriticalSpeedAnalysis",
    "CVTCompoundCriticalSpeedAnalysis",
    "CVTPulleyCompoundCriticalSpeedAnalysis",
    "CycloidalAssemblyCompoundCriticalSpeedAnalysis",
    "CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis",
    "CycloidalDiscCompoundCriticalSpeedAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionCompoundCriticalSpeedAnalysis",
    "CylindricalGearCompoundCriticalSpeedAnalysis",
    "CylindricalGearMeshCompoundCriticalSpeedAnalysis",
    "CylindricalGearSetCompoundCriticalSpeedAnalysis",
    "CylindricalPlanetGearCompoundCriticalSpeedAnalysis",
    "DatumCompoundCriticalSpeedAnalysis",
    "ExternalCADModelCompoundCriticalSpeedAnalysis",
    "FaceGearCompoundCriticalSpeedAnalysis",
    "FaceGearMeshCompoundCriticalSpeedAnalysis",
    "FaceGearSetCompoundCriticalSpeedAnalysis",
    "FEPartCompoundCriticalSpeedAnalysis",
    "FlexiblePinAssemblyCompoundCriticalSpeedAnalysis",
    "GearCompoundCriticalSpeedAnalysis",
    "GearMeshCompoundCriticalSpeedAnalysis",
    "GearSetCompoundCriticalSpeedAnalysis",
    "GuideDxfModelCompoundCriticalSpeedAnalysis",
    "HypoidGearCompoundCriticalSpeedAnalysis",
    "HypoidGearMeshCompoundCriticalSpeedAnalysis",
    "HypoidGearSetCompoundCriticalSpeedAnalysis",
    "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis",
    "MassDiscCompoundCriticalSpeedAnalysis",
    "MeasurementComponentCompoundCriticalSpeedAnalysis",
    "MountableComponentCompoundCriticalSpeedAnalysis",
    "OilSealCompoundCriticalSpeedAnalysis",
    "PartCompoundCriticalSpeedAnalysis",
    "PartToPartShearCouplingCompoundCriticalSpeedAnalysis",
    "PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis",
    "PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis",
    "PlanetaryConnectionCompoundCriticalSpeedAnalysis",
    "PlanetaryGearSetCompoundCriticalSpeedAnalysis",
    "PlanetCarrierCompoundCriticalSpeedAnalysis",
    "PointLoadCompoundCriticalSpeedAnalysis",
    "PowerLoadCompoundCriticalSpeedAnalysis",
    "PulleyCompoundCriticalSpeedAnalysis",
    "RingPinsCompoundCriticalSpeedAnalysis",
    "RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis",
    "RollingRingAssemblyCompoundCriticalSpeedAnalysis",
    "RollingRingCompoundCriticalSpeedAnalysis",
    "RollingRingConnectionCompoundCriticalSpeedAnalysis",
    "RootAssemblyCompoundCriticalSpeedAnalysis",
    "ShaftCompoundCriticalSpeedAnalysis",
    "ShaftHubConnectionCompoundCriticalSpeedAnalysis",
    "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
    "SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
    "SpiralBevelGearCompoundCriticalSpeedAnalysis",
    "SpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
    "SpiralBevelGearSetCompoundCriticalSpeedAnalysis",
    "SpringDamperCompoundCriticalSpeedAnalysis",
    "SpringDamperConnectionCompoundCriticalSpeedAnalysis",
    "SpringDamperHalfCompoundCriticalSpeedAnalysis",
    "StraightBevelDiffGearCompoundCriticalSpeedAnalysis",
    "StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis",
    "StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis",
    "StraightBevelGearCompoundCriticalSpeedAnalysis",
    "StraightBevelGearMeshCompoundCriticalSpeedAnalysis",
    "StraightBevelGearSetCompoundCriticalSpeedAnalysis",
    "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis",
    "StraightBevelSunGearCompoundCriticalSpeedAnalysis",
    "SynchroniserCompoundCriticalSpeedAnalysis",
    "SynchroniserHalfCompoundCriticalSpeedAnalysis",
    "SynchroniserPartCompoundCriticalSpeedAnalysis",
    "SynchroniserSleeveCompoundCriticalSpeedAnalysis",
    "TorqueConverterCompoundCriticalSpeedAnalysis",
    "TorqueConverterConnectionCompoundCriticalSpeedAnalysis",
    "TorqueConverterPumpCompoundCriticalSpeedAnalysis",
    "TorqueConverterTurbineCompoundCriticalSpeedAnalysis",
    "UnbalancedMassCompoundCriticalSpeedAnalysis",
    "VirtualComponentCompoundCriticalSpeedAnalysis",
    "WormGearCompoundCriticalSpeedAnalysis",
    "WormGearMeshCompoundCriticalSpeedAnalysis",
    "WormGearSetCompoundCriticalSpeedAnalysis",
    "ZerolBevelGearCompoundCriticalSpeedAnalysis",
    "ZerolBevelGearMeshCompoundCriticalSpeedAnalysis",
    "ZerolBevelGearSetCompoundCriticalSpeedAnalysis",
)
