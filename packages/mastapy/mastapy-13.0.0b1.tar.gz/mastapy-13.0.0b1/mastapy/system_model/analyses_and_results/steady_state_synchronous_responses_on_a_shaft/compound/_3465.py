"""RollingRingCompoundSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3412,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "RollingRingCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2594
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3336,
    )


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="RollingRingCompoundSteadyStateSynchronousResponseOnAShaft"
)


class RollingRingCompoundSteadyStateSynchronousResponseOnAShaft(
    _3412.CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
):
    """RollingRingCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_RollingRingCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_RollingRingCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting RollingRingCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "RollingRingCompoundSteadyStateSynchronousResponseOnAShaft._Cast_RollingRingCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "RollingRingCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "RollingRingCompoundSteadyStateSynchronousResponseOnAShaft._Cast_RollingRingCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            return self._parent._cast(
                _3412.CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "RollingRingCompoundSteadyStateSynchronousResponseOnAShaft._Cast_RollingRingCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3450,
            )

            return self._parent._cast(
                _3450.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "RollingRingCompoundSteadyStateSynchronousResponseOnAShaft._Cast_RollingRingCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3398,
            )

            return self._parent._cast(
                _3398.ComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "RollingRingCompoundSteadyStateSynchronousResponseOnAShaft._Cast_RollingRingCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3452,
            )

            return self._parent._cast(
                _3452.PartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_analysis(
            self: "RollingRingCompoundSteadyStateSynchronousResponseOnAShaft._Cast_RollingRingCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RollingRingCompoundSteadyStateSynchronousResponseOnAShaft._Cast_RollingRingCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingCompoundSteadyStateSynchronousResponseOnAShaft._Cast_RollingRingCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def rolling_ring_compound_steady_state_synchronous_response_on_a_shaft(
            self: "RollingRingCompoundSteadyStateSynchronousResponseOnAShaft._Cast_RollingRingCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "RollingRingCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "RollingRingCompoundSteadyStateSynchronousResponseOnAShaft._Cast_RollingRingCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "RollingRingCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
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
    ) -> "List[_3336.RollingRingSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.RollingRingSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[RollingRingCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.RollingRingCompoundSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3336.RollingRingSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.RollingRingSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "RollingRingCompoundSteadyStateSynchronousResponseOnAShaft._Cast_RollingRingCompoundSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_RollingRingCompoundSteadyStateSynchronousResponseOnAShaft(
            self
        )
