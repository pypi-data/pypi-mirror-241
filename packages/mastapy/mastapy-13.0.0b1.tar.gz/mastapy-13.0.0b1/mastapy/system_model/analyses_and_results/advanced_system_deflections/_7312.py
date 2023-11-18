"""CVTBeltConnectionAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7279
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "CVTBeltConnectionAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2271


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnectionAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="CVTBeltConnectionAdvancedSystemDeflection")


class CVTBeltConnectionAdvancedSystemDeflection(
    _7279.BeltConnectionAdvancedSystemDeflection
):
    """CVTBeltConnectionAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTBeltConnectionAdvancedSystemDeflection"
    )

    class _Cast_CVTBeltConnectionAdvancedSystemDeflection:
        """Special nested class for casting CVTBeltConnectionAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "CVTBeltConnectionAdvancedSystemDeflection._Cast_CVTBeltConnectionAdvancedSystemDeflection",
            parent: "CVTBeltConnectionAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def belt_connection_advanced_system_deflection(
            self: "CVTBeltConnectionAdvancedSystemDeflection._Cast_CVTBeltConnectionAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7279.BeltConnectionAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_advanced_system_deflection(
            self: "CVTBeltConnectionAdvancedSystemDeflection._Cast_CVTBeltConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7337,
            )

            return self._parent._cast(
                _7337.InterMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def connection_advanced_system_deflection(
            self: "CVTBeltConnectionAdvancedSystemDeflection._Cast_CVTBeltConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7305,
            )

            return self._parent._cast(_7305.ConnectionAdvancedSystemDeflection)

        @property
        def connection_static_load_analysis_case(
            self: "CVTBeltConnectionAdvancedSystemDeflection._Cast_CVTBeltConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CVTBeltConnectionAdvancedSystemDeflection._Cast_CVTBeltConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CVTBeltConnectionAdvancedSystemDeflection._Cast_CVTBeltConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTBeltConnectionAdvancedSystemDeflection._Cast_CVTBeltConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTBeltConnectionAdvancedSystemDeflection._Cast_CVTBeltConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_advanced_system_deflection(
            self: "CVTBeltConnectionAdvancedSystemDeflection._Cast_CVTBeltConnectionAdvancedSystemDeflection",
        ) -> "CVTBeltConnectionAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CVTBeltConnectionAdvancedSystemDeflection._Cast_CVTBeltConnectionAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "CVTBeltConnectionAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2271.CVTBeltConnection":
        """mastapy.system_model.connections_and_sockets.CVTBeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CVTBeltConnectionAdvancedSystemDeflection._Cast_CVTBeltConnectionAdvancedSystemDeflection":
        return self._Cast_CVTBeltConnectionAdvancedSystemDeflection(self)
