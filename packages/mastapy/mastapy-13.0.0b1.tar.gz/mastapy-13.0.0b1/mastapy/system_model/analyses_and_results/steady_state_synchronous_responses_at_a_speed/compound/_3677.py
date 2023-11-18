"""CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3633,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2567
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3548,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed"
)


class CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed(
    _3633.AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed
):
    """CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def abstract_shaft_compound_steady_state_synchronous_response_at_a_speed(
            self: "CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            return self._parent._cast(
                _3633.AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_shaft_or_housing_compound_steady_state_synchronous_response_at_a_speed(
            self: "CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3634,
            )

            return self._parent._cast(
                _3634.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_compound_steady_state_synchronous_response_at_a_speed(
            self: "CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3657,
            )

            return self._parent._cast(
                _3657.ComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3711,
            )

            return self._parent._cast(
                _3711.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_analysis(
            self: "CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cycloidal_disc_compound_steady_state_synchronous_response_at_a_speed(
            self: "CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2567.CycloidalDisc":
        """mastapy.system_model.part_model.cycloidal.CycloidalDisc

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
    ) -> "List[_3548.CycloidalDiscSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.CycloidalDiscSteadyStateSynchronousResponseAtASpeed]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3548.CycloidalDiscSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.CycloidalDiscSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed(
            self
        )
