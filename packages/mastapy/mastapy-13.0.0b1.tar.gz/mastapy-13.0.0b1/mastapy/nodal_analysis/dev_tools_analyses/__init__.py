"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._177 import DrawStyleForFE
    from ._178 import EigenvalueOptions
    from ._179 import ElementFaceGroup
    from ._180 import ElementGroup
    from ._181 import FEEntityGroup
    from ._182 import FEEntityGroupInteger
    from ._183 import FEModel
    from ._184 import FEModelComponentDrawStyle
    from ._185 import FEModelHarmonicAnalysisDrawStyle
    from ._186 import FEModelInstanceDrawStyle
    from ._187 import FEModelModalAnalysisDrawStyle
    from ._188 import FEModelPart
    from ._189 import FEModelSetupViewType
    from ._190 import FEModelStaticAnalysisDrawStyle
    from ._191 import FEModelTabDrawStyle
    from ._192 import FEModelTransparencyDrawStyle
    from ._193 import FENodeSelectionDrawStyle
    from ._194 import FESelectionMode
    from ._195 import FESurfaceAndNonDeformedDrawingOption
    from ._196 import FESurfaceDrawingOption
    from ._197 import MassMatrixType
    from ._198 import ModelSplittingMethod
    from ._199 import NodeGroup
    from ._200 import NoneSelectedAllOption
    from ._201 import RigidCouplingType
else:
    import_structure = {
        "_177": ["DrawStyleForFE"],
        "_178": ["EigenvalueOptions"],
        "_179": ["ElementFaceGroup"],
        "_180": ["ElementGroup"],
        "_181": ["FEEntityGroup"],
        "_182": ["FEEntityGroupInteger"],
        "_183": ["FEModel"],
        "_184": ["FEModelComponentDrawStyle"],
        "_185": ["FEModelHarmonicAnalysisDrawStyle"],
        "_186": ["FEModelInstanceDrawStyle"],
        "_187": ["FEModelModalAnalysisDrawStyle"],
        "_188": ["FEModelPart"],
        "_189": ["FEModelSetupViewType"],
        "_190": ["FEModelStaticAnalysisDrawStyle"],
        "_191": ["FEModelTabDrawStyle"],
        "_192": ["FEModelTransparencyDrawStyle"],
        "_193": ["FENodeSelectionDrawStyle"],
        "_194": ["FESelectionMode"],
        "_195": ["FESurfaceAndNonDeformedDrawingOption"],
        "_196": ["FESurfaceDrawingOption"],
        "_197": ["MassMatrixType"],
        "_198": ["ModelSplittingMethod"],
        "_199": ["NodeGroup"],
        "_200": ["NoneSelectedAllOption"],
        "_201": ["RigidCouplingType"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DrawStyleForFE",
    "EigenvalueOptions",
    "ElementFaceGroup",
    "ElementGroup",
    "FEEntityGroup",
    "FEEntityGroupInteger",
    "FEModel",
    "FEModelComponentDrawStyle",
    "FEModelHarmonicAnalysisDrawStyle",
    "FEModelInstanceDrawStyle",
    "FEModelModalAnalysisDrawStyle",
    "FEModelPart",
    "FEModelSetupViewType",
    "FEModelStaticAnalysisDrawStyle",
    "FEModelTabDrawStyle",
    "FEModelTransparencyDrawStyle",
    "FENodeSelectionDrawStyle",
    "FESelectionMode",
    "FESurfaceAndNonDeformedDrawingOption",
    "FESurfaceDrawingOption",
    "MassMatrixType",
    "ModelSplittingMethod",
    "NodeGroup",
    "NoneSelectedAllOption",
    "RigidCouplingType",
)
