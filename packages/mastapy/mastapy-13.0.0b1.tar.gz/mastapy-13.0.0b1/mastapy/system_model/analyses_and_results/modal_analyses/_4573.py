"""AGMAGleasonConicalGearMeshModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4601
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "AGMAGleasonConicalGearMeshModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2297
    from mastapy.system_model.analyses_and_results.system_deflections import _2687


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshModalAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearMeshModalAnalysis")


class AGMAGleasonConicalGearMeshModalAnalysis(_4601.ConicalGearMeshModalAnalysis):
    """AGMAGleasonConicalGearMeshModalAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearMeshModalAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearMeshModalAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearMeshModalAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshModalAnalysis._Cast_AGMAGleasonConicalGearMeshModalAnalysis",
            parent: "AGMAGleasonConicalGearMeshModalAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_modal_analysis(
            self: "AGMAGleasonConicalGearMeshModalAnalysis._Cast_AGMAGleasonConicalGearMeshModalAnalysis",
        ):
            return self._parent._cast(_4601.ConicalGearMeshModalAnalysis)

        @property
        def gear_mesh_modal_analysis(
            self: "AGMAGleasonConicalGearMeshModalAnalysis._Cast_AGMAGleasonConicalGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4632

            return self._parent._cast(_4632.GearMeshModalAnalysis)

        @property
        def inter_mountable_component_connection_modal_analysis(
            self: "AGMAGleasonConicalGearMeshModalAnalysis._Cast_AGMAGleasonConicalGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4639

            return self._parent._cast(
                _4639.InterMountableComponentConnectionModalAnalysis
            )

        @property
        def connection_modal_analysis(
            self: "AGMAGleasonConicalGearMeshModalAnalysis._Cast_AGMAGleasonConicalGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4604

            return self._parent._cast(_4604.ConnectionModalAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "AGMAGleasonConicalGearMeshModalAnalysis._Cast_AGMAGleasonConicalGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "AGMAGleasonConicalGearMeshModalAnalysis._Cast_AGMAGleasonConicalGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AGMAGleasonConicalGearMeshModalAnalysis._Cast_AGMAGleasonConicalGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearMeshModalAnalysis._Cast_AGMAGleasonConicalGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshModalAnalysis._Cast_AGMAGleasonConicalGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_modal_analysis(
            self: "AGMAGleasonConicalGearMeshModalAnalysis._Cast_AGMAGleasonConicalGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4580

            return self._parent._cast(_4580.BevelDifferentialGearMeshModalAnalysis)

        @property
        def bevel_gear_mesh_modal_analysis(
            self: "AGMAGleasonConicalGearMeshModalAnalysis._Cast_AGMAGleasonConicalGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4585

            return self._parent._cast(_4585.BevelGearMeshModalAnalysis)

        @property
        def hypoid_gear_mesh_modal_analysis(
            self: "AGMAGleasonConicalGearMeshModalAnalysis._Cast_AGMAGleasonConicalGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4636

            return self._parent._cast(_4636.HypoidGearMeshModalAnalysis)

        @property
        def spiral_bevel_gear_mesh_modal_analysis(
            self: "AGMAGleasonConicalGearMeshModalAnalysis._Cast_AGMAGleasonConicalGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4680

            return self._parent._cast(_4680.SpiralBevelGearMeshModalAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis(
            self: "AGMAGleasonConicalGearMeshModalAnalysis._Cast_AGMAGleasonConicalGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4686

            return self._parent._cast(_4686.StraightBevelDiffGearMeshModalAnalysis)

        @property
        def straight_bevel_gear_mesh_modal_analysis(
            self: "AGMAGleasonConicalGearMeshModalAnalysis._Cast_AGMAGleasonConicalGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4689

            return self._parent._cast(_4689.StraightBevelGearMeshModalAnalysis)

        @property
        def zerol_bevel_gear_mesh_modal_analysis(
            self: "AGMAGleasonConicalGearMeshModalAnalysis._Cast_AGMAGleasonConicalGearMeshModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4710

            return self._parent._cast(_4710.ZerolBevelGearMeshModalAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis(
            self: "AGMAGleasonConicalGearMeshModalAnalysis._Cast_AGMAGleasonConicalGearMeshModalAnalysis",
        ) -> "AGMAGleasonConicalGearMeshModalAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshModalAnalysis._Cast_AGMAGleasonConicalGearMeshModalAnalysis",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearMeshModalAnalysis.TYPE"
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
    def system_deflection_results(
        self: Self,
    ) -> "_2687.AGMAGleasonConicalGearMeshSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearMeshSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearMeshModalAnalysis._Cast_AGMAGleasonConicalGearMeshModalAnalysis":
        return self._Cast_AGMAGleasonConicalGearMeshModalAnalysis(self)
