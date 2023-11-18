"""ClutchConnectionPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4067
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_CONNECTION_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "ClutchConnectionPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2340
    from mastapy.system_model.analyses_and_results.static_loads import _6830


__docformat__ = "restructuredtext en"
__all__ = ("ClutchConnectionPowerFlow",)


Self = TypeVar("Self", bound="ClutchConnectionPowerFlow")


class ClutchConnectionPowerFlow(_4067.CouplingConnectionPowerFlow):
    """ClutchConnectionPowerFlow

    This is a mastapy class.
    """

    TYPE = _CLUTCH_CONNECTION_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClutchConnectionPowerFlow")

    class _Cast_ClutchConnectionPowerFlow:
        """Special nested class for casting ClutchConnectionPowerFlow to subclasses."""

        def __init__(
            self: "ClutchConnectionPowerFlow._Cast_ClutchConnectionPowerFlow",
            parent: "ClutchConnectionPowerFlow",
        ):
            self._parent = parent

        @property
        def coupling_connection_power_flow(
            self: "ClutchConnectionPowerFlow._Cast_ClutchConnectionPowerFlow",
        ):
            return self._parent._cast(_4067.CouplingConnectionPowerFlow)

        @property
        def inter_mountable_component_connection_power_flow(
            self: "ClutchConnectionPowerFlow._Cast_ClutchConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4097

            return self._parent._cast(_4097.InterMountableComponentConnectionPowerFlow)

        @property
        def connection_power_flow(
            self: "ClutchConnectionPowerFlow._Cast_ClutchConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4065

            return self._parent._cast(_4065.ConnectionPowerFlow)

        @property
        def connection_static_load_analysis_case(
            self: "ClutchConnectionPowerFlow._Cast_ClutchConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ClutchConnectionPowerFlow._Cast_ClutchConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ClutchConnectionPowerFlow._Cast_ClutchConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ClutchConnectionPowerFlow._Cast_ClutchConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchConnectionPowerFlow._Cast_ClutchConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def clutch_connection_power_flow(
            self: "ClutchConnectionPowerFlow._Cast_ClutchConnectionPowerFlow",
        ) -> "ClutchConnectionPowerFlow":
            return self._parent

        def __getattr__(
            self: "ClutchConnectionPowerFlow._Cast_ClutchConnectionPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ClutchConnectionPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2340.ClutchConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ClutchConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6830.ClutchConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ClutchConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ClutchConnectionPowerFlow._Cast_ClutchConnectionPowerFlow":
        return self._Cast_ClutchConnectionPowerFlow(self)
