"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1737 import ScriptingSetup
    from ._1738 import UserDefinedPropertyKey
    from ._1739 import UserSpecifiedData
else:
    import_structure = {
        "_1737": ["ScriptingSetup"],
        "_1738": ["UserDefinedPropertyKey"],
        "_1739": ["UserSpecifiedData"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ScriptingSetup",
    "UserDefinedPropertyKey",
    "UserSpecifiedData",
)
