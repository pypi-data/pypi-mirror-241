"""HypoidGearSetPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4036
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "HypoidGearSetPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2533
    from mastapy.system_model.analyses_and_results.static_loads import _6905
    from mastapy.gears.rating.hypoid import _438
    from mastapy.system_model.analyses_and_results.power_flows import _4095, _4094


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearSetPowerFlow",)


Self = TypeVar("Self", bound="HypoidGearSetPowerFlow")


class HypoidGearSetPowerFlow(_4036.AGMAGleasonConicalGearSetPowerFlow):
    """HypoidGearSetPowerFlow

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearSetPowerFlow")

    class _Cast_HypoidGearSetPowerFlow:
        """Special nested class for casting HypoidGearSetPowerFlow to subclasses."""

        def __init__(
            self: "HypoidGearSetPowerFlow._Cast_HypoidGearSetPowerFlow",
            parent: "HypoidGearSetPowerFlow",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_power_flow(
            self: "HypoidGearSetPowerFlow._Cast_HypoidGearSetPowerFlow",
        ):
            return self._parent._cast(_4036.AGMAGleasonConicalGearSetPowerFlow)

        @property
        def conical_gear_set_power_flow(
            self: "HypoidGearSetPowerFlow._Cast_HypoidGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4064

            return self._parent._cast(_4064.ConicalGearSetPowerFlow)

        @property
        def gear_set_power_flow(
            self: "HypoidGearSetPowerFlow._Cast_HypoidGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4092

            return self._parent._cast(_4092.GearSetPowerFlow)

        @property
        def specialised_assembly_power_flow(
            self: "HypoidGearSetPowerFlow._Cast_HypoidGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4132

            return self._parent._cast(_4132.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "HypoidGearSetPowerFlow._Cast_HypoidGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4030

            return self._parent._cast(_4030.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(
            self: "HypoidGearSetPowerFlow._Cast_HypoidGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4111

            return self._parent._cast(_4111.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "HypoidGearSetPowerFlow._Cast_HypoidGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "HypoidGearSetPowerFlow._Cast_HypoidGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(self: "HypoidGearSetPowerFlow._Cast_HypoidGearSetPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearSetPowerFlow._Cast_HypoidGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearSetPowerFlow._Cast_HypoidGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def hypoid_gear_set_power_flow(
            self: "HypoidGearSetPowerFlow._Cast_HypoidGearSetPowerFlow",
        ) -> "HypoidGearSetPowerFlow":
            return self._parent

        def __getattr__(
            self: "HypoidGearSetPowerFlow._Cast_HypoidGearSetPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearSetPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2533.HypoidGearSet":
        """mastapy.system_model.part_model.gears.HypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6905.HypoidGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating(self: Self) -> "_438.HypoidGearSetRating":
        """mastapy.gears.rating.hypoid.HypoidGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_438.HypoidGearSetRating":
        """mastapy.gears.rating.hypoid.HypoidGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears_power_flow(self: Self) -> "List[_4095.HypoidGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.HypoidGearPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearsPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_gears_power_flow(self: Self) -> "List[_4095.HypoidGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.HypoidGearPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearsPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_power_flow(self: Self) -> "List[_4094.HypoidGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.HypoidGearMeshPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshesPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_meshes_power_flow(self: Self) -> "List[_4094.HypoidGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.HypoidGearMeshPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidMeshesPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "HypoidGearSetPowerFlow._Cast_HypoidGearSetPowerFlow":
        return self._Cast_HypoidGearSetPowerFlow(self)
