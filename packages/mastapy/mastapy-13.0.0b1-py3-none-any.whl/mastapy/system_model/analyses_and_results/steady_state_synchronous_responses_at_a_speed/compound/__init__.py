"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._3632 import AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3633 import AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3634 import (
        AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3635 import (
        AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3636 import (
        AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3637 import (
        AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3638 import (
        AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3639 import AssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3640 import BearingCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3641 import BeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3642 import BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3643 import (
        BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3644 import (
        BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3645 import (
        BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3646 import (
        BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3647 import (
        BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3648 import BevelGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3649 import BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3650 import BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3651 import BoltCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3652 import BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3653 import ClutchCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3654 import ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3655 import ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3656 import CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3657 import ComponentCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3658 import ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3659 import (
        ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3660 import ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3661 import ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3662 import ConceptGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3663 import ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3664 import ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3665 import ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3666 import ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3667 import ConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3668 import ConnectorCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3669 import CouplingCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3670 import CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3671 import CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3672 import CVTBeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3673 import CVTCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3674 import CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3675 import CycloidalAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3676 import (
        CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3677 import CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3678 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3679 import CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3680 import CylindricalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3681 import CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3682 import (
        CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3683 import DatumCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3684 import ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3685 import FaceGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3686 import FaceGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3687 import FaceGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3688 import FEPartCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3689 import FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3690 import GearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3691 import GearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3692 import GearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3693 import GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3694 import HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3695 import HypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3696 import HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3697 import (
        InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3698 import (
        KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3699 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3700 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3701 import (
        KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3702 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3703 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3704 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3705 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3706 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3707 import MassDiscCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3708 import (
        MeasurementComponentCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3709 import MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3710 import OilSealCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3711 import PartCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3712 import (
        PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3713 import (
        PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3714 import (
        PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3715 import PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3716 import PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3717 import PlanetCarrierCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3718 import PointLoadCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3719 import PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3720 import PulleyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3721 import RingPinsCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3722 import (
        RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3723 import RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3724 import RollingRingCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3725 import (
        RollingRingConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3726 import RootAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3727 import ShaftCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3728 import ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3729 import (
        ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3730 import SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3731 import SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3732 import SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3733 import SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3734 import SpringDamperCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3735 import (
        SpringDamperConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3736 import SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3737 import (
        StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3738 import (
        StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3739 import (
        StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3740 import StraightBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3741 import (
        StraightBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3742 import (
        StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3743 import (
        StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3744 import (
        StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3745 import SynchroniserCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3746 import SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3747 import SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3748 import SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3749 import TorqueConverterCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3750 import (
        TorqueConverterConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3751 import TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3752 import (
        TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3753 import UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3754 import VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3755 import WormGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3756 import WormGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3757 import WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3758 import ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3759 import ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3760 import ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
else:
    import_structure = {
        "_3632": ["AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3633": ["AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3634": [
            "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3635": [
            "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3636": [
            "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3637": [
            "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3638": [
            "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3639": ["AssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3640": ["BearingCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3641": ["BeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3642": ["BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3643": [
            "BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3644": [
            "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3645": [
            "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3646": [
            "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3647": [
            "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3648": ["BevelGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3649": ["BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3650": ["BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3651": ["BoltCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3652": ["BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3653": ["ClutchCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3654": ["ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3655": ["ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3656": ["CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3657": ["ComponentCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3658": ["ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3659": [
            "ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3660": ["ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3661": ["ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3662": ["ConceptGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3663": ["ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3664": ["ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3665": ["ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3666": ["ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3667": ["ConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3668": ["ConnectorCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3669": ["CouplingCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3670": ["CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3671": ["CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3672": ["CVTBeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3673": ["CVTCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3674": ["CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3675": ["CycloidalAssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3676": [
            "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3677": ["CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3678": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3679": ["CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3680": ["CylindricalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3681": ["CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3682": [
            "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3683": ["DatumCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3684": ["ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3685": ["FaceGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3686": ["FaceGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3687": ["FaceGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3688": ["FEPartCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3689": ["FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3690": ["GearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3691": ["GearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3692": ["GearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3693": ["GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3694": ["HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3695": ["HypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3696": ["HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3697": [
            "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3698": [
            "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3699": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3700": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3701": [
            "KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3702": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3703": [
            "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3704": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3705": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3706": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3707": ["MassDiscCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3708": ["MeasurementComponentCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3709": ["MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3710": ["OilSealCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3711": ["PartCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3712": [
            "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3713": [
            "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3714": [
            "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3715": ["PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3716": ["PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3717": ["PlanetCarrierCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3718": ["PointLoadCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3719": ["PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3720": ["PulleyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3721": ["RingPinsCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3722": [
            "RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3723": ["RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3724": ["RollingRingCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3725": [
            "RollingRingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3726": ["RootAssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3727": ["ShaftCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3728": ["ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3729": [
            "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3730": ["SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3731": ["SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3732": ["SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3733": ["SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3734": ["SpringDamperCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3735": [
            "SpringDamperConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3736": ["SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3737": [
            "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3738": [
            "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3739": [
            "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3740": ["StraightBevelGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3741": [
            "StraightBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3742": ["StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3743": [
            "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3744": ["StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3745": ["SynchroniserCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3746": ["SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3747": ["SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3748": ["SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3749": ["TorqueConverterCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3750": [
            "TorqueConverterConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3751": ["TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3752": [
            "TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3753": ["UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3754": ["VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3755": ["WormGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3756": ["WormGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3757": ["WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3758": ["ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3759": ["ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3760": ["ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed",
    "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed",
    "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "AssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "BearingCompoundSteadyStateSynchronousResponseAtASpeed",
    "BeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "BoltCompoundSteadyStateSynchronousResponseAtASpeed",
    "BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed",
    "ClutchCompoundSteadyStateSynchronousResponseAtASpeed",
    "ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    "CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConceptGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConnectorCompoundSteadyStateSynchronousResponseAtASpeed",
    "CouplingCompoundSteadyStateSynchronousResponseAtASpeed",
    "CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    "CVTBeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "CVTCompoundSteadyStateSynchronousResponseAtASpeed",
    "CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed",
    "CycloidalAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed",
    "CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "CylindricalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "DatumCompoundSteadyStateSynchronousResponseAtASpeed",
    "ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed",
    "FaceGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "FaceGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "FaceGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "FEPartCompoundSteadyStateSynchronousResponseAtASpeed",
    "FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "GearCompoundSteadyStateSynchronousResponseAtASpeed",
    "GearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "GearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed",
    "HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "HypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "MassDiscCompoundSteadyStateSynchronousResponseAtASpeed",
    "MeasurementComponentCompoundSteadyStateSynchronousResponseAtASpeed",
    "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
    "OilSealCompoundSteadyStateSynchronousResponseAtASpeed",
    "PartCompoundSteadyStateSynchronousResponseAtASpeed",
    "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed",
    "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    "PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "PlanetCarrierCompoundSteadyStateSynchronousResponseAtASpeed",
    "PointLoadCompoundSteadyStateSynchronousResponseAtASpeed",
    "PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed",
    "PulleyCompoundSteadyStateSynchronousResponseAtASpeed",
    "RingPinsCompoundSteadyStateSynchronousResponseAtASpeed",
    "RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "RollingRingCompoundSteadyStateSynchronousResponseAtASpeed",
    "RollingRingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "RootAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "ShaftCompoundSteadyStateSynchronousResponseAtASpeed",
    "ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpringDamperCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpringDamperConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "SynchroniserCompoundSteadyStateSynchronousResponseAtASpeed",
    "SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    "SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed",
    "SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed",
    "TorqueConverterCompoundSteadyStateSynchronousResponseAtASpeed",
    "TorqueConverterConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed",
    "TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed",
    "UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed",
    "VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed",
    "WormGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "WormGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
)
