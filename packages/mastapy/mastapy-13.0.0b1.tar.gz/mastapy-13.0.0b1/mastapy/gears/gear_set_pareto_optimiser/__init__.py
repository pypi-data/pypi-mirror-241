"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._900 import BarForPareto
    from ._901 import CandidateDisplayChoice
    from ._902 import ChartInfoBase
    from ._903 import CylindricalGearSetParetoOptimiser
    from ._904 import DesignSpaceSearchBase
    from ._905 import DesignSpaceSearchCandidateBase
    from ._906 import FaceGearSetParetoOptimiser
    from ._907 import GearNameMapper
    from ._908 import GearNamePicker
    from ._909 import GearSetOptimiserCandidate
    from ._910 import GearSetParetoOptimiser
    from ._911 import HypoidGearSetParetoOptimiser
    from ._912 import InputSliderForPareto
    from ._913 import LargerOrSmaller
    from ._914 import MicroGeometryDesignSpaceSearch
    from ._915 import MicroGeometryDesignSpaceSearchCandidate
    from ._916 import MicroGeometryDesignSpaceSearchChartInformation
    from ._917 import MicroGeometryGearSetDesignSpaceSearch
    from ._918 import MicroGeometryGearSetDesignSpaceSearchStrategyDatabase
    from ._919 import MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase
    from ._920 import OptimisationTarget
    from ._921 import ParetoConicalRatingOptimisationStrategyDatabase
    from ._922 import ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase
    from ._923 import ParetoCylindricalGearSetOptimisationStrategyDatabase
    from ._924 import ParetoCylindricalRatingOptimisationStrategyDatabase
    from ._925 import ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase
    from ._926 import ParetoFaceGearSetOptimisationStrategyDatabase
    from ._927 import ParetoFaceRatingOptimisationStrategyDatabase
    from ._928 import ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase
    from ._929 import ParetoHypoidGearSetOptimisationStrategyDatabase
    from ._930 import ParetoOptimiserChartInformation
    from ._931 import ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase
    from ._932 import ParetoSpiralBevelGearSetOptimisationStrategyDatabase
    from ._933 import ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase
    from ._934 import ParetoStraightBevelGearSetOptimisationStrategyDatabase
    from ._935 import ReasonsForInvalidDesigns
    from ._936 import SpiralBevelGearSetParetoOptimiser
    from ._937 import StraightBevelGearSetParetoOptimiser
else:
    import_structure = {
        "_900": ["BarForPareto"],
        "_901": ["CandidateDisplayChoice"],
        "_902": ["ChartInfoBase"],
        "_903": ["CylindricalGearSetParetoOptimiser"],
        "_904": ["DesignSpaceSearchBase"],
        "_905": ["DesignSpaceSearchCandidateBase"],
        "_906": ["FaceGearSetParetoOptimiser"],
        "_907": ["GearNameMapper"],
        "_908": ["GearNamePicker"],
        "_909": ["GearSetOptimiserCandidate"],
        "_910": ["GearSetParetoOptimiser"],
        "_911": ["HypoidGearSetParetoOptimiser"],
        "_912": ["InputSliderForPareto"],
        "_913": ["LargerOrSmaller"],
        "_914": ["MicroGeometryDesignSpaceSearch"],
        "_915": ["MicroGeometryDesignSpaceSearchCandidate"],
        "_916": ["MicroGeometryDesignSpaceSearchChartInformation"],
        "_917": ["MicroGeometryGearSetDesignSpaceSearch"],
        "_918": ["MicroGeometryGearSetDesignSpaceSearchStrategyDatabase"],
        "_919": ["MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase"],
        "_920": ["OptimisationTarget"],
        "_921": ["ParetoConicalRatingOptimisationStrategyDatabase"],
        "_922": ["ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase"],
        "_923": ["ParetoCylindricalGearSetOptimisationStrategyDatabase"],
        "_924": ["ParetoCylindricalRatingOptimisationStrategyDatabase"],
        "_925": ["ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase"],
        "_926": ["ParetoFaceGearSetOptimisationStrategyDatabase"],
        "_927": ["ParetoFaceRatingOptimisationStrategyDatabase"],
        "_928": ["ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase"],
        "_929": ["ParetoHypoidGearSetOptimisationStrategyDatabase"],
        "_930": ["ParetoOptimiserChartInformation"],
        "_931": ["ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase"],
        "_932": ["ParetoSpiralBevelGearSetOptimisationStrategyDatabase"],
        "_933": ["ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase"],
        "_934": ["ParetoStraightBevelGearSetOptimisationStrategyDatabase"],
        "_935": ["ReasonsForInvalidDesigns"],
        "_936": ["SpiralBevelGearSetParetoOptimiser"],
        "_937": ["StraightBevelGearSetParetoOptimiser"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BarForPareto",
    "CandidateDisplayChoice",
    "ChartInfoBase",
    "CylindricalGearSetParetoOptimiser",
    "DesignSpaceSearchBase",
    "DesignSpaceSearchCandidateBase",
    "FaceGearSetParetoOptimiser",
    "GearNameMapper",
    "GearNamePicker",
    "GearSetOptimiserCandidate",
    "GearSetParetoOptimiser",
    "HypoidGearSetParetoOptimiser",
    "InputSliderForPareto",
    "LargerOrSmaller",
    "MicroGeometryDesignSpaceSearch",
    "MicroGeometryDesignSpaceSearchCandidate",
    "MicroGeometryDesignSpaceSearchChartInformation",
    "MicroGeometryGearSetDesignSpaceSearch",
    "MicroGeometryGearSetDesignSpaceSearchStrategyDatabase",
    "MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase",
    "OptimisationTarget",
    "ParetoConicalRatingOptimisationStrategyDatabase",
    "ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase",
    "ParetoCylindricalGearSetOptimisationStrategyDatabase",
    "ParetoCylindricalRatingOptimisationStrategyDatabase",
    "ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase",
    "ParetoFaceGearSetOptimisationStrategyDatabase",
    "ParetoFaceRatingOptimisationStrategyDatabase",
    "ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase",
    "ParetoHypoidGearSetOptimisationStrategyDatabase",
    "ParetoOptimiserChartInformation",
    "ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase",
    "ParetoSpiralBevelGearSetOptimisationStrategyDatabase",
    "ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase",
    "ParetoStraightBevelGearSetOptimisationStrategyDatabase",
    "ReasonsForInvalidDesigns",
    "SpiralBevelGearSetParetoOptimiser",
    "StraightBevelGearSetParetoOptimiser",
)
