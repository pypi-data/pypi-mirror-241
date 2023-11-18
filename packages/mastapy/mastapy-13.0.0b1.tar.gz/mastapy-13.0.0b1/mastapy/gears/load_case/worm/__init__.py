"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._874 import WormGearLoadCase
    from ._875 import WormGearSetLoadCase
    from ._876 import WormMeshLoadCase
else:
    import_structure = {
        "_874": ["WormGearLoadCase"],
        "_875": ["WormGearSetLoadCase"],
        "_876": ["WormMeshLoadCase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "WormGearLoadCase",
    "WormGearSetLoadCase",
    "WormMeshLoadCase",
)
