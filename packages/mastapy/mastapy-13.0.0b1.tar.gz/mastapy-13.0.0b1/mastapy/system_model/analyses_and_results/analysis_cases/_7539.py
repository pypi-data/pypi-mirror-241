"""ConnectionTimeSeriesLoadAnalysisCase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results.analysis_cases import _7535
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_TIME_SERIES_LOAD_ANALYSIS_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases",
    "ConnectionTimeSeriesLoadAnalysisCase",
)


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionTimeSeriesLoadAnalysisCase",)


Self = TypeVar("Self", bound="ConnectionTimeSeriesLoadAnalysisCase")


class ConnectionTimeSeriesLoadAnalysisCase(_7535.ConnectionAnalysisCase):
    """ConnectionTimeSeriesLoadAnalysisCase

    This is a mastapy class.
    """

    TYPE = _CONNECTION_TIME_SERIES_LOAD_ANALYSIS_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectionTimeSeriesLoadAnalysisCase")

    class _Cast_ConnectionTimeSeriesLoadAnalysisCase:
        """Special nested class for casting ConnectionTimeSeriesLoadAnalysisCase to subclasses."""

        def __init__(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
            parent: "ConnectionTimeSeriesLoadAnalysisCase",
        ):
            self._parent = parent

        @property
        def connection_analysis_case(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ):
            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5376

            return self._parent._cast(
                _5376.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5377

            return self._parent._cast(
                _5377.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def belt_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5384

            return self._parent._cast(_5384.BeltConnectionMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5386

            return self._parent._cast(
                _5386.BevelDifferentialGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5391

            return self._parent._cast(_5391.BevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def clutch_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5396

            return self._parent._cast(_5396.ClutchConnectionMultibodyDynamicsAnalysis)

        @property
        def coaxial_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5400

            return self._parent._cast(_5400.CoaxialConnectionMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5402

            return self._parent._cast(
                _5402.ConceptCouplingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def concept_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5405

            return self._parent._cast(_5405.ConceptGearMeshMultibodyDynamicsAnalysis)

        @property
        def conical_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5408

            return self._parent._cast(_5408.ConicalGearMeshMultibodyDynamicsAnalysis)

        @property
        def connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5411

            return self._parent._cast(_5411.ConnectionMultibodyDynamicsAnalysis)

        @property
        def coupling_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5413

            return self._parent._cast(_5413.CouplingConnectionMultibodyDynamicsAnalysis)

        @property
        def cvt_belt_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5416

            return self._parent._cast(_5416.CVTBeltConnectionMultibodyDynamicsAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5420

            return self._parent._cast(
                _5420.CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5422

            return self._parent._cast(
                _5422.CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5423

            return self._parent._cast(
                _5423.CylindricalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def face_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5429

            return self._parent._cast(_5429.FaceGearMeshMultibodyDynamicsAnalysis)

        @property
        def gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5434

            return self._parent._cast(_5434.GearMeshMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5439

            return self._parent._cast(_5439.HypoidGearMeshMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5446

            return self._parent._cast(
                _5446.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5447

            return self._parent._cast(
                _5447.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5450

            return self._parent._cast(
                _5450.KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5453

            return self._parent._cast(
                _5453.KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5465

            return self._parent._cast(
                _5465.PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def planetary_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5468

            return self._parent._cast(
                _5468.PlanetaryConnectionMultibodyDynamicsAnalysis
            )

        @property
        def ring_pins_to_disc_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5475

            return self._parent._cast(
                _5475.RingPinsToDiscConnectionMultibodyDynamicsAnalysis
            )

        @property
        def rolling_ring_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5477

            return self._parent._cast(
                _5477.RollingRingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5484

            return self._parent._cast(
                _5484.ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5487

            return self._parent._cast(
                _5487.SpiralBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5490

            return self._parent._cast(
                _5490.SpringDamperConnectionMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5493

            return self._parent._cast(
                _5493.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5496

            return self._parent._cast(
                _5496.StraightBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5505

            return self._parent._cast(
                _5505.TorqueConverterConnectionMultibodyDynamicsAnalysis
            )

        @property
        def worm_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5514

            return self._parent._cast(_5514.WormGearMeshMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5517

            return self._parent._cast(_5517.ZerolBevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "ConnectionTimeSeriesLoadAnalysisCase":
            return self._parent

        def __getattr__(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
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
        self: Self, instance_to_wrap: "ConnectionTimeSeriesLoadAnalysisCase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase":
        return self._Cast_ConnectionTimeSeriesLoadAnalysisCase(self)
