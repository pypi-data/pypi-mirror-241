"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1822 import Database
    from ._1823 import DatabaseConnectionSettings
    from ._1824 import DatabaseKey
    from ._1825 import DatabaseSettings
    from ._1826 import NamedDatabase
    from ._1827 import NamedDatabaseItem
    from ._1828 import NamedKey
    from ._1829 import SQLDatabase
else:
    import_structure = {
        "_1822": ["Database"],
        "_1823": ["DatabaseConnectionSettings"],
        "_1824": ["DatabaseKey"],
        "_1825": ["DatabaseSettings"],
        "_1826": ["NamedDatabase"],
        "_1827": ["NamedDatabaseItem"],
        "_1828": ["NamedKey"],
        "_1829": ["SQLDatabase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Database",
    "DatabaseConnectionSettings",
    "DatabaseKey",
    "DatabaseSettings",
    "NamedDatabase",
    "NamedDatabaseItem",
    "NamedKey",
    "SQLDatabase",
)
