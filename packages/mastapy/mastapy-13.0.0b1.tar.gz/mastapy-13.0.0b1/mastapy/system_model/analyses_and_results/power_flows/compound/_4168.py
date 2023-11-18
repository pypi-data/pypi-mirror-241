"""AGMAGleasonConicalGearCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4196
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "AGMAGleasonConicalGearCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4035


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearCompoundPowerFlow",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearCompoundPowerFlow")


class AGMAGleasonConicalGearCompoundPowerFlow(_4196.ConicalGearCompoundPowerFlow):
    """AGMAGleasonConicalGearCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearCompoundPowerFlow"
    )

    class _Cast_AGMAGleasonConicalGearCompoundPowerFlow:
        """Special nested class for casting AGMAGleasonConicalGearCompoundPowerFlow to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
            parent: "AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def conical_gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            return self._parent._cast(_4196.ConicalGearCompoundPowerFlow)

        @property
        def gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4222,
            )

            return self._parent._cast(_4222.GearCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4241,
            )

            return self._parent._cast(_4241.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4189,
            )

            return self._parent._cast(_4189.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4243,
            )

            return self._parent._cast(_4243.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4175,
            )

            return self._parent._cast(_4175.BevelDifferentialGearCompoundPowerFlow)

        @property
        def bevel_differential_planet_gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4178,
            )

            return self._parent._cast(
                _4178.BevelDifferentialPlanetGearCompoundPowerFlow
            )

        @property
        def bevel_differential_sun_gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4179,
            )

            return self._parent._cast(_4179.BevelDifferentialSunGearCompoundPowerFlow)

        @property
        def bevel_gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4180,
            )

            return self._parent._cast(_4180.BevelGearCompoundPowerFlow)

        @property
        def hypoid_gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4226,
            )

            return self._parent._cast(_4226.HypoidGearCompoundPowerFlow)

        @property
        def spiral_bevel_gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4263,
            )

            return self._parent._cast(_4263.SpiralBevelGearCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4269,
            )

            return self._parent._cast(_4269.StraightBevelDiffGearCompoundPowerFlow)

        @property
        def straight_bevel_gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4272,
            )

            return self._parent._cast(_4272.StraightBevelGearCompoundPowerFlow)

        @property
        def straight_bevel_planet_gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4275,
            )

            return self._parent._cast(_4275.StraightBevelPlanetGearCompoundPowerFlow)

        @property
        def straight_bevel_sun_gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4276,
            )

            return self._parent._cast(_4276.StraightBevelSunGearCompoundPowerFlow)

        @property
        def zerol_bevel_gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4290,
            )

            return self._parent._cast(_4290.ZerolBevelGearCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ) -> "AGMAGleasonConicalGearCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4035.AGMAGleasonConicalGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.AGMAGleasonConicalGearPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4035.AGMAGleasonConicalGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.AGMAGleasonConicalGearPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow":
        return self._Cast_AGMAGleasonConicalGearCompoundPowerFlow(self)
