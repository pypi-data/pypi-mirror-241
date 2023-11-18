"""ConceptCouplingStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3800
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "ConceptCouplingStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2579
    from mastapy.system_model.analyses_and_results.static_loads import _6838


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingStabilityAnalysis",)


Self = TypeVar("Self", bound="ConceptCouplingStabilityAnalysis")


class ConceptCouplingStabilityAnalysis(_3800.CouplingStabilityAnalysis):
    """ConceptCouplingStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptCouplingStabilityAnalysis")

    class _Cast_ConceptCouplingStabilityAnalysis:
        """Special nested class for casting ConceptCouplingStabilityAnalysis to subclasses."""

        def __init__(
            self: "ConceptCouplingStabilityAnalysis._Cast_ConceptCouplingStabilityAnalysis",
            parent: "ConceptCouplingStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_stability_analysis(
            self: "ConceptCouplingStabilityAnalysis._Cast_ConceptCouplingStabilityAnalysis",
        ):
            return self._parent._cast(_3800.CouplingStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(
            self: "ConceptCouplingStabilityAnalysis._Cast_ConceptCouplingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3861,
            )

            return self._parent._cast(_3861.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "ConceptCouplingStabilityAnalysis._Cast_ConceptCouplingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3761,
            )

            return self._parent._cast(_3761.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "ConceptCouplingStabilityAnalysis._Cast_ConceptCouplingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3842,
            )

            return self._parent._cast(_3842.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConceptCouplingStabilityAnalysis._Cast_ConceptCouplingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptCouplingStabilityAnalysis._Cast_ConceptCouplingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptCouplingStabilityAnalysis._Cast_ConceptCouplingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingStabilityAnalysis._Cast_ConceptCouplingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingStabilityAnalysis._Cast_ConceptCouplingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def concept_coupling_stability_analysis(
            self: "ConceptCouplingStabilityAnalysis._Cast_ConceptCouplingStabilityAnalysis",
        ) -> "ConceptCouplingStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingStabilityAnalysis._Cast_ConceptCouplingStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptCouplingStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2579.ConceptCoupling":
        """mastapy.system_model.part_model.couplings.ConceptCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6838.ConceptCouplingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptCouplingStabilityAnalysis._Cast_ConceptCouplingStabilityAnalysis":
        return self._Cast_ConceptCouplingStabilityAnalysis(self)
