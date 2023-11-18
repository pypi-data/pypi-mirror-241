"""ConicalGearPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4091
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "ConicalGearPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2521


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearPowerFlow",)


Self = TypeVar("Self", bound="ConicalGearPowerFlow")


class ConicalGearPowerFlow(_4091.GearPowerFlow):
    """ConicalGearPowerFlow

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearPowerFlow")

    class _Cast_ConicalGearPowerFlow:
        """Special nested class for casting ConicalGearPowerFlow to subclasses."""

        def __init__(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
            parent: "ConicalGearPowerFlow",
        ):
            self._parent = parent

        @property
        def gear_power_flow(self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow"):
            return self._parent._cast(_4091.GearPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4109

            return self._parent._cast(_4109.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4055

            return self._parent._cast(_4055.ComponentPowerFlow)

        @property
        def part_power_flow(self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4111

            return self._parent._cast(_4111.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4035

            return self._parent._cast(_4035.AGMAGleasonConicalGearPowerFlow)

        @property
        def bevel_differential_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4042

            return self._parent._cast(_4042.BevelDifferentialGearPowerFlow)

        @property
        def bevel_differential_planet_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4044

            return self._parent._cast(_4044.BevelDifferentialPlanetGearPowerFlow)

        @property
        def bevel_differential_sun_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4045

            return self._parent._cast(_4045.BevelDifferentialSunGearPowerFlow)

        @property
        def bevel_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4047

            return self._parent._cast(_4047.BevelGearPowerFlow)

        @property
        def hypoid_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4095

            return self._parent._cast(_4095.HypoidGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4099

            return self._parent._cast(
                _4099.KlingelnbergCycloPalloidConicalGearPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4102

            return self._parent._cast(_4102.KlingelnbergCycloPalloidHypoidGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4105

            return self._parent._cast(
                _4105.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow
            )

        @property
        def spiral_bevel_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4134

            return self._parent._cast(_4134.SpiralBevelGearPowerFlow)

        @property
        def straight_bevel_diff_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4140

            return self._parent._cast(_4140.StraightBevelDiffGearPowerFlow)

        @property
        def straight_bevel_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4143

            return self._parent._cast(_4143.StraightBevelGearPowerFlow)

        @property
        def straight_bevel_planet_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4145

            return self._parent._cast(_4145.StraightBevelPlanetGearPowerFlow)

        @property
        def straight_bevel_sun_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4146

            return self._parent._cast(_4146.StraightBevelSunGearPowerFlow)

        @property
        def zerol_bevel_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4162

            return self._parent._cast(_4162.ZerolBevelGearPowerFlow)

        @property
        def conical_gear_power_flow(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow",
        ) -> "ConicalGearPowerFlow":
            return self._parent

        def __getattr__(
            self: "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearPowerFlow.TYPE"):
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
    def cast_to(self: Self) -> "ConicalGearPowerFlow._Cast_ConicalGearPowerFlow":
        return self._Cast_ConicalGearPowerFlow(self)
