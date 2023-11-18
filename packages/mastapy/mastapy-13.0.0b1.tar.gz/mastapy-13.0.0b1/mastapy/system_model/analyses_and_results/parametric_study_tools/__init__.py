"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4293 import AbstractAssemblyParametricStudyTool
    from ._4294 import AbstractShaftOrHousingParametricStudyTool
    from ._4295 import AbstractShaftParametricStudyTool
    from ._4296 import AbstractShaftToMountableComponentConnectionParametricStudyTool
    from ._4297 import AGMAGleasonConicalGearMeshParametricStudyTool
    from ._4298 import AGMAGleasonConicalGearParametricStudyTool
    from ._4299 import AGMAGleasonConicalGearSetParametricStudyTool
    from ._4300 import AssemblyParametricStudyTool
    from ._4301 import BearingParametricStudyTool
    from ._4302 import BeltConnectionParametricStudyTool
    from ._4303 import BeltDriveParametricStudyTool
    from ._4304 import BevelDifferentialGearMeshParametricStudyTool
    from ._4305 import BevelDifferentialGearParametricStudyTool
    from ._4306 import BevelDifferentialGearSetParametricStudyTool
    from ._4307 import BevelDifferentialPlanetGearParametricStudyTool
    from ._4308 import BevelDifferentialSunGearParametricStudyTool
    from ._4309 import BevelGearMeshParametricStudyTool
    from ._4310 import BevelGearParametricStudyTool
    from ._4311 import BevelGearSetParametricStudyTool
    from ._4312 import BoltedJointParametricStudyTool
    from ._4313 import BoltParametricStudyTool
    from ._4314 import ClutchConnectionParametricStudyTool
    from ._4315 import ClutchHalfParametricStudyTool
    from ._4316 import ClutchParametricStudyTool
    from ._4317 import CoaxialConnectionParametricStudyTool
    from ._4318 import ComponentParametricStudyTool
    from ._4319 import ConceptCouplingConnectionParametricStudyTool
    from ._4320 import ConceptCouplingHalfParametricStudyTool
    from ._4321 import ConceptCouplingParametricStudyTool
    from ._4322 import ConceptGearMeshParametricStudyTool
    from ._4323 import ConceptGearParametricStudyTool
    from ._4324 import ConceptGearSetParametricStudyTool
    from ._4325 import ConicalGearMeshParametricStudyTool
    from ._4326 import ConicalGearParametricStudyTool
    from ._4327 import ConicalGearSetParametricStudyTool
    from ._4328 import ConnectionParametricStudyTool
    from ._4329 import ConnectorParametricStudyTool
    from ._4330 import CouplingConnectionParametricStudyTool
    from ._4331 import CouplingHalfParametricStudyTool
    from ._4332 import CouplingParametricStudyTool
    from ._4333 import CVTBeltConnectionParametricStudyTool
    from ._4334 import CVTParametricStudyTool
    from ._4335 import CVTPulleyParametricStudyTool
    from ._4336 import CycloidalAssemblyParametricStudyTool
    from ._4337 import CycloidalDiscCentralBearingConnectionParametricStudyTool
    from ._4338 import CycloidalDiscParametricStudyTool
    from ._4339 import CycloidalDiscPlanetaryBearingConnectionParametricStudyTool
    from ._4340 import CylindricalGearMeshParametricStudyTool
    from ._4341 import CylindricalGearParametricStudyTool
    from ._4342 import CylindricalGearSetParametricStudyTool
    from ._4343 import CylindricalPlanetGearParametricStudyTool
    from ._4344 import DatumParametricStudyTool
    from ._4345 import DesignOfExperimentsVariableSetter
    from ._4346 import DoeValueSpecificationOption
    from ._4347 import DutyCycleResultsForAllComponents
    from ._4348 import DutyCycleResultsForAllGearSets
    from ._4349 import DutyCycleResultsForRootAssembly
    from ._4350 import DutyCycleResultsForSingleBearing
    from ._4351 import DutyCycleResultsForSingleShaft
    from ._4352 import ExternalCADModelParametricStudyTool
    from ._4353 import FaceGearMeshParametricStudyTool
    from ._4354 import FaceGearParametricStudyTool
    from ._4355 import FaceGearSetParametricStudyTool
    from ._4356 import FEPartParametricStudyTool
    from ._4357 import FlexiblePinAssemblyParametricStudyTool
    from ._4358 import GearMeshParametricStudyTool
    from ._4359 import GearParametricStudyTool
    from ._4360 import GearSetParametricStudyTool
    from ._4361 import GuideDxfModelParametricStudyTool
    from ._4362 import HypoidGearMeshParametricStudyTool
    from ._4363 import HypoidGearParametricStudyTool
    from ._4364 import HypoidGearSetParametricStudyTool
    from ._4365 import InterMountableComponentConnectionParametricStudyTool
    from ._4366 import KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool
    from ._4367 import KlingelnbergCycloPalloidConicalGearParametricStudyTool
    from ._4368 import KlingelnbergCycloPalloidConicalGearSetParametricStudyTool
    from ._4369 import KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool
    from ._4370 import KlingelnbergCycloPalloidHypoidGearParametricStudyTool
    from ._4371 import KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool
    from ._4372 import KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool
    from ._4373 import KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool
    from ._4374 import KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool
    from ._4375 import MassDiscParametricStudyTool
    from ._4376 import MeasurementComponentParametricStudyTool
    from ._4377 import MonteCarloDistribution
    from ._4378 import MountableComponentParametricStudyTool
    from ._4379 import OilSealParametricStudyTool
    from ._4380 import ParametricStudyDimension
    from ._4381 import ParametricStudyDOEResultVariable
    from ._4382 import ParametricStudyDOEResultVariableForParallelCoordinatesPlot
    from ._4383 import ParametricStudyHistogram
    from ._4384 import ParametricStudyStaticLoad
    from ._4385 import ParametricStudyTool
    from ._4386 import ParametricStudyToolOptions
    from ._4387 import ParametricStudyToolResultsForReporting
    from ._4388 import ParametricStudyToolStepResult
    from ._4389 import ParametricStudyVariable
    from ._4390 import PartParametricStudyTool
    from ._4391 import PartToPartShearCouplingConnectionParametricStudyTool
    from ._4392 import PartToPartShearCouplingHalfParametricStudyTool
    from ._4393 import PartToPartShearCouplingParametricStudyTool
    from ._4394 import PlanetaryConnectionParametricStudyTool
    from ._4395 import PlanetaryGearSetParametricStudyTool
    from ._4396 import PlanetCarrierParametricStudyTool
    from ._4397 import PointLoadParametricStudyTool
    from ._4398 import PowerLoadParametricStudyTool
    from ._4399 import PulleyParametricStudyTool
    from ._4400 import RingPinsParametricStudyTool
    from ._4401 import RingPinsToDiscConnectionParametricStudyTool
    from ._4402 import RollingRingAssemblyParametricStudyTool
    from ._4403 import RollingRingConnectionParametricStudyTool
    from ._4404 import RollingRingParametricStudyTool
    from ._4405 import RootAssemblyParametricStudyTool
    from ._4406 import ShaftHubConnectionParametricStudyTool
    from ._4407 import ShaftParametricStudyTool
    from ._4408 import ShaftToMountableComponentConnectionParametricStudyTool
    from ._4409 import SpecialisedAssemblyParametricStudyTool
    from ._4410 import SpiralBevelGearMeshParametricStudyTool
    from ._4411 import SpiralBevelGearParametricStudyTool
    from ._4412 import SpiralBevelGearSetParametricStudyTool
    from ._4413 import SpringDamperConnectionParametricStudyTool
    from ._4414 import SpringDamperHalfParametricStudyTool
    from ._4415 import SpringDamperParametricStudyTool
    from ._4416 import StraightBevelDiffGearMeshParametricStudyTool
    from ._4417 import StraightBevelDiffGearParametricStudyTool
    from ._4418 import StraightBevelDiffGearSetParametricStudyTool
    from ._4419 import StraightBevelGearMeshParametricStudyTool
    from ._4420 import StraightBevelGearParametricStudyTool
    from ._4421 import StraightBevelGearSetParametricStudyTool
    from ._4422 import StraightBevelPlanetGearParametricStudyTool
    from ._4423 import StraightBevelSunGearParametricStudyTool
    from ._4424 import SynchroniserHalfParametricStudyTool
    from ._4425 import SynchroniserParametricStudyTool
    from ._4426 import SynchroniserPartParametricStudyTool
    from ._4427 import SynchroniserSleeveParametricStudyTool
    from ._4428 import TorqueConverterConnectionParametricStudyTool
    from ._4429 import TorqueConverterParametricStudyTool
    from ._4430 import TorqueConverterPumpParametricStudyTool
    from ._4431 import TorqueConverterTurbineParametricStudyTool
    from ._4432 import UnbalancedMassParametricStudyTool
    from ._4433 import VirtualComponentParametricStudyTool
    from ._4434 import WormGearMeshParametricStudyTool
    from ._4435 import WormGearParametricStudyTool
    from ._4436 import WormGearSetParametricStudyTool
    from ._4437 import ZerolBevelGearMeshParametricStudyTool
    from ._4438 import ZerolBevelGearParametricStudyTool
    from ._4439 import ZerolBevelGearSetParametricStudyTool
