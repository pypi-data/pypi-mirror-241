"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1087 import FinishStockSpecification
    from ._1088 import FinishStockType
    from ._1089 import NominalValueSpecification
    from ._1090 import NoValueSpecification
else:
    import_structure = {
        "_1087": ["FinishStockSpecification"],
        "_1088": ["FinishStockType"],
        "_1089": ["NominalValueSpecification"],
        "_1090": ["NoValueSpecification"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "FinishStockSpecification",
    "FinishStockType",
    "NominalValueSpecification",
    "NoValueSpecification",
)
