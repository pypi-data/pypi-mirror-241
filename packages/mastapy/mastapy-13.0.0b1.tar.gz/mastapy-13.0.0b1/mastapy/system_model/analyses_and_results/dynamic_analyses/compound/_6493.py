"""PulleyCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6444
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PULLEY_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "PulleyCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2588
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6364


__docformat__ = "restructuredtext en"
__all__ = ("PulleyCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="PulleyCompoundDynamicAnalysis")


class PulleyCompoundDynamicAnalysis(_6444.CouplingHalfCompoundDynamicAnalysis):
    """PulleyCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _PULLEY_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PulleyCompoundDynamicAnalysis")

    class _Cast_PulleyCompoundDynamicAnalysis:
        """Special nested class for casting PulleyCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "PulleyCompoundDynamicAnalysis._Cast_PulleyCompoundDynamicAnalysis",
            parent: "PulleyCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_dynamic_analysis(
            self: "PulleyCompoundDynamicAnalysis._Cast_PulleyCompoundDynamicAnalysis",
        ):
            return self._parent._cast(_6444.CouplingHalfCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "PulleyCompoundDynamicAnalysis._Cast_PulleyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6482,
            )

            return self._parent._cast(_6482.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "PulleyCompoundDynamicAnalysis._Cast_PulleyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6430,
            )

            return self._parent._cast(_6430.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "PulleyCompoundDynamicAnalysis._Cast_PulleyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6484,
            )

            return self._parent._cast(_6484.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "PulleyCompoundDynamicAnalysis._Cast_PulleyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PulleyCompoundDynamicAnalysis._Cast_PulleyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PulleyCompoundDynamicAnalysis._Cast_PulleyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cvt_pulley_compound_dynamic_analysis(
            self: "PulleyCompoundDynamicAnalysis._Cast_PulleyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6447,
            )

            return self._parent._cast(_6447.CVTPulleyCompoundDynamicAnalysis)

        @property
        def pulley_compound_dynamic_analysis(
            self: "PulleyCompoundDynamicAnalysis._Cast_PulleyCompoundDynamicAnalysis",
        ) -> "PulleyCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "PulleyCompoundDynamicAnalysis._Cast_PulleyCompoundDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PulleyCompoundDynamicAnalysis.TYPE"):
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
    ) -> "List[_6364.PulleyDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.PulleyDynamicAnalysis]

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
    def component_analysis_cases(self: Self) -> "List[_6364.PulleyDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.PulleyDynamicAnalysis]

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
    ) -> "PulleyCompoundDynamicAnalysis._Cast_PulleyCompoundDynamicAnalysis":
        return self._Cast_PulleyCompoundDynamicAnalysis(self)
