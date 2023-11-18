"""SpiralBevelGearMeshSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2704
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "SpiralBevelGearMeshSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.spiral_bevel import _400
    from mastapy.system_model.connections_and_sockets.gears import _2321
    from mastapy.system_model.analyses_and_results.static_loads import _6952
    from mastapy.system_model.analyses_and_results.power_flows import _4133


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearMeshSystemDeflection",)


Self = TypeVar("Self", bound="SpiralBevelGearMeshSystemDeflection")


class SpiralBevelGearMeshSystemDeflection(_2704.BevelGearMeshSystemDeflection):
    """SpiralBevelGearMeshSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MESH_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpiralBevelGearMeshSystemDeflection")

    class _Cast_SpiralBevelGearMeshSystemDeflection:
        """Special nested class for casting SpiralBevelGearMeshSystemDeflection to subclasses."""

        def __init__(
            self: "SpiralBevelGearMeshSystemDeflection._Cast_SpiralBevelGearMeshSystemDeflection",
            parent: "SpiralBevelGearMeshSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_system_deflection(
            self: "SpiralBevelGearMeshSystemDeflection._Cast_SpiralBevelGearMeshSystemDeflection",
        ):
            return self._parent._cast(_2704.BevelGearMeshSystemDeflection)

        @property
        def agma_gleason_conical_gear_mesh_system_deflection(
            self: "SpiralBevelGearMeshSystemDeflection._Cast_SpiralBevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2687,
            )

            return self._parent._cast(_2687.AGMAGleasonConicalGearMeshSystemDeflection)

        @property
        def conical_gear_mesh_system_deflection(
            self: "SpiralBevelGearMeshSystemDeflection._Cast_SpiralBevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2722,
            )

            return self._parent._cast(_2722.ConicalGearMeshSystemDeflection)

        @property
        def gear_mesh_system_deflection(
            self: "SpiralBevelGearMeshSystemDeflection._Cast_SpiralBevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2757,
            )

            return self._parent._cast(_2757.GearMeshSystemDeflection)

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "SpiralBevelGearMeshSystemDeflection._Cast_SpiralBevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2765,
            )

            return self._parent._cast(
                _2765.InterMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "SpiralBevelGearMeshSystemDeflection._Cast_SpiralBevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2725,
            )

            return self._parent._cast(_2725.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "SpiralBevelGearMeshSystemDeflection._Cast_SpiralBevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "SpiralBevelGearMeshSystemDeflection._Cast_SpiralBevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "SpiralBevelGearMeshSystemDeflection._Cast_SpiralBevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "SpiralBevelGearMeshSystemDeflection._Cast_SpiralBevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearMeshSystemDeflection._Cast_SpiralBevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearMeshSystemDeflection._Cast_SpiralBevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_mesh_system_deflection(
            self: "SpiralBevelGearMeshSystemDeflection._Cast_SpiralBevelGearMeshSystemDeflection",
        ) -> "SpiralBevelGearMeshSystemDeflection":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearMeshSystemDeflection._Cast_SpiralBevelGearMeshSystemDeflection",
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
        self: Self, instance_to_wrap: "SpiralBevelGearMeshSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self: Self) -> "_400.SpiralBevelGearMeshRating":
        """mastapy.gears.rating.spiral_bevel.SpiralBevelGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_400.SpiralBevelGearMeshRating":
        """mastapy.gears.rating.spiral_bevel.SpiralBevelGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def power_flow_results(self: Self) -> "_4133.SpiralBevelGearMeshPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.SpiralBevelGearMeshPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> (
        "SpiralBevelGearMeshSystemDeflection._Cast_SpiralBevelGearMeshSystemDeflection"
    ):
        return self._Cast_SpiralBevelGearMeshSystemDeflection(self)
