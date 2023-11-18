"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2133 import AngularContactBallBearing
    from ._2134 import AngularContactThrustBallBearing
    from ._2135 import AsymmetricSphericalRollerBearing
    from ._2136 import AxialThrustCylindricalRollerBearing
    from ._2137 import AxialThrustNeedleRollerBearing
    from ._2138 import BallBearing
    from ._2139 import BallBearingShoulderDefinition
    from ._2140 import BarrelRollerBearing
    from ._2141 import BearingProtection
    from ._2142 import BearingProtectionDetailsModifier
    from ._2143 import BearingProtectionLevel
    from ._2144 import BearingTypeExtraInformation
    from ._2145 import CageBridgeShape
    from ._2146 import CrossedRollerBearing
    from ._2147 import CylindricalRollerBearing
    from ._2148 import DeepGrooveBallBearing
    from ._2149 import DiameterSeries
    from ._2150 import FatigueLoadLimitCalculationMethodEnum
    from ._2151 import FourPointContactAngleDefinition
    from ._2152 import FourPointContactBallBearing
    from ._2153 import GeometricConstants
    from ._2154 import GeometricConstantsForRollingFrictionalMoments
    from ._2155 import GeometricConstantsForSlidingFrictionalMoments
    from ._2156 import HeightSeries
    from ._2157 import MultiPointContactBallBearing
    from ._2158 import NeedleRollerBearing
    from ._2159 import NonBarrelRollerBearing
    from ._2160 import RollerBearing
    from ._2161 import RollerEndShape
    from ._2162 import RollerRibDetail
    from ._2163 import RollingBearing
    from ._2164 import SelfAligningBallBearing
    from ._2165 import SKFSealFrictionalMomentConstants
    from ._2166 import SleeveType
    from ._2167 import SphericalRollerBearing
    from ._2168 import SphericalRollerThrustBearing
    from ._2169 import TaperRollerBearing
    from ._2170 import ThreePointContactBallBearing
    from ._2171 import ThrustBallBearing
    from ._2172 import ToroidalRollerBearing
    from ._2173 import WidthSeries
else:
    import_structure = {
        "_2133": ["AngularContactBallBearing"],
        "_2134": ["AngularContactThrustBallBearing"],
        "_2135": ["AsymmetricSphericalRollerBearing"],
        "_2136": ["AxialThrustCylindricalRollerBearing"],
        "_2137": ["AxialThrustNeedleRollerBearing"],
        "_2138": ["BallBearing"],
        "_2139": ["BallBearingShoulderDefinition"],
        "_2140": ["BarrelRollerBearing"],
        "_2141": ["BearingProtection"],
        "_2142": ["BearingProtectionDetailsModifier"],
        "_2143": ["BearingProtectionLevel"],
        "_2144": ["BearingTypeExtraInformation"],
        "_2145": ["CageBridgeShape"],
        "_2146": ["CrossedRollerBearing"],
        "_2147": ["CylindricalRollerBearing"],
        "_2148": ["DeepGrooveBallBearing"],
        "_2149": ["DiameterSeries"],
        "_2150": ["FatigueLoadLimitCalculationMethodEnum"],
        "_2151": ["FourPointContactAngleDefinition"],
        "_2152": ["FourPointContactBallBearing"],
        "_2153": ["GeometricConstants"],
        "_2154": ["GeometricConstantsForRollingFrictionalMoments"],
        "_2155": ["GeometricConstantsForSlidingFrictionalMoments"],
        "_2156": ["HeightSeries"],
        "_2157": ["MultiPointContactBallBearing"],
        "_2158": ["NeedleRollerBearing"],
        "_2159": ["NonBarrelRollerBearing"],
        "_2160": ["RollerBearing"],
        "_2161": ["RollerEndShape"],
        "_2162": ["RollerRibDetail"],
        "_2163": ["RollingBearing"],
        "_2164": ["SelfAligningBallBearing"],
        "_2165": ["SKFSealFrictionalMomentConstants"],
        "_2166": ["SleeveType"],
        "_2167": ["SphericalRollerBearing"],
        "_2168": ["SphericalRollerThrustBearing"],
        "_2169": ["TaperRollerBearing"],
        "_2170": ["ThreePointContactBallBearing"],
        "_2171": ["ThrustBallBearing"],
        "_2172": ["ToroidalRollerBearing"],
        "_2173": ["WidthSeries"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AngularContactBallBearing",
    "AngularContactThrustBallBearing",
    "AsymmetricSphericalRollerBearing",
    "AxialThrustCylindricalRollerBearing",
    "AxialThrustNeedleRollerBearing",
    "BallBearing",
    "BallBearingShoulderDefinition",
    "BarrelRollerBearing",
    "BearingProtection",
    "BearingProtectionDetailsModifier",
    "BearingProtectionLevel",
    "BearingTypeExtraInformation",
    "CageBridgeShape",
    "CrossedRollerBearing",
    "CylindricalRollerBearing",
    "DeepGrooveBallBearing",
    "DiameterSeries",
    "FatigueLoadLimitCalculationMethodEnum",
    "FourPointContactAngleDefinition",
    "FourPointContactBallBearing",
    "GeometricConstants",
    "GeometricConstantsForRollingFrictionalMoments",
    "GeometricConstantsForSlidingFrictionalMoments",
    "HeightSeries",
    "MultiPointContactBallBearing",
    "NeedleRollerBearing",
    "NonBarrelRollerBearing",
    "RollerBearing",
    "RollerEndShape",
    "RollerRibDetail",
    "RollingBearing",
    "SelfAligningBallBearing",
    "SKFSealFrictionalMomentConstants",
    "SleeveType",
    "SphericalRollerBearing",
    "SphericalRollerThrustBearing",
    "TaperRollerBearing",
    "ThreePointContactBallBearing",
    "ThrustBallBearing",
    "ToroidalRollerBearing",
    "WidthSeries",
)
