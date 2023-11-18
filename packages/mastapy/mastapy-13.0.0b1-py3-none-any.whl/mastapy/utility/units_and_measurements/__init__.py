"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1600 import DegreesMinutesSeconds
    from ._1601 import EnumUnit
    from ._1602 import InverseUnit
    from ._1603 import MeasurementBase
    from ._1604 import MeasurementSettings
    from ._1605 import MeasurementSystem
    from ._1606 import SafetyFactorUnit
    from ._1607 import TimeUnit
    from ._1608 import Unit
    from ._1609 import UnitGradient
else:
    import_structure = {
        "_1600": ["DegreesMinutesSeconds"],
        "_1601": ["EnumUnit"],
        "_1602": ["InverseUnit"],
        "_1603": ["MeasurementBase"],
        "_1604": ["MeasurementSettings"],
        "_1605": ["MeasurementSystem"],
        "_1606": ["SafetyFactorUnit"],
        "_1607": ["TimeUnit"],
        "_1608": ["Unit"],
        "_1609": ["UnitGradient"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DegreesMinutesSeconds",
    "EnumUnit",
    "InverseUnit",
    "MeasurementBase",
    "MeasurementSettings",
    "MeasurementSystem",
    "SafetyFactorUnit",
    "TimeUnit",
    "Unit",
    "UnitGradient",
)
