"""KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2766
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_SYSTEM_DEFLECTION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
        "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",
    )
)

if TYPE_CHECKING:
    from mastapy.gears.rating.klingelnberg_spiral_bevel import _403
    from mastapy.system_model.connections_and_sockets.gears import _2318
    from mastapy.system_model.analyses_and_results.static_loads import _6917
    from mastapy.system_model.analyses_and_results.power_flows import _4104


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection"
)


class KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection(
    _2766.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection
):
    """KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",
        ):
            return self._parent._cast(
                _2766.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection
            )

        @property
        def conical_gear_mesh_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2722,
            )

            return self._parent._cast(_2722.ConicalGearMeshSystemDeflection)

        @property
        def gear_mesh_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2757,
            )

            return self._parent._cast(_2757.GearMeshSystemDeflection)

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2765,
            )

            return self._parent._cast(
                _2765.InterMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2725,
            )

            return self._parent._cast(_2725.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self: Self) -> "_403.KlingelnbergCycloPalloidSpiralBevelGearMeshRating":
        """mastapy.gears.rating.klingelnberg_spiral_bevel.KlingelnbergCycloPalloidSpiralBevelGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(
        self: Self,
    ) -> "_403.KlingelnbergCycloPalloidSpiralBevelGearMeshRating":
        """mastapy.gears.rating.klingelnberg_spiral_bevel.KlingelnbergCycloPalloidSpiralBevelGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(
        self: Self,
    ) -> "_2318.KlingelnbergCycloPalloidSpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(
        self: Self,
    ) -> "_6917.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(
        self: Self,
    ) -> "_4104.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow

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
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection(
            self
        )
