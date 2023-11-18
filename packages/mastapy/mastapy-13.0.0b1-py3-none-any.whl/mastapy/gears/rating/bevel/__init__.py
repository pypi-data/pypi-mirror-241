"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._552 import BevelGearMeshRating
    from ._553 import BevelGearRating
    from ._554 import BevelGearSetRating
else:
    import_structure = {
        "_552": ["BevelGearMeshRating"],
        "_553": ["BevelGearRating"],
        "_554": ["BevelGearSetRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BevelGearMeshRating",
    "BevelGearRating",
    "BevelGearSetRating",
)
