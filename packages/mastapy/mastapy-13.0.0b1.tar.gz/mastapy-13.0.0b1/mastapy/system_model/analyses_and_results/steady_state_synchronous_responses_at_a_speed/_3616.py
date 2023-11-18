"""SynchroniserHalfSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3617,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "SynchroniserHalfSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2602
    from mastapy.system_model.analyses_and_results.static_loads import _6965


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserHalfSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="SynchroniserHalfSteadyStateSynchronousResponseAtASpeed")


class SynchroniserHalfSteadyStateSynchronousResponseAtASpeed(
    _3617.SynchroniserPartSteadyStateSynchronousResponseAtASpeed
):
    """SynchroniserHalfSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SynchroniserHalfSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_SynchroniserHalfSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting SynchroniserHalfSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "SynchroniserHalfSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserHalfSteadyStateSynchronousResponseAtASpeed",
            parent: "SynchroniserHalfSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def synchroniser_part_steady_state_synchronous_response_at_a_speed(
            self: "SynchroniserHalfSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserHalfSteadyStateSynchronousResponseAtASpeed",
        ):
            return self._parent._cast(
                _3617.SynchroniserPartSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "SynchroniserHalfSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserHalfSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3540,
            )

            return self._parent._cast(
                _3540.CouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "SynchroniserHalfSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserHalfSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3579,
            )

            return self._parent._cast(
                _3579.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "SynchroniserHalfSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserHalfSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3527,
            )

            return self._parent._cast(
                _3527.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "SynchroniserHalfSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserHalfSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3581,
            )

            return self._parent._cast(_3581.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserHalfSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserHalfSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserHalfSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserHalfSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserHalfSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserHalfSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserHalfSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserHalfSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserHalfSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserHalfSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def synchroniser_half_steady_state_synchronous_response_at_a_speed(
            self: "SynchroniserHalfSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserHalfSteadyStateSynchronousResponseAtASpeed",
        ) -> "SynchroniserHalfSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "SynchroniserHalfSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserHalfSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "SynchroniserHalfSteadyStateSynchronousResponseAtASpeed.TYPE",
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
    ) -> "SynchroniserHalfSteadyStateSynchronousResponseAtASpeed._Cast_SynchroniserHalfSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_SynchroniserHalfSteadyStateSynchronousResponseAtASpeed(self)
