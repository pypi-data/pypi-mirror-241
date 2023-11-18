"""ShaftCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6541
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "ShaftCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.shaft_model import _2480
    from mastapy.system_model.analyses_and_results.static_loads import _6948


__docformat__ = "restructuredtext en"
__all__ = ("ShaftCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="ShaftCriticalSpeedAnalysis")


class ShaftCriticalSpeedAnalysis(_6541.AbstractShaftCriticalSpeedAnalysis):
    """ShaftCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftCriticalSpeedAnalysis")

    class _Cast_ShaftCriticalSpeedAnalysis:
        """Special nested class for casting ShaftCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "ShaftCriticalSpeedAnalysis._Cast_ShaftCriticalSpeedAnalysis",
            parent: "ShaftCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_critical_speed_analysis(
            self: "ShaftCriticalSpeedAnalysis._Cast_ShaftCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6541.AbstractShaftCriticalSpeedAnalysis)

        @property
        def abstract_shaft_or_housing_critical_speed_analysis(
            self: "ShaftCriticalSpeedAnalysis._Cast_ShaftCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6542,
            )

            return self._parent._cast(_6542.AbstractShaftOrHousingCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "ShaftCriticalSpeedAnalysis._Cast_ShaftCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6565,
            )

            return self._parent._cast(_6565.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "ShaftCriticalSpeedAnalysis._Cast_ShaftCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6622,
            )

            return self._parent._cast(_6622.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ShaftCriticalSpeedAnalysis._Cast_ShaftCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ShaftCriticalSpeedAnalysis._Cast_ShaftCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ShaftCriticalSpeedAnalysis._Cast_ShaftCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftCriticalSpeedAnalysis._Cast_ShaftCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftCriticalSpeedAnalysis._Cast_ShaftCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def shaft_critical_speed_analysis(
            self: "ShaftCriticalSpeedAnalysis._Cast_ShaftCriticalSpeedAnalysis",
        ) -> "ShaftCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "ShaftCriticalSpeedAnalysis._Cast_ShaftCriticalSpeedAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftCriticalSpeedAnalysis.TYPE"):
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
    def component_load_case(self: Self) -> "_6948.ShaftLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ShaftLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ShaftCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ShaftCriticalSpeedAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "ShaftCriticalSpeedAnalysis._Cast_ShaftCriticalSpeedAnalysis":
        return self._Cast_ShaftCriticalSpeedAnalysis(self)
