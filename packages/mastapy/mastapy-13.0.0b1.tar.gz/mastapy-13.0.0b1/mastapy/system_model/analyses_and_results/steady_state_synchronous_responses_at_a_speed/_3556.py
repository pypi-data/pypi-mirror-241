"""FaceGearSetSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3561,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "FaceGearSetSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2527
    from mastapy.system_model.analyses_and_results.static_loads import _6884
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3557,
        _3555,
    )


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearSetSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="FaceGearSetSteadyStateSynchronousResponseAtASpeed")


class FaceGearSetSteadyStateSynchronousResponseAtASpeed(
    _3561.GearSetSteadyStateSynchronousResponseAtASpeed
):
    """FaceGearSetSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FaceGearSetSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_FaceGearSetSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting FaceGearSetSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "FaceGearSetSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearSetSteadyStateSynchronousResponseAtASpeed",
            parent: "FaceGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def gear_set_steady_state_synchronous_response_at_a_speed(
            self: "FaceGearSetSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            return self._parent._cast(
                _3561.GearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def specialised_assembly_steady_state_synchronous_response_at_a_speed(
            self: "FaceGearSetSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3600,
            )

            return self._parent._cast(
                _3600.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_at_a_speed(
            self: "FaceGearSetSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3502,
            )

            return self._parent._cast(
                _3502.AbstractAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "FaceGearSetSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3581,
            )

            return self._parent._cast(_3581.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "FaceGearSetSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FaceGearSetSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FaceGearSetSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearSetSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearSetSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def face_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "FaceGearSetSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "FaceGearSetSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "FaceGearSetSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearSetSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "FaceGearSetSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2527.FaceGearSet":
        """mastapy.system_model.part_model.gears.FaceGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6884.FaceGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FaceGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def face_gears_steady_state_synchronous_response_at_a_speed(
        self: Self,
    ) -> "List[_3557.FaceGearSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.FaceGearSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGearsSteadyStateSynchronousResponseAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_meshes_steady_state_synchronous_response_at_a_speed(
        self: Self,
    ) -> "List[_3555.FaceGearMeshSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.FaceGearMeshSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceMeshesSteadyStateSynchronousResponseAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "FaceGearSetSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearSetSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_FaceGearSetSteadyStateSynchronousResponseAtASpeed(self)
