"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1462 import AxialLoadType
    from ._1463 import BoltedJointMaterial
    from ._1464 import BoltedJointMaterialDatabase
    from ._1465 import BoltGeometry
    from ._1466 import BoltGeometryDatabase
    from ._1467 import BoltMaterial
    from ._1468 import BoltMaterialDatabase
    from ._1469 import BoltSection
    from ._1470 import BoltShankType
    from ._1471 import BoltTypes
    from ._1472 import ClampedSection
    from ._1473 import ClampedSectionMaterialDatabase
    from ._1474 import DetailedBoltDesign
    from ._1475 import DetailedBoltedJointDesign
    from ._1476 import HeadCapTypes
    from ._1477 import JointGeometries
    from ._1478 import JointTypes
    from ._1479 import LoadedBolt
    from ._1480 import RolledBeforeOrAfterHeatTreatment
    from ._1481 import StandardSizes
    from ._1482 import StrengthGrades
    from ._1483 import ThreadTypes
    from ._1484 import TighteningTechniques
else:
    import_structure = {
        "_1462": ["AxialLoadType"],
        "_1463": ["BoltedJointMaterial"],
        "_1464": ["BoltedJointMaterialDatabase"],
        "_1465": ["BoltGeometry"],
        "_1466": ["BoltGeometryDatabase"],
        "_1467": ["BoltMaterial"],
        "_1468": ["BoltMaterialDatabase"],
        "_1469": ["BoltSection"],
        "_1470": ["BoltShankType"],
        "_1471": ["BoltTypes"],
        "_1472": ["ClampedSection"],
        "_1473": ["ClampedSectionMaterialDatabase"],
        "_1474": ["DetailedBoltDesign"],
        "_1475": ["DetailedBoltedJointDesign"],
        "_1476": ["HeadCapTypes"],
        "_1477": ["JointGeometries"],
        "_1478": ["JointTypes"],
        "_1479": ["LoadedBolt"],
        "_1480": ["RolledBeforeOrAfterHeatTreatment"],
        "_1481": ["StandardSizes"],
        "_1482": ["StrengthGrades"],
        "_1483": ["ThreadTypes"],
        "_1484": ["TighteningTechniques"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AxialLoadType",
    "BoltedJointMaterial",
    "BoltedJointMaterialDatabase",
    "BoltGeometry",
    "BoltGeometryDatabase",
    "BoltMaterial",
    "BoltMaterialDatabase",
    "BoltSection",
    "BoltShankType",
    "BoltTypes",
    "ClampedSection",
    "ClampedSectionMaterialDatabase",
    "DetailedBoltDesign",
    "DetailedBoltedJointDesign",
    "HeadCapTypes",
    "JointGeometries",
    "JointTypes",
    "LoadedBolt",
    "RolledBeforeOrAfterHeatTreatment",
    "StandardSizes",
    "StrengthGrades",
    "ThreadTypes",
    "TighteningTechniques",
)
