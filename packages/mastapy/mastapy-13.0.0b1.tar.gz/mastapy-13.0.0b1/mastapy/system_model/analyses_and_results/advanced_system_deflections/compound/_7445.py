"""CVTPulleyCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7491,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "CVTPulleyCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7313,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="CVTPulleyCompoundAdvancedSystemDeflection")


class CVTPulleyCompoundAdvancedSystemDeflection(
    _7491.PulleyCompoundAdvancedSystemDeflection
):
    """CVTPulleyCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTPulleyCompoundAdvancedSystemDeflection"
    )

    class _Cast_CVTPulleyCompoundAdvancedSystemDeflection:
        """Special nested class for casting CVTPulleyCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "CVTPulleyCompoundAdvancedSystemDeflection._Cast_CVTPulleyCompoundAdvancedSystemDeflection",
            parent: "CVTPulleyCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def pulley_compound_advanced_system_deflection(
            self: "CVTPulleyCompoundAdvancedSystemDeflection._Cast_CVTPulleyCompoundAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7491.PulleyCompoundAdvancedSystemDeflection)

        @property
        def coupling_half_compound_advanced_system_deflection(
            self: "CVTPulleyCompoundAdvancedSystemDeflection._Cast_CVTPulleyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7442,
            )

            return self._parent._cast(
                _7442.CouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "CVTPulleyCompoundAdvancedSystemDeflection._Cast_CVTPulleyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7480,
            )

            return self._parent._cast(
                _7480.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "CVTPulleyCompoundAdvancedSystemDeflection._Cast_CVTPulleyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7428,
            )

            return self._parent._cast(_7428.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "CVTPulleyCompoundAdvancedSystemDeflection._Cast_CVTPulleyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7482,
            )

            return self._parent._cast(_7482.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "CVTPulleyCompoundAdvancedSystemDeflection._Cast_CVTPulleyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTPulleyCompoundAdvancedSystemDeflection._Cast_CVTPulleyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyCompoundAdvancedSystemDeflection._Cast_CVTPulleyCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cvt_pulley_compound_advanced_system_deflection(
            self: "CVTPulleyCompoundAdvancedSystemDeflection._Cast_CVTPulleyCompoundAdvancedSystemDeflection",
        ) -> "CVTPulleyCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CVTPulleyCompoundAdvancedSystemDeflection._Cast_CVTPulleyCompoundAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "CVTPulleyCompoundAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_7313.CVTPulleyAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CVTPulleyAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7313.CVTPulleyAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CVTPulleyAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CVTPulleyCompoundAdvancedSystemDeflection._Cast_CVTPulleyCompoundAdvancedSystemDeflection":
        return self._Cast_CVTPulleyCompoundAdvancedSystemDeflection(self)
