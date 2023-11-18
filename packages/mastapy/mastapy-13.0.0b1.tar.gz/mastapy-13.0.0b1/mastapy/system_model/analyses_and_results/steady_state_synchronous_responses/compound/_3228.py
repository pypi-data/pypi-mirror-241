"""SynchroniserHalfCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3229,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "SynchroniserHalfCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2602
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3098,
    )


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserHalfCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="SynchroniserHalfCompoundSteadyStateSynchronousResponse")


class SynchroniserHalfCompoundSteadyStateSynchronousResponse(
    _3229.SynchroniserPartCompoundSteadyStateSynchronousResponse
):
    """SynchroniserHalfCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SynchroniserHalfCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_SynchroniserHalfCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting SynchroniserHalfCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "SynchroniserHalfCompoundSteadyStateSynchronousResponse._Cast_SynchroniserHalfCompoundSteadyStateSynchronousResponse",
            parent: "SynchroniserHalfCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def synchroniser_part_compound_steady_state_synchronous_response(
            self: "SynchroniserHalfCompoundSteadyStateSynchronousResponse._Cast_SynchroniserHalfCompoundSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _3229.SynchroniserPartCompoundSteadyStateSynchronousResponse
            )

        @property
        def coupling_half_compound_steady_state_synchronous_response(
            self: "SynchroniserHalfCompoundSteadyStateSynchronousResponse._Cast_SynchroniserHalfCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3153,
            )

            return self._parent._cast(
                _3153.CouplingHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "SynchroniserHalfCompoundSteadyStateSynchronousResponse._Cast_SynchroniserHalfCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3191,
            )

            return self._parent._cast(
                _3191.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "SynchroniserHalfCompoundSteadyStateSynchronousResponse._Cast_SynchroniserHalfCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3139,
            )

            return self._parent._cast(
                _3139.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "SynchroniserHalfCompoundSteadyStateSynchronousResponse._Cast_SynchroniserHalfCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3193,
            )

            return self._parent._cast(_3193.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "SynchroniserHalfCompoundSteadyStateSynchronousResponse._Cast_SynchroniserHalfCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserHalfCompoundSteadyStateSynchronousResponse._Cast_SynchroniserHalfCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserHalfCompoundSteadyStateSynchronousResponse._Cast_SynchroniserHalfCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def synchroniser_half_compound_steady_state_synchronous_response(
            self: "SynchroniserHalfCompoundSteadyStateSynchronousResponse._Cast_SynchroniserHalfCompoundSteadyStateSynchronousResponse",
        ) -> "SynchroniserHalfCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "SynchroniserHalfCompoundSteadyStateSynchronousResponse._Cast_SynchroniserHalfCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "SynchroniserHalfCompoundSteadyStateSynchronousResponse.TYPE",
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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3098.SynchroniserHalfSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.SynchroniserHalfSteadyStateSynchronousResponse]

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
    ) -> "List[_3098.SynchroniserHalfSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.SynchroniserHalfSteadyStateSynchronousResponse]

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
    ) -> "SynchroniserHalfCompoundSteadyStateSynchronousResponse._Cast_SynchroniserHalfCompoundSteadyStateSynchronousResponse":
        return self._Cast_SynchroniserHalfCompoundSteadyStateSynchronousResponse(self)
