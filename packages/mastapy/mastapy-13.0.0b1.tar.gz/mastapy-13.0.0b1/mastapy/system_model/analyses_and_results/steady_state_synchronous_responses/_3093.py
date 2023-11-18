"""StraightBevelGearMeshSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _2997,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "StraightBevelGearMeshSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2325
    from mastapy.system_model.analyses_and_results.static_loads import _6961


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearMeshSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="StraightBevelGearMeshSteadyStateSynchronousResponse")


class StraightBevelGearMeshSteadyStateSynchronousResponse(
    _2997.BevelGearMeshSteadyStateSynchronousResponse
):
    """StraightBevelGearMeshSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelGearMeshSteadyStateSynchronousResponse"
    )

    class _Cast_StraightBevelGearMeshSteadyStateSynchronousResponse:
        """Special nested class for casting StraightBevelGearMeshSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponse._Cast_StraightBevelGearMeshSteadyStateSynchronousResponse",
            parent: "StraightBevelGearMeshSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_steady_state_synchronous_response(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponse._Cast_StraightBevelGearMeshSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(_2997.BevelGearMeshSteadyStateSynchronousResponse)

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponse._Cast_StraightBevelGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2985,
            )

            return self._parent._cast(
                _2985.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponse._Cast_StraightBevelGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3013,
            )

            return self._parent._cast(
                _3013.ConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def gear_mesh_steady_state_synchronous_response(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponse._Cast_StraightBevelGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3040,
            )

            return self._parent._cast(_3040.GearMeshSteadyStateSynchronousResponse)

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponse._Cast_StraightBevelGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3047,
            )

            return self._parent._cast(
                _3047.InterMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def connection_steady_state_synchronous_response(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponse._Cast_StraightBevelGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3016,
            )

            return self._parent._cast(_3016.ConnectionSteadyStateSynchronousResponse)

        @property
        def connection_static_load_analysis_case(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponse._Cast_StraightBevelGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponse._Cast_StraightBevelGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponse._Cast_StraightBevelGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponse._Cast_StraightBevelGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponse._Cast_StraightBevelGearMeshSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponse._Cast_StraightBevelGearMeshSteadyStateSynchronousResponse",
        ) -> "StraightBevelGearMeshSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearMeshSteadyStateSynchronousResponse._Cast_StraightBevelGearMeshSteadyStateSynchronousResponse",
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
        instance_to_wrap: "StraightBevelGearMeshSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2325.StraightBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6961.StraightBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelGearMeshSteadyStateSynchronousResponse._Cast_StraightBevelGearMeshSteadyStateSynchronousResponse":
        return self._Cast_StraightBevelGearMeshSteadyStateSynchronousResponse(self)
