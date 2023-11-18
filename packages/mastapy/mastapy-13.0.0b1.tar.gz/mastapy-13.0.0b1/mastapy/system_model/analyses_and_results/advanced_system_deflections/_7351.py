"""OilSealAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7306
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OIL_SEAL_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "OilSealAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2464
    from mastapy.system_model.analyses_and_results.static_loads import _6924
    from mastapy.system_model.analyses_and_results.system_deflections import _2782


__docformat__ = "restructuredtext en"
__all__ = ("OilSealAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="OilSealAdvancedSystemDeflection")


class OilSealAdvancedSystemDeflection(_7306.ConnectorAdvancedSystemDeflection):
    """OilSealAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _OIL_SEAL_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OilSealAdvancedSystemDeflection")

    class _Cast_OilSealAdvancedSystemDeflection:
        """Special nested class for casting OilSealAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "OilSealAdvancedSystemDeflection._Cast_OilSealAdvancedSystemDeflection",
            parent: "OilSealAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def connector_advanced_system_deflection(
            self: "OilSealAdvancedSystemDeflection._Cast_OilSealAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7306.ConnectorAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(
            self: "OilSealAdvancedSystemDeflection._Cast_OilSealAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7350,
            )

            return self._parent._cast(_7350.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "OilSealAdvancedSystemDeflection._Cast_OilSealAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7295,
            )

            return self._parent._cast(_7295.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "OilSealAdvancedSystemDeflection._Cast_OilSealAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7352,
            )

            return self._parent._cast(_7352.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "OilSealAdvancedSystemDeflection._Cast_OilSealAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "OilSealAdvancedSystemDeflection._Cast_OilSealAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "OilSealAdvancedSystemDeflection._Cast_OilSealAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "OilSealAdvancedSystemDeflection._Cast_OilSealAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "OilSealAdvancedSystemDeflection._Cast_OilSealAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def oil_seal_advanced_system_deflection(
            self: "OilSealAdvancedSystemDeflection._Cast_OilSealAdvancedSystemDeflection",
        ) -> "OilSealAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "OilSealAdvancedSystemDeflection._Cast_OilSealAdvancedSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "OilSealAdvancedSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2464.OilSeal":
        """mastapy.system_model.part_model.OilSeal

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6924.OilSealLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.OilSealLoadCase

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
    ) -> "List[_2782.OilSealSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.OilSealSystemDeflection]

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
    ) -> "OilSealAdvancedSystemDeflection._Cast_OilSealAdvancedSystemDeflection":
        return self._Cast_OilSealAdvancedSystemDeflection(self)
