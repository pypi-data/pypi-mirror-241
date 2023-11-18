"""ConnectionSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7538
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "ConnectionSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2270
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3087,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="ConnectionSteadyStateSynchronousResponse")


class ConnectionSteadyStateSynchronousResponse(_7538.ConnectionStaticLoadAnalysisCase):
    """ConnectionSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConnectionSteadyStateSynchronousResponse"
    )

    class _Cast_ConnectionSteadyStateSynchronousResponse:
        """Special nested class for casting ConnectionSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
            parent: "ConnectionSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def connection_static_load_analysis_case(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2984,
            )

            return self._parent._cast(
                _2984.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2985,
            )

            return self._parent._cast(
                _2985.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def belt_connection_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2990,
            )

            return self._parent._cast(
                _2990.BeltConnectionSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2992,
            )

            return self._parent._cast(
                _2992.BevelDifferentialGearMeshSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2997,
            )

            return self._parent._cast(_2997.BevelGearMeshSteadyStateSynchronousResponse)

        @property
        def clutch_connection_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3002,
            )

            return self._parent._cast(
                _3002.ClutchConnectionSteadyStateSynchronousResponse
            )

        @property
        def coaxial_connection_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3005,
            )

            return self._parent._cast(
                _3005.CoaxialConnectionSteadyStateSynchronousResponse
            )

        @property
        def concept_coupling_connection_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3007,
            )

            return self._parent._cast(
                _3007.ConceptCouplingConnectionSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3010,
            )

            return self._parent._cast(
                _3010.ConceptGearMeshSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3013,
            )

            return self._parent._cast(
                _3013.ConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def coupling_connection_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3018,
            )

            return self._parent._cast(
                _3018.CouplingConnectionSteadyStateSynchronousResponse
            )

        @property
        def cvt_belt_connection_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3021,
            )

            return self._parent._cast(
                _3021.CVTBeltConnectionSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_central_bearing_connection_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3025,
            )

            return self._parent._cast(
                _3025.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3026,
            )

            return self._parent._cast(
                _3026.CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3028,
            )

            return self._parent._cast(
                _3028.CylindricalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def face_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3035,
            )

            return self._parent._cast(_3035.FaceGearMeshSteadyStateSynchronousResponse)

        @property
        def gear_mesh_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3040,
            )

            return self._parent._cast(_3040.GearMeshSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3044,
            )

            return self._parent._cast(
                _3044.HypoidGearMeshSteadyStateSynchronousResponse
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3047,
            )

            return self._parent._cast(
                _3047.InterMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3048,
            )

            return self._parent._cast(
                _3048.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3051,
            )

            return self._parent._cast(
                _3051.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3054,
            )

            return self._parent._cast(
                _3054.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def part_to_part_shear_coupling_connection_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3062,
            )

            return self._parent._cast(
                _3062.PartToPartShearCouplingConnectionSteadyStateSynchronousResponse
            )

        @property
        def planetary_connection_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3065,
            )

            return self._parent._cast(
                _3065.PlanetaryConnectionSteadyStateSynchronousResponse
            )

        @property
        def ring_pins_to_disc_connection_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3072,
            )

            return self._parent._cast(
                _3072.RingPinsToDiscConnectionSteadyStateSynchronousResponse
            )

        @property
        def rolling_ring_connection_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3074,
            )

            return self._parent._cast(
                _3074.RollingRingConnectionSteadyStateSynchronousResponse
            )

        @property
        def shaft_to_mountable_component_connection_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3079,
            )

            return self._parent._cast(
                _3079.ShaftToMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3081,
            )

            return self._parent._cast(
                _3081.SpiralBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_connection_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3084,
            )

            return self._parent._cast(
                _3084.SpringDamperConnectionSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3090,
            )

            return self._parent._cast(
                _3090.StraightBevelDiffGearMeshSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3093,
            )

            return self._parent._cast(
                _3093.StraightBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_connection_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3102,
            )

            return self._parent._cast(
                _3102.TorqueConverterConnectionSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3108,
            )

            return self._parent._cast(_3108.WormGearMeshSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_mesh_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3111,
            )

            return self._parent._cast(
                _3111.ZerolBevelGearMeshSteadyStateSynchronousResponse
            )

        @property
        def connection_steady_state_synchronous_response(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
        ) -> "ConnectionSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse",
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
        self: Self, instance_to_wrap: "ConnectionSteadyStateSynchronousResponse.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2270.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2270.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def steady_state_synchronous_response(
        self: Self,
    ) -> "_3087.SteadyStateSynchronousResponse":
        """mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.SteadyStateSynchronousResponse

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SteadyStateSynchronousResponse

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConnectionSteadyStateSynchronousResponse._Cast_ConnectionSteadyStateSynchronousResponse":
        return self._Cast_ConnectionSteadyStateSynchronousResponse(self)
