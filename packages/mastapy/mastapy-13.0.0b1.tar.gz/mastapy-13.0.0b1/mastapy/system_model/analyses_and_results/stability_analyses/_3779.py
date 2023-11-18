"""BevelGearStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3767
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "BevelGearStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2517


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearStabilityAnalysis",)


Self = TypeVar("Self", bound="BevelGearStabilityAnalysis")


class BevelGearStabilityAnalysis(_3767.AGMAGleasonConicalGearStabilityAnalysis):
    """BevelGearStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearStabilityAnalysis")

    class _Cast_BevelGearStabilityAnalysis:
        """Special nested class for casting BevelGearStabilityAnalysis to subclasses."""

        def __init__(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
            parent: "BevelGearStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_stability_analysis(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ):
            return self._parent._cast(_3767.AGMAGleasonConicalGearStabilityAnalysis)

        @property
        def conical_gear_stability_analysis(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3795,
            )

            return self._parent._cast(_3795.ConicalGearStabilityAnalysis)

        @property
        def gear_stability_analysis(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3823,
            )

            return self._parent._cast(_3823.GearStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3840,
            )

            return self._parent._cast(_3840.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3786,
            )

            return self._parent._cast(_3786.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3842,
            )

            return self._parent._cast(_3842.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_stability_analysis(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3774,
            )

            return self._parent._cast(_3774.BevelDifferentialGearStabilityAnalysis)

        @property
        def bevel_differential_planet_gear_stability_analysis(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3775,
            )

            return self._parent._cast(
                _3775.BevelDifferentialPlanetGearStabilityAnalysis
            )

        @property
        def bevel_differential_sun_gear_stability_analysis(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3776,
            )

            return self._parent._cast(_3776.BevelDifferentialSunGearStabilityAnalysis)

        @property
        def spiral_bevel_gear_stability_analysis(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3864,
            )

            return self._parent._cast(_3864.SpiralBevelGearStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_stability_analysis(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3873,
            )

            return self._parent._cast(_3873.StraightBevelDiffGearStabilityAnalysis)

        @property
        def straight_bevel_gear_stability_analysis(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3876,
            )

            return self._parent._cast(_3876.StraightBevelGearStabilityAnalysis)

        @property
        def straight_bevel_planet_gear_stability_analysis(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3877,
            )

            return self._parent._cast(_3877.StraightBevelPlanetGearStabilityAnalysis)

        @property
        def straight_bevel_sun_gear_stability_analysis(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3878,
            )

            return self._parent._cast(_3878.StraightBevelSunGearStabilityAnalysis)

        @property
        def zerol_bevel_gear_stability_analysis(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3894,
            )

            return self._parent._cast(_3894.ZerolBevelGearStabilityAnalysis)

        @property
        def bevel_gear_stability_analysis(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
        ) -> "BevelGearStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2517.BevelGear":
        """mastapy.system_model.part_model.gears.BevelGear

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
    ) -> "BevelGearStabilityAnalysis._Cast_BevelGearStabilityAnalysis":
        return self._Cast_BevelGearStabilityAnalysis(self)
