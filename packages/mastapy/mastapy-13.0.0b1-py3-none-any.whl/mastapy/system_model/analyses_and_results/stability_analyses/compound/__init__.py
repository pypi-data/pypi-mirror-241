"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._3895 import AbstractAssemblyCompoundStabilityAnalysis
    from ._3896 import AbstractShaftCompoundStabilityAnalysis
    from ._3897 import AbstractShaftOrHousingCompoundStabilityAnalysis
    from ._3898 import (
        AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis,
    )
    from ._3899 import AGMAGleasonConicalGearCompoundStabilityAnalysis
    from ._3900 import AGMAGleasonConicalGearMeshCompoundStabilityAnalysis
    from ._3901 import AGMAGleasonConicalGearSetCompoundStabilityAnalysis
    from ._3902 import AssemblyCompoundStabilityAnalysis
    from ._3903 import BearingCompoundStabilityAnalysis
    from ._3904 import BeltConnectionCompoundStabilityAnalysis
    from ._3905 import BeltDriveCompoundStabilityAnalysis
    from ._3906 import BevelDifferentialGearCompoundStabilityAnalysis
    from ._3907 import BevelDifferentialGearMeshCompoundStabilityAnalysis
    from ._3908 import BevelDifferentialGearSetCompoundStabilityAnalysis
    from ._3909 import BevelDifferentialPlanetGearCompoundStabilityAnalysis
    from ._3910 import BevelDifferentialSunGearCompoundStabilityAnalysis
    from ._3911 import BevelGearCompoundStabilityAnalysis
    from ._3912 import BevelGearMeshCompoundStabilityAnalysis
    from ._3913 import BevelGearSetCompoundStabilityAnalysis
    from ._3914 import BoltCompoundStabilityAnalysis
    from ._3915 import BoltedJointCompoundStabilityAnalysis
    from ._3916 import ClutchCompoundStabilityAnalysis
    from ._3917 import ClutchConnectionCompoundStabilityAnalysis
    from ._3918 import ClutchHalfCompoundStabilityAnalysis
    from ._3919 import CoaxialConnectionCompoundStabilityAnalysis
    from ._3920 import ComponentCompoundStabilityAnalysis
    from ._3921 import ConceptCouplingCompoundStabilityAnalysis
    from ._3922 import ConceptCouplingConnectionCompoundStabilityAnalysis
    from ._3923 import ConceptCouplingHalfCompoundStabilityAnalysis
    from ._3924 import ConceptGearCompoundStabilityAnalysis
    from ._3925 import ConceptGearMeshCompoundStabilityAnalysis
    from ._3926 import ConceptGearSetCompoundStabilityAnalysis
    from ._3927 import ConicalGearCompoundStabilityAnalysis
    from ._3928 import ConicalGearMeshCompoundStabilityAnalysis
    from ._3929 import ConicalGearSetCompoundStabilityAnalysis
    from ._3930 import ConnectionCompoundStabilityAnalysis
    from ._3931 import ConnectorCompoundStabilityAnalysis
    from ._3932 import CouplingCompoundStabilityAnalysis
    from ._3933 import CouplingConnectionCompoundStabilityAnalysis
    from ._3934 import CouplingHalfCompoundStabilityAnalysis
    from ._3935 import CVTBeltConnectionCompoundStabilityAnalysis
    from ._3936 import CVTCompoundStabilityAnalysis
    from ._3937 import CVTPulleyCompoundStabilityAnalysis
    from ._3938 import CycloidalAssemblyCompoundStabilityAnalysis
    from ._3939 import CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis
    from ._3940 import CycloidalDiscCompoundStabilityAnalysis
    from ._3941 import CycloidalDiscPlanetaryBearingConnectionCompoundStabilityAnalysis
    from ._3942 import CylindricalGearCompoundStabilityAnalysis
    from ._3943 import CylindricalGearMeshCompoundStabilityAnalysis
    from ._3944 import CylindricalGearSetCompoundStabilityAnalysis
    from ._3945 import CylindricalPlanetGearCompoundStabilityAnalysis
    from ._3946 import DatumCompoundStabilityAnalysis
    from ._3947 import ExternalCADModelCompoundStabilityAnalysis
    from ._3948 import FaceGearCompoundStabilityAnalysis
    from ._3949 import FaceGearMeshCompoundStabilityAnalysis
    from ._3950 import FaceGearSetCompoundStabilityAnalysis
    from ._3951 import FEPartCompoundStabilityAnalysis
    from ._3952 import FlexiblePinAssemblyCompoundStabilityAnalysis
    from ._3953 import GearCompoundStabilityAnalysis
    from ._3954 import GearMeshCompoundStabilityAnalysis
    from ._3955 import GearSetCompoundStabilityAnalysis
    from ._3956 import GuideDxfModelCompoundStabilityAnalysis
    from ._3957 import HypoidGearCompoundStabilityAnalysis
    from ._3958 import HypoidGearMeshCompoundStabilityAnalysis
    from ._3959 import HypoidGearSetCompoundStabilityAnalysis
    from ._3960 import InterMountableComponentConnectionCompoundStabilityAnalysis
    from ._3961 import KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis
    from ._3962 import KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis
    from ._3963 import KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis
    from ._3964 import KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis
    from ._3965 import KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis
    from ._3966 import KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis
    from ._3967 import KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis
    from ._3968 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis,
    )
    from ._3969 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis,
    )
    from ._3970 import MassDiscCompoundStabilityAnalysis
    from ._3971 import MeasurementComponentCompoundStabilityAnalysis
    from ._3972 import MountableComponentCompoundStabilityAnalysis
    from ._3973 import OilSealCompoundStabilityAnalysis
    from ._3974 import PartCompoundStabilityAnalysis
    from ._3975 import PartToPartShearCouplingCompoundStabilityAnalysis
    from ._3976 import PartToPartShearCouplingConnectionCompoundStabilityAnalysis
    from ._3977 import PartToPartShearCouplingHalfCompoundStabilityAnalysis
    from ._3978 import PlanetaryConnectionCompoundStabilityAnalysis
    from ._3979 import PlanetaryGearSetCompoundStabilityAnalysis
    from ._3980 import PlanetCarrierCompoundStabilityAnalysis
    from ._3981 import PointLoadCompoundStabilityAnalysis
    from ._3982 import PowerLoadCompoundStabilityAnalysis
    from ._3983 import PulleyCompoundStabilityAnalysis
    from ._3984 import RingPinsCompoundStabilityAnalysis
    from ._3985 import RingPinsToDiscConnectionCompoundStabilityAnalysis
    from ._3986 import RollingRingAssemblyCompoundStabilityAnalysis
    from ._3987 import RollingRingCompoundStabilityAnalysis
    from ._3988 import RollingRingConnectionCompoundStabilityAnalysis
    from ._3989 import RootAssemblyCompoundStabilityAnalysis
    from ._3990 import ShaftCompoundStabilityAnalysis
    from ._3991 import ShaftHubConnectionCompoundStabilityAnalysis
    from ._3992 import ShaftToMountableComponentConnectionCompoundStabilityAnalysis
    from ._3993 import SpecialisedAssemblyCompoundStabilityAnalysis
    from ._3994 import SpiralBevelGearCompoundStabilityAnalysis
    from ._3995 import SpiralBevelGearMeshCompoundStabilityAnalysis
    from ._3996 import SpiralBevelGearSetCompoundStabilityAnalysis
    from ._3997 import SpringDamperCompoundStabilityAnalysis
    from ._3998 import SpringDamperConnectionCompoundStabilityAnalysis
    from ._3999 import SpringDamperHalfCompoundStabilityAnalysis
    from ._4000 import StraightBevelDiffGearCompoundStabilityAnalysis
    from ._4001 import StraightBevelDiffGearMeshCompoundStabilityAnalysis
    from ._4002 import StraightBevelDiffGearSetCompoundStabilityAnalysis
    from ._4003 import StraightBevelGearCompoundStabilityAnalysis
    from ._4004 import StraightBevelGearMeshCompoundStabilityAnalysis
    from ._4005 import StraightBevelGearSetCompoundStabilityAnalysis
    from ._4006 import StraightBevelPlanetGearCompoundStabilityAnalysis
    from ._4007 import StraightBevelSunGearCompoundStabilityAnalysis
    from ._4008 import SynchroniserCompoundStabilityAnalysis
    from ._4009 import SynchroniserHalfCompoundStabilityAnalysis
    from ._4010 import SynchroniserPartCompoundStabilityAnalysis
    from ._4011 import SynchroniserSleeveCompoundStabilityAnalysis
    from ._4012 import TorqueConverterCompoundStabilityAnalysis
    from ._4013 import TorqueConverterConnectionCompoundStabilityAnalysis
    from ._4014 import TorqueConverterPumpCompoundStabilityAnalysis
    from ._4015 import TorqueConverterTurbineCompoundStabilityAnalysis
    from ._4016 import UnbalancedMassCompoundStabilityAnalysis
    from ._4017 import VirtualComponentCompoundStabilityAnalysis
    from ._4018 import WormGearCompoundStabilityAnalysis
    from ._4019 import WormGearMeshCompoundStabilityAnalysis
    from ._4020 import WormGearSetCompoundStabilityAnalysis
    from ._4021 import ZerolBevelGearCompoundStabilityAnalysis
    from ._4022 import ZerolBevelGearMeshCompoundStabilityAnalysis
    from ._4023 import ZerolBevelGearSetCompoundStabilityAnalysis
