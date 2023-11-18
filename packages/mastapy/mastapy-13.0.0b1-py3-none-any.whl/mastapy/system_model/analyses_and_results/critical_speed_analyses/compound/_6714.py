"""CVTPulleyCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6760,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "CVTPulleyCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6585


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="CVTPulleyCompoundCriticalSpeedAnalysis")


class CVTPulleyCompoundCriticalSpeedAnalysis(_6760.PulleyCompoundCriticalSpeedAnalysis):
    """CVTPulleyCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTPulleyCompoundCriticalSpeedAnalysis"
    )

    class _Cast_CVTPulleyCompoundCriticalSpeedAnalysis:
        """Special nested class for casting CVTPulleyCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "CVTPulleyCompoundCriticalSpeedAnalysis._Cast_CVTPulleyCompoundCriticalSpeedAnalysis",
            parent: "CVTPulleyCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def pulley_compound_critical_speed_analysis(
            self: "CVTPulleyCompoundCriticalSpeedAnalysis._Cast_CVTPulleyCompoundCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6760.PulleyCompoundCriticalSpeedAnalysis)

        @property
        def coupling_half_compound_critical_speed_analysis(
            self: "CVTPulleyCompoundCriticalSpeedAnalysis._Cast_CVTPulleyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6711,
            )

            return self._parent._cast(_6711.CouplingHalfCompoundCriticalSpeedAnalysis)

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "CVTPulleyCompoundCriticalSpeedAnalysis._Cast_CVTPulleyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6749,
            )

            return self._parent._cast(
                _6749.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "CVTPulleyCompoundCriticalSpeedAnalysis._Cast_CVTPulleyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6697,
            )

            return self._parent._cast(_6697.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "CVTPulleyCompoundCriticalSpeedAnalysis._Cast_CVTPulleyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6751,
            )

            return self._parent._cast(_6751.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "CVTPulleyCompoundCriticalSpeedAnalysis._Cast_CVTPulleyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTPulleyCompoundCriticalSpeedAnalysis._Cast_CVTPulleyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyCompoundCriticalSpeedAnalysis._Cast_CVTPulleyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cvt_pulley_compound_critical_speed_analysis(
            self: "CVTPulleyCompoundCriticalSpeedAnalysis._Cast_CVTPulleyCompoundCriticalSpeedAnalysis",
        ) -> "CVTPulleyCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTPulleyCompoundCriticalSpeedAnalysis._Cast_CVTPulleyCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "CVTPulleyCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6585.CVTPulleyCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.CVTPulleyCriticalSpeedAnalysis]

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
    ) -> "List[_6585.CVTPulleyCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.CVTPulleyCriticalSpeedAnalysis]

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
    ) -> "CVTPulleyCompoundCriticalSpeedAnalysis._Cast_CVTPulleyCompoundCriticalSpeedAnalysis":
        return self._Cast_CVTPulleyCompoundCriticalSpeedAnalysis(self)
