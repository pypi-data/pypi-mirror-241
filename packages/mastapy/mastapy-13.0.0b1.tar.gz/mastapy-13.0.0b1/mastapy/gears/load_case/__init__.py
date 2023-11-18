"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._871 import GearLoadCaseBase
    from ._872 import GearSetLoadCaseBase
    from ._873 import MeshLoadCase
else:
    import_structure = {
        "_871": ["GearLoadCaseBase"],
        "_872": ["GearSetLoadCaseBase"],
        "_873": ["MeshLoadCase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "GearLoadCaseBase",
    "GearSetLoadCaseBase",
    "MeshLoadCase",
)
