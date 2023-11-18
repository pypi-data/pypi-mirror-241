"""ConnectorSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3320,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "ConnectorSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2445


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="ConnectorSteadyStateSynchronousResponseOnAShaft")


class ConnectorSteadyStateSynchronousResponseOnAShaft(
    _3320.MountableComponentSteadyStateSynchronousResponseOnAShaft
):
    """ConnectorSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConnectorSteadyStateSynchronousResponseOnAShaft"
    )

    class _Cast_ConnectorSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting ConnectorSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "ConnectorSteadyStateSynchronousResponseOnAShaft._Cast_ConnectorSteadyStateSynchronousResponseOnAShaft",
            parent: "ConnectorSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def mountable_component_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectorSteadyStateSynchronousResponseOnAShaft._Cast_ConnectorSteadyStateSynchronousResponseOnAShaft",
        ):
            return self._parent._cast(
                _3320.MountableComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectorSteadyStateSynchronousResponseOnAShaft._Cast_ConnectorSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3268,
            )

            return self._parent._cast(
                _3268.ComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectorSteadyStateSynchronousResponseOnAShaft._Cast_ConnectorSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3322,
            )

            return self._parent._cast(_3322.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "ConnectorSteadyStateSynchronousResponseOnAShaft._Cast_ConnectorSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConnectorSteadyStateSynchronousResponseOnAShaft._Cast_ConnectorSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConnectorSteadyStateSynchronousResponseOnAShaft._Cast_ConnectorSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectorSteadyStateSynchronousResponseOnAShaft._Cast_ConnectorSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorSteadyStateSynchronousResponseOnAShaft._Cast_ConnectorSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bearing_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectorSteadyStateSynchronousResponseOnAShaft._Cast_ConnectorSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3251,
            )

            return self._parent._cast(
                _3251.BearingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def oil_seal_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectorSteadyStateSynchronousResponseOnAShaft._Cast_ConnectorSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3321,
            )

            return self._parent._cast(
                _3321.OilSealSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_hub_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectorSteadyStateSynchronousResponseOnAShaft._Cast_ConnectorSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3338,
            )

            return self._parent._cast(
                _3338.ShaftHubConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connector_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectorSteadyStateSynchronousResponseOnAShaft._Cast_ConnectorSteadyStateSynchronousResponseOnAShaft",
        ) -> "ConnectorSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "ConnectorSteadyStateSynchronousResponseOnAShaft._Cast_ConnectorSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "ConnectorSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2445.Connector":
        """mastapy.system_model.part_model.Connector

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConnectorSteadyStateSynchronousResponseOnAShaft._Cast_ConnectorSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_ConnectorSteadyStateSynchronousResponseOnAShaft(self)
