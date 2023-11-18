"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1899 import BearingConnectionComponent
    from ._1900 import InternalClearanceClass
    from ._1901 import BearingToleranceClass
    from ._1902 import BearingToleranceDefinitionOptions
    from ._1903 import FitType
    from ._1904 import InnerRingTolerance
    from ._1905 import InnerSupportTolerance
    from ._1906 import InterferenceDetail
    from ._1907 import InterferenceTolerance
    from ._1908 import ITDesignation
    from ._1909 import MountingSleeveDiameterDetail
    from ._1910 import OuterRingTolerance
    from ._1911 import OuterSupportTolerance
    from ._1912 import RaceDetail
    from ._1913 import RaceRoundnessAtAngle
    from ._1914 import RadialSpecificationMethod
    from ._1915 import RingTolerance
    from ._1916 import RoundnessSpecification
    from ._1917 import RoundnessSpecificationType
    from ._1918 import SupportDetail
    from ._1919 import SupportMaterialSource
    from ._1920 import SupportTolerance
    from ._1921 import SupportToleranceLocationDesignation
    from ._1922 import ToleranceCombination
    from ._1923 import TypeOfFit
else:
    import_structure = {
        "_1899": ["BearingConnectionComponent"],
        "_1900": ["InternalClearanceClass"],
        "_1901": ["BearingToleranceClass"],
        "_1902": ["BearingToleranceDefinitionOptions"],
        "_1903": ["FitType"],
        "_1904": ["InnerRingTolerance"],
        "_1905": ["InnerSupportTolerance"],
        "_1906": ["InterferenceDetail"],
        "_1907": ["InterferenceTolerance"],
        "_1908": ["ITDesignation"],
        "_1909": ["MountingSleeveDiameterDetail"],
        "_1910": ["OuterRingTolerance"],
        "_1911": ["OuterSupportTolerance"],
        "_1912": ["RaceDetail"],
        "_1913": ["RaceRoundnessAtAngle"],
        "_1914": ["RadialSpecificationMethod"],
        "_1915": ["RingTolerance"],
        "_1916": ["RoundnessSpecification"],
        "_1917": ["RoundnessSpecificationType"],
        "_1918": ["SupportDetail"],
        "_1919": ["SupportMaterialSource"],
        "_1920": ["SupportTolerance"],
        "_1921": ["SupportToleranceLocationDesignation"],
        "_1922": ["ToleranceCombination"],
        "_1923": ["TypeOfFit"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BearingConnectionComponent",
    "InternalClearanceClass",
    "BearingToleranceClass",
    "BearingToleranceDefinitionOptions",
    "FitType",
    "InnerRingTolerance",
    "InnerSupportTolerance",
    "InterferenceDetail",
    "InterferenceTolerance",
    "ITDesignation",
    "MountingSleeveDiameterDetail",
    "OuterRingTolerance",
    "OuterSupportTolerance",
    "RaceDetail",
    "RaceRoundnessAtAngle",
    "RadialSpecificationMethod",
    "RingTolerance",
    "RoundnessSpecification",
    "RoundnessSpecificationType",
    "SupportDetail",
    "SupportMaterialSource",
    "SupportTolerance",
    "SupportToleranceLocationDesignation",
    "ToleranceCombination",
    "TypeOfFit",
)
