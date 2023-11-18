"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1239 import ElementPropertyClass
    from ._1240 import MaterialPropertyClass
else:
    import_structure = {
        "_1239": ["ElementPropertyClass"],
        "_1240": ["MaterialPropertyClass"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ElementPropertyClass",
    "MaterialPropertyClass",
)
