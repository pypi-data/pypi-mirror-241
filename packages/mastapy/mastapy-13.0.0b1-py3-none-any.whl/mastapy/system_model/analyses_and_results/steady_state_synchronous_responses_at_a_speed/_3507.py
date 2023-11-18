"""AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3535,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2512


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed"
)


class AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed(
    _3535.ConicalGearSetSteadyStateSynchronousResponseAtASpeed
):
    """AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
            parent: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            return self._parent._cast(
                _3535.ConicalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3561,
            )

            return self._parent._cast(
                _3561.GearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def specialised_assembly_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3600,
            )

            return self._parent._cast(
                _3600.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3502,
            )

            return self._parent._cast(
                _3502.AbstractAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3581,
            )

            return self._parent._cast(_3581.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3514,
            )

            return self._parent._cast(
                _3514.BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3519,
            )

            return self._parent._cast(
                _3519.BevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3565,
            )

            return self._parent._cast(
                _3565.HypoidGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3602,
            )

            return self._parent._cast(
                _3602.SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3609,
            )

            return self._parent._cast(
                _3609.StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3612,
            )

            return self._parent._cast(
                _3612.StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3630,
            )

            return self._parent._cast(
                _3630.ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2512.AGMAGleasonConicalGearSet":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed":
        return (
            self._Cast_AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed(
                self
            )
        )
