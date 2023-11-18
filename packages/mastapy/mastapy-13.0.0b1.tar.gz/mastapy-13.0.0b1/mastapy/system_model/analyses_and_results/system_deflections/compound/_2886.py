"""CouplingCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2949
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "CouplingCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2729


__docformat__ = "restructuredtext en"
__all__ = ("CouplingCompoundSystemDeflection",)


Self = TypeVar("Self", bound="CouplingCompoundSystemDeflection")


class CouplingCompoundSystemDeflection(
    _2949.SpecialisedAssemblyCompoundSystemDeflection
):
    """CouplingCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COUPLING_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingCompoundSystemDeflection")

    class _Cast_CouplingCompoundSystemDeflection:
        """Special nested class for casting CouplingCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "CouplingCompoundSystemDeflection._Cast_CouplingCompoundSystemDeflection",
            parent: "CouplingCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_system_deflection(
            self: "CouplingCompoundSystemDeflection._Cast_CouplingCompoundSystemDeflection",
        ):
            return self._parent._cast(_2949.SpecialisedAssemblyCompoundSystemDeflection)

        @property
        def abstract_assembly_compound_system_deflection(
            self: "CouplingCompoundSystemDeflection._Cast_CouplingCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2849,
            )

            return self._parent._cast(_2849.AbstractAssemblyCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "CouplingCompoundSystemDeflection._Cast_CouplingCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2929,
            )

            return self._parent._cast(_2929.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "CouplingCompoundSystemDeflection._Cast_CouplingCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingCompoundSystemDeflection._Cast_CouplingCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingCompoundSystemDeflection._Cast_CouplingCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def clutch_compound_system_deflection(
            self: "CouplingCompoundSystemDeflection._Cast_CouplingCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2870,
            )

            return self._parent._cast(_2870.ClutchCompoundSystemDeflection)

        @property
        def concept_coupling_compound_system_deflection(
            self: "CouplingCompoundSystemDeflection._Cast_CouplingCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2875,
            )

            return self._parent._cast(_2875.ConceptCouplingCompoundSystemDeflection)

        @property
        def part_to_part_shear_coupling_compound_system_deflection(
            self: "CouplingCompoundSystemDeflection._Cast_CouplingCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2930,
            )

            return self._parent._cast(
                _2930.PartToPartShearCouplingCompoundSystemDeflection
            )

        @property
        def spring_damper_compound_system_deflection(
            self: "CouplingCompoundSystemDeflection._Cast_CouplingCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2953,
            )

            return self._parent._cast(_2953.SpringDamperCompoundSystemDeflection)

        @property
        def torque_converter_compound_system_deflection(
            self: "CouplingCompoundSystemDeflection._Cast_CouplingCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2968,
            )

            return self._parent._cast(_2968.TorqueConverterCompoundSystemDeflection)

        @property
        def coupling_compound_system_deflection(
            self: "CouplingCompoundSystemDeflection._Cast_CouplingCompoundSystemDeflection",
        ) -> "CouplingCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CouplingCompoundSystemDeflection._Cast_CouplingCompoundSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingCompoundSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self: Self) -> "List[_2729.CouplingSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CouplingSystemDeflection]

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
    ) -> "List[_2729.CouplingSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CouplingSystemDeflection]

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
    ) -> "CouplingCompoundSystemDeflection._Cast_CouplingCompoundSystemDeflection":
        return self._Cast_CouplingCompoundSystemDeflection(self)
