"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5669 import AbstractAssemblyStaticLoadCaseGroup
    from ._5670 import ComponentStaticLoadCaseGroup
    from ._5671 import ConnectionStaticLoadCaseGroup
    from ._5672 import DesignEntityStaticLoadCaseGroup
    from ._5673 import GearSetStaticLoadCaseGroup
    from ._5674 import PartStaticLoadCaseGroup
else:
    import_structure = {
        "_5669": ["AbstractAssemblyStaticLoadCaseGroup"],
        "_5670": ["ComponentStaticLoadCaseGroup"],
        "_5671": ["ConnectionStaticLoadCaseGroup"],
        "_5672": ["DesignEntityStaticLoadCaseGroup"],
        "_5673": ["GearSetStaticLoadCaseGroup"],
        "_5674": ["PartStaticLoadCaseGroup"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyStaticLoadCaseGroup",
    "ComponentStaticLoadCaseGroup",
    "ConnectionStaticLoadCaseGroup",
    "DesignEntityStaticLoadCaseGroup",
    "GearSetStaticLoadCaseGroup",
    "PartStaticLoadCaseGroup",
)
