"""StraightBevelSunGearStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3873
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "StraightBevelSunGearStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2548


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelSunGearStabilityAnalysis",)


Self = TypeVar("Self", bound="StraightBevelSunGearStabilityAnalysis")


class StraightBevelSunGearStabilityAnalysis(
    _3873.StraightBevelDiffGearStabilityAnalysis
):
    """StraightBevelSunGearStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelSunGearStabilityAnalysis"
    )

    class _Cast_StraightBevelSunGearStabilityAnalysis:
        """Special nested class for casting StraightBevelSunGearStabilityAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelSunGearStabilityAnalysis._Cast_StraightBevelSunGearStabilityAnalysis",
            parent: "StraightBevelSunGearStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_stability_analysis(
            self: "StraightBevelSunGearStabilityAnalysis._Cast_StraightBevelSunGearStabilityAnalysis",
        ):
            return self._parent._cast(_3873.StraightBevelDiffGearStabilityAnalysis)

        @property
        def bevel_gear_stability_analysis(
            self: "StraightBevelSunGearStabilityAnalysis._Cast_StraightBevelSunGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3779,
            )

            return self._parent._cast(_3779.BevelGearStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_stability_analysis(
            self: "StraightBevelSunGearStabilityAnalysis._Cast_StraightBevelSunGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3767,
            )

            return self._parent._cast(_3767.AGMAGleasonConicalGearStabilityAnalysis)

        @property
        def conical_gear_stability_analysis(
            self: "StraightBevelSunGearStabilityAnalysis._Cast_StraightBevelSunGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3795,
            )

            return self._parent._cast(_3795.ConicalGearStabilityAnalysis)

        @property
        def gear_stability_analysis(
            self: "StraightBevelSunGearStabilityAnalysis._Cast_StraightBevelSunGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3823,
            )

            return self._parent._cast(_3823.GearStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "StraightBevelSunGearStabilityAnalysis._Cast_StraightBevelSunGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3840,
            )

            return self._parent._cast(_3840.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "StraightBevelSunGearStabilityAnalysis._Cast_StraightBevelSunGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3786,
            )

            return self._parent._cast(_3786.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "StraightBevelSunGearStabilityAnalysis._Cast_StraightBevelSunGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3842,
            )

            return self._parent._cast(_3842.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelSunGearStabilityAnalysis._Cast_StraightBevelSunGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelSunGearStabilityAnalysis._Cast_StraightBevelSunGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelSunGearStabilityAnalysis._Cast_StraightBevelSunGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelSunGearStabilityAnalysis._Cast_StraightBevelSunGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelSunGearStabilityAnalysis._Cast_StraightBevelSunGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def straight_bevel_sun_gear_stability_analysis(
            self: "StraightBevelSunGearStabilityAnalysis._Cast_StraightBevelSunGearStabilityAnalysis",
        ) -> "StraightBevelSunGearStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelSunGearStabilityAnalysis._Cast_StraightBevelSunGearStabilityAnalysis",
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
        self: Self, instance_to_wrap: "StraightBevelSunGearStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2548.StraightBevelSunGear":
        """mastapy.system_model.part_model.gears.StraightBevelSunGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelSunGearStabilityAnalysis._Cast_StraightBevelSunGearStabilityAnalysis":
        return self._Cast_StraightBevelSunGearStabilityAnalysis(self)
