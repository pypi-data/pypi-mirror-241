"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2099 import BallISO2812007Results
    from ._2100 import BallISOTS162812008Results
    from ._2101 import ISO2812007Results
    from ._2102 import ISO762006Results
    from ._2103 import ISOResults
    from ._2104 import ISOTS162812008Results
    from ._2105 import RollerISO2812007Results
    from ._2106 import RollerISOTS162812008Results
    from ._2107 import StressConcentrationMethod
else:
    import_structure = {
        "_2099": ["BallISO2812007Results"],
        "_2100": ["BallISOTS162812008Results"],
        "_2101": ["ISO2812007Results"],
        "_2102": ["ISO762006Results"],
        "_2103": ["ISOResults"],
        "_2104": ["ISOTS162812008Results"],
        "_2105": ["RollerISO2812007Results"],
        "_2106": ["RollerISOTS162812008Results"],
        "_2107": ["StressConcentrationMethod"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BallISO2812007Results",
    "BallISOTS162812008Results",
    "ISO2812007Results",
    "ISO762006Results",
    "ISOResults",
    "ISOTS162812008Results",
    "RollerISO2812007Results",
    "RollerISOTS162812008Results",
    "StressConcentrationMethod",
)
