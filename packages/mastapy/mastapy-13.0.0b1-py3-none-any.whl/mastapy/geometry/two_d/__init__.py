"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._308 import CADFace
    from ._309 import CADFaceGroup
    from ._310 import InternalExternalType
else:
    import_structure = {
        "_308": ["CADFace"],
        "_309": ["CADFaceGroup"],
        "_310": ["InternalExternalType"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CADFace",
    "CADFaceGroup",
    "InternalExternalType",
)
