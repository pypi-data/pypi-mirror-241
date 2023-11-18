"""ConnectionModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7538
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "ConnectionModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2270
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5191,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="ConnectionModalAnalysisAtASpeed")


class ConnectionModalAnalysisAtASpeed(_7538.ConnectionStaticLoadAnalysisCase):
    """ConnectionModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CONNECTION_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectionModalAnalysisAtASpeed")

    class _Cast_ConnectionModalAnalysisAtASpeed:
        """Special nested class for casting ConnectionModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
            parent: "ConnectionModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def connection_static_load_analysis_case(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_modal_analysis_at_a_speed(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5117,
            )

            return self._parent._cast(
                _5117.AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5118,
            )

            return self._parent._cast(
                _5118.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed
            )

        @property
        def belt_connection_modal_analysis_at_a_speed(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5123,
            )

            return self._parent._cast(_5123.BeltConnectionModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5125,
            )

            return self._parent._cast(
                _5125.BevelDifferentialGearMeshModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5130,
            )

            return self._parent._cast(_5130.BevelGearMeshModalAnalysisAtASpeed)

        @property
        def clutch_connection_modal_analysis_at_a_speed(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5135,
            )

            return self._parent._cast(_5135.ClutchConnectionModalAnalysisAtASpeed)

        @property
        def coaxial_connection_modal_analysis_at_a_speed(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5138,
            )

            return self._parent._cast(_5138.CoaxialConnectionModalAnalysisAtASpeed)

        @property
        def concept_coupling_connection_modal_analysis_at_a_speed(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5140,
            )

            return self._parent._cast(
                _5140.ConceptCouplingConnectionModalAnalysisAtASpeed
            )

        @property
        def concept_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5143,
            )

            return self._parent._cast(_5143.ConceptGearMeshModalAnalysisAtASpeed)

        @property
        def conical_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5146,
            )

            return self._parent._cast(_5146.ConicalGearMeshModalAnalysisAtASpeed)

        @property
        def coupling_connection_modal_analysis_at_a_speed(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5151,
            )

            return self._parent._cast(_5151.CouplingConnectionModalAnalysisAtASpeed)

        @property
        def cvt_belt_connection_modal_analysis_at_a_speed(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5154,
            )

            return self._parent._cast(_5154.CVTBeltConnectionModalAnalysisAtASpeed)

        @property
        def cycloidal_disc_central_bearing_connection_modal_analysis_at_a_speed(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5158,
            )

            return self._parent._cast(
                _5158.CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_modal_analysis_at_a_speed(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5160,
            )

            return self._parent._cast(
                _5160.CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed
            )

        @property
        def cylindrical_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5161,
            )

            return self._parent._cast(_5161.CylindricalGearMeshModalAnalysisAtASpeed)

        @property
        def face_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5167,
            )

            return self._parent._cast(_5167.FaceGearMeshModalAnalysisAtASpeed)

        @property
        def gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5172,
            )

            return self._parent._cast(_5172.GearMeshModalAnalysisAtASpeed)

        @property
        def hypoid_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5176,
            )

            return self._parent._cast(_5176.HypoidGearMeshModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_speed(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5179,
            )

            return self._parent._cast(
                _5179.InterMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5180,
            )

            return self._parent._cast(
                _5180.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5183,
            )

            return self._parent._cast(
                _5183.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5186,
            )

            return self._parent._cast(
                _5186.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed
            )

        @property
        def part_to_part_shear_coupling_connection_modal_analysis_at_a_speed(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5195,
            )

            return self._parent._cast(
                _5195.PartToPartShearCouplingConnectionModalAnalysisAtASpeed
            )

        @property
        def planetary_connection_modal_analysis_at_a_speed(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5198,
            )

            return self._parent._cast(_5198.PlanetaryConnectionModalAnalysisAtASpeed)

        @property
        def ring_pins_to_disc_connection_modal_analysis_at_a_speed(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5205,
            )

            return self._parent._cast(
                _5205.RingPinsToDiscConnectionModalAnalysisAtASpeed
            )

        @property
        def rolling_ring_connection_modal_analysis_at_a_speed(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5207,
            )

            return self._parent._cast(_5207.RollingRingConnectionModalAnalysisAtASpeed)

        @property
        def shaft_to_mountable_component_connection_modal_analysis_at_a_speed(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5212,
            )

            return self._parent._cast(
                _5212.ShaftToMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5214,
            )

            return self._parent._cast(_5214.SpiralBevelGearMeshModalAnalysisAtASpeed)

        @property
        def spring_damper_connection_modal_analysis_at_a_speed(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5217,
            )

            return self._parent._cast(_5217.SpringDamperConnectionModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5220,
            )

            return self._parent._cast(
                _5220.StraightBevelDiffGearMeshModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5223,
            )

            return self._parent._cast(_5223.StraightBevelGearMeshModalAnalysisAtASpeed)

        @property
        def torque_converter_connection_modal_analysis_at_a_speed(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5232,
            )

            return self._parent._cast(
                _5232.TorqueConverterConnectionModalAnalysisAtASpeed
            )

        @property
        def worm_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5238,
            )

            return self._parent._cast(_5238.WormGearMeshModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5241,
            )

            return self._parent._cast(_5241.ZerolBevelGearMeshModalAnalysisAtASpeed)

        @property
        def connection_modal_analysis_at_a_speed(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
        ) -> "ConnectionModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectionModalAnalysisAtASpeed.TYPE"):
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
    def modal_analysis_at_a_speed(self: Self) -> "_5191.ModalAnalysisAtASpeed":
        """mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.ModalAnalysisAtASpeed

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModalAnalysisAtASpeed

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConnectionModalAnalysisAtASpeed._Cast_ConnectionModalAnalysisAtASpeed":
        return self._Cast_ConnectionModalAnalysisAtASpeed(self)
