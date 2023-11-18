"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1448 import ContactSpecification
    from ._1449 import CrowningSpecificationMethod
    from ._1450 import CycloidalAssemblyDesign
    from ._1451 import CycloidalDiscDesign
    from ._1452 import CycloidalDiscDesignExporter
    from ._1453 import CycloidalDiscMaterial
    from ._1454 import CycloidalDiscMaterialDatabase
    from ._1455 import CycloidalDiscModificationsSpecification
    from ._1456 import DirectionOfMeasuredModifications
    from ._1457 import GeometryToExport
    from ._1458 import NamedDiscPhase
    from ._1459 import RingPinsDesign
    from ._1460 import RingPinsMaterial
    from ._1461 import RingPinsMaterialDatabase
else:
    import_structure = {
        "_1448": ["ContactSpecification"],
        "_1449": ["CrowningSpecificationMethod"],
        "_1450": ["CycloidalAssemblyDesign"],
        "_1451": ["CycloidalDiscDesign"],
        "_1452": ["CycloidalDiscDesignExporter"],
        "_1453": ["CycloidalDiscMaterial"],
        "_1454": ["CycloidalDiscMaterialDatabase"],
        "_1455": ["CycloidalDiscModificationsSpecification"],
        "_1456": ["DirectionOfMeasuredModifications"],
        "_1457": ["GeometryToExport"],
        "_1458": ["NamedDiscPhase"],
        "_1459": ["RingPinsDesign"],
        "_1460": ["RingPinsMaterial"],
        "_1461": ["RingPinsMaterialDatabase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ContactSpecification",
    "CrowningSpecificationMethod",
    "CycloidalAssemblyDesign",
    "CycloidalDiscDesign",
    "CycloidalDiscDesignExporter",
    "CycloidalDiscMaterial",
    "CycloidalDiscMaterialDatabase",
    "CycloidalDiscModificationsSpecification",
    "DirectionOfMeasuredModifications",
    "GeometryToExport",
    "NamedDiscPhase",
    "RingPinsDesign",
    "RingPinsMaterial",
    "RingPinsMaterialDatabase",
)
