"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5675 import AbstractAssemblyHarmonicAnalysis
    from ._5676 import AbstractPeriodicExcitationDetail
    from ._5677 import AbstractShaftHarmonicAnalysis
    from ._5678 import AbstractShaftOrHousingHarmonicAnalysis
    from ._5679 import AbstractShaftToMountableComponentConnectionHarmonicAnalysis
    from ._5680 import AGMAGleasonConicalGearHarmonicAnalysis
    from ._5681 import AGMAGleasonConicalGearMeshHarmonicAnalysis
    from ._5682 import AGMAGleasonConicalGearSetHarmonicAnalysis
    from ._5683 import AssemblyHarmonicAnalysis
    from ._5684 import BearingHarmonicAnalysis
    from ._5685 import BeltConnectionHarmonicAnalysis
    from ._5686 import BeltDriveHarmonicAnalysis
    from ._5687 import BevelDifferentialGearHarmonicAnalysis
    from ._5688 import BevelDifferentialGearMeshHarmonicAnalysis
    from ._5689 import BevelDifferentialGearSetHarmonicAnalysis
    from ._5690 import BevelDifferentialPlanetGearHarmonicAnalysis
    from ._5691 import BevelDifferentialSunGearHarmonicAnalysis
    from ._5692 import BevelGearHarmonicAnalysis
    from ._5693 import BevelGearMeshHarmonicAnalysis
    from ._5694 import BevelGearSetHarmonicAnalysis
    from ._5695 import BoltedJointHarmonicAnalysis
    from ._5696 import BoltHarmonicAnalysis
    from ._5697 import ClutchConnectionHarmonicAnalysis
    from ._5698 import ClutchHalfHarmonicAnalysis
    from ._5699 import ClutchHarmonicAnalysis
    from ._5700 import CoaxialConnectionHarmonicAnalysis
    from ._5701 import ComplianceAndForceData
    from ._5702 import ComponentHarmonicAnalysis
    from ._5703 import ConceptCouplingConnectionHarmonicAnalysis
    from ._5704 import ConceptCouplingHalfHarmonicAnalysis
    from ._5705 import ConceptCouplingHarmonicAnalysis
    from ._5706 import ConceptGearHarmonicAnalysis
    from ._5707 import ConceptGearMeshHarmonicAnalysis
    from ._5708 import ConceptGearSetHarmonicAnalysis
    from ._5709 import ConicalGearHarmonicAnalysis
    from ._5710 import ConicalGearMeshHarmonicAnalysis
    from ._5711 import ConicalGearSetHarmonicAnalysis
    from ._5712 import ConnectionHarmonicAnalysis
    from ._5713 import ConnectorHarmonicAnalysis
    from ._5714 import CouplingConnectionHarmonicAnalysis
    from ._5715 import CouplingHalfHarmonicAnalysis
    from ._5716 import CouplingHarmonicAnalysis
    from ._5717 import CVTBeltConnectionHarmonicAnalysis
    from ._5718 import CVTHarmonicAnalysis
    from ._5719 import CVTPulleyHarmonicAnalysis
    from ._5720 import CycloidalAssemblyHarmonicAnalysis
    from ._5721 import CycloidalDiscCentralBearingConnectionHarmonicAnalysis
    from ._5722 import CycloidalDiscHarmonicAnalysis
    from ._5723 import CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis
    from ._5724 import CylindricalGearHarmonicAnalysis
    from ._5725 import CylindricalGearMeshHarmonicAnalysis
    from ._5726 import CylindricalGearSetHarmonicAnalysis
    from ._5727 import CylindricalPlanetGearHarmonicAnalysis
    from ._5728 import DatumHarmonicAnalysis
    from ._5729 import DynamicModelForHarmonicAnalysis
    from ._5730 import ElectricMachinePeriodicExcitationDetail
    from ._5731 import ElectricMachineRotorXForcePeriodicExcitationDetail
    from ._5732 import ElectricMachineRotorXMomentPeriodicExcitationDetail
    from ._5733 import ElectricMachineRotorYForcePeriodicExcitationDetail
    from ._5734 import ElectricMachineRotorYMomentPeriodicExcitationDetail
    from ._5735 import ElectricMachineRotorZForcePeriodicExcitationDetail
    from ._5736 import ElectricMachineStatorToothAxialLoadsExcitationDetail
    from ._5737 import ElectricMachineStatorToothLoadsExcitationDetail
    from ._5738 import ElectricMachineStatorToothMomentsExcitationDetail
    from ._5739 import ElectricMachineStatorToothRadialLoadsExcitationDetail
    from ._5740 import ElectricMachineStatorToothTangentialLoadsExcitationDetail
    from ._5741 import ElectricMachineTorqueRipplePeriodicExcitationDetail
    from ._5742 import ExportOutputType
    from ._5743 import ExternalCADModelHarmonicAnalysis
    from ._5744 import FaceGearHarmonicAnalysis
    from ._5745 import FaceGearMeshHarmonicAnalysis
    from ._5746 import FaceGearSetHarmonicAnalysis
    from ._5747 import FEPartHarmonicAnalysis
    from ._5748 import FlexiblePinAssemblyHarmonicAnalysis
    from ._5749 import FrequencyOptionsForHarmonicAnalysisResults
    from ._5750 import GearHarmonicAnalysis
    from ._5751 import GearMeshExcitationDetail
    from ._5752 import GearMeshHarmonicAnalysis
    from ._5753 import GearMeshMisalignmentExcitationDetail
    from ._5754 import GearMeshTEExcitationDetail
    from ._5755 import GearSetHarmonicAnalysis
    from ._5756 import GeneralPeriodicExcitationDetail
    from ._5757 import GuideDxfModelHarmonicAnalysis
    from ._5758 import HarmonicAnalysis
    from ._5759 import HarmonicAnalysisDrawStyle
    from ._5760 import HarmonicAnalysisExportOptions
    from ._5761 import HarmonicAnalysisFEExportOptions
    from ._5762 import HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation
    from ._5763 import HarmonicAnalysisOptions
    from ._5764 import HarmonicAnalysisRootAssemblyExportOptions
    from ._5765 import HarmonicAnalysisShaftExportOptions
    from ._5766 import HarmonicAnalysisTorqueInputType
    from ._5767 import HarmonicAnalysisWithVaryingStiffnessStaticLoadCase
    from ._5768 import HypoidGearHarmonicAnalysis
    from ._5769 import HypoidGearMeshHarmonicAnalysis
    from ._5770 import HypoidGearSetHarmonicAnalysis
    from ._5771 import InterMountableComponentConnectionHarmonicAnalysis
    from ._5772 import KlingelnbergCycloPalloidConicalGearHarmonicAnalysis
    from ._5773 import KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis
    from ._5774 import KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis
    from ._5775 import KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis
    from ._5776 import KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis
    from ._5777 import KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis
    from ._5778 import KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis
    from ._5779 import KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis
    from ._5780 import KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis
    from ._5781 import MassDiscHarmonicAnalysis
    from ._5782 import MeasurementComponentHarmonicAnalysis
    from ._5783 import MountableComponentHarmonicAnalysis
    from ._5784 import OilSealHarmonicAnalysis
    from ._5785 import PartHarmonicAnalysis
    from ._5786 import PartToPartShearCouplingConnectionHarmonicAnalysis
    from ._5787 import PartToPartShearCouplingHalfHarmonicAnalysis
    from ._5788 import PartToPartShearCouplingHarmonicAnalysis
    from ._5789 import PeriodicExcitationWithReferenceShaft
    from ._5790 import PlanetaryConnectionHarmonicAnalysis
    from ._5791 import PlanetaryGearSetHarmonicAnalysis
    from ._5792 import PlanetCarrierHarmonicAnalysis
    from ._5793 import PointLoadHarmonicAnalysis
    from ._5794 import PowerLoadHarmonicAnalysis
    from ._5795 import PulleyHarmonicAnalysis
    from ._5796 import ResponseCacheLevel
    from ._5797 import RingPinsHarmonicAnalysis
    from ._5798 import RingPinsToDiscConnectionHarmonicAnalysis
    from ._5799 import RollingRingAssemblyHarmonicAnalysis
    from ._5800 import RollingRingConnectionHarmonicAnalysis
    from ._5801 import RollingRingHarmonicAnalysis
    from ._5802 import RootAssemblyHarmonicAnalysis
    from ._5803 import ShaftHarmonicAnalysis
    from ._5804 import ShaftHubConnectionHarmonicAnalysis
    from ._5805 import ShaftToMountableComponentConnectionHarmonicAnalysis
    from ._5806 import SingleNodePeriodicExcitationWithReferenceShaft
    from ._5807 import SpecialisedAssemblyHarmonicAnalysis
    from ._5808 import SpeedOptionsForHarmonicAnalysisResults
    from ._5809 import SpiralBevelGearHarmonicAnalysis
    from ._5810 import SpiralBevelGearMeshHarmonicAnalysis
    from ._5811 import SpiralBevelGearSetHarmonicAnalysis
    from ._5812 import SpringDamperConnectionHarmonicAnalysis
    from ._5813 import SpringDamperHalfHarmonicAnalysis
    from ._5814 import SpringDamperHarmonicAnalysis
    from ._5815 import StiffnessOptionsForHarmonicAnalysis
    from ._5816 import StraightBevelDiffGearHarmonicAnalysis
    from ._5817 import StraightBevelDiffGearMeshHarmonicAnalysis
    from ._5818 import StraightBevelDiffGearSetHarmonicAnalysis
    from ._5819 import StraightBevelGearHarmonicAnalysis
    from ._5820 import StraightBevelGearMeshHarmonicAnalysis
    from ._5821 import StraightBevelGearSetHarmonicAnalysis
    from ._5822 import StraightBevelPlanetGearHarmonicAnalysis
    from ._5823 import StraightBevelSunGearHarmonicAnalysis
    from ._5824 import SynchroniserHalfHarmonicAnalysis
    from ._5825 import SynchroniserHarmonicAnalysis
    from ._5826 import SynchroniserPartHarmonicAnalysis
    from ._5827 import SynchroniserSleeveHarmonicAnalysis
    from ._5828 import TorqueConverterConnectionHarmonicAnalysis
    from ._5829 import TorqueConverterHarmonicAnalysis
    from ._5830 import TorqueConverterPumpHarmonicAnalysis
    from ._5831 import TorqueConverterTurbineHarmonicAnalysis
    from ._5832 import UnbalancedMassExcitationDetail
    from ._5833 import UnbalancedMassHarmonicAnalysis
    from ._5834 import VirtualComponentHarmonicAnalysis
    from ._5835 import WormGearHarmonicAnalysis
    from ._5836 import WormGearMeshHarmonicAnalysis
    from ._5837 import WormGearSetHarmonicAnalysis
    from ._5838 import ZerolBevelGearHarmonicAnalysis
    from ._5839 import ZerolBevelGearMeshHarmonicAnalysis
    from ._5840 import ZerolBevelGearSetHarmonicAnalysis
