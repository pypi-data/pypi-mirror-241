"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1148 import ActiveConicalFlank
    from ._1149 import BacklashDistributionRule
    from ._1150 import ConicalFlanks
    from ._1151 import ConicalGearCutter
    from ._1152 import ConicalGearDesign
    from ._1153 import ConicalGearMeshDesign
    from ._1154 import ConicalGearSetDesign
    from ._1155 import ConicalMachineSettingCalculationMethods
    from ._1156 import ConicalManufactureMethods
    from ._1157 import ConicalMeshedGearDesign
    from ._1158 import ConicalMeshMisalignments
    from ._1159 import CutterBladeType
    from ._1160 import CutterGaugeLengths
    from ._1161 import DummyConicalGearCutter
    from ._1162 import FrontEndTypes
    from ._1163 import GleasonSafetyRequirements
    from ._1164 import KIMoSBevelHypoidSingleLoadCaseResultsData
    from ._1165 import KIMoSBevelHypoidSingleRotationAngleResult
    from ._1166 import KlingelnbergFinishingMethods
    from ._1167 import LoadDistributionFactorMethods
    from ._1168 import TopremEntryType
    from ._1169 import TopremLetter
else:
    import_structure = {
        "_1148": ["ActiveConicalFlank"],
        "_1149": ["BacklashDistributionRule"],
        "_1150": ["ConicalFlanks"],
        "_1151": ["ConicalGearCutter"],
        "_1152": ["ConicalGearDesign"],
        "_1153": ["ConicalGearMeshDesign"],
        "_1154": ["ConicalGearSetDesign"],
        "_1155": ["ConicalMachineSettingCalculationMethods"],
        "_1156": ["ConicalManufactureMethods"],
        "_1157": ["ConicalMeshedGearDesign"],
        "_1158": ["ConicalMeshMisalignments"],
        "_1159": ["CutterBladeType"],
        "_1160": ["CutterGaugeLengths"],
        "_1161": ["DummyConicalGearCutter"],
        "_1162": ["FrontEndTypes"],
        "_1163": ["GleasonSafetyRequirements"],
        "_1164": ["KIMoSBevelHypoidSingleLoadCaseResultsData"],
        "_1165": ["KIMoSBevelHypoidSingleRotationAngleResult"],
        "_1166": ["KlingelnbergFinishingMethods"],
        "_1167": ["LoadDistributionFactorMethods"],
        "_1168": ["TopremEntryType"],
        "_1169": ["TopremLetter"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ActiveConicalFlank",
    "BacklashDistributionRule",
    "ConicalFlanks",
    "ConicalGearCutter",
    "ConicalGearDesign",
    "ConicalGearMeshDesign",
    "ConicalGearSetDesign",
    "ConicalMachineSettingCalculationMethods",
    "ConicalManufactureMethods",
    "ConicalMeshedGearDesign",
    "ConicalMeshMisalignments",
    "CutterBladeType",
    "CutterGaugeLengths",
    "DummyConicalGearCutter",
    "FrontEndTypes",
    "GleasonSafetyRequirements",
    "KIMoSBevelHypoidSingleLoadCaseResultsData",
    "KIMoSBevelHypoidSingleRotationAngleResult",
    "KlingelnbergFinishingMethods",
    "LoadDistributionFactorMethods",
    "TopremEntryType",
    "TopremLetter",
)
