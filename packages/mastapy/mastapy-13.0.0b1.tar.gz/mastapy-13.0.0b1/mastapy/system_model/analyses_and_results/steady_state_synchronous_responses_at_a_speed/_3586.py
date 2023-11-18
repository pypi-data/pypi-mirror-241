"""PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3550,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2540


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed")


class PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed(
    _3550.CylindricalGearSetSteadyStateSynchronousResponseAtASpeed
):
    """PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed",
            parent: "PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            return self._parent._cast(
                _3550.CylindricalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3561,
            )

            return self._parent._cast(
                _3561.GearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def specialised_assembly_steady_state_synchronous_response_at_a_speed(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3600,
            )

            return self._parent._cast(
                _3600.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_at_a_speed(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3502,
            )

            return self._parent._cast(
                _3502.AbstractAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3581,
            )

            return self._parent._cast(_3581.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def planetary_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2540.PlanetaryGearSet":
        """mastapy.system_model.part_model.gears.PlanetaryGearSet

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
    ) -> "PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed._Cast_PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed(self)
