"""SpringDamperCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3151,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "SpringDamperCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2598
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3086,
    )


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="SpringDamperCompoundSteadyStateSynchronousResponse")


class SpringDamperCompoundSteadyStateSynchronousResponse(
    _3151.CouplingCompoundSteadyStateSynchronousResponse
):
    """SpringDamperCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpringDamperCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_SpringDamperCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting SpringDamperCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "SpringDamperCompoundSteadyStateSynchronousResponse._Cast_SpringDamperCompoundSteadyStateSynchronousResponse",
            parent: "SpringDamperCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def coupling_compound_steady_state_synchronous_response(
            self: "SpringDamperCompoundSteadyStateSynchronousResponse._Cast_SpringDamperCompoundSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _3151.CouplingCompoundSteadyStateSynchronousResponse
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response(
            self: "SpringDamperCompoundSteadyStateSynchronousResponse._Cast_SpringDamperCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3212,
            )

            return self._parent._cast(
                _3212.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response(
            self: "SpringDamperCompoundSteadyStateSynchronousResponse._Cast_SpringDamperCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3114,
            )

            return self._parent._cast(
                _3114.AbstractAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "SpringDamperCompoundSteadyStateSynchronousResponse._Cast_SpringDamperCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3193,
            )

            return self._parent._cast(_3193.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "SpringDamperCompoundSteadyStateSynchronousResponse._Cast_SpringDamperCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpringDamperCompoundSteadyStateSynchronousResponse._Cast_SpringDamperCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperCompoundSteadyStateSynchronousResponse._Cast_SpringDamperCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def spring_damper_compound_steady_state_synchronous_response(
            self: "SpringDamperCompoundSteadyStateSynchronousResponse._Cast_SpringDamperCompoundSteadyStateSynchronousResponse",
        ) -> "SpringDamperCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "SpringDamperCompoundSteadyStateSynchronousResponse._Cast_SpringDamperCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "SpringDamperCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2598.SpringDamper":
        """mastapy.system_model.part_model.couplings.SpringDamper

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2598.SpringDamper":
        """mastapy.system_model.part_model.couplings.SpringDamper

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3086.SpringDamperSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.SpringDamperSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3086.SpringDamperSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.SpringDamperSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpringDamperCompoundSteadyStateSynchronousResponse._Cast_SpringDamperCompoundSteadyStateSynchronousResponse":
        return self._Cast_SpringDamperCompoundSteadyStateSynchronousResponse(self)
