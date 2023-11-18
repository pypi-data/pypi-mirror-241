"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._563 import AGMAGleasonConicalGearMeshRating
    from ._564 import AGMAGleasonConicalGearRating
    from ._565 import AGMAGleasonConicalGearSetRating
    from ._566 import AGMAGleasonConicalRateableMesh
else:
    import_structure = {
        "_563": ["AGMAGleasonConicalGearMeshRating"],
        "_564": ["AGMAGleasonConicalGearRating"],
        "_565": ["AGMAGleasonConicalGearSetRating"],
        "_566": ["AGMAGleasonConicalRateableMesh"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMAGleasonConicalGearMeshRating",
    "AGMAGleasonConicalGearRating",
    "AGMAGleasonConicalGearSetRating",
    "AGMAGleasonConicalRateableMesh",
)
