"""SynchroniserPartCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4203
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "SynchroniserPartCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4148


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartCompoundPowerFlow",)


Self = TypeVar("Self", bound="SynchroniserPartCompoundPowerFlow")


class SynchroniserPartCompoundPowerFlow(_4203.CouplingHalfCompoundPowerFlow):
    """SynchroniserPartCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserPartCompoundPowerFlow")

    class _Cast_SynchroniserPartCompoundPowerFlow:
        """Special nested class for casting SynchroniserPartCompoundPowerFlow to subclasses."""

        def __init__(
            self: "SynchroniserPartCompoundPowerFlow._Cast_SynchroniserPartCompoundPowerFlow",
            parent: "SynchroniserPartCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_power_flow(
            self: "SynchroniserPartCompoundPowerFlow._Cast_SynchroniserPartCompoundPowerFlow",
        ):
            return self._parent._cast(_4203.CouplingHalfCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "SynchroniserPartCompoundPowerFlow._Cast_SynchroniserPartCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4241,
            )

            return self._parent._cast(_4241.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "SynchroniserPartCompoundPowerFlow._Cast_SynchroniserPartCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4189,
            )

            return self._parent._cast(_4189.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "SynchroniserPartCompoundPowerFlow._Cast_SynchroniserPartCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4243,
            )

            return self._parent._cast(_4243.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "SynchroniserPartCompoundPowerFlow._Cast_SynchroniserPartCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserPartCompoundPowerFlow._Cast_SynchroniserPartCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartCompoundPowerFlow._Cast_SynchroniserPartCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def synchroniser_half_compound_power_flow(
            self: "SynchroniserPartCompoundPowerFlow._Cast_SynchroniserPartCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4278,
            )

            return self._parent._cast(_4278.SynchroniserHalfCompoundPowerFlow)

        @property
        def synchroniser_sleeve_compound_power_flow(
            self: "SynchroniserPartCompoundPowerFlow._Cast_SynchroniserPartCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4280,
            )

            return self._parent._cast(_4280.SynchroniserSleeveCompoundPowerFlow)

        @property
        def synchroniser_part_compound_power_flow(
            self: "SynchroniserPartCompoundPowerFlow._Cast_SynchroniserPartCompoundPowerFlow",
        ) -> "SynchroniserPartCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartCompoundPowerFlow._Cast_SynchroniserPartCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "SynchroniserPartCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_4148.SynchroniserPartPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.SynchroniserPartPowerFlow]

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
    ) -> "List[_4148.SynchroniserPartPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.SynchroniserPartPowerFlow]

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
    ) -> "SynchroniserPartCompoundPowerFlow._Cast_SynchroniserPartCompoundPowerFlow":
        return self._Cast_SynchroniserPartCompoundPowerFlow(self)
