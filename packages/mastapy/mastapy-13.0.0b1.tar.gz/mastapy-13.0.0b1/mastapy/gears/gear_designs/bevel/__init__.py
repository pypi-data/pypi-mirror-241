"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1177 import AGMAGleasonConicalGearGeometryMethods
    from ._1178 import BevelGearDesign
    from ._1179 import BevelGearMeshDesign
    from ._1180 import BevelGearSetDesign
    from ._1181 import BevelMeshedGearDesign
    from ._1182 import DrivenMachineCharacteristicGleason
    from ._1183 import EdgeRadiusType
    from ._1184 import FinishingMethods
    from ._1185 import MachineCharacteristicAGMAKlingelnberg
    from ._1186 import PrimeMoverCharacteristicGleason
    from ._1187 import ToothProportionsInputMethod
    from ._1188 import ToothThicknessSpecificationMethod
    from ._1189 import WheelFinishCutterPointWidthRestrictionMethod
else:
    import_structure = {
        "_1177": ["AGMAGleasonConicalGearGeometryMethods"],
        "_1178": ["BevelGearDesign"],
        "_1179": ["BevelGearMeshDesign"],
        "_1180": ["BevelGearSetDesign"],
        "_1181": ["BevelMeshedGearDesign"],
        "_1182": ["DrivenMachineCharacteristicGleason"],
        "_1183": ["EdgeRadiusType"],
        "_1184": ["FinishingMethods"],
        "_1185": ["MachineCharacteristicAGMAKlingelnberg"],
        "_1186": ["PrimeMoverCharacteristicGleason"],
        "_1187": ["ToothProportionsInputMethod"],
        "_1188": ["ToothThicknessSpecificationMethod"],
        "_1189": ["WheelFinishCutterPointWidthRestrictionMethod"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMAGleasonConicalGearGeometryMethods",
    "BevelGearDesign",
    "BevelGearMeshDesign",
    "BevelGearSetDesign",
    "BevelMeshedGearDesign",
    "DrivenMachineCharacteristicGleason",
    "EdgeRadiusType",
    "FinishingMethods",
    "MachineCharacteristicAGMAKlingelnberg",
    "PrimeMoverCharacteristicGleason",
    "ToothProportionsInputMethod",
    "ToothThicknessSpecificationMethod",
    "WheelFinishCutterPointWidthRestrictionMethod",
)
