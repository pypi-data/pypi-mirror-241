"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4985 import AbstractAssemblyCompoundModalAnalysisAtAStiffness
    from ._4986 import AbstractShaftCompoundModalAnalysisAtAStiffness
    from ._4987 import AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness
    from ._4988 import (
        AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._4989 import AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness
    from ._4990 import AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness
    from ._4991 import AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness
    from ._4992 import AssemblyCompoundModalAnalysisAtAStiffness
    from ._4993 import BearingCompoundModalAnalysisAtAStiffness
    from ._4994 import BeltConnectionCompoundModalAnalysisAtAStiffness
    from ._4995 import BeltDriveCompoundModalAnalysisAtAStiffness
    from ._4996 import BevelDifferentialGearCompoundModalAnalysisAtAStiffness
    from ._4997 import BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness
    from ._4998 import BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness
    from ._4999 import BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness
    from ._5000 import BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness
    from ._5001 import BevelGearCompoundModalAnalysisAtAStiffness
    from ._5002 import BevelGearMeshCompoundModalAnalysisAtAStiffness
    from ._5003 import BevelGearSetCompoundModalAnalysisAtAStiffness
    from ._5004 import BoltCompoundModalAnalysisAtAStiffness
    from ._5005 import BoltedJointCompoundModalAnalysisAtAStiffness
    from ._5006 import ClutchCompoundModalAnalysisAtAStiffness
    from ._5007 import ClutchConnectionCompoundModalAnalysisAtAStiffness
    from ._5008 import ClutchHalfCompoundModalAnalysisAtAStiffness
    from ._5009 import CoaxialConnectionCompoundModalAnalysisAtAStiffness
    from ._5010 import ComponentCompoundModalAnalysisAtAStiffness
    from ._5011 import ConceptCouplingCompoundModalAnalysisAtAStiffness
    from ._5012 import ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness
    from ._5013 import ConceptCouplingHalfCompoundModalAnalysisAtAStiffness
    from ._5014 import ConceptGearCompoundModalAnalysisAtAStiffness
    from ._5015 import ConceptGearMeshCompoundModalAnalysisAtAStiffness
    from ._5016 import ConceptGearSetCompoundModalAnalysisAtAStiffness
    from ._5017 import ConicalGearCompoundModalAnalysisAtAStiffness
    from ._5018 import ConicalGearMeshCompoundModalAnalysisAtAStiffness
    from ._5019 import ConicalGearSetCompoundModalAnalysisAtAStiffness
    from ._5020 import ConnectionCompoundModalAnalysisAtAStiffness
    from ._5021 import ConnectorCompoundModalAnalysisAtAStiffness
    from ._5022 import CouplingCompoundModalAnalysisAtAStiffness
    from ._5023 import CouplingConnectionCompoundModalAnalysisAtAStiffness
    from ._5024 import CouplingHalfCompoundModalAnalysisAtAStiffness
    from ._5025 import CVTBeltConnectionCompoundModalAnalysisAtAStiffness
    from ._5026 import CVTCompoundModalAnalysisAtAStiffness
    from ._5027 import CVTPulleyCompoundModalAnalysisAtAStiffness
    from ._5028 import CycloidalAssemblyCompoundModalAnalysisAtAStiffness
    from ._5029 import (
        CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._5030 import CycloidalDiscCompoundModalAnalysisAtAStiffness
    from ._5031 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._5032 import CylindricalGearCompoundModalAnalysisAtAStiffness
    from ._5033 import CylindricalGearMeshCompoundModalAnalysisAtAStiffness
    from ._5034 import CylindricalGearSetCompoundModalAnalysisAtAStiffness
    from ._5035 import CylindricalPlanetGearCompoundModalAnalysisAtAStiffness
    from ._5036 import DatumCompoundModalAnalysisAtAStiffness
    from ._5037 import ExternalCADModelCompoundModalAnalysisAtAStiffness
    from ._5038 import FaceGearCompoundModalAnalysisAtAStiffness
    from ._5039 import FaceGearMeshCompoundModalAnalysisAtAStiffness
    from ._5040 import FaceGearSetCompoundModalAnalysisAtAStiffness
    from ._5041 import FEPartCompoundModalAnalysisAtAStiffness
    from ._5042 import FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness
    from ._5043 import GearCompoundModalAnalysisAtAStiffness
    from ._5044 import GearMeshCompoundModalAnalysisAtAStiffness
    from ._5045 import GearSetCompoundModalAnalysisAtAStiffness
    from ._5046 import GuideDxfModelCompoundModalAnalysisAtAStiffness
    from ._5047 import HypoidGearCompoundModalAnalysisAtAStiffness
    from ._5048 import HypoidGearMeshCompoundModalAnalysisAtAStiffness
    from ._5049 import HypoidGearSetCompoundModalAnalysisAtAStiffness
    from ._5050 import (
        InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._5051 import (
        KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness,
    )
    from ._5052 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness,
    )
    from ._5053 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness,
    )
    from ._5054 import (
        KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness,
    )
    from ._5055 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness,
    )
    from ._5056 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness,
    )
    from ._5057 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness,
    )
    from ._5058 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtAStiffness,
    )
    from ._5059 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness,
    )
    from ._5060 import MassDiscCompoundModalAnalysisAtAStiffness
    from ._5061 import MeasurementComponentCompoundModalAnalysisAtAStiffness
    from ._5062 import MountableComponentCompoundModalAnalysisAtAStiffness
    from ._5063 import OilSealCompoundModalAnalysisAtAStiffness
    from ._5064 import PartCompoundModalAnalysisAtAStiffness
    from ._5065 import PartToPartShearCouplingCompoundModalAnalysisAtAStiffness
    from ._5066 import (
        PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._5067 import PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness
    from ._5068 import PlanetaryConnectionCompoundModalAnalysisAtAStiffness
    from ._5069 import PlanetaryGearSetCompoundModalAnalysisAtAStiffness
    from ._5070 import PlanetCarrierCompoundModalAnalysisAtAStiffness
    from ._5071 import PointLoadCompoundModalAnalysisAtAStiffness
    from ._5072 import PowerLoadCompoundModalAnalysisAtAStiffness
    from ._5073 import PulleyCompoundModalAnalysisAtAStiffness
    from ._5074 import RingPinsCompoundModalAnalysisAtAStiffness
    from ._5075 import RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness
    from ._5076 import RollingRingAssemblyCompoundModalAnalysisAtAStiffness
    from ._5077 import RollingRingCompoundModalAnalysisAtAStiffness
    from ._5078 import RollingRingConnectionCompoundModalAnalysisAtAStiffness
    from ._5079 import RootAssemblyCompoundModalAnalysisAtAStiffness
    from ._5080 import ShaftCompoundModalAnalysisAtAStiffness
    from ._5081 import ShaftHubConnectionCompoundModalAnalysisAtAStiffness
    from ._5082 import (
        ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._5083 import SpecialisedAssemblyCompoundModalAnalysisAtAStiffness
    from ._5084 import SpiralBevelGearCompoundModalAnalysisAtAStiffness
    from ._5085 import SpiralBevelGearMeshCompoundModalAnalysisAtAStiffness
    from ._5086 import SpiralBevelGearSetCompoundModalAnalysisAtAStiffness
    from ._5087 import SpringDamperCompoundModalAnalysisAtAStiffness
    from ._5088 import SpringDamperConnectionCompoundModalAnalysisAtAStiffness
    from ._5089 import SpringDamperHalfCompoundModalAnalysisAtAStiffness
    from ._5090 import StraightBevelDiffGearCompoundModalAnalysisAtAStiffness
    from ._5091 import StraightBevelDiffGearMeshCompoundModalAnalysisAtAStiffness
    from ._5092 import StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness
    from ._5093 import StraightBevelGearCompoundModalAnalysisAtAStiffness
    from ._5094 import StraightBevelGearMeshCompoundModalAnalysisAtAStiffness
    from ._5095 import StraightBevelGearSetCompoundModalAnalysisAtAStiffness
    from ._5096 import StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness
    from ._5097 import StraightBevelSunGearCompoundModalAnalysisAtAStiffness
    from ._5098 import SynchroniserCompoundModalAnalysisAtAStiffness
    from ._5099 import SynchroniserHalfCompoundModalAnalysisAtAStiffness
    from ._5100 import SynchroniserPartCompoundModalAnalysisAtAStiffness
    from ._5101 import SynchroniserSleeveCompoundModalAnalysisAtAStiffness
    from ._5102 import TorqueConverterCompoundModalAnalysisAtAStiffness
    from ._5103 import TorqueConverterConnectionCompoundModalAnalysisAtAStiffness
    from ._5104 import TorqueConverterPumpCompoundModalAnalysisAtAStiffness
    from ._5105 import TorqueConverterTurbineCompoundModalAnalysisAtAStiffness
    from ._5106 import UnbalancedMassCompoundModalAnalysisAtAStiffness
    from ._5107 import VirtualComponentCompoundModalAnalysisAtAStiffness
    from ._5108 import WormGearCompoundModalAnalysisAtAStiffness
    from ._5109 import WormGearMeshCompoundModalAnalysisAtAStiffness
    from ._5110 import WormGearSetCompoundModalAnalysisAtAStiffness
    from ._5111 import ZerolBevelGearCompoundModalAnalysisAtAStiffness
    from ._5112 import ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness
    from ._5113 import ZerolBevelGearSetCompoundModalAnalysisAtAStiffness
else:
    import_structure = {
        "_4985": ["AbstractAssemblyCompoundModalAnalysisAtAStiffness"],
        "_4986": ["AbstractShaftCompoundModalAnalysisAtAStiffness"],
        "_4987": ["AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness"],
        "_4988": [
            "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness"
        ],
        "_4989": ["AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness"],
        "_4990": ["AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness"],
        "_4991": ["AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness"],
        "_4992": ["AssemblyCompoundModalAnalysisAtAStiffness"],
        "_4993": ["BearingCompoundModalAnalysisAtAStiffness"],
        "_4994": ["BeltConnectionCompoundModalAnalysisAtAStiffness"],
        "_4995": ["BeltDriveCompoundModalAnalysisAtAStiffness"],
        "_4996": ["BevelDifferentialGearCompoundModalAnalysisAtAStiffness"],
        "_4997": ["BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness"],
        "_4998": ["BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness"],
        "_4999": ["BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness"],
        "_5000": ["BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness"],
        "_5001": ["BevelGearCompoundModalAnalysisAtAStiffness"],
        "_5002": ["BevelGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5003": ["BevelGearSetCompoundModalAnalysisAtAStiffness"],
        "_5004": ["BoltCompoundModalAnalysisAtAStiffness"],
        "_5005": ["BoltedJointCompoundModalAnalysisAtAStiffness"],
        "_5006": ["ClutchCompoundModalAnalysisAtAStiffness"],
        "_5007": ["ClutchConnectionCompoundModalAnalysisAtAStiffness"],
        "_5008": ["ClutchHalfCompoundModalAnalysisAtAStiffness"],
        "_5009": ["CoaxialConnectionCompoundModalAnalysisAtAStiffness"],
        "_5010": ["ComponentCompoundModalAnalysisAtAStiffness"],
        "_5011": ["ConceptCouplingCompoundModalAnalysisAtAStiffness"],
        "_5012": ["ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness"],
        "_5013": ["ConceptCouplingHalfCompoundModalAnalysisAtAStiffness"],
        "_5014": ["ConceptGearCompoundModalAnalysisAtAStiffness"],
        "_5015": ["ConceptGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5016": ["ConceptGearSetCompoundModalAnalysisAtAStiffness"],
        "_5017": ["ConicalGearCompoundModalAnalysisAtAStiffness"],
        "_5018": ["ConicalGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5019": ["ConicalGearSetCompoundModalAnalysisAtAStiffness"],
        "_5020": ["ConnectionCompoundModalAnalysisAtAStiffness"],
        "_5021": ["ConnectorCompoundModalAnalysisAtAStiffness"],
        "_5022": ["CouplingCompoundModalAnalysisAtAStiffness"],
        "_5023": ["CouplingConnectionCompoundModalAnalysisAtAStiffness"],
        "_5024": ["CouplingHalfCompoundModalAnalysisAtAStiffness"],
        "_5025": ["CVTBeltConnectionCompoundModalAnalysisAtAStiffness"],
        "_5026": ["CVTCompoundModalAnalysisAtAStiffness"],
        "_5027": ["CVTPulleyCompoundModalAnalysisAtAStiffness"],
        "_5028": ["CycloidalAssemblyCompoundModalAnalysisAtAStiffness"],
        "_5029": [
            "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness"
        ],
        "_5030": ["CycloidalDiscCompoundModalAnalysisAtAStiffness"],
        "_5031": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness"
        ],
        "_5032": ["CylindricalGearCompoundModalAnalysisAtAStiffness"],
        "_5033": ["CylindricalGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5034": ["CylindricalGearSetCompoundModalAnalysisAtAStiffness"],
        "_5035": ["CylindricalPlanetGearCompoundModalAnalysisAtAStiffness"],
        "_5036": ["DatumCompoundModalAnalysisAtAStiffness"],
        "_5037": ["ExternalCADModelCompoundModalAnalysisAtAStiffness"],
        "_5038": ["FaceGearCompoundModalAnalysisAtAStiffness"],
        "_5039": ["FaceGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5040": ["FaceGearSetCompoundModalAnalysisAtAStiffness"],
        "_5041": ["FEPartCompoundModalAnalysisAtAStiffness"],
        "_5042": ["FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness"],
        "_5043": ["GearCompoundModalAnalysisAtAStiffness"],
        "_5044": ["GearMeshCompoundModalAnalysisAtAStiffness"],
        "_5045": ["GearSetCompoundModalAnalysisAtAStiffness"],
        "_5046": ["GuideDxfModelCompoundModalAnalysisAtAStiffness"],
        "_5047": ["HypoidGearCompoundModalAnalysisAtAStiffness"],
        "_5048": ["HypoidGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5049": ["HypoidGearSetCompoundModalAnalysisAtAStiffness"],
        "_5050": ["InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness"],
        "_5051": [
            "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness"
        ],
        "_5052": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness"
        ],
        "_5053": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness"
        ],
        "_5054": [
            "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness"
        ],
        "_5055": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness"
        ],
        "_5056": [
            "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness"
        ],
        "_5057": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness"
        ],
        "_5058": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtAStiffness"
        ],
        "_5059": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness"
        ],
        "_5060": ["MassDiscCompoundModalAnalysisAtAStiffness"],
        "_5061": ["MeasurementComponentCompoundModalAnalysisAtAStiffness"],
        "_5062": ["MountableComponentCompoundModalAnalysisAtAStiffness"],
        "_5063": ["OilSealCompoundModalAnalysisAtAStiffness"],
        "_5064": ["PartCompoundModalAnalysisAtAStiffness"],
        "_5065": ["PartToPartShearCouplingCompoundModalAnalysisAtAStiffness"],
        "_5066": ["PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness"],
        "_5067": ["PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness"],
        "_5068": ["PlanetaryConnectionCompoundModalAnalysisAtAStiffness"],
        "_5069": ["PlanetaryGearSetCompoundModalAnalysisAtAStiffness"],
        "_5070": ["PlanetCarrierCompoundModalAnalysisAtAStiffness"],
        "_5071": ["PointLoadCompoundModalAnalysisAtAStiffness"],
        "_5072": ["PowerLoadCompoundModalAnalysisAtAStiffness"],
        "_5073": ["PulleyCompoundModalAnalysisAtAStiffness"],
        "_5074": ["RingPinsCompoundModalAnalysisAtAStiffness"],
        "_5075": ["RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness"],
        "_5076": ["RollingRingAssemblyCompoundModalAnalysisAtAStiffness"],
        "_5077": ["RollingRingCompoundModalAnalysisAtAStiffness"],
        "_5078": ["RollingRingConnectionCompoundModalAnalysisAtAStiffness"],
        "_5079": ["RootAssemblyCompoundModalAnalysisAtAStiffness"],
        "_5080": ["ShaftCompoundModalAnalysisAtAStiffness"],
        "_5081": ["ShaftHubConnectionCompoundModalAnalysisAtAStiffness"],
        "_5082": [
            "ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness"
        ],
        "_5083": ["SpecialisedAssemblyCompoundModalAnalysisAtAStiffness"],
        "_5084": ["SpiralBevelGearCompoundModalAnalysisAtAStiffness"],
        "_5085": ["SpiralBevelGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5086": ["SpiralBevelGearSetCompoundModalAnalysisAtAStiffness"],
        "_5087": ["SpringDamperCompoundModalAnalysisAtAStiffness"],
        "_5088": ["SpringDamperConnectionCompoundModalAnalysisAtAStiffness"],
        "_5089": ["SpringDamperHalfCompoundModalAnalysisAtAStiffness"],
        "_5090": ["StraightBevelDiffGearCompoundModalAnalysisAtAStiffness"],
        "_5091": ["StraightBevelDiffGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5092": ["StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness"],
        "_5093": ["StraightBevelGearCompoundModalAnalysisAtAStiffness"],
        "_5094": ["StraightBevelGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5095": ["StraightBevelGearSetCompoundModalAnalysisAtAStiffness"],
        "_5096": ["StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness"],
        "_5097": ["StraightBevelSunGearCompoundModalAnalysisAtAStiffness"],
        "_5098": ["SynchroniserCompoundModalAnalysisAtAStiffness"],
        "_5099": ["SynchroniserHalfCompoundModalAnalysisAtAStiffness"],
        "_5100": ["SynchroniserPartCompoundModalAnalysisAtAStiffness"],
        "_5101": ["SynchroniserSleeveCompoundModalAnalysisAtAStiffness"],
        "_5102": ["TorqueConverterCompoundModalAnalysisAtAStiffness"],
        "_5103": ["TorqueConverterConnectionCompoundModalAnalysisAtAStiffness"],
        "_5104": ["TorqueConverterPumpCompoundModalAnalysisAtAStiffness"],
        "_5105": ["TorqueConverterTurbineCompoundModalAnalysisAtAStiffness"],
        "_5106": ["UnbalancedMassCompoundModalAnalysisAtAStiffness"],
        "_5107": ["VirtualComponentCompoundModalAnalysisAtAStiffness"],
        "_5108": ["WormGearCompoundModalAnalysisAtAStiffness"],
        "_5109": ["WormGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5110": ["WormGearSetCompoundModalAnalysisAtAStiffness"],
        "_5111": ["ZerolBevelGearCompoundModalAnalysisAtAStiffness"],
        "_5112": ["ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5113": ["ZerolBevelGearSetCompoundModalAnalysisAtAStiffness"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundModalAnalysisAtAStiffness",
    "AbstractShaftCompoundModalAnalysisAtAStiffness",
    "AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness",
    "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
    "AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness",
    "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness",
    "AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness",
    "AssemblyCompoundModalAnalysisAtAStiffness",
    "BearingCompoundModalAnalysisAtAStiffness",
    "BeltConnectionCompoundModalAnalysisAtAStiffness",
    "BeltDriveCompoundModalAnalysisAtAStiffness",
    "BevelDifferentialGearCompoundModalAnalysisAtAStiffness",
    "BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness",
    "BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness",
    "BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness",
    "BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness",
    "BevelGearCompoundModalAnalysisAtAStiffness",
    "BevelGearMeshCompoundModalAnalysisAtAStiffness",
    "BevelGearSetCompoundModalAnalysisAtAStiffness",
    "BoltCompoundModalAnalysisAtAStiffness",
    "BoltedJointCompoundModalAnalysisAtAStiffness",
    "ClutchCompoundModalAnalysisAtAStiffness",
    "ClutchConnectionCompoundModalAnalysisAtAStiffness",
    "ClutchHalfCompoundModalAnalysisAtAStiffness",
    "CoaxialConnectionCompoundModalAnalysisAtAStiffness",
    "ComponentCompoundModalAnalysisAtAStiffness",
    "ConceptCouplingCompoundModalAnalysisAtAStiffness",
    "ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness",
    "ConceptCouplingHalfCompoundModalAnalysisAtAStiffness",
    "ConceptGearCompoundModalAnalysisAtAStiffness",
    "ConceptGearMeshCompoundModalAnalysisAtAStiffness",
    "ConceptGearSetCompoundModalAnalysisAtAStiffness",
    "ConicalGearCompoundModalAnalysisAtAStiffness",
    "ConicalGearMeshCompoundModalAnalysisAtAStiffness",
    "ConicalGearSetCompoundModalAnalysisAtAStiffness",
    "ConnectionCompoundModalAnalysisAtAStiffness",
    "ConnectorCompoundModalAnalysisAtAStiffness",
    "CouplingCompoundModalAnalysisAtAStiffness",
    "CouplingConnectionCompoundModalAnalysisAtAStiffness",
    "CouplingHalfCompoundModalAnalysisAtAStiffness",
    "CVTBeltConnectionCompoundModalAnalysisAtAStiffness",
    "CVTCompoundModalAnalysisAtAStiffness",
    "CVTPulleyCompoundModalAnalysisAtAStiffness",
    "CycloidalAssemblyCompoundModalAnalysisAtAStiffness",
    "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness",
    "CycloidalDiscCompoundModalAnalysisAtAStiffness",
    "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness",
    "CylindricalGearCompoundModalAnalysisAtAStiffness",
    "CylindricalGearMeshCompoundModalAnalysisAtAStiffness",
    "CylindricalGearSetCompoundModalAnalysisAtAStiffness",
    "CylindricalPlanetGearCompoundModalAnalysisAtAStiffness",
    "DatumCompoundModalAnalysisAtAStiffness",
    "ExternalCADModelCompoundModalAnalysisAtAStiffness",
    "FaceGearCompoundModalAnalysisAtAStiffness",
    "FaceGearMeshCompoundModalAnalysisAtAStiffness",
    "FaceGearSetCompoundModalAnalysisAtAStiffness",
    "FEPartCompoundModalAnalysisAtAStiffness",
    "FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness",
    "GearCompoundModalAnalysisAtAStiffness",
    "GearMeshCompoundModalAnalysisAtAStiffness",
    "GearSetCompoundModalAnalysisAtAStiffness",
    "GuideDxfModelCompoundModalAnalysisAtAStiffness",
    "HypoidGearCompoundModalAnalysisAtAStiffness",
    "HypoidGearMeshCompoundModalAnalysisAtAStiffness",
    "HypoidGearSetCompoundModalAnalysisAtAStiffness",
    "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness",
    "MassDiscCompoundModalAnalysisAtAStiffness",
    "MeasurementComponentCompoundModalAnalysisAtAStiffness",
    "MountableComponentCompoundModalAnalysisAtAStiffness",
    "OilSealCompoundModalAnalysisAtAStiffness",
    "PartCompoundModalAnalysisAtAStiffness",
    "PartToPartShearCouplingCompoundModalAnalysisAtAStiffness",
    "PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness",
    "PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness",
    "PlanetaryConnectionCompoundModalAnalysisAtAStiffness",
    "PlanetaryGearSetCompoundModalAnalysisAtAStiffness",
    "PlanetCarrierCompoundModalAnalysisAtAStiffness",
    "PointLoadCompoundModalAnalysisAtAStiffness",
    "PowerLoadCompoundModalAnalysisAtAStiffness",
    "PulleyCompoundModalAnalysisAtAStiffness",
    "RingPinsCompoundModalAnalysisAtAStiffness",
    "RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness",
    "RollingRingAssemblyCompoundModalAnalysisAtAStiffness",
    "RollingRingCompoundModalAnalysisAtAStiffness",
    "RollingRingConnectionCompoundModalAnalysisAtAStiffness",
    "RootAssemblyCompoundModalAnalysisAtAStiffness",
    "ShaftCompoundModalAnalysisAtAStiffness",
    "ShaftHubConnectionCompoundModalAnalysisAtAStiffness",
    "ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
    "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
    "SpiralBevelGearCompoundModalAnalysisAtAStiffness",
    "SpiralBevelGearMeshCompoundModalAnalysisAtAStiffness",
    "SpiralBevelGearSetCompoundModalAnalysisAtAStiffness",
    "SpringDamperCompoundModalAnalysisAtAStiffness",
    "SpringDamperConnectionCompoundModalAnalysisAtAStiffness",
    "SpringDamperHalfCompoundModalAnalysisAtAStiffness",
    "StraightBevelDiffGearCompoundModalAnalysisAtAStiffness",
    "StraightBevelDiffGearMeshCompoundModalAnalysisAtAStiffness",
    "StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness",
    "StraightBevelGearCompoundModalAnalysisAtAStiffness",
    "StraightBevelGearMeshCompoundModalAnalysisAtAStiffness",
    "StraightBevelGearSetCompoundModalAnalysisAtAStiffness",
    "StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness",
    "StraightBevelSunGearCompoundModalAnalysisAtAStiffness",
    "SynchroniserCompoundModalAnalysisAtAStiffness",
    "SynchroniserHalfCompoundModalAnalysisAtAStiffness",
    "SynchroniserPartCompoundModalAnalysisAtAStiffness",
    "SynchroniserSleeveCompoundModalAnalysisAtAStiffness",
    "TorqueConverterCompoundModalAnalysisAtAStiffness",
    "TorqueConverterConnectionCompoundModalAnalysisAtAStiffness",
    "TorqueConverterPumpCompoundModalAnalysisAtAStiffness",
    "TorqueConverterTurbineCompoundModalAnalysisAtAStiffness",
    "UnbalancedMassCompoundModalAnalysisAtAStiffness",
    "VirtualComponentCompoundModalAnalysisAtAStiffness",
    "WormGearCompoundModalAnalysisAtAStiffness",
    "WormGearMeshCompoundModalAnalysisAtAStiffness",
    "WormGearSetCompoundModalAnalysisAtAStiffness",
    "ZerolBevelGearCompoundModalAnalysisAtAStiffness",
    "ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness",
    "ZerolBevelGearSetCompoundModalAnalysisAtAStiffness",
)
