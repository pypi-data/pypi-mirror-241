"""BevelGearMeshModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5118
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "BevelGearMeshModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2301


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="BevelGearMeshModalAnalysisAtASpeed")


class BevelGearMeshModalAnalysisAtASpeed(
    _5118.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed
):
    """BevelGearMeshModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearMeshModalAnalysisAtASpeed")

    class _Cast_BevelGearMeshModalAnalysisAtASpeed:
        """Special nested class for casting BevelGearMeshModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
            parent: "BevelGearMeshModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis_at_a_speed(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ):
            return self._parent._cast(
                _5118.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed
            )

        @property
        def conical_gear_mesh_modal_analysis_at_a_speed(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5146,
            )

            return self._parent._cast(_5146.ConicalGearMeshModalAnalysisAtASpeed)

        @property
        def gear_mesh_modal_analysis_at_a_speed(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5172,
            )

            return self._parent._cast(_5172.GearMeshModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_speed(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5179,
            )

            return self._parent._cast(
                _5179.InterMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def connection_modal_analysis_at_a_speed(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5149,
            )

            return self._parent._cast(_5149.ConnectionModalAnalysisAtASpeed)

        @property
        def connection_static_load_analysis_case(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_modal_analysis_at_a_speed(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5125,
            )

            return self._parent._cast(
                _5125.BevelDifferentialGearMeshModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5214,
            )

            return self._parent._cast(_5214.SpiralBevelGearMeshModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis_at_a_speed(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5220,
            )

            return self._parent._cast(
                _5220.StraightBevelDiffGearMeshModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5223,
            )

            return self._parent._cast(_5223.StraightBevelGearMeshModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5241,
            )

            return self._parent._cast(_5241.ZerolBevelGearMeshModalAnalysisAtASpeed)

        @property
        def bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
        ) -> "BevelGearMeshModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "BevelGearMeshModalAnalysisAtASpeed.TYPE"
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
    ) -> "BevelGearMeshModalAnalysisAtASpeed._Cast_BevelGearMeshModalAnalysisAtASpeed":
        return self._Cast_BevelGearMeshModalAnalysisAtASpeed(self)
