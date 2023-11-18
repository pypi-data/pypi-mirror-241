"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4725 import AbstractAssemblyCompoundModalAnalysis
    from ._4726 import AbstractShaftCompoundModalAnalysis
    from ._4727 import AbstractShaftOrHousingCompoundModalAnalysis
    from ._4728 import AbstractShaftToMountableComponentConnectionCompoundModalAnalysis
    from ._4729 import AGMAGleasonConicalGearCompoundModalAnalysis
    from ._4730 import AGMAGleasonConicalGearMeshCompoundModalAnalysis
    from ._4731 import AGMAGleasonConicalGearSetCompoundModalAnalysis
    from ._4732 import AssemblyCompoundModalAnalysis
    from ._4733 import BearingCompoundModalAnalysis
    from ._4734 import BeltConnectionCompoundModalAnalysis
    from ._4735 import BeltDriveCompoundModalAnalysis
    from ._4736 import BevelDifferentialGearCompoundModalAnalysis
    from ._4737 import BevelDifferentialGearMeshCompoundModalAnalysis
    from ._4738 import BevelDifferentialGearSetCompoundModalAnalysis
    from ._4739 import BevelDifferentialPlanetGearCompoundModalAnalysis
    from ._4740 import BevelDifferentialSunGearCompoundModalAnalysis
    from ._4741 import BevelGearCompoundModalAnalysis
    from ._4742 import BevelGearMeshCompoundModalAnalysis
    from ._4743 import BevelGearSetCompoundModalAnalysis
    from ._4744 import BoltCompoundModalAnalysis
    from ._4745 import BoltedJointCompoundModalAnalysis
    from ._4746 import ClutchCompoundModalAnalysis
    from ._4747 import ClutchConnectionCompoundModalAnalysis
    from ._4748 import ClutchHalfCompoundModalAnalysis
    from ._4749 import CoaxialConnectionCompoundModalAnalysis
    from ._4750 import ComponentCompoundModalAnalysis
    from ._4751 import ConceptCouplingCompoundModalAnalysis
    from ._4752 import ConceptCouplingConnectionCompoundModalAnalysis
    from ._4753 import ConceptCouplingHalfCompoundModalAnalysis
    from ._4754 import ConceptGearCompoundModalAnalysis
    from ._4755 import ConceptGearMeshCompoundModalAnalysis
    from ._4756 import ConceptGearSetCompoundModalAnalysis
    from ._4757 import ConicalGearCompoundModalAnalysis
    from ._4758 import ConicalGearMeshCompoundModalAnalysis
    from ._4759 import ConicalGearSetCompoundModalAnalysis
    from ._4760 import ConnectionCompoundModalAnalysis
    from ._4761 import ConnectorCompoundModalAnalysis
    from ._4762 import CouplingCompoundModalAnalysis
    from ._4763 import CouplingConnectionCompoundModalAnalysis
    from ._4764 import CouplingHalfCompoundModalAnalysis
    from ._4765 import CVTBeltConnectionCompoundModalAnalysis
    from ._4766 import CVTCompoundModalAnalysis
    from ._4767 import CVTPulleyCompoundModalAnalysis
    from ._4768 import CycloidalAssemblyCompoundModalAnalysis
    from ._4769 import CycloidalDiscCentralBearingConnectionCompoundModalAnalysis
    from ._4770 import CycloidalDiscCompoundModalAnalysis
    from ._4771 import CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis
    from ._4772 import CylindricalGearCompoundModalAnalysis
    from ._4773 import CylindricalGearMeshCompoundModalAnalysis
    from ._4774 import CylindricalGearSetCompoundModalAnalysis
    from ._4775 import CylindricalPlanetGearCompoundModalAnalysis
    from ._4776 import DatumCompoundModalAnalysis
    from ._4777 import ExternalCADModelCompoundModalAnalysis
    from ._4778 import FaceGearCompoundModalAnalysis
    from ._4779 import FaceGearMeshCompoundModalAnalysis
    from ._4780 import FaceGearSetCompoundModalAnalysis
    from ._4781 import FEPartCompoundModalAnalysis
    from ._4782 import FlexiblePinAssemblyCompoundModalAnalysis
    from ._4783 import GearCompoundModalAnalysis
    from ._4784 import GearMeshCompoundModalAnalysis
    from ._4785 import GearSetCompoundModalAnalysis
    from ._4786 import GuideDxfModelCompoundModalAnalysis
    from ._4787 import HypoidGearCompoundModalAnalysis
    from ._4788 import HypoidGearMeshCompoundModalAnalysis
    from ._4789 import HypoidGearSetCompoundModalAnalysis
    from ._4790 import InterMountableComponentConnectionCompoundModalAnalysis
    from ._4791 import KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis
    from ._4792 import KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis
    from ._4793 import KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis
    from ._4794 import KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis
    from ._4795 import KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis
    from ._4796 import KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis
    from ._4797 import KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis
    from ._4798 import KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis
    from ._4799 import KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis
    from ._4800 import MassDiscCompoundModalAnalysis
    from ._4801 import MeasurementComponentCompoundModalAnalysis
    from ._4802 import MountableComponentCompoundModalAnalysis
    from ._4803 import OilSealCompoundModalAnalysis
    from ._4804 import PartCompoundModalAnalysis
    from ._4805 import PartToPartShearCouplingCompoundModalAnalysis
    from ._4806 import PartToPartShearCouplingConnectionCompoundModalAnalysis
    from ._4807 import PartToPartShearCouplingHalfCompoundModalAnalysis
    from ._4808 import PlanetaryConnectionCompoundModalAnalysis
    from ._4809 import PlanetaryGearSetCompoundModalAnalysis
    from ._4810 import PlanetCarrierCompoundModalAnalysis
    from ._4811 import PointLoadCompoundModalAnalysis
    from ._4812 import PowerLoadCompoundModalAnalysis
    from ._4813 import PulleyCompoundModalAnalysis
    from ._4814 import RingPinsCompoundModalAnalysis
    from ._4815 import RingPinsToDiscConnectionCompoundModalAnalysis
    from ._4816 import RollingRingAssemblyCompoundModalAnalysis
    from ._4817 import RollingRingCompoundModalAnalysis
    from ._4818 import RollingRingConnectionCompoundModalAnalysis
    from ._4819 import RootAssemblyCompoundModalAnalysis
    from ._4820 import ShaftCompoundModalAnalysis
    from ._4821 import ShaftHubConnectionCompoundModalAnalysis
    from ._4822 import ShaftToMountableComponentConnectionCompoundModalAnalysis
    from ._4823 import SpecialisedAssemblyCompoundModalAnalysis
    from ._4824 import SpiralBevelGearCompoundModalAnalysis
    from ._4825 import SpiralBevelGearMeshCompoundModalAnalysis
    from ._4826 import SpiralBevelGearSetCompoundModalAnalysis
    from ._4827 import SpringDamperCompoundModalAnalysis
    from ._4828 import SpringDamperConnectionCompoundModalAnalysis
    from ._4829 import SpringDamperHalfCompoundModalAnalysis
    from ._4830 import StraightBevelDiffGearCompoundModalAnalysis
    from ._4831 import StraightBevelDiffGearMeshCompoundModalAnalysis
    from ._4832 import StraightBevelDiffGearSetCompoundModalAnalysis
    from ._4833 import StraightBevelGearCompoundModalAnalysis
    from ._4834 import StraightBevelGearMeshCompoundModalAnalysis
    from ._4835 import StraightBevelGearSetCompoundModalAnalysis
    from ._4836 import StraightBevelPlanetGearCompoundModalAnalysis
    from ._4837 import StraightBevelSunGearCompoundModalAnalysis
    from ._4838 import SynchroniserCompoundModalAnalysis
    from ._4839 import SynchroniserHalfCompoundModalAnalysis
    from ._4840 import SynchroniserPartCompoundModalAnalysis
    from ._4841 import SynchroniserSleeveCompoundModalAnalysis
    from ._4842 import TorqueConverterCompoundModalAnalysis
    from ._4843 import TorqueConverterConnectionCompoundModalAnalysis
    from ._4844 import TorqueConverterPumpCompoundModalAnalysis
    from ._4845 import TorqueConverterTurbineCompoundModalAnalysis
    from ._4846 import UnbalancedMassCompoundModalAnalysis
    from ._4847 import VirtualComponentCompoundModalAnalysis
    from ._4848 import WormGearCompoundModalAnalysis
    from ._4849 import WormGearMeshCompoundModalAnalysis
    from ._4850 import WormGearSetCompoundModalAnalysis
    from ._4851 import ZerolBevelGearCompoundModalAnalysis
    from ._4852 import ZerolBevelGearMeshCompoundModalAnalysis
    from ._4853 import ZerolBevelGearSetCompoundModalAnalysis
