"""ShaftSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3504,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "ShaftSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.shaft_model import _2480
    from mastapy.system_model.analyses_and_results.static_loads import _6948


__docformat__ = "restructuredtext en"
__all__ = ("ShaftSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="ShaftSteadyStateSynchronousResponseAtASpeed")


class ShaftSteadyStateSynchronousResponseAtASpeed(
    _3504.AbstractShaftSteadyStateSynchronousResponseAtASpeed
):
    """ShaftSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _SHAFT_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ShaftSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_ShaftSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting ShaftSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "ShaftSteadyStateSynchronousResponseAtASpeed._Cast_ShaftSteadyStateSynchronousResponseAtASpeed",
            parent: "ShaftSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def abstract_shaft_steady_state_synchronous_response_at_a_speed(
            self: "ShaftSteadyStateSynchronousResponseAtASpeed._Cast_ShaftSteadyStateSynchronousResponseAtASpeed",
        ):
            return self._parent._cast(
                _3504.AbstractShaftSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response_at_a_speed(
            self: "ShaftSteadyStateSynchronousResponseAtASpeed._Cast_ShaftSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3503,
            )

            return self._parent._cast(
                _3503.AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "ShaftSteadyStateSynchronousResponseAtASpeed._Cast_ShaftSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3527,
            )

            return self._parent._cast(
                _3527.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "ShaftSteadyStateSynchronousResponseAtASpeed._Cast_ShaftSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3581,
            )

            return self._parent._cast(_3581.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "ShaftSteadyStateSynchronousResponseAtASpeed._Cast_ShaftSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ShaftSteadyStateSynchronousResponseAtASpeed._Cast_ShaftSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ShaftSteadyStateSynchronousResponseAtASpeed._Cast_ShaftSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftSteadyStateSynchronousResponseAtASpeed._Cast_ShaftSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftSteadyStateSynchronousResponseAtASpeed._Cast_ShaftSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def shaft_steady_state_synchronous_response_at_a_speed(
            self: "ShaftSteadyStateSynchronousResponseAtASpeed._Cast_ShaftSteadyStateSynchronousResponseAtASpeed",
        ) -> "ShaftSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "ShaftSteadyStateSynchronousResponseAtASpeed._Cast_ShaftSteadyStateSynchronousResponseAtASpeed",
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
        self: Self, instance_to_wrap: "ShaftSteadyStateSynchronousResponseAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2480.Shaft":
        """mastapy.system_model.part_model.shaft_model.Shaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6948.ShaftLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ShaftLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ShaftSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.ShaftSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ShaftSteadyStateSynchronousResponseAtASpeed._Cast_ShaftSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_ShaftSteadyStateSynchronousResponseAtASpeed(self)
