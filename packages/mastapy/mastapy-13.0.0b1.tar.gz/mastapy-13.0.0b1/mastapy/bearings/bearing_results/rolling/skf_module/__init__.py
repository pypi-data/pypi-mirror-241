"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2074 import AdjustedSpeed
    from ._2075 import AdjustmentFactors
    from ._2076 import BearingLoads
    from ._2077 import BearingRatingLife
    from ._2078 import DynamicAxialLoadCarryingCapacity
    from ._2079 import Frequencies
    from ._2080 import FrequencyOfOverRolling
    from ._2081 import Friction
    from ._2082 import FrictionalMoment
    from ._2083 import FrictionSources
    from ._2084 import Grease
    from ._2085 import GreaseLifeAndRelubricationInterval
    from ._2086 import GreaseQuantity
    from ._2087 import InitialFill
    from ._2088 import LifeModel
    from ._2089 import MinimumLoad
    from ._2090 import OperatingViscosity
    from ._2091 import PermissibleAxialLoad
    from ._2092 import RotationalFrequency
    from ._2093 import SKFAuthentication
    from ._2094 import SKFCalculationResult
    from ._2095 import SKFCredentials
    from ._2096 import SKFModuleResults
    from ._2097 import StaticSafetyFactors
    from ._2098 import Viscosities
else:
    import_structure = {
        "_2074": ["AdjustedSpeed"],
        "_2075": ["AdjustmentFactors"],
        "_2076": ["BearingLoads"],
        "_2077": ["BearingRatingLife"],
        "_2078": ["DynamicAxialLoadCarryingCapacity"],
        "_2079": ["Frequencies"],
        "_2080": ["FrequencyOfOverRolling"],
        "_2081": ["Friction"],
        "_2082": ["FrictionalMoment"],
        "_2083": ["FrictionSources"],
        "_2084": ["Grease"],
        "_2085": ["GreaseLifeAndRelubricationInterval"],
        "_2086": ["GreaseQuantity"],
        "_2087": ["InitialFill"],
        "_2088": ["LifeModel"],
        "_2089": ["MinimumLoad"],
        "_2090": ["OperatingViscosity"],
        "_2091": ["PermissibleAxialLoad"],
        "_2092": ["RotationalFrequency"],
        "_2093": ["SKFAuthentication"],
        "_2094": ["SKFCalculationResult"],
        "_2095": ["SKFCredentials"],
        "_2096": ["SKFModuleResults"],
        "_2097": ["StaticSafetyFactors"],
        "_2098": ["Viscosities"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AdjustedSpeed",
    "AdjustmentFactors",
    "BearingLoads",
    "BearingRatingLife",
    "DynamicAxialLoadCarryingCapacity",
    "Frequencies",
    "FrequencyOfOverRolling",
    "Friction",
    "FrictionalMoment",
    "FrictionSources",
    "Grease",
    "GreaseLifeAndRelubricationInterval",
    "GreaseQuantity",
    "InitialFill",
    "LifeModel",
    "MinimumLoad",
    "OperatingViscosity",
    "PermissibleAxialLoad",
    "RotationalFrequency",
    "SKFAuthentication",
    "SKFCalculationResult",
    "SKFCredentials",
    "SKFModuleResults",
    "StaticSafetyFactors",
    "Viscosities",
)
