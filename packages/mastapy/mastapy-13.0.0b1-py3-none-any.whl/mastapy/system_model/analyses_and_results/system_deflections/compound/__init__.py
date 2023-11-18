"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2849 import AbstractAssemblyCompoundSystemDeflection
    from ._2850 import AbstractShaftCompoundSystemDeflection
    from ._2851 import AbstractShaftOrHousingCompoundSystemDeflection
    from ._2852 import (
        AbstractShaftToMountableComponentConnectionCompoundSystemDeflection,
    )
    from ._2853 import AGMAGleasonConicalGearCompoundSystemDeflection
    from ._2854 import AGMAGleasonConicalGearMeshCompoundSystemDeflection
    from ._2855 import AGMAGleasonConicalGearSetCompoundSystemDeflection
    from ._2856 import AssemblyCompoundSystemDeflection
    from ._2857 import BearingCompoundSystemDeflection
    from ._2858 import BeltConnectionCompoundSystemDeflection
    from ._2859 import BeltDriveCompoundSystemDeflection
    from ._2860 import BevelDifferentialGearCompoundSystemDeflection
    from ._2861 import BevelDifferentialGearMeshCompoundSystemDeflection
    from ._2862 import BevelDifferentialGearSetCompoundSystemDeflection
    from ._2863 import BevelDifferentialPlanetGearCompoundSystemDeflection
    from ._2864 import BevelDifferentialSunGearCompoundSystemDeflection
    from ._2865 import BevelGearCompoundSystemDeflection
    from ._2866 import BevelGearMeshCompoundSystemDeflection
    from ._2867 import BevelGearSetCompoundSystemDeflection
    from ._2868 import BoltCompoundSystemDeflection
    from ._2869 import BoltedJointCompoundSystemDeflection
    from ._2870 import ClutchCompoundSystemDeflection
    from ._2871 import ClutchConnectionCompoundSystemDeflection
    from ._2872 import ClutchHalfCompoundSystemDeflection
    from ._2873 import CoaxialConnectionCompoundSystemDeflection
    from ._2874 import ComponentCompoundSystemDeflection
    from ._2875 import ConceptCouplingCompoundSystemDeflection
    from ._2876 import ConceptCouplingConnectionCompoundSystemDeflection
    from ._2877 import ConceptCouplingHalfCompoundSystemDeflection
    from ._2878 import ConceptGearCompoundSystemDeflection
    from ._2879 import ConceptGearMeshCompoundSystemDeflection
    from ._2880 import ConceptGearSetCompoundSystemDeflection
    from ._2881 import ConicalGearCompoundSystemDeflection
    from ._2882 import ConicalGearMeshCompoundSystemDeflection
    from ._2883 import ConicalGearSetCompoundSystemDeflection
    from ._2884 import ConnectionCompoundSystemDeflection
    from ._2885 import ConnectorCompoundSystemDeflection
    from ._2886 import CouplingCompoundSystemDeflection
    from ._2887 import CouplingConnectionCompoundSystemDeflection
    from ._2888 import CouplingHalfCompoundSystemDeflection
    from ._2889 import CVTBeltConnectionCompoundSystemDeflection
    from ._2890 import CVTCompoundSystemDeflection
    from ._2891 import CVTPulleyCompoundSystemDeflection
    from ._2892 import CycloidalAssemblyCompoundSystemDeflection
    from ._2893 import CycloidalDiscCentralBearingConnectionCompoundSystemDeflection
    from ._2894 import CycloidalDiscCompoundSystemDeflection
    from ._2895 import CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection
    from ._2896 import CylindricalGearCompoundSystemDeflection
    from ._2897 import CylindricalGearMeshCompoundSystemDeflection
    from ._2898 import CylindricalGearSetCompoundSystemDeflection
    from ._2899 import CylindricalPlanetGearCompoundSystemDeflection
    from ._2900 import DatumCompoundSystemDeflection
    from ._2901 import DutyCycleEfficiencyResults
    from ._2902 import ExternalCADModelCompoundSystemDeflection
    from ._2903 import FaceGearCompoundSystemDeflection
    from ._2904 import FaceGearMeshCompoundSystemDeflection
    from ._2905 import FaceGearSetCompoundSystemDeflection
    from ._2906 import FEPartCompoundSystemDeflection
    from ._2907 import FlexiblePinAssemblyCompoundSystemDeflection
    from ._2908 import GearCompoundSystemDeflection
    from ._2909 import GearMeshCompoundSystemDeflection
    from ._2910 import GearSetCompoundSystemDeflection
    from ._2911 import GuideDxfModelCompoundSystemDeflection
    from ._2912 import HypoidGearCompoundSystemDeflection
    from ._2913 import HypoidGearMeshCompoundSystemDeflection
    from ._2914 import HypoidGearSetCompoundSystemDeflection
    from ._2915 import InterMountableComponentConnectionCompoundSystemDeflection
    from ._2916 import KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection
    from ._2917 import KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection
    from ._2918 import KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection
    from ._2919 import KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection
    from ._2920 import KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection
    from ._2921 import KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection
    from ._2922 import KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection
    from ._2923 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection,
    )
    from ._2924 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection,
    )
    from ._2925 import MassDiscCompoundSystemDeflection
    from ._2926 import MeasurementComponentCompoundSystemDeflection
    from ._2927 import MountableComponentCompoundSystemDeflection
    from ._2928 import OilSealCompoundSystemDeflection
    from ._2929 import PartCompoundSystemDeflection
    from ._2930 import PartToPartShearCouplingCompoundSystemDeflection
    from ._2931 import PartToPartShearCouplingConnectionCompoundSystemDeflection
    from ._2932 import PartToPartShearCouplingHalfCompoundSystemDeflection
    from ._2933 import PlanetaryConnectionCompoundSystemDeflection
    from ._2934 import PlanetaryGearSetCompoundSystemDeflection
    from ._2935 import PlanetCarrierCompoundSystemDeflection
    from ._2936 import PointLoadCompoundSystemDeflection
    from ._2937 import PowerLoadCompoundSystemDeflection
    from ._2938 import PulleyCompoundSystemDeflection
    from ._2939 import RingPinsCompoundSystemDeflection
    from ._2940 import RingPinsToDiscConnectionCompoundSystemDeflection
    from ._2941 import RollingRingAssemblyCompoundSystemDeflection
    from ._2942 import RollingRingCompoundSystemDeflection
    from ._2943 import RollingRingConnectionCompoundSystemDeflection
    from ._2944 import RootAssemblyCompoundSystemDeflection
    from ._2945 import ShaftCompoundSystemDeflection
    from ._2946 import ShaftDutyCycleSystemDeflection
    from ._2947 import ShaftHubConnectionCompoundSystemDeflection
    from ._2948 import ShaftToMountableComponentConnectionCompoundSystemDeflection
    from ._2949 import SpecialisedAssemblyCompoundSystemDeflection
    from ._2950 import SpiralBevelGearCompoundSystemDeflection
    from ._2951 import SpiralBevelGearMeshCompoundSystemDeflection
    from ._2952 import SpiralBevelGearSetCompoundSystemDeflection
    from ._2953 import SpringDamperCompoundSystemDeflection
    from ._2954 import SpringDamperConnectionCompoundSystemDeflection
    from ._2955 import SpringDamperHalfCompoundSystemDeflection
    from ._2956 import StraightBevelDiffGearCompoundSystemDeflection
    from ._2957 import StraightBevelDiffGearMeshCompoundSystemDeflection
    from ._2958 import StraightBevelDiffGearSetCompoundSystemDeflection
    from ._2959 import StraightBevelGearCompoundSystemDeflection
    from ._2960 import StraightBevelGearMeshCompoundSystemDeflection
    from ._2961 import StraightBevelGearSetCompoundSystemDeflection
    from ._2962 import StraightBevelPlanetGearCompoundSystemDeflection
    from ._2963 import StraightBevelSunGearCompoundSystemDeflection
    from ._2964 import SynchroniserCompoundSystemDeflection
    from ._2965 import SynchroniserHalfCompoundSystemDeflection
    from ._2966 import SynchroniserPartCompoundSystemDeflection
    from ._2967 import SynchroniserSleeveCompoundSystemDeflection
    from ._2968 import TorqueConverterCompoundSystemDeflection
    from ._2969 import TorqueConverterConnectionCompoundSystemDeflection
    from ._2970 import TorqueConverterPumpCompoundSystemDeflection
    from ._2971 import TorqueConverterTurbineCompoundSystemDeflection
    from ._2972 import UnbalancedMassCompoundSystemDeflection
    from ._2973 import VirtualComponentCompoundSystemDeflection
    from ._2974 import WormGearCompoundSystemDeflection
    from ._2975 import WormGearMeshCompoundSystemDeflection
    from ._2976 import WormGearSetCompoundSystemDeflection
    from ._2977 import ZerolBevelGearCompoundSystemDeflection
    from ._2978 import ZerolBevelGearMeshCompoundSystemDeflection
    from ._2979 import ZerolBevelGearSetCompoundSystemDeflection
