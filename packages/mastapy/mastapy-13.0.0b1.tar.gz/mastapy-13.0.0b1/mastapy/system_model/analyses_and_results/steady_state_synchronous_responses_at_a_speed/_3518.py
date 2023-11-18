"""BevelGearMeshSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3506,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "BevelGearMeshSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2301


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="BevelGearMeshSteadyStateSynchronousResponseAtASpeed")


class BevelGearMeshSteadyStateSynchronousResponseAtASpeed(
    _3506.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed
):
    """BevelGearMeshSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearMeshSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_BevelGearMeshSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting BevelGearMeshSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "BevelGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearMeshSteadyStateSynchronousResponseAtASpeed",
            parent: "BevelGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "BevelGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            return self._parent._cast(
                _3506.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "BevelGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3534,
            )

            return self._parent._cast(
                _3534.ConicalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "BevelGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3560,
            )

            return self._parent._cast(
                _3560.GearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
            self: "BevelGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3567,
            )

            return self._parent._cast(
                _3567.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_steady_state_synchronous_response_at_a_speed(
            self: "BevelGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3537,
            )

            return self._parent._cast(
                _3537.ConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_static_load_analysis_case(
            self: "BevelGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "BevelGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3513,
            )

            return self._parent._cast(
                _3513.BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "BevelGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3601,
            )

            return self._parent._cast(
                _3601.SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "BevelGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3608,
            )

            return self._parent._cast(
                _3608.StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "BevelGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3611,
            )

            return self._parent._cast(
                _3611.StraightBevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "BevelGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3629,
            )

            return self._parent._cast(
                _3629.ZerolBevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "BevelGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "BevelGearMeshSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearMeshSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "BevelGearMeshSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2301.BevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BevelGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_BevelGearMeshSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_BevelGearMeshSteadyStateSynchronousResponseAtASpeed(self)
