"""ConceptCouplingAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7308
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "ConceptCouplingAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2579
    from mastapy.system_model.analyses_and_results.static_loads import _6838
    from mastapy.system_model.analyses_and_results.system_deflections import _2717


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="ConceptCouplingAdvancedSystemDeflection")


class ConceptCouplingAdvancedSystemDeflection(_7308.CouplingAdvancedSystemDeflection):
    """ConceptCouplingAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingAdvancedSystemDeflection"
    )

    class _Cast_ConceptCouplingAdvancedSystemDeflection:
        """Special nested class for casting ConceptCouplingAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ConceptCouplingAdvancedSystemDeflection._Cast_ConceptCouplingAdvancedSystemDeflection",
            parent: "ConceptCouplingAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_advanced_system_deflection(
            self: "ConceptCouplingAdvancedSystemDeflection._Cast_ConceptCouplingAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7308.CouplingAdvancedSystemDeflection)

        @property
        def specialised_assembly_advanced_system_deflection(
            self: "ConceptCouplingAdvancedSystemDeflection._Cast_ConceptCouplingAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7371,
            )

            return self._parent._cast(_7371.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "ConceptCouplingAdvancedSystemDeflection._Cast_ConceptCouplingAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7267,
            )

            return self._parent._cast(_7267.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "ConceptCouplingAdvancedSystemDeflection._Cast_ConceptCouplingAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7352,
            )

            return self._parent._cast(_7352.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "ConceptCouplingAdvancedSystemDeflection._Cast_ConceptCouplingAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptCouplingAdvancedSystemDeflection._Cast_ConceptCouplingAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptCouplingAdvancedSystemDeflection._Cast_ConceptCouplingAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingAdvancedSystemDeflection._Cast_ConceptCouplingAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingAdvancedSystemDeflection._Cast_ConceptCouplingAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def concept_coupling_advanced_system_deflection(
            self: "ConceptCouplingAdvancedSystemDeflection._Cast_ConceptCouplingAdvancedSystemDeflection",
        ) -> "ConceptCouplingAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingAdvancedSystemDeflection._Cast_ConceptCouplingAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "ConceptCouplingAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2579.ConceptCoupling":
        """mastapy.system_model.part_model.couplings.ConceptCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6838.ConceptCouplingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_system_deflection_results(
        self: Self,
    ) -> "List[_2717.ConceptCouplingSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ConceptCouplingSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblySystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptCouplingAdvancedSystemDeflection._Cast_ConceptCouplingAdvancedSystemDeflection":
        return self._Cast_ConceptCouplingAdvancedSystemDeflection(self)
