"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5876 import AbstractAssemblyCompoundHarmonicAnalysis
    from ._5877 import AbstractShaftCompoundHarmonicAnalysis
    from ._5878 import AbstractShaftOrHousingCompoundHarmonicAnalysis
    from ._5879 import (
        AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis,
    )
    from ._5880 import AGMAGleasonConicalGearCompoundHarmonicAnalysis
    from ._5881 import AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis
    from ._5882 import AGMAGleasonConicalGearSetCompoundHarmonicAnalysis
    from ._5883 import AssemblyCompoundHarmonicAnalysis
    from ._5884 import BearingCompoundHarmonicAnalysis
    from ._5885 import BeltConnectionCompoundHarmonicAnalysis
    from ._5886 import BeltDriveCompoundHarmonicAnalysis
    from ._5887 import BevelDifferentialGearCompoundHarmonicAnalysis
    from ._5888 import BevelDifferentialGearMeshCompoundHarmonicAnalysis
    from ._5889 import BevelDifferentialGearSetCompoundHarmonicAnalysis
    from ._5890 import BevelDifferentialPlanetGearCompoundHarmonicAnalysis
    from ._5891 import BevelDifferentialSunGearCompoundHarmonicAnalysis
    from ._5892 import BevelGearCompoundHarmonicAnalysis
    from ._5893 import BevelGearMeshCompoundHarmonicAnalysis
    from ._5894 import BevelGearSetCompoundHarmonicAnalysis
    from ._5895 import BoltCompoundHarmonicAnalysis
    from ._5896 import BoltedJointCompoundHarmonicAnalysis
    from ._5897 import ClutchCompoundHarmonicAnalysis
    from ._5898 import ClutchConnectionCompoundHarmonicAnalysis
    from ._5899 import ClutchHalfCompoundHarmonicAnalysis
    from ._5900 import CoaxialConnectionCompoundHarmonicAnalysis
    from ._5901 import ComponentCompoundHarmonicAnalysis
    from ._5902 import ConceptCouplingCompoundHarmonicAnalysis
    from ._5903 import ConceptCouplingConnectionCompoundHarmonicAnalysis
    from ._5904 import ConceptCouplingHalfCompoundHarmonicAnalysis
    from ._5905 import ConceptGearCompoundHarmonicAnalysis
    from ._5906 import ConceptGearMeshCompoundHarmonicAnalysis
    from ._5907 import ConceptGearSetCompoundHarmonicAnalysis
    from ._5908 import ConicalGearCompoundHarmonicAnalysis
    from ._5909 import ConicalGearMeshCompoundHarmonicAnalysis
    from ._5910 import ConicalGearSetCompoundHarmonicAnalysis
    from ._5911 import ConnectionCompoundHarmonicAnalysis
    from ._5912 import ConnectorCompoundHarmonicAnalysis
    from ._5913 import CouplingCompoundHarmonicAnalysis
    from ._5914 import CouplingConnectionCompoundHarmonicAnalysis
    from ._5915 import CouplingHalfCompoundHarmonicAnalysis
    from ._5916 import CVTBeltConnectionCompoundHarmonicAnalysis
    from ._5917 import CVTCompoundHarmonicAnalysis
    from ._5918 import CVTPulleyCompoundHarmonicAnalysis
    from ._5919 import CycloidalAssemblyCompoundHarmonicAnalysis
    from ._5920 import CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis
    from ._5921 import CycloidalDiscCompoundHarmonicAnalysis
    from ._5922 import CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysis
    from ._5923 import CylindricalGearCompoundHarmonicAnalysis
    from ._5924 import CylindricalGearMeshCompoundHarmonicAnalysis
    from ._5925 import CylindricalGearSetCompoundHarmonicAnalysis
    from ._5926 import CylindricalPlanetGearCompoundHarmonicAnalysis
    from ._5927 import DatumCompoundHarmonicAnalysis
    from ._5928 import ExternalCADModelCompoundHarmonicAnalysis
    from ._5929 import FaceGearCompoundHarmonicAnalysis
    from ._5930 import FaceGearMeshCompoundHarmonicAnalysis
    from ._5931 import FaceGearSetCompoundHarmonicAnalysis
    from ._5932 import FEPartCompoundHarmonicAnalysis
    from ._5933 import FlexiblePinAssemblyCompoundHarmonicAnalysis
    from ._5934 import GearCompoundHarmonicAnalysis
    from ._5935 import GearMeshCompoundHarmonicAnalysis
    from ._5936 import GearSetCompoundHarmonicAnalysis
    from ._5937 import GuideDxfModelCompoundHarmonicAnalysis
    from ._5938 import HypoidGearCompoundHarmonicAnalysis
    from ._5939 import HypoidGearMeshCompoundHarmonicAnalysis
    from ._5940 import HypoidGearSetCompoundHarmonicAnalysis
    from ._5941 import InterMountableComponentConnectionCompoundHarmonicAnalysis
    from ._5942 import KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis
    from ._5943 import KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis
    from ._5944 import KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis
    from ._5945 import KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis
    from ._5946 import KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis
    from ._5947 import KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis
    from ._5948 import KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis
    from ._5949 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis,
    )
    from ._5950 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis,
    )
    from ._5951 import MassDiscCompoundHarmonicAnalysis
    from ._5952 import MeasurementComponentCompoundHarmonicAnalysis
    from ._5953 import MountableComponentCompoundHarmonicAnalysis
    from ._5954 import OilSealCompoundHarmonicAnalysis
    from ._5955 import PartCompoundHarmonicAnalysis
    from ._5956 import PartToPartShearCouplingCompoundHarmonicAnalysis
    from ._5957 import PartToPartShearCouplingConnectionCompoundHarmonicAnalysis
    from ._5958 import PartToPartShearCouplingHalfCompoundHarmonicAnalysis
    from ._5959 import PlanetaryConnectionCompoundHarmonicAnalysis
    from ._5960 import PlanetaryGearSetCompoundHarmonicAnalysis
    from ._5961 import PlanetCarrierCompoundHarmonicAnalysis
    from ._5962 import PointLoadCompoundHarmonicAnalysis
    from ._5963 import PowerLoadCompoundHarmonicAnalysis
    from ._5964 import PulleyCompoundHarmonicAnalysis
    from ._5965 import RingPinsCompoundHarmonicAnalysis
    from ._5966 import RingPinsToDiscConnectionCompoundHarmonicAnalysis
    from ._5967 import RollingRingAssemblyCompoundHarmonicAnalysis
    from ._5968 import RollingRingCompoundHarmonicAnalysis
    from ._5969 import RollingRingConnectionCompoundHarmonicAnalysis
    from ._5970 import RootAssemblyCompoundHarmonicAnalysis
    from ._5971 import ShaftCompoundHarmonicAnalysis
    from ._5972 import ShaftHubConnectionCompoundHarmonicAnalysis
    from ._5973 import ShaftToMountableComponentConnectionCompoundHarmonicAnalysis
    from ._5974 import SpecialisedAssemblyCompoundHarmonicAnalysis
    from ._5975 import SpiralBevelGearCompoundHarmonicAnalysis
    from ._5976 import SpiralBevelGearMeshCompoundHarmonicAnalysis
    from ._5977 import SpiralBevelGearSetCompoundHarmonicAnalysis
    from ._5978 import SpringDamperCompoundHarmonicAnalysis
    from ._5979 import SpringDamperConnectionCompoundHarmonicAnalysis
    from ._5980 import SpringDamperHalfCompoundHarmonicAnalysis
    from ._5981 import StraightBevelDiffGearCompoundHarmonicAnalysis
    from ._5982 import StraightBevelDiffGearMeshCompoundHarmonicAnalysis
    from ._5983 import StraightBevelDiffGearSetCompoundHarmonicAnalysis
    from ._5984 import StraightBevelGearCompoundHarmonicAnalysis
    from ._5985 import StraightBevelGearMeshCompoundHarmonicAnalysis
    from ._5986 import StraightBevelGearSetCompoundHarmonicAnalysis
    from ._5987 import StraightBevelPlanetGearCompoundHarmonicAnalysis
    from ._5988 import StraightBevelSunGearCompoundHarmonicAnalysis
    from ._5989 import SynchroniserCompoundHarmonicAnalysis
    from ._5990 import SynchroniserHalfCompoundHarmonicAnalysis
    from ._5991 import SynchroniserPartCompoundHarmonicAnalysis
    from ._5992 import SynchroniserSleeveCompoundHarmonicAnalysis
    from ._5993 import TorqueConverterCompoundHarmonicAnalysis
    from ._5994 import TorqueConverterConnectionCompoundHarmonicAnalysis
    from ._5995 import TorqueConverterPumpCompoundHarmonicAnalysis
    from ._5996 import TorqueConverterTurbineCompoundHarmonicAnalysis
    from ._5997 import UnbalancedMassCompoundHarmonicAnalysis
    from ._5998 import VirtualComponentCompoundHarmonicAnalysis
    from ._5999 import WormGearCompoundHarmonicAnalysis
    from ._6000 import WormGearMeshCompoundHarmonicAnalysis
    from ._6001 import WormGearSetCompoundHarmonicAnalysis
    from ._6002 import ZerolBevelGearCompoundHarmonicAnalysis
    from ._6003 import ZerolBevelGearMeshCompoundHarmonicAnalysis
    from ._6004 import ZerolBevelGearSetCompoundHarmonicAnalysis
