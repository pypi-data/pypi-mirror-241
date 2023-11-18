"""KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3831
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2538
    from mastapy.system_model.analyses_and_results.static_loads import _6916


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis")


class KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis(
    _3831.KlingelnbergCycloPalloidConicalGearStabilityAnalysis
):
    """KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_stability_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis",
        ):
            return self._parent._cast(
                _3831.KlingelnbergCycloPalloidConicalGearStabilityAnalysis
            )

        @property
        def conical_gear_stability_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3795,
            )

            return self._parent._cast(_3795.ConicalGearStabilityAnalysis)

        @property
        def gear_stability_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3823,
            )

            return self._parent._cast(_3823.GearStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3840,
            )

            return self._parent._cast(_3840.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3786,
            )

            return self._parent._cast(_3786.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3842,
            )

            return self._parent._cast(_3842.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_stability_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2538.KlingelnbergCycloPalloidSpiralBevelGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(
        self: Self,
    ) -> "_6916.KlingelnbergCycloPalloidSpiralBevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearLoadCase

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
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis(self)
