"""ConicalGearMeshMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5434
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "ConicalGearMeshMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2305


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="ConicalGearMeshMultibodyDynamicsAnalysis")


class ConicalGearMeshMultibodyDynamicsAnalysis(_5434.GearMeshMultibodyDynamicsAnalysis):
    """ConicalGearMeshMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearMeshMultibodyDynamicsAnalysis"
    )

    class _Cast_ConicalGearMeshMultibodyDynamicsAnalysis:
        """Special nested class for casting ConicalGearMeshMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
            parent: "ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5434.GearMeshMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5446

            return self._parent._cast(
                _5446.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def connection_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5411

            return self._parent._cast(_5411.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5377

            return self._parent._cast(
                _5377.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_gear_mesh_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5386

            return self._parent._cast(
                _5386.BevelDifferentialGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5391

            return self._parent._cast(_5391.BevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_mesh_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5439

            return self._parent._cast(_5439.HypoidGearMeshMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5447

            return self._parent._cast(
                _5447.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5450

            return self._parent._cast(
                _5450.KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5453

            return self._parent._cast(
                _5453.KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5487

            return self._parent._cast(
                _5487.SpiralBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5493

            return self._parent._cast(
                _5493.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5496

            return self._parent._cast(
                _5496.StraightBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5517

            return self._parent._cast(_5517.ZerolBevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def conical_gear_mesh_multibody_dynamics_analysis(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "ConicalGearMeshMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "ConicalGearMeshMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2305.ConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ConicalGearMeshMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ConicalGearMeshMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearMeshMultibodyDynamicsAnalysis._Cast_ConicalGearMeshMultibodyDynamicsAnalysis":
        return self._Cast_ConicalGearMeshMultibodyDynamicsAnalysis(self)
