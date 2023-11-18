"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2683 import AbstractAssemblySystemDeflection
    from ._2684 import AbstractShaftOrHousingSystemDeflection
    from ._2685 import AbstractShaftSystemDeflection
    from ._2686 import AbstractShaftToMountableComponentConnectionSystemDeflection
    from ._2687 import AGMAGleasonConicalGearMeshSystemDeflection
    from ._2688 import AGMAGleasonConicalGearSetSystemDeflection
    from ._2689 import AGMAGleasonConicalGearSystemDeflection
    from ._2690 import AssemblySystemDeflection
    from ._2691 import BearingDynamicElementContactPropertyWrapper
    from ._2692 import BearingDynamicElementPropertyWrapper
    from ._2693 import BearingDynamicPostAnalysisResultWrapper
    from ._2694 import BearingDynamicResultsPropertyWrapper
    from ._2695 import BearingDynamicResultsUIWrapper
    from ._2696 import BearingSystemDeflection
    from ._2697 import BeltConnectionSystemDeflection
    from ._2698 import BeltDriveSystemDeflection
    from ._2699 import BevelDifferentialGearMeshSystemDeflection
    from ._2700 import BevelDifferentialGearSetSystemDeflection
    from ._2701 import BevelDifferentialGearSystemDeflection
    from ._2702 import BevelDifferentialPlanetGearSystemDeflection
    from ._2703 import BevelDifferentialSunGearSystemDeflection
    from ._2704 import BevelGearMeshSystemDeflection
    from ._2705 import BevelGearSetSystemDeflection
    from ._2706 import BevelGearSystemDeflection
    from ._2707 import BoltedJointSystemDeflection
    from ._2708 import BoltSystemDeflection
    from ._2709 import ClutchConnectionSystemDeflection
    from ._2710 import ClutchHalfSystemDeflection
    from ._2711 import ClutchSystemDeflection
    from ._2712 import CoaxialConnectionSystemDeflection
    from ._2713 import ComponentSystemDeflection
    from ._2714 import ConcentricPartGroupCombinationSystemDeflectionResults
    from ._2715 import ConceptCouplingConnectionSystemDeflection
    from ._2716 import ConceptCouplingHalfSystemDeflection
    from ._2717 import ConceptCouplingSystemDeflection
    from ._2718 import ConceptGearMeshSystemDeflection
    from ._2719 import ConceptGearSetSystemDeflection
    from ._2720 import ConceptGearSystemDeflection
    from ._2721 import ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator
    from ._2722 import ConicalGearMeshSystemDeflection
    from ._2723 import ConicalGearSetSystemDeflection
    from ._2724 import ConicalGearSystemDeflection
    from ._2725 import ConnectionSystemDeflection
    from ._2726 import ConnectorSystemDeflection
    from ._2727 import CouplingConnectionSystemDeflection
    from ._2728 import CouplingHalfSystemDeflection
    from ._2729 import CouplingSystemDeflection
    from ._2730 import CVTBeltConnectionSystemDeflection
    from ._2731 import CVTPulleySystemDeflection
    from ._2732 import CVTSystemDeflection
    from ._2733 import CycloidalAssemblySystemDeflection
    from ._2734 import CycloidalDiscCentralBearingConnectionSystemDeflection
    from ._2735 import CycloidalDiscPlanetaryBearingConnectionSystemDeflection
    from ._2736 import CycloidalDiscSystemDeflection
    from ._2737 import CylindricalGearMeshSystemDeflection
    from ._2738 import CylindricalGearMeshSystemDeflectionTimestep
    from ._2739 import CylindricalGearMeshSystemDeflectionWithLTCAResults
    from ._2740 import CylindricalGearSetSystemDeflection
    from ._2741 import CylindricalGearSetSystemDeflectionTimestep
    from ._2742 import CylindricalGearSetSystemDeflectionWithLTCAResults
    from ._2743 import CylindricalGearSystemDeflection
    from ._2744 import CylindricalGearSystemDeflectionTimestep
    from ._2745 import CylindricalGearSystemDeflectionWithLTCAResults
    from ._2746 import CylindricalMeshedGearFlankSystemDeflection
    from ._2747 import CylindricalMeshedGearSystemDeflection
    from ._2748 import CylindricalPlanetGearSystemDeflection
    from ._2749 import DatumSystemDeflection
    from ._2750 import ExternalCADModelSystemDeflection
    from ._2751 import FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator
    from ._2752 import FaceGearMeshSystemDeflection
    from ._2753 import FaceGearSetSystemDeflection
    from ._2754 import FaceGearSystemDeflection
    from ._2755 import FEPartSystemDeflection
    from ._2756 import FlexiblePinAssemblySystemDeflection
    from ._2757 import GearMeshSystemDeflection
    from ._2758 import GearSetSystemDeflection
    from ._2759 import GearSystemDeflection
    from ._2760 import GuideDxfModelSystemDeflection
    from ._2761 import HypoidGearMeshSystemDeflection
    from ._2762 import HypoidGearSetSystemDeflection
    from ._2763 import HypoidGearSystemDeflection
    from ._2764 import InformationForContactAtPointAlongFaceWidth
    from ._2765 import InterMountableComponentConnectionSystemDeflection
    from ._2766 import KlingelnbergCycloPalloidConicalGearMeshSystemDeflection
    from ._2767 import KlingelnbergCycloPalloidConicalGearSetSystemDeflection
    from ._2768 import KlingelnbergCycloPalloidConicalGearSystemDeflection
    from ._2769 import KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection
    from ._2770 import KlingelnbergCycloPalloidHypoidGearSetSystemDeflection
    from ._2771 import KlingelnbergCycloPalloidHypoidGearSystemDeflection
    from ._2772 import KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection
    from ._2773 import KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection
    from ._2774 import KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection
    from ._2775 import LoadCaseOverallEfficiencyResult
    from ._2776 import LoadSharingFactorReporter
    from ._2777 import MassDiscSystemDeflection
    from ._2778 import MeasurementComponentSystemDeflection
    from ._2779 import MeshSeparationsAtFaceWidth
    from ._2780 import MountableComponentSystemDeflection
    from ._2781 import ObservedPinStiffnessReporter
    from ._2782 import OilSealSystemDeflection
    from ._2783 import PartSystemDeflection
    from ._2784 import PartToPartShearCouplingConnectionSystemDeflection
    from ._2785 import PartToPartShearCouplingHalfSystemDeflection
    from ._2786 import PartToPartShearCouplingSystemDeflection
    from ._2787 import PlanetaryConnectionSystemDeflection
    from ._2788 import PlanetCarrierSystemDeflection
    from ._2789 import PointLoadSystemDeflection
    from ._2790 import PowerLoadSystemDeflection
    from ._2791 import PulleySystemDeflection
    from ._2792 import RingPinsSystemDeflection
    from ._2793 import RingPinsToDiscConnectionSystemDeflection
    from ._2794 import RingPinToDiscContactReporting
    from ._2795 import RollingRingAssemblySystemDeflection
    from ._2796 import RollingRingConnectionSystemDeflection
    from ._2797 import RollingRingSystemDeflection
    from ._2798 import RootAssemblySystemDeflection
    from ._2799 import ShaftHubConnectionSystemDeflection
    from ._2800 import ShaftSectionEndResultsSystemDeflection
    from ._2801 import ShaftSectionSystemDeflection
    from ._2802 import ShaftSystemDeflection
    from ._2803 import ShaftToMountableComponentConnectionSystemDeflection
    from ._2804 import SpecialisedAssemblySystemDeflection
    from ._2805 import SpiralBevelGearMeshSystemDeflection
    from ._2806 import SpiralBevelGearSetSystemDeflection
    from ._2807 import SpiralBevelGearSystemDeflection
    from ._2808 import SpringDamperConnectionSystemDeflection
    from ._2809 import SpringDamperHalfSystemDeflection
    from ._2810 import SpringDamperSystemDeflection
    from ._2811 import StraightBevelDiffGearMeshSystemDeflection
    from ._2812 import StraightBevelDiffGearSetSystemDeflection
    from ._2813 import StraightBevelDiffGearSystemDeflection
    from ._2814 import StraightBevelGearMeshSystemDeflection
    from ._2815 import StraightBevelGearSetSystemDeflection
    from ._2816 import StraightBevelGearSystemDeflection
    from ._2817 import StraightBevelPlanetGearSystemDeflection
    from ._2818 import StraightBevelSunGearSystemDeflection
    from ._2819 import SynchroniserHalfSystemDeflection
    from ._2820 import SynchroniserPartSystemDeflection
    from ._2821 import SynchroniserSleeveSystemDeflection
    from ._2822 import SynchroniserSystemDeflection
    from ._2823 import SystemDeflection
    from ._2824 import SystemDeflectionDrawStyle
    from ._2825 import SystemDeflectionOptions
    from ._2826 import TorqueConverterConnectionSystemDeflection
    from ._2827 import TorqueConverterPumpSystemDeflection
    from ._2828 import TorqueConverterSystemDeflection
    from ._2829 import TorqueConverterTurbineSystemDeflection
    from ._2830 import TorsionalSystemDeflection
    from ._2831 import TransmissionErrorResult
    from ._2832 import UnbalancedMassSystemDeflection
    from ._2833 import VirtualComponentSystemDeflection
    from ._2834 import WormGearMeshSystemDeflection
    from ._2835 import WormGearSetSystemDeflection
    from ._2836 import WormGearSystemDeflection
    from ._2837 import ZerolBevelGearMeshSystemDeflection
    from ._2838 import ZerolBevelGearSetSystemDeflection
    from ._2839 import ZerolBevelGearSystemDeflection
