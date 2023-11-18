"""ClutchCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2886
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "ClutchCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2576
    from mastapy.system_model.analyses_and_results.system_deflections import _2711


__docformat__ = "restructuredtext en"
__all__ = ("ClutchCompoundSystemDeflection",)


Self = TypeVar("Self", bound="ClutchCompoundSystemDeflection")


class ClutchCompoundSystemDeflection(_2886.CouplingCompoundSystemDeflection):
    """ClutchCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CLUTCH_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClutchCompoundSystemDeflection")

    class _Cast_ClutchCompoundSystemDeflection:
        """Special nested class for casting ClutchCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "ClutchCompoundSystemDeflection._Cast_ClutchCompoundSystemDeflection",
            parent: "ClutchCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_compound_system_deflection(
            self: "ClutchCompoundSystemDeflection._Cast_ClutchCompoundSystemDeflection",
        ):
            return self._parent._cast(_2886.CouplingCompoundSystemDeflection)

        @property
        def specialised_assembly_compound_system_deflection(
            self: "ClutchCompoundSystemDeflection._Cast_ClutchCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2949,
            )

            return self._parent._cast(_2949.SpecialisedAssemblyCompoundSystemDeflection)

        @property
        def abstract_assembly_compound_system_deflection(
            self: "ClutchCompoundSystemDeflection._Cast_ClutchCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2849,
            )

            return self._parent._cast(_2849.AbstractAssemblyCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "ClutchCompoundSystemDeflection._Cast_ClutchCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2929,
            )

            return self._parent._cast(_2929.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "ClutchCompoundSystemDeflection._Cast_ClutchCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ClutchCompoundSystemDeflection._Cast_ClutchCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchCompoundSystemDeflection._Cast_ClutchCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def clutch_compound_system_deflection(
            self: "ClutchCompoundSystemDeflection._Cast_ClutchCompoundSystemDeflection",
        ) -> "ClutchCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ClutchCompoundSystemDeflection._Cast_ClutchCompoundSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ClutchCompoundSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2576.Clutch":
        """mastapy.system_model.part_model.couplings.Clutch

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2576.Clutch":
        """mastapy.system_model.part_model.couplings.Clutch

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
    ) -> "List[_2711.ClutchSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ClutchSystemDeflection]

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
    def assembly_analysis_cases(self: Self) -> "List[_2711.ClutchSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ClutchSystemDeflection]

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
    ) -> "ClutchCompoundSystemDeflection._Cast_ClutchCompoundSystemDeflection":
        return self._Cast_ClutchCompoundSystemDeflection(self)
