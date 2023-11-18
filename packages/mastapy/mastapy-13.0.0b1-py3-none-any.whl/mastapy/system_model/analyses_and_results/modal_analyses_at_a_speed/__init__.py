"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5114 import AbstractAssemblyModalAnalysisAtASpeed
    from ._5115 import AbstractShaftModalAnalysisAtASpeed
    from ._5116 import AbstractShaftOrHousingModalAnalysisAtASpeed
    from ._5117 import AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed
    from ._5118 import AGMAGleasonConicalGearMeshModalAnalysisAtASpeed
    from ._5119 import AGMAGleasonConicalGearModalAnalysisAtASpeed
    from ._5120 import AGMAGleasonConicalGearSetModalAnalysisAtASpeed
    from ._5121 import AssemblyModalAnalysisAtASpeed
    from ._5122 import BearingModalAnalysisAtASpeed
    from ._5123 import BeltConnectionModalAnalysisAtASpeed
    from ._5124 import BeltDriveModalAnalysisAtASpeed
    from ._5125 import BevelDifferentialGearMeshModalAnalysisAtASpeed
    from ._5126 import BevelDifferentialGearModalAnalysisAtASpeed
    from ._5127 import BevelDifferentialGearSetModalAnalysisAtASpeed
    from ._5128 import BevelDifferentialPlanetGearModalAnalysisAtASpeed
    from ._5129 import BevelDifferentialSunGearModalAnalysisAtASpeed
    from ._5130 import BevelGearMeshModalAnalysisAtASpeed
    from ._5131 import BevelGearModalAnalysisAtASpeed
    from ._5132 import BevelGearSetModalAnalysisAtASpeed
    from ._5133 import BoltedJointModalAnalysisAtASpeed
    from ._5134 import BoltModalAnalysisAtASpeed
    from ._5135 import ClutchConnectionModalAnalysisAtASpeed
    from ._5136 import ClutchHalfModalAnalysisAtASpeed
    from ._5137 import ClutchModalAnalysisAtASpeed
    from ._5138 import CoaxialConnectionModalAnalysisAtASpeed
    from ._5139 import ComponentModalAnalysisAtASpeed
    from ._5140 import ConceptCouplingConnectionModalAnalysisAtASpeed
    from ._5141 import ConceptCouplingHalfModalAnalysisAtASpeed
    from ._5142 import ConceptCouplingModalAnalysisAtASpeed
    from ._5143 import ConceptGearMeshModalAnalysisAtASpeed
    from ._5144 import ConceptGearModalAnalysisAtASpeed
    from ._5145 import ConceptGearSetModalAnalysisAtASpeed
    from ._5146 import ConicalGearMeshModalAnalysisAtASpeed
    from ._5147 import ConicalGearModalAnalysisAtASpeed
    from ._5148 import ConicalGearSetModalAnalysisAtASpeed
    from ._5149 import ConnectionModalAnalysisAtASpeed
    from ._5150 import ConnectorModalAnalysisAtASpeed
    from ._5151 import CouplingConnectionModalAnalysisAtASpeed
    from ._5152 import CouplingHalfModalAnalysisAtASpeed
    from ._5153 import CouplingModalAnalysisAtASpeed
    from ._5154 import CVTBeltConnectionModalAnalysisAtASpeed
    from ._5155 import CVTModalAnalysisAtASpeed
    from ._5156 import CVTPulleyModalAnalysisAtASpeed
    from ._5157 import CycloidalAssemblyModalAnalysisAtASpeed
    from ._5158 import CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed
    from ._5159 import CycloidalDiscModalAnalysisAtASpeed
    from ._5160 import CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed
    from ._5161 import CylindricalGearMeshModalAnalysisAtASpeed
    from ._5162 import CylindricalGearModalAnalysisAtASpeed
    from ._5163 import CylindricalGearSetModalAnalysisAtASpeed
    from ._5164 import CylindricalPlanetGearModalAnalysisAtASpeed
    from ._5165 import DatumModalAnalysisAtASpeed
    from ._5166 import ExternalCADModelModalAnalysisAtASpeed
    from ._5167 import FaceGearMeshModalAnalysisAtASpeed
    from ._5168 import FaceGearModalAnalysisAtASpeed
    from ._5169 import FaceGearSetModalAnalysisAtASpeed
    from ._5170 import FEPartModalAnalysisAtASpeed
    from ._5171 import FlexiblePinAssemblyModalAnalysisAtASpeed
    from ._5172 import GearMeshModalAnalysisAtASpeed
    from ._5173 import GearModalAnalysisAtASpeed
    from ._5174 import GearSetModalAnalysisAtASpeed
    from ._5175 import GuideDxfModelModalAnalysisAtASpeed
    from ._5176 import HypoidGearMeshModalAnalysisAtASpeed
    from ._5177 import HypoidGearModalAnalysisAtASpeed
    from ._5178 import HypoidGearSetModalAnalysisAtASpeed
    from ._5179 import InterMountableComponentConnectionModalAnalysisAtASpeed
    from ._5180 import KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed
    from ._5181 import KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed
    from ._5182 import KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed
    from ._5183 import KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed
    from ._5184 import KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed
    from ._5185 import KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed
    from ._5186 import KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed
    from ._5187 import KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed
    from ._5188 import KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed
    from ._5189 import MassDiscModalAnalysisAtASpeed
    from ._5190 import MeasurementComponentModalAnalysisAtASpeed
    from ._5191 import ModalAnalysisAtASpeed
    from ._5192 import MountableComponentModalAnalysisAtASpeed
    from ._5193 import OilSealModalAnalysisAtASpeed
    from ._5194 import PartModalAnalysisAtASpeed
    from ._5195 import PartToPartShearCouplingConnectionModalAnalysisAtASpeed
    from ._5196 import PartToPartShearCouplingHalfModalAnalysisAtASpeed
    from ._5197 import PartToPartShearCouplingModalAnalysisAtASpeed
    from ._5198 import PlanetaryConnectionModalAnalysisAtASpeed
    from ._5199 import PlanetaryGearSetModalAnalysisAtASpeed
    from ._5200 import PlanetCarrierModalAnalysisAtASpeed
    from ._5201 import PointLoadModalAnalysisAtASpeed
    from ._5202 import PowerLoadModalAnalysisAtASpeed
    from ._5203 import PulleyModalAnalysisAtASpeed
    from ._5204 import RingPinsModalAnalysisAtASpeed
    from ._5205 import RingPinsToDiscConnectionModalAnalysisAtASpeed
    from ._5206 import RollingRingAssemblyModalAnalysisAtASpeed
    from ._5207 import RollingRingConnectionModalAnalysisAtASpeed
    from ._5208 import RollingRingModalAnalysisAtASpeed
    from ._5209 import RootAssemblyModalAnalysisAtASpeed
    from ._5210 import ShaftHubConnectionModalAnalysisAtASpeed
    from ._5211 import ShaftModalAnalysisAtASpeed
    from ._5212 import ShaftToMountableComponentConnectionModalAnalysisAtASpeed
    from ._5213 import SpecialisedAssemblyModalAnalysisAtASpeed
    from ._5214 import SpiralBevelGearMeshModalAnalysisAtASpeed
    from ._5215 import SpiralBevelGearModalAnalysisAtASpeed
    from ._5216 import SpiralBevelGearSetModalAnalysisAtASpeed
    from ._5217 import SpringDamperConnectionModalAnalysisAtASpeed
    from ._5218 import SpringDamperHalfModalAnalysisAtASpeed
    from ._5219 import SpringDamperModalAnalysisAtASpeed
    from ._5220 import StraightBevelDiffGearMeshModalAnalysisAtASpeed
    from ._5221 import StraightBevelDiffGearModalAnalysisAtASpeed
    from ._5222 import StraightBevelDiffGearSetModalAnalysisAtASpeed
    from ._5223 import StraightBevelGearMeshModalAnalysisAtASpeed
    from ._5224 import StraightBevelGearModalAnalysisAtASpeed
    from ._5225 import StraightBevelGearSetModalAnalysisAtASpeed
    from ._5226 import StraightBevelPlanetGearModalAnalysisAtASpeed
    from ._5227 import StraightBevelSunGearModalAnalysisAtASpeed
    from ._5228 import SynchroniserHalfModalAnalysisAtASpeed
    from ._5229 import SynchroniserModalAnalysisAtASpeed
    from ._5230 import SynchroniserPartModalAnalysisAtASpeed
    from ._5231 import SynchroniserSleeveModalAnalysisAtASpeed
    from ._5232 import TorqueConverterConnectionModalAnalysisAtASpeed
    from ._5233 import TorqueConverterModalAnalysisAtASpeed
    from ._5234 import TorqueConverterPumpModalAnalysisAtASpeed
    from ._5235 import TorqueConverterTurbineModalAnalysisAtASpeed
    from ._5236 import UnbalancedMassModalAnalysisAtASpeed
    from ._5237 import VirtualComponentModalAnalysisAtASpeed
    from ._5238 import WormGearMeshModalAnalysisAtASpeed
    from ._5239 import WormGearModalAnalysisAtASpeed
    from ._5240 import WormGearSetModalAnalysisAtASpeed
    from ._5241 import ZerolBevelGearMeshModalAnalysisAtASpeed
    from ._5242 import ZerolBevelGearModalAnalysisAtASpeed
    from ._5243 import ZerolBevelGearSetModalAnalysisAtASpeed