else:
    import_structure = {
        "_2683": ["AbstractAssemblySystemDeflection"],
        "_2684": ["AbstractShaftOrHousingSystemDeflection"],
        "_2685": ["AbstractShaftSystemDeflection"],
        "_2686": ["AbstractShaftToMountableComponentConnectionSystemDeflection"],
        "_2687": ["AGMAGleasonConicalGearMeshSystemDeflection"],
        "_2688": ["AGMAGleasonConicalGearSetSystemDeflection"],
        "_2689": ["AGMAGleasonConicalGearSystemDeflection"],
        "_2690": ["AssemblySystemDeflection"],
        "_2691": ["BearingDynamicElementContactPropertyWrapper"],
        "_2692": ["BearingDynamicElementPropertyWrapper"],
        "_2693": ["BearingDynamicPostAnalysisResultWrapper"],
        "_2694": ["BearingDynamicResultsPropertyWrapper"],
        "_2695": ["BearingDynamicResultsUIWrapper"],
        "_2696": ["BearingSystemDeflection"],
        "_2697": ["BeltConnectionSystemDeflection"],
        "_2698": ["BeltDriveSystemDeflection"],
        "_2699": ["BevelDifferentialGearMeshSystemDeflection"],
        "_2700": ["BevelDifferentialGearSetSystemDeflection"],
        "_2701": ["BevelDifferentialGearSystemDeflection"],
        "_2702": ["BevelDifferentialPlanetGearSystemDeflection"],
        "_2703": ["BevelDifferentialSunGearSystemDeflection"],
        "_2704": ["BevelGearMeshSystemDeflection"],
        "_2705": ["BevelGearSetSystemDeflection"],
        "_2706": ["BevelGearSystemDeflection"],
        "_2707": ["BoltedJointSystemDeflection"],
        "_2708": ["BoltSystemDeflection"],
        "_2709": ["ClutchConnectionSystemDeflection"],
        "_2710": ["ClutchHalfSystemDeflection"],
        "_2711": ["ClutchSystemDeflection"],
        "_2712": ["CoaxialConnectionSystemDeflection"],
        "_2713": ["ComponentSystemDeflection"],
        "_2714": ["ConcentricPartGroupCombinationSystemDeflectionResults"],
        "_2715": ["ConceptCouplingConnectionSystemDeflection"],
        "_2716": ["ConceptCouplingHalfSystemDeflection"],
        "_2717": ["ConceptCouplingSystemDeflection"],
        "_2718": ["ConceptGearMeshSystemDeflection"],
        "_2719": ["ConceptGearSetSystemDeflection"],
        "_2720": ["ConceptGearSystemDeflection"],
        "_2721": ["ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator"],
        "_2722": ["ConicalGearMeshSystemDeflection"],
        "_2723": ["ConicalGearSetSystemDeflection"],
        "_2724": ["ConicalGearSystemDeflection"],
        "_2725": ["ConnectionSystemDeflection"],
        "_2726": ["ConnectorSystemDeflection"],
        "_2727": ["CouplingConnectionSystemDeflection"],
        "_2728": ["CouplingHalfSystemDeflection"],
        "_2729": ["CouplingSystemDeflection"],
        "_2730": ["CVTBeltConnectionSystemDeflection"],
        "_2731": ["CVTPulleySystemDeflection"],
        "_2732": ["CVTSystemDeflection"],
        "_2733": ["CycloidalAssemblySystemDeflection"],
        "_2734": ["CycloidalDiscCentralBearingConnectionSystemDeflection"],
        "_2735": ["CycloidalDiscPlanetaryBearingConnectionSystemDeflection"],
        "_2736": ["CycloidalDiscSystemDeflection"],
        "_2737": ["CylindricalGearMeshSystemDeflection"],
        "_2738": ["CylindricalGearMeshSystemDeflectionTimestep"],
        "_2739": ["CylindricalGearMeshSystemDeflectionWithLTCAResults"],
        "_2740": ["CylindricalGearSetSystemDeflection"],
        "_2741": ["CylindricalGearSetSystemDeflectionTimestep"],
        "_2742": ["CylindricalGearSetSystemDeflectionWithLTCAResults"],
        "_2743": ["CylindricalGearSystemDeflection"],
        "_2744": ["CylindricalGearSystemDeflectionTimestep"],
        "_2745": ["CylindricalGearSystemDeflectionWithLTCAResults"],
        "_2746": ["CylindricalMeshedGearFlankSystemDeflection"],
        "_2747": ["CylindricalMeshedGearSystemDeflection"],
        "_2748": ["CylindricalPlanetGearSystemDeflection"],
        "_2749": ["DatumSystemDeflection"],
        "_2750": ["ExternalCADModelSystemDeflection"],
        "_2751": ["FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator"],
        "_2752": ["FaceGearMeshSystemDeflection"],
        "_2753": ["FaceGearSetSystemDeflection"],
        "_2754": ["FaceGearSystemDeflection"],
        "_2755": ["FEPartSystemDeflection"],
        "_2756": ["FlexiblePinAssemblySystemDeflection"],
        "_2757": ["GearMeshSystemDeflection"],
        "_2758": ["GearSetSystemDeflection"],
        "_2759": ["GearSystemDeflection"],
        "_2760": ["GuideDxfModelSystemDeflection"],
        "_2761": ["HypoidGearMeshSystemDeflection"],
        "_2762": ["HypoidGearSetSystemDeflection"],
        "_2763": ["HypoidGearSystemDeflection"],
        "_2764": ["InformationForContactAtPointAlongFaceWidth"],
        "_2765": ["InterMountableComponentConnectionSystemDeflection"],
        "_2766": ["KlingelnbergCycloPalloidConicalGearMeshSystemDeflection"],
        "_2767": ["KlingelnbergCycloPalloidConicalGearSetSystemDeflection"],
        "_2768": ["KlingelnbergCycloPalloidConicalGearSystemDeflection"],
        "_2769": ["KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection"],
        "_2770": ["KlingelnbergCycloPalloidHypoidGearSetSystemDeflection"],
        "_2771": ["KlingelnbergCycloPalloidHypoidGearSystemDeflection"],
        "_2772": ["KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection"],
        "_2773": ["KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection"],
        "_2774": ["KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection"],
        "_2775": ["LoadCaseOverallEfficiencyResult"],
        "_2776": ["LoadSharingFactorReporter"],
        "_2777": ["MassDiscSystemDeflection"],
        "_2778": ["MeasurementComponentSystemDeflection"],
        "_2779": ["MeshSeparationsAtFaceWidth"],
        "_2780": ["MountableComponentSystemDeflection"],
        "_2781": ["ObservedPinStiffnessReporter"],
        "_2782": ["OilSealSystemDeflection"],
        "_2783": ["PartSystemDeflection"],
        "_2784": ["PartToPartShearCouplingConnectionSystemDeflection"],
        "_2785": ["PartToPartShearCouplingHalfSystemDeflection"],
        "_2786": ["PartToPartShearCouplingSystemDeflection"],
        "_2787": ["PlanetaryConnectionSystemDeflection"],
        "_2788": ["PlanetCarrierSystemDeflection"],
        "_2789": ["PointLoadSystemDeflection"],
        "_2790": ["PowerLoadSystemDeflection"],
        "_2791": ["PulleySystemDeflection"],
        "_2792": ["RingPinsSystemDeflection"],
        "_2793": ["RingPinsToDiscConnectionSystemDeflection"],
        "_2794": ["RingPinToDiscContactReporting"],
        "_2795": ["RollingRingAssemblySystemDeflection"],
        "_2796": ["RollingRingConnectionSystemDeflection"],
        "_2797": ["RollingRingSystemDeflection"],
        "_2798": ["RootAssemblySystemDeflection"],
        "_2799": ["ShaftHubConnectionSystemDeflection"],
        "_2800": ["ShaftSectionEndResultsSystemDeflection"],
        "_2801": ["ShaftSectionSystemDeflection"],
        "_2802": ["ShaftSystemDeflection"],
        "_2803": ["ShaftToMountableComponentConnectionSystemDeflection"],
        "_2804": ["SpecialisedAssemblySystemDeflection"],
        "_2805": ["SpiralBevelGearMeshSystemDeflection"],
        "_2806": ["SpiralBevelGearSetSystemDeflection"],
        "_2807": ["SpiralBevelGearSystemDeflection"],
        "_2808": ["SpringDamperConnectionSystemDeflection"],
        "_2809": ["SpringDamperHalfSystemDeflection"],
        "_2810": ["SpringDamperSystemDeflection"],
        "_2811": ["StraightBevelDiffGearMeshSystemDeflection"],
        "_2812": ["StraightBevelDiffGearSetSystemDeflection"],
        "_2813": ["StraightBevelDiffGearSystemDeflection"],
        "_2814": ["StraightBevelGearMeshSystemDeflection"],
        "_2815": ["StraightBevelGearSetSystemDeflection"],
        "_2816": ["StraightBevelGearSystemDeflection"],
        "_2817": ["StraightBevelPlanetGearSystemDeflection"],
        "_2818": ["StraightBevelSunGearSystemDeflection"],
        "_2819": ["SynchroniserHalfSystemDeflection"],
        "_2820": ["SynchroniserPartSystemDeflection"],
        "_2821": ["SynchroniserSleeveSystemDeflection"],
        "_2822": ["SynchroniserSystemDeflection"],
        "_2823": ["SystemDeflection"],
        "_2824": ["SystemDeflectionDrawStyle"],
        "_2825": ["SystemDeflectionOptions"],
        "_2826": ["TorqueConverterConnectionSystemDeflection"],
        "_2827": ["TorqueConverterPumpSystemDeflection"],
        "_2828": ["TorqueConverterSystemDeflection"],
        "_2829": ["TorqueConverterTurbineSystemDeflection"],
        "_2830": ["TorsionalSystemDeflection"],
        "_2831": ["TransmissionErrorResult"],
        "_2832": ["UnbalancedMassSystemDeflection"],
        "_2833": ["VirtualComponentSystemDeflection"],
        "_2834": ["WormGearMeshSystemDeflection"],
        "_2835": ["WormGearSetSystemDeflection"],
        "_2836": ["WormGearSystemDeflection"],
        "_2837": ["ZerolBevelGearMeshSystemDeflection"],
        "_2838": ["ZerolBevelGearSetSystemDeflection"],
        "_2839": ["ZerolBevelGearSystemDeflection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblySystemDeflection",
    "AbstractShaftOrHousingSystemDeflection",
    "AbstractShaftSystemDeflection",
    "AbstractShaftToMountableComponentConnectionSystemDeflection",
    "AGMAGleasonConicalGearMeshSystemDeflection",
    "AGMAGleasonConicalGearSetSystemDeflection",
    "AGMAGleasonConicalGearSystemDeflection",
    "AssemblySystemDeflection",
    "BearingDynamicElementContactPropertyWrapper",
    "BearingDynamicElementPropertyWrapper",
    "BearingDynamicPostAnalysisResultWrapper",
    "BearingDynamicResultsPropertyWrapper",
    "BearingDynamicResultsUIWrapper",
    "BearingSystemDeflection",
    "BeltConnectionSystemDeflection",
    "BeltDriveSystemDeflection",
    "BevelDifferentialGearMeshSystemDeflection",
    "BevelDifferentialGearSetSystemDeflection",
    "BevelDifferentialGearSystemDeflection",
    "BevelDifferentialPlanetGearSystemDeflection",
    "BevelDifferentialSunGearSystemDeflection",
    "BevelGearMeshSystemDeflection",
    "BevelGearSetSystemDeflection",
    "BevelGearSystemDeflection",
    "BoltedJointSystemDeflection",
    "BoltSystemDeflection",
    "ClutchConnectionSystemDeflection",
    "ClutchHalfSystemDeflection",
    "ClutchSystemDeflection",
    "CoaxialConnectionSystemDeflection",
    "ComponentSystemDeflection",
    "ConcentricPartGroupCombinationSystemDeflectionResults",
    "ConceptCouplingConnectionSystemDeflection",
    "ConceptCouplingHalfSystemDeflection",
    "ConceptCouplingSystemDeflection",
    "ConceptGearMeshSystemDeflection",
    "ConceptGearSetSystemDeflection",
    "ConceptGearSystemDeflection",
    "ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator",
    "ConicalGearMeshSystemDeflection",
    "ConicalGearSetSystemDeflection",
    "ConicalGearSystemDeflection",
    "ConnectionSystemDeflection",
    "ConnectorSystemDeflection",
    "CouplingConnectionSystemDeflection",
    "CouplingHalfSystemDeflection",
    "CouplingSystemDeflection",
    "CVTBeltConnectionSystemDeflection",
    "CVTPulleySystemDeflection",
    "CVTSystemDeflection",
    "CycloidalAssemblySystemDeflection",
    "CycloidalDiscCentralBearingConnectionSystemDeflection",
    "CycloidalDiscPlanetaryBearingConnectionSystemDeflection",
    "CycloidalDiscSystemDeflection",
    "CylindricalGearMeshSystemDeflection",
    "CylindricalGearMeshSystemDeflectionTimestep",
    "CylindricalGearMeshSystemDeflectionWithLTCAResults",
    "CylindricalGearSetSystemDeflection",
    "CylindricalGearSetSystemDeflectionTimestep",
    "CylindricalGearSetSystemDeflectionWithLTCAResults",
    "CylindricalGearSystemDeflection",
    "CylindricalGearSystemDeflectionTimestep",
    "CylindricalGearSystemDeflectionWithLTCAResults",
    "CylindricalMeshedGearFlankSystemDeflection",
    "CylindricalMeshedGearSystemDeflection",
    "CylindricalPlanetGearSystemDeflection",
    "DatumSystemDeflection",
    "ExternalCADModelSystemDeflection",
    "FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator",
    "FaceGearMeshSystemDeflection",
    "FaceGearSetSystemDeflection",
    "FaceGearSystemDeflection",
    "FEPartSystemDeflection",
    "FlexiblePinAssemblySystemDeflection",
    "GearMeshSystemDeflection",
    "GearSetSystemDeflection",
    "GearSystemDeflection",
    "GuideDxfModelSystemDeflection",
    "HypoidGearMeshSystemDeflection",
    "HypoidGearSetSystemDeflection",
    "HypoidGearSystemDeflection",
    "InformationForContactAtPointAlongFaceWidth",
    "InterMountableComponentConnectionSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearMeshSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearSetSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection",
    "LoadCaseOverallEfficiencyResult",
    "LoadSharingFactorReporter",
    "MassDiscSystemDeflection",
    "MeasurementComponentSystemDeflection",
    "MeshSeparationsAtFaceWidth",
    "MountableComponentSystemDeflection",
    "ObservedPinStiffnessReporter",
    "OilSealSystemDeflection",
    "PartSystemDeflection",
    "PartToPartShearCouplingConnectionSystemDeflection",
    "PartToPartShearCouplingHalfSystemDeflection",
    "PartToPartShearCouplingSystemDeflection",
    "PlanetaryConnectionSystemDeflection",
    "PlanetCarrierSystemDeflection",
    "PointLoadSystemDeflection",
    "PowerLoadSystemDeflection",
    "PulleySystemDeflection",
    "RingPinsSystemDeflection",
    "RingPinsToDiscConnectionSystemDeflection",
    "RingPinToDiscContactReporting",
    "RollingRingAssemblySystemDeflection",
    "RollingRingConnectionSystemDeflection",
    "RollingRingSystemDeflection",
    "RootAssemblySystemDeflection",
    "ShaftHubConnectionSystemDeflection",
    "ShaftSectionEndResultsSystemDeflection",
    "ShaftSectionSystemDeflection",
    "ShaftSystemDeflection",
    "ShaftToMountableComponentConnectionSystemDeflection",
    "SpecialisedAssemblySystemDeflection",
    "SpiralBevelGearMeshSystemDeflection",
    "SpiralBevelGearSetSystemDeflection",
    "SpiralBevelGearSystemDeflection",
    "SpringDamperConnectionSystemDeflection",
    "SpringDamperHalfSystemDeflection",
    "SpringDamperSystemDeflection",
    "StraightBevelDiffGearMeshSystemDeflection",
    "StraightBevelDiffGearSetSystemDeflection",
    "StraightBevelDiffGearSystemDeflection",
    "StraightBevelGearMeshSystemDeflection",
    "StraightBevelGearSetSystemDeflection",
    "StraightBevelGearSystemDeflection",
    "StraightBevelPlanetGearSystemDeflection",
    "StraightBevelSunGearSystemDeflection",
    "SynchroniserHalfSystemDeflection",
    "SynchroniserPartSystemDeflection",
    "SynchroniserSleeveSystemDeflection",
    "SynchroniserSystemDeflection",
    "SystemDeflection",
    "SystemDeflectionDrawStyle",
    "SystemDeflectionOptions",
    "TorqueConverterConnectionSystemDeflection",
    "TorqueConverterPumpSystemDeflection",
    "TorqueConverterSystemDeflection",
    "TorqueConverterTurbineSystemDeflection",
    "TorsionalSystemDeflection",
    "TransmissionErrorResult",
    "UnbalancedMassSystemDeflection",
    "VirtualComponentSystemDeflection",
    "WormGearMeshSystemDeflection",
    "WormGearSetSystemDeflection",
    "WormGearSystemDeflection",
    "ZerolBevelGearMeshSystemDeflection",
    "ZerolBevelGearSetSystemDeflection",
    "ZerolBevelGearSystemDeflection",
)
