"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._3761 import AbstractAssemblyStabilityAnalysis
    from ._3762 import AbstractShaftOrHousingStabilityAnalysis
    from ._3763 import AbstractShaftStabilityAnalysis
    from ._3764 import AbstractShaftToMountableComponentConnectionStabilityAnalysis
    from ._3765 import AGMAGleasonConicalGearMeshStabilityAnalysis
    from ._3766 import AGMAGleasonConicalGearSetStabilityAnalysis
    from ._3767 import AGMAGleasonConicalGearStabilityAnalysis
    from ._3768 import AssemblyStabilityAnalysis
    from ._3769 import BearingStabilityAnalysis
    from ._3770 import BeltConnectionStabilityAnalysis
    from ._3771 import BeltDriveStabilityAnalysis
    from ._3772 import BevelDifferentialGearMeshStabilityAnalysis
    from ._3773 import BevelDifferentialGearSetStabilityAnalysis
    from ._3774 import BevelDifferentialGearStabilityAnalysis
    from ._3775 import BevelDifferentialPlanetGearStabilityAnalysis
    from ._3776 import BevelDifferentialSunGearStabilityAnalysis
    from ._3777 import BevelGearMeshStabilityAnalysis
    from ._3778 import BevelGearSetStabilityAnalysis
    from ._3779 import BevelGearStabilityAnalysis
    from ._3780 import BoltedJointStabilityAnalysis
    from ._3781 import BoltStabilityAnalysis
    from ._3782 import ClutchConnectionStabilityAnalysis
    from ._3783 import ClutchHalfStabilityAnalysis
    from ._3784 import ClutchStabilityAnalysis
    from ._3785 import CoaxialConnectionStabilityAnalysis
    from ._3786 import ComponentStabilityAnalysis
    from ._3787 import ConceptCouplingConnectionStabilityAnalysis
    from ._3788 import ConceptCouplingHalfStabilityAnalysis
    from ._3789 import ConceptCouplingStabilityAnalysis
    from ._3790 import ConceptGearMeshStabilityAnalysis
    from ._3791 import ConceptGearSetStabilityAnalysis
    from ._3792 import ConceptGearStabilityAnalysis
    from ._3793 import ConicalGearMeshStabilityAnalysis
    from ._3794 import ConicalGearSetStabilityAnalysis
    from ._3795 import ConicalGearStabilityAnalysis
    from ._3796 import ConnectionStabilityAnalysis
    from ._3797 import ConnectorStabilityAnalysis
    from ._3798 import CouplingConnectionStabilityAnalysis
    from ._3799 import CouplingHalfStabilityAnalysis
    from ._3800 import CouplingStabilityAnalysis
    from ._3801 import CriticalSpeed
    from ._3802 import CVTBeltConnectionStabilityAnalysis
    from ._3803 import CVTPulleyStabilityAnalysis
    from ._3804 import CVTStabilityAnalysis
    from ._3805 import CycloidalAssemblyStabilityAnalysis
    from ._3806 import CycloidalDiscCentralBearingConnectionStabilityAnalysis
    from ._3807 import CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis
    from ._3808 import CycloidalDiscStabilityAnalysis
    from ._3809 import CylindricalGearMeshStabilityAnalysis
    from ._3810 import CylindricalGearSetStabilityAnalysis
    from ._3811 import CylindricalGearStabilityAnalysis
    from ._3812 import CylindricalPlanetGearStabilityAnalysis
    from ._3813 import DatumStabilityAnalysis
    from ._3814 import DynamicModelForStabilityAnalysis
    from ._3815 import ExternalCADModelStabilityAnalysis
    from ._3816 import FaceGearMeshStabilityAnalysis
    from ._3817 import FaceGearSetStabilityAnalysis
    from ._3818 import FaceGearStabilityAnalysis
    from ._3819 import FEPartStabilityAnalysis
    from ._3820 import FlexiblePinAssemblyStabilityAnalysis
    from ._3821 import GearMeshStabilityAnalysis
    from ._3822 import GearSetStabilityAnalysis
    from ._3823 import GearStabilityAnalysis
    from ._3824 import GuideDxfModelStabilityAnalysis
    from ._3825 import HypoidGearMeshStabilityAnalysis
    from ._3826 import HypoidGearSetStabilityAnalysis
    from ._3827 import HypoidGearStabilityAnalysis
    from ._3828 import InterMountableComponentConnectionStabilityAnalysis
    from ._3829 import KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis
    from ._3830 import KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis
    from ._3831 import KlingelnbergCycloPalloidConicalGearStabilityAnalysis
    from ._3832 import KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis
    from ._3833 import KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis
    from ._3834 import KlingelnbergCycloPalloidHypoidGearStabilityAnalysis
    from ._3835 import KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis
    from ._3836 import KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis
    from ._3837 import KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis
    from ._3838 import MassDiscStabilityAnalysis
    from ._3839 import MeasurementComponentStabilityAnalysis
    from ._3840 import MountableComponentStabilityAnalysis
    from ._3841 import OilSealStabilityAnalysis
    from ._3842 import PartStabilityAnalysis
    from ._3843 import PartToPartShearCouplingConnectionStabilityAnalysis
    from ._3844 import PartToPartShearCouplingHalfStabilityAnalysis
    from ._3845 import PartToPartShearCouplingStabilityAnalysis
    from ._3846 import PlanetaryConnectionStabilityAnalysis
    from ._3847 import PlanetaryGearSetStabilityAnalysis
    from ._3848 import PlanetCarrierStabilityAnalysis
    from ._3849 import PointLoadStabilityAnalysis
    from ._3850 import PowerLoadStabilityAnalysis
    from ._3851 import PulleyStabilityAnalysis
    from ._3852 import RingPinsStabilityAnalysis
    from ._3853 import RingPinsToDiscConnectionStabilityAnalysis
    from ._3854 import RollingRingAssemblyStabilityAnalysis
    from ._3855 import RollingRingConnectionStabilityAnalysis
    from ._3856 import RollingRingStabilityAnalysis
    from ._3857 import RootAssemblyStabilityAnalysis
    from ._3858 import ShaftHubConnectionStabilityAnalysis
    from ._3859 import ShaftStabilityAnalysis
    from ._3860 import ShaftToMountableComponentConnectionStabilityAnalysis
    from ._3861 import SpecialisedAssemblyStabilityAnalysis
    from ._3862 import SpiralBevelGearMeshStabilityAnalysis
    from ._3863 import SpiralBevelGearSetStabilityAnalysis
    from ._3864 import SpiralBevelGearStabilityAnalysis
    from ._3865 import SpringDamperConnectionStabilityAnalysis
    from ._3866 import SpringDamperHalfStabilityAnalysis
    from ._3867 import SpringDamperStabilityAnalysis
    from ._3868 import StabilityAnalysis
    from ._3869 import StabilityAnalysisDrawStyle
    from ._3870 import StabilityAnalysisOptions
    from ._3871 import StraightBevelDiffGearMeshStabilityAnalysis
    from ._3872 import StraightBevelDiffGearSetStabilityAnalysis
    from ._3873 import StraightBevelDiffGearStabilityAnalysis
    from ._3874 import StraightBevelGearMeshStabilityAnalysis
    from ._3875 import StraightBevelGearSetStabilityAnalysis
    from ._3876 import StraightBevelGearStabilityAnalysis
    from ._3877 import StraightBevelPlanetGearStabilityAnalysis
    from ._3878 import StraightBevelSunGearStabilityAnalysis
    from ._3879 import SynchroniserHalfStabilityAnalysis
    from ._3880 import SynchroniserPartStabilityAnalysis
    from ._3881 import SynchroniserSleeveStabilityAnalysis
    from ._3882 import SynchroniserStabilityAnalysis
    from ._3883 import TorqueConverterConnectionStabilityAnalysis
    from ._3884 import TorqueConverterPumpStabilityAnalysis
    from ._3885 import TorqueConverterStabilityAnalysis
    from ._3886 import TorqueConverterTurbineStabilityAnalysis
    from ._3887 import UnbalancedMassStabilityAnalysis
    from ._3888 import VirtualComponentStabilityAnalysis
    from ._3889 import WormGearMeshStabilityAnalysis
    from ._3890 import WormGearSetStabilityAnalysis
    from ._3891 import WormGearStabilityAnalysis
    from ._3892 import ZerolBevelGearMeshStabilityAnalysis
    from ._3893 import ZerolBevelGearSetStabilityAnalysis
    from ._3894 import ZerolBevelGearStabilityAnalysis
