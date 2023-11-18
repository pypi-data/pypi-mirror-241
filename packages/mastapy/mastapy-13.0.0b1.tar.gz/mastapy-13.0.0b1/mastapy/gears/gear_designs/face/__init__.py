"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._987 import FaceGearDesign
    from ._988 import FaceGearDiameterFaceWidthSpecificationMethod
    from ._989 import FaceGearMeshDesign
    from ._990 import FaceGearMeshMicroGeometry
    from ._991 import FaceGearMicroGeometry
    from ._992 import FaceGearPinionDesign
    from ._993 import FaceGearSetDesign
    from ._994 import FaceGearSetMicroGeometry
    from ._995 import FaceGearWheelDesign
else:
    import_structure = {
        "_987": ["FaceGearDesign"],
        "_988": ["FaceGearDiameterFaceWidthSpecificationMethod"],
        "_989": ["FaceGearMeshDesign"],
        "_990": ["FaceGearMeshMicroGeometry"],
        "_991": ["FaceGearMicroGeometry"],
        "_992": ["FaceGearPinionDesign"],
        "_993": ["FaceGearSetDesign"],
        "_994": ["FaceGearSetMicroGeometry"],
        "_995": ["FaceGearWheelDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "FaceGearDesign",
    "FaceGearDiameterFaceWidthSpecificationMethod",
    "FaceGearMeshDesign",
    "FaceGearMeshMicroGeometry",
    "FaceGearMicroGeometry",
    "FaceGearPinionDesign",
    "FaceGearSetDesign",
    "FaceGearSetMicroGeometry",
    "FaceGearWheelDesign",
)
