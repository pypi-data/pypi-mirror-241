"""AGMAGleasonConicalGearSetPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4064
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "AGMAGleasonConicalGearSetPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2512


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetPowerFlow",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetPowerFlow")


class AGMAGleasonConicalGearSetPowerFlow(_4064.ConicalGearSetPowerFlow):
    """AGMAGleasonConicalGearSetPowerFlow

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalGearSetPowerFlow")

    class _Cast_AGMAGleasonConicalGearSetPowerFlow:
        """Special nested class for casting AGMAGleasonConicalGearSetPowerFlow to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow",
            parent: "AGMAGleasonConicalGearSetPowerFlow",
        ):
            self._parent = parent

        @property
        def conical_gear_set_power_flow(
            self: "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow",
        ):
            return self._parent._cast(_4064.ConicalGearSetPowerFlow)

        @property
        def gear_set_power_flow(
            self: "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4092

            return self._parent._cast(_4092.GearSetPowerFlow)

        @property
        def specialised_assembly_power_flow(
            self: "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4132

            return self._parent._cast(_4132.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4030

            return self._parent._cast(_4030.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(
            self: "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4111

            return self._parent._cast(_4111.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_power_flow(
            self: "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4043

            return self._parent._cast(_4043.BevelDifferentialGearSetPowerFlow)

        @property
        def bevel_gear_set_power_flow(
            self: "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4048

            return self._parent._cast(_4048.BevelGearSetPowerFlow)

        @property
        def hypoid_gear_set_power_flow(
            self: "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4096

            return self._parent._cast(_4096.HypoidGearSetPowerFlow)

        @property
        def spiral_bevel_gear_set_power_flow(
            self: "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4135

            return self._parent._cast(_4135.SpiralBevelGearSetPowerFlow)

        @property
        def straight_bevel_diff_gear_set_power_flow(
            self: "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4141

            return self._parent._cast(_4141.StraightBevelDiffGearSetPowerFlow)

        @property
        def straight_bevel_gear_set_power_flow(
            self: "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4144

            return self._parent._cast(_4144.StraightBevelGearSetPowerFlow)

        @property
        def zerol_bevel_gear_set_power_flow(
            self: "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4163

            return self._parent._cast(_4163.ZerolBevelGearSetPowerFlow)

        @property
        def agma_gleason_conical_gear_set_power_flow(
            self: "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow",
        ) -> "AGMAGleasonConicalGearSetPowerFlow":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearSetPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2512.AGMAGleasonConicalGearSet":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearSetPowerFlow._Cast_AGMAGleasonConicalGearSetPowerFlow":
        return self._Cast_AGMAGleasonConicalGearSetPowerFlow(self)
