"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1789 import Fix
    from ._1790 import Severity
    from ._1791 import Status
    from ._1792 import StatusItem
    from ._1793 import StatusItemSeverity
else:
    import_structure = {
        "_1789": ["Fix"],
        "_1790": ["Severity"],
        "_1791": ["Status"],
        "_1792": ["StatusItem"],
        "_1793": ["StatusItemSeverity"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Fix",
    "Severity",
    "Status",
    "StatusItem",
    "StatusItemSeverity",
)
