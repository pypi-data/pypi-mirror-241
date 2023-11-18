"""SynchroniserHalfCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _4010
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "SynchroniserHalfCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2602
    from mastapy.system_model.analyses_and_results.stability_analyses import _3879


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserHalfCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="SynchroniserHalfCompoundStabilityAnalysis")


class SynchroniserHalfCompoundStabilityAnalysis(
    _4010.SynchroniserPartCompoundStabilityAnalysis
):
    """SynchroniserHalfCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_HALF_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserHalfCompoundStabilityAnalysis"
    )

    class _Cast_SynchroniserHalfCompoundStabilityAnalysis:
        """Special nested class for casting SynchroniserHalfCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserHalfCompoundStabilityAnalysis._Cast_SynchroniserHalfCompoundStabilityAnalysis",
            parent: "SynchroniserHalfCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def synchroniser_part_compound_stability_analysis(
            self: "SynchroniserHalfCompoundStabilityAnalysis._Cast_SynchroniserHalfCompoundStabilityAnalysis",
        ):
            return self._parent._cast(_4010.SynchroniserPartCompoundStabilityAnalysis)

        @property
        def coupling_half_compound_stability_analysis(
            self: "SynchroniserHalfCompoundStabilityAnalysis._Cast_SynchroniserHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3934,
            )

            return self._parent._cast(_3934.CouplingHalfCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(
            self: "SynchroniserHalfCompoundStabilityAnalysis._Cast_SynchroniserHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3972,
            )

            return self._parent._cast(_3972.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "SynchroniserHalfCompoundStabilityAnalysis._Cast_SynchroniserHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3920,
            )

            return self._parent._cast(_3920.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "SynchroniserHalfCompoundStabilityAnalysis._Cast_SynchroniserHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3974,
            )

            return self._parent._cast(_3974.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "SynchroniserHalfCompoundStabilityAnalysis._Cast_SynchroniserHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserHalfCompoundStabilityAnalysis._Cast_SynchroniserHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserHalfCompoundStabilityAnalysis._Cast_SynchroniserHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def synchroniser_half_compound_stability_analysis(
            self: "SynchroniserHalfCompoundStabilityAnalysis._Cast_SynchroniserHalfCompoundStabilityAnalysis",
        ) -> "SynchroniserHalfCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserHalfCompoundStabilityAnalysis._Cast_SynchroniserHalfCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "SynchroniserHalfCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2602.SynchroniserHalf":
        """mastapy.system_model.part_model.couplings.SynchroniserHalf

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
    ) -> "List[_3879.SynchroniserHalfStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.SynchroniserHalfStabilityAnalysis]

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
    ) -> "List[_3879.SynchroniserHalfStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.SynchroniserHalfStabilityAnalysis]

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
    ) -> "SynchroniserHalfCompoundStabilityAnalysis._Cast_SynchroniserHalfCompoundStabilityAnalysis":
        return self._Cast_SynchroniserHalfCompoundStabilityAnalysis(self)
