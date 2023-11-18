"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7003 import AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7004 import AbstractShaftAdvancedTimeSteppingAnalysisForModulation
    from ._7005 import AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation
    from ._7006 import (
        AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7007 import AdvancedTimeSteppingAnalysisForModulation
    from ._7008 import AtsamExcitationsOrOthers
    from ._7009 import AtsamNaturalFrequencyViewOption
    from ._7010 import AdvancedTimeSteppingAnalysisForModulationOptions
    from ._7011 import AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation
    from ._7012 import (
        AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7013 import (
        AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7014 import AssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7015 import ATSAMResultsVsLargeTimeStepSettings
    from ._7016 import BearingAdvancedTimeSteppingAnalysisForModulation
    from ._7017 import BeltConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7018 import BeltDriveAdvancedTimeSteppingAnalysisForModulation
    from ._7019 import BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation
    from ._7020 import (
        BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7021 import BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7022 import (
        BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7023 import BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation
    from ._7024 import BevelGearAdvancedTimeSteppingAnalysisForModulation
    from ._7025 import BevelGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7026 import BevelGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7027 import BoltAdvancedTimeSteppingAnalysisForModulation
    from ._7028 import BoltedJointAdvancedTimeSteppingAnalysisForModulation
    from ._7029 import ClutchAdvancedTimeSteppingAnalysisForModulation
    from ._7030 import ClutchConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7031 import ClutchHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7032 import CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7033 import ComponentAdvancedTimeSteppingAnalysisForModulation
    from ._7034 import ConceptCouplingAdvancedTimeSteppingAnalysisForModulation
    from ._7035 import (
        ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7036 import ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7037 import ConceptGearAdvancedTimeSteppingAnalysisForModulation
    from ._7038 import ConceptGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7039 import ConceptGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7040 import ConicalGearAdvancedTimeSteppingAnalysisForModulation
    from ._7041 import ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7042 import ConicalGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7043 import ConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7044 import ConnectorAdvancedTimeSteppingAnalysisForModulation
    from ._7045 import CouplingAdvancedTimeSteppingAnalysisForModulation
    from ._7046 import CouplingConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7047 import CouplingHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7048 import CVTAdvancedTimeSteppingAnalysisForModulation
    from ._7049 import CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7050 import CVTPulleyAdvancedTimeSteppingAnalysisForModulation
    from ._7051 import CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7052 import CycloidalDiscAdvancedTimeSteppingAnalysisForModulation
    from ._7053 import (
        CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7054 import (
        CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7055 import CylindricalGearAdvancedTimeSteppingAnalysisForModulation
    from ._7056 import CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7057 import CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7058 import CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation
    from ._7059 import DatumAdvancedTimeSteppingAnalysisForModulation
    from ._7060 import ExternalCADModelAdvancedTimeSteppingAnalysisForModulation
    from ._7061 import FaceGearAdvancedTimeSteppingAnalysisForModulation
    from ._7062 import FaceGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7063 import FaceGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7064 import FEPartAdvancedTimeSteppingAnalysisForModulation
    from ._7065 import FlexiblePinAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7066 import GearAdvancedTimeSteppingAnalysisForModulation
    from ._7067 import GearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7068 import GearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7069 import GuideDxfModelAdvancedTimeSteppingAnalysisForModulation
    from ._7070 import (
        HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7071 import HypoidGearAdvancedTimeSteppingAnalysisForModulation
    from ._7072 import HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7073 import HypoidGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7074 import (
        InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7075 import (
        KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7076 import (
        KlingelnbergCycloPalloidConicalGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7077 import (
        KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7078 import (
        KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7079 import (
        KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7080 import (
        KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7081 import (
        KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7082 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7083 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7084 import MassDiscAdvancedTimeSteppingAnalysisForModulation
    from ._7085 import MeasurementComponentAdvancedTimeSteppingAnalysisForModulation
    from ._7086 import MountableComponentAdvancedTimeSteppingAnalysisForModulation
    from ._7087 import OilSealAdvancedTimeSteppingAnalysisForModulation
    from ._7088 import PartAdvancedTimeSteppingAnalysisForModulation
    from ._7089 import PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation
    from ._7090 import (
        PartToPartShearCouplingConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7091 import (
        PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7092 import PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7093 import PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7094 import PlanetCarrierAdvancedTimeSteppingAnalysisForModulation
    from ._7095 import PointLoadAdvancedTimeSteppingAnalysisForModulation
    from ._7096 import PowerLoadAdvancedTimeSteppingAnalysisForModulation
    from ._7097 import PulleyAdvancedTimeSteppingAnalysisForModulation
    from ._7098 import RingPinsAdvancedTimeSteppingAnalysisForModulation
    from ._7099 import RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7100 import RollingRingAdvancedTimeSteppingAnalysisForModulation
    from ._7101 import RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7102 import RollingRingConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7103 import RootAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7104 import ShaftAdvancedTimeSteppingAnalysisForModulation
    from ._7105 import ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7106 import (
        ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7107 import SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7108 import SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation
    from ._7109 import SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7110 import SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7111 import SpringDamperAdvancedTimeSteppingAnalysisForModulation
    from ._7112 import SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7113 import SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7114 import StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation
    from ._7115 import (
        StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7116 import StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7117 import StraightBevelGearAdvancedTimeSteppingAnalysisForModulation
    from ._7118 import StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7119 import StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7120 import StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation
    from ._7121 import StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation
    from ._7122 import SynchroniserAdvancedTimeSteppingAnalysisForModulation
    from ._7123 import SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7124 import SynchroniserPartAdvancedTimeSteppingAnalysisForModulation
    from ._7125 import SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation
    from ._7126 import TorqueConverterAdvancedTimeSteppingAnalysisForModulation
    from ._7127 import (
        TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7128 import TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation
    from ._7129 import TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation
    from ._7130 import UnbalancedMassAdvancedTimeSteppingAnalysisForModulation
    from ._7131 import VirtualComponentAdvancedTimeSteppingAnalysisForModulation
    from ._7132 import WormGearAdvancedTimeSteppingAnalysisForModulation
    from ._7133 import WormGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7134 import WormGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7135 import ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation
    from ._7136 import ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7137 import ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation
else:
    import_structure = {
        "_7003": ["AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7004": ["AbstractShaftAdvancedTimeSteppingAnalysisForModulation"],
        "_7005": ["AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation"],
        "_7006": [
            "AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7007": ["AdvancedTimeSteppingAnalysisForModulation"],
        "_7008": ["AtsamExcitationsOrOthers"],
        "_7009": ["AtsamNaturalFrequencyViewOption"],
        "_7010": ["AdvancedTimeSteppingAnalysisForModulationOptions"],
        "_7011": ["AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7012": [
            "AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7013": ["AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7014": ["AssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7015": ["ATSAMResultsVsLargeTimeStepSettings"],
        "_7016": ["BearingAdvancedTimeSteppingAnalysisForModulation"],
        "_7017": ["BeltConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7018": ["BeltDriveAdvancedTimeSteppingAnalysisForModulation"],
        "_7019": ["BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7020": ["BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7021": ["BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7022": [
            "BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7023": ["BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7024": ["BevelGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7025": ["BevelGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7026": ["BevelGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7027": ["BoltAdvancedTimeSteppingAnalysisForModulation"],
        "_7028": ["BoltedJointAdvancedTimeSteppingAnalysisForModulation"],
        "_7029": ["ClutchAdvancedTimeSteppingAnalysisForModulation"],
        "_7030": ["ClutchConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7031": ["ClutchHalfAdvancedTimeSteppingAnalysisForModulation"],
        "_7032": ["CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7033": ["ComponentAdvancedTimeSteppingAnalysisForModulation"],
        "_7034": ["ConceptCouplingAdvancedTimeSteppingAnalysisForModulation"],
        "_7035": ["ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7036": ["ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation"],
        "_7037": ["ConceptGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7038": ["ConceptGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7039": ["ConceptGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7040": ["ConicalGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7041": ["ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7042": ["ConicalGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7043": ["ConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7044": ["ConnectorAdvancedTimeSteppingAnalysisForModulation"],
        "_7045": ["CouplingAdvancedTimeSteppingAnalysisForModulation"],
        "_7046": ["CouplingConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7047": ["CouplingHalfAdvancedTimeSteppingAnalysisForModulation"],
        "_7048": ["CVTAdvancedTimeSteppingAnalysisForModulation"],
        "_7049": ["CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7050": ["CVTPulleyAdvancedTimeSteppingAnalysisForModulation"],
        "_7051": ["CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7052": ["CycloidalDiscAdvancedTimeSteppingAnalysisForModulation"],
        "_7053": [
            "CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7054": [
            "CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7055": ["CylindricalGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7056": ["CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7057": ["CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7058": ["CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7059": ["DatumAdvancedTimeSteppingAnalysisForModulation"],
        "_7060": ["ExternalCADModelAdvancedTimeSteppingAnalysisForModulation"],
        "_7061": ["FaceGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7062": ["FaceGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7063": ["FaceGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7064": ["FEPartAdvancedTimeSteppingAnalysisForModulation"],
        "_7065": ["FlexiblePinAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7066": ["GearAdvancedTimeSteppingAnalysisForModulation"],
        "_7067": ["GearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7068": ["GearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7069": ["GuideDxfModelAdvancedTimeSteppingAnalysisForModulation"],
        "_7070": [
            "HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7071": ["HypoidGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7072": ["HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7073": ["HypoidGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7074": [
            "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7075": [
            "KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7076": [
            "KlingelnbergCycloPalloidConicalGearMeshAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7077": [
            "KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7078": [
            "KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7079": [
            "KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7080": [
            "KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7081": [
            "KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7082": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7083": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7084": ["MassDiscAdvancedTimeSteppingAnalysisForModulation"],
        "_7085": ["MeasurementComponentAdvancedTimeSteppingAnalysisForModulation"],
        "_7086": ["MountableComponentAdvancedTimeSteppingAnalysisForModulation"],
        "_7087": ["OilSealAdvancedTimeSteppingAnalysisForModulation"],
        "_7088": ["PartAdvancedTimeSteppingAnalysisForModulation"],
        "_7089": ["PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation"],
        "_7090": [
            "PartToPartShearCouplingConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7091": [
            "PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7092": ["PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7093": ["PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7094": ["PlanetCarrierAdvancedTimeSteppingAnalysisForModulation"],
        "_7095": ["PointLoadAdvancedTimeSteppingAnalysisForModulation"],
        "_7096": ["PowerLoadAdvancedTimeSteppingAnalysisForModulation"],
        "_7097": ["PulleyAdvancedTimeSteppingAnalysisForModulation"],
        "_7098": ["RingPinsAdvancedTimeSteppingAnalysisForModulation"],
        "_7099": ["RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7100": ["RollingRingAdvancedTimeSteppingAnalysisForModulation"],
        "_7101": ["RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7102": ["RollingRingConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7103": ["RootAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7104": ["ShaftAdvancedTimeSteppingAnalysisForModulation"],
        "_7105": ["ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7106": [
            "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7107": ["SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7108": ["SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7109": ["SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7110": ["SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7111": ["SpringDamperAdvancedTimeSteppingAnalysisForModulation"],
        "_7112": ["SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7113": ["SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation"],
        "_7114": ["StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7115": ["StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7116": ["StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7117": ["StraightBevelGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7118": ["StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7119": ["StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7120": ["StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7121": ["StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7122": ["SynchroniserAdvancedTimeSteppingAnalysisForModulation"],
        "_7123": ["SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation"],
        "_7124": ["SynchroniserPartAdvancedTimeSteppingAnalysisForModulation"],
        "_7125": ["SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation"],
        "_7126": ["TorqueConverterAdvancedTimeSteppingAnalysisForModulation"],
        "_7127": ["TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7128": ["TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation"],
        "_7129": ["TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation"],
        "_7130": ["UnbalancedMassAdvancedTimeSteppingAnalysisForModulation"],
        "_7131": ["VirtualComponentAdvancedTimeSteppingAnalysisForModulation"],
        "_7132": ["WormGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7133": ["WormGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7134": ["WormGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7135": ["ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7136": ["ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7137": ["ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
    "AbstractShaftAdvancedTimeSteppingAnalysisForModulation",
    "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",
    "AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
    "AdvancedTimeSteppingAnalysisForModulation",
    "AtsamExcitationsOrOthers",
    "AtsamNaturalFrequencyViewOption",
    "AdvancedTimeSteppingAnalysisForModulationOptions",
    "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
    "AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
    "AssemblyAdvancedTimeSteppingAnalysisForModulation",
    "ATSAMResultsVsLargeTimeStepSettings",
    "BearingAdvancedTimeSteppingAnalysisForModulation",
    "BeltConnectionAdvancedTimeSteppingAnalysisForModulation",
    "BeltDriveAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
    "BevelGearAdvancedTimeSteppingAnalysisForModulation",
    "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "BevelGearSetAdvancedTimeSteppingAnalysisForModulation",
    "BoltAdvancedTimeSteppingAnalysisForModulation",
    "BoltedJointAdvancedTimeSteppingAnalysisForModulation",
    "ClutchAdvancedTimeSteppingAnalysisForModulation",
    "ClutchConnectionAdvancedTimeSteppingAnalysisForModulation",
    "ClutchHalfAdvancedTimeSteppingAnalysisForModulation",
    "CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation",
    "ComponentAdvancedTimeSteppingAnalysisForModulation",
    "ConceptCouplingAdvancedTimeSteppingAnalysisForModulation",
    "ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation",
    "ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation",
    "ConceptGearAdvancedTimeSteppingAnalysisForModulation",
    "ConceptGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "ConceptGearSetAdvancedTimeSteppingAnalysisForModulation",
    "ConicalGearAdvancedTimeSteppingAnalysisForModulation",
    "ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
    "ConnectionAdvancedTimeSteppingAnalysisForModulation",
    "ConnectorAdvancedTimeSteppingAnalysisForModulation",
    "CouplingAdvancedTimeSteppingAnalysisForModulation",
    "CouplingConnectionAdvancedTimeSteppingAnalysisForModulation",
    "CouplingHalfAdvancedTimeSteppingAnalysisForModulation",
    "CVTAdvancedTimeSteppingAnalysisForModulation",
    "CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation",
    "CVTPulleyAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalDiscAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalGearAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation",
    "DatumAdvancedTimeSteppingAnalysisForModulation",
    "ExternalCADModelAdvancedTimeSteppingAnalysisForModulation",
    "FaceGearAdvancedTimeSteppingAnalysisForModulation",
    "FaceGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "FaceGearSetAdvancedTimeSteppingAnalysisForModulation",
    "FEPartAdvancedTimeSteppingAnalysisForModulation",
    "FlexiblePinAssemblyAdvancedTimeSteppingAnalysisForModulation",
    "GearAdvancedTimeSteppingAnalysisForModulation",
    "GearMeshAdvancedTimeSteppingAnalysisForModulation",
    "GearSetAdvancedTimeSteppingAnalysisForModulation",
    "GuideDxfModelAdvancedTimeSteppingAnalysisForModulation",
    "HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation",
    "HypoidGearAdvancedTimeSteppingAnalysisForModulation",
    "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "HypoidGearSetAdvancedTimeSteppingAnalysisForModulation",
    "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidConicalGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
    "MassDiscAdvancedTimeSteppingAnalysisForModulation",
    "MeasurementComponentAdvancedTimeSteppingAnalysisForModulation",
    "MountableComponentAdvancedTimeSteppingAnalysisForModulation",
    "OilSealAdvancedTimeSteppingAnalysisForModulation",
    "PartAdvancedTimeSteppingAnalysisForModulation",
    "PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation",
    "PartToPartShearCouplingConnectionAdvancedTimeSteppingAnalysisForModulation",
    "PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation",
    "PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation",
    "PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation",
    "PlanetCarrierAdvancedTimeSteppingAnalysisForModulation",
    "PointLoadAdvancedTimeSteppingAnalysisForModulation",
    "PowerLoadAdvancedTimeSteppingAnalysisForModulation",
    "PulleyAdvancedTimeSteppingAnalysisForModulation",
    "RingPinsAdvancedTimeSteppingAnalysisForModulation",
    "RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation",
    "RollingRingAdvancedTimeSteppingAnalysisForModulation",
    "RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation",
    "RollingRingConnectionAdvancedTimeSteppingAnalysisForModulation",
    "RootAssemblyAdvancedTimeSteppingAnalysisForModulation",
    "ShaftAdvancedTimeSteppingAnalysisForModulation",
    "ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation",
    "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
    "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
    "SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation",
    "SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
    "SpringDamperAdvancedTimeSteppingAnalysisForModulation",
    "SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation",
    "SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelGearAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserPartAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation",
    "UnbalancedMassAdvancedTimeSteppingAnalysisForModulation",
    "VirtualComponentAdvancedTimeSteppingAnalysisForModulation",
    "WormGearAdvancedTimeSteppingAnalysisForModulation",
    "WormGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "WormGearSetAdvancedTimeSteppingAnalysisForModulation",
    "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
    "ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
)
