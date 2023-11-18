"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1375 import ElectricMachineHarmonicLoadDataBase
    from ._1376 import ForceDisplayOption
    from ._1377 import HarmonicLoadDataBase
    from ._1378 import HarmonicLoadDataControlExcitationOptionBase
    from ._1379 import HarmonicLoadDataType
    from ._1380 import SpeedDependentHarmonicLoadData
    from ._1381 import StatorToothInterpolator
    from ._1382 import StatorToothLoadInterpolator
    from ._1383 import StatorToothMomentInterpolator
else:
    import_structure = {
        "_1375": ["ElectricMachineHarmonicLoadDataBase"],
        "_1376": ["ForceDisplayOption"],
        "_1377": ["HarmonicLoadDataBase"],
        "_1378": ["HarmonicLoadDataControlExcitationOptionBase"],
        "_1379": ["HarmonicLoadDataType"],
        "_1380": ["SpeedDependentHarmonicLoadData"],
        "_1381": ["StatorToothInterpolator"],
        "_1382": ["StatorToothLoadInterpolator"],
        "_1383": ["StatorToothMomentInterpolator"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ElectricMachineHarmonicLoadDataBase",
    "ForceDisplayOption",
    "HarmonicLoadDataBase",
    "HarmonicLoadDataControlExcitationOptionBase",
    "HarmonicLoadDataType",
    "SpeedDependentHarmonicLoadData",
    "StatorToothInterpolator",
    "StatorToothLoadInterpolator",
    "StatorToothMomentInterpolator",
)
