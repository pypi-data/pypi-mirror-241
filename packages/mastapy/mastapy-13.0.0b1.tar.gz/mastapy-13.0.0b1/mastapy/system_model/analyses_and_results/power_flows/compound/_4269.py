"""StraightBevelDiffGearCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4180
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "StraightBevelDiffGearCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2543
    from mastapy.system_model.analyses_and_results.power_flows import _4140


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearCompoundPowerFlow",)


Self = TypeVar("Self", bound="StraightBevelDiffGearCompoundPowerFlow")


class StraightBevelDiffGearCompoundPowerFlow(_4180.BevelGearCompoundPowerFlow):
    """StraightBevelDiffGearCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearCompoundPowerFlow"
    )

    class _Cast_StraightBevelDiffGearCompoundPowerFlow:
        """Special nested class for casting StraightBevelDiffGearCompoundPowerFlow to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearCompoundPowerFlow._Cast_StraightBevelDiffGearCompoundPowerFlow",
            parent: "StraightBevelDiffGearCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_power_flow(
            self: "StraightBevelDiffGearCompoundPowerFlow._Cast_StraightBevelDiffGearCompoundPowerFlow",
        ):
            return self._parent._cast(_4180.BevelGearCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_compound_power_flow(
            self: "StraightBevelDiffGearCompoundPowerFlow._Cast_StraightBevelDiffGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4168,
            )

            return self._parent._cast(_4168.AGMAGleasonConicalGearCompoundPowerFlow)

        @property
        def conical_gear_compound_power_flow(
            self: "StraightBevelDiffGearCompoundPowerFlow._Cast_StraightBevelDiffGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4196,
            )

            return self._parent._cast(_4196.ConicalGearCompoundPowerFlow)

        @property
        def gear_compound_power_flow(
            self: "StraightBevelDiffGearCompoundPowerFlow._Cast_StraightBevelDiffGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4222,
            )

            return self._parent._cast(_4222.GearCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "StraightBevelDiffGearCompoundPowerFlow._Cast_StraightBevelDiffGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4241,
            )

            return self._parent._cast(_4241.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "StraightBevelDiffGearCompoundPowerFlow._Cast_StraightBevelDiffGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4189,
            )

            return self._parent._cast(_4189.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "StraightBevelDiffGearCompoundPowerFlow._Cast_StraightBevelDiffGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4243,
            )

            return self._parent._cast(_4243.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "StraightBevelDiffGearCompoundPowerFlow._Cast_StraightBevelDiffGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelDiffGearCompoundPowerFlow._Cast_StraightBevelDiffGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearCompoundPowerFlow._Cast_StraightBevelDiffGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_power_flow(
            self: "StraightBevelDiffGearCompoundPowerFlow._Cast_StraightBevelDiffGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4275,
            )

            return self._parent._cast(_4275.StraightBevelPlanetGearCompoundPowerFlow)

        @property
        def straight_bevel_sun_gear_compound_power_flow(
            self: "StraightBevelDiffGearCompoundPowerFlow._Cast_StraightBevelDiffGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4276,
            )

            return self._parent._cast(_4276.StraightBevelSunGearCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_compound_power_flow(
            self: "StraightBevelDiffGearCompoundPowerFlow._Cast_StraightBevelDiffGearCompoundPowerFlow",
        ) -> "StraightBevelDiffGearCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearCompoundPowerFlow._Cast_StraightBevelDiffGearCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "StraightBevelDiffGearCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2543.StraightBevelDiffGear":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4140.StraightBevelDiffGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.StraightBevelDiffGearPowerFlow]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4140.StraightBevelDiffGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.StraightBevelDiffGearPowerFlow]

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
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearCompoundPowerFlow._Cast_StraightBevelDiffGearCompoundPowerFlow":
        return self._Cast_StraightBevelDiffGearCompoundPowerFlow(self)
