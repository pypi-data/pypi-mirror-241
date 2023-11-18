"""StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3478,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3355,
    )


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self",
    bound="StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
)


class StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft(
    _3478.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft
):
    """StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            return self._parent._cast(
                _3478.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3389,
            )

            return self._parent._cast(
                _3389.BevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3377,
            )

            return self._parent._cast(
                _3377.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3405,
            )

            return self._parent._cast(
                _3405.ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3431,
            )

            return self._parent._cast(
                _3431.GearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3450,
            )

            return self._parent._cast(
                _3450.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3398,
            )

            return self._parent._cast(
                _3398.ComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3452,
            )

            return self._parent._cast(
                _3452.PartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_analysis(
            self: "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3355.StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3355.StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft._Cast_StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft(
            self
        )
