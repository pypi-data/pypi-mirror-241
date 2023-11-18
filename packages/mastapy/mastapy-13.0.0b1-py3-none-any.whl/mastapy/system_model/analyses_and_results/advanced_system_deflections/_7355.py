"""PartToPartShearCouplingHalfAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7310
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "PartToPartShearCouplingHalfAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2587
    from mastapy.system_model.analyses_and_results.static_loads import _6928
    from mastapy.system_model.analyses_and_results.system_deflections import _2785


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingHalfAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="PartToPartShearCouplingHalfAdvancedSystemDeflection")


class PartToPartShearCouplingHalfAdvancedSystemDeflection(
    _7310.CouplingHalfAdvancedSystemDeflection
):
    """PartToPartShearCouplingHalfAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartToPartShearCouplingHalfAdvancedSystemDeflection"
    )

    class _Cast_PartToPartShearCouplingHalfAdvancedSystemDeflection:
        """Special nested class for casting PartToPartShearCouplingHalfAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingHalfAdvancedSystemDeflection._Cast_PartToPartShearCouplingHalfAdvancedSystemDeflection",
            parent: "PartToPartShearCouplingHalfAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_half_advanced_system_deflection(
            self: "PartToPartShearCouplingHalfAdvancedSystemDeflection._Cast_PartToPartShearCouplingHalfAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7310.CouplingHalfAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(
            self: "PartToPartShearCouplingHalfAdvancedSystemDeflection._Cast_PartToPartShearCouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7350,
            )

            return self._parent._cast(_7350.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "PartToPartShearCouplingHalfAdvancedSystemDeflection._Cast_PartToPartShearCouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7295,
            )

            return self._parent._cast(_7295.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "PartToPartShearCouplingHalfAdvancedSystemDeflection._Cast_PartToPartShearCouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7352,
            )

            return self._parent._cast(_7352.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "PartToPartShearCouplingHalfAdvancedSystemDeflection._Cast_PartToPartShearCouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartToPartShearCouplingHalfAdvancedSystemDeflection._Cast_PartToPartShearCouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartToPartShearCouplingHalfAdvancedSystemDeflection._Cast_PartToPartShearCouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingHalfAdvancedSystemDeflection._Cast_PartToPartShearCouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingHalfAdvancedSystemDeflection._Cast_PartToPartShearCouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_half_advanced_system_deflection(
            self: "PartToPartShearCouplingHalfAdvancedSystemDeflection._Cast_PartToPartShearCouplingHalfAdvancedSystemDeflection",
        ) -> "PartToPartShearCouplingHalfAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingHalfAdvancedSystemDeflection._Cast_PartToPartShearCouplingHalfAdvancedSystemDeflection",
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
        instance_to_wrap: "PartToPartShearCouplingHalfAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2587.PartToPartShearCouplingHalf":
        """mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6928.PartToPartShearCouplingHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingHalfLoadCase

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
    ) -> "List[_2785.PartToPartShearCouplingHalfSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.PartToPartShearCouplingHalfSystemDeflection]

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
    ) -> "PartToPartShearCouplingHalfAdvancedSystemDeflection._Cast_PartToPartShearCouplingHalfAdvancedSystemDeflection":
        return self._Cast_PartToPartShearCouplingHalfAdvancedSystemDeflection(self)
