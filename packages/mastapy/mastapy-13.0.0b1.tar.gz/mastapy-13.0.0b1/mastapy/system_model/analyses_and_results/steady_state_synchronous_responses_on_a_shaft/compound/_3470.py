"""ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3376,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3340,
    )


__docformat__ = "restructuredtext en"
__all__ = (
    "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
)


Self = TypeVar(
    "Self",
    bound="ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
)


class ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft(
    _3376.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
):
    """ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            return self._parent._cast(
                _3376.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3408,
            )

            return self._parent._cast(
                _3408.ConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3397,
            )

            return self._parent._cast(
                _3397.CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3417,
            )

            return self._parent._cast(
                _3417.CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planetary_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3456,
            )

            return self._parent._cast(
                _3456.PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_to_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3340.ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft]

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3340.ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.ShaftToMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft]

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
    def cast_to(
        self: Self,
    ) -> "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft(
            self
        )
