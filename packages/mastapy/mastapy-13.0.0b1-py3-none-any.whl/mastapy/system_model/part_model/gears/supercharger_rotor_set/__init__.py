"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2553 import BoostPressureInputOptions
    from ._2554 import InputPowerInputOptions
    from ._2555 import PressureRatioInputOptions
    from ._2556 import RotorSetDataInputFileOptions
    from ._2557 import RotorSetMeasuredPoint
    from ._2558 import RotorSpeedInputOptions
    from ._2559 import SuperchargerMap
    from ._2560 import SuperchargerMaps
    from ._2561 import SuperchargerRotorSet
    from ._2562 import SuperchargerRotorSetDatabase
    from ._2563 import YVariableForImportedData
else:
    import_structure = {
        "_2553": ["BoostPressureInputOptions"],
        "_2554": ["InputPowerInputOptions"],
        "_2555": ["PressureRatioInputOptions"],
        "_2556": ["RotorSetDataInputFileOptions"],
        "_2557": ["RotorSetMeasuredPoint"],
        "_2558": ["RotorSpeedInputOptions"],
        "_2559": ["SuperchargerMap"],
        "_2560": ["SuperchargerMaps"],
        "_2561": ["SuperchargerRotorSet"],
        "_2562": ["SuperchargerRotorSetDatabase"],
        "_2563": ["YVariableForImportedData"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BoostPressureInputOptions",
    "InputPowerInputOptions",
    "PressureRatioInputOptions",
    "RotorSetDataInputFileOptions",
    "RotorSetMeasuredPoint",
    "RotorSpeedInputOptions",
    "SuperchargerMap",
    "SuperchargerMaps",
    "SuperchargerRotorSet",
    "SuperchargerRotorSetDatabase",
    "YVariableForImportedData",
)
