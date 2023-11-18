"""CycloidalDiscCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6541
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "CycloidalDiscCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2567
    from mastapy.system_model.analyses_and_results.static_loads import _6857


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="CycloidalDiscCriticalSpeedAnalysis")


class CycloidalDiscCriticalSpeedAnalysis(_6541.AbstractShaftCriticalSpeedAnalysis):
    """CycloidalDiscCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CycloidalDiscCriticalSpeedAnalysis")

    class _Cast_CycloidalDiscCriticalSpeedAnalysis:
        """Special nested class for casting CycloidalDiscCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "CycloidalDiscCriticalSpeedAnalysis._Cast_CycloidalDiscCriticalSpeedAnalysis",
            parent: "CycloidalDiscCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_critical_speed_analysis(
            self: "CycloidalDiscCriticalSpeedAnalysis._Cast_CycloidalDiscCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6541.AbstractShaftCriticalSpeedAnalysis)

        @property
        def abstract_shaft_or_housing_critical_speed_analysis(
            self: "CycloidalDiscCriticalSpeedAnalysis._Cast_CycloidalDiscCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6542,
            )

            return self._parent._cast(_6542.AbstractShaftOrHousingCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "CycloidalDiscCriticalSpeedAnalysis._Cast_CycloidalDiscCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6565,
            )

            return self._parent._cast(_6565.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "CycloidalDiscCriticalSpeedAnalysis._Cast_CycloidalDiscCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6622,
            )

            return self._parent._cast(_6622.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CycloidalDiscCriticalSpeedAnalysis._Cast_CycloidalDiscCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CycloidalDiscCriticalSpeedAnalysis._Cast_CycloidalDiscCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CycloidalDiscCriticalSpeedAnalysis._Cast_CycloidalDiscCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscCriticalSpeedAnalysis._Cast_CycloidalDiscCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCriticalSpeedAnalysis._Cast_CycloidalDiscCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cycloidal_disc_critical_speed_analysis(
            self: "CycloidalDiscCriticalSpeedAnalysis._Cast_CycloidalDiscCriticalSpeedAnalysis",
        ) -> "CycloidalDiscCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCriticalSpeedAnalysis._Cast_CycloidalDiscCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "CycloidalDiscCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2567.CycloidalDisc":
        """mastapy.system_model.part_model.cycloidal.CycloidalDisc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6857.CycloidalDiscLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscCriticalSpeedAnalysis._Cast_CycloidalDiscCriticalSpeedAnalysis":
        return self._Cast_CycloidalDiscCriticalSpeedAnalysis(self)
