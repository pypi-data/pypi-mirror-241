"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1867 import BearingCatalog
    from ._1868 import BasicDynamicLoadRatingCalculationMethod
    from ._1869 import BasicStaticLoadRatingCalculationMethod
    from ._1870 import BearingCageMaterial
    from ._1871 import BearingDampingMatrixOption
    from ._1872 import BearingLoadCaseResultsForPST
    from ._1873 import BearingLoadCaseResultsLightweight
    from ._1874 import BearingMeasurementType
    from ._1875 import BearingModel
    from ._1876 import BearingRow
    from ._1877 import BearingSettings
    from ._1878 import BearingSettingsDatabase
    from ._1879 import BearingSettingsItem
    from ._1880 import BearingStiffnessMatrixOption
    from ._1881 import ExponentAndReductionFactorsInISO16281Calculation
    from ._1882 import FluidFilmTemperatureOptions
    from ._1883 import HybridSteelAll
    from ._1884 import JournalBearingType
    from ._1885 import JournalOilFeedType
    from ._1886 import MountingPointSurfaceFinishes
    from ._1887 import OuterRingMounting
    from ._1888 import RatingLife
    from ._1889 import RollerBearingProfileTypes
    from ._1890 import RollingBearingArrangement
    from ._1891 import RollingBearingDatabase
    from ._1892 import RollingBearingKey
    from ._1893 import RollingBearingRaceType
    from ._1894 import RollingBearingType
    from ._1895 import RotationalDirections
    from ._1896 import SealLocation
    from ._1897 import SKFSettings
    from ._1898 import TiltingPadTypes
else:
    import_structure = {
        "_1867": ["BearingCatalog"],
        "_1868": ["BasicDynamicLoadRatingCalculationMethod"],
        "_1869": ["BasicStaticLoadRatingCalculationMethod"],
        "_1870": ["BearingCageMaterial"],
        "_1871": ["BearingDampingMatrixOption"],
        "_1872": ["BearingLoadCaseResultsForPST"],
        "_1873": ["BearingLoadCaseResultsLightweight"],
        "_1874": ["BearingMeasurementType"],
        "_1875": ["BearingModel"],
        "_1876": ["BearingRow"],
        "_1877": ["BearingSettings"],
        "_1878": ["BearingSettingsDatabase"],
        "_1879": ["BearingSettingsItem"],
        "_1880": ["BearingStiffnessMatrixOption"],
        "_1881": ["ExponentAndReductionFactorsInISO16281Calculation"],
        "_1882": ["FluidFilmTemperatureOptions"],
        "_1883": ["HybridSteelAll"],
        "_1884": ["JournalBearingType"],
        "_1885": ["JournalOilFeedType"],
        "_1886": ["MountingPointSurfaceFinishes"],
        "_1887": ["OuterRingMounting"],
        "_1888": ["RatingLife"],
        "_1889": ["RollerBearingProfileTypes"],
        "_1890": ["RollingBearingArrangement"],
        "_1891": ["RollingBearingDatabase"],
        "_1892": ["RollingBearingKey"],
        "_1893": ["RollingBearingRaceType"],
        "_1894": ["RollingBearingType"],
        "_1895": ["RotationalDirections"],
        "_1896": ["SealLocation"],
        "_1897": ["SKFSettings"],
        "_1898": ["TiltingPadTypes"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BearingCatalog",
    "BasicDynamicLoadRatingCalculationMethod",
    "BasicStaticLoadRatingCalculationMethod",
    "BearingCageMaterial",
    "BearingDampingMatrixOption",
    "BearingLoadCaseResultsForPST",
    "BearingLoadCaseResultsLightweight",
    "BearingMeasurementType",
    "BearingModel",
    "BearingRow",
    "BearingSettings",
    "BearingSettingsDatabase",
    "BearingSettingsItem",
    "BearingStiffnessMatrixOption",
    "ExponentAndReductionFactorsInISO16281Calculation",
    "FluidFilmTemperatureOptions",
    "HybridSteelAll",
    "JournalBearingType",
    "JournalOilFeedType",
    "MountingPointSurfaceFinishes",
    "OuterRingMounting",
    "RatingLife",
    "RollerBearingProfileTypes",
    "RollingBearingArrangement",
    "RollingBearingDatabase",
    "RollingBearingKey",
    "RollingBearingRaceType",
    "RollingBearingType",
    "RotationalDirections",
    "SealLocation",
    "SKFSettings",
    "TiltingPadTypes",
)
