"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1925 import ProfileDataToUse
    from ._1926 import ProfileSet
    from ._1927 import ProfileToFit
    from ._1928 import RollerBearingConicalProfile
    from ._1929 import RollerBearingCrownedProfile
    from ._1930 import RollerBearingDinLundbergProfile
    from ._1931 import RollerBearingFlatProfile
    from ._1932 import RollerBearingJohnsGoharProfile
    from ._1933 import RollerBearingLundbergProfile
    from ._1934 import RollerBearingProfile
    from ._1935 import RollerBearingUserSpecifiedProfile
    from ._1936 import RollerRaceProfilePoint
    from ._1937 import UserSpecifiedProfilePoint
    from ._1938 import UserSpecifiedRollerRaceProfilePoint
else:
    import_structure = {
        "_1925": ["ProfileDataToUse"],
        "_1926": ["ProfileSet"],
        "_1927": ["ProfileToFit"],
        "_1928": ["RollerBearingConicalProfile"],
        "_1929": ["RollerBearingCrownedProfile"],
        "_1930": ["RollerBearingDinLundbergProfile"],
        "_1931": ["RollerBearingFlatProfile"],
        "_1932": ["RollerBearingJohnsGoharProfile"],
        "_1933": ["RollerBearingLundbergProfile"],
        "_1934": ["RollerBearingProfile"],
        "_1935": ["RollerBearingUserSpecifiedProfile"],
        "_1936": ["RollerRaceProfilePoint"],
        "_1937": ["UserSpecifiedProfilePoint"],
        "_1938": ["UserSpecifiedRollerRaceProfilePoint"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ProfileDataToUse",
    "ProfileSet",
    "ProfileToFit",
    "RollerBearingConicalProfile",
    "RollerBearingCrownedProfile",
    "RollerBearingDinLundbergProfile",
    "RollerBearingFlatProfile",
    "RollerBearingJohnsGoharProfile",
    "RollerBearingLundbergProfile",
    "RollerBearingProfile",
    "RollerBearingUserSpecifiedProfile",
    "RollerRaceProfilePoint",
    "UserSpecifiedProfilePoint",
    "UserSpecifiedRollerRaceProfilePoint",
)
