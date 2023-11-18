"""CouplingCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7501,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "CouplingCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7308,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CouplingCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="CouplingCompoundAdvancedSystemDeflection")


class CouplingCompoundAdvancedSystemDeflection(
    _7501.SpecialisedAssemblyCompoundAdvancedSystemDeflection
):
    """CouplingCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COUPLING_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingCompoundAdvancedSystemDeflection"
    )

    class _Cast_CouplingCompoundAdvancedSystemDeflection:
        """Special nested class for casting CouplingCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "CouplingCompoundAdvancedSystemDeflection._Cast_CouplingCompoundAdvancedSystemDeflection",
            parent: "CouplingCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_advanced_system_deflection(
            self: "CouplingCompoundAdvancedSystemDeflection._Cast_CouplingCompoundAdvancedSystemDeflection",
        ):
            return self._parent._cast(
                _7501.SpecialisedAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_assembly_compound_advanced_system_deflection(
            self: "CouplingCompoundAdvancedSystemDeflection._Cast_CouplingCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7403,
            )

            return self._parent._cast(
                _7403.AbstractAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def part_compound_advanced_system_deflection(
            self: "CouplingCompoundAdvancedSystemDeflection._Cast_CouplingCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7482,
            )

            return self._parent._cast(_7482.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "CouplingCompoundAdvancedSystemDeflection._Cast_CouplingCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingCompoundAdvancedSystemDeflection._Cast_CouplingCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingCompoundAdvancedSystemDeflection._Cast_CouplingCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def clutch_compound_advanced_system_deflection(
            self: "CouplingCompoundAdvancedSystemDeflection._Cast_CouplingCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7424,
            )

            return self._parent._cast(_7424.ClutchCompoundAdvancedSystemDeflection)

        @property
        def concept_coupling_compound_advanced_system_deflection(
            self: "CouplingCompoundAdvancedSystemDeflection._Cast_CouplingCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7429,
            )

            return self._parent._cast(
                _7429.ConceptCouplingCompoundAdvancedSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_compound_advanced_system_deflection(
            self: "CouplingCompoundAdvancedSystemDeflection._Cast_CouplingCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7483,
            )

            return self._parent._cast(
                _7483.PartToPartShearCouplingCompoundAdvancedSystemDeflection
            )

        @property
        def spring_damper_compound_advanced_system_deflection(
            self: "CouplingCompoundAdvancedSystemDeflection._Cast_CouplingCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7505,
            )

            return self._parent._cast(
                _7505.SpringDamperCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_compound_advanced_system_deflection(
            self: "CouplingCompoundAdvancedSystemDeflection._Cast_CouplingCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7520,
            )

            return self._parent._cast(
                _7520.TorqueConverterCompoundAdvancedSystemDeflection
            )

        @property
        def coupling_compound_advanced_system_deflection(
            self: "CouplingCompoundAdvancedSystemDeflection._Cast_CouplingCompoundAdvancedSystemDeflection",
        ) -> "CouplingCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CouplingCompoundAdvancedSystemDeflection._Cast_CouplingCompoundAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "CouplingCompoundAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_7308.CouplingAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CouplingAdvancedSystemDeflection]

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
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_7308.CouplingAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CouplingAdvancedSystemDeflection]

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
    def cast_to(
        self: Self,
    ) -> "CouplingCompoundAdvancedSystemDeflection._Cast_CouplingCompoundAdvancedSystemDeflection":
        return self._Cast_CouplingCompoundAdvancedSystemDeflection(self)