else:
    import_structure = {
        "_5675": ["AbstractAssemblyHarmonicAnalysis"],
        "_5676": ["AbstractPeriodicExcitationDetail"],
        "_5677": ["AbstractShaftHarmonicAnalysis"],
        "_5678": ["AbstractShaftOrHousingHarmonicAnalysis"],
        "_5679": ["AbstractShaftToMountableComponentConnectionHarmonicAnalysis"],
        "_5680": ["AGMAGleasonConicalGearHarmonicAnalysis"],
        "_5681": ["AGMAGleasonConicalGearMeshHarmonicAnalysis"],
        "_5682": ["AGMAGleasonConicalGearSetHarmonicAnalysis"],
        "_5683": ["AssemblyHarmonicAnalysis"],
        "_5684": ["BearingHarmonicAnalysis"],
        "_5685": ["BeltConnectionHarmonicAnalysis"],
        "_5686": ["BeltDriveHarmonicAnalysis"],
        "_5687": ["BevelDifferentialGearHarmonicAnalysis"],
        "_5688": ["BevelDifferentialGearMeshHarmonicAnalysis"],
        "_5689": ["BevelDifferentialGearSetHarmonicAnalysis"],
        "_5690": ["BevelDifferentialPlanetGearHarmonicAnalysis"],
        "_5691": ["BevelDifferentialSunGearHarmonicAnalysis"],
        "_5692": ["BevelGearHarmonicAnalysis"],
        "_5693": ["BevelGearMeshHarmonicAnalysis"],
        "_5694": ["BevelGearSetHarmonicAnalysis"],
        "_5695": ["BoltedJointHarmonicAnalysis"],
        "_5696": ["BoltHarmonicAnalysis"],
        "_5697": ["ClutchConnectionHarmonicAnalysis"],
        "_5698": ["ClutchHalfHarmonicAnalysis"],
        "_5699": ["ClutchHarmonicAnalysis"],
        "_5700": ["CoaxialConnectionHarmonicAnalysis"],
        "_5701": ["ComplianceAndForceData"],
        "_5702": ["ComponentHarmonicAnalysis"],
        "_5703": ["ConceptCouplingConnectionHarmonicAnalysis"],
        "_5704": ["ConceptCouplingHalfHarmonicAnalysis"],
        "_5705": ["ConceptCouplingHarmonicAnalysis"],
        "_5706": ["ConceptGearHarmonicAnalysis"],
        "_5707": ["ConceptGearMeshHarmonicAnalysis"],
        "_5708": ["ConceptGearSetHarmonicAnalysis"],
        "_5709": ["ConicalGearHarmonicAnalysis"],
        "_5710": ["ConicalGearMeshHarmonicAnalysis"],
        "_5711": ["ConicalGearSetHarmonicAnalysis"],
        "_5712": ["ConnectionHarmonicAnalysis"],
        "_5713": ["ConnectorHarmonicAnalysis"],
        "_5714": ["CouplingConnectionHarmonicAnalysis"],
        "_5715": ["CouplingHalfHarmonicAnalysis"],
        "_5716": ["CouplingHarmonicAnalysis"],
        "_5717": ["CVTBeltConnectionHarmonicAnalysis"],
        "_5718": ["CVTHarmonicAnalysis"],
        "_5719": ["CVTPulleyHarmonicAnalysis"],
        "_5720": ["CycloidalAssemblyHarmonicAnalysis"],
        "_5721": ["CycloidalDiscCentralBearingConnectionHarmonicAnalysis"],
        "_5722": ["CycloidalDiscHarmonicAnalysis"],
        "_5723": ["CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis"],
        "_5724": ["CylindricalGearHarmonicAnalysis"],
        "_5725": ["CylindricalGearMeshHarmonicAnalysis"],
        "_5726": ["CylindricalGearSetHarmonicAnalysis"],
        "_5727": ["CylindricalPlanetGearHarmonicAnalysis"],
        "_5728": ["DatumHarmonicAnalysis"],
        "_5729": ["DynamicModelForHarmonicAnalysis"],
        "_5730": ["ElectricMachinePeriodicExcitationDetail"],
        "_5731": ["ElectricMachineRotorXForcePeriodicExcitationDetail"],
        "_5732": ["ElectricMachineRotorXMomentPeriodicExcitationDetail"],
        "_5733": ["ElectricMachineRotorYForcePeriodicExcitationDetail"],
        "_5734": ["ElectricMachineRotorYMomentPeriodicExcitationDetail"],
        "_5735": ["ElectricMachineRotorZForcePeriodicExcitationDetail"],
        "_5736": ["ElectricMachineStatorToothAxialLoadsExcitationDetail"],
        "_5737": ["ElectricMachineStatorToothLoadsExcitationDetail"],
        "_5738": ["ElectricMachineStatorToothMomentsExcitationDetail"],
        "_5739": ["ElectricMachineStatorToothRadialLoadsExcitationDetail"],
        "_5740": ["ElectricMachineStatorToothTangentialLoadsExcitationDetail"],
        "_5741": ["ElectricMachineTorqueRipplePeriodicExcitationDetail"],
        "_5742": ["ExportOutputType"],
        "_5743": ["ExternalCADModelHarmonicAnalysis"],
        "_5744": ["FaceGearHarmonicAnalysis"],
        "_5745": ["FaceGearMeshHarmonicAnalysis"],
        "_5746": ["FaceGearSetHarmonicAnalysis"],
        "_5747": ["FEPartHarmonicAnalysis"],
        "_5748": ["FlexiblePinAssemblyHarmonicAnalysis"],
        "_5749": ["FrequencyOptionsForHarmonicAnalysisResults"],
        "_5750": ["GearHarmonicAnalysis"],
        "_5751": ["GearMeshExcitationDetail"],
        "_5752": ["GearMeshHarmonicAnalysis"],
        "_5753": ["GearMeshMisalignmentExcitationDetail"],
        "_5754": ["GearMeshTEExcitationDetail"],
        "_5755": ["GearSetHarmonicAnalysis"],
        "_5756": ["GeneralPeriodicExcitationDetail"],
        "_5757": ["GuideDxfModelHarmonicAnalysis"],
        "_5758": ["HarmonicAnalysis"],
        "_5759": ["HarmonicAnalysisDrawStyle"],
        "_5760": ["HarmonicAnalysisExportOptions"],
        "_5761": ["HarmonicAnalysisFEExportOptions"],
        "_5762": ["HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation"],
        "_5763": ["HarmonicAnalysisOptions"],
        "_5764": ["HarmonicAnalysisRootAssemblyExportOptions"],
        "_5765": ["HarmonicAnalysisShaftExportOptions"],
        "_5766": ["HarmonicAnalysisTorqueInputType"],
        "_5767": ["HarmonicAnalysisWithVaryingStiffnessStaticLoadCase"],
        "_5768": ["HypoidGearHarmonicAnalysis"],
        "_5769": ["HypoidGearMeshHarmonicAnalysis"],
        "_5770": ["HypoidGearSetHarmonicAnalysis"],
        "_5771": ["InterMountableComponentConnectionHarmonicAnalysis"],
        "_5772": ["KlingelnbergCycloPalloidConicalGearHarmonicAnalysis"],
        "_5773": ["KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis"],
        "_5774": ["KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis"],
        "_5775": ["KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis"],
        "_5776": ["KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis"],
        "_5777": ["KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis"],
        "_5778": ["KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis"],
        "_5779": ["KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis"],
        "_5780": ["KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis"],
        "_5781": ["MassDiscHarmonicAnalysis"],
        "_5782": ["MeasurementComponentHarmonicAnalysis"],
        "_5783": ["MountableComponentHarmonicAnalysis"],
        "_5784": ["OilSealHarmonicAnalysis"],
        "_5785": ["PartHarmonicAnalysis"],
        "_5786": ["PartToPartShearCouplingConnectionHarmonicAnalysis"],
        "_5787": ["PartToPartShearCouplingHalfHarmonicAnalysis"],
        "_5788": ["PartToPartShearCouplingHarmonicAnalysis"],
        "_5789": ["PeriodicExcitationWithReferenceShaft"],
        "_5790": ["PlanetaryConnectionHarmonicAnalysis"],
        "_5791": ["PlanetaryGearSetHarmonicAnalysis"],
        "_5792": ["PlanetCarrierHarmonicAnalysis"],
        "_5793": ["PointLoadHarmonicAnalysis"],
        "_5794": ["PowerLoadHarmonicAnalysis"],
        "_5795": ["PulleyHarmonicAnalysis"],
        "_5796": ["ResponseCacheLevel"],
        "_5797": ["RingPinsHarmonicAnalysis"],
        "_5798": ["RingPinsToDiscConnectionHarmonicAnalysis"],
        "_5799": ["RollingRingAssemblyHarmonicAnalysis"],
        "_5800": ["RollingRingConnectionHarmonicAnalysis"],
        "_5801": ["RollingRingHarmonicAnalysis"],
        "_5802": ["RootAssemblyHarmonicAnalysis"],
        "_5803": ["ShaftHarmonicAnalysis"],
        "_5804": ["ShaftHubConnectionHarmonicAnalysis"],
        "_5805": ["ShaftToMountableComponentConnectionHarmonicAnalysis"],
        "_5806": ["SingleNodePeriodicExcitationWithReferenceShaft"],
        "_5807": ["SpecialisedAssemblyHarmonicAnalysis"],
        "_5808": ["SpeedOptionsForHarmonicAnalysisResults"],
        "_5809": ["SpiralBevelGearHarmonicAnalysis"],
        "_5810": ["SpiralBevelGearMeshHarmonicAnalysis"],
        "_5811": ["SpiralBevelGearSetHarmonicAnalysis"],
        "_5812": ["SpringDamperConnectionHarmonicAnalysis"],
        "_5813": ["SpringDamperHalfHarmonicAnalysis"],
        "_5814": ["SpringDamperHarmonicAnalysis"],
        "_5815": ["StiffnessOptionsForHarmonicAnalysis"],
        "_5816": ["StraightBevelDiffGearHarmonicAnalysis"],
        "_5817": ["StraightBevelDiffGearMeshHarmonicAnalysis"],
        "_5818": ["StraightBevelDiffGearSetHarmonicAnalysis"],
        "_5819": ["StraightBevelGearHarmonicAnalysis"],
        "_5820": ["StraightBevelGearMeshHarmonicAnalysis"],
        "_5821": ["StraightBevelGearSetHarmonicAnalysis"],
        "_5822": ["StraightBevelPlanetGearHarmonicAnalysis"],
        "_5823": ["StraightBevelSunGearHarmonicAnalysis"],
        "_5824": ["SynchroniserHalfHarmonicAnalysis"],
        "_5825": ["SynchroniserHarmonicAnalysis"],
        "_5826": ["SynchroniserPartHarmonicAnalysis"],
        "_5827": ["SynchroniserSleeveHarmonicAnalysis"],
        "_5828": ["TorqueConverterConnectionHarmonicAnalysis"],
        "_5829": ["TorqueConverterHarmonicAnalysis"],
        "_5830": ["TorqueConverterPumpHarmonicAnalysis"],
        "_5831": ["TorqueConverterTurbineHarmonicAnalysis"],
        "_5832": ["UnbalancedMassExcitationDetail"],
        "_5833": ["UnbalancedMassHarmonicAnalysis"],
        "_5834": ["VirtualComponentHarmonicAnalysis"],
        "_5835": ["WormGearHarmonicAnalysis"],
        "_5836": ["WormGearMeshHarmonicAnalysis"],
        "_5837": ["WormGearSetHarmonicAnalysis"],
        "_5838": ["ZerolBevelGearHarmonicAnalysis"],
        "_5839": ["ZerolBevelGearMeshHarmonicAnalysis"],
        "_5840": ["ZerolBevelGearSetHarmonicAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyHarmonicAnalysis",
    "AbstractPeriodicExcitationDetail",
    "AbstractShaftHarmonicAnalysis",
    "AbstractShaftOrHousingHarmonicAnalysis",
    "AbstractShaftToMountableComponentConnectionHarmonicAnalysis",
    "AGMAGleasonConicalGearHarmonicAnalysis",
    "AGMAGleasonConicalGearMeshHarmonicAnalysis",
    "AGMAGleasonConicalGearSetHarmonicAnalysis",
    "AssemblyHarmonicAnalysis",
    "BearingHarmonicAnalysis",
    "BeltConnectionHarmonicAnalysis",
    "BeltDriveHarmonicAnalysis",
    "BevelDifferentialGearHarmonicAnalysis",
    "BevelDifferentialGearMeshHarmonicAnalysis",
    "BevelDifferentialGearSetHarmonicAnalysis",
    "BevelDifferentialPlanetGearHarmonicAnalysis",
    "BevelDifferentialSunGearHarmonicAnalysis",
    "BevelGearHarmonicAnalysis",
    "BevelGearMeshHarmonicAnalysis",
    "BevelGearSetHarmonicAnalysis",
    "BoltedJointHarmonicAnalysis",
    "BoltHarmonicAnalysis",
    "ClutchConnectionHarmonicAnalysis",
    "ClutchHalfHarmonicAnalysis",
    "ClutchHarmonicAnalysis",
    "CoaxialConnectionHarmonicAnalysis",
    "ComplianceAndForceData",
    "ComponentHarmonicAnalysis",
    "ConceptCouplingConnectionHarmonicAnalysis",
    "ConceptCouplingHalfHarmonicAnalysis",
    "ConceptCouplingHarmonicAnalysis",
    "ConceptGearHarmonicAnalysis",
    "ConceptGearMeshHarmonicAnalysis",
    "ConceptGearSetHarmonicAnalysis",
    "ConicalGearHarmonicAnalysis",
    "ConicalGearMeshHarmonicAnalysis",
    "ConicalGearSetHarmonicAnalysis",
    "ConnectionHarmonicAnalysis",
    "ConnectorHarmonicAnalysis",
    "CouplingConnectionHarmonicAnalysis",
    "CouplingHalfHarmonicAnalysis",
    "CouplingHarmonicAnalysis",
    "CVTBeltConnectionHarmonicAnalysis",
    "CVTHarmonicAnalysis",
    "CVTPulleyHarmonicAnalysis",
    "CycloidalAssemblyHarmonicAnalysis",
    "CycloidalDiscCentralBearingConnectionHarmonicAnalysis",
    "CycloidalDiscHarmonicAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis",
    "CylindricalGearHarmonicAnalysis",
    "CylindricalGearMeshHarmonicAnalysis",
    "CylindricalGearSetHarmonicAnalysis",
    "CylindricalPlanetGearHarmonicAnalysis",
    "DatumHarmonicAnalysis",
    "DynamicModelForHarmonicAnalysis",
    "ElectricMachinePeriodicExcitationDetail",
    "ElectricMachineRotorXForcePeriodicExcitationDetail",
    "ElectricMachineRotorXMomentPeriodicExcitationDetail",
    "ElectricMachineRotorYForcePeriodicExcitationDetail",
    "ElectricMachineRotorYMomentPeriodicExcitationDetail",
    "ElectricMachineRotorZForcePeriodicExcitationDetail",
    "ElectricMachineStatorToothAxialLoadsExcitationDetail",
    "ElectricMachineStatorToothLoadsExcitationDetail",
    "ElectricMachineStatorToothMomentsExcitationDetail",
    "ElectricMachineStatorToothRadialLoadsExcitationDetail",
    "ElectricMachineStatorToothTangentialLoadsExcitationDetail",
    "ElectricMachineTorqueRipplePeriodicExcitationDetail",
    "ExportOutputType",
    "ExternalCADModelHarmonicAnalysis",
    "FaceGearHarmonicAnalysis",
    "FaceGearMeshHarmonicAnalysis",
    "FaceGearSetHarmonicAnalysis",
    "FEPartHarmonicAnalysis",
    "FlexiblePinAssemblyHarmonicAnalysis",
    "FrequencyOptionsForHarmonicAnalysisResults",
    "GearHarmonicAnalysis",
    "GearMeshExcitationDetail",
    "GearMeshHarmonicAnalysis",
    "GearMeshMisalignmentExcitationDetail",
    "GearMeshTEExcitationDetail",
    "GearSetHarmonicAnalysis",
    "GeneralPeriodicExcitationDetail",
    "GuideDxfModelHarmonicAnalysis",
    "HarmonicAnalysis",
    "HarmonicAnalysisDrawStyle",
    "HarmonicAnalysisExportOptions",
    "HarmonicAnalysisFEExportOptions",
    "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
    "HarmonicAnalysisOptions",
    "HarmonicAnalysisRootAssemblyExportOptions",
    "HarmonicAnalysisShaftExportOptions",
    "HarmonicAnalysisTorqueInputType",
    "HarmonicAnalysisWithVaryingStiffnessStaticLoadCase",
    "HypoidGearHarmonicAnalysis",
    "HypoidGearMeshHarmonicAnalysis",
    "HypoidGearSetHarmonicAnalysis",
    "InterMountableComponentConnectionHarmonicAnalysis",
    "KlingelnbergCycloPalloidConicalGearHarmonicAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis",
    "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis",
    "MassDiscHarmonicAnalysis",
    "MeasurementComponentHarmonicAnalysis",
    "MountableComponentHarmonicAnalysis",
    "OilSealHarmonicAnalysis",
    "PartHarmonicAnalysis",
    "PartToPartShearCouplingConnectionHarmonicAnalysis",
    "PartToPartShearCouplingHalfHarmonicAnalysis",
    "PartToPartShearCouplingHarmonicAnalysis",
    "PeriodicExcitationWithReferenceShaft",
    "PlanetaryConnectionHarmonicAnalysis",
    "PlanetaryGearSetHarmonicAnalysis",
    "PlanetCarrierHarmonicAnalysis",
    "PointLoadHarmonicAnalysis",
    "PowerLoadHarmonicAnalysis",
    "PulleyHarmonicAnalysis",
    "ResponseCacheLevel",
    "RingPinsHarmonicAnalysis",
    "RingPinsToDiscConnectionHarmonicAnalysis",
    "RollingRingAssemblyHarmonicAnalysis",
    "RollingRingConnectionHarmonicAnalysis",
    "RollingRingHarmonicAnalysis",
    "RootAssemblyHarmonicAnalysis",
    "ShaftHarmonicAnalysis",
    "ShaftHubConnectionHarmonicAnalysis",
    "ShaftToMountableComponentConnectionHarmonicAnalysis",
    "SingleNodePeriodicExcitationWithReferenceShaft",
    "SpecialisedAssemblyHarmonicAnalysis",
    "SpeedOptionsForHarmonicAnalysisResults",
    "SpiralBevelGearHarmonicAnalysis",
    "SpiralBevelGearMeshHarmonicAnalysis",
    "SpiralBevelGearSetHarmonicAnalysis",
    "SpringDamperConnectionHarmonicAnalysis",
    "SpringDamperHalfHarmonicAnalysis",
    "SpringDamperHarmonicAnalysis",
    "StiffnessOptionsForHarmonicAnalysis",
    "StraightBevelDiffGearHarmonicAnalysis",
    "StraightBevelDiffGearMeshHarmonicAnalysis",
    "StraightBevelDiffGearSetHarmonicAnalysis",
    "StraightBevelGearHarmonicAnalysis",
    "StraightBevelGearMeshHarmonicAnalysis",
    "StraightBevelGearSetHarmonicAnalysis",
    "StraightBevelPlanetGearHarmonicAnalysis",
    "StraightBevelSunGearHarmonicAnalysis",
    "SynchroniserHalfHarmonicAnalysis",
    "SynchroniserHarmonicAnalysis",
    "SynchroniserPartHarmonicAnalysis",
    "SynchroniserSleeveHarmonicAnalysis",
    "TorqueConverterConnectionHarmonicAnalysis",
    "TorqueConverterHarmonicAnalysis",
    "TorqueConverterPumpHarmonicAnalysis",
    "TorqueConverterTurbineHarmonicAnalysis",
    "UnbalancedMassExcitationDetail",
    "UnbalancedMassHarmonicAnalysis",
    "VirtualComponentHarmonicAnalysis",
    "WormGearHarmonicAnalysis",
    "WormGearMeshHarmonicAnalysis",
    "WormGearSetHarmonicAnalysis",
    "ZerolBevelGearHarmonicAnalysis",
    "ZerolBevelGearMeshHarmonicAnalysis",
    "ZerolBevelGearSetHarmonicAnalysis",
)
