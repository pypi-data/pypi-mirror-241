"""ConnectionSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7538
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "ConnectionSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2270
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3607,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="ConnectionSteadyStateSynchronousResponseAtASpeed")


class ConnectionSteadyStateSynchronousResponseAtASpeed(
    _7538.ConnectionStaticLoadAnalysisCase
):
    """ConnectionSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConnectionSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_ConnectionSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting ConnectionSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
            parent: "ConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def connection_static_load_analysis_case(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3505,
            )

            return self._parent._cast(
                _3505.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3506,
            )

            return self._parent._cast(
                _3506.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def belt_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3511,
            )

            return self._parent._cast(
                _3511.BeltConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3513,
            )

            return self._parent._cast(
                _3513.BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3518,
            )

            return self._parent._cast(
                _3518.BevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def clutch_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3523,
            )

            return self._parent._cast(
                _3523.ClutchConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coaxial_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3526,
            )

            return self._parent._cast(
                _3526.CoaxialConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3528,
            )

            return self._parent._cast(
                _3528.ConceptCouplingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3531,
            )

            return self._parent._cast(
                _3531.ConceptGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3534,
            )

            return self._parent._cast(
                _3534.ConicalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3539,
            )

            return self._parent._cast(
                _3539.CouplingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_belt_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3542,
            )

            return self._parent._cast(
                _3542.CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cycloidal_disc_central_bearing_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3546,
            )

            return self._parent._cast(
                _3546.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3547,
            )

            return self._parent._cast(
                _3547.CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3549,
            )

            return self._parent._cast(
                _3549.CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3555,
            )

            return self._parent._cast(
                _3555.FaceGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3560,
            )

            return self._parent._cast(
                _3560.GearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3564,
            )

            return self._parent._cast(
                _3564.HypoidGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3567,
            )

            return self._parent._cast(
                _3567.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3568,
            )

            return self._parent._cast(
                _3568.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3571,
            )

            return self._parent._cast(
                _3571.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3574,
            )

            return self._parent._cast(
                _3574.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3582,
            )

            return self._parent._cast(
                _3582.PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planetary_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3585,
            )

            return self._parent._cast(
                _3585.PlanetaryConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def ring_pins_to_disc_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3592,
            )

            return self._parent._cast(
                _3592.RingPinsToDiscConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3594,
            )

            return self._parent._cast(
                _3594.RollingRingConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_to_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3599,
            )

            return self._parent._cast(
                _3599.ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3601,
            )

            return self._parent._cast(
                _3601.SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3604,
            )

            return self._parent._cast(
                _3604.SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3608,
            )

            return self._parent._cast(
                _3608.StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3611,
            )

            return self._parent._cast(
                _3611.StraightBevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3620,
            )

            return self._parent._cast(
                _3620.TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3626,
            )

            return self._parent._cast(
                _3626.WormGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3629,
            )

            return self._parent._cast(
                _3629.ZerolBevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_steady_state_synchronous_response_at_a_speed(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
        ) -> "ConnectionSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "ConnectionSteadyStateSynchronousResponseAtASpeed.TYPE",
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
    def steady_state_synchronous_response_at_a_speed(
        self: Self,
    ) -> "_3607.SteadyStateSynchronousResponseAtASpeed":
        """mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.SteadyStateSynchronousResponseAtASpeed

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SteadyStateSynchronousResponseAtASpeed

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_ConnectionSteadyStateSynchronousResponseAtASpeed(self)
