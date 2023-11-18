"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6534 import ExcelBatchDutyCycleCreator
    from ._6535 import ExcelBatchDutyCycleSpectraCreatorDetails
    from ._6536 import ExcelFileDetails
    from ._6537 import ExcelSheet
    from ._6538 import ExcelSheetDesignStateSelector
    from ._6539 import MASTAFileDetails
else:
    import_structure = {
        "_6534": ["ExcelBatchDutyCycleCreator"],
        "_6535": ["ExcelBatchDutyCycleSpectraCreatorDetails"],
        "_6536": ["ExcelFileDetails"],
        "_6537": ["ExcelSheet"],
        "_6538": ["ExcelSheetDesignStateSelector"],
        "_6539": ["MASTAFileDetails"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ExcelBatchDutyCycleCreator",
    "ExcelBatchDutyCycleSpectraCreatorDetails",
    "ExcelFileDetails",
    "ExcelSheet",
    "ExcelSheetDesignStateSelector",
    "MASTAFileDetails",
)
