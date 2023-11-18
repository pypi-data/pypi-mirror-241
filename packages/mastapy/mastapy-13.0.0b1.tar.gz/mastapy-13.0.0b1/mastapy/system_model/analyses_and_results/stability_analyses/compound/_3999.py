"""SpringDamperHalfCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3934
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HALF_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "SpringDamperHalfCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2599
    from mastapy.system_model.analyses_and_results.stability_analyses import _3866


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperHalfCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="SpringDamperHalfCompoundStabilityAnalysis")


class SpringDamperHalfCompoundStabilityAnalysis(
    _3934.CouplingHalfCompoundStabilityAnalysis
):
    """SpringDamperHalfCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_HALF_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpringDamperHalfCompoundStabilityAnalysis"
    )

    class _Cast_SpringDamperHalfCompoundStabilityAnalysis:
        """Special nested class for casting SpringDamperHalfCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "SpringDamperHalfCompoundStabilityAnalysis._Cast_SpringDamperHalfCompoundStabilityAnalysis",
            parent: "SpringDamperHalfCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_stability_analysis(
            self: "SpringDamperHalfCompoundStabilityAnalysis._Cast_SpringDamperHalfCompoundStabilityAnalysis",
        ):
            return self._parent._cast(_3934.CouplingHalfCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(
            self: "SpringDamperHalfCompoundStabilityAnalysis._Cast_SpringDamperHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3972,
            )

            return self._parent._cast(_3972.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "SpringDamperHalfCompoundStabilityAnalysis._Cast_SpringDamperHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3920,
            )

            return self._parent._cast(_3920.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "SpringDamperHalfCompoundStabilityAnalysis._Cast_SpringDamperHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3974,
            )

            return self._parent._cast(_3974.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "SpringDamperHalfCompoundStabilityAnalysis._Cast_SpringDamperHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpringDamperHalfCompoundStabilityAnalysis._Cast_SpringDamperHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperHalfCompoundStabilityAnalysis._Cast_SpringDamperHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def spring_damper_half_compound_stability_analysis(
            self: "SpringDamperHalfCompoundStabilityAnalysis._Cast_SpringDamperHalfCompoundStabilityAnalysis",
        ) -> "SpringDamperHalfCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "SpringDamperHalfCompoundStabilityAnalysis._Cast_SpringDamperHalfCompoundStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "SpringDamperHalfCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2599.SpringDamperHalf":
        """mastapy.system_model.part_model.couplings.SpringDamperHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3866.SpringDamperHalfStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.SpringDamperHalfStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3866.SpringDamperHalfStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.SpringDamperHalfStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpringDamperHalfCompoundStabilityAnalysis._Cast_SpringDamperHalfCompoundStabilityAnalysis":
        return self._Cast_SpringDamperHalfCompoundStabilityAnalysis(self)
