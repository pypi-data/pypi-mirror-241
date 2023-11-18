"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1190 import AGMAGleasonConicalAccuracyGrades
    from ._1191 import AGMAGleasonConicalGearDesign
    from ._1192 import AGMAGleasonConicalGearMeshDesign
    from ._1193 import AGMAGleasonConicalGearSetDesign
    from ._1194 import AGMAGleasonConicalMeshedGearDesign
else:
    import_structure = {
        "_1190": ["AGMAGleasonConicalAccuracyGrades"],
        "_1191": ["AGMAGleasonConicalGearDesign"],
        "_1192": ["AGMAGleasonConicalGearMeshDesign"],
        "_1193": ["AGMAGleasonConicalGearSetDesign"],
        "_1194": ["AGMAGleasonConicalMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMAGleasonConicalAccuracyGrades",
    "AGMAGleasonConicalGearDesign",
    "AGMAGleasonConicalGearMeshDesign",
    "AGMAGleasonConicalGearSetDesign",
    "AGMAGleasonConicalMeshedGearDesign",
)
