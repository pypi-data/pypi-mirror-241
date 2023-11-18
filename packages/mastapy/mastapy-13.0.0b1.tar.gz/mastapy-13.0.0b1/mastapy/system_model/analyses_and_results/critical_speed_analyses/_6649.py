"""StraightBevelDiffGearMeshCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6557
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MESH_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "StraightBevelDiffGearMeshCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2323
    from mastapy.system_model.analyses_and_results.static_loads import _6958


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearMeshCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="StraightBevelDiffGearMeshCriticalSpeedAnalysis")


class StraightBevelDiffGearMeshCriticalSpeedAnalysis(
    _6557.BevelGearMeshCriticalSpeedAnalysis
):
    """StraightBevelDiffGearMeshCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MESH_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearMeshCriticalSpeedAnalysis"
    )

    class _Cast_StraightBevelDiffGearMeshCriticalSpeedAnalysis:
        """Special nested class for casting StraightBevelDiffGearMeshCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearMeshCriticalSpeedAnalysis._Cast_StraightBevelDiffGearMeshCriticalSpeedAnalysis",
            parent: "StraightBevelDiffGearMeshCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_critical_speed_analysis(
            self: "StraightBevelDiffGearMeshCriticalSpeedAnalysis._Cast_StraightBevelDiffGearMeshCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6557.BevelGearMeshCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_critical_speed_analysis(
            self: "StraightBevelDiffGearMeshCriticalSpeedAnalysis._Cast_StraightBevelDiffGearMeshCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6545,
            )

            return self._parent._cast(
                _6545.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis
            )

        @property
        def conical_gear_mesh_critical_speed_analysis(
            self: "StraightBevelDiffGearMeshCriticalSpeedAnalysis._Cast_StraightBevelDiffGearMeshCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6573,
            )

            return self._parent._cast(_6573.ConicalGearMeshCriticalSpeedAnalysis)

        @property
        def gear_mesh_critical_speed_analysis(
            self: "StraightBevelDiffGearMeshCriticalSpeedAnalysis._Cast_StraightBevelDiffGearMeshCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6602,
            )

            return self._parent._cast(_6602.GearMeshCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_critical_speed_analysis(
            self: "StraightBevelDiffGearMeshCriticalSpeedAnalysis._Cast_StraightBevelDiffGearMeshCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6608,
            )

            return self._parent._cast(
                _6608.InterMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def connection_critical_speed_analysis(
            self: "StraightBevelDiffGearMeshCriticalSpeedAnalysis._Cast_StraightBevelDiffGearMeshCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6575,
            )

            return self._parent._cast(_6575.ConnectionCriticalSpeedAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "StraightBevelDiffGearMeshCriticalSpeedAnalysis._Cast_StraightBevelDiffGearMeshCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "StraightBevelDiffGearMeshCriticalSpeedAnalysis._Cast_StraightBevelDiffGearMeshCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "StraightBevelDiffGearMeshCriticalSpeedAnalysis._Cast_StraightBevelDiffGearMeshCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearMeshCriticalSpeedAnalysis._Cast_StraightBevelDiffGearMeshCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearMeshCriticalSpeedAnalysis._Cast_StraightBevelDiffGearMeshCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_critical_speed_analysis(
            self: "StraightBevelDiffGearMeshCriticalSpeedAnalysis._Cast_StraightBevelDiffGearMeshCriticalSpeedAnalysis",
        ) -> "StraightBevelDiffGearMeshCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearMeshCriticalSpeedAnalysis._Cast_StraightBevelDiffGearMeshCriticalSpeedAnalysis",
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
        instance_to_wrap: "StraightBevelDiffGearMeshCriticalSpeedAnalysis.TYPE",
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
    ) -> "StraightBevelDiffGearMeshCriticalSpeedAnalysis._Cast_StraightBevelDiffGearMeshCriticalSpeedAnalysis":
        return self._Cast_StraightBevelDiffGearMeshCriticalSpeedAnalysis(self)
