"""WormGearMeshSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3301,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "WormGearMeshSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2327
    from mastapy.system_model.analyses_and_results.static_loads import _6981


__docformat__ = "restructuredtext en"
__all__ = ("WormGearMeshSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="WormGearMeshSteadyStateSynchronousResponseOnAShaft")


class WormGearMeshSteadyStateSynchronousResponseOnAShaft(
    _3301.GearMeshSteadyStateSynchronousResponseOnAShaft
):
    """WormGearMeshSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_WormGearMeshSteadyStateSynchronousResponseOnAShaft"
    )

    class _Cast_WormGearMeshSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting WormGearMeshSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "WormGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_WormGearMeshSteadyStateSynchronousResponseOnAShaft",
            parent: "WormGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "WormGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_WormGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            return self._parent._cast(
                _3301.GearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "WormGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_WormGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3308,
            )

            return self._parent._cast(
                _3308.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_steady_state_synchronous_response_on_a_shaft(
            self: "WormGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_WormGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3278,
            )

            return self._parent._cast(
                _3278.ConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_static_load_analysis_case(
            self: "WormGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_WormGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "WormGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_WormGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "WormGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_WormGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "WormGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_WormGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_WormGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def worm_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "WormGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_WormGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "WormGearMeshSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "WormGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_WormGearMeshSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "WormGearMeshSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2327.WormGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.WormGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6981.WormGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.WormGearMeshLoadCase

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
    ) -> "WormGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_WormGearMeshSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_WormGearMeshSteadyStateSynchronousResponseOnAShaft(self)
