"""ZerolBevelGearMeshPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4046
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MESH_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "ZerolBevelGearMeshPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.zerol_bevel import _367
    from mastapy.system_model.connections_and_sockets.gears import _2329
    from mastapy.system_model.analyses_and_results.static_loads import _6984


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearMeshPowerFlow",)


Self = TypeVar("Self", bound="ZerolBevelGearMeshPowerFlow")


class ZerolBevelGearMeshPowerFlow(_4046.BevelGearMeshPowerFlow):
    """ZerolBevelGearMeshPowerFlow

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_MESH_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ZerolBevelGearMeshPowerFlow")

    class _Cast_ZerolBevelGearMeshPowerFlow:
        """Special nested class for casting ZerolBevelGearMeshPowerFlow to subclasses."""

        def __init__(
            self: "ZerolBevelGearMeshPowerFlow._Cast_ZerolBevelGearMeshPowerFlow",
            parent: "ZerolBevelGearMeshPowerFlow",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_power_flow(
            self: "ZerolBevelGearMeshPowerFlow._Cast_ZerolBevelGearMeshPowerFlow",
        ):
            return self._parent._cast(_4046.BevelGearMeshPowerFlow)

        @property
        def agma_gleason_conical_gear_mesh_power_flow(
            self: "ZerolBevelGearMeshPowerFlow._Cast_ZerolBevelGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4034

            return self._parent._cast(_4034.AGMAGleasonConicalGearMeshPowerFlow)

        @property
        def conical_gear_mesh_power_flow(
            self: "ZerolBevelGearMeshPowerFlow._Cast_ZerolBevelGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4062

            return self._parent._cast(_4062.ConicalGearMeshPowerFlow)

        @property
        def gear_mesh_power_flow(
            self: "ZerolBevelGearMeshPowerFlow._Cast_ZerolBevelGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4090

            return self._parent._cast(_4090.GearMeshPowerFlow)

        @property
        def inter_mountable_component_connection_power_flow(
            self: "ZerolBevelGearMeshPowerFlow._Cast_ZerolBevelGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4097

            return self._parent._cast(_4097.InterMountableComponentConnectionPowerFlow)

        @property
        def connection_power_flow(
            self: "ZerolBevelGearMeshPowerFlow._Cast_ZerolBevelGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4065

            return self._parent._cast(_4065.ConnectionPowerFlow)

        @property
        def connection_static_load_analysis_case(
            self: "ZerolBevelGearMeshPowerFlow._Cast_ZerolBevelGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ZerolBevelGearMeshPowerFlow._Cast_ZerolBevelGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ZerolBevelGearMeshPowerFlow._Cast_ZerolBevelGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ZerolBevelGearMeshPowerFlow._Cast_ZerolBevelGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearMeshPowerFlow._Cast_ZerolBevelGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_mesh_power_flow(
            self: "ZerolBevelGearMeshPowerFlow._Cast_ZerolBevelGearMeshPowerFlow",
        ) -> "ZerolBevelGearMeshPowerFlow":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearMeshPowerFlow._Cast_ZerolBevelGearMeshPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ZerolBevelGearMeshPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self: Self) -> "_367.ZerolBevelGearMeshRating":
        """mastapy.gears.rating.zerol_bevel.ZerolBevelGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_367.ZerolBevelGearMeshRating":
        """mastapy.gears.rating.zerol_bevel.ZerolBevelGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2329.ZerolBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6984.ZerolBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearMeshLoadCase

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
    ) -> "ZerolBevelGearMeshPowerFlow._Cast_ZerolBevelGearMeshPowerFlow":
        return self._Cast_ZerolBevelGearMeshPowerFlow(self)
