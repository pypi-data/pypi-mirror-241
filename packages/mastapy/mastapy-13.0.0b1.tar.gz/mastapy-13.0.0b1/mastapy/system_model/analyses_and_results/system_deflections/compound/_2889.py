"""CVTBeltConnectionCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2858
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "CVTBeltConnectionCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2730


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnectionCompoundSystemDeflection",)


Self = TypeVar("Self", bound="CVTBeltConnectionCompoundSystemDeflection")


class CVTBeltConnectionCompoundSystemDeflection(
    _2858.BeltConnectionCompoundSystemDeflection
):
    """CVTBeltConnectionCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTBeltConnectionCompoundSystemDeflection"
    )

    class _Cast_CVTBeltConnectionCompoundSystemDeflection:
        """Special nested class for casting CVTBeltConnectionCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "CVTBeltConnectionCompoundSystemDeflection._Cast_CVTBeltConnectionCompoundSystemDeflection",
            parent: "CVTBeltConnectionCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def belt_connection_compound_system_deflection(
            self: "CVTBeltConnectionCompoundSystemDeflection._Cast_CVTBeltConnectionCompoundSystemDeflection",
        ):
            return self._parent._cast(_2858.BeltConnectionCompoundSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_system_deflection(
            self: "CVTBeltConnectionCompoundSystemDeflection._Cast_CVTBeltConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2915,
            )

            return self._parent._cast(
                _2915.InterMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def connection_compound_system_deflection(
            self: "CVTBeltConnectionCompoundSystemDeflection._Cast_CVTBeltConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2884,
            )

            return self._parent._cast(_2884.ConnectionCompoundSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "CVTBeltConnectionCompoundSystemDeflection._Cast_CVTBeltConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTBeltConnectionCompoundSystemDeflection._Cast_CVTBeltConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTBeltConnectionCompoundSystemDeflection._Cast_CVTBeltConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_compound_system_deflection(
            self: "CVTBeltConnectionCompoundSystemDeflection._Cast_CVTBeltConnectionCompoundSystemDeflection",
        ) -> "CVTBeltConnectionCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CVTBeltConnectionCompoundSystemDeflection._Cast_CVTBeltConnectionCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "CVTBeltConnectionCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def belt_safety_factor_for_clamping_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BeltSafetyFactorForClampingForce

        if temp is None:
            return 0.0

        return temp

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_2730.CVTBeltConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CVTBeltConnectionSystemDeflection]

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
    ) -> "List[_2730.CVTBeltConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CVTBeltConnectionSystemDeflection]

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
    ) -> "CVTBeltConnectionCompoundSystemDeflection._Cast_CVTBeltConnectionCompoundSystemDeflection":
        return self._Cast_CVTBeltConnectionCompoundSystemDeflection(self)
