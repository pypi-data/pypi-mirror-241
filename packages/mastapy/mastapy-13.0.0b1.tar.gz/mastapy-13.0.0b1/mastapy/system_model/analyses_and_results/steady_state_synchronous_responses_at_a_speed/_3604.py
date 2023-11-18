"""SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3539,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2348
    from mastapy.system_model.analyses_and_results.static_loads import _6954


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed"
)


class SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed(
    _3539.CouplingConnectionSteadyStateSynchronousResponseAtASpeed
):
    """SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed._Cast_SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed",
            parent: "SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_connection_steady_state_synchronous_response_at_a_speed(
            self: "SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed._Cast_SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            return self._parent._cast(
                _3539.CouplingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
            self: "SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed._Cast_SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3567,
            )

            return self._parent._cast(
                _3567.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_steady_state_synchronous_response_at_a_speed(
            self: "SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed._Cast_SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3537,
            )

            return self._parent._cast(
                _3537.ConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_static_load_analysis_case(
            self: "SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed._Cast_SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed._Cast_SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed._Cast_SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed._Cast_SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed._Cast_SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def spring_damper_connection_steady_state_synchronous_response_at_a_speed(
            self: "SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed._Cast_SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed._Cast_SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def connection_load_case(self: Self) -> "_6954.SpringDamperConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpringDamperConnectionLoadCase

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
    ) -> "SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed._Cast_SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed(
            self
        )