else:
    import_structure = {
        "_4725": ["AbstractAssemblyCompoundModalAnalysis"],
        "_4726": ["AbstractShaftCompoundModalAnalysis"],
        "_4727": ["AbstractShaftOrHousingCompoundModalAnalysis"],
        "_4728": ["AbstractShaftToMountableComponentConnectionCompoundModalAnalysis"],
        "_4729": ["AGMAGleasonConicalGearCompoundModalAnalysis"],
        "_4730": ["AGMAGleasonConicalGearMeshCompoundModalAnalysis"],
        "_4731": ["AGMAGleasonConicalGearSetCompoundModalAnalysis"],
        "_4732": ["AssemblyCompoundModalAnalysis"],
        "_4733": ["BearingCompoundModalAnalysis"],
        "_4734": ["BeltConnectionCompoundModalAnalysis"],
        "_4735": ["BeltDriveCompoundModalAnalysis"],
        "_4736": ["BevelDifferentialGearCompoundModalAnalysis"],
        "_4737": ["BevelDifferentialGearMeshCompoundModalAnalysis"],
        "_4738": ["BevelDifferentialGearSetCompoundModalAnalysis"],
        "_4739": ["BevelDifferentialPlanetGearCompoundModalAnalysis"],
        "_4740": ["BevelDifferentialSunGearCompoundModalAnalysis"],
        "_4741": ["BevelGearCompoundModalAnalysis"],
        "_4742": ["BevelGearMeshCompoundModalAnalysis"],
        "_4743": ["BevelGearSetCompoundModalAnalysis"],
        "_4744": ["BoltCompoundModalAnalysis"],
        "_4745": ["BoltedJointCompoundModalAnalysis"],
        "_4746": ["ClutchCompoundModalAnalysis"],
        "_4747": ["ClutchConnectionCompoundModalAnalysis"],
        "_4748": ["ClutchHalfCompoundModalAnalysis"],
        "_4749": ["CoaxialConnectionCompoundModalAnalysis"],
        "_4750": ["ComponentCompoundModalAnalysis"],
        "_4751": ["ConceptCouplingCompoundModalAnalysis"],
        "_4752": ["ConceptCouplingConnectionCompoundModalAnalysis"],
        "_4753": ["ConceptCouplingHalfCompoundModalAnalysis"],
        "_4754": ["ConceptGearCompoundModalAnalysis"],
        "_4755": ["ConceptGearMeshCompoundModalAnalysis"],
        "_4756": ["ConceptGearSetCompoundModalAnalysis"],
        "_4757": ["ConicalGearCompoundModalAnalysis"],
        "_4758": ["ConicalGearMeshCompoundModalAnalysis"],
        "_4759": ["ConicalGearSetCompoundModalAnalysis"],
        "_4760": ["ConnectionCompoundModalAnalysis"],
        "_4761": ["ConnectorCompoundModalAnalysis"],
        "_4762": ["CouplingCompoundModalAnalysis"],
        "_4763": ["CouplingConnectionCompoundModalAnalysis"],
        "_4764": ["CouplingHalfCompoundModalAnalysis"],
        "_4765": ["CVTBeltConnectionCompoundModalAnalysis"],
        "_4766": ["CVTCompoundModalAnalysis"],
        "_4767": ["CVTPulleyCompoundModalAnalysis"],
        "_4768": ["CycloidalAssemblyCompoundModalAnalysis"],
        "_4769": ["CycloidalDiscCentralBearingConnectionCompoundModalAnalysis"],
        "_4770": ["CycloidalDiscCompoundModalAnalysis"],
        "_4771": ["CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis"],
        "_4772": ["CylindricalGearCompoundModalAnalysis"],
        "_4773": ["CylindricalGearMeshCompoundModalAnalysis"],
        "_4774": ["CylindricalGearSetCompoundModalAnalysis"],
        "_4775": ["CylindricalPlanetGearCompoundModalAnalysis"],
        "_4776": ["DatumCompoundModalAnalysis"],
        "_4777": ["ExternalCADModelCompoundModalAnalysis"],
        "_4778": ["FaceGearCompoundModalAnalysis"],
        "_4779": ["FaceGearMeshCompoundModalAnalysis"],
        "_4780": ["FaceGearSetCompoundModalAnalysis"],
        "_4781": ["FEPartCompoundModalAnalysis"],
        "_4782": ["FlexiblePinAssemblyCompoundModalAnalysis"],
        "_4783": ["GearCompoundModalAnalysis"],
        "_4784": ["GearMeshCompoundModalAnalysis"],
        "_4785": ["GearSetCompoundModalAnalysis"],
        "_4786": ["GuideDxfModelCompoundModalAnalysis"],
        "_4787": ["HypoidGearCompoundModalAnalysis"],
        "_4788": ["HypoidGearMeshCompoundModalAnalysis"],
        "_4789": ["HypoidGearSetCompoundModalAnalysis"],
        "_4790": ["InterMountableComponentConnectionCompoundModalAnalysis"],
        "_4791": ["KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis"],
        "_4792": ["KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis"],
        "_4793": ["KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis"],
        "_4794": ["KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis"],
        "_4795": ["KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis"],
        "_4796": ["KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis"],
        "_4797": ["KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis"],
        "_4798": ["KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis"],
        "_4799": ["KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis"],
        "_4800": ["MassDiscCompoundModalAnalysis"],
        "_4801": ["MeasurementComponentCompoundModalAnalysis"],
        "_4802": ["MountableComponentCompoundModalAnalysis"],
        "_4803": ["OilSealCompoundModalAnalysis"],
        "_4804": ["PartCompoundModalAnalysis"],
        "_4805": ["PartToPartShearCouplingCompoundModalAnalysis"],
        "_4806": ["PartToPartShearCouplingConnectionCompoundModalAnalysis"],
        "_4807": ["PartToPartShearCouplingHalfCompoundModalAnalysis"],
        "_4808": ["PlanetaryConnectionCompoundModalAnalysis"],
        "_4809": ["PlanetaryGearSetCompoundModalAnalysis"],
        "_4810": ["PlanetCarrierCompoundModalAnalysis"],
        "_4811": ["PointLoadCompoundModalAnalysis"],
        "_4812": ["PowerLoadCompoundModalAnalysis"],
        "_4813": ["PulleyCompoundModalAnalysis"],
        "_4814": ["RingPinsCompoundModalAnalysis"],
        "_4815": ["RingPinsToDiscConnectionCompoundModalAnalysis"],
        "_4816": ["RollingRingAssemblyCompoundModalAnalysis"],
        "_4817": ["RollingRingCompoundModalAnalysis"],
        "_4818": ["RollingRingConnectionCompoundModalAnalysis"],
        "_4819": ["RootAssemblyCompoundModalAnalysis"],
        "_4820": ["ShaftCompoundModalAnalysis"],
        "_4821": ["ShaftHubConnectionCompoundModalAnalysis"],
        "_4822": ["ShaftToMountableComponentConnectionCompoundModalAnalysis"],
        "_4823": ["SpecialisedAssemblyCompoundModalAnalysis"],
        "_4824": ["SpiralBevelGearCompoundModalAnalysis"],
        "_4825": ["SpiralBevelGearMeshCompoundModalAnalysis"],
        "_4826": ["SpiralBevelGearSetCompoundModalAnalysis"],
        "_4827": ["SpringDamperCompoundModalAnalysis"],
        "_4828": ["SpringDamperConnectionCompoundModalAnalysis"],
        "_4829": ["SpringDamperHalfCompoundModalAnalysis"],
        "_4830": ["StraightBevelDiffGearCompoundModalAnalysis"],
        "_4831": ["StraightBevelDiffGearMeshCompoundModalAnalysis"],
        "_4832": ["StraightBevelDiffGearSetCompoundModalAnalysis"],
        "_4833": ["StraightBevelGearCompoundModalAnalysis"],
        "_4834": ["StraightBevelGearMeshCompoundModalAnalysis"],
        "_4835": ["StraightBevelGearSetCompoundModalAnalysis"],
        "_4836": ["StraightBevelPlanetGearCompoundModalAnalysis"],
        "_4837": ["StraightBevelSunGearCompoundModalAnalysis"],
        "_4838": ["SynchroniserCompoundModalAnalysis"],
        "_4839": ["SynchroniserHalfCompoundModalAnalysis"],
        "_4840": ["SynchroniserPartCompoundModalAnalysis"],
        "_4841": ["SynchroniserSleeveCompoundModalAnalysis"],
        "_4842": ["TorqueConverterCompoundModalAnalysis"],
        "_4843": ["TorqueConverterConnectionCompoundModalAnalysis"],
        "_4844": ["TorqueConverterPumpCompoundModalAnalysis"],
        "_4845": ["TorqueConverterTurbineCompoundModalAnalysis"],
        "_4846": ["UnbalancedMassCompoundModalAnalysis"],
        "_4847": ["VirtualComponentCompoundModalAnalysis"],
        "_4848": ["WormGearCompoundModalAnalysis"],
        "_4849": ["WormGearMeshCompoundModalAnalysis"],
        "_4850": ["WormGearSetCompoundModalAnalysis"],
        "_4851": ["ZerolBevelGearCompoundModalAnalysis"],
        "_4852": ["ZerolBevelGearMeshCompoundModalAnalysis"],
        "_4853": ["ZerolBevelGearSetCompoundModalAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundModalAnalysis",
    "AbstractShaftCompoundModalAnalysis",
    "AbstractShaftOrHousingCompoundModalAnalysis",
    "AbstractShaftToMountableComponentConnectionCompoundModalAnalysis",
    "AGMAGleasonConicalGearCompoundModalAnalysis",
    "AGMAGleasonConicalGearMeshCompoundModalAnalysis",
    "AGMAGleasonConicalGearSetCompoundModalAnalysis",
    "AssemblyCompoundModalAnalysis",
    "BearingCompoundModalAnalysis",
    "BeltConnectionCompoundModalAnalysis",
    "BeltDriveCompoundModalAnalysis",
    "BevelDifferentialGearCompoundModalAnalysis",
    "BevelDifferentialGearMeshCompoundModalAnalysis",
    "BevelDifferentialGearSetCompoundModalAnalysis",
    "BevelDifferentialPlanetGearCompoundModalAnalysis",
    "BevelDifferentialSunGearCompoundModalAnalysis",
    "BevelGearCompoundModalAnalysis",
    "BevelGearMeshCompoundModalAnalysis",
    "BevelGearSetCompoundModalAnalysis",
    "BoltCompoundModalAnalysis",
    "BoltedJointCompoundModalAnalysis",
    "ClutchCompoundModalAnalysis",
    "ClutchConnectionCompoundModalAnalysis",
    "ClutchHalfCompoundModalAnalysis",
    "CoaxialConnectionCompoundModalAnalysis",
    "ComponentCompoundModalAnalysis",
    "ConceptCouplingCompoundModalAnalysis",
    "ConceptCouplingConnectionCompoundModalAnalysis",
    "ConceptCouplingHalfCompoundModalAnalysis",
    "ConceptGearCompoundModalAnalysis",
    "ConceptGearMeshCompoundModalAnalysis",
    "ConceptGearSetCompoundModalAnalysis",
    "ConicalGearCompoundModalAnalysis",
    "ConicalGearMeshCompoundModalAnalysis",
    "ConicalGearSetCompoundModalAnalysis",
    "ConnectionCompoundModalAnalysis",
    "ConnectorCompoundModalAnalysis",
    "CouplingCompoundModalAnalysis",
    "CouplingConnectionCompoundModalAnalysis",
    "CouplingHalfCompoundModalAnalysis",
    "CVTBeltConnectionCompoundModalAnalysis",
    "CVTCompoundModalAnalysis",
    "CVTPulleyCompoundModalAnalysis",
    "CycloidalAssemblyCompoundModalAnalysis",
    "CycloidalDiscCentralBearingConnectionCompoundModalAnalysis",
    "CycloidalDiscCompoundModalAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis",
    "CylindricalGearCompoundModalAnalysis",
    "CylindricalGearMeshCompoundModalAnalysis",
    "CylindricalGearSetCompoundModalAnalysis",
    "CylindricalPlanetGearCompoundModalAnalysis",
    "DatumCompoundModalAnalysis",
    "ExternalCADModelCompoundModalAnalysis",
    "FaceGearCompoundModalAnalysis",
    "FaceGearMeshCompoundModalAnalysis",
    "FaceGearSetCompoundModalAnalysis",
    "FEPartCompoundModalAnalysis",
    "FlexiblePinAssemblyCompoundModalAnalysis",
    "GearCompoundModalAnalysis",
    "GearMeshCompoundModalAnalysis",
    "GearSetCompoundModalAnalysis",
    "GuideDxfModelCompoundModalAnalysis",
    "HypoidGearCompoundModalAnalysis",
    "HypoidGearMeshCompoundModalAnalysis",
    "HypoidGearSetCompoundModalAnalysis",
    "InterMountableComponentConnectionCompoundModalAnalysis",
    "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis",
    "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis",
    "MassDiscCompoundModalAnalysis",
    "MeasurementComponentCompoundModalAnalysis",
    "MountableComponentCompoundModalAnalysis",
    "OilSealCompoundModalAnalysis",
    "PartCompoundModalAnalysis",
    "PartToPartShearCouplingCompoundModalAnalysis",
    "PartToPartShearCouplingConnectionCompoundModalAnalysis",
    "PartToPartShearCouplingHalfCompoundModalAnalysis",
    "PlanetaryConnectionCompoundModalAnalysis",
    "PlanetaryGearSetCompoundModalAnalysis",
    "PlanetCarrierCompoundModalAnalysis",
    "PointLoadCompoundModalAnalysis",
    "PowerLoadCompoundModalAnalysis",
    "PulleyCompoundModalAnalysis",
    "RingPinsCompoundModalAnalysis",
    "RingPinsToDiscConnectionCompoundModalAnalysis",
    "RollingRingAssemblyCompoundModalAnalysis",
    "RollingRingCompoundModalAnalysis",
    "RollingRingConnectionCompoundModalAnalysis",
    "RootAssemblyCompoundModalAnalysis",
    "ShaftCompoundModalAnalysis",
    "ShaftHubConnectionCompoundModalAnalysis",
    "ShaftToMountableComponentConnectionCompoundModalAnalysis",
    "SpecialisedAssemblyCompoundModalAnalysis",
    "SpiralBevelGearCompoundModalAnalysis",
    "SpiralBevelGearMeshCompoundModalAnalysis",
    "SpiralBevelGearSetCompoundModalAnalysis",
    "SpringDamperCompoundModalAnalysis",
    "SpringDamperConnectionCompoundModalAnalysis",
    "SpringDamperHalfCompoundModalAnalysis",
    "StraightBevelDiffGearCompoundModalAnalysis",
    "StraightBevelDiffGearMeshCompoundModalAnalysis",
    "StraightBevelDiffGearSetCompoundModalAnalysis",
    "StraightBevelGearCompoundModalAnalysis",
    "StraightBevelGearMeshCompoundModalAnalysis",
    "StraightBevelGearSetCompoundModalAnalysis",
    "StraightBevelPlanetGearCompoundModalAnalysis",
    "StraightBevelSunGearCompoundModalAnalysis",
    "SynchroniserCompoundModalAnalysis",
    "SynchroniserHalfCompoundModalAnalysis",
    "SynchroniserPartCompoundModalAnalysis",
    "SynchroniserSleeveCompoundModalAnalysis",
    "TorqueConverterCompoundModalAnalysis",
    "TorqueConverterConnectionCompoundModalAnalysis",
    "TorqueConverterPumpCompoundModalAnalysis",
    "TorqueConverterTurbineCompoundModalAnalysis",
    "UnbalancedMassCompoundModalAnalysis",
    "VirtualComponentCompoundModalAnalysis",
    "WormGearCompoundModalAnalysis",
    "WormGearMeshCompoundModalAnalysis",
    "WormGearSetCompoundModalAnalysis",
    "ZerolBevelGearCompoundModalAnalysis",
    "ZerolBevelGearMeshCompoundModalAnalysis",
    "ZerolBevelGearSetCompoundModalAnalysis",
)
