"""StraightBevelSunGearCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3219,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "StraightBevelSunGearCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3097,
    )


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelSunGearCompoundSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self", bound="StraightBevelSunGearCompoundSteadyStateSynchronousResponse"
)


class StraightBevelSunGearCompoundSteadyStateSynchronousResponse(
    _3219.StraightBevelDiffGearCompoundSteadyStateSynchronousResponse
):
    """StraightBevelSunGearCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting StraightBevelSunGearCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponse",
            parent: "StraightBevelSunGearCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _3219.StraightBevelDiffGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_compound_steady_state_synchronous_response(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3130,
            )

            return self._parent._cast(
                _3130.BevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3118,
            )

            return self._parent._cast(
                _3118.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3146,
            )

            return self._parent._cast(
                _3146.ConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_compound_steady_state_synchronous_response(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3172,
            )

            return self._parent._cast(_3172.GearCompoundSteadyStateSynchronousResponse)

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3191,
            )

            return self._parent._cast(
                _3191.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3139,
            )

            return self._parent._cast(
                _3139.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3193,
            )

            return self._parent._cast(_3193.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def straight_bevel_sun_gear_compound_steady_state_synchronous_response(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponse",
        ) -> "StraightBevelSunGearCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "StraightBevelSunGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "StraightBevelSunGearCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3097.StraightBevelSunGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.StraightBevelSunGearSteadyStateSynchronousResponse]

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
    ) -> "List[_3097.StraightBevelSunGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.StraightBevelSunGearSteadyStateSynchronousResponse]

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
    ) -> "StraightBevelSunGearCompoundSteadyStateSynchronousResponse._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponse":
        return self._Cast_StraightBevelSunGearCompoundSteadyStateSynchronousResponse(
            self
        )
