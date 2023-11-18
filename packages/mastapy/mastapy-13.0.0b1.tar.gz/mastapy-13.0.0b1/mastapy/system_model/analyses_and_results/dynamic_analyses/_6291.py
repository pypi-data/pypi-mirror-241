"""BevelGearMeshDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6279
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "BevelGearMeshDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2301


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshDynamicAnalysis",)


Self = TypeVar("Self", bound="BevelGearMeshDynamicAnalysis")


class BevelGearMeshDynamicAnalysis(_6279.AGMAGleasonConicalGearMeshDynamicAnalysis):
    """BevelGearMeshDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearMeshDynamicAnalysis")

    class _Cast_BevelGearMeshDynamicAnalysis:
        """Special nested class for casting BevelGearMeshDynamicAnalysis to subclasses."""

        def __init__(
            self: "BevelGearMeshDynamicAnalysis._Cast_BevelGearMeshDynamicAnalysis",
            parent: "BevelGearMeshDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_dynamic_analysis(
            self: "BevelGearMeshDynamicAnalysis._Cast_BevelGearMeshDynamicAnalysis",
        ):
            return self._parent._cast(_6279.AGMAGleasonConicalGearMeshDynamicAnalysis)

        @property
        def conical_gear_mesh_dynamic_analysis(
            self: "BevelGearMeshDynamicAnalysis._Cast_BevelGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6307

            return self._parent._cast(_6307.ConicalGearMeshDynamicAnalysis)

        @property
        def gear_mesh_dynamic_analysis(
            self: "BevelGearMeshDynamicAnalysis._Cast_BevelGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6335

            return self._parent._cast(_6335.GearMeshDynamicAnalysis)

        @property
        def inter_mountable_component_connection_dynamic_analysis(
            self: "BevelGearMeshDynamicAnalysis._Cast_BevelGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6341

            return self._parent._cast(
                _6341.InterMountableComponentConnectionDynamicAnalysis
            )

        @property
        def connection_dynamic_analysis(
            self: "BevelGearMeshDynamicAnalysis._Cast_BevelGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6309

            return self._parent._cast(_6309.ConnectionDynamicAnalysis)

        @property
        def connection_fe_analysis(
            self: "BevelGearMeshDynamicAnalysis._Cast_BevelGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "BevelGearMeshDynamicAnalysis._Cast_BevelGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelGearMeshDynamicAnalysis._Cast_BevelGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelGearMeshDynamicAnalysis._Cast_BevelGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearMeshDynamicAnalysis._Cast_BevelGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshDynamicAnalysis._Cast_BevelGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_dynamic_analysis(
            self: "BevelGearMeshDynamicAnalysis._Cast_BevelGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6286

            return self._parent._cast(_6286.BevelDifferentialGearMeshDynamicAnalysis)

        @property
        def spiral_bevel_gear_mesh_dynamic_analysis(
            self: "BevelGearMeshDynamicAnalysis._Cast_BevelGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6376

            return self._parent._cast(_6376.SpiralBevelGearMeshDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_dynamic_analysis(
            self: "BevelGearMeshDynamicAnalysis._Cast_BevelGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6382

            return self._parent._cast(_6382.StraightBevelDiffGearMeshDynamicAnalysis)

        @property
        def straight_bevel_gear_mesh_dynamic_analysis(
            self: "BevelGearMeshDynamicAnalysis._Cast_BevelGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6385

            return self._parent._cast(_6385.StraightBevelGearMeshDynamicAnalysis)

        @property
        def zerol_bevel_gear_mesh_dynamic_analysis(
            self: "BevelGearMeshDynamicAnalysis._Cast_BevelGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6403

            return self._parent._cast(_6403.ZerolBevelGearMeshDynamicAnalysis)

        @property
        def bevel_gear_mesh_dynamic_analysis(
            self: "BevelGearMeshDynamicAnalysis._Cast_BevelGearMeshDynamicAnalysis",
        ) -> "BevelGearMeshDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshDynamicAnalysis._Cast_BevelGearMeshDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearMeshDynamicAnalysis.TYPE"):
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
    ) -> "BevelGearMeshDynamicAnalysis._Cast_BevelGearMeshDynamicAnalysis":
        return self._Cast_BevelGearMeshDynamicAnalysis(self)
