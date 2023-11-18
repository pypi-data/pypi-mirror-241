"""HypoidGearSetCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7409,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "HypoidGearSetCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2533
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7336,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7465,
        _7466,
    )


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearSetCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="HypoidGearSetCompoundAdvancedSystemDeflection")


class HypoidGearSetCompoundAdvancedSystemDeflection(
    _7409.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection
):
    """HypoidGearSetCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_HypoidGearSetCompoundAdvancedSystemDeflection"
    )

    class _Cast_HypoidGearSetCompoundAdvancedSystemDeflection:
        """Special nested class for casting HypoidGearSetCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "HypoidGearSetCompoundAdvancedSystemDeflection._Cast_HypoidGearSetCompoundAdvancedSystemDeflection",
            parent: "HypoidGearSetCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_compound_advanced_system_deflection(
            self: "HypoidGearSetCompoundAdvancedSystemDeflection._Cast_HypoidGearSetCompoundAdvancedSystemDeflection",
        ):
            return self._parent._cast(
                _7409.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_set_compound_advanced_system_deflection(
            self: "HypoidGearSetCompoundAdvancedSystemDeflection._Cast_HypoidGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7437,
            )

            return self._parent._cast(
                _7437.ConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def gear_set_compound_advanced_system_deflection(
            self: "HypoidGearSetCompoundAdvancedSystemDeflection._Cast_HypoidGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7463,
            )

            return self._parent._cast(_7463.GearSetCompoundAdvancedSystemDeflection)

        @property
        def specialised_assembly_compound_advanced_system_deflection(
            self: "HypoidGearSetCompoundAdvancedSystemDeflection._Cast_HypoidGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7501,
            )

            return self._parent._cast(
                _7501.SpecialisedAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_assembly_compound_advanced_system_deflection(
            self: "HypoidGearSetCompoundAdvancedSystemDeflection._Cast_HypoidGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7403,
            )

            return self._parent._cast(
                _7403.AbstractAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def part_compound_advanced_system_deflection(
            self: "HypoidGearSetCompoundAdvancedSystemDeflection._Cast_HypoidGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7482,
            )

            return self._parent._cast(_7482.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "HypoidGearSetCompoundAdvancedSystemDeflection._Cast_HypoidGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "HypoidGearSetCompoundAdvancedSystemDeflection._Cast_HypoidGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearSetCompoundAdvancedSystemDeflection._Cast_HypoidGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def hypoid_gear_set_compound_advanced_system_deflection(
            self: "HypoidGearSetCompoundAdvancedSystemDeflection._Cast_HypoidGearSetCompoundAdvancedSystemDeflection",
        ) -> "HypoidGearSetCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "HypoidGearSetCompoundAdvancedSystemDeflection._Cast_HypoidGearSetCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "HypoidGearSetCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2533.HypoidGearSet":
        """mastapy.system_model.part_model.gears.HypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2533.HypoidGearSet":
        """mastapy.system_model.part_model.gears.HypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_7336.HypoidGearSetAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.HypoidGearSetAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_gears_compound_advanced_system_deflection(
        self: Self,
    ) -> "List[_7465.HypoidGearCompoundAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.HypoidGearCompoundAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearsCompoundAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_meshes_compound_advanced_system_deflection(
        self: Self,
    ) -> "List[_7466.HypoidGearMeshCompoundAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.HypoidGearMeshCompoundAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidMeshesCompoundAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_7336.HypoidGearSetAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.HypoidGearSetAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "HypoidGearSetCompoundAdvancedSystemDeflection._Cast_HypoidGearSetCompoundAdvancedSystemDeflection":
        return self._Cast_HypoidGearSetCompoundAdvancedSystemDeflection(self)
