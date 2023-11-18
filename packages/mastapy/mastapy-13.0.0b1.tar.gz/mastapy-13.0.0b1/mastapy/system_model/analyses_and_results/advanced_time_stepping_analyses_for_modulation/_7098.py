"""RingPinsAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7086,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "RingPinsAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2568
    from mastapy.system_model.analyses_and_results.static_loads import _6941
    from mastapy.system_model.analyses_and_results.system_deflections import _2792


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="RingPinsAdvancedTimeSteppingAnalysisForModulation")


class RingPinsAdvancedTimeSteppingAnalysisForModulation(
    _7086.MountableComponentAdvancedTimeSteppingAnalysisForModulation
):
    """RingPinsAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _RING_PINS_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RingPinsAdvancedTimeSteppingAnalysisForModulation"
    )

    class _Cast_RingPinsAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting RingPinsAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "RingPinsAdvancedTimeSteppingAnalysisForModulation._Cast_RingPinsAdvancedTimeSteppingAnalysisForModulation",
            parent: "RingPinsAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(
            self: "RingPinsAdvancedTimeSteppingAnalysisForModulation._Cast_RingPinsAdvancedTimeSteppingAnalysisForModulation",
        ):
            return self._parent._cast(
                _7086.MountableComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "RingPinsAdvancedTimeSteppingAnalysisForModulation._Cast_RingPinsAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7033,
            )

            return self._parent._cast(
                _7033.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "RingPinsAdvancedTimeSteppingAnalysisForModulation._Cast_RingPinsAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7088,
            )

            return self._parent._cast(
                _7088.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "RingPinsAdvancedTimeSteppingAnalysisForModulation._Cast_RingPinsAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RingPinsAdvancedTimeSteppingAnalysisForModulation._Cast_RingPinsAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RingPinsAdvancedTimeSteppingAnalysisForModulation._Cast_RingPinsAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RingPinsAdvancedTimeSteppingAnalysisForModulation._Cast_RingPinsAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsAdvancedTimeSteppingAnalysisForModulation._Cast_RingPinsAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def ring_pins_advanced_time_stepping_analysis_for_modulation(
            self: "RingPinsAdvancedTimeSteppingAnalysisForModulation._Cast_RingPinsAdvancedTimeSteppingAnalysisForModulation",
        ) -> "RingPinsAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "RingPinsAdvancedTimeSteppingAnalysisForModulation._Cast_RingPinsAdvancedTimeSteppingAnalysisForModulation",
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
        self: Self,
        instance_to_wrap: "RingPinsAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2568.RingPins":
        """mastapy.system_model.part_model.cycloidal.RingPins

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6941.RingPinsLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RingPinsLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2792.RingPinsSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.RingPinsSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "RingPinsAdvancedTimeSteppingAnalysisForModulation._Cast_RingPinsAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_RingPinsAdvancedTimeSteppingAnalysisForModulation(self)
