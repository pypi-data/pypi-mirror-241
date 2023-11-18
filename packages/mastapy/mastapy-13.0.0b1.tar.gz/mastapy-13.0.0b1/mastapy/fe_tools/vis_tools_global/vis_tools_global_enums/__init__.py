"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1232 import BeamSectionType
    from ._1233 import ContactPairConstrainedSurfaceType
    from ._1234 import ContactPairReferenceSurfaceType
    from ._1235 import ElementPropertiesShellWallType
else:
    import_structure = {
        "_1232": ["BeamSectionType"],
        "_1233": ["ContactPairConstrainedSurfaceType"],
        "_1234": ["ContactPairReferenceSurfaceType"],
        "_1235": ["ElementPropertiesShellWallType"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BeamSectionType",
    "ContactPairConstrainedSurfaceType",
    "ContactPairReferenceSurfaceType",
    "ElementPropertiesShellWallType",
)
