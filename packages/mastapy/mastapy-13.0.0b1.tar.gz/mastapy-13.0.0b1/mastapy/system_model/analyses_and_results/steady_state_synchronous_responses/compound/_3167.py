"""FaceGearCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3172,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "FaceGearCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2526
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3037,
    )


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="FaceGearCompoundSteadyStateSynchronousResponse")


class FaceGearCompoundSteadyStateSynchronousResponse(
    _3172.GearCompoundSteadyStateSynchronousResponse
):
    """FaceGearCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FaceGearCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_FaceGearCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting FaceGearCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "FaceGearCompoundSteadyStateSynchronousResponse._Cast_FaceGearCompoundSteadyStateSynchronousResponse",
            parent: "FaceGearCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def gear_compound_steady_state_synchronous_response(
            self: "FaceGearCompoundSteadyStateSynchronousResponse._Cast_FaceGearCompoundSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(_3172.GearCompoundSteadyStateSynchronousResponse)

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "FaceGearCompoundSteadyStateSynchronousResponse._Cast_FaceGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3191,
            )

            return self._parent._cast(
                _3191.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "FaceGearCompoundSteadyStateSynchronousResponse._Cast_FaceGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3139,
            )

            return self._parent._cast(
                _3139.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "FaceGearCompoundSteadyStateSynchronousResponse._Cast_FaceGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3193,
            )

            return self._parent._cast(_3193.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "FaceGearCompoundSteadyStateSynchronousResponse._Cast_FaceGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "FaceGearCompoundSteadyStateSynchronousResponse._Cast_FaceGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearCompoundSteadyStateSynchronousResponse._Cast_FaceGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def face_gear_compound_steady_state_synchronous_response(
            self: "FaceGearCompoundSteadyStateSynchronousResponse._Cast_FaceGearCompoundSteadyStateSynchronousResponse",
        ) -> "FaceGearCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "FaceGearCompoundSteadyStateSynchronousResponse._Cast_FaceGearCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "FaceGearCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2526.FaceGear":
        """mastapy.system_model.part_model.gears.FaceGear

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
    ) -> "List[_3037.FaceGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.FaceGearSteadyStateSynchronousResponse]

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
    ) -> "List[_3037.FaceGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.FaceGearSteadyStateSynchronousResponse]

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
    ) -> "FaceGearCompoundSteadyStateSynchronousResponse._Cast_FaceGearCompoundSteadyStateSynchronousResponse":
        return self._Cast_FaceGearCompoundSteadyStateSynchronousResponse(self)
