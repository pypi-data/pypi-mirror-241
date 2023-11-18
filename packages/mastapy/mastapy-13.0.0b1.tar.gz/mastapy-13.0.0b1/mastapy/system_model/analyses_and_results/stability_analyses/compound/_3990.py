"""ShaftCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3896
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "ShaftCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.shaft_model import _2480
    from mastapy.system_model.analyses_and_results.stability_analyses import _3859


__docformat__ = "restructuredtext en"
__all__ = ("ShaftCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="ShaftCompoundStabilityAnalysis")


class ShaftCompoundStabilityAnalysis(_3896.AbstractShaftCompoundStabilityAnalysis):
    """ShaftCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftCompoundStabilityAnalysis")

    class _Cast_ShaftCompoundStabilityAnalysis:
        """Special nested class for casting ShaftCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "ShaftCompoundStabilityAnalysis._Cast_ShaftCompoundStabilityAnalysis",
            parent: "ShaftCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_compound_stability_analysis(
            self: "ShaftCompoundStabilityAnalysis._Cast_ShaftCompoundStabilityAnalysis",
        ):
            return self._parent._cast(_3896.AbstractShaftCompoundStabilityAnalysis)

        @property
        def abstract_shaft_or_housing_compound_stability_analysis(
            self: "ShaftCompoundStabilityAnalysis._Cast_ShaftCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3897,
            )

            return self._parent._cast(
                _3897.AbstractShaftOrHousingCompoundStabilityAnalysis
            )

        @property
        def component_compound_stability_analysis(
            self: "ShaftCompoundStabilityAnalysis._Cast_ShaftCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3920,
            )

            return self._parent._cast(_3920.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "ShaftCompoundStabilityAnalysis._Cast_ShaftCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3974,
            )

            return self._parent._cast(_3974.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "ShaftCompoundStabilityAnalysis._Cast_ShaftCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ShaftCompoundStabilityAnalysis._Cast_ShaftCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftCompoundStabilityAnalysis._Cast_ShaftCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def shaft_compound_stability_analysis(
            self: "ShaftCompoundStabilityAnalysis._Cast_ShaftCompoundStabilityAnalysis",
        ) -> "ShaftCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ShaftCompoundStabilityAnalysis._Cast_ShaftCompoundStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftCompoundStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2480.Shaft":
        """mastapy.system_model.part_model.shaft_model.Shaft

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
    ) -> "List[_3859.ShaftStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ShaftStabilityAnalysis]

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
    def planetaries(self: Self) -> "List[ShaftCompoundStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.compound.ShaftCompoundStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(self: Self) -> "List[_3859.ShaftStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ShaftStabilityAnalysis]

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
    ) -> "ShaftCompoundStabilityAnalysis._Cast_ShaftCompoundStabilityAnalysis":
        return self._Cast_ShaftCompoundStabilityAnalysis(self)
