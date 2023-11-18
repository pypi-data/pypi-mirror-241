"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._883 import ConicalGearLoadCase
    from ._884 import ConicalGearSetLoadCase
    from ._885 import ConicalMeshLoadCase
else:
    import_structure = {
        "_883": ["ConicalGearLoadCase"],
        "_884": ["ConicalGearSetLoadCase"],
        "_885": ["ConicalMeshLoadCase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConicalGearLoadCase",
    "ConicalGearSetLoadCase",
    "ConicalMeshLoadCase",
)
