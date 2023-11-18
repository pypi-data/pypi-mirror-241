"""TorqueConverterCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3151,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "TorqueConverterCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2605
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3104,
    )


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="TorqueConverterCompoundSteadyStateSynchronousResponse")


class TorqueConverterCompoundSteadyStateSynchronousResponse(
    _3151.CouplingCompoundSteadyStateSynchronousResponse
):
    """TorqueConverterCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_TorqueConverterCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting TorqueConverterCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "TorqueConverterCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterCompoundSteadyStateSynchronousResponse",
            parent: "TorqueConverterCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def coupling_compound_steady_state_synchronous_response(
            self: "TorqueConverterCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterCompoundSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _3151.CouplingCompoundSteadyStateSynchronousResponse
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response(
            self: "TorqueConverterCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3212,
            )

            return self._parent._cast(
                _3212.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response(
            self: "TorqueConverterCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3114,
            )

            return self._parent._cast(
                _3114.AbstractAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "TorqueConverterCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3193,
            )

            return self._parent._cast(_3193.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "TorqueConverterCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "TorqueConverterCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def torque_converter_compound_steady_state_synchronous_response(
            self: "TorqueConverterCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterCompoundSteadyStateSynchronousResponse",
        ) -> "TorqueConverterCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "TorqueConverterCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "TorqueConverterCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2605.TorqueConverter":
        """mastapy.system_model.part_model.couplings.TorqueConverter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2605.TorqueConverter":
        """mastapy.system_model.part_model.couplings.TorqueConverter

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
    ) -> "List[_3104.TorqueConverterSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.TorqueConverterSteadyStateSynchronousResponse]

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
    ) -> "List[_3104.TorqueConverterSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.TorqueConverterSteadyStateSynchronousResponse]

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
    ) -> "TorqueConverterCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterCompoundSteadyStateSynchronousResponse":
        return self._Cast_TorqueConverterCompoundSteadyStateSynchronousResponse(self)
