"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7559 import ApiEnumForAttribute
    from ._7560 import ApiVersion
    from ._7561 import SMTBitmap
    from ._7563 import MastaPropertyAttribute
    from ._7564 import PythonCommand
    from ._7565 import ScriptingCommand
    from ._7566 import ScriptingExecutionCommand
    from ._7567 import ScriptingObjectCommand
    from ._7568 import ApiVersioning
else:
    import_structure = {
        "_7559": ["ApiEnumForAttribute"],
        "_7560": ["ApiVersion"],
        "_7561": ["SMTBitmap"],
        "_7563": ["MastaPropertyAttribute"],
        "_7564": ["PythonCommand"],
        "_7565": ["ScriptingCommand"],
        "_7566": ["ScriptingExecutionCommand"],
        "_7567": ["ScriptingObjectCommand"],
        "_7568": ["ApiVersioning"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ApiEnumForAttribute",
    "ApiVersion",
    "SMTBitmap",
    "MastaPropertyAttribute",
    "PythonCommand",
    "ScriptingCommand",
    "ScriptingExecutionCommand",
    "ScriptingObjectCommand",
    "ApiVersioning",
)
