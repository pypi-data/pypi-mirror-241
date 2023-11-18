"""SpringDamperConnectionCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4202
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "SpringDamperConnectionCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2348
    from mastapy.system_model.analyses_and_results.power_flows import _4136


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperConnectionCompoundPowerFlow",)


Self = TypeVar("Self", bound="SpringDamperConnectionCompoundPowerFlow")


class SpringDamperConnectionCompoundPowerFlow(
    _4202.CouplingConnectionCompoundPowerFlow
):
    """SpringDamperConnectionCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_CONNECTION_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpringDamperConnectionCompoundPowerFlow"
    )

    class _Cast_SpringDamperConnectionCompoundPowerFlow:
        """Special nested class for casting SpringDamperConnectionCompoundPowerFlow to subclasses."""

        def __init__(
            self: "SpringDamperConnectionCompoundPowerFlow._Cast_SpringDamperConnectionCompoundPowerFlow",
            parent: "SpringDamperConnectionCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_power_flow(
            self: "SpringDamperConnectionCompoundPowerFlow._Cast_SpringDamperConnectionCompoundPowerFlow",
        ):
            return self._parent._cast(_4202.CouplingConnectionCompoundPowerFlow)

        @property
        def inter_mountable_component_connection_compound_power_flow(
            self: "SpringDamperConnectionCompoundPowerFlow._Cast_SpringDamperConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4229,
            )

            return self._parent._cast(
                _4229.InterMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def connection_compound_power_flow(
            self: "SpringDamperConnectionCompoundPowerFlow._Cast_SpringDamperConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4199,
            )

            return self._parent._cast(_4199.ConnectionCompoundPowerFlow)

        @property
        def connection_compound_analysis(
            self: "SpringDamperConnectionCompoundPowerFlow._Cast_SpringDamperConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpringDamperConnectionCompoundPowerFlow._Cast_SpringDamperConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperConnectionCompoundPowerFlow._Cast_SpringDamperConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def spring_damper_connection_compound_power_flow(
            self: "SpringDamperConnectionCompoundPowerFlow._Cast_SpringDamperConnectionCompoundPowerFlow",
        ) -> "SpringDamperConnectionCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "SpringDamperConnectionCompoundPowerFlow._Cast_SpringDamperConnectionCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "SpringDamperConnectionCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2348.SpringDamperConnection":
        """mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2348.SpringDamperConnection":
        """mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4136.SpringDamperConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.SpringDamperConnectionPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4136.SpringDamperConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.SpringDamperConnectionPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpringDamperConnectionCompoundPowerFlow._Cast_SpringDamperConnectionCompoundPowerFlow":
        return self._Cast_SpringDamperConnectionCompoundPowerFlow(self)
