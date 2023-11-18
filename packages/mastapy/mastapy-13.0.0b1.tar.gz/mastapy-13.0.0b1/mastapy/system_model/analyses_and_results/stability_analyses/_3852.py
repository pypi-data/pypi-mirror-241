"""RingPinsStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3840
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "RingPinsStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2568
    from mastapy.system_model.analyses_and_results.static_loads import _6941


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsStabilityAnalysis",)


Self = TypeVar("Self", bound="RingPinsStabilityAnalysis")


class RingPinsStabilityAnalysis(_3840.MountableComponentStabilityAnalysis):
    """RingPinsStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _RING_PINS_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RingPinsStabilityAnalysis")

    class _Cast_RingPinsStabilityAnalysis:
        """Special nested class for casting RingPinsStabilityAnalysis to subclasses."""

        def __init__(
            self: "RingPinsStabilityAnalysis._Cast_RingPinsStabilityAnalysis",
            parent: "RingPinsStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_stability_analysis(
            self: "RingPinsStabilityAnalysis._Cast_RingPinsStabilityAnalysis",
        ):
            return self._parent._cast(_3840.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "RingPinsStabilityAnalysis._Cast_RingPinsStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3786,
            )

            return self._parent._cast(_3786.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "RingPinsStabilityAnalysis._Cast_RingPinsStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3842,
            )

            return self._parent._cast(_3842.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "RingPinsStabilityAnalysis._Cast_RingPinsStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RingPinsStabilityAnalysis._Cast_RingPinsStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RingPinsStabilityAnalysis._Cast_RingPinsStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RingPinsStabilityAnalysis._Cast_RingPinsStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsStabilityAnalysis._Cast_RingPinsStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def ring_pins_stability_analysis(
            self: "RingPinsStabilityAnalysis._Cast_RingPinsStabilityAnalysis",
        ) -> "RingPinsStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "RingPinsStabilityAnalysis._Cast_RingPinsStabilityAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RingPinsStabilityAnalysis.TYPE"):
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
    def cast_to(
        self: Self,
    ) -> "RingPinsStabilityAnalysis._Cast_RingPinsStabilityAnalysis":
        return self._Cast_RingPinsStabilityAnalysis(self)
