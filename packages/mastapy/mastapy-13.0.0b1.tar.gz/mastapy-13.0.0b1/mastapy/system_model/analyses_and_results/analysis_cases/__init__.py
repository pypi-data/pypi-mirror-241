"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7532 import AnalysisCase
    from ._7533 import AbstractAnalysisOptions
    from ._7534 import CompoundAnalysisCase
    from ._7535 import ConnectionAnalysisCase
    from ._7536 import ConnectionCompoundAnalysis
    from ._7537 import ConnectionFEAnalysis
    from ._7538 import ConnectionStaticLoadAnalysisCase
    from ._7539 import ConnectionTimeSeriesLoadAnalysisCase
    from ._7540 import DesignEntityCompoundAnalysis
    from ._7541 import FEAnalysis
    from ._7542 import PartAnalysisCase
    from ._7543 import PartCompoundAnalysis
    from ._7544 import PartFEAnalysis
    from ._7545 import PartStaticLoadAnalysisCase
    from ._7546 import PartTimeSeriesLoadAnalysisCase
    from ._7547 import StaticLoadAnalysisCase
    from ._7548 import TimeSeriesLoadAnalysisCase
else:
    import_structure = {
        "_7532": ["AnalysisCase"],
        "_7533": ["AbstractAnalysisOptions"],
        "_7534": ["CompoundAnalysisCase"],
        "_7535": ["ConnectionAnalysisCase"],
        "_7536": ["ConnectionCompoundAnalysis"],
        "_7537": ["ConnectionFEAnalysis"],
        "_7538": ["ConnectionStaticLoadAnalysisCase"],
        "_7539": ["ConnectionTimeSeriesLoadAnalysisCase"],
        "_7540": ["DesignEntityCompoundAnalysis"],
        "_7541": ["FEAnalysis"],
        "_7542": ["PartAnalysisCase"],
        "_7543": ["PartCompoundAnalysis"],
        "_7544": ["PartFEAnalysis"],
        "_7545": ["PartStaticLoadAnalysisCase"],
        "_7546": ["PartTimeSeriesLoadAnalysisCase"],
        "_7547": ["StaticLoadAnalysisCase"],
        "_7548": ["TimeSeriesLoadAnalysisCase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AnalysisCase",
    "AbstractAnalysisOptions",
    "CompoundAnalysisCase",
    "ConnectionAnalysisCase",
    "ConnectionCompoundAnalysis",
    "ConnectionFEAnalysis",
    "ConnectionStaticLoadAnalysisCase",
    "ConnectionTimeSeriesLoadAnalysisCase",
    "DesignEntityCompoundAnalysis",
    "FEAnalysis",
    "PartAnalysisCase",
    "PartCompoundAnalysis",
    "PartFEAnalysis",
    "PartStaticLoadAnalysisCase",
    "PartTimeSeriesLoadAnalysisCase",
    "StaticLoadAnalysisCase",
    "TimeSeriesLoadAnalysisCase",
)
