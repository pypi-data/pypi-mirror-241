"""SpiralBevelGearSetCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4182
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "SpiralBevelGearSetCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2542
    from mastapy.system_model.analyses_and_results.power_flows import _4135
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4263,
        _4264,
    )


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearSetCompoundPowerFlow",)


Self = TypeVar("Self", bound="SpiralBevelGearSetCompoundPowerFlow")


class SpiralBevelGearSetCompoundPowerFlow(_4182.BevelGearSetCompoundPowerFlow):
    """SpiralBevelGearSetCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_SET_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpiralBevelGearSetCompoundPowerFlow")

    class _Cast_SpiralBevelGearSetCompoundPowerFlow:
        """Special nested class for casting SpiralBevelGearSetCompoundPowerFlow to subclasses."""

        def __init__(
            self: "SpiralBevelGearSetCompoundPowerFlow._Cast_SpiralBevelGearSetCompoundPowerFlow",
            parent: "SpiralBevelGearSetCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_power_flow(
            self: "SpiralBevelGearSetCompoundPowerFlow._Cast_SpiralBevelGearSetCompoundPowerFlow",
        ):
            return self._parent._cast(_4182.BevelGearSetCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_set_compound_power_flow(
            self: "SpiralBevelGearSetCompoundPowerFlow._Cast_SpiralBevelGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4170,
            )

            return self._parent._cast(_4170.AGMAGleasonConicalGearSetCompoundPowerFlow)

        @property
        def conical_gear_set_compound_power_flow(
            self: "SpiralBevelGearSetCompoundPowerFlow._Cast_SpiralBevelGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4198,
            )

            return self._parent._cast(_4198.ConicalGearSetCompoundPowerFlow)

        @property
        def gear_set_compound_power_flow(
            self: "SpiralBevelGearSetCompoundPowerFlow._Cast_SpiralBevelGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4224,
            )

            return self._parent._cast(_4224.GearSetCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(
            self: "SpiralBevelGearSetCompoundPowerFlow._Cast_SpiralBevelGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4262,
            )

            return self._parent._cast(_4262.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def abstract_assembly_compound_power_flow(
            self: "SpiralBevelGearSetCompoundPowerFlow._Cast_SpiralBevelGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4164,
            )

            return self._parent._cast(_4164.AbstractAssemblyCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "SpiralBevelGearSetCompoundPowerFlow._Cast_SpiralBevelGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4243,
            )

            return self._parent._cast(_4243.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "SpiralBevelGearSetCompoundPowerFlow._Cast_SpiralBevelGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpiralBevelGearSetCompoundPowerFlow._Cast_SpiralBevelGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearSetCompoundPowerFlow._Cast_SpiralBevelGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_set_compound_power_flow(
            self: "SpiralBevelGearSetCompoundPowerFlow._Cast_SpiralBevelGearSetCompoundPowerFlow",
        ) -> "SpiralBevelGearSetCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearSetCompoundPowerFlow._Cast_SpiralBevelGearSetCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "SpiralBevelGearSetCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2542.SpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.SpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2542.SpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.SpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4135.SpiralBevelGearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.SpiralBevelGearSetPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spiral_bevel_gears_compound_power_flow(
        self: Self,
    ) -> "List[_4263.SpiralBevelGearCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.SpiralBevelGearCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelGearsCompoundPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spiral_bevel_meshes_compound_power_flow(
        self: Self,
    ) -> "List[_4264.SpiralBevelGearMeshCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.SpiralBevelGearMeshCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelMeshesCompoundPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4135.SpiralBevelGearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.SpiralBevelGearSetPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

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
        "SpiralBevelGearSetCompoundPowerFlow._Cast_SpiralBevelGearSetCompoundPowerFlow"
    ):
        return self._Cast_SpiralBevelGearSetCompoundPowerFlow(self)
