"""PulleyAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7310
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PULLEY_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "PulleyAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2588
    from mastapy.system_model.analyses_and_results.static_loads import _6938
    from mastapy.system_model.analyses_and_results.system_deflections import _2791


__docformat__ = "restructuredtext en"
__all__ = ("PulleyAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="PulleyAdvancedSystemDeflection")


class PulleyAdvancedSystemDeflection(_7310.CouplingHalfAdvancedSystemDeflection):
    """PulleyAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _PULLEY_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PulleyAdvancedSystemDeflection")

    class _Cast_PulleyAdvancedSystemDeflection:
        """Special nested class for casting PulleyAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "PulleyAdvancedSystemDeflection._Cast_PulleyAdvancedSystemDeflection",
            parent: "PulleyAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_half_advanced_system_deflection(
            self: "PulleyAdvancedSystemDeflection._Cast_PulleyAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7310.CouplingHalfAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(
            self: "PulleyAdvancedSystemDeflection._Cast_PulleyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7350,
            )

            return self._parent._cast(_7350.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "PulleyAdvancedSystemDeflection._Cast_PulleyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7295,
            )

            return self._parent._cast(_7295.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "PulleyAdvancedSystemDeflection._Cast_PulleyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7352,
            )

            return self._parent._cast(_7352.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "PulleyAdvancedSystemDeflection._Cast_PulleyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PulleyAdvancedSystemDeflection._Cast_PulleyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PulleyAdvancedSystemDeflection._Cast_PulleyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PulleyAdvancedSystemDeflection._Cast_PulleyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PulleyAdvancedSystemDeflection._Cast_PulleyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cvt_pulley_advanced_system_deflection(
            self: "PulleyAdvancedSystemDeflection._Cast_PulleyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7313,
            )

            return self._parent._cast(_7313.CVTPulleyAdvancedSystemDeflection)

        @property
        def pulley_advanced_system_deflection(
            self: "PulleyAdvancedSystemDeflection._Cast_PulleyAdvancedSystemDeflection",
        ) -> "PulleyAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "PulleyAdvancedSystemDeflection._Cast_PulleyAdvancedSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PulleyAdvancedSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2588.Pulley":
        """mastapy.system_model.part_model.couplings.Pulley

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6938.PulleyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PulleyLoadCase

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
    ) -> "List[_2791.PulleySystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.PulleySystemDeflection]

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
    ) -> "PulleyAdvancedSystemDeflection._Cast_PulleyAdvancedSystemDeflection":
        return self._Cast_PulleyAdvancedSystemDeflection(self)
