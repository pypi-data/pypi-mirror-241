"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._938 import BevelHypoidGearDesignSettingsDatabase
    from ._939 import BevelHypoidGearDesignSettingsItem
    from ._940 import BevelHypoidGearRatingSettingsDatabase
    from ._941 import BevelHypoidGearRatingSettingsItem
    from ._942 import DesignConstraint
    from ._943 import DesignConstraintCollectionDatabase
    from ._944 import DesignConstraintsCollection
    from ._945 import GearDesign
    from ._946 import GearDesignComponent
    from ._947 import GearMeshDesign
    from ._948 import GearSetDesign
    from ._949 import SelectedDesignConstraintsCollection
else:
    import_structure = {
        "_938": ["BevelHypoidGearDesignSettingsDatabase"],
        "_939": ["BevelHypoidGearDesignSettingsItem"],
        "_940": ["BevelHypoidGearRatingSettingsDatabase"],
        "_941": ["BevelHypoidGearRatingSettingsItem"],
        "_942": ["DesignConstraint"],
        "_943": ["DesignConstraintCollectionDatabase"],
        "_944": ["DesignConstraintsCollection"],
        "_945": ["GearDesign"],
        "_946": ["GearDesignComponent"],
        "_947": ["GearMeshDesign"],
        "_948": ["GearSetDesign"],
        "_949": ["SelectedDesignConstraintsCollection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BevelHypoidGearDesignSettingsDatabase",
    "BevelHypoidGearDesignSettingsItem",
    "BevelHypoidGearRatingSettingsDatabase",
    "BevelHypoidGearRatingSettingsItem",
    "DesignConstraint",
    "DesignConstraintCollectionDatabase",
    "DesignConstraintsCollection",
    "GearDesign",
    "GearDesignComponent",
    "GearMeshDesign",
    "GearSetDesign",
    "SelectedDesignConstraintsCollection",
)
