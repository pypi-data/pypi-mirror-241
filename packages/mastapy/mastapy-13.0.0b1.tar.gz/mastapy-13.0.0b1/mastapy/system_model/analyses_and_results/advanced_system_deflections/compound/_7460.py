"""FlexiblePinAssemblyCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7501,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "FlexiblePinAssemblyCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2452
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7329,
    )


__docformat__ = "restructuredtext en"
__all__ = ("FlexiblePinAssemblyCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="FlexiblePinAssemblyCompoundAdvancedSystemDeflection")


class FlexiblePinAssemblyCompoundAdvancedSystemDeflection(
    _7501.SpecialisedAssemblyCompoundAdvancedSystemDeflection
):
    """FlexiblePinAssemblyCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ASSEMBLY_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FlexiblePinAssemblyCompoundAdvancedSystemDeflection"
    )

    class _Cast_FlexiblePinAssemblyCompoundAdvancedSystemDeflection:
        """Special nested class for casting FlexiblePinAssemblyCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "FlexiblePinAssemblyCompoundAdvancedSystemDeflection._Cast_FlexiblePinAssemblyCompoundAdvancedSystemDeflection",
            parent: "FlexiblePinAssemblyCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_advanced_system_deflection(
            self: "FlexiblePinAssemblyCompoundAdvancedSystemDeflection._Cast_FlexiblePinAssemblyCompoundAdvancedSystemDeflection",
        ):
            return self._parent._cast(
                _7501.SpecialisedAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_assembly_compound_advanced_system_deflection(
            self: "FlexiblePinAssemblyCompoundAdvancedSystemDeflection._Cast_FlexiblePinAssemblyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7403,
            )

            return self._parent._cast(
                _7403.AbstractAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def part_compound_advanced_system_deflection(
            self: "FlexiblePinAssemblyCompoundAdvancedSystemDeflection._Cast_FlexiblePinAssemblyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7482,
            )

            return self._parent._cast(_7482.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "FlexiblePinAssemblyCompoundAdvancedSystemDeflection._Cast_FlexiblePinAssemblyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "FlexiblePinAssemblyCompoundAdvancedSystemDeflection._Cast_FlexiblePinAssemblyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "FlexiblePinAssemblyCompoundAdvancedSystemDeflection._Cast_FlexiblePinAssemblyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def flexible_pin_assembly_compound_advanced_system_deflection(
            self: "FlexiblePinAssemblyCompoundAdvancedSystemDeflection._Cast_FlexiblePinAssemblyCompoundAdvancedSystemDeflection",
        ) -> "FlexiblePinAssemblyCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "FlexiblePinAssemblyCompoundAdvancedSystemDeflection._Cast_FlexiblePinAssemblyCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "FlexiblePinAssemblyCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2452.FlexiblePinAssembly":
        """mastapy.system_model.part_model.FlexiblePinAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2452.FlexiblePinAssembly":
        """mastapy.system_model.part_model.FlexiblePinAssembly

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
    ) -> "List[_7329.FlexiblePinAssemblyAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.FlexiblePinAssemblyAdvancedSystemDeflection]

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
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_7329.FlexiblePinAssemblyAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.FlexiblePinAssemblyAdvancedSystemDeflection]

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
    ) -> "FlexiblePinAssemblyCompoundAdvancedSystemDeflection._Cast_FlexiblePinAssemblyCompoundAdvancedSystemDeflection":
        return self._Cast_FlexiblePinAssemblyCompoundAdvancedSystemDeflection(self)
