"""SpiralBevelGearMeshStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3777
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "SpiralBevelGearMeshStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2321
    from mastapy.system_model.analyses_and_results.static_loads import _6952


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearMeshStabilityAnalysis",)


Self = TypeVar("Self", bound="SpiralBevelGearMeshStabilityAnalysis")


class SpiralBevelGearMeshStabilityAnalysis(_3777.BevelGearMeshStabilityAnalysis):
    """SpiralBevelGearMeshStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MESH_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpiralBevelGearMeshStabilityAnalysis")

    class _Cast_SpiralBevelGearMeshStabilityAnalysis:
        """Special nested class for casting SpiralBevelGearMeshStabilityAnalysis to subclasses."""

        def __init__(
            self: "SpiralBevelGearMeshStabilityAnalysis._Cast_SpiralBevelGearMeshStabilityAnalysis",
            parent: "SpiralBevelGearMeshStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_stability_analysis(
            self: "SpiralBevelGearMeshStabilityAnalysis._Cast_SpiralBevelGearMeshStabilityAnalysis",
        ):
            return self._parent._cast(_3777.BevelGearMeshStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_stability_analysis(
            self: "SpiralBevelGearMeshStabilityAnalysis._Cast_SpiralBevelGearMeshStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3765,
            )

            return self._parent._cast(_3765.AGMAGleasonConicalGearMeshStabilityAnalysis)

        @property
        def conical_gear_mesh_stability_analysis(
            self: "SpiralBevelGearMeshStabilityAnalysis._Cast_SpiralBevelGearMeshStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3793,
            )

            return self._parent._cast(_3793.ConicalGearMeshStabilityAnalysis)

        @property
        def gear_mesh_stability_analysis(
            self: "SpiralBevelGearMeshStabilityAnalysis._Cast_SpiralBevelGearMeshStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3821,
            )

            return self._parent._cast(_3821.GearMeshStabilityAnalysis)

        @property
        def inter_mountable_component_connection_stability_analysis(
            self: "SpiralBevelGearMeshStabilityAnalysis._Cast_SpiralBevelGearMeshStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3828,
            )

            return self._parent._cast(
                _3828.InterMountableComponentConnectionStabilityAnalysis
            )

        @property
        def connection_stability_analysis(
            self: "SpiralBevelGearMeshStabilityAnalysis._Cast_SpiralBevelGearMeshStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3796,
            )

            return self._parent._cast(_3796.ConnectionStabilityAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "SpiralBevelGearMeshStabilityAnalysis._Cast_SpiralBevelGearMeshStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "SpiralBevelGearMeshStabilityAnalysis._Cast_SpiralBevelGearMeshStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "SpiralBevelGearMeshStabilityAnalysis._Cast_SpiralBevelGearMeshStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearMeshStabilityAnalysis._Cast_SpiralBevelGearMeshStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearMeshStabilityAnalysis._Cast_SpiralBevelGearMeshStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_mesh_stability_analysis(
            self: "SpiralBevelGearMeshStabilityAnalysis._Cast_SpiralBevelGearMeshStabilityAnalysis",
        ) -> "SpiralBevelGearMeshStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearMeshStabilityAnalysis._Cast_SpiralBevelGearMeshStabilityAnalysis",
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
        self: Self, instance_to_wrap: "SpiralBevelGearMeshStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2321.SpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6952.SpiralBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase

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
    ) -> "SpiralBevelGearMeshStabilityAnalysis._Cast_SpiralBevelGearMeshStabilityAnalysis":
        return self._Cast_SpiralBevelGearMeshStabilityAnalysis(self)
