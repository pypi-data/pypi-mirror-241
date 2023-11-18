"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._819 import BasicConicalGearMachineSettings
    from ._820 import BasicConicalGearMachineSettingsFormate
    from ._821 import BasicConicalGearMachineSettingsGenerated
    from ._822 import CradleStyleConicalMachineSettingsGenerated
else:
    import_structure = {
        "_819": ["BasicConicalGearMachineSettings"],
        "_820": ["BasicConicalGearMachineSettingsFormate"],
        "_821": ["BasicConicalGearMachineSettingsGenerated"],
        "_822": ["CradleStyleConicalMachineSettingsGenerated"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BasicConicalGearMachineSettings",
    "BasicConicalGearMachineSettingsFormate",
    "BasicConicalGearMachineSettingsGenerated",
    "CradleStyleConicalMachineSettingsGenerated",
)
