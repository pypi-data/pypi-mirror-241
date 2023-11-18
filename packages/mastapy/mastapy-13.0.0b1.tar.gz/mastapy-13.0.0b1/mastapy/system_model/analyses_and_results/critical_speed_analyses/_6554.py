"""BevelDifferentialPlanetGearCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6551
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "BevelDifferentialPlanetGearCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2515


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialPlanetGearCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialPlanetGearCriticalSpeedAnalysis")


class BevelDifferentialPlanetGearCriticalSpeedAnalysis(
    _6551.BevelDifferentialGearCriticalSpeedAnalysis
):
    """BevelDifferentialPlanetGearCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialPlanetGearCriticalSpeedAnalysis"
    )

    class _Cast_BevelDifferentialPlanetGearCriticalSpeedAnalysis:
        """Special nested class for casting BevelDifferentialPlanetGearCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialPlanetGearCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCriticalSpeedAnalysis",
            parent: "BevelDifferentialPlanetGearCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_critical_speed_analysis(
            self: "BevelDifferentialPlanetGearCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6551.BevelDifferentialGearCriticalSpeedAnalysis)

        @property
        def bevel_gear_critical_speed_analysis(
            self: "BevelDifferentialPlanetGearCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6556,
            )

            return self._parent._cast(_6556.BevelGearCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_critical_speed_analysis(
            self: "BevelDifferentialPlanetGearCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6544,
            )

            return self._parent._cast(_6544.AGMAGleasonConicalGearCriticalSpeedAnalysis)

        @property
        def conical_gear_critical_speed_analysis(
            self: "BevelDifferentialPlanetGearCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6572,
            )

            return self._parent._cast(_6572.ConicalGearCriticalSpeedAnalysis)

        @property
        def gear_critical_speed_analysis(
            self: "BevelDifferentialPlanetGearCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6601,
            )

            return self._parent._cast(_6601.GearCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "BevelDifferentialPlanetGearCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6620,
            )

            return self._parent._cast(_6620.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "BevelDifferentialPlanetGearCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6565,
            )

            return self._parent._cast(_6565.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "BevelDifferentialPlanetGearCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6622,
            )

            return self._parent._cast(_6622.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialPlanetGearCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialPlanetGearCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialPlanetGearCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialPlanetGearCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialPlanetGearCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_critical_speed_analysis(
            self: "BevelDifferentialPlanetGearCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCriticalSpeedAnalysis",
        ) -> "BevelDifferentialPlanetGearCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialPlanetGearCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCriticalSpeedAnalysis",
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
        instance_to_wrap: "BevelDifferentialPlanetGearCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2515.BevelDifferentialPlanetGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear

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
    ) -> "BevelDifferentialPlanetGearCriticalSpeedAnalysis._Cast_BevelDifferentialPlanetGearCriticalSpeedAnalysis":
        return self._Cast_BevelDifferentialPlanetGearCriticalSpeedAnalysis(self)
