"""FEPartCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3116,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_PART_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "FEPartCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2451
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3038,
    )


__docformat__ = "restructuredtext en"
__all__ = ("FEPartCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="FEPartCompoundSteadyStateSynchronousResponse")


class FEPartCompoundSteadyStateSynchronousResponse(
    _3116.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse
):
    """FEPartCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _FE_PART_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FEPartCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_FEPartCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting FEPartCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "FEPartCompoundSteadyStateSynchronousResponse._Cast_FEPartCompoundSteadyStateSynchronousResponse",
            parent: "FEPartCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_steady_state_synchronous_response(
            self: "FEPartCompoundSteadyStateSynchronousResponse._Cast_FEPartCompoundSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _3116.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "FEPartCompoundSteadyStateSynchronousResponse._Cast_FEPartCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3139,
            )

            return self._parent._cast(
                _3139.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "FEPartCompoundSteadyStateSynchronousResponse._Cast_FEPartCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3193,
            )

            return self._parent._cast(_3193.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "FEPartCompoundSteadyStateSynchronousResponse._Cast_FEPartCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "FEPartCompoundSteadyStateSynchronousResponse._Cast_FEPartCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "FEPartCompoundSteadyStateSynchronousResponse._Cast_FEPartCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def fe_part_compound_steady_state_synchronous_response(
            self: "FEPartCompoundSteadyStateSynchronousResponse._Cast_FEPartCompoundSteadyStateSynchronousResponse",
        ) -> "FEPartCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "FEPartCompoundSteadyStateSynchronousResponse._Cast_FEPartCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "FEPartCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2451.FEPart":
        """mastapy.system_model.part_model.FEPart

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
    ) -> "List[_3038.FEPartSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.FEPartSteadyStateSynchronousResponse]

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
    def planetaries(self: Self) -> "List[FEPartCompoundSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound.FEPartCompoundSteadyStateSynchronousResponse]

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
    ) -> "List[_3038.FEPartSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.FEPartSteadyStateSynchronousResponse]

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
    ) -> "FEPartCompoundSteadyStateSynchronousResponse._Cast_FEPartCompoundSteadyStateSynchronousResponse":
        return self._Cast_FEPartCompoundSteadyStateSynchronousResponse(self)
