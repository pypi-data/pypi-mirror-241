"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1091 import CylindricalGearBiasModification
    from ._1092 import CylindricalGearCommonFlankMicroGeometry
    from ._1093 import CylindricalGearFlankMicroGeometry
    from ._1094 import CylindricalGearLeadModification
    from ._1095 import CylindricalGearLeadModificationAtProfilePosition
    from ._1096 import CylindricalGearMeshMicroGeometry
    from ._1097 import CylindricalGearMeshMicroGeometryDutyCycle
    from ._1098 import CylindricalGearMicroGeometry
    from ._1099 import CylindricalGearMicroGeometryBase
    from ._1100 import CylindricalGearMicroGeometryDutyCycle
    from ._1101 import CylindricalGearMicroGeometryMap
    from ._1102 import CylindricalGearMicroGeometryPerTooth
    from ._1103 import CylindricalGearProfileModification
    from ._1104 import CylindricalGearProfileModificationAtFaceWidthPosition
    from ._1105 import CylindricalGearSetMicroGeometry
    from ._1106 import CylindricalGearSetMicroGeometryDutyCycle
    from ._1107 import CylindricalGearToothMicroGeometry
    from ._1108 import CylindricalGearTriangularEndModification
    from ._1109 import CylindricalGearTriangularEndModificationAtOrientation
    from ._1110 import DrawDefiningGearOrBoth
    from ._1111 import GearAlignment
    from ._1112 import LeadFormReliefWithDeviation
    from ._1113 import LeadReliefWithDeviation
    from ._1114 import LeadSlopeReliefWithDeviation
    from ._1115 import LinearCylindricalGearTriangularEndModification
    from ._1116 import MeasuredMapDataTypes
    from ._1117 import MeshAlignment
    from ._1118 import MeshedCylindricalGearFlankMicroGeometry
    from ._1119 import MeshedCylindricalGearMicroGeometry
    from ._1120 import MicroGeometryLeadToleranceChartView
    from ._1121 import MicroGeometryViewingOptions
    from ._1122 import ParabolicCylindricalGearTriangularEndModification
    from ._1123 import ProfileFormReliefWithDeviation
    from ._1124 import ProfileReliefWithDeviation
    from ._1125 import ProfileSlopeReliefWithDeviation
    from ._1126 import ReliefWithDeviation
    from ._1127 import SingleCylindricalGearTriangularEndModification
    from ._1128 import TotalLeadReliefWithDeviation
    from ._1129 import TotalProfileReliefWithDeviation
else:
    import_structure = {
        "_1091": ["CylindricalGearBiasModification"],
        "_1092": ["CylindricalGearCommonFlankMicroGeometry"],
        "_1093": ["CylindricalGearFlankMicroGeometry"],
        "_1094": ["CylindricalGearLeadModification"],
        "_1095": ["CylindricalGearLeadModificationAtProfilePosition"],
        "_1096": ["CylindricalGearMeshMicroGeometry"],
        "_1097": ["CylindricalGearMeshMicroGeometryDutyCycle"],
        "_1098": ["CylindricalGearMicroGeometry"],
        "_1099": ["CylindricalGearMicroGeometryBase"],
        "_1100": ["CylindricalGearMicroGeometryDutyCycle"],
        "_1101": ["CylindricalGearMicroGeometryMap"],
        "_1102": ["CylindricalGearMicroGeometryPerTooth"],
        "_1103": ["CylindricalGearProfileModification"],
        "_1104": ["CylindricalGearProfileModificationAtFaceWidthPosition"],
        "_1105": ["CylindricalGearSetMicroGeometry"],
        "_1106": ["CylindricalGearSetMicroGeometryDutyCycle"],
        "_1107": ["CylindricalGearToothMicroGeometry"],
        "_1108": ["CylindricalGearTriangularEndModification"],
        "_1109": ["CylindricalGearTriangularEndModificationAtOrientation"],
        "_1110": ["DrawDefiningGearOrBoth"],
        "_1111": ["GearAlignment"],
        "_1112": ["LeadFormReliefWithDeviation"],
        "_1113": ["LeadReliefWithDeviation"],
        "_1114": ["LeadSlopeReliefWithDeviation"],
        "_1115": ["LinearCylindricalGearTriangularEndModification"],
        "_1116": ["MeasuredMapDataTypes"],
        "_1117": ["MeshAlignment"],
        "_1118": ["MeshedCylindricalGearFlankMicroGeometry"],
        "_1119": ["MeshedCylindricalGearMicroGeometry"],
        "_1120": ["MicroGeometryLeadToleranceChartView"],
        "_1121": ["MicroGeometryViewingOptions"],
        "_1122": ["ParabolicCylindricalGearTriangularEndModification"],
        "_1123": ["ProfileFormReliefWithDeviation"],
        "_1124": ["ProfileReliefWithDeviation"],
        "_1125": ["ProfileSlopeReliefWithDeviation"],
        "_1126": ["ReliefWithDeviation"],
        "_1127": ["SingleCylindricalGearTriangularEndModification"],
        "_1128": ["TotalLeadReliefWithDeviation"],
        "_1129": ["TotalProfileReliefWithDeviation"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearBiasModification",
    "CylindricalGearCommonFlankMicroGeometry",
    "CylindricalGearFlankMicroGeometry",
    "CylindricalGearLeadModification",
    "CylindricalGearLeadModificationAtProfilePosition",
    "CylindricalGearMeshMicroGeometry",
    "CylindricalGearMeshMicroGeometryDutyCycle",
    "CylindricalGearMicroGeometry",
    "CylindricalGearMicroGeometryBase",
    "CylindricalGearMicroGeometryDutyCycle",
    "CylindricalGearMicroGeometryMap",
    "CylindricalGearMicroGeometryPerTooth",
    "CylindricalGearProfileModification",
    "CylindricalGearProfileModificationAtFaceWidthPosition",
    "CylindricalGearSetMicroGeometry",
    "CylindricalGearSetMicroGeometryDutyCycle",
    "CylindricalGearToothMicroGeometry",
    "CylindricalGearTriangularEndModification",
    "CylindricalGearTriangularEndModificationAtOrientation",
    "DrawDefiningGearOrBoth",
    "GearAlignment",
    "LeadFormReliefWithDeviation",
    "LeadReliefWithDeviation",
    "LeadSlopeReliefWithDeviation",
    "LinearCylindricalGearTriangularEndModification",
    "MeasuredMapDataTypes",
    "MeshAlignment",
    "MeshedCylindricalGearFlankMicroGeometry",
    "MeshedCylindricalGearMicroGeometry",
    "MicroGeometryLeadToleranceChartView",
    "MicroGeometryViewingOptions",
    "ParabolicCylindricalGearTriangularEndModification",
    "ProfileFormReliefWithDeviation",
    "ProfileReliefWithDeviation",
    "ProfileSlopeReliefWithDeviation",
    "ReliefWithDeviation",
    "SingleCylindricalGearTriangularEndModification",
    "TotalLeadReliefWithDeviation",
    "TotalProfileReliefWithDeviation",
)
