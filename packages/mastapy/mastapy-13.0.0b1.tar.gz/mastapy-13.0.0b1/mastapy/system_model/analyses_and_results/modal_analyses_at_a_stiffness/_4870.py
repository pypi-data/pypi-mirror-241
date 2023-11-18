"""BevelGearMeshModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4858,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "BevelGearMeshModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2301


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="BevelGearMeshModalAnalysisAtAStiffness")


class BevelGearMeshModalAnalysisAtAStiffness(
    _4858.AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness
):
    """BevelGearMeshModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearMeshModalAnalysisAtAStiffness"
    )

    class _Cast_BevelGearMeshModalAnalysisAtAStiffness:
        """Special nested class for casting BevelGearMeshModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
            parent: "BevelGearMeshModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(
                _4858.AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4886,
            )

            return self._parent._cast(_4886.ConicalGearMeshModalAnalysisAtAStiffness)

        @property
        def gear_mesh_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4913,
            )

            return self._parent._cast(_4913.GearMeshModalAnalysisAtAStiffness)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4920,
            )

            return self._parent._cast(
                _4920.InterMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def connection_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4889,
            )

            return self._parent._cast(_4889.ConnectionModalAnalysisAtAStiffness)

        @property
        def connection_static_load_analysis_case(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4865,
            )

            return self._parent._cast(
                _4865.BevelDifferentialGearMeshModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4955,
            )

            return self._parent._cast(
                _4955.SpiralBevelGearMeshModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4961,
            )

            return self._parent._cast(
                _4961.StraightBevelDiffGearMeshModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4964,
            )

            return self._parent._cast(
                _4964.StraightBevelGearMeshModalAnalysisAtAStiffness
            )

        @property
        def zerol_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4982,
            )

            return self._parent._cast(_4982.ZerolBevelGearMeshModalAnalysisAtAStiffness)

        @property
        def bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
        ) -> "BevelGearMeshModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "BevelGearMeshModalAnalysisAtAStiffness.TYPE"
    ):
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
    ) -> "BevelGearMeshModalAnalysisAtAStiffness._Cast_BevelGearMeshModalAnalysisAtAStiffness":
        return self._Cast_BevelGearMeshModalAnalysisAtAStiffness(self)
