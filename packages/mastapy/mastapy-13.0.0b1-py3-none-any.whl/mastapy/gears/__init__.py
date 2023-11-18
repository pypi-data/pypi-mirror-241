"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._312 import AccuracyGrades
    from ._313 import AGMAToleranceStandard
    from ._314 import BevelHypoidGearDesignSettings
    from ._315 import BevelHypoidGearRatingSettings
    from ._316 import CentreDistanceChangeMethod
    from ._317 import CoefficientOfFrictionCalculationMethod
    from ._318 import ConicalGearToothSurface
    from ._319 import ContactRatioDataSource
    from ._320 import ContactRatioRequirements
    from ._321 import CylindricalFlanks
    from ._322 import CylindricalMisalignmentDataSource
    from ._323 import DeflectionFromBendingOption
    from ._324 import GearFlanks
    from ._325 import GearNURBSSurface
    from ._326 import GearSetDesignGroup
    from ._327 import GearSetModes
    from ._328 import GearSetOptimisationResult
    from ._329 import GearSetOptimisationResults
    from ._330 import GearSetOptimiser
    from ._331 import Hand
    from ._332 import ISOToleranceStandard
    from ._333 import LubricationMethods
    from ._334 import MicroGeometryInputTypes
    from ._335 import MicroGeometryModel
    from ._336 import MicropittingCoefficientOfFrictionCalculationMethod
    from ._337 import NamedPlanetAngle
    from ._338 import PlanetaryDetail
    from ._339 import PlanetaryRatingLoadSharingOption
    from ._340 import PocketingPowerLossCoefficients
    from ._341 import PocketingPowerLossCoefficientsDatabase
    from ._342 import QualityGradeTypes
    from ._343 import SafetyRequirementsAGMA
    from ._344 import SpecificationForTheEffectOfOilKinematicViscosity
    from ._345 import SpiralBevelRootLineTilt
    from ._346 import SpiralBevelToothTaper
    from ._347 import TESpecificationType
    from ._348 import WormAddendumFactor
    from ._349 import WormType
    from ._350 import ZerolBevelGleasonToothTaperOption
else:
    import_structure = {
        "_312": ["AccuracyGrades"],
        "_313": ["AGMAToleranceStandard"],
        "_314": ["BevelHypoidGearDesignSettings"],
        "_315": ["BevelHypoidGearRatingSettings"],
        "_316": ["CentreDistanceChangeMethod"],
        "_317": ["CoefficientOfFrictionCalculationMethod"],
        "_318": ["ConicalGearToothSurface"],
        "_319": ["ContactRatioDataSource"],
        "_320": ["ContactRatioRequirements"],
        "_321": ["CylindricalFlanks"],
        "_322": ["CylindricalMisalignmentDataSource"],
        "_323": ["DeflectionFromBendingOption"],
        "_324": ["GearFlanks"],
        "_325": ["GearNURBSSurface"],
        "_326": ["GearSetDesignGroup"],
        "_327": ["GearSetModes"],
        "_328": ["GearSetOptimisationResult"],
        "_329": ["GearSetOptimisationResults"],
        "_330": ["GearSetOptimiser"],
        "_331": ["Hand"],
        "_332": ["ISOToleranceStandard"],
        "_333": ["LubricationMethods"],
        "_334": ["MicroGeometryInputTypes"],
        "_335": ["MicroGeometryModel"],
        "_336": ["MicropittingCoefficientOfFrictionCalculationMethod"],
        "_337": ["NamedPlanetAngle"],
        "_338": ["PlanetaryDetail"],
        "_339": ["PlanetaryRatingLoadSharingOption"],
        "_340": ["PocketingPowerLossCoefficients"],
        "_341": ["PocketingPowerLossCoefficientsDatabase"],
        "_342": ["QualityGradeTypes"],
        "_343": ["SafetyRequirementsAGMA"],
        "_344": ["SpecificationForTheEffectOfOilKinematicViscosity"],
        "_345": ["SpiralBevelRootLineTilt"],
        "_346": ["SpiralBevelToothTaper"],
        "_347": ["TESpecificationType"],
        "_348": ["WormAddendumFactor"],
        "_349": ["WormType"],
        "_350": ["ZerolBevelGleasonToothTaperOption"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AccuracyGrades",
    "AGMAToleranceStandard",
    "BevelHypoidGearDesignSettings",
    "BevelHypoidGearRatingSettings",
    "CentreDistanceChangeMethod",
    "CoefficientOfFrictionCalculationMethod",
    "ConicalGearToothSurface",
    "ContactRatioDataSource",
    "ContactRatioRequirements",
    "CylindricalFlanks",
    "CylindricalMisalignmentDataSource",
    "DeflectionFromBendingOption",
    "GearFlanks",
    "GearNURBSSurface",
    "GearSetDesignGroup",
    "GearSetModes",
    "GearSetOptimisationResult",
    "GearSetOptimisationResults",
    "GearSetOptimiser",
    "Hand",
    "ISOToleranceStandard",
    "LubricationMethods",
    "MicroGeometryInputTypes",
    "MicroGeometryModel",
    "MicropittingCoefficientOfFrictionCalculationMethod",
    "NamedPlanetAngle",
    "PlanetaryDetail",
    "PlanetaryRatingLoadSharingOption",
    "PocketingPowerLossCoefficients",
    "PocketingPowerLossCoefficientsDatabase",
    "QualityGradeTypes",
    "SafetyRequirementsAGMA",
    "SpecificationForTheEffectOfOilKinematicViscosity",
    "SpiralBevelRootLineTilt",
    "SpiralBevelToothTaper",
    "TESpecificationType",
    "WormAddendumFactor",
    "WormType",
    "ZerolBevelGleasonToothTaperOption",
)
