"""StraightBevelDiffGearMeshModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4870,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MESH_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "StraightBevelDiffGearMeshModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2323
    from mastapy.system_model.analyses_and_results.static_loads import _6958


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearMeshModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="StraightBevelDiffGearMeshModalAnalysisAtAStiffness")


class StraightBevelDiffGearMeshModalAnalysisAtAStiffness(
    _4870.BevelGearMeshModalAnalysisAtAStiffness
):
    """StraightBevelDiffGearMeshModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MESH_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearMeshModalAnalysisAtAStiffness"
    )

    class _Cast_StraightBevelDiffGearMeshModalAnalysisAtAStiffness:
        """Special nested class for casting StraightBevelDiffGearMeshModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearMeshModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearMeshModalAnalysisAtAStiffness",
            parent: "StraightBevelDiffGearMeshModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearMeshModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearMeshModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(_4870.BevelGearMeshModalAnalysisAtAStiffness)

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearMeshModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4858,
            )

            return self._parent._cast(
                _4858.AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearMeshModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4886,
            )

            return self._parent._cast(_4886.ConicalGearMeshModalAnalysisAtAStiffness)

        @property
        def gear_mesh_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearMeshModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4913,
            )

            return self._parent._cast(_4913.GearMeshModalAnalysisAtAStiffness)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearMeshModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4920,
            )

            return self._parent._cast(
                _4920.InterMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def connection_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearMeshModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4889,
            )

            return self._parent._cast(_4889.ConnectionModalAnalysisAtAStiffness)

        @property
        def connection_static_load_analysis_case(
            self: "StraightBevelDiffGearMeshModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "StraightBevelDiffGearMeshModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "StraightBevelDiffGearMeshModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearMeshModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearMeshModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearMeshModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearMeshModalAnalysisAtAStiffness",
        ) -> "StraightBevelDiffGearMeshModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearMeshModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearMeshModalAnalysisAtAStiffness",
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
        instance_to_wrap: "StraightBevelDiffGearMeshModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2323.StraightBevelDiffGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6958.StraightBevelDiffGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearMeshModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearMeshModalAnalysisAtAStiffness":
        return self._Cast_StraightBevelDiffGearMeshModalAnalysisAtAStiffness(self)
