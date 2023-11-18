"""StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7420,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2323
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7379,
    )


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection",)


Self = TypeVar(
    "Self", bound="StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection"
)


class StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection(
    _7420.BevelGearMeshCompoundAdvancedSystemDeflection
):
    """StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection",
    )

    class _Cast_StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection:
        """Special nested class for casting StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection._Cast_StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection",
            parent: "StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_advanced_system_deflection(
            self: "StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection._Cast_StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection",
        ):
            return self._parent._cast(
                _7420.BevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_advanced_system_deflection(
            self: "StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection._Cast_StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7408,
            )

            return self._parent._cast(
                _7408.AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_mesh_compound_advanced_system_deflection(
            self: "StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection._Cast_StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7436,
            )

            return self._parent._cast(
                _7436.ConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def gear_mesh_compound_advanced_system_deflection(
            self: "StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection._Cast_StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7462,
            )

            return self._parent._cast(_7462.GearMeshCompoundAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_advanced_system_deflection(
            self: "StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection._Cast_StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7468,
            )

            return self._parent._cast(
                _7468.InterMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def connection_compound_advanced_system_deflection(
            self: "StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection._Cast_StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7438,
            )

            return self._parent._cast(_7438.ConnectionCompoundAdvancedSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection._Cast_StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection._Cast_StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection._Cast_StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_advanced_system_deflection(
            self: "StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection._Cast_StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection",
        ) -> "StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection._Cast_StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2323.StraightBevelDiffGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_7379.StraightBevelDiffGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.StraightBevelDiffGearMeshAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_7379.StraightBevelDiffGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.StraightBevelDiffGearMeshAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection._Cast_StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection":
        return self._Cast_StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection(
            self
        )
