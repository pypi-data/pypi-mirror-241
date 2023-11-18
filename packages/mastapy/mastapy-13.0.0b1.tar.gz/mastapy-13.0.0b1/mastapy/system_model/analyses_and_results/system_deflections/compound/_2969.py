"""TorqueConverterConnectionCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2887
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "TorqueConverterConnectionCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2350
    from mastapy.system_model.analyses_and_results.system_deflections import _2826


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterConnectionCompoundSystemDeflection",)


Self = TypeVar("Self", bound="TorqueConverterConnectionCompoundSystemDeflection")


class TorqueConverterConnectionCompoundSystemDeflection(
    _2887.CouplingConnectionCompoundSystemDeflection
):
    """TorqueConverterConnectionCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_CONNECTION_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterConnectionCompoundSystemDeflection"
    )

    class _Cast_TorqueConverterConnectionCompoundSystemDeflection:
        """Special nested class for casting TorqueConverterConnectionCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "TorqueConverterConnectionCompoundSystemDeflection._Cast_TorqueConverterConnectionCompoundSystemDeflection",
            parent: "TorqueConverterConnectionCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_system_deflection(
            self: "TorqueConverterConnectionCompoundSystemDeflection._Cast_TorqueConverterConnectionCompoundSystemDeflection",
        ):
            return self._parent._cast(_2887.CouplingConnectionCompoundSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_system_deflection(
            self: "TorqueConverterConnectionCompoundSystemDeflection._Cast_TorqueConverterConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2915,
            )

            return self._parent._cast(
                _2915.InterMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def connection_compound_system_deflection(
            self: "TorqueConverterConnectionCompoundSystemDeflection._Cast_TorqueConverterConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2884,
            )

            return self._parent._cast(_2884.ConnectionCompoundSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "TorqueConverterConnectionCompoundSystemDeflection._Cast_TorqueConverterConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "TorqueConverterConnectionCompoundSystemDeflection._Cast_TorqueConverterConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterConnectionCompoundSystemDeflection._Cast_TorqueConverterConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def torque_converter_connection_compound_system_deflection(
            self: "TorqueConverterConnectionCompoundSystemDeflection._Cast_TorqueConverterConnectionCompoundSystemDeflection",
        ) -> "TorqueConverterConnectionCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "TorqueConverterConnectionCompoundSystemDeflection._Cast_TorqueConverterConnectionCompoundSystemDeflection",
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
        instance_to_wrap: "TorqueConverterConnectionCompoundSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2350.TorqueConverterConnection":
        """mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2350.TorqueConverterConnection":
        """mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection

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
    ) -> "List[_2826.TorqueConverterConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterConnectionSystemDeflection]

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
    ) -> "List[_2826.TorqueConverterConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterConnectionSystemDeflection]

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
    ) -> "TorqueConverterConnectionCompoundSystemDeflection._Cast_TorqueConverterConnectionCompoundSystemDeflection":
        return self._Cast_TorqueConverterConnectionCompoundSystemDeflection(self)
