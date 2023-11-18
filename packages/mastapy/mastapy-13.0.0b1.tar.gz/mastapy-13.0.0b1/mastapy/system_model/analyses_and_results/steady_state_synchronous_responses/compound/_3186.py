"""KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3180,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2538
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3056,
    )


__docformat__ = "restructuredtext en"
__all__ = (
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse",
)


Self = TypeVar(
    "Self",
    bound="KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse",
)


class KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse(
    _3180.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse
):
    """KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _3180.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3146,
            )

            return self._parent._cast(
                _3146.ConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_compound_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3172,
            )

            return self._parent._cast(_3172.GearCompoundSteadyStateSynchronousResponse)

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3191,
            )

            return self._parent._cast(
                _3191.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3139,
            )

            return self._parent._cast(
                _3139.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3193,
            )

            return self._parent._cast(_3193.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2538.KlingelnbergCycloPalloidSpiralBevelGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear

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
    ) -> "List[_3056.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse]

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
    ) -> "List[_3056.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse]

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
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse(
            self
        )
