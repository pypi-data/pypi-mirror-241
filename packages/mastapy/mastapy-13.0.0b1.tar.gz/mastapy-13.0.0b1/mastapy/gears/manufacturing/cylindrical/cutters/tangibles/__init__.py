"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._721 import CutterShapeDefinition
    from ._722 import CylindricalGearFormedWheelGrinderTangible
    from ._723 import CylindricalGearHobShape
    from ._724 import CylindricalGearShaperTangible
    from ._725 import CylindricalGearShaverTangible
    from ._726 import CylindricalGearWormGrinderShape
    from ._727 import NamedPoint
    from ._728 import RackShape
else:
    import_structure = {
        "_721": ["CutterShapeDefinition"],
        "_722": ["CylindricalGearFormedWheelGrinderTangible"],
        "_723": ["CylindricalGearHobShape"],
        "_724": ["CylindricalGearShaperTangible"],
        "_725": ["CylindricalGearShaverTangible"],
        "_726": ["CylindricalGearWormGrinderShape"],
        "_727": ["NamedPoint"],
        "_728": ["RackShape"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CutterShapeDefinition",
    "CylindricalGearFormedWheelGrinderTangible",
    "CylindricalGearHobShape",
    "CylindricalGearShaperTangible",
    "CylindricalGearShaverTangible",
    "CylindricalGearWormGrinderShape",
    "NamedPoint",
    "RackShape",
)
