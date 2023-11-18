"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2128 import BearingDesign
    from ._2129 import DetailedBearing
    from ._2130 import DummyRollingBearing
    from ._2131 import LinearBearing
    from ._2132 import NonLinearBearing
else:
    import_structure = {
        "_2128": ["BearingDesign"],
        "_2129": ["DetailedBearing"],
        "_2130": ["DummyRollingBearing"],
        "_2131": ["LinearBearing"],
        "_2132": ["NonLinearBearing"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BearingDesign",
    "DetailedBearing",
    "DummyRollingBearing",
    "LinearBearing",
    "NonLinearBearing",
)