else:
    import_structure = {
        "_5876": ["AbstractAssemblyCompoundHarmonicAnalysis"],
        "_5877": ["AbstractShaftCompoundHarmonicAnalysis"],
        "_5878": ["AbstractShaftOrHousingCompoundHarmonicAnalysis"],
        "_5879": [
            "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis"
        ],
        "_5880": ["AGMAGleasonConicalGearCompoundHarmonicAnalysis"],
        "_5881": ["AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis"],
        "_5882": ["AGMAGleasonConicalGearSetCompoundHarmonicAnalysis"],
        "_5883": ["AssemblyCompoundHarmonicAnalysis"],
        "_5884": ["BearingCompoundHarmonicAnalysis"],
        "_5885": ["BeltConnectionCompoundHarmonicAnalysis"],
        "_5886": ["BeltDriveCompoundHarmonicAnalysis"],
        "_5887": ["BevelDifferentialGearCompoundHarmonicAnalysis"],
        "_5888": ["BevelDifferentialGearMeshCompoundHarmonicAnalysis"],
        "_5889": ["BevelDifferentialGearSetCompoundHarmonicAnalysis"],
        "_5890": ["BevelDifferentialPlanetGearCompoundHarmonicAnalysis"],
        "_5891": ["BevelDifferentialSunGearCompoundHarmonicAnalysis"],
        "_5892": ["BevelGearCompoundHarmonicAnalysis"],
        "_5893": ["BevelGearMeshCompoundHarmonicAnalysis"],
        "_5894": ["BevelGearSetCompoundHarmonicAnalysis"],
        "_5895": ["BoltCompoundHarmonicAnalysis"],
        "_5896": ["BoltedJointCompoundHarmonicAnalysis"],
        "_5897": ["ClutchCompoundHarmonicAnalysis"],
        "_5898": ["ClutchConnectionCompoundHarmonicAnalysis"],
        "_5899": ["ClutchHalfCompoundHarmonicAnalysis"],
        "_5900": ["CoaxialConnectionCompoundHarmonicAnalysis"],
        "_5901": ["ComponentCompoundHarmonicAnalysis"],
        "_5902": ["ConceptCouplingCompoundHarmonicAnalysis"],
        "_5903": ["ConceptCouplingConnectionCompoundHarmonicAnalysis"],
        "_5904": ["ConceptCouplingHalfCompoundHarmonicAnalysis"],
        "_5905": ["ConceptGearCompoundHarmonicAnalysis"],
        "_5906": ["ConceptGearMeshCompoundHarmonicAnalysis"],
        "_5907": ["ConceptGearSetCompoundHarmonicAnalysis"],
        "_5908": ["ConicalGearCompoundHarmonicAnalysis"],
        "_5909": ["ConicalGearMeshCompoundHarmonicAnalysis"],
        "_5910": ["ConicalGearSetCompoundHarmonicAnalysis"],
        "_5911": ["ConnectionCompoundHarmonicAnalysis"],
        "_5912": ["ConnectorCompoundHarmonicAnalysis"],
        "_5913": ["CouplingCompoundHarmonicAnalysis"],
        "_5914": ["CouplingConnectionCompoundHarmonicAnalysis"],
        "_5915": ["CouplingHalfCompoundHarmonicAnalysis"],
        "_5916": ["CVTBeltConnectionCompoundHarmonicAnalysis"],
        "_5917": ["CVTCompoundHarmonicAnalysis"],
        "_5918": ["CVTPulleyCompoundHarmonicAnalysis"],
        "_5919": ["CycloidalAssemblyCompoundHarmonicAnalysis"],
        "_5920": ["CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis"],
        "_5921": ["CycloidalDiscCompoundHarmonicAnalysis"],
        "_5922": ["CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysis"],
        "_5923": ["CylindricalGearCompoundHarmonicAnalysis"],
        "_5924": ["CylindricalGearMeshCompoundHarmonicAnalysis"],
        "_5925": ["CylindricalGearSetCompoundHarmonicAnalysis"],
        "_5926": ["CylindricalPlanetGearCompoundHarmonicAnalysis"],
        "_5927": ["DatumCompoundHarmonicAnalysis"],
        "_5928": ["ExternalCADModelCompoundHarmonicAnalysis"],
        "_5929": ["FaceGearCompoundHarmonicAnalysis"],
        "_5930": ["FaceGearMeshCompoundHarmonicAnalysis"],
        "_5931": ["FaceGearSetCompoundHarmonicAnalysis"],
        "_5932": ["FEPartCompoundHarmonicAnalysis"],
        "_5933": ["FlexiblePinAssemblyCompoundHarmonicAnalysis"],
        "_5934": ["GearCompoundHarmonicAnalysis"],
        "_5935": ["GearMeshCompoundHarmonicAnalysis"],
        "_5936": ["GearSetCompoundHarmonicAnalysis"],
        "_5937": ["GuideDxfModelCompoundHarmonicAnalysis"],
        "_5938": ["HypoidGearCompoundHarmonicAnalysis"],
        "_5939": ["HypoidGearMeshCompoundHarmonicAnalysis"],
        "_5940": ["HypoidGearSetCompoundHarmonicAnalysis"],
        "_5941": ["InterMountableComponentConnectionCompoundHarmonicAnalysis"],
        "_5942": ["KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis"],
        "_5943": ["KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis"],
        "_5944": ["KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis"],
        "_5945": ["KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis"],
        "_5946": ["KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis"],
        "_5947": ["KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis"],
        "_5948": ["KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis"],
        "_5949": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis"
        ],
        "_5950": ["KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis"],
        "_5951": ["MassDiscCompoundHarmonicAnalysis"],
        "_5952": ["MeasurementComponentCompoundHarmonicAnalysis"],
        "_5953": ["MountableComponentCompoundHarmonicAnalysis"],
        "_5954": ["OilSealCompoundHarmonicAnalysis"],
        "_5955": ["PartCompoundHarmonicAnalysis"],
        "_5956": ["PartToPartShearCouplingCompoundHarmonicAnalysis"],
        "_5957": ["PartToPartShearCouplingConnectionCompoundHarmonicAnalysis"],
        "_5958": ["PartToPartShearCouplingHalfCompoundHarmonicAnalysis"],
        "_5959": ["PlanetaryConnectionCompoundHarmonicAnalysis"],
        "_5960": ["PlanetaryGearSetCompoundHarmonicAnalysis"],
        "_5961": ["PlanetCarrierCompoundHarmonicAnalysis"],
        "_5962": ["PointLoadCompoundHarmonicAnalysis"],
        "_5963": ["PowerLoadCompoundHarmonicAnalysis"],
        "_5964": ["PulleyCompoundHarmonicAnalysis"],
        "_5965": ["RingPinsCompoundHarmonicAnalysis"],
        "_5966": ["RingPinsToDiscConnectionCompoundHarmonicAnalysis"],
        "_5967": ["RollingRingAssemblyCompoundHarmonicAnalysis"],
        "_5968": ["RollingRingCompoundHarmonicAnalysis"],
        "_5969": ["RollingRingConnectionCompoundHarmonicAnalysis"],
        "_5970": ["RootAssemblyCompoundHarmonicAnalysis"],
        "_5971": ["ShaftCompoundHarmonicAnalysis"],
        "_5972": ["ShaftHubConnectionCompoundHarmonicAnalysis"],
        "_5973": ["ShaftToMountableComponentConnectionCompoundHarmonicAnalysis"],
        "_5974": ["SpecialisedAssemblyCompoundHarmonicAnalysis"],
        "_5975": ["SpiralBevelGearCompoundHarmonicAnalysis"],
        "_5976": ["SpiralBevelGearMeshCompoundHarmonicAnalysis"],
        "_5977": ["SpiralBevelGearSetCompoundHarmonicAnalysis"],
        "_5978": ["SpringDamperCompoundHarmonicAnalysis"],
        "_5979": ["SpringDamperConnectionCompoundHarmonicAnalysis"],
        "_5980": ["SpringDamperHalfCompoundHarmonicAnalysis"],
        "_5981": ["StraightBevelDiffGearCompoundHarmonicAnalysis"],
        "_5982": ["StraightBevelDiffGearMeshCompoundHarmonicAnalysis"],
        "_5983": ["StraightBevelDiffGearSetCompoundHarmonicAnalysis"],
        "_5984": ["StraightBevelGearCompoundHarmonicAnalysis"],
        "_5985": ["StraightBevelGearMeshCompoundHarmonicAnalysis"],
        "_5986": ["StraightBevelGearSetCompoundHarmonicAnalysis"],
        "_5987": ["StraightBevelPlanetGearCompoundHarmonicAnalysis"],
        "_5988": ["StraightBevelSunGearCompoundHarmonicAnalysis"],
        "_5989": ["SynchroniserCompoundHarmonicAnalysis"],
        "_5990": ["SynchroniserHalfCompoundHarmonicAnalysis"],
        "_5991": ["SynchroniserPartCompoundHarmonicAnalysis"],
        "_5992": ["SynchroniserSleeveCompoundHarmonicAnalysis"],
        "_5993": ["TorqueConverterCompoundHarmonicAnalysis"],
        "_5994": ["TorqueConverterConnectionCompoundHarmonicAnalysis"],
        "_5995": ["TorqueConverterPumpCompoundHarmonicAnalysis"],
        "_5996": ["TorqueConverterTurbineCompoundHarmonicAnalysis"],
        "_5997": ["UnbalancedMassCompoundHarmonicAnalysis"],
        "_5998": ["VirtualComponentCompoundHarmonicAnalysis"],
        "_5999": ["WormGearCompoundHarmonicAnalysis"],
        "_6000": ["WormGearMeshCompoundHarmonicAnalysis"],
        "_6001": ["WormGearSetCompoundHarmonicAnalysis"],
        "_6002": ["ZerolBevelGearCompoundHarmonicAnalysis"],
        "_6003": ["ZerolBevelGearMeshCompoundHarmonicAnalysis"],
        "_6004": ["ZerolBevelGearSetCompoundHarmonicAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundHarmonicAnalysis",
    "AbstractShaftCompoundHarmonicAnalysis",
    "AbstractShaftOrHousingCompoundHarmonicAnalysis",
    "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
    "AGMAGleasonConicalGearCompoundHarmonicAnalysis",
    "AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis",
    "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
    "AssemblyCompoundHarmonicAnalysis",
    "BearingCompoundHarmonicAnalysis",
    "BeltConnectionCompoundHarmonicAnalysis",
    "BeltDriveCompoundHarmonicAnalysis",
    "BevelDifferentialGearCompoundHarmonicAnalysis",
    "BevelDifferentialGearMeshCompoundHarmonicAnalysis",
    "BevelDifferentialGearSetCompoundHarmonicAnalysis",
    "BevelDifferentialPlanetGearCompoundHarmonicAnalysis",
    "BevelDifferentialSunGearCompoundHarmonicAnalysis",
    "BevelGearCompoundHarmonicAnalysis",
    "BevelGearMeshCompoundHarmonicAnalysis",
    "BevelGearSetCompoundHarmonicAnalysis",
    "BoltCompoundHarmonicAnalysis",
    "BoltedJointCompoundHarmonicAnalysis",
    "ClutchCompoundHarmonicAnalysis",
    "ClutchConnectionCompoundHarmonicAnalysis",
    "ClutchHalfCompoundHarmonicAnalysis",
    "CoaxialConnectionCompoundHarmonicAnalysis",
    "ComponentCompoundHarmonicAnalysis",
    "ConceptCouplingCompoundHarmonicAnalysis",
    "ConceptCouplingConnectionCompoundHarmonicAnalysis",
    "ConceptCouplingHalfCompoundHarmonicAnalysis",
    "ConceptGearCompoundHarmonicAnalysis",
    "ConceptGearMeshCompoundHarmonicAnalysis",
    "ConceptGearSetCompoundHarmonicAnalysis",
    "ConicalGearCompoundHarmonicAnalysis",
    "ConicalGearMeshCompoundHarmonicAnalysis",
    "ConicalGearSetCompoundHarmonicAnalysis",
    "ConnectionCompoundHarmonicAnalysis",
    "ConnectorCompoundHarmonicAnalysis",
    "CouplingCompoundHarmonicAnalysis",
    "CouplingConnectionCompoundHarmonicAnalysis",
    "CouplingHalfCompoundHarmonicAnalysis",
    "CVTBeltConnectionCompoundHarmonicAnalysis",
    "CVTCompoundHarmonicAnalysis",
    "CVTPulleyCompoundHarmonicAnalysis",
    "CycloidalAssemblyCompoundHarmonicAnalysis",
    "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
    "CycloidalDiscCompoundHarmonicAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysis",
    "CylindricalGearCompoundHarmonicAnalysis",
    "CylindricalGearMeshCompoundHarmonicAnalysis",
    "CylindricalGearSetCompoundHarmonicAnalysis",
    "CylindricalPlanetGearCompoundHarmonicAnalysis",
    "DatumCompoundHarmonicAnalysis",
    "ExternalCADModelCompoundHarmonicAnalysis",
    "FaceGearCompoundHarmonicAnalysis",
    "FaceGearMeshCompoundHarmonicAnalysis",
    "FaceGearSetCompoundHarmonicAnalysis",
    "FEPartCompoundHarmonicAnalysis",
    "FlexiblePinAssemblyCompoundHarmonicAnalysis",
    "GearCompoundHarmonicAnalysis",
    "GearMeshCompoundHarmonicAnalysis",
    "GearSetCompoundHarmonicAnalysis",
    "GuideDxfModelCompoundHarmonicAnalysis",
    "HypoidGearCompoundHarmonicAnalysis",
    "HypoidGearMeshCompoundHarmonicAnalysis",
    "HypoidGearSetCompoundHarmonicAnalysis",
    "InterMountableComponentConnectionCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis",
    "MassDiscCompoundHarmonicAnalysis",
    "MeasurementComponentCompoundHarmonicAnalysis",
    "MountableComponentCompoundHarmonicAnalysis",
    "OilSealCompoundHarmonicAnalysis",
    "PartCompoundHarmonicAnalysis",
    "PartToPartShearCouplingCompoundHarmonicAnalysis",
    "PartToPartShearCouplingConnectionCompoundHarmonicAnalysis",
    "PartToPartShearCouplingHalfCompoundHarmonicAnalysis",
    "PlanetaryConnectionCompoundHarmonicAnalysis",
    "PlanetaryGearSetCompoundHarmonicAnalysis",
    "PlanetCarrierCompoundHarmonicAnalysis",
    "PointLoadCompoundHarmonicAnalysis",
    "PowerLoadCompoundHarmonicAnalysis",
    "PulleyCompoundHarmonicAnalysis",
    "RingPinsCompoundHarmonicAnalysis",
    "RingPinsToDiscConnectionCompoundHarmonicAnalysis",
    "RollingRingAssemblyCompoundHarmonicAnalysis",
    "RollingRingCompoundHarmonicAnalysis",
    "RollingRingConnectionCompoundHarmonicAnalysis",
    "RootAssemblyCompoundHarmonicAnalysis",
    "ShaftCompoundHarmonicAnalysis",
    "ShaftHubConnectionCompoundHarmonicAnalysis",
    "ShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
    "SpecialisedAssemblyCompoundHarmonicAnalysis",
    "SpiralBevelGearCompoundHarmonicAnalysis",
    "SpiralBevelGearMeshCompoundHarmonicAnalysis",
    "SpiralBevelGearSetCompoundHarmonicAnalysis",
    "SpringDamperCompoundHarmonicAnalysis",
    "SpringDamperConnectionCompoundHarmonicAnalysis",
    "SpringDamperHalfCompoundHarmonicAnalysis",
    "StraightBevelDiffGearCompoundHarmonicAnalysis",
    "StraightBevelDiffGearMeshCompoundHarmonicAnalysis",
    "StraightBevelDiffGearSetCompoundHarmonicAnalysis",
    "StraightBevelGearCompoundHarmonicAnalysis",
    "StraightBevelGearMeshCompoundHarmonicAnalysis",
    "StraightBevelGearSetCompoundHarmonicAnalysis",
    "StraightBevelPlanetGearCompoundHarmonicAnalysis",
    "StraightBevelSunGearCompoundHarmonicAnalysis",
    "SynchroniserCompoundHarmonicAnalysis",
    "SynchroniserHalfCompoundHarmonicAnalysis",
    "SynchroniserPartCompoundHarmonicAnalysis",
    "SynchroniserSleeveCompoundHarmonicAnalysis",
    "TorqueConverterCompoundHarmonicAnalysis",
    "TorqueConverterConnectionCompoundHarmonicAnalysis",
    "TorqueConverterPumpCompoundHarmonicAnalysis",
    "TorqueConverterTurbineCompoundHarmonicAnalysis",
    "UnbalancedMassCompoundHarmonicAnalysis",
    "VirtualComponentCompoundHarmonicAnalysis",
    "WormGearCompoundHarmonicAnalysis",
    "WormGearMeshCompoundHarmonicAnalysis",
    "WormGearSetCompoundHarmonicAnalysis",
    "ZerolBevelGearCompoundHarmonicAnalysis",
    "ZerolBevelGearMeshCompoundHarmonicAnalysis",
    "ZerolBevelGearSetCompoundHarmonicAnalysis",
)
