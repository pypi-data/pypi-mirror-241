"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2174 import AbstractXmlVariableAssignment
    from ._2175 import BearingImportFile
    from ._2176 import RollingBearingImporter
    from ._2177 import XmlBearingTypeMapping
    from ._2178 import XMLVariableAssignment
else:
    import_structure = {
        "_2174": ["AbstractXmlVariableAssignment"],
        "_2175": ["BearingImportFile"],
        "_2176": ["RollingBearingImporter"],
        "_2177": ["XmlBearingTypeMapping"],
        "_2178": ["XMLVariableAssignment"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractXmlVariableAssignment",
    "BearingImportFile",
    "RollingBearingImporter",
    "XmlBearingTypeMapping",
    "XMLVariableAssignment",
)
