"""AGMAGleasonConicalGearCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6572
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "AGMAGleasonConicalGearCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2511


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearCriticalSpeedAnalysis")


class AGMAGleasonConicalGearCriticalSpeedAnalysis(
    _6572.ConicalGearCriticalSpeedAnalysis
):
    """AGMAGleasonConicalGearCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
            parent: "AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6572.ConicalGearCriticalSpeedAnalysis)

        @property
        def gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6601,
            )

            return self._parent._cast(_6601.GearCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6620,
            )

            return self._parent._cast(_6620.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6565,
            )

            return self._parent._cast(_6565.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6622,
            )

            return self._parent._cast(_6622.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6551,
            )

            return self._parent._cast(_6551.BevelDifferentialGearCriticalSpeedAnalysis)

        @property
        def bevel_differential_planet_gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6554,
            )

            return self._parent._cast(
                _6554.BevelDifferentialPlanetGearCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_sun_gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6555,
            )

            return self._parent._cast(
                _6555.BevelDifferentialSunGearCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6556,
            )

            return self._parent._cast(_6556.BevelGearCriticalSpeedAnalysis)

        @property
        def hypoid_gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6605,
            )

            return self._parent._cast(_6605.HypoidGearCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6642,
            )

            return self._parent._cast(_6642.SpiralBevelGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6648,
            )

            return self._parent._cast(_6648.StraightBevelDiffGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6651,
            )

            return self._parent._cast(_6651.StraightBevelGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_planet_gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6654,
            )

            return self._parent._cast(
                _6654.StraightBevelPlanetGearCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_sun_gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6655,
            )

            return self._parent._cast(_6655.StraightBevelSunGearCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6669,
            )

            return self._parent._cast(_6669.ZerolBevelGearCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
        ) -> "AGMAGleasonConicalGearCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2511.AGMAGleasonConicalGear":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGear

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
    ) -> "AGMAGleasonConicalGearCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis":
        return self._Cast_AGMAGleasonConicalGearCriticalSpeedAnalysis(self)
