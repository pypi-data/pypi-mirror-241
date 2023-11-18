"""HypoidGearSetSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3248,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "HypoidGearSetSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2533
    from mastapy.system_model.analyses_and_results.static_loads import _6905
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3307,
        _3305,
    )


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearSetSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="HypoidGearSetSteadyStateSynchronousResponseOnAShaft")


class HypoidGearSetSteadyStateSynchronousResponseOnAShaft(
    _3248.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft
):
    """HypoidGearSetSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_HypoidGearSetSteadyStateSynchronousResponseOnAShaft"
    )

    class _Cast_HypoidGearSetSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting HypoidGearSetSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "HypoidGearSetSteadyStateSynchronousResponseOnAShaft._Cast_HypoidGearSetSteadyStateSynchronousResponseOnAShaft",
            parent: "HypoidGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "HypoidGearSetSteadyStateSynchronousResponseOnAShaft._Cast_HypoidGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            return self._parent._cast(
                _3248.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "HypoidGearSetSteadyStateSynchronousResponseOnAShaft._Cast_HypoidGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3276,
            )

            return self._parent._cast(
                _3276.ConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "HypoidGearSetSteadyStateSynchronousResponseOnAShaft._Cast_HypoidGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3302,
            )

            return self._parent._cast(
                _3302.GearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def specialised_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "HypoidGearSetSteadyStateSynchronousResponseOnAShaft._Cast_HypoidGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3341,
            )

            return self._parent._cast(
                _3341.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "HypoidGearSetSteadyStateSynchronousResponseOnAShaft._Cast_HypoidGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3243,
            )

            return self._parent._cast(
                _3243.AbstractAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "HypoidGearSetSteadyStateSynchronousResponseOnAShaft._Cast_HypoidGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3322,
            )

            return self._parent._cast(_3322.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "HypoidGearSetSteadyStateSynchronousResponseOnAShaft._Cast_HypoidGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "HypoidGearSetSteadyStateSynchronousResponseOnAShaft._Cast_HypoidGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "HypoidGearSetSteadyStateSynchronousResponseOnAShaft._Cast_HypoidGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearSetSteadyStateSynchronousResponseOnAShaft._Cast_HypoidGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearSetSteadyStateSynchronousResponseOnAShaft._Cast_HypoidGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def hypoid_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "HypoidGearSetSteadyStateSynchronousResponseOnAShaft._Cast_HypoidGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "HypoidGearSetSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "HypoidGearSetSteadyStateSynchronousResponseOnAShaft._Cast_HypoidGearSetSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "HypoidGearSetSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2533.HypoidGearSet":
        """mastapy.system_model.part_model.gears.HypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6905.HypoidGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def hypoid_gears_steady_state_synchronous_response_on_a_shaft(
        self: Self,
    ) -> "List[_3307.HypoidGearSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.HypoidGearSteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearsSteadyStateSynchronousResponseOnAShaft

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_meshes_steady_state_synchronous_response_on_a_shaft(
        self: Self,
    ) -> "List[_3305.HypoidGearMeshSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.HypoidGearMeshSteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidMeshesSteadyStateSynchronousResponseOnAShaft

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "HypoidGearSetSteadyStateSynchronousResponseOnAShaft._Cast_HypoidGearSetSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_HypoidGearSetSteadyStateSynchronousResponseOnAShaft(self)
