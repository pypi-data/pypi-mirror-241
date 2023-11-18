"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1434 import KeyedJointDesign
    from ._1435 import KeyTypes
    from ._1436 import KeywayJointHalfDesign
    from ._1437 import NumberOfKeys
else:
    import_structure = {
        "_1434": ["KeyedJointDesign"],
        "_1435": ["KeyTypes"],
        "_1436": ["KeywayJointHalfDesign"],
        "_1437": ["NumberOfKeys"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KeyedJointDesign",
    "KeyTypes",
    "KeywayJointHalfDesign",
    "NumberOfKeys",
)
