"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5841 import ConnectedComponentType
    from ._5842 import ExcitationSourceSelection
    from ._5843 import ExcitationSourceSelectionBase
    from ._5844 import ExcitationSourceSelectionGroup
    from ._5845 import HarmonicSelection
    from ._5846 import ModalContributionDisplayMethod
    from ._5847 import ModalContributionFilteringMethod
    from ._5848 import ResultLocationSelectionGroup
    from ._5849 import ResultLocationSelectionGroups
    from ._5850 import ResultNodeSelection
else:
    import_structure = {
        "_5841": ["ConnectedComponentType"],
        "_5842": ["ExcitationSourceSelection"],
        "_5843": ["ExcitationSourceSelectionBase"],
        "_5844": ["ExcitationSourceSelectionGroup"],
        "_5845": ["HarmonicSelection"],
        "_5846": ["ModalContributionDisplayMethod"],
        "_5847": ["ModalContributionFilteringMethod"],
        "_5848": ["ResultLocationSelectionGroup"],
        "_5849": ["ResultLocationSelectionGroups"],
        "_5850": ["ResultNodeSelection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConnectedComponentType",
    "ExcitationSourceSelection",
    "ExcitationSourceSelectionBase",
    "ExcitationSourceSelectionGroup",
    "HarmonicSelection",
    "ModalContributionDisplayMethod",
    "ModalContributionFilteringMethod",
    "ResultLocationSelectionGroup",
    "ResultLocationSelectionGroups",
    "ResultNodeSelection",
)