else:
    import_structure = {
        "_2849": ["AbstractAssemblyCompoundSystemDeflection"],
        "_2850": ["AbstractShaftCompoundSystemDeflection"],
        "_2851": ["AbstractShaftOrHousingCompoundSystemDeflection"],
        "_2852": [
            "AbstractShaftToMountableComponentConnectionCompoundSystemDeflection"
        ],
        "_2853": ["AGMAGleasonConicalGearCompoundSystemDeflection"],
        "_2854": ["AGMAGleasonConicalGearMeshCompoundSystemDeflection"],
        "_2855": ["AGMAGleasonConicalGearSetCompoundSystemDeflection"],
        "_2856": ["AssemblyCompoundSystemDeflection"],
        "_2857": ["BearingCompoundSystemDeflection"],
        "_2858": ["BeltConnectionCompoundSystemDeflection"],
        "_2859": ["BeltDriveCompoundSystemDeflection"],
        "_2860": ["BevelDifferentialGearCompoundSystemDeflection"],
        "_2861": ["BevelDifferentialGearMeshCompoundSystemDeflection"],
        "_2862": ["BevelDifferentialGearSetCompoundSystemDeflection"],
        "_2863": ["BevelDifferentialPlanetGearCompoundSystemDeflection"],
        "_2864": ["BevelDifferentialSunGearCompoundSystemDeflection"],
        "_2865": ["BevelGearCompoundSystemDeflection"],
        "_2866": ["BevelGearMeshCompoundSystemDeflection"],
        "_2867": ["BevelGearSetCompoundSystemDeflection"],
        "_2868": ["BoltCompoundSystemDeflection"],
        "_2869": ["BoltedJointCompoundSystemDeflection"],
        "_2870": ["ClutchCompoundSystemDeflection"],
        "_2871": ["ClutchConnectionCompoundSystemDeflection"],
        "_2872": ["ClutchHalfCompoundSystemDeflection"],
        "_2873": ["CoaxialConnectionCompoundSystemDeflection"],
        "_2874": ["ComponentCompoundSystemDeflection"],
        "_2875": ["ConceptCouplingCompoundSystemDeflection"],
        "_2876": ["ConceptCouplingConnectionCompoundSystemDeflection"],
        "_2877": ["ConceptCouplingHalfCompoundSystemDeflection"],
        "_2878": ["ConceptGearCompoundSystemDeflection"],
        "_2879": ["ConceptGearMeshCompoundSystemDeflection"],
        "_2880": ["ConceptGearSetCompoundSystemDeflection"],
        "_2881": ["ConicalGearCompoundSystemDeflection"],
        "_2882": ["ConicalGearMeshCompoundSystemDeflection"],
        "_2883": ["ConicalGearSetCompoundSystemDeflection"],
        "_2884": ["ConnectionCompoundSystemDeflection"],
        "_2885": ["ConnectorCompoundSystemDeflection"],
        "_2886": ["CouplingCompoundSystemDeflection"],
        "_2887": ["CouplingConnectionCompoundSystemDeflection"],
        "_2888": ["CouplingHalfCompoundSystemDeflection"],
        "_2889": ["CVTBeltConnectionCompoundSystemDeflection"],
        "_2890": ["CVTCompoundSystemDeflection"],
        "_2891": ["CVTPulleyCompoundSystemDeflection"],
        "_2892": ["CycloidalAssemblyCompoundSystemDeflection"],
        "_2893": ["CycloidalDiscCentralBearingConnectionCompoundSystemDeflection"],
        "_2894": ["CycloidalDiscCompoundSystemDeflection"],
        "_2895": ["CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection"],
        "_2896": ["CylindricalGearCompoundSystemDeflection"],
        "_2897": ["CylindricalGearMeshCompoundSystemDeflection"],
        "_2898": ["CylindricalGearSetCompoundSystemDeflection"],
        "_2899": ["CylindricalPlanetGearCompoundSystemDeflection"],
        "_2900": ["DatumCompoundSystemDeflection"],
        "_2901": ["DutyCycleEfficiencyResults"],
        "_2902": ["ExternalCADModelCompoundSystemDeflection"],
        "_2903": ["FaceGearCompoundSystemDeflection"],
        "_2904": ["FaceGearMeshCompoundSystemDeflection"],
        "_2905": ["FaceGearSetCompoundSystemDeflection"],
        "_2906": ["FEPartCompoundSystemDeflection"],
        "_2907": ["FlexiblePinAssemblyCompoundSystemDeflection"],
        "_2908": ["GearCompoundSystemDeflection"],
        "_2909": ["GearMeshCompoundSystemDeflection"],
        "_2910": ["GearSetCompoundSystemDeflection"],
        "_2911": ["GuideDxfModelCompoundSystemDeflection"],
        "_2912": ["HypoidGearCompoundSystemDeflection"],
        "_2913": ["HypoidGearMeshCompoundSystemDeflection"],
        "_2914": ["HypoidGearSetCompoundSystemDeflection"],
        "_2915": ["InterMountableComponentConnectionCompoundSystemDeflection"],
        "_2916": ["KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection"],
        "_2917": ["KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection"],
        "_2918": ["KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection"],
        "_2919": ["KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection"],
        "_2920": ["KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection"],
        "_2921": ["KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection"],
        "_2922": ["KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection"],
        "_2923": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection"
        ],
        "_2924": ["KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection"],
        "_2925": ["MassDiscCompoundSystemDeflection"],
        "_2926": ["MeasurementComponentCompoundSystemDeflection"],
        "_2927": ["MountableComponentCompoundSystemDeflection"],
        "_2928": ["OilSealCompoundSystemDeflection"],
        "_2929": ["PartCompoundSystemDeflection"],
        "_2930": ["PartToPartShearCouplingCompoundSystemDeflection"],
        "_2931": ["PartToPartShearCouplingConnectionCompoundSystemDeflection"],
        "_2932": ["PartToPartShearCouplingHalfCompoundSystemDeflection"],
        "_2933": ["PlanetaryConnectionCompoundSystemDeflection"],
        "_2934": ["PlanetaryGearSetCompoundSystemDeflection"],
        "_2935": ["PlanetCarrierCompoundSystemDeflection"],
        "_2936": ["PointLoadCompoundSystemDeflection"],
        "_2937": ["PowerLoadCompoundSystemDeflection"],
        "_2938": ["PulleyCompoundSystemDeflection"],
        "_2939": ["RingPinsCompoundSystemDeflection"],
        "_2940": ["RingPinsToDiscConnectionCompoundSystemDeflection"],
        "_2941": ["RollingRingAssemblyCompoundSystemDeflection"],
        "_2942": ["RollingRingCompoundSystemDeflection"],
        "_2943": ["RollingRingConnectionCompoundSystemDeflection"],
        "_2944": ["RootAssemblyCompoundSystemDeflection"],
        "_2945": ["ShaftCompoundSystemDeflection"],
        "_2946": ["ShaftDutyCycleSystemDeflection"],
        "_2947": ["ShaftHubConnectionCompoundSystemDeflection"],
        "_2948": ["ShaftToMountableComponentConnectionCompoundSystemDeflection"],
        "_2949": ["SpecialisedAssemblyCompoundSystemDeflection"],
        "_2950": ["SpiralBevelGearCompoundSystemDeflection"],
        "_2951": ["SpiralBevelGearMeshCompoundSystemDeflection"],
        "_2952": ["SpiralBevelGearSetCompoundSystemDeflection"],
        "_2953": ["SpringDamperCompoundSystemDeflection"],
        "_2954": ["SpringDamperConnectionCompoundSystemDeflection"],
        "_2955": ["SpringDamperHalfCompoundSystemDeflection"],
        "_2956": ["StraightBevelDiffGearCompoundSystemDeflection"],
        "_2957": ["StraightBevelDiffGearMeshCompoundSystemDeflection"],
        "_2958": ["StraightBevelDiffGearSetCompoundSystemDeflection"],
        "_2959": ["StraightBevelGearCompoundSystemDeflection"],
        "_2960": ["StraightBevelGearMeshCompoundSystemDeflection"],
        "_2961": ["StraightBevelGearSetCompoundSystemDeflection"],
        "_2962": ["StraightBevelPlanetGearCompoundSystemDeflection"],
        "_2963": ["StraightBevelSunGearCompoundSystemDeflection"],
        "_2964": ["SynchroniserCompoundSystemDeflection"],
        "_2965": ["SynchroniserHalfCompoundSystemDeflection"],
        "_2966": ["SynchroniserPartCompoundSystemDeflection"],
        "_2967": ["SynchroniserSleeveCompoundSystemDeflection"],
        "_2968": ["TorqueConverterCompoundSystemDeflection"],
        "_2969": ["TorqueConverterConnectionCompoundSystemDeflection"],
        "_2970": ["TorqueConverterPumpCompoundSystemDeflection"],
        "_2971": ["TorqueConverterTurbineCompoundSystemDeflection"],
        "_2972": ["UnbalancedMassCompoundSystemDeflection"],
        "_2973": ["VirtualComponentCompoundSystemDeflection"],
        "_2974": ["WormGearCompoundSystemDeflection"],
        "_2975": ["WormGearMeshCompoundSystemDeflection"],
        "_2976": ["WormGearSetCompoundSystemDeflection"],
        "_2977": ["ZerolBevelGearCompoundSystemDeflection"],
        "_2978": ["ZerolBevelGearMeshCompoundSystemDeflection"],
        "_2979": ["ZerolBevelGearSetCompoundSystemDeflection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundSystemDeflection",
    "AbstractShaftCompoundSystemDeflection",
    "AbstractShaftOrHousingCompoundSystemDeflection",
    "AbstractShaftToMountableComponentConnectionCompoundSystemDeflection",
    "AGMAGleasonConicalGearCompoundSystemDeflection",
    "AGMAGleasonConicalGearMeshCompoundSystemDeflection",
    "AGMAGleasonConicalGearSetCompoundSystemDeflection",
    "AssemblyCompoundSystemDeflection",
    "BearingCompoundSystemDeflection",
    "BeltConnectionCompoundSystemDeflection",
    "BeltDriveCompoundSystemDeflection",
    "BevelDifferentialGearCompoundSystemDeflection",
    "BevelDifferentialGearMeshCompoundSystemDeflection",
    "BevelDifferentialGearSetCompoundSystemDeflection",
    "BevelDifferentialPlanetGearCompoundSystemDeflection",
    "BevelDifferentialSunGearCompoundSystemDeflection",
    "BevelGearCompoundSystemDeflection",
    "BevelGearMeshCompoundSystemDeflection",
    "BevelGearSetCompoundSystemDeflection",
    "BoltCompoundSystemDeflection",
    "BoltedJointCompoundSystemDeflection",
    "ClutchCompoundSystemDeflection",
    "ClutchConnectionCompoundSystemDeflection",
    "ClutchHalfCompoundSystemDeflection",
    "CoaxialConnectionCompoundSystemDeflection",
    "ComponentCompoundSystemDeflection",
    "ConceptCouplingCompoundSystemDeflection",
    "ConceptCouplingConnectionCompoundSystemDeflection",
    "ConceptCouplingHalfCompoundSystemDeflection",
    "ConceptGearCompoundSystemDeflection",
    "ConceptGearMeshCompoundSystemDeflection",
    "ConceptGearSetCompoundSystemDeflection",
    "ConicalGearCompoundSystemDeflection",
    "ConicalGearMeshCompoundSystemDeflection",
    "ConicalGearSetCompoundSystemDeflection",
    "ConnectionCompoundSystemDeflection",
    "ConnectorCompoundSystemDeflection",
    "CouplingCompoundSystemDeflection",
    "CouplingConnectionCompoundSystemDeflection",
    "CouplingHalfCompoundSystemDeflection",
    "CVTBeltConnectionCompoundSystemDeflection",
    "CVTCompoundSystemDeflection",
    "CVTPulleyCompoundSystemDeflection",
    "CycloidalAssemblyCompoundSystemDeflection",
    "CycloidalDiscCentralBearingConnectionCompoundSystemDeflection",
    "CycloidalDiscCompoundSystemDeflection",
    "CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection",
    "CylindricalGearCompoundSystemDeflection",
    "CylindricalGearMeshCompoundSystemDeflection",
    "CylindricalGearSetCompoundSystemDeflection",
    "CylindricalPlanetGearCompoundSystemDeflection",
    "DatumCompoundSystemDeflection",
    "DutyCycleEfficiencyResults",
    "ExternalCADModelCompoundSystemDeflection",
    "FaceGearCompoundSystemDeflection",
    "FaceGearMeshCompoundSystemDeflection",
    "FaceGearSetCompoundSystemDeflection",
    "FEPartCompoundSystemDeflection",
    "FlexiblePinAssemblyCompoundSystemDeflection",
    "GearCompoundSystemDeflection",
    "GearMeshCompoundSystemDeflection",
    "GearSetCompoundSystemDeflection",
    "GuideDxfModelCompoundSystemDeflection",
    "HypoidGearCompoundSystemDeflection",
    "HypoidGearMeshCompoundSystemDeflection",
    "HypoidGearSetCompoundSystemDeflection",
    "InterMountableComponentConnectionCompoundSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection",
    "MassDiscCompoundSystemDeflection",
    "MeasurementComponentCompoundSystemDeflection",
    "MountableComponentCompoundSystemDeflection",
    "OilSealCompoundSystemDeflection",
    "PartCompoundSystemDeflection",
    "PartToPartShearCouplingCompoundSystemDeflection",
    "PartToPartShearCouplingConnectionCompoundSystemDeflection",
    "PartToPartShearCouplingHalfCompoundSystemDeflection",
    "PlanetaryConnectionCompoundSystemDeflection",
    "PlanetaryGearSetCompoundSystemDeflection",
    "PlanetCarrierCompoundSystemDeflection",
    "PointLoadCompoundSystemDeflection",
    "PowerLoadCompoundSystemDeflection",
    "PulleyCompoundSystemDeflection",
    "RingPinsCompoundSystemDeflection",
    "RingPinsToDiscConnectionCompoundSystemDeflection",
    "RollingRingAssemblyCompoundSystemDeflection",
    "RollingRingCompoundSystemDeflection",
    "RollingRingConnectionCompoundSystemDeflection",
    "RootAssemblyCompoundSystemDeflection",
    "ShaftCompoundSystemDeflection",
    "ShaftDutyCycleSystemDeflection",
    "ShaftHubConnectionCompoundSystemDeflection",
    "ShaftToMountableComponentConnectionCompoundSystemDeflection",
    "SpecialisedAssemblyCompoundSystemDeflection",
    "SpiralBevelGearCompoundSystemDeflection",
    "SpiralBevelGearMeshCompoundSystemDeflection",
    "SpiralBevelGearSetCompoundSystemDeflection",
    "SpringDamperCompoundSystemDeflection",
    "SpringDamperConnectionCompoundSystemDeflection",
    "SpringDamperHalfCompoundSystemDeflection",
    "StraightBevelDiffGearCompoundSystemDeflection",
    "StraightBevelDiffGearMeshCompoundSystemDeflection",
    "StraightBevelDiffGearSetCompoundSystemDeflection",
    "StraightBevelGearCompoundSystemDeflection",
    "StraightBevelGearMeshCompoundSystemDeflection",
    "StraightBevelGearSetCompoundSystemDeflection",
    "StraightBevelPlanetGearCompoundSystemDeflection",
    "StraightBevelSunGearCompoundSystemDeflection",
    "SynchroniserCompoundSystemDeflection",
    "SynchroniserHalfCompoundSystemDeflection",
    "SynchroniserPartCompoundSystemDeflection",
    "SynchroniserSleeveCompoundSystemDeflection",
    "TorqueConverterCompoundSystemDeflection",
    "TorqueConverterConnectionCompoundSystemDeflection",
    "TorqueConverterPumpCompoundSystemDeflection",
    "TorqueConverterTurbineCompoundSystemDeflection",
    "UnbalancedMassCompoundSystemDeflection",
    "VirtualComponentCompoundSystemDeflection",
    "WormGearCompoundSystemDeflection",
    "WormGearMeshCompoundSystemDeflection",
    "WormGearSetCompoundSystemDeflection",
    "ZerolBevelGearCompoundSystemDeflection",
    "ZerolBevelGearMeshCompoundSystemDeflection",
    "ZerolBevelGearSetCompoundSystemDeflection",
)
