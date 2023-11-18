"""CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3267,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2333


__docformat__ = "restructuredtext en"
__all__ = (
    "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft",
)


Self = TypeVar(
    "Self",
    bound="CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft",
)


class CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft(
    _3267.CoaxialConnectionSteadyStateSynchronousResponseOnAShaft
):
    """CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft",
            parent: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def coaxial_connection_steady_state_synchronous_response_on_a_shaft(
            self: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            return self._parent._cast(
                _3267.CoaxialConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_to_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3340,
            )

            return self._parent._cast(
                _3340.ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3246,
            )

            return self._parent._cast(
                _3246.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_steady_state_synchronous_response_on_a_shaft(
            self: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3278,
            )

            return self._parent._cast(
                _3278.ConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_static_load_analysis_case(
            self: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_steady_state_synchronous_response_on_a_shaft(
            self: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft",
        ) -> "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2333.CycloidalDiscCentralBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscCentralBearingConnection

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
    ) -> "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseOnAShaft(
            self
        )
