"""BevelGearCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3118,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "BevelGearCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _2999,
    )


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="BevelGearCompoundSteadyStateSynchronousResponse")


class BevelGearCompoundSteadyStateSynchronousResponse(
    _3118.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse
):
    """BevelGearCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_BevelGearCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting BevelGearCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "BevelGearCompoundSteadyStateSynchronousResponse._Cast_BevelGearCompoundSteadyStateSynchronousResponse",
            parent: "BevelGearCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response(
            self: "BevelGearCompoundSteadyStateSynchronousResponse._Cast_BevelGearCompoundSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _3118.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response(
            self: "BevelGearCompoundSteadyStateSynchronousResponse._Cast_BevelGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3146,
            )

            return self._parent._cast(
                _3146.ConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_compound_steady_state_synchronous_response(
            self: "BevelGearCompoundSteadyStateSynchronousResponse._Cast_BevelGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3172,
            )

            return self._parent._cast(_3172.GearCompoundSteadyStateSynchronousResponse)

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "BevelGearCompoundSteadyStateSynchronousResponse._Cast_BevelGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3191,
            )

            return self._parent._cast(
                _3191.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "BevelGearCompoundSteadyStateSynchronousResponse._Cast_BevelGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3139,
            )

            return self._parent._cast(
                _3139.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "BevelGearCompoundSteadyStateSynchronousResponse._Cast_BevelGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3193,
            )

            return self._parent._cast(_3193.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "BevelGearCompoundSteadyStateSynchronousResponse._Cast_BevelGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearCompoundSteadyStateSynchronousResponse._Cast_BevelGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearCompoundSteadyStateSynchronousResponse._Cast_BevelGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_compound_steady_state_synchronous_response(
            self: "BevelGearCompoundSteadyStateSynchronousResponse._Cast_BevelGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3125,
            )

            return self._parent._cast(
                _3125.BevelDifferentialGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_planet_gear_compound_steady_state_synchronous_response(
            self: "BevelGearCompoundSteadyStateSynchronousResponse._Cast_BevelGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3128,
            )

            return self._parent._cast(
                _3128.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_sun_gear_compound_steady_state_synchronous_response(
            self: "BevelGearCompoundSteadyStateSynchronousResponse._Cast_BevelGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3129,
            )

            return self._parent._cast(
                _3129.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_compound_steady_state_synchronous_response(
            self: "BevelGearCompoundSteadyStateSynchronousResponse._Cast_BevelGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3213,
            )

            return self._parent._cast(
                _3213.SpiralBevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response(
            self: "BevelGearCompoundSteadyStateSynchronousResponse._Cast_BevelGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3219,
            )

            return self._parent._cast(
                _3219.StraightBevelDiffGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_compound_steady_state_synchronous_response(
            self: "BevelGearCompoundSteadyStateSynchronousResponse._Cast_BevelGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3222,
            )

            return self._parent._cast(
                _3222.StraightBevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_planet_gear_compound_steady_state_synchronous_response(
            self: "BevelGearCompoundSteadyStateSynchronousResponse._Cast_BevelGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3225,
            )

            return self._parent._cast(
                _3225.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_sun_gear_compound_steady_state_synchronous_response(
            self: "BevelGearCompoundSteadyStateSynchronousResponse._Cast_BevelGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3226,
            )

            return self._parent._cast(
                _3226.StraightBevelSunGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_compound_steady_state_synchronous_response(
            self: "BevelGearCompoundSteadyStateSynchronousResponse._Cast_BevelGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3240,
            )

            return self._parent._cast(
                _3240.ZerolBevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_compound_steady_state_synchronous_response(
            self: "BevelGearCompoundSteadyStateSynchronousResponse._Cast_BevelGearCompoundSteadyStateSynchronousResponse",
        ) -> "BevelGearCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "BevelGearCompoundSteadyStateSynchronousResponse._Cast_BevelGearCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "BevelGearCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_2999.BevelGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.BevelGearSteadyStateSynchronousResponse]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_2999.BevelGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.BevelGearSteadyStateSynchronousResponse]

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
    def cast_to(
        self: Self,
    ) -> "BevelGearCompoundSteadyStateSynchronousResponse._Cast_BevelGearCompoundSteadyStateSynchronousResponse":
        return self._Cast_BevelGearCompoundSteadyStateSynchronousResponse(self)
