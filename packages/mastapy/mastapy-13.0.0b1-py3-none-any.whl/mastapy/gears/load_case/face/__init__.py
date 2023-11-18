"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._877 import FaceGearLoadCase
    from ._878 import FaceGearSetLoadCase
    from ._879 import FaceMeshLoadCase
else:
    import_structure = {
        "_877": ["FaceGearLoadCase"],
        "_878": ["FaceGearSetLoadCase"],
        "_879": ["FaceMeshLoadCase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "FaceGearLoadCase",
    "FaceGearSetLoadCase",
    "FaceMeshLoadCase",
)
