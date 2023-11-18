"""BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3379,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3260,
    )


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft"
)


class BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft(
    _3379.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
):
    """BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            return self._parent._cast(
                _3379.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3407,
            )

            return self._parent._cast(
                _3407.ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3433,
            )

            return self._parent._cast(
                _3433.GearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3471,
            )

            return self._parent._cast(
                _3471.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3373,
            )

            return self._parent._cast(
                _3373.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3452,
            )

            return self._parent._cast(
                _3452.PartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_analysis(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3386,
            )

            return self._parent._cast(
                _3386.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3474,
            )

            return self._parent._cast(
                _3474.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3480,
            )

            return self._parent._cast(
                _3480.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3483,
            )

            return self._parent._cast(
                _3483.StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3501,
            )

            return self._parent._cast(
                _3501.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3260.BevelGearSetSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.BevelGearSetSteadyStateSynchronousResponseOnAShaft]

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
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3260.BevelGearSetSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.BevelGearSetSteadyStateSynchronousResponseOnAShaft]

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
    def cast_to(
        self: Self,
    ) -> "BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft(
            self
        )
