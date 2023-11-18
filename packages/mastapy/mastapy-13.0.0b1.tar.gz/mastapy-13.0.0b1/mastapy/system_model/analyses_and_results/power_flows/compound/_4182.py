"""BevelGearSetCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4170
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "BevelGearSetCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4048


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetCompoundPowerFlow",)


Self = TypeVar("Self", bound="BevelGearSetCompoundPowerFlow")


class BevelGearSetCompoundPowerFlow(_4170.AGMAGleasonConicalGearSetCompoundPowerFlow):
    """BevelGearSetCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearSetCompoundPowerFlow")

    class _Cast_BevelGearSetCompoundPowerFlow:
        """Special nested class for casting BevelGearSetCompoundPowerFlow to subclasses."""

        def __init__(
            self: "BevelGearSetCompoundPowerFlow._Cast_BevelGearSetCompoundPowerFlow",
            parent: "BevelGearSetCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_compound_power_flow(
            self: "BevelGearSetCompoundPowerFlow._Cast_BevelGearSetCompoundPowerFlow",
        ):
            return self._parent._cast(_4170.AGMAGleasonConicalGearSetCompoundPowerFlow)

        @property
        def conical_gear_set_compound_power_flow(
            self: "BevelGearSetCompoundPowerFlow._Cast_BevelGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4198,
            )

            return self._parent._cast(_4198.ConicalGearSetCompoundPowerFlow)

        @property
        def gear_set_compound_power_flow(
            self: "BevelGearSetCompoundPowerFlow._Cast_BevelGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4224,
            )

            return self._parent._cast(_4224.GearSetCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(
            self: "BevelGearSetCompoundPowerFlow._Cast_BevelGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4262,
            )

            return self._parent._cast(_4262.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def abstract_assembly_compound_power_flow(
            self: "BevelGearSetCompoundPowerFlow._Cast_BevelGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4164,
            )

            return self._parent._cast(_4164.AbstractAssemblyCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "BevelGearSetCompoundPowerFlow._Cast_BevelGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4243,
            )

            return self._parent._cast(_4243.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "BevelGearSetCompoundPowerFlow._Cast_BevelGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearSetCompoundPowerFlow._Cast_BevelGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSetCompoundPowerFlow._Cast_BevelGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_power_flow(
            self: "BevelGearSetCompoundPowerFlow._Cast_BevelGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4177,
            )

            return self._parent._cast(_4177.BevelDifferentialGearSetCompoundPowerFlow)

        @property
        def spiral_bevel_gear_set_compound_power_flow(
            self: "BevelGearSetCompoundPowerFlow._Cast_BevelGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4265,
            )

            return self._parent._cast(_4265.SpiralBevelGearSetCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_set_compound_power_flow(
            self: "BevelGearSetCompoundPowerFlow._Cast_BevelGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4271,
            )

            return self._parent._cast(_4271.StraightBevelDiffGearSetCompoundPowerFlow)

        @property
        def straight_bevel_gear_set_compound_power_flow(
            self: "BevelGearSetCompoundPowerFlow._Cast_BevelGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4274,
            )

            return self._parent._cast(_4274.StraightBevelGearSetCompoundPowerFlow)

        @property
        def zerol_bevel_gear_set_compound_power_flow(
            self: "BevelGearSetCompoundPowerFlow._Cast_BevelGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4292,
            )

            return self._parent._cast(_4292.ZerolBevelGearSetCompoundPowerFlow)

        @property
        def bevel_gear_set_compound_power_flow(
            self: "BevelGearSetCompoundPowerFlow._Cast_BevelGearSetCompoundPowerFlow",
        ) -> "BevelGearSetCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "BevelGearSetCompoundPowerFlow._Cast_BevelGearSetCompoundPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearSetCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self: Self) -> "List[_4048.BevelGearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.BevelGearSetPowerFlow]

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
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4048.BevelGearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.BevelGearSetPowerFlow]

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
    def cast_to(
        self: Self,
    ) -> "BevelGearSetCompoundPowerFlow._Cast_BevelGearSetCompoundPowerFlow":
        return self._Cast_BevelGearSetCompoundPowerFlow(self)
