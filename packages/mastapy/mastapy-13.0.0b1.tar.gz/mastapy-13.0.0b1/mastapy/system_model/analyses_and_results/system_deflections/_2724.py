"""ConicalGearSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2759
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "ConicalGearSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2521
    from mastapy.gears.ltca.conical import _865
    from mastapy.system_model.analyses_and_results.power_flows import _4063


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSystemDeflection",)


Self = TypeVar("Self", bound="ConicalGearSystemDeflection")


class ConicalGearSystemDeflection(_2759.GearSystemDeflection):
    """ConicalGearSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearSystemDeflection")

    class _Cast_ConicalGearSystemDeflection:
        """Special nested class for casting ConicalGearSystemDeflection to subclasses."""

        def __init__(
            self: "ConicalGearSystemDeflection._Cast_ConicalGearSystemDeflection",
            parent: "ConicalGearSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_system_deflection(
            self: "ConicalGearSystemDeflection._Cast_ConicalGearSystemDeflection",
        ):
            return self._parent._cast(_2759.GearSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "ConicalGearSystemDeflection._Cast_ConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2780,
            )

            return self._parent._cast(_2780.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "ConicalGearSystemDeflection._Cast_ConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2713,
            )

            return self._parent._cast(_2713.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "ConicalGearSystemDeflection._Cast_ConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2783,
            )

            return self._parent._cast(_2783.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "ConicalGearSystemDeflection._Cast_ConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConicalGearSystemDeflection._Cast_ConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConicalGearSystemDeflection._Cast_ConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearSystemDeflection._Cast_ConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearSystemDeflection._Cast_ConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSystemDeflection._Cast_ConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_system_deflection(
            self: "ConicalGearSystemDeflection._Cast_ConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2689,
            )

            return self._parent._cast(_2689.AGMAGleasonConicalGearSystemDeflection)

        @property
        def bevel_differential_gear_system_deflection(
            self: "ConicalGearSystemDeflection._Cast_ConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2701,
            )

            return self._parent._cast(_2701.BevelDifferentialGearSystemDeflection)

        @property
        def bevel_differential_planet_gear_system_deflection(
            self: "ConicalGearSystemDeflection._Cast_ConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2702,
            )

            return self._parent._cast(_2702.BevelDifferentialPlanetGearSystemDeflection)

        @property
        def bevel_differential_sun_gear_system_deflection(
            self: "ConicalGearSystemDeflection._Cast_ConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2703,
            )

            return self._parent._cast(_2703.BevelDifferentialSunGearSystemDeflection)

        @property
        def bevel_gear_system_deflection(
            self: "ConicalGearSystemDeflection._Cast_ConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2706,
            )

            return self._parent._cast(_2706.BevelGearSystemDeflection)

        @property
        def hypoid_gear_system_deflection(
            self: "ConicalGearSystemDeflection._Cast_ConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2763,
            )

            return self._parent._cast(_2763.HypoidGearSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_system_deflection(
            self: "ConicalGearSystemDeflection._Cast_ConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2768,
            )

            return self._parent._cast(
                _2768.KlingelnbergCycloPalloidConicalGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_system_deflection(
            self: "ConicalGearSystemDeflection._Cast_ConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2771,
            )

            return self._parent._cast(
                _2771.KlingelnbergCycloPalloidHypoidGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_system_deflection(
            self: "ConicalGearSystemDeflection._Cast_ConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2774,
            )

            return self._parent._cast(
                _2774.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection
            )

        @property
        def spiral_bevel_gear_system_deflection(
            self: "ConicalGearSystemDeflection._Cast_ConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2807,
            )

            return self._parent._cast(_2807.SpiralBevelGearSystemDeflection)

        @property
        def straight_bevel_diff_gear_system_deflection(
            self: "ConicalGearSystemDeflection._Cast_ConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2813,
            )

            return self._parent._cast(_2813.StraightBevelDiffGearSystemDeflection)

        @property
        def straight_bevel_gear_system_deflection(
            self: "ConicalGearSystemDeflection._Cast_ConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2816,
            )

            return self._parent._cast(_2816.StraightBevelGearSystemDeflection)

        @property
        def straight_bevel_planet_gear_system_deflection(
            self: "ConicalGearSystemDeflection._Cast_ConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2817,
            )

            return self._parent._cast(_2817.StraightBevelPlanetGearSystemDeflection)

        @property
        def straight_bevel_sun_gear_system_deflection(
            self: "ConicalGearSystemDeflection._Cast_ConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2818,
            )

            return self._parent._cast(_2818.StraightBevelSunGearSystemDeflection)

        @property
        def zerol_bevel_gear_system_deflection(
            self: "ConicalGearSystemDeflection._Cast_ConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2839,
            )

            return self._parent._cast(_2839.ZerolBevelGearSystemDeflection)

        @property
        def conical_gear_system_deflection(
            self: "ConicalGearSystemDeflection._Cast_ConicalGearSystemDeflection",
        ) -> "ConicalGearSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConicalGearSystemDeflection._Cast_ConicalGearSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearSystemDeflection.TYPE"):
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
    def conical_gear_ltca_results(
        self: Self,
    ) -> "_865.ConicalGearLoadDistributionAnalysis":
        """mastapy.gears.ltca.conical.ConicalGearLoadDistributionAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearLTCAResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ConicalGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ConicalGearSystemDeflection]

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
    def power_flow_results(self: Self) -> "_4063.ConicalGearPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.ConicalGearPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearSystemDeflection._Cast_ConicalGearSystemDeflection":
        return self._Cast_ConicalGearSystemDeflection(self)
