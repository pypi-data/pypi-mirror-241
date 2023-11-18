"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6986 import AdditionalForcesObtainedFrom
    from ._6987 import BoostPressureLoadCaseInputOptions
    from ._6988 import DesignStateOptions
    from ._6989 import DestinationDesignState
    from ._6990 import ForceInputOptions
    from ._6991 import GearRatioInputOptions
    from ._6992 import LoadCaseNameOptions
    from ._6993 import MomentInputOptions
    from ._6994 import MultiTimeSeriesDataInputFileOptions
    from ._6995 import PointLoadInputOptions
    from ._6996 import PowerLoadInputOptions
    from ._6997 import RampOrSteadyStateInputOptions
    from ._6998 import SpeedInputOptions
    from ._6999 import TimeSeriesImporter
    from ._7000 import TimeStepInputOptions
    from ._7001 import TorqueInputOptions
    from ._7002 import TorqueValuesObtainedFrom
else:
    import_structure = {
        "_6986": ["AdditionalForcesObtainedFrom"],
        "_6987": ["BoostPressureLoadCaseInputOptions"],
        "_6988": ["DesignStateOptions"],
        "_6989": ["DestinationDesignState"],
        "_6990": ["ForceInputOptions"],
        "_6991": ["GearRatioInputOptions"],
        "_6992": ["LoadCaseNameOptions"],
        "_6993": ["MomentInputOptions"],
        "_6994": ["MultiTimeSeriesDataInputFileOptions"],
        "_6995": ["PointLoadInputOptions"],
        "_6996": ["PowerLoadInputOptions"],
        "_6997": ["RampOrSteadyStateInputOptions"],
        "_6998": ["SpeedInputOptions"],
        "_6999": ["TimeSeriesImporter"],
        "_7000": ["TimeStepInputOptions"],
        "_7001": ["TorqueInputOptions"],
        "_7002": ["TorqueValuesObtainedFrom"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AdditionalForcesObtainedFrom",
    "BoostPressureLoadCaseInputOptions",
    "DesignStateOptions",
    "DestinationDesignState",
    "ForceInputOptions",
    "GearRatioInputOptions",
    "LoadCaseNameOptions",
    "MomentInputOptions",
    "MultiTimeSeriesDataInputFileOptions",
    "PointLoadInputOptions",
    "PowerLoadInputOptions",
    "RampOrSteadyStateInputOptions",
    "SpeedInputOptions",
    "TimeSeriesImporter",
    "TimeStepInputOptions",
    "TorqueInputOptions",
    "TorqueValuesObtainedFrom",
)
