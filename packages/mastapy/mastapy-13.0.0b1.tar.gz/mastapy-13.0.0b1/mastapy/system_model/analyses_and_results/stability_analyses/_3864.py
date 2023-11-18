"""SpiralBevelGearStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3779
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "SpiralBevelGearStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2541
    from mastapy.system_model.analyses_and_results.static_loads import _6951


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearStabilityAnalysis",)


Self = TypeVar("Self", bound="SpiralBevelGearStabilityAnalysis")


class SpiralBevelGearStabilityAnalysis(_3779.BevelGearStabilityAnalysis):
    """SpiralBevelGearStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpiralBevelGearStabilityAnalysis")

    class _Cast_SpiralBevelGearStabilityAnalysis:
        """Special nested class for casting SpiralBevelGearStabilityAnalysis to subclasses."""

        def __init__(
            self: "SpiralBevelGearStabilityAnalysis._Cast_SpiralBevelGearStabilityAnalysis",
            parent: "SpiralBevelGearStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_stability_analysis(
            self: "SpiralBevelGearStabilityAnalysis._Cast_SpiralBevelGearStabilityAnalysis",
        ):
            return self._parent._cast(_3779.BevelGearStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_stability_analysis(
            self: "SpiralBevelGearStabilityAnalysis._Cast_SpiralBevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3767,
            )

            return self._parent._cast(_3767.AGMAGleasonConicalGearStabilityAnalysis)

        @property
        def conical_gear_stability_analysis(
            self: "SpiralBevelGearStabilityAnalysis._Cast_SpiralBevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3795,
            )

            return self._parent._cast(_3795.ConicalGearStabilityAnalysis)

        @property
        def gear_stability_analysis(
            self: "SpiralBevelGearStabilityAnalysis._Cast_SpiralBevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3823,
            )

            return self._parent._cast(_3823.GearStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "SpiralBevelGearStabilityAnalysis._Cast_SpiralBevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3840,
            )

            return self._parent._cast(_3840.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "SpiralBevelGearStabilityAnalysis._Cast_SpiralBevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3786,
            )

            return self._parent._cast(_3786.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "SpiralBevelGearStabilityAnalysis._Cast_SpiralBevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3842,
            )

            return self._parent._cast(_3842.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SpiralBevelGearStabilityAnalysis._Cast_SpiralBevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpiralBevelGearStabilityAnalysis._Cast_SpiralBevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpiralBevelGearStabilityAnalysis._Cast_SpiralBevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearStabilityAnalysis._Cast_SpiralBevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearStabilityAnalysis._Cast_SpiralBevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_stability_analysis(
            self: "SpiralBevelGearStabilityAnalysis._Cast_SpiralBevelGearStabilityAnalysis",
        ) -> "SpiralBevelGearStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearStabilityAnalysis._Cast_SpiralBevelGearStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpiralBevelGearStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2541.SpiralBevelGear":
        """mastapy.system_model.part_model.gears.SpiralBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6951.SpiralBevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearLoadCase

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
    ) -> "SpiralBevelGearStabilityAnalysis._Cast_SpiralBevelGearStabilityAnalysis":
        return self._Cast_SpiralBevelGearStabilityAnalysis(self)
