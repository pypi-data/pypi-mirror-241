"""ShaftToMountableComponentConnectionSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _2984,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
        "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2293


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self", bound="ShaftToMountableComponentConnectionSteadyStateSynchronousResponse"
)


class ShaftToMountableComponentConnectionSteadyStateSynchronousResponse(
    _2984.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse
):
    """ShaftToMountableComponentConnectionSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
    )

    class _Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse:
        """Special nested class for casting ShaftToMountableComponentConnectionSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
            parent: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _2984.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def connection_steady_state_synchronous_response(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3016,
            )

            return self._parent._cast(_3016.ConnectionSteadyStateSynchronousResponse)

        @property
        def connection_static_load_analysis_case(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def coaxial_connection_steady_state_synchronous_response(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3005,
            )

            return self._parent._cast(
                _3005.CoaxialConnectionSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_central_bearing_connection_steady_state_synchronous_response(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3025,
            )

            return self._parent._cast(
                _3025.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse
            )

        @property
        def planetary_connection_steady_state_synchronous_response(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3065,
            )

            return self._parent._cast(
                _3065.PlanetaryConnectionSteadyStateSynchronousResponse
            )

        @property
        def shaft_to_mountable_component_connection_steady_state_synchronous_response(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
        ) -> "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse",
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
        self: Self,
        instance_to_wrap: "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse.TYPE",
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
    ) -> "ShaftToMountableComponentConnectionSteadyStateSynchronousResponse._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse":
        return self._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponse(
            self
        )
