"""PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3291,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2540


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft")


class PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft(
    _3291.CylindricalGearSetSteadyStateSynchronousResponseOnAShaft
):
    """PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft",
            parent: "PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            return self._parent._cast(
                _3291.CylindricalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3302,
            )

            return self._parent._cast(
                _3302.GearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def specialised_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3341,
            )

            return self._parent._cast(
                _3341.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3243,
            )

            return self._parent._cast(
                _3243.AbstractAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3322,
            )

            return self._parent._cast(_3322.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def planetary_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft.TYPE",
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
    ) -> "PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft(self)
