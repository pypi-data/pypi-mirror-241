"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7138 import AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7139 import AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7140 import (
        AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7141 import (
        AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7142 import (
        AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7143 import (
        AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7144 import (
        AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7145 import AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7146 import BearingCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7147 import BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7148 import BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7149 import (
        BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7150 import (
        BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7151 import (
        BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7152 import (
        BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7153 import (
        BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7154 import BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7155 import BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7156 import BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7157 import BoltCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7158 import BoltedJointCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7159 import ClutchCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7160 import ClutchConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7161 import ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7162 import (
        CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7163 import ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7164 import ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7165 import (
        ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7166 import (
        ConceptCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7167 import ConceptGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7168 import ConceptGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7169 import ConceptGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7170 import ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7171 import ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7172 import ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7173 import ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7174 import ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7175 import CouplingCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7176 import (
        CouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7177 import CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7178 import (
        CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7179 import CVTCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7180 import CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7181 import (
        CycloidalAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7182 import (
        CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7183 import CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7184 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7185 import CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7186 import (
        CylindricalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7187 import (
        CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7188 import (
        CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7189 import DatumCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7190 import ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7191 import FaceGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7192 import FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7193 import FaceGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7194 import FEPartCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7195 import (
        FlexiblePinAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7196 import GearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7197 import GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7198 import GearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7199 import GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7200 import HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7201 import HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7202 import HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7203 import (
        InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7204 import (
        KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7205 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7206 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7207 import (
        KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7208 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7209 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7210 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7211 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7212 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7213 import MassDiscCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7214 import (
        MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7215 import (
        MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7216 import OilSealCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7217 import PartCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7218 import (
        PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7219 import (
        PartToPartShearCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7220 import (
        PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7221 import (
        PlanetaryConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7222 import PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7223 import PlanetCarrierCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7224 import PointLoadCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7225 import PowerLoadCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7226 import PulleyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7227 import RingPinsCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7228 import (
        RingPinsToDiscConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7229 import (
        RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7230 import RollingRingCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7231 import (
        RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7232 import RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7233 import ShaftCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7234 import (
        ShaftHubConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7235 import (
        ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7236 import (
        SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7237 import SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7238 import (
        SpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7239 import (
        SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7240 import SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7241 import (
        SpringDamperConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7242 import SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7243 import (
        StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7244 import (
        StraightBevelDiffGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7245 import (
        StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7246 import (
        StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7247 import (
        StraightBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7248 import (
        StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7249 import (
        StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7250 import (
        StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7251 import SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7252 import SynchroniserHalfCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7253 import SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7254 import (
        SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7255 import TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7256 import (
        TorqueConverterConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7257 import (
        TorqueConverterPumpCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7258 import (
        TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7259 import UnbalancedMassCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7260 import VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7261 import WormGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7262 import WormGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7263 import WormGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7264 import ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7265 import (
        ZerolBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7266 import (
        ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
else:
    import_structure = {
        "_7138": ["AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7139": ["AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7140": [
            "AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7141": [
            "AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7142": [
            "AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7143": [
            "AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7144": [
            "AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7145": ["AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7146": ["BearingCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7147": ["BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7148": ["BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7149": [
            "BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7150": [
            "BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7151": [
            "BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7152": [
            "BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7153": [
            "BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7154": ["BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7155": ["BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7156": ["BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7157": ["BoltCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7158": ["BoltedJointCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7159": ["ClutchCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7160": ["ClutchConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7161": ["ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7162": ["CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7163": ["ComponentCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7164": ["ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7165": [
            "ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7166": [
            "ConceptCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7167": ["ConceptGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7168": ["ConceptGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7169": ["ConceptGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7170": ["ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7171": ["ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7172": ["ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7173": ["ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7174": ["ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7175": ["CouplingCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7176": [
            "CouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7177": ["CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7178": ["CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7179": ["CVTCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7180": ["CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7181": ["CycloidalAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7182": [
            "CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7183": ["CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7184": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7185": ["CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7186": [
            "CylindricalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7187": [
            "CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7188": [
            "CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7189": ["DatumCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7190": ["ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7191": ["FaceGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7192": ["FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7193": ["FaceGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7194": ["FEPartCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7195": [
            "FlexiblePinAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7196": ["GearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7197": ["GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7198": ["GearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7199": ["GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7200": ["HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7201": ["HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7202": ["HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7203": [
            "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7204": [
            "KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7205": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7206": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7207": [
            "KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7208": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7209": [
            "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7210": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7211": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7212": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7213": ["MassDiscCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7214": [
            "MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7215": [
            "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7216": ["OilSealCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7217": ["PartCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7218": [
            "PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7219": [
            "PartToPartShearCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7220": [
            "PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7221": [
            "PlanetaryConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7222": ["PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7223": ["PlanetCarrierCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7224": ["PointLoadCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7225": ["PowerLoadCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7226": ["PulleyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7227": ["RingPinsCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7228": [
            "RingPinsToDiscConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7229": [
            "RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7230": ["RollingRingCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7231": [
            "RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7232": ["RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7233": ["ShaftCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7234": [
            "ShaftHubConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7235": [
            "ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7236": [
            "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7237": ["SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7238": [
            "SpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7239": [
            "SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7240": ["SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7241": [
            "SpringDamperConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7242": ["SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7243": [
            "StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7244": [
            "StraightBevelDiffGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7245": [
            "StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7246": ["StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7247": [
            "StraightBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7248": [
            "StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7249": [
            "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7250": [
            "StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7251": ["SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7252": ["SynchroniserHalfCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7253": ["SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7254": [
            "SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7255": ["TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7256": [
            "TorqueConverterConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7257": [
            "TorqueConverterPumpCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7258": [
            "TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7259": ["UnbalancedMassCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7260": ["VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7261": ["WormGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7262": ["WormGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7263": ["WormGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7264": ["ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7265": [
            "ZerolBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7266": ["ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BearingCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BoltCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BoltedJointCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ClutchCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ClutchConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConceptCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConceptGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConceptGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConceptGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CVTCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "DatumCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation",
    "FaceGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "FaceGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "FEPartCompoundAdvancedTimeSteppingAnalysisForModulation",
    "FlexiblePinAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "GearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "GearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation",
    "HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "MassDiscCompoundAdvancedTimeSteppingAnalysisForModulation",
    "MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
    "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
    "OilSealCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PartCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PartToPartShearCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PlanetaryConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PlanetCarrierCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PointLoadCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PowerLoadCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PulleyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "RingPinsCompoundAdvancedTimeSteppingAnalysisForModulation",
    "RingPinsToDiscConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "RollingRingCompoundAdvancedTimeSteppingAnalysisForModulation",
    "RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ShaftCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ShaftHubConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpringDamperConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelDiffGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterPumpCompoundAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation",
    "UnbalancedMassCompoundAdvancedTimeSteppingAnalysisForModulation",
    "VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
    "WormGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "WormGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "WormGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ZerolBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
)
