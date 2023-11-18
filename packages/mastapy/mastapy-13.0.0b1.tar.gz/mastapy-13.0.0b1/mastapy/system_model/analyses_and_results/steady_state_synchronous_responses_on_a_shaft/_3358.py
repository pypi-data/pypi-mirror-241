"""SynchroniserPartSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3281,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "SynchroniserPartSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2603


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="SynchroniserPartSteadyStateSynchronousResponseOnAShaft")


class SynchroniserPartSteadyStateSynchronousResponseOnAShaft(
    _3281.CouplingHalfSteadyStateSynchronousResponseOnAShaft
):
    """SynchroniserPartSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SynchroniserPartSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_SynchroniserPartSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting SynchroniserPartSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "SynchroniserPartSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserPartSteadyStateSynchronousResponseOnAShaft",
            parent: "SynchroniserPartSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def coupling_half_steady_state_synchronous_response_on_a_shaft(
            self: "SynchroniserPartSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserPartSteadyStateSynchronousResponseOnAShaft",
        ):
            return self._parent._cast(
                _3281.CouplingHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mountable_component_steady_state_synchronous_response_on_a_shaft(
            self: "SynchroniserPartSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserPartSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3320,
            )

            return self._parent._cast(
                _3320.MountableComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_steady_state_synchronous_response_on_a_shaft(
            self: "SynchroniserPartSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserPartSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3268,
            )

            return self._parent._cast(
                _3268.ComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "SynchroniserPartSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserPartSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3322,
            )

            return self._parent._cast(_3322.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserPartSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserPartSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserPartSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserPartSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserPartSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserPartSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserPartSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserPartSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserPartSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def synchroniser_half_steady_state_synchronous_response_on_a_shaft(
            self: "SynchroniserPartSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserPartSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3357,
            )

            return self._parent._cast(
                _3357.SynchroniserHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_sleeve_steady_state_synchronous_response_on_a_shaft(
            self: "SynchroniserPartSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserPartSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3359,
            )

            return self._parent._cast(
                _3359.SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_part_steady_state_synchronous_response_on_a_shaft(
            self: "SynchroniserPartSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserPartSteadyStateSynchronousResponseOnAShaft",
        ) -> "SynchroniserPartSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserPartSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "SynchroniserPartSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2603.SynchroniserPart":
        """mastapy.system_model.part_model.couplings.SynchroniserPart

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
    ) -> "SynchroniserPartSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserPartSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_SynchroniserPartSteadyStateSynchronousResponseOnAShaft(self)
