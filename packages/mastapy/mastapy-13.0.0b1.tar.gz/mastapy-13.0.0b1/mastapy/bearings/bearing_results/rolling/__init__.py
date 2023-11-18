"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1964 import BallBearingAnalysisMethod
    from ._1965 import BallBearingContactCalculation
    from ._1966 import BallBearingRaceContactGeometry
    from ._1967 import DIN7322010Results
    from ._1968 import ForceAtLaminaGroupReportable
    from ._1969 import ForceAtLaminaReportable
    from ._1970 import FrictionModelForGyroscopicMoment
    from ._1971 import InternalClearance
    from ._1972 import ISO14179Settings
    from ._1973 import ISO14179SettingsDatabase
    from ._1974 import ISO14179SettingsPerBearingType
    from ._1975 import ISO153122018Results
    from ._1976 import ISOTR1417912001Results
    from ._1977 import ISOTR141792001Results
    from ._1978 import ISOTR1417922001Results
    from ._1979 import LoadedAbstractSphericalRollerBearingStripLoadResults
    from ._1980 import LoadedAngularContactBallBearingElement
    from ._1981 import LoadedAngularContactBallBearingResults
    from ._1982 import LoadedAngularContactBallBearingRow
    from ._1983 import LoadedAngularContactThrustBallBearingElement
    from ._1984 import LoadedAngularContactThrustBallBearingResults
    from ._1985 import LoadedAngularContactThrustBallBearingRow
    from ._1986 import LoadedAsymmetricSphericalRollerBearingElement
    from ._1987 import LoadedAsymmetricSphericalRollerBearingResults
    from ._1988 import LoadedAsymmetricSphericalRollerBearingRow
    from ._1989 import LoadedAsymmetricSphericalRollerBearingStripLoadResults
    from ._1990 import LoadedAxialThrustCylindricalRollerBearingDutyCycle
    from ._1991 import LoadedAxialThrustCylindricalRollerBearingElement
    from ._1992 import LoadedAxialThrustCylindricalRollerBearingResults
    from ._1993 import LoadedAxialThrustCylindricalRollerBearingRow
    from ._1994 import LoadedAxialThrustNeedleRollerBearingElement
    from ._1995 import LoadedAxialThrustNeedleRollerBearingResults
    from ._1996 import LoadedAxialThrustNeedleRollerBearingRow
    from ._1997 import LoadedBallBearingDutyCycle
    from ._1998 import LoadedBallBearingElement
    from ._1999 import LoadedBallBearingRaceResults
    from ._2000 import LoadedBallBearingResults
    from ._2001 import LoadedBallBearingRow
    from ._2002 import LoadedCrossedRollerBearingElement
    from ._2003 import LoadedCrossedRollerBearingResults
    from ._2004 import LoadedCrossedRollerBearingRow
    from ._2005 import LoadedCylindricalRollerBearingDutyCycle
    from ._2006 import LoadedCylindricalRollerBearingElement
    from ._2007 import LoadedCylindricalRollerBearingResults
    from ._2008 import LoadedCylindricalRollerBearingRow
    from ._2009 import LoadedDeepGrooveBallBearingElement
    from ._2010 import LoadedDeepGrooveBallBearingResults
    from ._2011 import LoadedDeepGrooveBallBearingRow
    from ._2012 import LoadedElement
    from ._2013 import LoadedFourPointContactBallBearingElement
    from ._2014 import LoadedFourPointContactBallBearingRaceResults
    from ._2015 import LoadedFourPointContactBallBearingResults
    from ._2016 import LoadedFourPointContactBallBearingRow
    from ._2017 import LoadedMultiPointContactBallBearingElement
    from ._2018 import LoadedNeedleRollerBearingElement
    from ._2019 import LoadedNeedleRollerBearingResults
    from ._2020 import LoadedNeedleRollerBearingRow
    from ._2021 import LoadedNonBarrelRollerBearingDutyCycle
    from ._2022 import LoadedNonBarrelRollerBearingResults
    from ._2023 import LoadedNonBarrelRollerBearingRow
    from ._2024 import LoadedNonBarrelRollerBearingStripLoadResults
    from ._2025 import LoadedNonBarrelRollerElement
    from ._2026 import LoadedRollerBearingElement
    from ._2027 import LoadedRollerBearingResults
    from ._2028 import LoadedRollerBearingRow
    from ._2029 import LoadedRollerStripLoadResults
    from ._2030 import LoadedRollingBearingRaceResults
    from ._2031 import LoadedRollingBearingResults
    from ._2032 import LoadedRollingBearingRow
    from ._2033 import LoadedSelfAligningBallBearingElement
    from ._2034 import LoadedSelfAligningBallBearingResults
    from ._2035 import LoadedSelfAligningBallBearingRow
    from ._2036 import LoadedSphericalRadialRollerBearingElement
    from ._2037 import LoadedSphericalRollerBearingElement
    from ._2038 import LoadedSphericalRollerRadialBearingResults
    from ._2039 import LoadedSphericalRollerRadialBearingRow
    from ._2040 import LoadedSphericalRollerRadialBearingStripLoadResults
    from ._2041 import LoadedSphericalRollerThrustBearingResults
    from ._2042 import LoadedSphericalRollerThrustBearingRow
    from ._2043 import LoadedSphericalThrustRollerBearingElement
    from ._2044 import LoadedTaperRollerBearingDutyCycle
    from ._2045 import LoadedTaperRollerBearingElement
    from ._2046 import LoadedTaperRollerBearingResults
    from ._2047 import LoadedTaperRollerBearingRow
    from ._2048 import LoadedThreePointContactBallBearingElement
    from ._2049 import LoadedThreePointContactBallBearingResults
    from ._2050 import LoadedThreePointContactBallBearingRow
    from ._2051 import LoadedThrustBallBearingElement
    from ._2052 import LoadedThrustBallBearingResults
    from ._2053 import LoadedThrustBallBearingRow
    from ._2054 import LoadedToroidalRollerBearingElement
    from ._2055 import LoadedToroidalRollerBearingResults
    from ._2056 import LoadedToroidalRollerBearingRow
    from ._2057 import LoadedToroidalRollerBearingStripLoadResults
    from ._2058 import MaximumStaticContactStress
    from ._2059 import MaximumStaticContactStressDutyCycle
    from ._2060 import MaximumStaticContactStressResultsAbstract
    from ._2061 import MaxStripLoadStressObject
    from ._2062 import PermissibleContinuousAxialLoadResults
    from ._2063 import PowerRatingF1EstimationMethod
    from ._2064 import PreloadFactorLookupTable
    from ._2065 import ResultsAtRollerOffset
    from ._2066 import RingForceAndDisplacement
    from ._2067 import RollerAnalysisMethod
    from ._2068 import RollingBearingFrictionCoefficients
    from ._2069 import RollingBearingSpeedResults
    from ._2070 import SMTRibStressResults
    from ._2071 import StressAtPosition
    from ._2072 import ThreePointContactInternalClearance
    from ._2073 import TrackTruncationSafetyFactorResults
