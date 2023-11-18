"""ConicalGearSetSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3561,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2522


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="ConicalGearSetSteadyStateSynchronousResponseAtASpeed")


class ConicalGearSetSteadyStateSynchronousResponseAtASpeed(
    _3561.GearSetSteadyStateSynchronousResponseAtASpeed
):
    """ConicalGearSetSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting ConicalGearSetSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
            parent: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def gear_set_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            return self._parent._cast(
                _3561.GearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def specialised_assembly_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3600,
            )

            return self._parent._cast(
                _3600.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3502,
            )

            return self._parent._cast(
                _3502.AbstractAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3581,
            )

            return self._parent._cast(_3581.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3507,
            )

            return self._parent._cast(
                _3507.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3514,
            )

            return self._parent._cast(
                _3514.BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3519,
            )

            return self._parent._cast(
                _3519.BevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3565,
            )

            return self._parent._cast(
                _3565.HypoidGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3569,
            )

            return self._parent._cast(
                _3569.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3572,
            )

            return self._parent._cast(
                _3572.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3575,
            )

            return self._parent._cast(
                _3575.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3602,
            )

            return self._parent._cast(
                _3602.SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3609,
            )

            return self._parent._cast(
                _3609.StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3612,
            )

            return self._parent._cast(
                _3612.StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3630,
            )

            return self._parent._cast(
                _3630.ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "ConicalGearSetSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "ConicalGearSetSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2522.ConicalGearSet":
        """mastapy.system_model.part_model.gears.ConicalGearSet

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
    ) -> "ConicalGearSetSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_ConicalGearSetSteadyStateSynchronousResponseAtASpeed(self)
