"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._3373 import AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3374 import AbstractShaftCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3375 import (
        AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3376 import (
        AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3377 import (
        AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3378 import (
        AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3379 import (
        AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3380 import AssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3381 import BearingCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3382 import BeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3383 import BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3384 import (
        BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3385 import (
        BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3386 import (
        BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3387 import (
        BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3388 import (
        BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3389 import BevelGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3390 import BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3391 import BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3392 import BoltCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3393 import BoltedJointCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3394 import ClutchCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3395 import ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3396 import ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3397 import CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3398 import ComponentCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3399 import ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3400 import (
        ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3401 import ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3402 import ConceptGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3403 import ConceptGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3404 import ConceptGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3405 import ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3406 import ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3407 import ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3408 import ConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3409 import ConnectorCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3410 import CouplingCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3411 import CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3412 import CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3413 import CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3414 import CVTCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3415 import CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3416 import CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3417 import (
        CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3418 import CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3419 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3420 import CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3421 import CylindricalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3422 import CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3423 import (
        CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3424 import DatumCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3425 import ExternalCADModelCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3426 import FaceGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3427 import FaceGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3428 import FaceGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3429 import FEPartCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3430 import FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3431 import GearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3432 import GearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3433 import GearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3434 import GuideDxfModelCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3435 import HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3436 import HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3437 import HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3438 import (
        InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3439 import (
        KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3440 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3441 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3442 import (
        KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3443 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3444 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3445 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3446 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3447 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3448 import MassDiscCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3449 import (
        MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3450 import MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3451 import OilSealCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3452 import PartCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3453 import (
        PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3454 import (
        PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3455 import (
        PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3456 import PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3457 import PlanetaryGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3458 import PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3459 import PointLoadCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3460 import PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3461 import PulleyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3462 import RingPinsCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3463 import (
        RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3464 import RollingRingAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3465 import RollingRingCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3466 import (
        RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3467 import RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3468 import ShaftCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3469 import ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3470 import (
        ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3471 import SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3472 import SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3473 import SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3474 import SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3475 import SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3476 import (
        SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3477 import SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3478 import (
        StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3479 import (
        StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3480 import (
        StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3481 import StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3482 import (
        StraightBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3483 import (
        StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3484 import (
        StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3485 import (
        StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3486 import SynchroniserCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3487 import SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3488 import SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3489 import SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3490 import TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3491 import (
        TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3492 import TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3493 import (
        TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3494 import UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3495 import VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3496 import WormGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3497 import WormGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3498 import WormGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3499 import ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3500 import ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3501 import ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
else:
    import_structure = {
        "_3373": ["AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3374": ["AbstractShaftCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3375": [
            "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3376": [
            "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3377": [
            "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3378": [
            "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3379": [
            "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3380": ["AssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3381": ["BearingCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3382": ["BeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3383": ["BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3384": [
            "BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3385": [
            "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3386": [
            "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3387": [
            "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3388": [
            "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3389": ["BevelGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3390": ["BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3391": ["BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3392": ["BoltCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3393": ["BoltedJointCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3394": ["ClutchCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3395": ["ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3396": ["ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3397": ["CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3398": ["ComponentCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3399": ["ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3400": [
            "ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3401": ["ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3402": ["ConceptGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3403": ["ConceptGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3404": ["ConceptGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3405": ["ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3406": ["ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3407": ["ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3408": ["ConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3409": ["ConnectorCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3410": ["CouplingCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3411": ["CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3412": ["CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3413": ["CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3414": ["CVTCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3415": ["CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3416": ["CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3417": [
            "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3418": ["CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3419": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3420": ["CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3421": ["CylindricalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3422": ["CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3423": [
            "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3424": ["DatumCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3425": ["ExternalCADModelCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3426": ["FaceGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3427": ["FaceGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3428": ["FaceGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3429": ["FEPartCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3430": ["FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3431": ["GearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3432": ["GearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3433": ["GearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3434": ["GuideDxfModelCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3435": ["HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3436": ["HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3437": ["HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3438": [
            "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3439": [
            "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3440": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3441": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3442": [
            "KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3443": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3444": [
            "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3445": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3446": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3447": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3448": ["MassDiscCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3449": ["MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3450": ["MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3451": ["OilSealCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3452": ["PartCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3453": [
            "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3454": [
            "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3455": [
            "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3456": ["PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3457": ["PlanetaryGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3458": ["PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3459": ["PointLoadCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3460": ["PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3461": ["PulleyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3462": ["RingPinsCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3463": [
            "RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3464": ["RollingRingAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3465": ["RollingRingCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3466": [
            "RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3467": ["RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3468": ["ShaftCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3469": ["ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3470": [
            "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3471": ["SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3472": ["SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3473": ["SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3474": ["SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3475": ["SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3476": [
            "SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3477": ["SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3478": [
            "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3479": [
            "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3480": [
            "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3481": ["StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3482": [
            "StraightBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3483": ["StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3484": [
            "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3485": ["StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3486": ["SynchroniserCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3487": ["SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3488": ["SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3489": ["SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3490": ["TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3491": [
            "TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3492": ["TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3493": [
            "TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3494": ["UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3495": ["VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3496": ["WormGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3497": ["WormGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3498": ["WormGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3499": ["ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3500": ["ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3501": ["ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "AbstractShaftCompoundSteadyStateSynchronousResponseOnAShaft",
    "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft",
    "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "AssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "BearingCompoundSteadyStateSynchronousResponseOnAShaft",
    "BeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "BoltCompoundSteadyStateSynchronousResponseOnAShaft",
    "BoltedJointCompoundSteadyStateSynchronousResponseOnAShaft",
    "ClutchCompoundSteadyStateSynchronousResponseOnAShaft",
    "ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft",
    "CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConceptGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConceptGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConceptGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConnectorCompoundSteadyStateSynchronousResponseOnAShaft",
    "CouplingCompoundSteadyStateSynchronousResponseOnAShaft",
    "CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
    "CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "CVTCompoundSteadyStateSynchronousResponseOnAShaft",
    "CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft",
    "CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft",
    "CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "CylindricalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "DatumCompoundSteadyStateSynchronousResponseOnAShaft",
    "ExternalCADModelCompoundSteadyStateSynchronousResponseOnAShaft",
    "FaceGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "FaceGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "FaceGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "FEPartCompoundSteadyStateSynchronousResponseOnAShaft",
    "FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "GearCompoundSteadyStateSynchronousResponseOnAShaft",
    "GearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "GearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "GuideDxfModelCompoundSteadyStateSynchronousResponseOnAShaft",
    "HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "MassDiscCompoundSteadyStateSynchronousResponseOnAShaft",
    "MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft",
    "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
    "OilSealCompoundSteadyStateSynchronousResponseOnAShaft",
    "PartCompoundSteadyStateSynchronousResponseOnAShaft",
    "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft",
    "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
    "PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "PlanetaryGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft",
    "PointLoadCompoundSteadyStateSynchronousResponseOnAShaft",
    "PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft",
    "PulleyCompoundSteadyStateSynchronousResponseOnAShaft",
    "RingPinsCompoundSteadyStateSynchronousResponseOnAShaft",
    "RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "RollingRingAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "RollingRingCompoundSteadyStateSynchronousResponseOnAShaft",
    "RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "ShaftCompoundSteadyStateSynchronousResponseOnAShaft",
    "ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "SynchroniserCompoundSteadyStateSynchronousResponseOnAShaft",
    "SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft",
    "SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft",
    "SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft",
    "TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft",
    "TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft",
    "TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft",
    "UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft",
    "VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft",
    "WormGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "WormGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "WormGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
)