else:
    import_structure = {
        "_4293": ["AbstractAssemblyParametricStudyTool"],
        "_4294": ["AbstractShaftOrHousingParametricStudyTool"],
        "_4295": ["AbstractShaftParametricStudyTool"],
        "_4296": ["AbstractShaftToMountableComponentConnectionParametricStudyTool"],
        "_4297": ["AGMAGleasonConicalGearMeshParametricStudyTool"],
        "_4298": ["AGMAGleasonConicalGearParametricStudyTool"],
        "_4299": ["AGMAGleasonConicalGearSetParametricStudyTool"],
        "_4300": ["AssemblyParametricStudyTool"],
        "_4301": ["BearingParametricStudyTool"],
        "_4302": ["BeltConnectionParametricStudyTool"],
        "_4303": ["BeltDriveParametricStudyTool"],
        "_4304": ["BevelDifferentialGearMeshParametricStudyTool"],
        "_4305": ["BevelDifferentialGearParametricStudyTool"],
        "_4306": ["BevelDifferentialGearSetParametricStudyTool"],
        "_4307": ["BevelDifferentialPlanetGearParametricStudyTool"],
        "_4308": ["BevelDifferentialSunGearParametricStudyTool"],
        "_4309": ["BevelGearMeshParametricStudyTool"],
        "_4310": ["BevelGearParametricStudyTool"],
        "_4311": ["BevelGearSetParametricStudyTool"],
        "_4312": ["BoltedJointParametricStudyTool"],
        "_4313": ["BoltParametricStudyTool"],
        "_4314": ["ClutchConnectionParametricStudyTool"],
        "_4315": ["ClutchHalfParametricStudyTool"],
        "_4316": ["ClutchParametricStudyTool"],
        "_4317": ["CoaxialConnectionParametricStudyTool"],
        "_4318": ["ComponentParametricStudyTool"],
        "_4319": ["ConceptCouplingConnectionParametricStudyTool"],
        "_4320": ["ConceptCouplingHalfParametricStudyTool"],
        "_4321": ["ConceptCouplingParametricStudyTool"],
        "_4322": ["ConceptGearMeshParametricStudyTool"],
        "_4323": ["ConceptGearParametricStudyTool"],
        "_4324": ["ConceptGearSetParametricStudyTool"],
        "_4325": ["ConicalGearMeshParametricStudyTool"],
        "_4326": ["ConicalGearParametricStudyTool"],
        "_4327": ["ConicalGearSetParametricStudyTool"],
        "_4328": ["ConnectionParametricStudyTool"],
        "_4329": ["ConnectorParametricStudyTool"],
        "_4330": ["CouplingConnectionParametricStudyTool"],
        "_4331": ["CouplingHalfParametricStudyTool"],
        "_4332": ["CouplingParametricStudyTool"],
        "_4333": ["CVTBeltConnectionParametricStudyTool"],
        "_4334": ["CVTParametricStudyTool"],
        "_4335": ["CVTPulleyParametricStudyTool"],
        "_4336": ["CycloidalAssemblyParametricStudyTool"],
        "_4337": ["CycloidalDiscCentralBearingConnectionParametricStudyTool"],
        "_4338": ["CycloidalDiscParametricStudyTool"],
        "_4339": ["CycloidalDiscPlanetaryBearingConnectionParametricStudyTool"],
        "_4340": ["CylindricalGearMeshParametricStudyTool"],
        "_4341": ["CylindricalGearParametricStudyTool"],
        "_4342": ["CylindricalGearSetParametricStudyTool"],
        "_4343": ["CylindricalPlanetGearParametricStudyTool"],
        "_4344": ["DatumParametricStudyTool"],
        "_4345": ["DesignOfExperimentsVariableSetter"],
        "_4346": ["DoeValueSpecificationOption"],
        "_4347": ["DutyCycleResultsForAllComponents"],
        "_4348": ["DutyCycleResultsForAllGearSets"],
        "_4349": ["DutyCycleResultsForRootAssembly"],
        "_4350": ["DutyCycleResultsForSingleBearing"],
        "_4351": ["DutyCycleResultsForSingleShaft"],
        "_4352": ["ExternalCADModelParametricStudyTool"],
        "_4353": ["FaceGearMeshParametricStudyTool"],
        "_4354": ["FaceGearParametricStudyTool"],
        "_4355": ["FaceGearSetParametricStudyTool"],
        "_4356": ["FEPartParametricStudyTool"],
        "_4357": ["FlexiblePinAssemblyParametricStudyTool"],
        "_4358": ["GearMeshParametricStudyTool"],
        "_4359": ["GearParametricStudyTool"],
        "_4360": ["GearSetParametricStudyTool"],
        "_4361": ["GuideDxfModelParametricStudyTool"],
        "_4362": ["HypoidGearMeshParametricStudyTool"],
        "_4363": ["HypoidGearParametricStudyTool"],
        "_4364": ["HypoidGearSetParametricStudyTool"],
        "_4365": ["InterMountableComponentConnectionParametricStudyTool"],
        "_4366": ["KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool"],
        "_4367": ["KlingelnbergCycloPalloidConicalGearParametricStudyTool"],
        "_4368": ["KlingelnbergCycloPalloidConicalGearSetParametricStudyTool"],
        "_4369": ["KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool"],
        "_4370": ["KlingelnbergCycloPalloidHypoidGearParametricStudyTool"],
        "_4371": ["KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool"],
        "_4372": ["KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool"],
        "_4373": ["KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool"],
        "_4374": ["KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool"],
        "_4375": ["MassDiscParametricStudyTool"],
        "_4376": ["MeasurementComponentParametricStudyTool"],
        "_4377": ["MonteCarloDistribution"],
        "_4378": ["MountableComponentParametricStudyTool"],
        "_4379": ["OilSealParametricStudyTool"],
        "_4380": ["ParametricStudyDimension"],
        "_4381": ["ParametricStudyDOEResultVariable"],
        "_4382": ["ParametricStudyDOEResultVariableForParallelCoordinatesPlot"],
        "_4383": ["ParametricStudyHistogram"],
        "_4384": ["ParametricStudyStaticLoad"],
        "_4385": ["ParametricStudyTool"],
        "_4386": ["ParametricStudyToolOptions"],
        "_4387": ["ParametricStudyToolResultsForReporting"],
        "_4388": ["ParametricStudyToolStepResult"],
        "_4389": ["ParametricStudyVariable"],
        "_4390": ["PartParametricStudyTool"],
        "_4391": ["PartToPartShearCouplingConnectionParametricStudyTool"],
        "_4392": ["PartToPartShearCouplingHalfParametricStudyTool"],
        "_4393": ["PartToPartShearCouplingParametricStudyTool"],
        "_4394": ["PlanetaryConnectionParametricStudyTool"],
        "_4395": ["PlanetaryGearSetParametricStudyTool"],
        "_4396": ["PlanetCarrierParametricStudyTool"],
        "_4397": ["PointLoadParametricStudyTool"],
        "_4398": ["PowerLoadParametricStudyTool"],
        "_4399": ["PulleyParametricStudyTool"],
        "_4400": ["RingPinsParametricStudyTool"],
        "_4401": ["RingPinsToDiscConnectionParametricStudyTool"],
        "_4402": ["RollingRingAssemblyParametricStudyTool"],
        "_4403": ["RollingRingConnectionParametricStudyTool"],
        "_4404": ["RollingRingParametricStudyTool"],
        "_4405": ["RootAssemblyParametricStudyTool"],
        "_4406": ["ShaftHubConnectionParametricStudyTool"],
        "_4407": ["ShaftParametricStudyTool"],
        "_4408": ["ShaftToMountableComponentConnectionParametricStudyTool"],
        "_4409": ["SpecialisedAssemblyParametricStudyTool"],
        "_4410": ["SpiralBevelGearMeshParametricStudyTool"],
        "_4411": ["SpiralBevelGearParametricStudyTool"],
        "_4412": ["SpiralBevelGearSetParametricStudyTool"],
        "_4413": ["SpringDamperConnectionParametricStudyTool"],
        "_4414": ["SpringDamperHalfParametricStudyTool"],
        "_4415": ["SpringDamperParametricStudyTool"],
        "_4416": ["StraightBevelDiffGearMeshParametricStudyTool"],
        "_4417": ["StraightBevelDiffGearParametricStudyTool"],
        "_4418": ["StraightBevelDiffGearSetParametricStudyTool"],
        "_4419": ["StraightBevelGearMeshParametricStudyTool"],
        "_4420": ["StraightBevelGearParametricStudyTool"],
        "_4421": ["StraightBevelGearSetParametricStudyTool"],
        "_4422": ["StraightBevelPlanetGearParametricStudyTool"],
        "_4423": ["StraightBevelSunGearParametricStudyTool"],
        "_4424": ["SynchroniserHalfParametricStudyTool"],
        "_4425": ["SynchroniserParametricStudyTool"],
        "_4426": ["SynchroniserPartParametricStudyTool"],
        "_4427": ["SynchroniserSleeveParametricStudyTool"],
        "_4428": ["TorqueConverterConnectionParametricStudyTool"],
        "_4429": ["TorqueConverterParametricStudyTool"],
        "_4430": ["TorqueConverterPumpParametricStudyTool"],
        "_4431": ["TorqueConverterTurbineParametricStudyTool"],
        "_4432": ["UnbalancedMassParametricStudyTool"],
        "_4433": ["VirtualComponentParametricStudyTool"],
        "_4434": ["WormGearMeshParametricStudyTool"],
        "_4435": ["WormGearParametricStudyTool"],
        "_4436": ["WormGearSetParametricStudyTool"],
        "_4437": ["ZerolBevelGearMeshParametricStudyTool"],
        "_4438": ["ZerolBevelGearParametricStudyTool"],
        "_4439": ["ZerolBevelGearSetParametricStudyTool"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyParametricStudyTool",
    "AbstractShaftOrHousingParametricStudyTool",
    "AbstractShaftParametricStudyTool",
    "AbstractShaftToMountableComponentConnectionParametricStudyTool",
    "AGMAGleasonConicalGearMeshParametricStudyTool",
    "AGMAGleasonConicalGearParametricStudyTool",
    "AGMAGleasonConicalGearSetParametricStudyTool",
    "AssemblyParametricStudyTool",
    "BearingParametricStudyTool",
    "BeltConnectionParametricStudyTool",
    "BeltDriveParametricStudyTool",
    "BevelDifferentialGearMeshParametricStudyTool",
    "BevelDifferentialGearParametricStudyTool",
    "BevelDifferentialGearSetParametricStudyTool",
    "BevelDifferentialPlanetGearParametricStudyTool",
    "BevelDifferentialSunGearParametricStudyTool",
    "BevelGearMeshParametricStudyTool",
    "BevelGearParametricStudyTool",
    "BevelGearSetParametricStudyTool",
    "BoltedJointParametricStudyTool",
    "BoltParametricStudyTool",
    "ClutchConnectionParametricStudyTool",
    "ClutchHalfParametricStudyTool",
    "ClutchParametricStudyTool",
    "CoaxialConnectionParametricStudyTool",
    "ComponentParametricStudyTool",
    "ConceptCouplingConnectionParametricStudyTool",
    "ConceptCouplingHalfParametricStudyTool",
    "ConceptCouplingParametricStudyTool",
    "ConceptGearMeshParametricStudyTool",
    "ConceptGearParametricStudyTool",
    "ConceptGearSetParametricStudyTool",
    "ConicalGearMeshParametricStudyTool",
    "ConicalGearParametricStudyTool",
    "ConicalGearSetParametricStudyTool",
    "ConnectionParametricStudyTool",
    "ConnectorParametricStudyTool",
    "CouplingConnectionParametricStudyTool",
    "CouplingHalfParametricStudyTool",
    "CouplingParametricStudyTool",
    "CVTBeltConnectionParametricStudyTool",
    "CVTParametricStudyTool",
    "CVTPulleyParametricStudyTool",
    "CycloidalAssemblyParametricStudyTool",
    "CycloidalDiscCentralBearingConnectionParametricStudyTool",
    "CycloidalDiscParametricStudyTool",
    "CycloidalDiscPlanetaryBearingConnectionParametricStudyTool",
    "CylindricalGearMeshParametricStudyTool",
    "CylindricalGearParametricStudyTool",
    "CylindricalGearSetParametricStudyTool",
    "CylindricalPlanetGearParametricStudyTool",
    "DatumParametricStudyTool",
    "DesignOfExperimentsVariableSetter",
    "DoeValueSpecificationOption",
    "DutyCycleResultsForAllComponents",
    "DutyCycleResultsForAllGearSets",
    "DutyCycleResultsForRootAssembly",
    "DutyCycleResultsForSingleBearing",
    "DutyCycleResultsForSingleShaft",
    "ExternalCADModelParametricStudyTool",
    "FaceGearMeshParametricStudyTool",
    "FaceGearParametricStudyTool",
    "FaceGearSetParametricStudyTool",
    "FEPartParametricStudyTool",
    "FlexiblePinAssemblyParametricStudyTool",
    "GearMeshParametricStudyTool",
    "GearParametricStudyTool",
    "GearSetParametricStudyTool",
    "GuideDxfModelParametricStudyTool",
    "HypoidGearMeshParametricStudyTool",
    "HypoidGearParametricStudyTool",
    "HypoidGearSetParametricStudyTool",
    "InterMountableComponentConnectionParametricStudyTool",
    "KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool",
    "KlingelnbergCycloPalloidConicalGearParametricStudyTool",
    "KlingelnbergCycloPalloidConicalGearSetParametricStudyTool",
    "KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool",
    "KlingelnbergCycloPalloidHypoidGearParametricStudyTool",
    "KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool",
    "KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool",
    "KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool",
    "MassDiscParametricStudyTool",
    "MeasurementComponentParametricStudyTool",
    "MonteCarloDistribution",
    "MountableComponentParametricStudyTool",
    "OilSealParametricStudyTool",
    "ParametricStudyDimension",
    "ParametricStudyDOEResultVariable",
    "ParametricStudyDOEResultVariableForParallelCoordinatesPlot",
    "ParametricStudyHistogram",
    "ParametricStudyStaticLoad",
    "ParametricStudyTool",
    "ParametricStudyToolOptions",
    "ParametricStudyToolResultsForReporting",
    "ParametricStudyToolStepResult",
    "ParametricStudyVariable",
    "PartParametricStudyTool",
    "PartToPartShearCouplingConnectionParametricStudyTool",
    "PartToPartShearCouplingHalfParametricStudyTool",
    "PartToPartShearCouplingParametricStudyTool",
    "PlanetaryConnectionParametricStudyTool",
    "PlanetaryGearSetParametricStudyTool",
    "PlanetCarrierParametricStudyTool",
    "PointLoadParametricStudyTool",
    "PowerLoadParametricStudyTool",
    "PulleyParametricStudyTool",
    "RingPinsParametricStudyTool",
    "RingPinsToDiscConnectionParametricStudyTool",
    "RollingRingAssemblyParametricStudyTool",
    "RollingRingConnectionParametricStudyTool",
    "RollingRingParametricStudyTool",
    "RootAssemblyParametricStudyTool",
    "ShaftHubConnectionParametricStudyTool",
    "ShaftParametricStudyTool",
    "ShaftToMountableComponentConnectionParametricStudyTool",
    "SpecialisedAssemblyParametricStudyTool",
    "SpiralBevelGearMeshParametricStudyTool",
    "SpiralBevelGearParametricStudyTool",
    "SpiralBevelGearSetParametricStudyTool",
    "SpringDamperConnectionParametricStudyTool",
    "SpringDamperHalfParametricStudyTool",
    "SpringDamperParametricStudyTool",
    "StraightBevelDiffGearMeshParametricStudyTool",
    "StraightBevelDiffGearParametricStudyTool",
    "StraightBevelDiffGearSetParametricStudyTool",
    "StraightBevelGearMeshParametricStudyTool",
    "StraightBevelGearParametricStudyTool",
    "StraightBevelGearSetParametricStudyTool",
    "StraightBevelPlanetGearParametricStudyTool",
    "StraightBevelSunGearParametricStudyTool",
    "SynchroniserHalfParametricStudyTool",
    "SynchroniserParametricStudyTool",
    "SynchroniserPartParametricStudyTool",
    "SynchroniserSleeveParametricStudyTool",
    "TorqueConverterConnectionParametricStudyTool",
    "TorqueConverterParametricStudyTool",
    "TorqueConverterPumpParametricStudyTool",
    "TorqueConverterTurbineParametricStudyTool",
    "UnbalancedMassParametricStudyTool",
    "VirtualComponentParametricStudyTool",
    "WormGearMeshParametricStudyTool",
    "WormGearParametricStudyTool",
    "WormGearSetParametricStudyTool",
    "ZerolBevelGearMeshParametricStudyTool",
    "ZerolBevelGearParametricStudyTool",
    "ZerolBevelGearSetParametricStudyTool",
)
