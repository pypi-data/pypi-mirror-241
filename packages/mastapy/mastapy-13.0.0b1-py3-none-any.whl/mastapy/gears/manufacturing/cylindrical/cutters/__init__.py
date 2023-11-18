"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._701 import CurveInLinkedList
    from ._702 import CustomisableEdgeProfile
    from ._703 import CylindricalFormedWheelGrinderDatabase
    from ._704 import CylindricalGearAbstractCutterDesign
    from ._705 import CylindricalGearFormGrindingWheel
    from ._706 import CylindricalGearGrindingWorm
    from ._707 import CylindricalGearHobDesign
    from ._708 import CylindricalGearPlungeShaver
    from ._709 import CylindricalGearPlungeShaverDatabase
    from ._710 import CylindricalGearRackDesign
    from ._711 import CylindricalGearRealCutterDesign
    from ._712 import CylindricalGearShaper
    from ._713 import CylindricalGearShaver
    from ._714 import CylindricalGearShaverDatabase
    from ._715 import CylindricalWormGrinderDatabase
    from ._716 import InvoluteCutterDesign
    from ._717 import MutableCommon
    from ._718 import MutableCurve
    from ._719 import MutableFillet
    from ._720 import RoughCutterCreationSettings
else:
    import_structure = {
        "_701": ["CurveInLinkedList"],
        "_702": ["CustomisableEdgeProfile"],
        "_703": ["CylindricalFormedWheelGrinderDatabase"],
        "_704": ["CylindricalGearAbstractCutterDesign"],
        "_705": ["CylindricalGearFormGrindingWheel"],
        "_706": ["CylindricalGearGrindingWorm"],
        "_707": ["CylindricalGearHobDesign"],
        "_708": ["CylindricalGearPlungeShaver"],
        "_709": ["CylindricalGearPlungeShaverDatabase"],
        "_710": ["CylindricalGearRackDesign"],
        "_711": ["CylindricalGearRealCutterDesign"],
        "_712": ["CylindricalGearShaper"],
        "_713": ["CylindricalGearShaver"],
        "_714": ["CylindricalGearShaverDatabase"],
        "_715": ["CylindricalWormGrinderDatabase"],
        "_716": ["InvoluteCutterDesign"],
        "_717": ["MutableCommon"],
        "_718": ["MutableCurve"],
        "_719": ["MutableFillet"],
        "_720": ["RoughCutterCreationSettings"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CurveInLinkedList",
    "CustomisableEdgeProfile",
    "CylindricalFormedWheelGrinderDatabase",
    "CylindricalGearAbstractCutterDesign",
    "CylindricalGearFormGrindingWheel",
    "CylindricalGearGrindingWorm",
    "CylindricalGearHobDesign",
    "CylindricalGearPlungeShaver",
    "CylindricalGearPlungeShaverDatabase",
    "CylindricalGearRackDesign",
    "CylindricalGearRealCutterDesign",
    "CylindricalGearShaper",
    "CylindricalGearShaver",
    "CylindricalGearShaverDatabase",
    "CylindricalWormGrinderDatabase",
    "InvoluteCutterDesign",
    "MutableCommon",
    "MutableCurve",
    "MutableFillet",
    "RoughCutterCreationSettings",
)
