"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._567 import BiasModification
    from ._568 import FlankMicroGeometry
    from ._569 import FlankSide
    from ._570 import LeadModification
    from ._571 import LocationOfEvaluationLowerLimit
    from ._572 import LocationOfEvaluationUpperLimit
    from ._573 import LocationOfRootReliefEvaluation
    from ._574 import LocationOfTipReliefEvaluation
    from ._575 import MainProfileReliefEndsAtTheStartOfRootReliefOption
    from ._576 import MainProfileReliefEndsAtTheStartOfTipReliefOption
    from ._577 import Modification
    from ._578 import ParabolicRootReliefStartsTangentToMainProfileRelief
    from ._579 import ParabolicTipReliefStartsTangentToMainProfileRelief
    from ._580 import ProfileModification
else:
    import_structure = {
        "_567": ["BiasModification"],
        "_568": ["FlankMicroGeometry"],
        "_569": ["FlankSide"],
        "_570": ["LeadModification"],
        "_571": ["LocationOfEvaluationLowerLimit"],
        "_572": ["LocationOfEvaluationUpperLimit"],
        "_573": ["LocationOfRootReliefEvaluation"],
        "_574": ["LocationOfTipReliefEvaluation"],
        "_575": ["MainProfileReliefEndsAtTheStartOfRootReliefOption"],
        "_576": ["MainProfileReliefEndsAtTheStartOfTipReliefOption"],
        "_577": ["Modification"],
        "_578": ["ParabolicRootReliefStartsTangentToMainProfileRelief"],
        "_579": ["ParabolicTipReliefStartsTangentToMainProfileRelief"],
        "_580": ["ProfileModification"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BiasModification",
    "FlankMicroGeometry",
    "FlankSide",
    "LeadModification",
    "LocationOfEvaluationLowerLimit",
    "LocationOfEvaluationUpperLimit",
    "LocationOfRootReliefEvaluation",
    "LocationOfTipReliefEvaluation",
    "MainProfileReliefEndsAtTheStartOfRootReliefOption",
    "MainProfileReliefEndsAtTheStartOfTipReliefOption",
    "Modification",
    "ParabolicRootReliefStartsTangentToMainProfileRelief",
    "ParabolicTipReliefStartsTangentToMainProfileRelief",
    "ProfileModification",
)
