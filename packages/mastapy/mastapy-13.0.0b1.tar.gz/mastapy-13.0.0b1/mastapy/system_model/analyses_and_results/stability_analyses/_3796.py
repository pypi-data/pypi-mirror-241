"""ConnectionStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7538
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "ConnectionStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2270
    from mastapy.system_model.analyses_and_results.stability_analyses import _3868


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionStabilityAnalysis",)


Self = TypeVar("Self", bound="ConnectionStabilityAnalysis")


class ConnectionStabilityAnalysis(_7538.ConnectionStaticLoadAnalysisCase):
    """ConnectionStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTION_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectionStabilityAnalysis")

    class _Cast_ConnectionStabilityAnalysis:
        """Special nested class for casting ConnectionStabilityAnalysis to subclasses."""

        def __init__(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
            parent: "ConnectionStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def connection_static_load_analysis_case(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ):
            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3764,
            )

            return self._parent._cast(
                _3764.AbstractShaftToMountableComponentConnectionStabilityAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3765,
            )

            return self._parent._cast(_3765.AGMAGleasonConicalGearMeshStabilityAnalysis)

        @property
        def belt_connection_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3770,
            )

            return self._parent._cast(_3770.BeltConnectionStabilityAnalysis)

        @property
        def bevel_differential_gear_mesh_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3772,
            )

            return self._parent._cast(_3772.BevelDifferentialGearMeshStabilityAnalysis)

        @property
        def bevel_gear_mesh_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3777,
            )

            return self._parent._cast(_3777.BevelGearMeshStabilityAnalysis)

        @property
        def clutch_connection_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3782,
            )

            return self._parent._cast(_3782.ClutchConnectionStabilityAnalysis)

        @property
        def coaxial_connection_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3785,
            )

            return self._parent._cast(_3785.CoaxialConnectionStabilityAnalysis)

        @property
        def concept_coupling_connection_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3787,
            )

            return self._parent._cast(_3787.ConceptCouplingConnectionStabilityAnalysis)

        @property
        def concept_gear_mesh_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3790,
            )

            return self._parent._cast(_3790.ConceptGearMeshStabilityAnalysis)

        @property
        def conical_gear_mesh_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3793,
            )

            return self._parent._cast(_3793.ConicalGearMeshStabilityAnalysis)

        @property
        def coupling_connection_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3798,
            )

            return self._parent._cast(_3798.CouplingConnectionStabilityAnalysis)

        @property
        def cvt_belt_connection_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3802,
            )

            return self._parent._cast(_3802.CVTBeltConnectionStabilityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3806,
            )

            return self._parent._cast(
                _3806.CycloidalDiscCentralBearingConnectionStabilityAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3807,
            )

            return self._parent._cast(
                _3807.CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis
            )

        @property
        def cylindrical_gear_mesh_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3809,
            )

            return self._parent._cast(_3809.CylindricalGearMeshStabilityAnalysis)

        @property
        def face_gear_mesh_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3816,
            )

            return self._parent._cast(_3816.FaceGearMeshStabilityAnalysis)

        @property
        def gear_mesh_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3821,
            )

            return self._parent._cast(_3821.GearMeshStabilityAnalysis)

        @property
        def hypoid_gear_mesh_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3825,
            )

            return self._parent._cast(_3825.HypoidGearMeshStabilityAnalysis)

        @property
        def inter_mountable_component_connection_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3828,
            )

            return self._parent._cast(
                _3828.InterMountableComponentConnectionStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3829,
            )

            return self._parent._cast(
                _3829.KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3832,
            )

            return self._parent._cast(
                _3832.KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3835,
            )

            return self._parent._cast(
                _3835.KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3843,
            )

            return self._parent._cast(
                _3843.PartToPartShearCouplingConnectionStabilityAnalysis
            )

        @property
        def planetary_connection_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3846,
            )

            return self._parent._cast(_3846.PlanetaryConnectionStabilityAnalysis)

        @property
        def ring_pins_to_disc_connection_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3853,
            )

            return self._parent._cast(_3853.RingPinsToDiscConnectionStabilityAnalysis)

        @property
        def rolling_ring_connection_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3855,
            )

            return self._parent._cast(_3855.RollingRingConnectionStabilityAnalysis)

        @property
        def shaft_to_mountable_component_connection_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3860,
            )

            return self._parent._cast(
                _3860.ShaftToMountableComponentConnectionStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3862,
            )

            return self._parent._cast(_3862.SpiralBevelGearMeshStabilityAnalysis)

        @property
        def spring_damper_connection_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3865,
            )

            return self._parent._cast(_3865.SpringDamperConnectionStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3871,
            )

            return self._parent._cast(_3871.StraightBevelDiffGearMeshStabilityAnalysis)

        @property
        def straight_bevel_gear_mesh_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3874,
            )

            return self._parent._cast(_3874.StraightBevelGearMeshStabilityAnalysis)

        @property
        def torque_converter_connection_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3883,
            )

            return self._parent._cast(_3883.TorqueConverterConnectionStabilityAnalysis)

        @property
        def worm_gear_mesh_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3889,
            )

            return self._parent._cast(_3889.WormGearMeshStabilityAnalysis)

        @property
        def zerol_bevel_gear_mesh_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3892,
            )

            return self._parent._cast(_3892.ZerolBevelGearMeshStabilityAnalysis)

        @property
        def connection_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "ConnectionStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectionStabilityAnalysis.TYPE"):
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
    def stability_analysis(self: Self) -> "_3868.StabilityAnalysis":
        """mastapy.system_model.analyses_and_results.stability_analyses.StabilityAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StabilityAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis":
        return self._Cast_ConnectionStabilityAnalysis(self)
