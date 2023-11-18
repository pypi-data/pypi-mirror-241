"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1832 import EnumWithSelectedValue
    from ._1834 import DeletableCollectionMember
    from ._1835 import DutyCyclePropertySummary
    from ._1836 import DutyCyclePropertySummaryForce
    from ._1837 import DutyCyclePropertySummaryPercentage
    from ._1838 import DutyCyclePropertySummarySmallAngle
    from ._1839 import DutyCyclePropertySummaryStress
    from ._1840 import DutyCyclePropertySummaryVeryShortLength
    from ._1841 import EnumWithBoolean
    from ._1842 import NamedRangeWithOverridableMinAndMax
    from ._1843 import TypedObjectsWithOption
else:
    import_structure = {
        "_1832": ["EnumWithSelectedValue"],
        "_1834": ["DeletableCollectionMember"],
        "_1835": ["DutyCyclePropertySummary"],
        "_1836": ["DutyCyclePropertySummaryForce"],
        "_1837": ["DutyCyclePropertySummaryPercentage"],
        "_1838": ["DutyCyclePropertySummarySmallAngle"],
        "_1839": ["DutyCyclePropertySummaryStress"],
        "_1840": ["DutyCyclePropertySummaryVeryShortLength"],
        "_1841": ["EnumWithBoolean"],
        "_1842": ["NamedRangeWithOverridableMinAndMax"],
        "_1843": ["TypedObjectsWithOption"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "EnumWithSelectedValue",
    "DeletableCollectionMember",
    "DutyCyclePropertySummary",
    "DutyCyclePropertySummaryForce",
    "DutyCyclePropertySummaryPercentage",
    "DutyCyclePropertySummarySmallAngle",
    "DutyCyclePropertySummaryStress",
    "DutyCyclePropertySummaryVeryShortLength",
    "EnumWithBoolean",
    "NamedRangeWithOverridableMinAndMax",
    "TypedObjectsWithOption",
)
