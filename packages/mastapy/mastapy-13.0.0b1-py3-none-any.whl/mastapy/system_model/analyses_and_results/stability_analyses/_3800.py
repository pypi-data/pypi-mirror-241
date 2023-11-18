"""CouplingStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3861
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "CouplingStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2581


__docformat__ = "restructuredtext en"
__all__ = ("CouplingStabilityAnalysis",)


Self = TypeVar("Self", bound="CouplingStabilityAnalysis")


class CouplingStabilityAnalysis(_3861.SpecialisedAssemblyStabilityAnalysis):
    """CouplingStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingStabilityAnalysis")

    class _Cast_CouplingStabilityAnalysis:
        """Special nested class for casting CouplingStabilityAnalysis to subclasses."""

        def __init__(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
            parent: "CouplingStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_stability_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ):
            return self._parent._cast(_3861.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3761,
            )

            return self._parent._cast(_3761.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3842,
            )

            return self._parent._cast(_3842.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def clutch_stability_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3784,
            )

            return self._parent._cast(_3784.ClutchStabilityAnalysis)

        @property
        def concept_coupling_stability_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3789,
            )

            return self._parent._cast(_3789.ConceptCouplingStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_stability_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3845,
            )

            return self._parent._cast(_3845.PartToPartShearCouplingStabilityAnalysis)

        @property
        def spring_damper_stability_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3867,
            )

            return self._parent._cast(_3867.SpringDamperStabilityAnalysis)

        @property
        def torque_converter_stability_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3885,
            )

            return self._parent._cast(_3885.TorqueConverterStabilityAnalysis)

        @property
        def coupling_stability_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ) -> "CouplingStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2581.Coupling":
        """mastapy.system_model.part_model.couplings.Coupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis":
        return self._Cast_CouplingStabilityAnalysis(self)
