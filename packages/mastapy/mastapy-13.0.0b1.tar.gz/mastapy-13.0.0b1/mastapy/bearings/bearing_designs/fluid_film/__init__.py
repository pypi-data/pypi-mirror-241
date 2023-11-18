"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2179 import AxialFeedJournalBearing
    from ._2180 import AxialGrooveJournalBearing
    from ._2181 import AxialHoleJournalBearing
    from ._2182 import CircumferentialFeedJournalBearing
    from ._2183 import CylindricalHousingJournalBearing
    from ._2184 import MachineryEncasedJournalBearing
    from ._2185 import PadFluidFilmBearing
    from ._2186 import PedestalJournalBearing
    from ._2187 import PlainGreaseFilledJournalBearing
    from ._2188 import PlainGreaseFilledJournalBearingHousingType
    from ._2189 import PlainJournalBearing
    from ._2190 import PlainJournalHousing
    from ._2191 import PlainOilFedJournalBearing
    from ._2192 import TiltingPadJournalBearing
    from ._2193 import TiltingPadThrustBearing
else:
    import_structure = {
        "_2179": ["AxialFeedJournalBearing"],
        "_2180": ["AxialGrooveJournalBearing"],
        "_2181": ["AxialHoleJournalBearing"],
        "_2182": ["CircumferentialFeedJournalBearing"],
        "_2183": ["CylindricalHousingJournalBearing"],
        "_2184": ["MachineryEncasedJournalBearing"],
        "_2185": ["PadFluidFilmBearing"],
        "_2186": ["PedestalJournalBearing"],
        "_2187": ["PlainGreaseFilledJournalBearing"],
        "_2188": ["PlainGreaseFilledJournalBearingHousingType"],
        "_2189": ["PlainJournalBearing"],
        "_2190": ["PlainJournalHousing"],
        "_2191": ["PlainOilFedJournalBearing"],
        "_2192": ["TiltingPadJournalBearing"],
        "_2193": ["TiltingPadThrustBearing"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AxialFeedJournalBearing",
    "AxialGrooveJournalBearing",
    "AxialHoleJournalBearing",
    "CircumferentialFeedJournalBearing",
    "CylindricalHousingJournalBearing",
    "MachineryEncasedJournalBearing",
    "PadFluidFilmBearing",
    "PedestalJournalBearing",
    "PlainGreaseFilledJournalBearing",
    "PlainGreaseFilledJournalBearingHousingType",
    "PlainJournalBearing",
    "PlainJournalHousing",
    "PlainOilFedJournalBearing",
    "TiltingPadJournalBearing",
    "TiltingPadThrustBearing",
)