else:
    import_structure = {
        "_3895": ["AbstractAssemblyCompoundStabilityAnalysis"],
        "_3896": ["AbstractShaftCompoundStabilityAnalysis"],
        "_3897": ["AbstractShaftOrHousingCompoundStabilityAnalysis"],
        "_3898": [
            "AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis"
        ],
        "_3899": ["AGMAGleasonConicalGearCompoundStabilityAnalysis"],
        "_3900": ["AGMAGleasonConicalGearMeshCompoundStabilityAnalysis"],
        "_3901": ["AGMAGleasonConicalGearSetCompoundStabilityAnalysis"],
        "_3902": ["AssemblyCompoundStabilityAnalysis"],
        "_3903": ["BearingCompoundStabilityAnalysis"],
        "_3904": ["BeltConnectionCompoundStabilityAnalysis"],
        "_3905": ["BeltDriveCompoundStabilityAnalysis"],
        "_3906": ["BevelDifferentialGearCompoundStabilityAnalysis"],
        "_3907": ["BevelDifferentialGearMeshCompoundStabilityAnalysis"],
        "_3908": ["BevelDifferentialGearSetCompoundStabilityAnalysis"],
        "_3909": ["BevelDifferentialPlanetGearCompoundStabilityAnalysis"],
        "_3910": ["BevelDifferentialSunGearCompoundStabilityAnalysis"],
        "_3911": ["BevelGearCompoundStabilityAnalysis"],
        "_3912": ["BevelGearMeshCompoundStabilityAnalysis"],
        "_3913": ["BevelGearSetCompoundStabilityAnalysis"],
        "_3914": ["BoltCompoundStabilityAnalysis"],
        "_3915": ["BoltedJointCompoundStabilityAnalysis"],
        "_3916": ["ClutchCompoundStabilityAnalysis"],
        "_3917": ["ClutchConnectionCompoundStabilityAnalysis"],
        "_3918": ["ClutchHalfCompoundStabilityAnalysis"],
        "_3919": ["CoaxialConnectionCompoundStabilityAnalysis"],
        "_3920": ["ComponentCompoundStabilityAnalysis"],
        "_3921": ["ConceptCouplingCompoundStabilityAnalysis"],
        "_3922": ["ConceptCouplingConnectionCompoundStabilityAnalysis"],
        "_3923": ["ConceptCouplingHalfCompoundStabilityAnalysis"],
        "_3924": ["ConceptGearCompoundStabilityAnalysis"],
        "_3925": ["ConceptGearMeshCompoundStabilityAnalysis"],
        "_3926": ["ConceptGearSetCompoundStabilityAnalysis"],
        "_3927": ["ConicalGearCompoundStabilityAnalysis"],
        "_3928": ["ConicalGearMeshCompoundStabilityAnalysis"],
        "_3929": ["ConicalGearSetCompoundStabilityAnalysis"],
        "_3930": ["ConnectionCompoundStabilityAnalysis"],
        "_3931": ["ConnectorCompoundStabilityAnalysis"],
        "_3932": ["CouplingCompoundStabilityAnalysis"],
        "_3933": ["CouplingConnectionCompoundStabilityAnalysis"],
        "_3934": ["CouplingHalfCompoundStabilityAnalysis"],
        "_3935": ["CVTBeltConnectionCompoundStabilityAnalysis"],
        "_3936": ["CVTCompoundStabilityAnalysis"],
        "_3937": ["CVTPulleyCompoundStabilityAnalysis"],
        "_3938": ["CycloidalAssemblyCompoundStabilityAnalysis"],
        "_3939": ["CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis"],
        "_3940": ["CycloidalDiscCompoundStabilityAnalysis"],
        "_3941": ["CycloidalDiscPlanetaryBearingConnectionCompoundStabilityAnalysis"],
        "_3942": ["CylindricalGearCompoundStabilityAnalysis"],
        "_3943": ["CylindricalGearMeshCompoundStabilityAnalysis"],
        "_3944": ["CylindricalGearSetCompoundStabilityAnalysis"],
        "_3945": ["CylindricalPlanetGearCompoundStabilityAnalysis"],
        "_3946": ["DatumCompoundStabilityAnalysis"],
        "_3947": ["ExternalCADModelCompoundStabilityAnalysis"],
        "_3948": ["FaceGearCompoundStabilityAnalysis"],
        "_3949": ["FaceGearMeshCompoundStabilityAnalysis"],
        "_3950": ["FaceGearSetCompoundStabilityAnalysis"],
        "_3951": ["FEPartCompoundStabilityAnalysis"],
        "_3952": ["FlexiblePinAssemblyCompoundStabilityAnalysis"],
        "_3953": ["GearCompoundStabilityAnalysis"],
        "_3954": ["GearMeshCompoundStabilityAnalysis"],
        "_3955": ["GearSetCompoundStabilityAnalysis"],
        "_3956": ["GuideDxfModelCompoundStabilityAnalysis"],
        "_3957": ["HypoidGearCompoundStabilityAnalysis"],
        "_3958": ["HypoidGearMeshCompoundStabilityAnalysis"],
        "_3959": ["HypoidGearSetCompoundStabilityAnalysis"],
        "_3960": ["InterMountableComponentConnectionCompoundStabilityAnalysis"],
        "_3961": ["KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis"],
        "_3962": ["KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis"],
        "_3963": ["KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis"],
        "_3964": ["KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis"],
        "_3965": ["KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis"],
        "_3966": ["KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis"],
        "_3967": ["KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis"],
        "_3968": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis"
        ],
        "_3969": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis"
        ],
        "_3970": ["MassDiscCompoundStabilityAnalysis"],
        "_3971": ["MeasurementComponentCompoundStabilityAnalysis"],
        "_3972": ["MountableComponentCompoundStabilityAnalysis"],
        "_3973": ["OilSealCompoundStabilityAnalysis"],
        "_3974": ["PartCompoundStabilityAnalysis"],
        "_3975": ["PartToPartShearCouplingCompoundStabilityAnalysis"],
        "_3976": ["PartToPartShearCouplingConnectionCompoundStabilityAnalysis"],
        "_3977": ["PartToPartShearCouplingHalfCompoundStabilityAnalysis"],
        "_3978": ["PlanetaryConnectionCompoundStabilityAnalysis"],
        "_3979": ["PlanetaryGearSetCompoundStabilityAnalysis"],
        "_3980": ["PlanetCarrierCompoundStabilityAnalysis"],
        "_3981": ["PointLoadCompoundStabilityAnalysis"],
        "_3982": ["PowerLoadCompoundStabilityAnalysis"],
        "_3983": ["PulleyCompoundStabilityAnalysis"],
        "_3984": ["RingPinsCompoundStabilityAnalysis"],
        "_3985": ["RingPinsToDiscConnectionCompoundStabilityAnalysis"],
        "_3986": ["RollingRingAssemblyCompoundStabilityAnalysis"],
        "_3987": ["RollingRingCompoundStabilityAnalysis"],
        "_3988": ["RollingRingConnectionCompoundStabilityAnalysis"],
        "_3989": ["RootAssemblyCompoundStabilityAnalysis"],
        "_3990": ["ShaftCompoundStabilityAnalysis"],
        "_3991": ["ShaftHubConnectionCompoundStabilityAnalysis"],
        "_3992": ["ShaftToMountableComponentConnectionCompoundStabilityAnalysis"],
        "_3993": ["SpecialisedAssemblyCompoundStabilityAnalysis"],
        "_3994": ["SpiralBevelGearCompoundStabilityAnalysis"],
        "_3995": ["SpiralBevelGearMeshCompoundStabilityAnalysis"],
        "_3996": ["SpiralBevelGearSetCompoundStabilityAnalysis"],
        "_3997": ["SpringDamperCompoundStabilityAnalysis"],
        "_3998": ["SpringDamperConnectionCompoundStabilityAnalysis"],
        "_3999": ["SpringDamperHalfCompoundStabilityAnalysis"],
        "_4000": ["StraightBevelDiffGearCompoundStabilityAnalysis"],
        "_4001": ["StraightBevelDiffGearMeshCompoundStabilityAnalysis"],
        "_4002": ["StraightBevelDiffGearSetCompoundStabilityAnalysis"],
        "_4003": ["StraightBevelGearCompoundStabilityAnalysis"],
        "_4004": ["StraightBevelGearMeshCompoundStabilityAnalysis"],
        "_4005": ["StraightBevelGearSetCompoundStabilityAnalysis"],
        "_4006": ["StraightBevelPlanetGearCompoundStabilityAnalysis"],
        "_4007": ["StraightBevelSunGearCompoundStabilityAnalysis"],
        "_4008": ["SynchroniserCompoundStabilityAnalysis"],
        "_4009": ["SynchroniserHalfCompoundStabilityAnalysis"],
        "_4010": ["SynchroniserPartCompoundStabilityAnalysis"],
        "_4011": ["SynchroniserSleeveCompoundStabilityAnalysis"],
        "_4012": ["TorqueConverterCompoundStabilityAnalysis"],
        "_4013": ["TorqueConverterConnectionCompoundStabilityAnalysis"],
        "_4014": ["TorqueConverterPumpCompoundStabilityAnalysis"],
        "_4015": ["TorqueConverterTurbineCompoundStabilityAnalysis"],
        "_4016": ["UnbalancedMassCompoundStabilityAnalysis"],
        "_4017": ["VirtualComponentCompoundStabilityAnalysis"],
        "_4018": ["WormGearCompoundStabilityAnalysis"],
        "_4019": ["WormGearMeshCompoundStabilityAnalysis"],
        "_4020": ["WormGearSetCompoundStabilityAnalysis"],
        "_4021": ["ZerolBevelGearCompoundStabilityAnalysis"],
        "_4022": ["ZerolBevelGearMeshCompoundStabilityAnalysis"],
        "_4023": ["ZerolBevelGearSetCompoundStabilityAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundStabilityAnalysis",
    "AbstractShaftCompoundStabilityAnalysis",
    "AbstractShaftOrHousingCompoundStabilityAnalysis",
    "AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis",
    "AGMAGleasonConicalGearCompoundStabilityAnalysis",
    "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
    "AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
    "AssemblyCompoundStabilityAnalysis",
    "BearingCompoundStabilityAnalysis",
    "BeltConnectionCompoundStabilityAnalysis",
    "BeltDriveCompoundStabilityAnalysis",
    "BevelDifferentialGearCompoundStabilityAnalysis",
    "BevelDifferentialGearMeshCompoundStabilityAnalysis",
    "BevelDifferentialGearSetCompoundStabilityAnalysis",
    "BevelDifferentialPlanetGearCompoundStabilityAnalysis",
    "BevelDifferentialSunGearCompoundStabilityAnalysis",
    "BevelGearCompoundStabilityAnalysis",
    "BevelGearMeshCompoundStabilityAnalysis",
    "BevelGearSetCompoundStabilityAnalysis",
    "BoltCompoundStabilityAnalysis",
    "BoltedJointCompoundStabilityAnalysis",
    "ClutchCompoundStabilityAnalysis",
    "ClutchConnectionCompoundStabilityAnalysis",
    "ClutchHalfCompoundStabilityAnalysis",
    "CoaxialConnectionCompoundStabilityAnalysis",
    "ComponentCompoundStabilityAnalysis",
    "ConceptCouplingCompoundStabilityAnalysis",
    "ConceptCouplingConnectionCompoundStabilityAnalysis",
    "ConceptCouplingHalfCompoundStabilityAnalysis",
    "ConceptGearCompoundStabilityAnalysis",
    "ConceptGearMeshCompoundStabilityAnalysis",
    "ConceptGearSetCompoundStabilityAnalysis",
    "ConicalGearCompoundStabilityAnalysis",
    "ConicalGearMeshCompoundStabilityAnalysis",
    "ConicalGearSetCompoundStabilityAnalysis",
    "ConnectionCompoundStabilityAnalysis",
    "ConnectorCompoundStabilityAnalysis",
    "CouplingCompoundStabilityAnalysis",
    "CouplingConnectionCompoundStabilityAnalysis",
    "CouplingHalfCompoundStabilityAnalysis",
    "CVTBeltConnectionCompoundStabilityAnalysis",
    "CVTCompoundStabilityAnalysis",
    "CVTPulleyCompoundStabilityAnalysis",
    "CycloidalAssemblyCompoundStabilityAnalysis",
    "CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis",
    "CycloidalDiscCompoundStabilityAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionCompoundStabilityAnalysis",
    "CylindricalGearCompoundStabilityAnalysis",
    "CylindricalGearMeshCompoundStabilityAnalysis",
    "CylindricalGearSetCompoundStabilityAnalysis",
    "CylindricalPlanetGearCompoundStabilityAnalysis",
    "DatumCompoundStabilityAnalysis",
    "ExternalCADModelCompoundStabilityAnalysis",
    "FaceGearCompoundStabilityAnalysis",
    "FaceGearMeshCompoundStabilityAnalysis",
    "FaceGearSetCompoundStabilityAnalysis",
    "FEPartCompoundStabilityAnalysis",
    "FlexiblePinAssemblyCompoundStabilityAnalysis",
    "GearCompoundStabilityAnalysis",
    "GearMeshCompoundStabilityAnalysis",
    "GearSetCompoundStabilityAnalysis",
    "GuideDxfModelCompoundStabilityAnalysis",
    "HypoidGearCompoundStabilityAnalysis",
    "HypoidGearMeshCompoundStabilityAnalysis",
    "HypoidGearSetCompoundStabilityAnalysis",
    "InterMountableComponentConnectionCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis",
    "MassDiscCompoundStabilityAnalysis",
    "MeasurementComponentCompoundStabilityAnalysis",
    "MountableComponentCompoundStabilityAnalysis",
    "OilSealCompoundStabilityAnalysis",
    "PartCompoundStabilityAnalysis",
    "PartToPartShearCouplingCompoundStabilityAnalysis",
    "PartToPartShearCouplingConnectionCompoundStabilityAnalysis",
    "PartToPartShearCouplingHalfCompoundStabilityAnalysis",
    "PlanetaryConnectionCompoundStabilityAnalysis",
    "PlanetaryGearSetCompoundStabilityAnalysis",
    "PlanetCarrierCompoundStabilityAnalysis",
    "PointLoadCompoundStabilityAnalysis",
    "PowerLoadCompoundStabilityAnalysis",
    "PulleyCompoundStabilityAnalysis",
    "RingPinsCompoundStabilityAnalysis",
    "RingPinsToDiscConnectionCompoundStabilityAnalysis",
    "RollingRingAssemblyCompoundStabilityAnalysis",
    "RollingRingCompoundStabilityAnalysis",
    "RollingRingConnectionCompoundStabilityAnalysis",
    "RootAssemblyCompoundStabilityAnalysis",
    "ShaftCompoundStabilityAnalysis",
    "ShaftHubConnectionCompoundStabilityAnalysis",
    "ShaftToMountableComponentConnectionCompoundStabilityAnalysis",
    "SpecialisedAssemblyCompoundStabilityAnalysis",
    "SpiralBevelGearCompoundStabilityAnalysis",
    "SpiralBevelGearMeshCompoundStabilityAnalysis",
    "SpiralBevelGearSetCompoundStabilityAnalysis",
    "SpringDamperCompoundStabilityAnalysis",
    "SpringDamperConnectionCompoundStabilityAnalysis",
    "SpringDamperHalfCompoundStabilityAnalysis",
    "StraightBevelDiffGearCompoundStabilityAnalysis",
    "StraightBevelDiffGearMeshCompoundStabilityAnalysis",
    "StraightBevelDiffGearSetCompoundStabilityAnalysis",
    "StraightBevelGearCompoundStabilityAnalysis",
    "StraightBevelGearMeshCompoundStabilityAnalysis",
    "StraightBevelGearSetCompoundStabilityAnalysis",
    "StraightBevelPlanetGearCompoundStabilityAnalysis",
    "StraightBevelSunGearCompoundStabilityAnalysis",
    "SynchroniserCompoundStabilityAnalysis",
    "SynchroniserHalfCompoundStabilityAnalysis",
    "SynchroniserPartCompoundStabilityAnalysis",
    "SynchroniserSleeveCompoundStabilityAnalysis",
    "TorqueConverterCompoundStabilityAnalysis",
    "TorqueConverterConnectionCompoundStabilityAnalysis",
    "TorqueConverterPumpCompoundStabilityAnalysis",
    "TorqueConverterTurbineCompoundStabilityAnalysis",
    "UnbalancedMassCompoundStabilityAnalysis",
    "VirtualComponentCompoundStabilityAnalysis",
    "WormGearCompoundStabilityAnalysis",
    "WormGearMeshCompoundStabilityAnalysis",
    "WormGearSetCompoundStabilityAnalysis",
    "ZerolBevelGearCompoundStabilityAnalysis",
    "ZerolBevelGearMeshCompoundStabilityAnalysis",
    "ZerolBevelGearSetCompoundStabilityAnalysis",
)
