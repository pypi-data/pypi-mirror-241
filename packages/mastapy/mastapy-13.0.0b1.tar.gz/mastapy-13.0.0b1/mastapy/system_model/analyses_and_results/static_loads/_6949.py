"""ShaftToMountableComponentConnectionLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6807
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ShaftToMountableComponentConnectionLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2293


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionLoadCase",)


Self = TypeVar("Self", bound="ShaftToMountableComponentConnectionLoadCase")


class ShaftToMountableComponentConnectionLoadCase(
    _6807.AbstractShaftToMountableComponentConnectionLoadCase
):
    """ShaftToMountableComponentConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ShaftToMountableComponentConnectionLoadCase"
    )

    class _Cast_ShaftToMountableComponentConnectionLoadCase:
        """Special nested class for casting ShaftToMountableComponentConnectionLoadCase to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionLoadCase._Cast_ShaftToMountableComponentConnectionLoadCase",
            parent: "ShaftToMountableComponentConnectionLoadCase",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_load_case(
            self: "ShaftToMountableComponentConnectionLoadCase._Cast_ShaftToMountableComponentConnectionLoadCase",
        ):
            return self._parent._cast(
                _6807.AbstractShaftToMountableComponentConnectionLoadCase
            )

        @property
        def connection_load_case(
            self: "ShaftToMountableComponentConnectionLoadCase._Cast_ShaftToMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6847

            return self._parent._cast(_6847.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "ShaftToMountableComponentConnectionLoadCase._Cast_ShaftToMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftToMountableComponentConnectionLoadCase._Cast_ShaftToMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionLoadCase._Cast_ShaftToMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def coaxial_connection_load_case(
            self: "ShaftToMountableComponentConnectionLoadCase._Cast_ShaftToMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6834

            return self._parent._cast(_6834.CoaxialConnectionLoadCase)

        @property
        def cycloidal_disc_central_bearing_connection_load_case(
            self: "ShaftToMountableComponentConnectionLoadCase._Cast_ShaftToMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6856

            return self._parent._cast(
                _6856.CycloidalDiscCentralBearingConnectionLoadCase
            )

        @property
        def planetary_connection_load_case(
            self: "ShaftToMountableComponentConnectionLoadCase._Cast_ShaftToMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6930

            return self._parent._cast(_6930.PlanetaryConnectionLoadCase)

        @property
        def shaft_to_mountable_component_connection_load_case(
            self: "ShaftToMountableComponentConnectionLoadCase._Cast_ShaftToMountableComponentConnectionLoadCase",
        ) -> "ShaftToMountableComponentConnectionLoadCase":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionLoadCase._Cast_ShaftToMountableComponentConnectionLoadCase",
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
        self: Self, instance_to_wrap: "ShaftToMountableComponentConnectionLoadCase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2293.ShaftToMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ShaftToMountableComponentConnectionLoadCase._Cast_ShaftToMountableComponentConnectionLoadCase":
        return self._Cast_ShaftToMountableComponentConnectionLoadCase(self)
