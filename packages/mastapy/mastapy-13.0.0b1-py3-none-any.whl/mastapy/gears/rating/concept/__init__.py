"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._546 import ConceptGearDutyCycleRating
    from ._547 import ConceptGearMeshDutyCycleRating
    from ._548 import ConceptGearMeshRating
    from ._549 import ConceptGearRating
    from ._550 import ConceptGearSetDutyCycleRating
    from ._551 import ConceptGearSetRating
else:
    import_structure = {
        "_546": ["ConceptGearDutyCycleRating"],
        "_547": ["ConceptGearMeshDutyCycleRating"],
        "_548": ["ConceptGearMeshRating"],
        "_549": ["ConceptGearRating"],
        "_550": ["ConceptGearSetDutyCycleRating"],
        "_551": ["ConceptGearSetRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConceptGearDutyCycleRating",
    "ConceptGearMeshDutyCycleRating",
    "ConceptGearMeshRating",
    "ConceptGearRating",
    "ConceptGearSetDutyCycleRating",
    "ConceptGearSetRating",
)
