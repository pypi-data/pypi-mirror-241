"""AGMAGleasonConicalGearMeshDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6307
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "AGMAGleasonConicalGearMeshDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2297


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshDynamicAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearMeshDynamicAnalysis")


class AGMAGleasonConicalGearMeshDynamicAnalysis(_6307.ConicalGearMeshDynamicAnalysis):
    """AGMAGleasonConicalGearMeshDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearMeshDynamicAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearMeshDynamicAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearMeshDynamicAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis",
            parent: "AGMAGleasonConicalGearMeshDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_dynamic_analysis(
            self: "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis",
        ):
            return self._parent._cast(_6307.ConicalGearMeshDynamicAnalysis)

        @property
        def gear_mesh_dynamic_analysis(
            self: "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6335

            return self._parent._cast(_6335.GearMeshDynamicAnalysis)

        @property
        def inter_mountable_component_connection_dynamic_analysis(
            self: "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6341

            return self._parent._cast(
                _6341.InterMountableComponentConnectionDynamicAnalysis
            )

        @property
        def connection_dynamic_analysis(
            self: "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6309

            return self._parent._cast(_6309.ConnectionDynamicAnalysis)

        @property
        def connection_fe_analysis(
            self: "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_dynamic_analysis(
            self: "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6286

            return self._parent._cast(_6286.BevelDifferentialGearMeshDynamicAnalysis)

        @property
        def bevel_gear_mesh_dynamic_analysis(
            self: "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6291

            return self._parent._cast(_6291.BevelGearMeshDynamicAnalysis)

        @property
        def hypoid_gear_mesh_dynamic_analysis(
            self: "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6339

            return self._parent._cast(_6339.HypoidGearMeshDynamicAnalysis)

        @property
        def spiral_bevel_gear_mesh_dynamic_analysis(
            self: "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6376

            return self._parent._cast(_6376.SpiralBevelGearMeshDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_dynamic_analysis(
            self: "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6382

            return self._parent._cast(_6382.StraightBevelDiffGearMeshDynamicAnalysis)

        @property
        def straight_bevel_gear_mesh_dynamic_analysis(
            self: "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6385

            return self._parent._cast(_6385.StraightBevelGearMeshDynamicAnalysis)

        @property
        def zerol_bevel_gear_mesh_dynamic_analysis(
            self: "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6403

            return self._parent._cast(_6403.ZerolBevelGearMeshDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_dynamic_analysis(
            self: "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis",
        ) -> "AGMAGleasonConicalGearMeshDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearMeshDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2297.AGMAGleasonConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh

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
    ) -> "AGMAGleasonConicalGearMeshDynamicAnalysis._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis":
        return self._Cast_AGMAGleasonConicalGearMeshDynamicAnalysis(self)