else:
    import_structure = {
        "_1964": ["BallBearingAnalysisMethod"],
        "_1965": ["BallBearingContactCalculation"],
        "_1966": ["BallBearingRaceContactGeometry"],
        "_1967": ["DIN7322010Results"],
        "_1968": ["ForceAtLaminaGroupReportable"],
        "_1969": ["ForceAtLaminaReportable"],
        "_1970": ["FrictionModelForGyroscopicMoment"],
        "_1971": ["InternalClearance"],
        "_1972": ["ISO14179Settings"],
        "_1973": ["ISO14179SettingsDatabase"],
        "_1974": ["ISO14179SettingsPerBearingType"],
        "_1975": ["ISO153122018Results"],
        "_1976": ["ISOTR1417912001Results"],
        "_1977": ["ISOTR141792001Results"],
        "_1978": ["ISOTR1417922001Results"],
        "_1979": ["LoadedAbstractSphericalRollerBearingStripLoadResults"],
        "_1980": ["LoadedAngularContactBallBearingElement"],
        "_1981": ["LoadedAngularContactBallBearingResults"],
        "_1982": ["LoadedAngularContactBallBearingRow"],
        "_1983": ["LoadedAngularContactThrustBallBearingElement"],
        "_1984": ["LoadedAngularContactThrustBallBearingResults"],
        "_1985": ["LoadedAngularContactThrustBallBearingRow"],
        "_1986": ["LoadedAsymmetricSphericalRollerBearingElement"],
        "_1987": ["LoadedAsymmetricSphericalRollerBearingResults"],
        "_1988": ["LoadedAsymmetricSphericalRollerBearingRow"],
        "_1989": ["LoadedAsymmetricSphericalRollerBearingStripLoadResults"],
        "_1990": ["LoadedAxialThrustCylindricalRollerBearingDutyCycle"],
        "_1991": ["LoadedAxialThrustCylindricalRollerBearingElement"],
        "_1992": ["LoadedAxialThrustCylindricalRollerBearingResults"],
        "_1993": ["LoadedAxialThrustCylindricalRollerBearingRow"],
        "_1994": ["LoadedAxialThrustNeedleRollerBearingElement"],
        "_1995": ["LoadedAxialThrustNeedleRollerBearingResults"],
        "_1996": ["LoadedAxialThrustNeedleRollerBearingRow"],
        "_1997": ["LoadedBallBearingDutyCycle"],
        "_1998": ["LoadedBallBearingElement"],
        "_1999": ["LoadedBallBearingRaceResults"],
        "_2000": ["LoadedBallBearingResults"],
        "_2001": ["LoadedBallBearingRow"],
        "_2002": ["LoadedCrossedRollerBearingElement"],
        "_2003": ["LoadedCrossedRollerBearingResults"],
        "_2004": ["LoadedCrossedRollerBearingRow"],
        "_2005": ["LoadedCylindricalRollerBearingDutyCycle"],
        "_2006": ["LoadedCylindricalRollerBearingElement"],
        "_2007": ["LoadedCylindricalRollerBearingResults"],
        "_2008": ["LoadedCylindricalRollerBearingRow"],
        "_2009": ["LoadedDeepGrooveBallBearingElement"],
        "_2010": ["LoadedDeepGrooveBallBearingResults"],
        "_2011": ["LoadedDeepGrooveBallBearingRow"],
        "_2012": ["LoadedElement"],
        "_2013": ["LoadedFourPointContactBallBearingElement"],
        "_2014": ["LoadedFourPointContactBallBearingRaceResults"],
        "_2015": ["LoadedFourPointContactBallBearingResults"],
        "_2016": ["LoadedFourPointContactBallBearingRow"],
        "_2017": ["LoadedMultiPointContactBallBearingElement"],
        "_2018": ["LoadedNeedleRollerBearingElement"],
        "_2019": ["LoadedNeedleRollerBearingResults"],
        "_2020": ["LoadedNeedleRollerBearingRow"],
        "_2021": ["LoadedNonBarrelRollerBearingDutyCycle"],
        "_2022": ["LoadedNonBarrelRollerBearingResults"],
        "_2023": ["LoadedNonBarrelRollerBearingRow"],
        "_2024": ["LoadedNonBarrelRollerBearingStripLoadResults"],
        "_2025": ["LoadedNonBarrelRollerElement"],
        "_2026": ["LoadedRollerBearingElement"],
        "_2027": ["LoadedRollerBearingResults"],
        "_2028": ["LoadedRollerBearingRow"],
        "_2029": ["LoadedRollerStripLoadResults"],
        "_2030": ["LoadedRollingBearingRaceResults"],
        "_2031": ["LoadedRollingBearingResults"],
        "_2032": ["LoadedRollingBearingRow"],
        "_2033": ["LoadedSelfAligningBallBearingElement"],
        "_2034": ["LoadedSelfAligningBallBearingResults"],
        "_2035": ["LoadedSelfAligningBallBearingRow"],
        "_2036": ["LoadedSphericalRadialRollerBearingElement"],
        "_2037": ["LoadedSphericalRollerBearingElement"],
        "_2038": ["LoadedSphericalRollerRadialBearingResults"],
        "_2039": ["LoadedSphericalRollerRadialBearingRow"],
        "_2040": ["LoadedSphericalRollerRadialBearingStripLoadResults"],
        "_2041": ["LoadedSphericalRollerThrustBearingResults"],
        "_2042": ["LoadedSphericalRollerThrustBearingRow"],
        "_2043": ["LoadedSphericalThrustRollerBearingElement"],
        "_2044": ["LoadedTaperRollerBearingDutyCycle"],
        "_2045": ["LoadedTaperRollerBearingElement"],
        "_2046": ["LoadedTaperRollerBearingResults"],
        "_2047": ["LoadedTaperRollerBearingRow"],
        "_2048": ["LoadedThreePointContactBallBearingElement"],
        "_2049": ["LoadedThreePointContactBallBearingResults"],
        "_2050": ["LoadedThreePointContactBallBearingRow"],
        "_2051": ["LoadedThrustBallBearingElement"],
        "_2052": ["LoadedThrustBallBearingResults"],
        "_2053": ["LoadedThrustBallBearingRow"],
        "_2054": ["LoadedToroidalRollerBearingElement"],
        "_2055": ["LoadedToroidalRollerBearingResults"],
        "_2056": ["LoadedToroidalRollerBearingRow"],
        "_2057": ["LoadedToroidalRollerBearingStripLoadResults"],
        "_2058": ["MaximumStaticContactStress"],
        "_2059": ["MaximumStaticContactStressDutyCycle"],
        "_2060": ["MaximumStaticContactStressResultsAbstract"],
        "_2061": ["MaxStripLoadStressObject"],
        "_2062": ["PermissibleContinuousAxialLoadResults"],
        "_2063": ["PowerRatingF1EstimationMethod"],
        "_2064": ["PreloadFactorLookupTable"],
        "_2065": ["ResultsAtRollerOffset"],
        "_2066": ["RingForceAndDisplacement"],
        "_2067": ["RollerAnalysisMethod"],
        "_2068": ["RollingBearingFrictionCoefficients"],
        "_2069": ["RollingBearingSpeedResults"],
        "_2070": ["SMTRibStressResults"],
        "_2071": ["StressAtPosition"],
        "_2072": ["ThreePointContactInternalClearance"],
        "_2073": ["TrackTruncationSafetyFactorResults"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BallBearingAnalysisMethod",
    "BallBearingContactCalculation",
    "BallBearingRaceContactGeometry",
    "DIN7322010Results",
    "ForceAtLaminaGroupReportable",
    "ForceAtLaminaReportable",
    "FrictionModelForGyroscopicMoment",
    "InternalClearance",
    "ISO14179Settings",
    "ISO14179SettingsDatabase",
    "ISO14179SettingsPerBearingType",
    "ISO153122018Results",
    "ISOTR1417912001Results",
    "ISOTR141792001Results",
    "ISOTR1417922001Results",
    "LoadedAbstractSphericalRollerBearingStripLoadResults",
    "LoadedAngularContactBallBearingElement",
    "LoadedAngularContactBallBearingResults",
    "LoadedAngularContactBallBearingRow",
    "LoadedAngularContactThrustBallBearingElement",
    "LoadedAngularContactThrustBallBearingResults",
    "LoadedAngularContactThrustBallBearingRow",
    "LoadedAsymmetricSphericalRollerBearingElement",
    "LoadedAsymmetricSphericalRollerBearingResults",
    "LoadedAsymmetricSphericalRollerBearingRow",
    "LoadedAsymmetricSphericalRollerBearingStripLoadResults",
    "LoadedAxialThrustCylindricalRollerBearingDutyCycle",
    "LoadedAxialThrustCylindricalRollerBearingElement",
    "LoadedAxialThrustCylindricalRollerBearingResults",
    "LoadedAxialThrustCylindricalRollerBearingRow",
    "LoadedAxialThrustNeedleRollerBearingElement",
    "LoadedAxialThrustNeedleRollerBearingResults",
    "LoadedAxialThrustNeedleRollerBearingRow",
    "LoadedBallBearingDutyCycle",
    "LoadedBallBearingElement",
    "LoadedBallBearingRaceResults",
    "LoadedBallBearingResults",
    "LoadedBallBearingRow",
    "LoadedCrossedRollerBearingElement",
    "LoadedCrossedRollerBearingResults",
    "LoadedCrossedRollerBearingRow",
    "LoadedCylindricalRollerBearingDutyCycle",
    "LoadedCylindricalRollerBearingElement",
    "LoadedCylindricalRollerBearingResults",
    "LoadedCylindricalRollerBearingRow",
    "LoadedDeepGrooveBallBearingElement",
    "LoadedDeepGrooveBallBearingResults",
    "LoadedDeepGrooveBallBearingRow",
    "LoadedElement",
    "LoadedFourPointContactBallBearingElement",
    "LoadedFourPointContactBallBearingRaceResults",
    "LoadedFourPointContactBallBearingResults",
    "LoadedFourPointContactBallBearingRow",
    "LoadedMultiPointContactBallBearingElement",
    "LoadedNeedleRollerBearingElement",
    "LoadedNeedleRollerBearingResults",
    "LoadedNeedleRollerBearingRow",
    "LoadedNonBarrelRollerBearingDutyCycle",
    "LoadedNonBarrelRollerBearingResults",
    "LoadedNonBarrelRollerBearingRow",
    "LoadedNonBarrelRollerBearingStripLoadResults",
    "LoadedNonBarrelRollerElement",
    "LoadedRollerBearingElement",
    "LoadedRollerBearingResults",
    "LoadedRollerBearingRow",
    "LoadedRollerStripLoadResults",
    "LoadedRollingBearingRaceResults",
    "LoadedRollingBearingResults",
    "LoadedRollingBearingRow",
    "LoadedSelfAligningBallBearingElement",
    "LoadedSelfAligningBallBearingResults",
    "LoadedSelfAligningBallBearingRow",
    "LoadedSphericalRadialRollerBearingElement",
    "LoadedSphericalRollerBearingElement",
    "LoadedSphericalRollerRadialBearingResults",
    "LoadedSphericalRollerRadialBearingRow",
    "LoadedSphericalRollerRadialBearingStripLoadResults",
    "LoadedSphericalRollerThrustBearingResults",
    "LoadedSphericalRollerThrustBearingRow",
    "LoadedSphericalThrustRollerBearingElement",
    "LoadedTaperRollerBearingDutyCycle",
    "LoadedTaperRollerBearingElement",
    "LoadedTaperRollerBearingResults",
    "LoadedTaperRollerBearingRow",
    "LoadedThreePointContactBallBearingElement",
    "LoadedThreePointContactBallBearingResults",
    "LoadedThreePointContactBallBearingRow",
    "LoadedThrustBallBearingElement",
    "LoadedThrustBallBearingResults",
    "LoadedThrustBallBearingRow",
    "LoadedToroidalRollerBearingElement",
    "LoadedToroidalRollerBearingResults",
    "LoadedToroidalRollerBearingRow",
    "LoadedToroidalRollerBearingStripLoadResults",
    "MaximumStaticContactStress",
    "MaximumStaticContactStressDutyCycle",
    "MaximumStaticContactStressResultsAbstract",
    "MaxStripLoadStressObject",
    "PermissibleContinuousAxialLoadResults",
    "PowerRatingF1EstimationMethod",
    "PreloadFactorLookupTable",
    "ResultsAtRollerOffset",
    "RingForceAndDisplacement",
    "RollerAnalysisMethod",
    "RollingBearingFrictionCoefficients",
    "RollingBearingSpeedResults",
    "SMTRibStressResults",
    "StressAtPosition",
    "ThreePointContactInternalClearance",
    "TrackTruncationSafetyFactorResults",
)
