"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1386 import CustomSplineHalfDesign
    from ._1387 import CustomSplineJointDesign
    from ._1388 import DetailedSplineJointSettings
    from ._1389 import DIN5480SplineHalfDesign
    from ._1390 import DIN5480SplineJointDesign
    from ._1391 import DudleyEffectiveLengthApproximationOption
    from ._1392 import FitTypes
    from ._1393 import GBT3478SplineHalfDesign
    from ._1394 import GBT3478SplineJointDesign
    from ._1395 import HeatTreatmentTypes
    from ._1396 import ISO4156SplineHalfDesign
    from ._1397 import ISO4156SplineJointDesign
    from ._1398 import JISB1603SplineJointDesign
    from ._1399 import ManufacturingTypes
    from ._1400 import Modules
    from ._1401 import PressureAngleTypes
    from ._1402 import RootTypes
    from ._1403 import SAEFatigueLifeFactorTypes
    from ._1404 import SAESplineHalfDesign
    from ._1405 import SAESplineJointDesign
    from ._1406 import SAETorqueCycles
    from ._1407 import SplineDesignTypes
    from ._1408 import FinishingMethods
    from ._1409 import SplineFitClassType
    from ._1410 import SplineFixtureTypes
    from ._1411 import SplineHalfDesign
    from ._1412 import SplineJointDesign
    from ._1413 import SplineMaterial
    from ._1414 import SplineRatingTypes
    from ._1415 import SplineToleranceClassTypes
    from ._1416 import StandardSplineHalfDesign
    from ._1417 import StandardSplineJointDesign
else:
    import_structure = {
        "_1386": ["CustomSplineHalfDesign"],
        "_1387": ["CustomSplineJointDesign"],
        "_1388": ["DetailedSplineJointSettings"],
        "_1389": ["DIN5480SplineHalfDesign"],
        "_1390": ["DIN5480SplineJointDesign"],
        "_1391": ["DudleyEffectiveLengthApproximationOption"],
        "_1392": ["FitTypes"],
        "_1393": ["GBT3478SplineHalfDesign"],
        "_1394": ["GBT3478SplineJointDesign"],
        "_1395": ["HeatTreatmentTypes"],
        "_1396": ["ISO4156SplineHalfDesign"],
        "_1397": ["ISO4156SplineJointDesign"],
        "_1398": ["JISB1603SplineJointDesign"],
        "_1399": ["ManufacturingTypes"],
        "_1400": ["Modules"],
        "_1401": ["PressureAngleTypes"],
        "_1402": ["RootTypes"],
        "_1403": ["SAEFatigueLifeFactorTypes"],
        "_1404": ["SAESplineHalfDesign"],
        "_1405": ["SAESplineJointDesign"],
        "_1406": ["SAETorqueCycles"],
        "_1407": ["SplineDesignTypes"],
        "_1408": ["FinishingMethods"],
        "_1409": ["SplineFitClassType"],
        "_1410": ["SplineFixtureTypes"],
        "_1411": ["SplineHalfDesign"],
        "_1412": ["SplineJointDesign"],
        "_1413": ["SplineMaterial"],
        "_1414": ["SplineRatingTypes"],
        "_1415": ["SplineToleranceClassTypes"],
        "_1416": ["StandardSplineHalfDesign"],
        "_1417": ["StandardSplineJointDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CustomSplineHalfDesign",
    "CustomSplineJointDesign",
    "DetailedSplineJointSettings",
    "DIN5480SplineHalfDesign",
    "DIN5480SplineJointDesign",
    "DudleyEffectiveLengthApproximationOption",
    "FitTypes",
    "GBT3478SplineHalfDesign",
    "GBT3478SplineJointDesign",
    "HeatTreatmentTypes",
    "ISO4156SplineHalfDesign",
    "ISO4156SplineJointDesign",
    "JISB1603SplineJointDesign",
    "ManufacturingTypes",
    "Modules",
    "PressureAngleTypes",
    "RootTypes",
    "SAEFatigueLifeFactorTypes",
    "SAESplineHalfDesign",
    "SAESplineJointDesign",
    "SAETorqueCycles",
    "SplineDesignTypes",
    "FinishingMethods",
    "SplineFitClassType",
    "SplineFixtureTypes",
    "SplineHalfDesign",
    "SplineJointDesign",
    "SplineMaterial",
    "SplineRatingTypes",
    "SplineToleranceClassTypes",
    "StandardSplineHalfDesign",
    "StandardSplineJointDesign",
)
