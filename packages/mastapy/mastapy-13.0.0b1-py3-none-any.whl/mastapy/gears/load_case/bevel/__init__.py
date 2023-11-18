"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._889 import BevelLoadCase
    from ._890 import BevelMeshLoadCase
    from ._891 import BevelSetLoadCase
else:
    import_structure = {
        "_889": ["BevelLoadCase"],
        "_890": ["BevelMeshLoadCase"],
        "_891": ["BevelSetLoadCase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BevelLoadCase",
    "BevelMeshLoadCase",
    "BevelSetLoadCase",
)
