"""SynchroniserHalfSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3358,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "SynchroniserHalfSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2602
    from mastapy.system_model.analyses_and_results.static_loads import _6965


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserHalfSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="SynchroniserHalfSteadyStateSynchronousResponseOnAShaft")


class SynchroniserHalfSteadyStateSynchronousResponseOnAShaft(
    _3358.SynchroniserPartSteadyStateSynchronousResponseOnAShaft
):
    """SynchroniserHalfSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SynchroniserHalfSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_SynchroniserHalfSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting SynchroniserHalfSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "SynchroniserHalfSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserHalfSteadyStateSynchronousResponseOnAShaft",
            parent: "SynchroniserHalfSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def synchroniser_part_steady_state_synchronous_response_on_a_shaft(
            self: "SynchroniserHalfSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserHalfSteadyStateSynchronousResponseOnAShaft",
        ):
            return self._parent._cast(
                _3358.SynchroniserPartSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_half_steady_state_synchronous_response_on_a_shaft(
            self: "SynchroniserHalfSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserHalfSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3281,
            )

            return self._parent._cast(
                _3281.CouplingHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mountable_component_steady_state_synchronous_response_on_a_shaft(
            self: "SynchroniserHalfSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserHalfSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3320,
            )

            return self._parent._cast(
                _3320.MountableComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_steady_state_synchronous_response_on_a_shaft(
            self: "SynchroniserHalfSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserHalfSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3268,
            )

            return self._parent._cast(
                _3268.ComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "SynchroniserHalfSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserHalfSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3322,
            )

            return self._parent._cast(_3322.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserHalfSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserHalfSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserHalfSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserHalfSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserHalfSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserHalfSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserHalfSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserHalfSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserHalfSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserHalfSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def synchroniser_half_steady_state_synchronous_response_on_a_shaft(
            self: "SynchroniserHalfSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "SynchroniserHalfSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "SynchroniserHalfSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserHalfSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "SynchroniserHalfSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2602.SynchroniserHalf":
        """mastapy.system_model.part_model.couplings.SynchroniserHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6965.SynchroniserHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserHalfLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SynchroniserHalfSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserHalfSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_SynchroniserHalfSteadyStateSynchronousResponseOnAShaft(self)
