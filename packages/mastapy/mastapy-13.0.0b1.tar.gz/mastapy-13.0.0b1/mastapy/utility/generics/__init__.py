"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1808 import NamedTuple1
    from ._1809 import NamedTuple2
    from ._1810 import NamedTuple3
    from ._1811 import NamedTuple4
    from ._1812 import NamedTuple5
    from ._1813 import NamedTuple6
    from ._1814 import NamedTuple7
else:
    import_structure = {
        "_1808": ["NamedTuple1"],
        "_1809": ["NamedTuple2"],
        "_1810": ["NamedTuple3"],
        "_1811": ["NamedTuple4"],
        "_1812": ["NamedTuple5"],
        "_1813": ["NamedTuple6"],
        "_1814": ["NamedTuple7"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "NamedTuple1",
    "NamedTuple2",
    "NamedTuple3",
    "NamedTuple4",
    "NamedTuple5",
    "NamedTuple6",
    "NamedTuple7",
)
