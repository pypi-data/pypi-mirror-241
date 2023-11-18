"""ConceptCouplingHalfAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7310
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_HALF_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "ConceptCouplingHalfAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2580
    from mastapy.system_model.analyses_and_results.static_loads import _6837
    from mastapy.system_model.analyses_and_results.system_deflections import _2716


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingHalfAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="ConceptCouplingHalfAdvancedSystemDeflection")


class ConceptCouplingHalfAdvancedSystemDeflection(
    _7310.CouplingHalfAdvancedSystemDeflection
):
    """ConceptCouplingHalfAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_HALF_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingHalfAdvancedSystemDeflection"
    )

    class _Cast_ConceptCouplingHalfAdvancedSystemDeflection:
        """Special nested class for casting ConceptCouplingHalfAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ConceptCouplingHalfAdvancedSystemDeflection._Cast_ConceptCouplingHalfAdvancedSystemDeflection",
            parent: "ConceptCouplingHalfAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_half_advanced_system_deflection(
            self: "ConceptCouplingHalfAdvancedSystemDeflection._Cast_ConceptCouplingHalfAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7310.CouplingHalfAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(
            self: "ConceptCouplingHalfAdvancedSystemDeflection._Cast_ConceptCouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7350,
            )

            return self._parent._cast(_7350.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "ConceptCouplingHalfAdvancedSystemDeflection._Cast_ConceptCouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7295,
            )

            return self._parent._cast(_7295.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "ConceptCouplingHalfAdvancedSystemDeflection._Cast_ConceptCouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7352,
            )

            return self._parent._cast(_7352.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "ConceptCouplingHalfAdvancedSystemDeflection._Cast_ConceptCouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptCouplingHalfAdvancedSystemDeflection._Cast_ConceptCouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptCouplingHalfAdvancedSystemDeflection._Cast_ConceptCouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingHalfAdvancedSystemDeflection._Cast_ConceptCouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingHalfAdvancedSystemDeflection._Cast_ConceptCouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def concept_coupling_half_advanced_system_deflection(
            self: "ConceptCouplingHalfAdvancedSystemDeflection._Cast_ConceptCouplingHalfAdvancedSystemDeflection",
        ) -> "ConceptCouplingHalfAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingHalfAdvancedSystemDeflection._Cast_ConceptCouplingHalfAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "ConceptCouplingHalfAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2580.ConceptCouplingHalf":
        """mastapy.system_model.part_model.couplings.ConceptCouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6837.ConceptCouplingHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingHalfLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_system_deflection_results(
        self: Self,
    ) -> "List[_2716.ConceptCouplingHalfSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ConceptCouplingHalfSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptCouplingHalfAdvancedSystemDeflection._Cast_ConceptCouplingHalfAdvancedSystemDeflection":
        return self._Cast_ConceptCouplingHalfAdvancedSystemDeflection(self)
