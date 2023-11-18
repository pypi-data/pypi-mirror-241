"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1174 import ConceptGearDesign
    from ._1175 import ConceptGearMeshDesign
    from ._1176 import ConceptGearSetDesign
else:
    import_structure = {
        "_1174": ["ConceptGearDesign"],
        "_1175": ["ConceptGearMeshDesign"],
        "_1176": ["ConceptGearSetDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConceptGearDesign",
    "ConceptGearMeshDesign",
    "ConceptGearSetDesign",
)
