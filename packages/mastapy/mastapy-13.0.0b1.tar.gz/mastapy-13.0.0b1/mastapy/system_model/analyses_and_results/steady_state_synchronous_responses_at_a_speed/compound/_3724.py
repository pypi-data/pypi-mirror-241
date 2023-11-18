"""RollingRingCompoundSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3671,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "RollingRingCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2594
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3595,
    )


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="RollingRingCompoundSteadyStateSynchronousResponseAtASpeed"
)


class RollingRingCompoundSteadyStateSynchronousResponseAtASpeed(
    _3671.CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
):
    """RollingRingCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_RollingRingCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_RollingRingCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting RollingRingCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "RollingRingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "RollingRingCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "RollingRingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            return self._parent._cast(
                _3671.CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "RollingRingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3709,
            )

            return self._parent._cast(
                _3709.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_compound_steady_state_synchronous_response_at_a_speed(
            self: "RollingRingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3657,
            )

            return self._parent._cast(
                _3657.ComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "RollingRingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3711,
            )

            return self._parent._cast(
                _3711.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_analysis(
            self: "RollingRingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RollingRingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def rolling_ring_compound_steady_state_synchronous_response_at_a_speed(
            self: "RollingRingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "RollingRingCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "RollingRingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "RollingRingCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2594.RollingRing":
        """mastapy.system_model.part_model.couplings.RollingRing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3595.RollingRingSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.RollingRingSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def planetaries(
        self: Self,
    ) -> "List[RollingRingCompoundSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound.RollingRingCompoundSteadyStateSynchronousResponseAtASpeed]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3595.RollingRingSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.RollingRingSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "RollingRingCompoundSteadyStateSynchronousResponseAtASpeed._Cast_RollingRingCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_RollingRingCompoundSteadyStateSynchronousResponseAtASpeed(
            self
        )
