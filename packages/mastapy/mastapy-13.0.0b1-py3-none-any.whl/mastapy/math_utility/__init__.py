"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1486 import Range
    from ._1487 import AcousticWeighting
    from ._1488 import AlignmentAxis
    from ._1489 import Axis
    from ._1490 import CirclesOnAxis
    from ._1491 import ComplexMatrix
    from ._1492 import ComplexPartDisplayOption
    from ._1493 import ComplexVector
    from ._1494 import ComplexVector3D
    from ._1495 import ComplexVector6D
    from ._1496 import CoordinateSystem3D
    from ._1497 import CoordinateSystemEditor
    from ._1498 import CoordinateSystemForRotation
    from ._1499 import CoordinateSystemForRotationOrigin
    from ._1500 import DataPrecision
    from ._1501 import DegreeOfFreedom
    from ._1502 import DynamicsResponseScalarResult
    from ._1503 import DynamicsResponseScaling
    from ._1504 import Eigenmode
    from ._1505 import Eigenmodes
    from ._1506 import EulerParameters
    from ._1507 import ExtrapolationOptions
    from ._1508 import FacetedBody
    from ._1509 import FacetedSurface
    from ._1510 import FourierSeries
    from ._1511 import GenericMatrix
    from ._1512 import GriddedSurface
    from ._1513 import HarmonicValue
    from ._1514 import InertiaTensor
    from ._1515 import MassProperties
    from ._1516 import MaxMinMean
    from ._1517 import ComplexMagnitudeMethod
    from ._1518 import MultipleFourierSeriesInterpolator
    from ._1519 import Named2DLocation
    from ._1520 import PIDControlUpdateMethod
    from ._1521 import Quaternion
    from ._1522 import RealMatrix
    from ._1523 import RealVector
    from ._1524 import ResultOptionsFor3DVector
    from ._1525 import RotationAxis
    from ._1526 import RoundedOrder
    from ._1527 import SinCurve
    from ._1528 import SquareMatrix
    from ._1529 import StressPoint
    from ._1530 import TransformMatrix3D
    from ._1531 import TranslationRotation
    from ._1532 import Vector2DListAccessor
    from ._1533 import Vector6D
else:
    import_structure = {
        "_1486": ["Range"],
        "_1487": ["AcousticWeighting"],
        "_1488": ["AlignmentAxis"],
        "_1489": ["Axis"],
        "_1490": ["CirclesOnAxis"],
        "_1491": ["ComplexMatrix"],
        "_1492": ["ComplexPartDisplayOption"],
        "_1493": ["ComplexVector"],
        "_1494": ["ComplexVector3D"],
        "_1495": ["ComplexVector6D"],
        "_1496": ["CoordinateSystem3D"],
        "_1497": ["CoordinateSystemEditor"],
        "_1498": ["CoordinateSystemForRotation"],
        "_1499": ["CoordinateSystemForRotationOrigin"],
        "_1500": ["DataPrecision"],
        "_1501": ["DegreeOfFreedom"],
        "_1502": ["DynamicsResponseScalarResult"],
        "_1503": ["DynamicsResponseScaling"],
        "_1504": ["Eigenmode"],
        "_1505": ["Eigenmodes"],
        "_1506": ["EulerParameters"],
        "_1507": ["ExtrapolationOptions"],
        "_1508": ["FacetedBody"],
        "_1509": ["FacetedSurface"],
        "_1510": ["FourierSeries"],
        "_1511": ["GenericMatrix"],
        "_1512": ["GriddedSurface"],
        "_1513": ["HarmonicValue"],
        "_1514": ["InertiaTensor"],
        "_1515": ["MassProperties"],
        "_1516": ["MaxMinMean"],
        "_1517": ["ComplexMagnitudeMethod"],
        "_1518": ["MultipleFourierSeriesInterpolator"],
        "_1519": ["Named2DLocation"],
        "_1520": ["PIDControlUpdateMethod"],
        "_1521": ["Quaternion"],
        "_1522": ["RealMatrix"],
        "_1523": ["RealVector"],
        "_1524": ["ResultOptionsFor3DVector"],
        "_1525": ["RotationAxis"],
        "_1526": ["RoundedOrder"],
        "_1527": ["SinCurve"],
        "_1528": ["SquareMatrix"],
        "_1529": ["StressPoint"],
        "_1530": ["TransformMatrix3D"],
        "_1531": ["TranslationRotation"],
        "_1532": ["Vector2DListAccessor"],
        "_1533": ["Vector6D"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Range",
    "AcousticWeighting",
    "AlignmentAxis",
    "Axis",
    "CirclesOnAxis",
    "ComplexMatrix",
    "ComplexPartDisplayOption",
    "ComplexVector",
    "ComplexVector3D",
    "ComplexVector6D",
    "CoordinateSystem3D",
    "CoordinateSystemEditor",
    "CoordinateSystemForRotation",
    "CoordinateSystemForRotationOrigin",
    "DataPrecision",
    "DegreeOfFreedom",
    "DynamicsResponseScalarResult",
    "DynamicsResponseScaling",
    "Eigenmode",
    "Eigenmodes",
    "EulerParameters",
    "ExtrapolationOptions",
    "FacetedBody",
    "FacetedSurface",
    "FourierSeries",
    "GenericMatrix",
    "GriddedSurface",
    "HarmonicValue",
    "InertiaTensor",
    "MassProperties",
    "MaxMinMean",
    "ComplexMagnitudeMethod",
    "MultipleFourierSeriesInterpolator",
    "Named2DLocation",
    "PIDControlUpdateMethod",
    "Quaternion",
    "RealMatrix",
    "RealVector",
    "ResultOptionsFor3DVector",
    "RotationAxis",
    "RoundedOrder",
    "SinCurve",
    "SquareMatrix",
    "StressPoint",
    "TransformMatrix3D",
    "TranslationRotation",
    "Vector2DListAccessor",
    "Vector6D",
)
