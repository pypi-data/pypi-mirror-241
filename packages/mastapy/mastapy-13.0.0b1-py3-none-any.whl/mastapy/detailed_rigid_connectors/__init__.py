"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1384 import DetailedRigidConnectorDesign
    from ._1385 import DetailedRigidConnectorHalfDesign
else:
    import_structure = {
        "_1384": ["DetailedRigidConnectorDesign"],
        "_1385": ["DetailedRigidConnectorHalfDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DetailedRigidConnectorDesign",
    "DetailedRigidConnectorHalfDesign",
)
