"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._880 import CylindricalGearLoadCase
    from ._881 import CylindricalGearSetLoadCase
    from ._882 import CylindricalMeshLoadCase
else:
    import_structure = {
        "_880": ["CylindricalGearLoadCase"],
        "_881": ["CylindricalGearSetLoadCase"],
        "_882": ["CylindricalMeshLoadCase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearLoadCase",
    "CylindricalGearSetLoadCase",
    "CylindricalMeshLoadCase",
)
