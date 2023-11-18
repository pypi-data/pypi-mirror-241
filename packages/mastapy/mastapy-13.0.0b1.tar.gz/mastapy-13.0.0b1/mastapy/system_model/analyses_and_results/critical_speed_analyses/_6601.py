"""GearCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6620
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "GearCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2528


__docformat__ = "restructuredtext en"
__all__ = ("GearCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="GearCriticalSpeedAnalysis")


class GearCriticalSpeedAnalysis(_6620.MountableComponentCriticalSpeedAnalysis):
    """GearCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearCriticalSpeedAnalysis")

    class _Cast_GearCriticalSpeedAnalysis:
        """Special nested class for casting GearCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
            parent: "GearCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6620.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6565,
            )

            return self._parent._cast(_6565.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6622,
            )

            return self._parent._cast(_6622.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6544,
            )

            return self._parent._cast(_6544.AGMAGleasonConicalGearCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6551,
            )

            return self._parent._cast(_6551.BevelDifferentialGearCriticalSpeedAnalysis)

        @property
        def bevel_differential_planet_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6554,
            )

            return self._parent._cast(
                _6554.BevelDifferentialPlanetGearCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_sun_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6555,
            )

            return self._parent._cast(
                _6555.BevelDifferentialSunGearCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6556,
            )

            return self._parent._cast(_6556.BevelGearCriticalSpeedAnalysis)

        @property
        def concept_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6569,
            )

            return self._parent._cast(_6569.ConceptGearCriticalSpeedAnalysis)

        @property
        def conical_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6572,
            )

            return self._parent._cast(_6572.ConicalGearCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6590,
            )

            return self._parent._cast(_6590.CylindricalGearCriticalSpeedAnalysis)

        @property
        def cylindrical_planet_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6593,
            )

            return self._parent._cast(_6593.CylindricalPlanetGearCriticalSpeedAnalysis)

        @property
        def face_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6596,
            )

            return self._parent._cast(_6596.FaceGearCriticalSpeedAnalysis)

        @property
        def hypoid_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6605,
            )

            return self._parent._cast(_6605.HypoidGearCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6609,
            )

            return self._parent._cast(
                _6609.KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6612,
            )

            return self._parent._cast(
                _6612.KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6615,
            )

            return self._parent._cast(
                _6615.KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6642,
            )

            return self._parent._cast(_6642.SpiralBevelGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6648,
            )

            return self._parent._cast(_6648.StraightBevelDiffGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6651,
            )

            return self._parent._cast(_6651.StraightBevelGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_planet_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6654,
            )

            return self._parent._cast(
                _6654.StraightBevelPlanetGearCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_sun_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6655,
            )

            return self._parent._cast(_6655.StraightBevelSunGearCriticalSpeedAnalysis)

        @property
        def worm_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6666,
            )

            return self._parent._cast(_6666.WormGearCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6669,
            )

            return self._parent._cast(_6669.ZerolBevelGearCriticalSpeedAnalysis)

        @property
        def gear_critical_speed_analysis(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis",
        ) -> "GearCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearCriticalSpeedAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2528.Gear":
        """mastapy.system_model.part_model.gears.Gear

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
    ) -> "GearCriticalSpeedAnalysis._Cast_GearCriticalSpeedAnalysis":
        return self._Cast_GearCriticalSpeedAnalysis(self)
