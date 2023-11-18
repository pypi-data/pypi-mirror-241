"""AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3537,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2263


__docformat__ = "restructuredtext en"
__all__ = (
    "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
)


Self = TypeVar(
    "Self",
    bound="AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
)


class AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed(
    _3537.ConnectionSteadyStateSynchronousResponseAtASpeed
):
    """AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
            parent: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def connection_steady_state_synchronous_response_at_a_speed(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            return self._parent._cast(
                _3537.ConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_static_load_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def coaxial_connection_steady_state_synchronous_response_at_a_speed(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3526,
            )

            return self._parent._cast(
                _3526.CoaxialConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cycloidal_disc_central_bearing_connection_steady_state_synchronous_response_at_a_speed(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3546,
            )

            return self._parent._cast(
                _3546.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_steady_state_synchronous_response_at_a_speed(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3547,
            )

            return self._parent._cast(
                _3547.CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planetary_connection_steady_state_synchronous_response_at_a_speed(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3585,
            )

            return self._parent._cast(
                _3585.PlanetaryConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_to_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3599,
            )

            return self._parent._cast(
                _3599.ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2263.AbstractShaftToMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.AbstractShaftToMountableComponentConnection

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
    ) -> "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed(
            self
        )
