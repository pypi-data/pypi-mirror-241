"""CouplingConnectionCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7468,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "CouplingConnectionCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7309,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="CouplingConnectionCompoundAdvancedSystemDeflection")


class CouplingConnectionCompoundAdvancedSystemDeflection(
    _7468.InterMountableComponentConnectionCompoundAdvancedSystemDeflection
):
    """CouplingConnectionCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingConnectionCompoundAdvancedSystemDeflection"
    )

    class _Cast_CouplingConnectionCompoundAdvancedSystemDeflection:
        """Special nested class for casting CouplingConnectionCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "CouplingConnectionCompoundAdvancedSystemDeflection._Cast_CouplingConnectionCompoundAdvancedSystemDeflection",
            parent: "CouplingConnectionCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_advanced_system_deflection(
            self: "CouplingConnectionCompoundAdvancedSystemDeflection._Cast_CouplingConnectionCompoundAdvancedSystemDeflection",
        ):
            return self._parent._cast(
                _7468.InterMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def connection_compound_advanced_system_deflection(
            self: "CouplingConnectionCompoundAdvancedSystemDeflection._Cast_CouplingConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7438,
            )

            return self._parent._cast(_7438.ConnectionCompoundAdvancedSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "CouplingConnectionCompoundAdvancedSystemDeflection._Cast_CouplingConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingConnectionCompoundAdvancedSystemDeflection._Cast_CouplingConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionCompoundAdvancedSystemDeflection._Cast_CouplingConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def clutch_connection_compound_advanced_system_deflection(
            self: "CouplingConnectionCompoundAdvancedSystemDeflection._Cast_CouplingConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7425,
            )

            return self._parent._cast(
                _7425.ClutchConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def concept_coupling_connection_compound_advanced_system_deflection(
            self: "CouplingConnectionCompoundAdvancedSystemDeflection._Cast_CouplingConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7430,
            )

            return self._parent._cast(
                _7430.ConceptCouplingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_connection_compound_advanced_system_deflection(
            self: "CouplingConnectionCompoundAdvancedSystemDeflection._Cast_CouplingConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7484,
            )

            return self._parent._cast(
                _7484.PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def spring_damper_connection_compound_advanced_system_deflection(
            self: "CouplingConnectionCompoundAdvancedSystemDeflection._Cast_CouplingConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7506,
            )

            return self._parent._cast(
                _7506.SpringDamperConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_connection_compound_advanced_system_deflection(
            self: "CouplingConnectionCompoundAdvancedSystemDeflection._Cast_CouplingConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7521,
            )

            return self._parent._cast(
                _7521.TorqueConverterConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def coupling_connection_compound_advanced_system_deflection(
            self: "CouplingConnectionCompoundAdvancedSystemDeflection._Cast_CouplingConnectionCompoundAdvancedSystemDeflection",
        ) -> "CouplingConnectionCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionCompoundAdvancedSystemDeflection._Cast_CouplingConnectionCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "CouplingConnectionCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_7309.CouplingConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CouplingConnectionAdvancedSystemDeflection]

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_7309.CouplingConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CouplingConnectionAdvancedSystemDeflection]

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
    def cast_to(
        self: Self,
    ) -> "CouplingConnectionCompoundAdvancedSystemDeflection._Cast_CouplingConnectionCompoundAdvancedSystemDeflection":
        return self._Cast_CouplingConnectionCompoundAdvancedSystemDeflection(self)
