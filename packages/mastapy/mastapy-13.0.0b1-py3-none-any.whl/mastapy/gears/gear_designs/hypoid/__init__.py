"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._983 import HypoidGearDesign
    from ._984 import HypoidGearMeshDesign
    from ._985 import HypoidGearSetDesign
    from ._986 import HypoidMeshedGearDesign
else:
    import_structure = {
        "_983": ["HypoidGearDesign"],
        "_984": ["HypoidGearMeshDesign"],
        "_985": ["HypoidGearSetDesign"],
        "_986": ["HypoidMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "HypoidGearDesign",
    "HypoidGearMeshDesign",
    "HypoidGearSetDesign",
    "HypoidMeshedGearDesign",
)
