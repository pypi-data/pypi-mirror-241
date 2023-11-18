"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._886 import ConceptGearLoadCase
    from ._887 import ConceptGearSetLoadCase
    from ._888 import ConceptMeshLoadCase
else:
    import_structure = {
        "_886": ["ConceptGearLoadCase"],
        "_887": ["ConceptGearSetLoadCase"],
        "_888": ["ConceptMeshLoadCase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConceptGearLoadCase",
    "ConceptGearSetLoadCase",
    "ConceptMeshLoadCase",
)
