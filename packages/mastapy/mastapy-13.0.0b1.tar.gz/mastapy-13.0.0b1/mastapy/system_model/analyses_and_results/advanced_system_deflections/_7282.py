"""BevelDifferentialGearMeshAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7287
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "BevelDifferentialGearMeshAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.bevel import _552
    from mastapy.system_model.connections_and_sockets.gears import _2299
    from mastapy.system_model.analyses_and_results.static_loads import _6821
    from mastapy.system_model.analyses_and_results.system_deflections import _2699


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearMeshAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="BevelDifferentialGearMeshAdvancedSystemDeflection")


class BevelDifferentialGearMeshAdvancedSystemDeflection(
    _7287.BevelGearMeshAdvancedSystemDeflection
):
    """BevelDifferentialGearMeshAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearMeshAdvancedSystemDeflection"
    )

    class _Cast_BevelDifferentialGearMeshAdvancedSystemDeflection:
        """Special nested class for casting BevelDifferentialGearMeshAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "BevelDifferentialGearMeshAdvancedSystemDeflection._Cast_BevelDifferentialGearMeshAdvancedSystemDeflection",
            parent: "BevelDifferentialGearMeshAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_advanced_system_deflection(
            self: "BevelDifferentialGearMeshAdvancedSystemDeflection._Cast_BevelDifferentialGearMeshAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7287.BevelGearMeshAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_mesh_advanced_system_deflection(
            self: "BevelDifferentialGearMeshAdvancedSystemDeflection._Cast_BevelDifferentialGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7275,
            )

            return self._parent._cast(
                _7275.AGMAGleasonConicalGearMeshAdvancedSystemDeflection
            )

        @property
        def conical_gear_mesh_advanced_system_deflection(
            self: "BevelDifferentialGearMeshAdvancedSystemDeflection._Cast_BevelDifferentialGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7303,
            )

            return self._parent._cast(_7303.ConicalGearMeshAdvancedSystemDeflection)

        @property
        def gear_mesh_advanced_system_deflection(
            self: "BevelDifferentialGearMeshAdvancedSystemDeflection._Cast_BevelDifferentialGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7331,
            )

            return self._parent._cast(_7331.GearMeshAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_advanced_system_deflection(
            self: "BevelDifferentialGearMeshAdvancedSystemDeflection._Cast_BevelDifferentialGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7337,
            )

            return self._parent._cast(
                _7337.InterMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def connection_advanced_system_deflection(
            self: "BevelDifferentialGearMeshAdvancedSystemDeflection._Cast_BevelDifferentialGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7305,
            )

            return self._parent._cast(_7305.ConnectionAdvancedSystemDeflection)

        @property
        def connection_static_load_analysis_case(
            self: "BevelDifferentialGearMeshAdvancedSystemDeflection._Cast_BevelDifferentialGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelDifferentialGearMeshAdvancedSystemDeflection._Cast_BevelDifferentialGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelDifferentialGearMeshAdvancedSystemDeflection._Cast_BevelDifferentialGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearMeshAdvancedSystemDeflection._Cast_BevelDifferentialGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearMeshAdvancedSystemDeflection._Cast_BevelDifferentialGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_advanced_system_deflection(
            self: "BevelDifferentialGearMeshAdvancedSystemDeflection._Cast_BevelDifferentialGearMeshAdvancedSystemDeflection",
        ) -> "BevelDifferentialGearMeshAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearMeshAdvancedSystemDeflection._Cast_BevelDifferentialGearMeshAdvancedSystemDeflection",
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
        instance_to_wrap: "BevelDifferentialGearMeshAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_detailed_analysis(self: Self) -> "_552.BevelGearMeshRating":
        """mastapy.gears.rating.bevel.BevelGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2299.BevelDifferentialGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6821.BevelDifferentialGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_system_deflection_results(
        self: Self,
    ) -> "List[_2699.BevelDifferentialGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialGearMeshSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialGearMeshAdvancedSystemDeflection._Cast_BevelDifferentialGearMeshAdvancedSystemDeflection":
        return self._Cast_BevelDifferentialGearMeshAdvancedSystemDeflection(self)
