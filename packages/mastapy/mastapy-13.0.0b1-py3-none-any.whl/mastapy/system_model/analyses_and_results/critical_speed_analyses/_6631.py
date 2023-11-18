"""PulleyCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6579
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PULLEY_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "PulleyCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2588
    from mastapy.system_model.analyses_and_results.static_loads import _6938


__docformat__ = "restructuredtext en"
__all__ = ("PulleyCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="PulleyCriticalSpeedAnalysis")


class PulleyCriticalSpeedAnalysis(_6579.CouplingHalfCriticalSpeedAnalysis):
    """PulleyCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _PULLEY_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PulleyCriticalSpeedAnalysis")

    class _Cast_PulleyCriticalSpeedAnalysis:
        """Special nested class for casting PulleyCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "PulleyCriticalSpeedAnalysis._Cast_PulleyCriticalSpeedAnalysis",
            parent: "PulleyCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_critical_speed_analysis(
            self: "PulleyCriticalSpeedAnalysis._Cast_PulleyCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6579.CouplingHalfCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "PulleyCriticalSpeedAnalysis._Cast_PulleyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6620,
            )

            return self._parent._cast(_6620.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "PulleyCriticalSpeedAnalysis._Cast_PulleyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6565,
            )

            return self._parent._cast(_6565.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "PulleyCriticalSpeedAnalysis._Cast_PulleyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6622,
            )

            return self._parent._cast(_6622.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PulleyCriticalSpeedAnalysis._Cast_PulleyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PulleyCriticalSpeedAnalysis._Cast_PulleyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PulleyCriticalSpeedAnalysis._Cast_PulleyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PulleyCriticalSpeedAnalysis._Cast_PulleyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PulleyCriticalSpeedAnalysis._Cast_PulleyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cvt_pulley_critical_speed_analysis(
            self: "PulleyCriticalSpeedAnalysis._Cast_PulleyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6585,
            )

            return self._parent._cast(_6585.CVTPulleyCriticalSpeedAnalysis)

        @property
        def pulley_critical_speed_analysis(
            self: "PulleyCriticalSpeedAnalysis._Cast_PulleyCriticalSpeedAnalysis",
        ) -> "PulleyCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "PulleyCriticalSpeedAnalysis._Cast_PulleyCriticalSpeedAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PulleyCriticalSpeedAnalysis.TYPE"):
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
    def component_load_case(self: Self) -> "_6938.PulleyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PulleyLoadCase

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
    ) -> "PulleyCriticalSpeedAnalysis._Cast_PulleyCriticalSpeedAnalysis":
        return self._Cast_PulleyCriticalSpeedAnalysis(self)
