"""AGMAGleasonConicalGearMeshStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3793
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "AGMAGleasonConicalGearMeshStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2297


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshStabilityAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearMeshStabilityAnalysis")


class AGMAGleasonConicalGearMeshStabilityAnalysis(
    _3793.ConicalGearMeshStabilityAnalysis
):
    """AGMAGleasonConicalGearMeshStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearMeshStabilityAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearMeshStabilityAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearMeshStabilityAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis",
            parent: "AGMAGleasonConicalGearMeshStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_stability_analysis(
            self: "AGMAGleasonConicalGearMeshStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis",
        ):
            return self._parent._cast(_3793.ConicalGearMeshStabilityAnalysis)

        @property
        def gear_mesh_stability_analysis(
            self: "AGMAGleasonConicalGearMeshStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3821,
            )

            return self._parent._cast(_3821.GearMeshStabilityAnalysis)

        @property
        def inter_mountable_component_connection_stability_analysis(
            self: "AGMAGleasonConicalGearMeshStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3828,
            )

            return self._parent._cast(
                _3828.InterMountableComponentConnectionStabilityAnalysis
            )

        @property
        def connection_stability_analysis(
            self: "AGMAGleasonConicalGearMeshStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3796,
            )

            return self._parent._cast(_3796.ConnectionStabilityAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "AGMAGleasonConicalGearMeshStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "AGMAGleasonConicalGearMeshStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AGMAGleasonConicalGearMeshStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearMeshStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_stability_analysis(
            self: "AGMAGleasonConicalGearMeshStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3772,
            )

            return self._parent._cast(_3772.BevelDifferentialGearMeshStabilityAnalysis)

        @property
        def bevel_gear_mesh_stability_analysis(
            self: "AGMAGleasonConicalGearMeshStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3777,
            )

            return self._parent._cast(_3777.BevelGearMeshStabilityAnalysis)

        @property
        def hypoid_gear_mesh_stability_analysis(
            self: "AGMAGleasonConicalGearMeshStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3825,
            )

            return self._parent._cast(_3825.HypoidGearMeshStabilityAnalysis)

        @property
        def spiral_bevel_gear_mesh_stability_analysis(
            self: "AGMAGleasonConicalGearMeshStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3862,
            )

            return self._parent._cast(_3862.SpiralBevelGearMeshStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_stability_analysis(
            self: "AGMAGleasonConicalGearMeshStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3871,
            )

            return self._parent._cast(_3871.StraightBevelDiffGearMeshStabilityAnalysis)

        @property
        def straight_bevel_gear_mesh_stability_analysis(
            self: "AGMAGleasonConicalGearMeshStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3874,
            )

            return self._parent._cast(_3874.StraightBevelGearMeshStabilityAnalysis)

        @property
        def zerol_bevel_gear_mesh_stability_analysis(
            self: "AGMAGleasonConicalGearMeshStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3892,
            )

            return self._parent._cast(_3892.ZerolBevelGearMeshStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_stability_analysis(
            self: "AGMAGleasonConicalGearMeshStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis",
        ) -> "AGMAGleasonConicalGearMeshStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearMeshStabilityAnalysis.TYPE"
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
    ) -> "AGMAGleasonConicalGearMeshStabilityAnalysis._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis":
        return self._Cast_AGMAGleasonConicalGearMeshStabilityAnalysis(self)
