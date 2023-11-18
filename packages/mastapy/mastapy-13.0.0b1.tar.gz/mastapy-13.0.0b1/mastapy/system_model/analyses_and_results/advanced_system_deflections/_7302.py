"""ConicalGearAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7330
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "ConicalGearAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2521


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="ConicalGearAdvancedSystemDeflection")


class ConicalGearAdvancedSystemDeflection(_7330.GearAdvancedSystemDeflection):
    """ConicalGearAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearAdvancedSystemDeflection")

    class _Cast_ConicalGearAdvancedSystemDeflection:
        """Special nested class for casting ConicalGearAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
            parent: "ConicalGearAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7330.GearAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7350,
            )

            return self._parent._cast(_7350.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7295,
            )

            return self._parent._cast(_7295.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7352,
            )

            return self._parent._cast(_7352.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7274,
            )

            return self._parent._cast(
                _7274.AGMAGleasonConicalGearAdvancedSystemDeflection
            )

        @property
        def bevel_differential_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7281,
            )

            return self._parent._cast(
                _7281.BevelDifferentialGearAdvancedSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7284,
            )

            return self._parent._cast(
                _7284.BevelDifferentialPlanetGearAdvancedSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7285,
            )

            return self._parent._cast(
                _7285.BevelDifferentialSunGearAdvancedSystemDeflection
            )

        @property
        def bevel_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7286,
            )

            return self._parent._cast(_7286.BevelGearAdvancedSystemDeflection)

        @property
        def hypoid_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7334,
            )

            return self._parent._cast(_7334.HypoidGearAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7338,
            )

            return self._parent._cast(
                _7338.KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7341,
            )

            return self._parent._cast(
                _7341.KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7344,
            )

            return self._parent._cast(
                _7344.KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7372,
            )

            return self._parent._cast(_7372.SpiralBevelGearAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7378,
            )

            return self._parent._cast(
                _7378.StraightBevelDiffGearAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7381,
            )

            return self._parent._cast(_7381.StraightBevelGearAdvancedSystemDeflection)

        @property
        def straight_bevel_planet_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7384,
            )

            return self._parent._cast(
                _7384.StraightBevelPlanetGearAdvancedSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7385,
            )

            return self._parent._cast(
                _7385.StraightBevelSunGearAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7400,
            )

            return self._parent._cast(_7400.ZerolBevelGearAdvancedSystemDeflection)

        @property
        def conical_gear_advanced_system_deflection(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
        ) -> "ConicalGearAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "ConicalGearAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2521.ConicalGear":
        """mastapy.system_model.part_model.gears.ConicalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ConicalGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ConicalGearAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> (
        "ConicalGearAdvancedSystemDeflection._Cast_ConicalGearAdvancedSystemDeflection"
    ):
        return self._Cast_ConicalGearAdvancedSystemDeflection(self)
