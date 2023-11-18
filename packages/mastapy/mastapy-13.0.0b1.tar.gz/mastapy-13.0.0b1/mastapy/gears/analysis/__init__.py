"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1213 import AbstractGearAnalysis
    from ._1214 import AbstractGearMeshAnalysis
    from ._1215 import AbstractGearSetAnalysis
    from ._1216 import GearDesignAnalysis
    from ._1217 import GearImplementationAnalysis
    from ._1218 import GearImplementationAnalysisDutyCycle
    from ._1219 import GearImplementationDetail
    from ._1220 import GearMeshDesignAnalysis
    from ._1221 import GearMeshImplementationAnalysis
    from ._1222 import GearMeshImplementationAnalysisDutyCycle
    from ._1223 import GearMeshImplementationDetail
    from ._1224 import GearSetDesignAnalysis
    from ._1225 import GearSetGroupDutyCycle
    from ._1226 import GearSetImplementationAnalysis
    from ._1227 import GearSetImplementationAnalysisAbstract
    from ._1228 import GearSetImplementationAnalysisDutyCycle
    from ._1229 import GearSetImplementationDetail
else:
    import_structure = {
        "_1213": ["AbstractGearAnalysis"],
        "_1214": ["AbstractGearMeshAnalysis"],
        "_1215": ["AbstractGearSetAnalysis"],
        "_1216": ["GearDesignAnalysis"],
        "_1217": ["GearImplementationAnalysis"],
        "_1218": ["GearImplementationAnalysisDutyCycle"],
        "_1219": ["GearImplementationDetail"],
        "_1220": ["GearMeshDesignAnalysis"],
        "_1221": ["GearMeshImplementationAnalysis"],
        "_1222": ["GearMeshImplementationAnalysisDutyCycle"],
        "_1223": ["GearMeshImplementationDetail"],
        "_1224": ["GearSetDesignAnalysis"],
        "_1225": ["GearSetGroupDutyCycle"],
        "_1226": ["GearSetImplementationAnalysis"],
        "_1227": ["GearSetImplementationAnalysisAbstract"],
        "_1228": ["GearSetImplementationAnalysisDutyCycle"],
        "_1229": ["GearSetImplementationDetail"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractGearAnalysis",
    "AbstractGearMeshAnalysis",
    "AbstractGearSetAnalysis",
    "GearDesignAnalysis",
    "GearImplementationAnalysis",
    "GearImplementationAnalysisDutyCycle",
    "GearImplementationDetail",
    "GearMeshDesignAnalysis",
    "GearMeshImplementationAnalysis",
    "GearMeshImplementationAnalysisDutyCycle",
    "GearMeshImplementationDetail",
    "GearSetDesignAnalysis",
    "GearSetGroupDutyCycle",
    "GearSetImplementationAnalysis",
    "GearSetImplementationAnalysisAbstract",
    "GearSetImplementationAnalysisDutyCycle",
    "GearSetImplementationDetail",
)
