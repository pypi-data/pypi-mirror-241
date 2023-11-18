"""SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3650,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2542
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3602,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3731,
        _3732,
    )


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
)


class SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed(
    _3650.BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
):
    """SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            return self._parent._cast(
                _3650.BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3638,
            )

            return self._parent._cast(
                _3638.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3666,
            )

            return self._parent._cast(
                _3666.ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3692,
            )

            return self._parent._cast(
                _3692.GearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3730,
            )

            return self._parent._cast(
                _3730.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3632,
            )

            return self._parent._cast(
                _3632.AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3711,
            )

            return self._parent._cast(
                _3711.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_analysis(
            self: "SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2542.SpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.SpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2542.SpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.SpiralBevelGearSet

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
    ) -> "List[_3602.SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed]

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
    def spiral_bevel_gears_compound_steady_state_synchronous_response_at_a_speed(
        self: Self,
    ) -> "List[_3731.SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound.SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.SpiralBevelGearsCompoundSteadyStateSynchronousResponseAtASpeed
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spiral_bevel_meshes_compound_steady_state_synchronous_response_at_a_speed(
        self: Self,
    ) -> (
        "List[_3732.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed]"
    ):
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.SpiralBevelMeshesCompoundSteadyStateSynchronousResponseAtASpeed
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3602.SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        return (
            self._Cast_SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed(
                self
            )
        )
