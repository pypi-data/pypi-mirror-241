"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2331 import CycloidalDiscAxialLeftSocket
    from ._2332 import CycloidalDiscAxialRightSocket
    from ._2333 import CycloidalDiscCentralBearingConnection
    from ._2334 import CycloidalDiscInnerSocket
    from ._2335 import CycloidalDiscOuterSocket
    from ._2336 import CycloidalDiscPlanetaryBearingConnection
    from ._2337 import CycloidalDiscPlanetaryBearingSocket
    from ._2338 import RingPinsSocket
    from ._2339 import RingPinsToDiscConnection
else:
    import_structure = {
        "_2331": ["CycloidalDiscAxialLeftSocket"],
        "_2332": ["CycloidalDiscAxialRightSocket"],
        "_2333": ["CycloidalDiscCentralBearingConnection"],
        "_2334": ["CycloidalDiscInnerSocket"],
        "_2335": ["CycloidalDiscOuterSocket"],
        "_2336": ["CycloidalDiscPlanetaryBearingConnection"],
        "_2337": ["CycloidalDiscPlanetaryBearingSocket"],
        "_2338": ["RingPinsSocket"],
        "_2339": ["RingPinsToDiscConnection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CycloidalDiscAxialLeftSocket",
    "CycloidalDiscAxialRightSocket",
    "CycloidalDiscCentralBearingConnection",
    "CycloidalDiscInnerSocket",
    "CycloidalDiscOuterSocket",
    "CycloidalDiscPlanetaryBearingConnection",
    "CycloidalDiscPlanetaryBearingSocket",
    "RingPinsSocket",
    "RingPinsToDiscConnection",
)
