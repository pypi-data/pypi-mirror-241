"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2609 import ActiveFESubstructureSelection
    from ._2610 import ActiveFESubstructureSelectionGroup
    from ._2611 import ActiveShaftDesignSelection
    from ._2612 import ActiveShaftDesignSelectionGroup
    from ._2613 import BearingDetailConfiguration
    from ._2614 import BearingDetailSelection
    from ._2615 import PartDetailConfiguration
    from ._2616 import PartDetailSelection
else:
    import_structure = {
        "_2609": ["ActiveFESubstructureSelection"],
        "_2610": ["ActiveFESubstructureSelectionGroup"],
        "_2611": ["ActiveShaftDesignSelection"],
        "_2612": ["ActiveShaftDesignSelectionGroup"],
        "_2613": ["BearingDetailConfiguration"],
        "_2614": ["BearingDetailSelection"],
        "_2615": ["PartDetailConfiguration"],
        "_2616": ["PartDetailSelection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ActiveFESubstructureSelection",
    "ActiveFESubstructureSelectionGroup",
    "ActiveShaftDesignSelection",
    "ActiveShaftDesignSelectionGroup",
    "BearingDetailConfiguration",
    "BearingDetailSelection",
    "PartDetailConfiguration",
    "PartDetailSelection",
)