else:
    import_structure = {
        "_3761": ["AbstractAssemblyStabilityAnalysis"],
        "_3762": ["AbstractShaftOrHousingStabilityAnalysis"],
        "_3763": ["AbstractShaftStabilityAnalysis"],
        "_3764": ["AbstractShaftToMountableComponentConnectionStabilityAnalysis"],
        "_3765": ["AGMAGleasonConicalGearMeshStabilityAnalysis"],
        "_3766": ["AGMAGleasonConicalGearSetStabilityAnalysis"],
        "_3767": ["AGMAGleasonConicalGearStabilityAnalysis"],
        "_3768": ["AssemblyStabilityAnalysis"],
        "_3769": ["BearingStabilityAnalysis"],
        "_3770": ["BeltConnectionStabilityAnalysis"],
        "_3771": ["BeltDriveStabilityAnalysis"],
        "_3772": ["BevelDifferentialGearMeshStabilityAnalysis"],
        "_3773": ["BevelDifferentialGearSetStabilityAnalysis"],
        "_3774": ["BevelDifferentialGearStabilityAnalysis"],
        "_3775": ["BevelDifferentialPlanetGearStabilityAnalysis"],
        "_3776": ["BevelDifferentialSunGearStabilityAnalysis"],
        "_3777": ["BevelGearMeshStabilityAnalysis"],
        "_3778": ["BevelGearSetStabilityAnalysis"],
        "_3779": ["BevelGearStabilityAnalysis"],
        "_3780": ["BoltedJointStabilityAnalysis"],
        "_3781": ["BoltStabilityAnalysis"],
        "_3782": ["ClutchConnectionStabilityAnalysis"],
        "_3783": ["ClutchHalfStabilityAnalysis"],
        "_3784": ["ClutchStabilityAnalysis"],
        "_3785": ["CoaxialConnectionStabilityAnalysis"],
        "_3786": ["ComponentStabilityAnalysis"],
        "_3787": ["ConceptCouplingConnectionStabilityAnalysis"],
        "_3788": ["ConceptCouplingHalfStabilityAnalysis"],
        "_3789": ["ConceptCouplingStabilityAnalysis"],
        "_3790": ["ConceptGearMeshStabilityAnalysis"],
        "_3791": ["ConceptGearSetStabilityAnalysis"],
        "_3792": ["ConceptGearStabilityAnalysis"],
        "_3793": ["ConicalGearMeshStabilityAnalysis"],
        "_3794": ["ConicalGearSetStabilityAnalysis"],
        "_3795": ["ConicalGearStabilityAnalysis"],
        "_3796": ["ConnectionStabilityAnalysis"],
        "_3797": ["ConnectorStabilityAnalysis"],
        "_3798": ["CouplingConnectionStabilityAnalysis"],
        "_3799": ["CouplingHalfStabilityAnalysis"],
        "_3800": ["CouplingStabilityAnalysis"],
        "_3801": ["CriticalSpeed"],
        "_3802": ["CVTBeltConnectionStabilityAnalysis"],
        "_3803": ["CVTPulleyStabilityAnalysis"],
        "_3804": ["CVTStabilityAnalysis"],
        "_3805": ["CycloidalAssemblyStabilityAnalysis"],
        "_3806": ["CycloidalDiscCentralBearingConnectionStabilityAnalysis"],
        "_3807": ["CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis"],
        "_3808": ["CycloidalDiscStabilityAnalysis"],
        "_3809": ["CylindricalGearMeshStabilityAnalysis"],
        "_3810": ["CylindricalGearSetStabilityAnalysis"],
        "_3811": ["CylindricalGearStabilityAnalysis"],
        "_3812": ["CylindricalPlanetGearStabilityAnalysis"],
        "_3813": ["DatumStabilityAnalysis"],
        "_3814": ["DynamicModelForStabilityAnalysis"],
        "_3815": ["ExternalCADModelStabilityAnalysis"],
        "_3816": ["FaceGearMeshStabilityAnalysis"],
        "_3817": ["FaceGearSetStabilityAnalysis"],
        "_3818": ["FaceGearStabilityAnalysis"],
        "_3819": ["FEPartStabilityAnalysis"],
        "_3820": ["FlexiblePinAssemblyStabilityAnalysis"],
        "_3821": ["GearMeshStabilityAnalysis"],
        "_3822": ["GearSetStabilityAnalysis"],
        "_3823": ["GearStabilityAnalysis"],
        "_3824": ["GuideDxfModelStabilityAnalysis"],
        "_3825": ["HypoidGearMeshStabilityAnalysis"],
        "_3826": ["HypoidGearSetStabilityAnalysis"],
        "_3827": ["HypoidGearStabilityAnalysis"],
        "_3828": ["InterMountableComponentConnectionStabilityAnalysis"],
        "_3829": ["KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis"],
        "_3830": ["KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis"],
        "_3831": ["KlingelnbergCycloPalloidConicalGearStabilityAnalysis"],
        "_3832": ["KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis"],
        "_3833": ["KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis"],
        "_3834": ["KlingelnbergCycloPalloidHypoidGearStabilityAnalysis"],
        "_3835": ["KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis"],
        "_3836": ["KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis"],
        "_3837": ["KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis"],
        "_3838": ["MassDiscStabilityAnalysis"],
        "_3839": ["MeasurementComponentStabilityAnalysis"],
        "_3840": ["MountableComponentStabilityAnalysis"],
        "_3841": ["OilSealStabilityAnalysis"],
        "_3842": ["PartStabilityAnalysis"],
        "_3843": ["PartToPartShearCouplingConnectionStabilityAnalysis"],
        "_3844": ["PartToPartShearCouplingHalfStabilityAnalysis"],
        "_3845": ["PartToPartShearCouplingStabilityAnalysis"],
        "_3846": ["PlanetaryConnectionStabilityAnalysis"],
        "_3847": ["PlanetaryGearSetStabilityAnalysis"],
        "_3848": ["PlanetCarrierStabilityAnalysis"],
        "_3849": ["PointLoadStabilityAnalysis"],
        "_3850": ["PowerLoadStabilityAnalysis"],
        "_3851": ["PulleyStabilityAnalysis"],
        "_3852": ["RingPinsStabilityAnalysis"],
        "_3853": ["RingPinsToDiscConnectionStabilityAnalysis"],
        "_3854": ["RollingRingAssemblyStabilityAnalysis"],
        "_3855": ["RollingRingConnectionStabilityAnalysis"],
        "_3856": ["RollingRingStabilityAnalysis"],
        "_3857": ["RootAssemblyStabilityAnalysis"],
        "_3858": ["ShaftHubConnectionStabilityAnalysis"],
        "_3859": ["ShaftStabilityAnalysis"],
        "_3860": ["ShaftToMountableComponentConnectionStabilityAnalysis"],
        "_3861": ["SpecialisedAssemblyStabilityAnalysis"],
        "_3862": ["SpiralBevelGearMeshStabilityAnalysis"],
        "_3863": ["SpiralBevelGearSetStabilityAnalysis"],
        "_3864": ["SpiralBevelGearStabilityAnalysis"],
        "_3865": ["SpringDamperConnectionStabilityAnalysis"],
        "_3866": ["SpringDamperHalfStabilityAnalysis"],
        "_3867": ["SpringDamperStabilityAnalysis"],
        "_3868": ["StabilityAnalysis"],
        "_3869": ["StabilityAnalysisDrawStyle"],
        "_3870": ["StabilityAnalysisOptions"],
        "_3871": ["StraightBevelDiffGearMeshStabilityAnalysis"],
        "_3872": ["StraightBevelDiffGearSetStabilityAnalysis"],
        "_3873": ["StraightBevelDiffGearStabilityAnalysis"],
        "_3874": ["StraightBevelGearMeshStabilityAnalysis"],
        "_3875": ["StraightBevelGearSetStabilityAnalysis"],
        "_3876": ["StraightBevelGearStabilityAnalysis"],
        "_3877": ["StraightBevelPlanetGearStabilityAnalysis"],
        "_3878": ["StraightBevelSunGearStabilityAnalysis"],
        "_3879": ["SynchroniserHalfStabilityAnalysis"],
        "_3880": ["SynchroniserPartStabilityAnalysis"],
        "_3881": ["SynchroniserSleeveStabilityAnalysis"],
        "_3882": ["SynchroniserStabilityAnalysis"],
        "_3883": ["TorqueConverterConnectionStabilityAnalysis"],
        "_3884": ["TorqueConverterPumpStabilityAnalysis"],
        "_3885": ["TorqueConverterStabilityAnalysis"],
        "_3886": ["TorqueConverterTurbineStabilityAnalysis"],
        "_3887": ["UnbalancedMassStabilityAnalysis"],
        "_3888": ["VirtualComponentStabilityAnalysis"],
        "_3889": ["WormGearMeshStabilityAnalysis"],
        "_3890": ["WormGearSetStabilityAnalysis"],
        "_3891": ["WormGearStabilityAnalysis"],
        "_3892": ["ZerolBevelGearMeshStabilityAnalysis"],
        "_3893": ["ZerolBevelGearSetStabilityAnalysis"],
        "_3894": ["ZerolBevelGearStabilityAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyStabilityAnalysis",
    "AbstractShaftOrHousingStabilityAnalysis",
    "AbstractShaftStabilityAnalysis",
    "AbstractShaftToMountableComponentConnectionStabilityAnalysis",
    "AGMAGleasonConicalGearMeshStabilityAnalysis",
    "AGMAGleasonConicalGearSetStabilityAnalysis",
    "AGMAGleasonConicalGearStabilityAnalysis",
    "AssemblyStabilityAnalysis",
    "BearingStabilityAnalysis",
    "BeltConnectionStabilityAnalysis",
    "BeltDriveStabilityAnalysis",
    "BevelDifferentialGearMeshStabilityAnalysis",
    "BevelDifferentialGearSetStabilityAnalysis",
    "BevelDifferentialGearStabilityAnalysis",
    "BevelDifferentialPlanetGearStabilityAnalysis",
    "BevelDifferentialSunGearStabilityAnalysis",
    "BevelGearMeshStabilityAnalysis",
    "BevelGearSetStabilityAnalysis",
    "BevelGearStabilityAnalysis",
    "BoltedJointStabilityAnalysis",
    "BoltStabilityAnalysis",
    "ClutchConnectionStabilityAnalysis",
    "ClutchHalfStabilityAnalysis",
    "ClutchStabilityAnalysis",
    "CoaxialConnectionStabilityAnalysis",
    "ComponentStabilityAnalysis",
    "ConceptCouplingConnectionStabilityAnalysis",
    "ConceptCouplingHalfStabilityAnalysis",
    "ConceptCouplingStabilityAnalysis",
    "ConceptGearMeshStabilityAnalysis",
    "ConceptGearSetStabilityAnalysis",
    "ConceptGearStabilityAnalysis",
    "ConicalGearMeshStabilityAnalysis",
    "ConicalGearSetStabilityAnalysis",
    "ConicalGearStabilityAnalysis",
    "ConnectionStabilityAnalysis",
    "ConnectorStabilityAnalysis",
    "CouplingConnectionStabilityAnalysis",
    "CouplingHalfStabilityAnalysis",
    "CouplingStabilityAnalysis",
    "CriticalSpeed",
    "CVTBeltConnectionStabilityAnalysis",
    "CVTPulleyStabilityAnalysis",
    "CVTStabilityAnalysis",
    "CycloidalAssemblyStabilityAnalysis",
    "CycloidalDiscCentralBearingConnectionStabilityAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis",
    "CycloidalDiscStabilityAnalysis",
    "CylindricalGearMeshStabilityAnalysis",
    "CylindricalGearSetStabilityAnalysis",
    "CylindricalGearStabilityAnalysis",
    "CylindricalPlanetGearStabilityAnalysis",
    "DatumStabilityAnalysis",
    "DynamicModelForStabilityAnalysis",
    "ExternalCADModelStabilityAnalysis",
    "FaceGearMeshStabilityAnalysis",
    "FaceGearSetStabilityAnalysis",
    "FaceGearStabilityAnalysis",
    "FEPartStabilityAnalysis",
    "FlexiblePinAssemblyStabilityAnalysis",
    "GearMeshStabilityAnalysis",
    "GearSetStabilityAnalysis",
    "GearStabilityAnalysis",
    "GuideDxfModelStabilityAnalysis",
    "HypoidGearMeshStabilityAnalysis",
    "HypoidGearSetStabilityAnalysis",
    "HypoidGearStabilityAnalysis",
    "InterMountableComponentConnectionStabilityAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
    "KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis",
    "KlingelnbergCycloPalloidHypoidGearStabilityAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis",
    "MassDiscStabilityAnalysis",
    "MeasurementComponentStabilityAnalysis",
    "MountableComponentStabilityAnalysis",
    "OilSealStabilityAnalysis",
    "PartStabilityAnalysis",
    "PartToPartShearCouplingConnectionStabilityAnalysis",
    "PartToPartShearCouplingHalfStabilityAnalysis",
    "PartToPartShearCouplingStabilityAnalysis",
    "PlanetaryConnectionStabilityAnalysis",
    "PlanetaryGearSetStabilityAnalysis",
    "PlanetCarrierStabilityAnalysis",
    "PointLoadStabilityAnalysis",
    "PowerLoadStabilityAnalysis",
    "PulleyStabilityAnalysis",
    "RingPinsStabilityAnalysis",
    "RingPinsToDiscConnectionStabilityAnalysis",
    "RollingRingAssemblyStabilityAnalysis",
    "RollingRingConnectionStabilityAnalysis",
    "RollingRingStabilityAnalysis",
    "RootAssemblyStabilityAnalysis",
    "ShaftHubConnectionStabilityAnalysis",
    "ShaftStabilityAnalysis",
    "ShaftToMountableComponentConnectionStabilityAnalysis",
    "SpecialisedAssemblyStabilityAnalysis",
    "SpiralBevelGearMeshStabilityAnalysis",
    "SpiralBevelGearSetStabilityAnalysis",
    "SpiralBevelGearStabilityAnalysis",
    "SpringDamperConnectionStabilityAnalysis",
    "SpringDamperHalfStabilityAnalysis",
    "SpringDamperStabilityAnalysis",
    "StabilityAnalysis",
    "StabilityAnalysisDrawStyle",
    "StabilityAnalysisOptions",
    "StraightBevelDiffGearMeshStabilityAnalysis",
    "StraightBevelDiffGearSetStabilityAnalysis",
    "StraightBevelDiffGearStabilityAnalysis",
    "StraightBevelGearMeshStabilityAnalysis",
    "StraightBevelGearSetStabilityAnalysis",
    "StraightBevelGearStabilityAnalysis",
    "StraightBevelPlanetGearStabilityAnalysis",
    "StraightBevelSunGearStabilityAnalysis",
    "SynchroniserHalfStabilityAnalysis",
    "SynchroniserPartStabilityAnalysis",
    "SynchroniserSleeveStabilityAnalysis",
    "SynchroniserStabilityAnalysis",
    "TorqueConverterConnectionStabilityAnalysis",
    "TorqueConverterPumpStabilityAnalysis",
    "TorqueConverterStabilityAnalysis",
    "TorqueConverterTurbineStabilityAnalysis",
    "UnbalancedMassStabilityAnalysis",
    "VirtualComponentStabilityAnalysis",
    "WormGearMeshStabilityAnalysis",
    "WormGearSetStabilityAnalysis",
    "WormGearStabilityAnalysis",
    "ZerolBevelGearMeshStabilityAnalysis",
    "ZerolBevelGearSetStabilityAnalysis",
    "ZerolBevelGearStabilityAnalysis",
)
