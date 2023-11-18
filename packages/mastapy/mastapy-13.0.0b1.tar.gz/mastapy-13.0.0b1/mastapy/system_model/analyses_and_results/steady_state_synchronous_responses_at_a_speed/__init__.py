"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._3502 import AbstractAssemblySteadyStateSynchronousResponseAtASpeed
    from ._3503 import AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed
    from ._3504 import AbstractShaftSteadyStateSynchronousResponseAtASpeed
    from ._3505 import (
        AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3506 import AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3507 import AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3508 import AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed
    from ._3509 import AssemblySteadyStateSynchronousResponseAtASpeed
    from ._3510 import BearingSteadyStateSynchronousResponseAtASpeed
    from ._3511 import BeltConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3512 import BeltDriveSteadyStateSynchronousResponseAtASpeed
    from ._3513 import BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3514 import BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3515 import BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed
    from ._3516 import BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed
    from ._3517 import BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed
    from ._3518 import BevelGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3519 import BevelGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3520 import BevelGearSteadyStateSynchronousResponseAtASpeed
    from ._3521 import BoltedJointSteadyStateSynchronousResponseAtASpeed
    from ._3522 import BoltSteadyStateSynchronousResponseAtASpeed
    from ._3523 import ClutchConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3524 import ClutchHalfSteadyStateSynchronousResponseAtASpeed
    from ._3525 import ClutchSteadyStateSynchronousResponseAtASpeed
    from ._3526 import CoaxialConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3527 import ComponentSteadyStateSynchronousResponseAtASpeed
    from ._3528 import ConceptCouplingConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3529 import ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed
    from ._3530 import ConceptCouplingSteadyStateSynchronousResponseAtASpeed
    from ._3531 import ConceptGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3532 import ConceptGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3533 import ConceptGearSteadyStateSynchronousResponseAtASpeed
    from ._3534 import ConicalGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3535 import ConicalGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3536 import ConicalGearSteadyStateSynchronousResponseAtASpeed
    from ._3537 import ConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3538 import ConnectorSteadyStateSynchronousResponseAtASpeed
    from ._3539 import CouplingConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3540 import CouplingHalfSteadyStateSynchronousResponseAtASpeed
    from ._3541 import CouplingSteadyStateSynchronousResponseAtASpeed
    from ._3542 import CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3543 import CVTPulleySteadyStateSynchronousResponseAtASpeed
    from ._3544 import CVTSteadyStateSynchronousResponseAtASpeed
    from ._3545 import CycloidalAssemblySteadyStateSynchronousResponseAtASpeed
    from ._3546 import (
        CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3547 import (
        CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3548 import CycloidalDiscSteadyStateSynchronousResponseAtASpeed
    from ._3549 import CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3550 import CylindricalGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3551 import CylindricalGearSteadyStateSynchronousResponseAtASpeed
    from ._3552 import CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed
    from ._3553 import DatumSteadyStateSynchronousResponseAtASpeed
    from ._3554 import ExternalCADModelSteadyStateSynchronousResponseAtASpeed
    from ._3555 import FaceGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3556 import FaceGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3557 import FaceGearSteadyStateSynchronousResponseAtASpeed
    from ._3558 import FEPartSteadyStateSynchronousResponseAtASpeed
    from ._3559 import FlexiblePinAssemblySteadyStateSynchronousResponseAtASpeed
    from ._3560 import GearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3561 import GearSetSteadyStateSynchronousResponseAtASpeed
    from ._3562 import GearSteadyStateSynchronousResponseAtASpeed
    from ._3563 import GuideDxfModelSteadyStateSynchronousResponseAtASpeed
    from ._3564 import HypoidGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3565 import HypoidGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3566 import HypoidGearSteadyStateSynchronousResponseAtASpeed
    from ._3567 import (
        InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3568 import (
        KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3569 import (
        KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3570 import (
        KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3571 import (
        KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3572 import (
        KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3573 import (
        KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3574 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3575 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3576 import (
        KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3577 import MassDiscSteadyStateSynchronousResponseAtASpeed
    from ._3578 import MeasurementComponentSteadyStateSynchronousResponseAtASpeed
    from ._3579 import MountableComponentSteadyStateSynchronousResponseAtASpeed
    from ._3580 import OilSealSteadyStateSynchronousResponseAtASpeed
    from ._3581 import PartSteadyStateSynchronousResponseAtASpeed
    from ._3582 import (
        PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3583 import PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed
    from ._3584 import PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed
    from ._3585 import PlanetaryConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3586 import PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3587 import PlanetCarrierSteadyStateSynchronousResponseAtASpeed
    from ._3588 import PointLoadSteadyStateSynchronousResponseAtASpeed
    from ._3589 import PowerLoadSteadyStateSynchronousResponseAtASpeed
    from ._3590 import PulleySteadyStateSynchronousResponseAtASpeed
    from ._3591 import RingPinsSteadyStateSynchronousResponseAtASpeed
    from ._3592 import RingPinsToDiscConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3593 import RollingRingAssemblySteadyStateSynchronousResponseAtASpeed
    from ._3594 import RollingRingConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3595 import RollingRingSteadyStateSynchronousResponseAtASpeed
    from ._3596 import RootAssemblySteadyStateSynchronousResponseAtASpeed
    from ._3597 import ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3598 import ShaftSteadyStateSynchronousResponseAtASpeed
    from ._3599 import (
        ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3600 import SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed
    from ._3601 import SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3602 import SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3603 import SpiralBevelGearSteadyStateSynchronousResponseAtASpeed
    from ._3604 import SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3605 import SpringDamperHalfSteadyStateSynchronousResponseAtASpeed
    from ._3606 import SpringDamperSteadyStateSynchronousResponseAtASpeed
    from ._3607 import SteadyStateSynchronousResponseAtASpeed
    from ._3608 import StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3609 import StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3610 import StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed
    from ._3611 import StraightBevelGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3612 import StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3613 import StraightBevelGearSteadyStateSynchronousResponseAtASpeed
    from ._3614 import StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed
    from ._3615 import StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed
    from ._3616 import SynchroniserHalfSteadyStateSynchronousResponseAtASpeed
    from ._3617 import SynchroniserPartSteadyStateSynchronousResponseAtASpeed
    from ._3618 import SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed
    from ._3619 import SynchroniserSteadyStateSynchronousResponseAtASpeed
    from ._3620 import TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3621 import TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed
    from ._3622 import TorqueConverterSteadyStateSynchronousResponseAtASpeed
    from ._3623 import TorqueConverterTurbineSteadyStateSynchronousResponseAtASpeed
    from ._3624 import UnbalancedMassSteadyStateSynchronousResponseAtASpeed
    from ._3625 import VirtualComponentSteadyStateSynchronousResponseAtASpeed
    from ._3626 import WormGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3627 import WormGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3628 import WormGearSteadyStateSynchronousResponseAtASpeed
    from ._3629 import ZerolBevelGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3630 import ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3631 import ZerolBevelGearSteadyStateSynchronousResponseAtASpeed
else:
    import_structure = {
        "_3502": ["AbstractAssemblySteadyStateSynchronousResponseAtASpeed"],
        "_3503": ["AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed"],
        "_3504": ["AbstractShaftSteadyStateSynchronousResponseAtASpeed"],
        "_3505": [
            "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3506": ["AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3507": ["AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3508": ["AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed"],
        "_3509": ["AssemblySteadyStateSynchronousResponseAtASpeed"],
        "_3510": ["BearingSteadyStateSynchronousResponseAtASpeed"],
        "_3511": ["BeltConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3512": ["BeltDriveSteadyStateSynchronousResponseAtASpeed"],
        "_3513": ["BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3514": ["BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3515": ["BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed"],
        "_3516": ["BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed"],
        "_3517": ["BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed"],
        "_3518": ["BevelGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3519": ["BevelGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3520": ["BevelGearSteadyStateSynchronousResponseAtASpeed"],
        "_3521": ["BoltedJointSteadyStateSynchronousResponseAtASpeed"],
        "_3522": ["BoltSteadyStateSynchronousResponseAtASpeed"],
        "_3523": ["ClutchConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3524": ["ClutchHalfSteadyStateSynchronousResponseAtASpeed"],
        "_3525": ["ClutchSteadyStateSynchronousResponseAtASpeed"],
        "_3526": ["CoaxialConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3527": ["ComponentSteadyStateSynchronousResponseAtASpeed"],
        "_3528": ["ConceptCouplingConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3529": ["ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed"],
        "_3530": ["ConceptCouplingSteadyStateSynchronousResponseAtASpeed"],
        "_3531": ["ConceptGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3532": ["ConceptGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3533": ["ConceptGearSteadyStateSynchronousResponseAtASpeed"],
        "_3534": ["ConicalGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3535": ["ConicalGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3536": ["ConicalGearSteadyStateSynchronousResponseAtASpeed"],
        "_3537": ["ConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3538": ["ConnectorSteadyStateSynchronousResponseAtASpeed"],
        "_3539": ["CouplingConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3540": ["CouplingHalfSteadyStateSynchronousResponseAtASpeed"],
        "_3541": ["CouplingSteadyStateSynchronousResponseAtASpeed"],
        "_3542": ["CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3543": ["CVTPulleySteadyStateSynchronousResponseAtASpeed"],
        "_3544": ["CVTSteadyStateSynchronousResponseAtASpeed"],
        "_3545": ["CycloidalAssemblySteadyStateSynchronousResponseAtASpeed"],
        "_3546": [
            "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3547": [
            "CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3548": ["CycloidalDiscSteadyStateSynchronousResponseAtASpeed"],
        "_3549": ["CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3550": ["CylindricalGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3551": ["CylindricalGearSteadyStateSynchronousResponseAtASpeed"],
        "_3552": ["CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed"],
        "_3553": ["DatumSteadyStateSynchronousResponseAtASpeed"],
        "_3554": ["ExternalCADModelSteadyStateSynchronousResponseAtASpeed"],
        "_3555": ["FaceGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3556": ["FaceGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3557": ["FaceGearSteadyStateSynchronousResponseAtASpeed"],
        "_3558": ["FEPartSteadyStateSynchronousResponseAtASpeed"],
        "_3559": ["FlexiblePinAssemblySteadyStateSynchronousResponseAtASpeed"],
        "_3560": ["GearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3561": ["GearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3562": ["GearSteadyStateSynchronousResponseAtASpeed"],
        "_3563": ["GuideDxfModelSteadyStateSynchronousResponseAtASpeed"],
        "_3564": ["HypoidGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3565": ["HypoidGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3566": ["HypoidGearSteadyStateSynchronousResponseAtASpeed"],
        "_3567": [
            "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3568": [
            "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3569": [
            "KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3570": [
            "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3571": [
            "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3572": [
            "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3573": [
            "KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3574": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3575": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3576": [
            "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3577": ["MassDiscSteadyStateSynchronousResponseAtASpeed"],
        "_3578": ["MeasurementComponentSteadyStateSynchronousResponseAtASpeed"],
        "_3579": ["MountableComponentSteadyStateSynchronousResponseAtASpeed"],
        "_3580": ["OilSealSteadyStateSynchronousResponseAtASpeed"],
        "_3581": ["PartSteadyStateSynchronousResponseAtASpeed"],
        "_3582": [
            "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3583": ["PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed"],
        "_3584": ["PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed"],
        "_3585": ["PlanetaryConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3586": ["PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3587": ["PlanetCarrierSteadyStateSynchronousResponseAtASpeed"],
        "_3588": ["PointLoadSteadyStateSynchronousResponseAtASpeed"],
        "_3589": ["PowerLoadSteadyStateSynchronousResponseAtASpeed"],
        "_3590": ["PulleySteadyStateSynchronousResponseAtASpeed"],
        "_3591": ["RingPinsSteadyStateSynchronousResponseAtASpeed"],
        "_3592": ["RingPinsToDiscConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3593": ["RollingRingAssemblySteadyStateSynchronousResponseAtASpeed"],
        "_3594": ["RollingRingConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3595": ["RollingRingSteadyStateSynchronousResponseAtASpeed"],
        "_3596": ["RootAssemblySteadyStateSynchronousResponseAtASpeed"],
        "_3597": ["ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3598": ["ShaftSteadyStateSynchronousResponseAtASpeed"],
        "_3599": [
            "ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3600": ["SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed"],
        "_3601": ["SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3602": ["SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3603": ["SpiralBevelGearSteadyStateSynchronousResponseAtASpeed"],
        "_3604": ["SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3605": ["SpringDamperHalfSteadyStateSynchronousResponseAtASpeed"],
        "_3606": ["SpringDamperSteadyStateSynchronousResponseAtASpeed"],
        "_3607": ["SteadyStateSynchronousResponseAtASpeed"],
        "_3608": ["StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3609": ["StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3610": ["StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed"],
        "_3611": ["StraightBevelGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3612": ["StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3613": ["StraightBevelGearSteadyStateSynchronousResponseAtASpeed"],
        "_3614": ["StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed"],
        "_3615": ["StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed"],
        "_3616": ["SynchroniserHalfSteadyStateSynchronousResponseAtASpeed"],
        "_3617": ["SynchroniserPartSteadyStateSynchronousResponseAtASpeed"],
        "_3618": ["SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed"],
        "_3619": ["SynchroniserSteadyStateSynchronousResponseAtASpeed"],
        "_3620": ["TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3621": ["TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed"],
        "_3622": ["TorqueConverterSteadyStateSynchronousResponseAtASpeed"],
        "_3623": ["TorqueConverterTurbineSteadyStateSynchronousResponseAtASpeed"],
        "_3624": ["UnbalancedMassSteadyStateSynchronousResponseAtASpeed"],
        "_3625": ["VirtualComponentSteadyStateSynchronousResponseAtASpeed"],
        "_3626": ["WormGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3627": ["WormGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3628": ["WormGearSteadyStateSynchronousResponseAtASpeed"],
        "_3629": ["ZerolBevelGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3630": ["ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3631": ["ZerolBevelGearSteadyStateSynchronousResponseAtASpeed"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
    "AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed",
    "AbstractShaftSteadyStateSynchronousResponseAtASpeed",
    "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
    "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed",
    "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
    "AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed",
    "AssemblySteadyStateSynchronousResponseAtASpeed",
    "BearingSteadyStateSynchronousResponseAtASpeed",
    "BeltConnectionSteadyStateSynchronousResponseAtASpeed",
    "BeltDriveSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed",
    "BevelGearMeshSteadyStateSynchronousResponseAtASpeed",
    "BevelGearSetSteadyStateSynchronousResponseAtASpeed",
    "BevelGearSteadyStateSynchronousResponseAtASpeed",
    "BoltedJointSteadyStateSynchronousResponseAtASpeed",
    "BoltSteadyStateSynchronousResponseAtASpeed",
    "ClutchConnectionSteadyStateSynchronousResponseAtASpeed",
    "ClutchHalfSteadyStateSynchronousResponseAtASpeed",
    "ClutchSteadyStateSynchronousResponseAtASpeed",
    "CoaxialConnectionSteadyStateSynchronousResponseAtASpeed",
    "ComponentSteadyStateSynchronousResponseAtASpeed",
    "ConceptCouplingConnectionSteadyStateSynchronousResponseAtASpeed",
    "ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed",
    "ConceptCouplingSteadyStateSynchronousResponseAtASpeed",
    "ConceptGearMeshSteadyStateSynchronousResponseAtASpeed",
    "ConceptGearSetSteadyStateSynchronousResponseAtASpeed",
    "ConceptGearSteadyStateSynchronousResponseAtASpeed",
    "ConicalGearMeshSteadyStateSynchronousResponseAtASpeed",
    "ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
    "ConicalGearSteadyStateSynchronousResponseAtASpeed",
    "ConnectionSteadyStateSynchronousResponseAtASpeed",
    "ConnectorSteadyStateSynchronousResponseAtASpeed",
    "CouplingConnectionSteadyStateSynchronousResponseAtASpeed",
    "CouplingHalfSteadyStateSynchronousResponseAtASpeed",
    "CouplingSteadyStateSynchronousResponseAtASpeed",
    "CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed",
    "CVTPulleySteadyStateSynchronousResponseAtASpeed",
    "CVTSteadyStateSynchronousResponseAtASpeed",
    "CycloidalAssemblySteadyStateSynchronousResponseAtASpeed",
    "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed",
    "CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseAtASpeed",
    "CycloidalDiscSteadyStateSynchronousResponseAtASpeed",
    "CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed",
    "CylindricalGearSetSteadyStateSynchronousResponseAtASpeed",
    "CylindricalGearSteadyStateSynchronousResponseAtASpeed",
    "CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed",
    "DatumSteadyStateSynchronousResponseAtASpeed",
    "ExternalCADModelSteadyStateSynchronousResponseAtASpeed",
    "FaceGearMeshSteadyStateSynchronousResponseAtASpeed",
    "FaceGearSetSteadyStateSynchronousResponseAtASpeed",
    "FaceGearSteadyStateSynchronousResponseAtASpeed",
    "FEPartSteadyStateSynchronousResponseAtASpeed",
    "FlexiblePinAssemblySteadyStateSynchronousResponseAtASpeed",
    "GearMeshSteadyStateSynchronousResponseAtASpeed",
    "GearSetSteadyStateSynchronousResponseAtASpeed",
    "GearSteadyStateSynchronousResponseAtASpeed",
    "GuideDxfModelSteadyStateSynchronousResponseAtASpeed",
    "HypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
    "HypoidGearSetSteadyStateSynchronousResponseAtASpeed",
    "HypoidGearSteadyStateSynchronousResponseAtASpeed",
    "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseAtASpeed",
    "MassDiscSteadyStateSynchronousResponseAtASpeed",
    "MeasurementComponentSteadyStateSynchronousResponseAtASpeed",
    "MountableComponentSteadyStateSynchronousResponseAtASpeed",
    "OilSealSteadyStateSynchronousResponseAtASpeed",
    "PartSteadyStateSynchronousResponseAtASpeed",
    "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed",
    "PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed",
    "PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed",
    "PlanetaryConnectionSteadyStateSynchronousResponseAtASpeed",
    "PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed",
    "PlanetCarrierSteadyStateSynchronousResponseAtASpeed",
    "PointLoadSteadyStateSynchronousResponseAtASpeed",
    "PowerLoadSteadyStateSynchronousResponseAtASpeed",
    "PulleySteadyStateSynchronousResponseAtASpeed",
    "RingPinsSteadyStateSynchronousResponseAtASpeed",
    "RingPinsToDiscConnectionSteadyStateSynchronousResponseAtASpeed",
    "RollingRingAssemblySteadyStateSynchronousResponseAtASpeed",
    "RollingRingConnectionSteadyStateSynchronousResponseAtASpeed",
    "RollingRingSteadyStateSynchronousResponseAtASpeed",
    "RootAssemblySteadyStateSynchronousResponseAtASpeed",
    "ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed",
    "ShaftSteadyStateSynchronousResponseAtASpeed",
    "ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
    "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
    "SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed",
    "SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed",
    "SpiralBevelGearSteadyStateSynchronousResponseAtASpeed",
    "SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed",
    "SpringDamperHalfSteadyStateSynchronousResponseAtASpeed",
    "SpringDamperSteadyStateSynchronousResponseAtASpeed",
    "SteadyStateSynchronousResponseAtASpeed",
    "StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelGearMeshSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelGearSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
    "SynchroniserHalfSteadyStateSynchronousResponseAtASpeed",
    "SynchroniserPartSteadyStateSynchronousResponseAtASpeed",
    "SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed",
    "SynchroniserSteadyStateSynchronousResponseAtASpeed",
    "TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed",
    "TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed",
    "TorqueConverterSteadyStateSynchronousResponseAtASpeed",
    "TorqueConverterTurbineSteadyStateSynchronousResponseAtASpeed",
    "UnbalancedMassSteadyStateSynchronousResponseAtASpeed",
    "VirtualComponentSteadyStateSynchronousResponseAtASpeed",
    "WormGearMeshSteadyStateSynchronousResponseAtASpeed",
    "WormGearSetSteadyStateSynchronousResponseAtASpeed",
    "WormGearSteadyStateSynchronousResponseAtASpeed",
    "ZerolBevelGearMeshSteadyStateSynchronousResponseAtASpeed",
    "ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed",
    "ZerolBevelGearSteadyStateSynchronousResponseAtASpeed",
)
