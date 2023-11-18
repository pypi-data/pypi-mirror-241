"""SpringDamperConnectionCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7441,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "SpringDamperConnectionCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2348
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7376,
    )


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperConnectionCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="SpringDamperConnectionCompoundAdvancedSystemDeflection")


class SpringDamperConnectionCompoundAdvancedSystemDeflection(
    _7441.CouplingConnectionCompoundAdvancedSystemDeflection
):
    """SpringDamperConnectionCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SpringDamperConnectionCompoundAdvancedSystemDeflection",
    )

    class _Cast_SpringDamperConnectionCompoundAdvancedSystemDeflection:
        """Special nested class for casting SpringDamperConnectionCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "SpringDamperConnectionCompoundAdvancedSystemDeflection._Cast_SpringDamperConnectionCompoundAdvancedSystemDeflection",
            parent: "SpringDamperConnectionCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_advanced_system_deflection(
            self: "SpringDamperConnectionCompoundAdvancedSystemDeflection._Cast_SpringDamperConnectionCompoundAdvancedSystemDeflection",
        ):
            return self._parent._cast(
                _7441.CouplingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def inter_mountable_component_connection_compound_advanced_system_deflection(
            self: "SpringDamperConnectionCompoundAdvancedSystemDeflection._Cast_SpringDamperConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7468,
            )

            return self._parent._cast(
                _7468.InterMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def connection_compound_advanced_system_deflection(
            self: "SpringDamperConnectionCompoundAdvancedSystemDeflection._Cast_SpringDamperConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7438,
            )

            return self._parent._cast(_7438.ConnectionCompoundAdvancedSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "SpringDamperConnectionCompoundAdvancedSystemDeflection._Cast_SpringDamperConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpringDamperConnectionCompoundAdvancedSystemDeflection._Cast_SpringDamperConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperConnectionCompoundAdvancedSystemDeflection._Cast_SpringDamperConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def spring_damper_connection_compound_advanced_system_deflection(
            self: "SpringDamperConnectionCompoundAdvancedSystemDeflection._Cast_SpringDamperConnectionCompoundAdvancedSystemDeflection",
        ) -> "SpringDamperConnectionCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "SpringDamperConnectionCompoundAdvancedSystemDeflection._Cast_SpringDamperConnectionCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "SpringDamperConnectionCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2348.SpringDamperConnection":
        """mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2348.SpringDamperConnection":
        """mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_7376.SpringDamperConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.SpringDamperConnectionAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_7376.SpringDamperConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.SpringDamperConnectionAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpringDamperConnectionCompoundAdvancedSystemDeflection._Cast_SpringDamperConnectionCompoundAdvancedSystemDeflection":
        return self._Cast_SpringDamperConnectionCompoundAdvancedSystemDeflection(self)
