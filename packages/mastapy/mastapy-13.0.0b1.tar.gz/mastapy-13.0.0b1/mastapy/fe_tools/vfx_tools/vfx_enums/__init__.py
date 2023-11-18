"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1237 import ProSolveMpcType
    from ._1238 import ProSolveSolverType
else:
    import_structure = {
        "_1237": ["ProSolveMpcType"],
        "_1238": ["ProSolveSolverType"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ProSolveMpcType",
    "ProSolveSolverType",
)
