"""PulleyCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3934
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PULLEY_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "PulleyCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2588
    from mastapy.system_model.analyses_and_results.stability_analyses import _3851


__docformat__ = "restructuredtext en"
__all__ = ("PulleyCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="PulleyCompoundStabilityAnalysis")


class PulleyCompoundStabilityAnalysis(_3934.CouplingHalfCompoundStabilityAnalysis):
    """PulleyCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _PULLEY_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PulleyCompoundStabilityAnalysis")

    class _Cast_PulleyCompoundStabilityAnalysis:
        """Special nested class for casting PulleyCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "PulleyCompoundStabilityAnalysis._Cast_PulleyCompoundStabilityAnalysis",
            parent: "PulleyCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_stability_analysis(
            self: "PulleyCompoundStabilityAnalysis._Cast_PulleyCompoundStabilityAnalysis",
        ):
            return self._parent._cast(_3934.CouplingHalfCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(
            self: "PulleyCompoundStabilityAnalysis._Cast_PulleyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3972,
            )

            return self._parent._cast(_3972.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "PulleyCompoundStabilityAnalysis._Cast_PulleyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3920,
            )

            return self._parent._cast(_3920.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "PulleyCompoundStabilityAnalysis._Cast_PulleyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3974,
            )

            return self._parent._cast(_3974.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "PulleyCompoundStabilityAnalysis._Cast_PulleyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PulleyCompoundStabilityAnalysis._Cast_PulleyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PulleyCompoundStabilityAnalysis._Cast_PulleyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cvt_pulley_compound_stability_analysis(
            self: "PulleyCompoundStabilityAnalysis._Cast_PulleyCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3937,
            )

            return self._parent._cast(_3937.CVTPulleyCompoundStabilityAnalysis)

        @property
        def pulley_compound_stability_analysis(
            self: "PulleyCompoundStabilityAnalysis._Cast_PulleyCompoundStabilityAnalysis",
        ) -> "PulleyCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "PulleyCompoundStabilityAnalysis._Cast_PulleyCompoundStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PulleyCompoundStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2588.Pulley":
        """mastapy.system_model.part_model.couplings.Pulley

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
    ) -> "List[_3851.PulleyStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.PulleyStabilityAnalysis]

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
    def component_analysis_cases(self: Self) -> "List[_3851.PulleyStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.PulleyStabilityAnalysis]

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
    ) -> "PulleyCompoundStabilityAnalysis._Cast_PulleyCompoundStabilityAnalysis":
        return self._Cast_PulleyCompoundStabilityAnalysis(self)
