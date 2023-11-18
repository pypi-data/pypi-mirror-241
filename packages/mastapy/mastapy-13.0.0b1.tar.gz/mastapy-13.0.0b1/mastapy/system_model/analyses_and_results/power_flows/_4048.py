"""BevelGearSetPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4036
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "BevelGearSetPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2518


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetPowerFlow",)


Self = TypeVar("Self", bound="BevelGearSetPowerFlow")


class BevelGearSetPowerFlow(_4036.AGMAGleasonConicalGearSetPowerFlow):
    """BevelGearSetPowerFlow

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearSetPowerFlow")

    class _Cast_BevelGearSetPowerFlow:
        """Special nested class for casting BevelGearSetPowerFlow to subclasses."""

        def __init__(
            self: "BevelGearSetPowerFlow._Cast_BevelGearSetPowerFlow",
            parent: "BevelGearSetPowerFlow",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_power_flow(
            self: "BevelGearSetPowerFlow._Cast_BevelGearSetPowerFlow",
        ):
            return self._parent._cast(_4036.AGMAGleasonConicalGearSetPowerFlow)

        @property
        def conical_gear_set_power_flow(
            self: "BevelGearSetPowerFlow._Cast_BevelGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4064

            return self._parent._cast(_4064.ConicalGearSetPowerFlow)

        @property
        def gear_set_power_flow(
            self: "BevelGearSetPowerFlow._Cast_BevelGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4092

            return self._parent._cast(_4092.GearSetPowerFlow)

        @property
        def specialised_assembly_power_flow(
            self: "BevelGearSetPowerFlow._Cast_BevelGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4132

            return self._parent._cast(_4132.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "BevelGearSetPowerFlow._Cast_BevelGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4030

            return self._parent._cast(_4030.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(self: "BevelGearSetPowerFlow._Cast_BevelGearSetPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4111

            return self._parent._cast(_4111.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "BevelGearSetPowerFlow._Cast_BevelGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelGearSetPowerFlow._Cast_BevelGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(self: "BevelGearSetPowerFlow._Cast_BevelGearSetPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearSetPowerFlow._Cast_BevelGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSetPowerFlow._Cast_BevelGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_power_flow(
            self: "BevelGearSetPowerFlow._Cast_BevelGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4043

            return self._parent._cast(_4043.BevelDifferentialGearSetPowerFlow)

        @property
        def spiral_bevel_gear_set_power_flow(
            self: "BevelGearSetPowerFlow._Cast_BevelGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4135

            return self._parent._cast(_4135.SpiralBevelGearSetPowerFlow)

        @property
        def straight_bevel_diff_gear_set_power_flow(
            self: "BevelGearSetPowerFlow._Cast_BevelGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4141

            return self._parent._cast(_4141.StraightBevelDiffGearSetPowerFlow)

        @property
        def straight_bevel_gear_set_power_flow(
            self: "BevelGearSetPowerFlow._Cast_BevelGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4144

            return self._parent._cast(_4144.StraightBevelGearSetPowerFlow)

        @property
        def zerol_bevel_gear_set_power_flow(
            self: "BevelGearSetPowerFlow._Cast_BevelGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4163

            return self._parent._cast(_4163.ZerolBevelGearSetPowerFlow)

        @property
        def bevel_gear_set_power_flow(
            self: "BevelGearSetPowerFlow._Cast_BevelGearSetPowerFlow",
        ) -> "BevelGearSetPowerFlow":
            return self._parent

        def __getattr__(
            self: "BevelGearSetPowerFlow._Cast_BevelGearSetPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearSetPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2518.BevelGearSet":
        """mastapy.system_model.part_model.gears.BevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "BevelGearSetPowerFlow._Cast_BevelGearSetPowerFlow":
        return self._Cast_BevelGearSetPowerFlow(self)