else:
    import_structure = {
        "_5114": ["AbstractAssemblyModalAnalysisAtASpeed"],
        "_5115": ["AbstractShaftModalAnalysisAtASpeed"],
        "_5116": ["AbstractShaftOrHousingModalAnalysisAtASpeed"],
        "_5117": ["AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed"],
        "_5118": ["AGMAGleasonConicalGearMeshModalAnalysisAtASpeed"],
        "_5119": ["AGMAGleasonConicalGearModalAnalysisAtASpeed"],
        "_5120": ["AGMAGleasonConicalGearSetModalAnalysisAtASpeed"],
        "_5121": ["AssemblyModalAnalysisAtASpeed"],
        "_5122": ["BearingModalAnalysisAtASpeed"],
        "_5123": ["BeltConnectionModalAnalysisAtASpeed"],
        "_5124": ["BeltDriveModalAnalysisAtASpeed"],
        "_5125": ["BevelDifferentialGearMeshModalAnalysisAtASpeed"],
        "_5126": ["BevelDifferentialGearModalAnalysisAtASpeed"],
        "_5127": ["BevelDifferentialGearSetModalAnalysisAtASpeed"],
        "_5128": ["BevelDifferentialPlanetGearModalAnalysisAtASpeed"],
        "_5129": ["BevelDifferentialSunGearModalAnalysisAtASpeed"],
        "_5130": ["BevelGearMeshModalAnalysisAtASpeed"],
        "_5131": ["BevelGearModalAnalysisAtASpeed"],
        "_5132": ["BevelGearSetModalAnalysisAtASpeed"],
        "_5133": ["BoltedJointModalAnalysisAtASpeed"],
        "_5134": ["BoltModalAnalysisAtASpeed"],
        "_5135": ["ClutchConnectionModalAnalysisAtASpeed"],
        "_5136": ["ClutchHalfModalAnalysisAtASpeed"],
        "_5137": ["ClutchModalAnalysisAtASpeed"],
        "_5138": ["CoaxialConnectionModalAnalysisAtASpeed"],
        "_5139": ["ComponentModalAnalysisAtASpeed"],
        "_5140": ["ConceptCouplingConnectionModalAnalysisAtASpeed"],
        "_5141": ["ConceptCouplingHalfModalAnalysisAtASpeed"],
        "_5142": ["ConceptCouplingModalAnalysisAtASpeed"],
        "_5143": ["ConceptGearMeshModalAnalysisAtASpeed"],
        "_5144": ["ConceptGearModalAnalysisAtASpeed"],
        "_5145": ["ConceptGearSetModalAnalysisAtASpeed"],
        "_5146": ["ConicalGearMeshModalAnalysisAtASpeed"],
        "_5147": ["ConicalGearModalAnalysisAtASpeed"],
        "_5148": ["ConicalGearSetModalAnalysisAtASpeed"],
        "_5149": ["ConnectionModalAnalysisAtASpeed"],
        "_5150": ["ConnectorModalAnalysisAtASpeed"],
        "_5151": ["CouplingConnectionModalAnalysisAtASpeed"],
        "_5152": ["CouplingHalfModalAnalysisAtASpeed"],
        "_5153": ["CouplingModalAnalysisAtASpeed"],
        "_5154": ["CVTBeltConnectionModalAnalysisAtASpeed"],
        "_5155": ["CVTModalAnalysisAtASpeed"],
        "_5156": ["CVTPulleyModalAnalysisAtASpeed"],
        "_5157": ["CycloidalAssemblyModalAnalysisAtASpeed"],
        "_5158": ["CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed"],
        "_5159": ["CycloidalDiscModalAnalysisAtASpeed"],
        "_5160": ["CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed"],
        "_5161": ["CylindricalGearMeshModalAnalysisAtASpeed"],
        "_5162": ["CylindricalGearModalAnalysisAtASpeed"],
        "_5163": ["CylindricalGearSetModalAnalysisAtASpeed"],
        "_5164": ["CylindricalPlanetGearModalAnalysisAtASpeed"],
        "_5165": ["DatumModalAnalysisAtASpeed"],
        "_5166": ["ExternalCADModelModalAnalysisAtASpeed"],
        "_5167": ["FaceGearMeshModalAnalysisAtASpeed"],
        "_5168": ["FaceGearModalAnalysisAtASpeed"],
        "_5169": ["FaceGearSetModalAnalysisAtASpeed"],
        "_5170": ["FEPartModalAnalysisAtASpeed"],
        "_5171": ["FlexiblePinAssemblyModalAnalysisAtASpeed"],
        "_5172": ["GearMeshModalAnalysisAtASpeed"],
        "_5173": ["GearModalAnalysisAtASpeed"],
        "_5174": ["GearSetModalAnalysisAtASpeed"],
        "_5175": ["GuideDxfModelModalAnalysisAtASpeed"],
        "_5176": ["HypoidGearMeshModalAnalysisAtASpeed"],
        "_5177": ["HypoidGearModalAnalysisAtASpeed"],
        "_5178": ["HypoidGearSetModalAnalysisAtASpeed"],
        "_5179": ["InterMountableComponentConnectionModalAnalysisAtASpeed"],
        "_5180": ["KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed"],
        "_5181": ["KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed"],
        "_5182": ["KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed"],
        "_5183": ["KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed"],
        "_5184": ["KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed"],
        "_5185": ["KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed"],
        "_5186": ["KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed"],
        "_5187": ["KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed"],
        "_5188": ["KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed"],
        "_5189": ["MassDiscModalAnalysisAtASpeed"],
        "_5190": ["MeasurementComponentModalAnalysisAtASpeed"],
        "_5191": ["ModalAnalysisAtASpeed"],
        "_5192": ["MountableComponentModalAnalysisAtASpeed"],
        "_5193": ["OilSealModalAnalysisAtASpeed"],
        "_5194": ["PartModalAnalysisAtASpeed"],
        "_5195": ["PartToPartShearCouplingConnectionModalAnalysisAtASpeed"],
        "_5196": ["PartToPartShearCouplingHalfModalAnalysisAtASpeed"],
        "_5197": ["PartToPartShearCouplingModalAnalysisAtASpeed"],
        "_5198": ["PlanetaryConnectionModalAnalysisAtASpeed"],
        "_5199": ["PlanetaryGearSetModalAnalysisAtASpeed"],
        "_5200": ["PlanetCarrierModalAnalysisAtASpeed"],
        "_5201": ["PointLoadModalAnalysisAtASpeed"],
        "_5202": ["PowerLoadModalAnalysisAtASpeed"],
        "_5203": ["PulleyModalAnalysisAtASpeed"],
        "_5204": ["RingPinsModalAnalysisAtASpeed"],
        "_5205": ["RingPinsToDiscConnectionModalAnalysisAtASpeed"],
        "_5206": ["RollingRingAssemblyModalAnalysisAtASpeed"],
        "_5207": ["RollingRingConnectionModalAnalysisAtASpeed"],
        "_5208": ["RollingRingModalAnalysisAtASpeed"],
        "_5209": ["RootAssemblyModalAnalysisAtASpeed"],
        "_5210": ["ShaftHubConnectionModalAnalysisAtASpeed"],
        "_5211": ["ShaftModalAnalysisAtASpeed"],
        "_5212": ["ShaftToMountableComponentConnectionModalAnalysisAtASpeed"],
        "_5213": ["SpecialisedAssemblyModalAnalysisAtASpeed"],
        "_5214": ["SpiralBevelGearMeshModalAnalysisAtASpeed"],
        "_5215": ["SpiralBevelGearModalAnalysisAtASpeed"],
        "_5216": ["SpiralBevelGearSetModalAnalysisAtASpeed"],
        "_5217": ["SpringDamperConnectionModalAnalysisAtASpeed"],
        "_5218": ["SpringDamperHalfModalAnalysisAtASpeed"],
        "_5219": ["SpringDamperModalAnalysisAtASpeed"],
        "_5220": ["StraightBevelDiffGearMeshModalAnalysisAtASpeed"],
        "_5221": ["StraightBevelDiffGearModalAnalysisAtASpeed"],
        "_5222": ["StraightBevelDiffGearSetModalAnalysisAtASpeed"],
        "_5223": ["StraightBevelGearMeshModalAnalysisAtASpeed"],
        "_5224": ["StraightBevelGearModalAnalysisAtASpeed"],
        "_5225": ["StraightBevelGearSetModalAnalysisAtASpeed"],
        "_5226": ["StraightBevelPlanetGearModalAnalysisAtASpeed"],
        "_5227": ["StraightBevelSunGearModalAnalysisAtASpeed"],
        "_5228": ["SynchroniserHalfModalAnalysisAtASpeed"],
        "_5229": ["SynchroniserModalAnalysisAtASpeed"],
        "_5230": ["SynchroniserPartModalAnalysisAtASpeed"],
        "_5231": ["SynchroniserSleeveModalAnalysisAtASpeed"],
        "_5232": ["TorqueConverterConnectionModalAnalysisAtASpeed"],
        "_5233": ["TorqueConverterModalAnalysisAtASpeed"],
        "_5234": ["TorqueConverterPumpModalAnalysisAtASpeed"],
        "_5235": ["TorqueConverterTurbineModalAnalysisAtASpeed"],
        "_5236": ["UnbalancedMassModalAnalysisAtASpeed"],
        "_5237": ["VirtualComponentModalAnalysisAtASpeed"],
        "_5238": ["WormGearMeshModalAnalysisAtASpeed"],
        "_5239": ["WormGearModalAnalysisAtASpeed"],
        "_5240": ["WormGearSetModalAnalysisAtASpeed"],
        "_5241": ["ZerolBevelGearMeshModalAnalysisAtASpeed"],
        "_5242": ["ZerolBevelGearModalAnalysisAtASpeed"],
        "_5243": ["ZerolBevelGearSetModalAnalysisAtASpeed"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyModalAnalysisAtASpeed",
    "AbstractShaftModalAnalysisAtASpeed",
    "AbstractShaftOrHousingModalAnalysisAtASpeed",
    "AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed",
    "AGMAGleasonConicalGearMeshModalAnalysisAtASpeed",
    "AGMAGleasonConicalGearModalAnalysisAtASpeed",
    "AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
    "AssemblyModalAnalysisAtASpeed",
    "BearingModalAnalysisAtASpeed",
    "BeltConnectionModalAnalysisAtASpeed",
    "BeltDriveModalAnalysisAtASpeed",
    "BevelDifferentialGearMeshModalAnalysisAtASpeed",
    "BevelDifferentialGearModalAnalysisAtASpeed",
    "BevelDifferentialGearSetModalAnalysisAtASpeed",
    "BevelDifferentialPlanetGearModalAnalysisAtASpeed",
    "BevelDifferentialSunGearModalAnalysisAtASpeed",
    "BevelGearMeshModalAnalysisAtASpeed",
    "BevelGearModalAnalysisAtASpeed",
    "BevelGearSetModalAnalysisAtASpeed",
    "BoltedJointModalAnalysisAtASpeed",
    "BoltModalAnalysisAtASpeed",
    "ClutchConnectionModalAnalysisAtASpeed",
    "ClutchHalfModalAnalysisAtASpeed",
    "ClutchModalAnalysisAtASpeed",
    "CoaxialConnectionModalAnalysisAtASpeed",
    "ComponentModalAnalysisAtASpeed",
    "ConceptCouplingConnectionModalAnalysisAtASpeed",
    "ConceptCouplingHalfModalAnalysisAtASpeed",
    "ConceptCouplingModalAnalysisAtASpeed",
    "ConceptGearMeshModalAnalysisAtASpeed",
    "ConceptGearModalAnalysisAtASpeed",
    "ConceptGearSetModalAnalysisAtASpeed",
    "ConicalGearMeshModalAnalysisAtASpeed",
    "ConicalGearModalAnalysisAtASpeed",
    "ConicalGearSetModalAnalysisAtASpeed",
    "ConnectionModalAnalysisAtASpeed",
    "ConnectorModalAnalysisAtASpeed",
    "CouplingConnectionModalAnalysisAtASpeed",
    "CouplingHalfModalAnalysisAtASpeed",
    "CouplingModalAnalysisAtASpeed",
    "CVTBeltConnectionModalAnalysisAtASpeed",
    "CVTModalAnalysisAtASpeed",
    "CVTPulleyModalAnalysisAtASpeed",
    "CycloidalAssemblyModalAnalysisAtASpeed",
    "CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed",
    "CycloidalDiscModalAnalysisAtASpeed",
    "CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed",
    "CylindricalGearMeshModalAnalysisAtASpeed",
    "CylindricalGearModalAnalysisAtASpeed",
    "CylindricalGearSetModalAnalysisAtASpeed",
    "CylindricalPlanetGearModalAnalysisAtASpeed",
    "DatumModalAnalysisAtASpeed",
    "ExternalCADModelModalAnalysisAtASpeed",
    "FaceGearMeshModalAnalysisAtASpeed",
    "FaceGearModalAnalysisAtASpeed",
    "FaceGearSetModalAnalysisAtASpeed",
    "FEPartModalAnalysisAtASpeed",
    "FlexiblePinAssemblyModalAnalysisAtASpeed",
    "GearMeshModalAnalysisAtASpeed",
    "GearModalAnalysisAtASpeed",
    "GearSetModalAnalysisAtASpeed",
    "GuideDxfModelModalAnalysisAtASpeed",
    "HypoidGearMeshModalAnalysisAtASpeed",
    "HypoidGearModalAnalysisAtASpeed",
    "HypoidGearSetModalAnalysisAtASpeed",
    "InterMountableComponentConnectionModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed",
    "MassDiscModalAnalysisAtASpeed",
    "MeasurementComponentModalAnalysisAtASpeed",
    "ModalAnalysisAtASpeed",
    "MountableComponentModalAnalysisAtASpeed",
    "OilSealModalAnalysisAtASpeed",
    "PartModalAnalysisAtASpeed",
    "PartToPartShearCouplingConnectionModalAnalysisAtASpeed",
    "PartToPartShearCouplingHalfModalAnalysisAtASpeed",
    "PartToPartShearCouplingModalAnalysisAtASpeed",
    "PlanetaryConnectionModalAnalysisAtASpeed",
    "PlanetaryGearSetModalAnalysisAtASpeed",
    "PlanetCarrierModalAnalysisAtASpeed",
    "PointLoadModalAnalysisAtASpeed",
    "PowerLoadModalAnalysisAtASpeed",
    "PulleyModalAnalysisAtASpeed",
    "RingPinsModalAnalysisAtASpeed",
    "RingPinsToDiscConnectionModalAnalysisAtASpeed",
    "RollingRingAssemblyModalAnalysisAtASpeed",
    "RollingRingConnectionModalAnalysisAtASpeed",
    "RollingRingModalAnalysisAtASpeed",
    "RootAssemblyModalAnalysisAtASpeed",
    "ShaftHubConnectionModalAnalysisAtASpeed",
    "ShaftModalAnalysisAtASpeed",
    "ShaftToMountableComponentConnectionModalAnalysisAtASpeed",
    "SpecialisedAssemblyModalAnalysisAtASpeed",
    "SpiralBevelGearMeshModalAnalysisAtASpeed",
    "SpiralBevelGearModalAnalysisAtASpeed",
    "SpiralBevelGearSetModalAnalysisAtASpeed",
    "SpringDamperConnectionModalAnalysisAtASpeed",
    "SpringDamperHalfModalAnalysisAtASpeed",
    "SpringDamperModalAnalysisAtASpeed",
    "StraightBevelDiffGearMeshModalAnalysisAtASpeed",
    "StraightBevelDiffGearModalAnalysisAtASpeed",
    "StraightBevelDiffGearSetModalAnalysisAtASpeed",
    "StraightBevelGearMeshModalAnalysisAtASpeed",
    "StraightBevelGearModalAnalysisAtASpeed",
    "StraightBevelGearSetModalAnalysisAtASpeed",
    "StraightBevelPlanetGearModalAnalysisAtASpeed",
    "StraightBevelSunGearModalAnalysisAtASpeed",
    "SynchroniserHalfModalAnalysisAtASpeed",
    "SynchroniserModalAnalysisAtASpeed",
    "SynchroniserPartModalAnalysisAtASpeed",
    "SynchroniserSleeveModalAnalysisAtASpeed",
    "TorqueConverterConnectionModalAnalysisAtASpeed",
    "TorqueConverterModalAnalysisAtASpeed",
    "TorqueConverterPumpModalAnalysisAtASpeed",
    "TorqueConverterTurbineModalAnalysisAtASpeed",
    "UnbalancedMassModalAnalysisAtASpeed",
    "VirtualComponentModalAnalysisAtASpeed",
    "WormGearMeshModalAnalysisAtASpeed",
    "WormGearModalAnalysisAtASpeed",
    "WormGearSetModalAnalysisAtASpeed",
    "ZerolBevelGearMeshModalAnalysisAtASpeed",
    "ZerolBevelGearModalAnalysisAtASpeed",
    "ZerolBevelGearSetModalAnalysisAtASpeed",
)
