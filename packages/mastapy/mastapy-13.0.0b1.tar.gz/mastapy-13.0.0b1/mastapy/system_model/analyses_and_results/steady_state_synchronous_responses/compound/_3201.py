"""PowerLoadCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3236,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "PowerLoadCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2470
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3069,
    )


__docformat__ = "restructuredtext en"
__all__ = ("PowerLoadCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="PowerLoadCompoundSteadyStateSynchronousResponse")


class PowerLoadCompoundSteadyStateSynchronousResponse(
    _3236.VirtualComponentCompoundSteadyStateSynchronousResponse
):
    """PowerLoadCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _POWER_LOAD_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PowerLoadCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_PowerLoadCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting PowerLoadCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "PowerLoadCompoundSteadyStateSynchronousResponse._Cast_PowerLoadCompoundSteadyStateSynchronousResponse",
            parent: "PowerLoadCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_steady_state_synchronous_response(
            self: "PowerLoadCompoundSteadyStateSynchronousResponse._Cast_PowerLoadCompoundSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _3236.VirtualComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "PowerLoadCompoundSteadyStateSynchronousResponse._Cast_PowerLoadCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3191,
            )

            return self._parent._cast(
                _3191.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "PowerLoadCompoundSteadyStateSynchronousResponse._Cast_PowerLoadCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3139,
            )

            return self._parent._cast(
                _3139.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "PowerLoadCompoundSteadyStateSynchronousResponse._Cast_PowerLoadCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3193,
            )

            return self._parent._cast(_3193.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "PowerLoadCompoundSteadyStateSynchronousResponse._Cast_PowerLoadCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PowerLoadCompoundSteadyStateSynchronousResponse._Cast_PowerLoadCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PowerLoadCompoundSteadyStateSynchronousResponse._Cast_PowerLoadCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def power_load_compound_steady_state_synchronous_response(
            self: "PowerLoadCompoundSteadyStateSynchronousResponse._Cast_PowerLoadCompoundSteadyStateSynchronousResponse",
        ) -> "PowerLoadCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "PowerLoadCompoundSteadyStateSynchronousResponse._Cast_PowerLoadCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "PowerLoadCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2470.PowerLoad":
        """mastapy.system_model.part_model.PowerLoad

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
    ) -> "List[_3069.PowerLoadSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.PowerLoadSteadyStateSynchronousResponse]

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
    ) -> "List[_3069.PowerLoadSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.PowerLoadSteadyStateSynchronousResponse]

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
    ) -> "PowerLoadCompoundSteadyStateSynchronousResponse._Cast_PowerLoadCompoundSteadyStateSynchronousResponse":
        return self._Cast_PowerLoadCompoundSteadyStateSynchronousResponse(self)
