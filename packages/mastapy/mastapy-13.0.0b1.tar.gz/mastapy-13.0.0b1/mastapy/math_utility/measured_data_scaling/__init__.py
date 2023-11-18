"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1567 import DataScalingOptions
    from ._1568 import DataScalingReferenceValues
    from ._1569 import DataScalingReferenceValuesBase
else:
    import_structure = {
        "_1567": ["DataScalingOptions"],
        "_1568": ["DataScalingReferenceValues"],
        "_1569": ["DataScalingReferenceValuesBase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DataScalingOptions",
    "DataScalingReferenceValues",
    "DataScalingReferenceValuesBase",
)
