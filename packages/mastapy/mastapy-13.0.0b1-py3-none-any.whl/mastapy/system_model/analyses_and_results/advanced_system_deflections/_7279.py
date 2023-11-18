"""BeltConnectionAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7337
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "BeltConnectionAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2266
    from mastapy.system_model.analyses_and_results.static_loads import _6818
    from mastapy.system_model.analyses_and_results.system_deflections import _2697


__docformat__ = "restructuredtext en"
__all__ = ("BeltConnectionAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="BeltConnectionAdvancedSystemDeflection")


class BeltConnectionAdvancedSystemDeflection(
    _7337.InterMountableComponentConnectionAdvancedSystemDeflection
):
    """BeltConnectionAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BELT_CONNECTION_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BeltConnectionAdvancedSystemDeflection"
    )

    class _Cast_BeltConnectionAdvancedSystemDeflection:
        """Special nested class for casting BeltConnectionAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "BeltConnectionAdvancedSystemDeflection._Cast_BeltConnectionAdvancedSystemDeflection",
            parent: "BeltConnectionAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_advanced_system_deflection(
            self: "BeltConnectionAdvancedSystemDeflection._Cast_BeltConnectionAdvancedSystemDeflection",
        ):
            return self._parent._cast(
                _7337.InterMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def connection_advanced_system_deflection(
            self: "BeltConnectionAdvancedSystemDeflection._Cast_BeltConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7305,
            )

            return self._parent._cast(_7305.ConnectionAdvancedSystemDeflection)

        @property
        def connection_static_load_analysis_case(
            self: "BeltConnectionAdvancedSystemDeflection._Cast_BeltConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BeltConnectionAdvancedSystemDeflection._Cast_BeltConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BeltConnectionAdvancedSystemDeflection._Cast_BeltConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BeltConnectionAdvancedSystemDeflection._Cast_BeltConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltConnectionAdvancedSystemDeflection._Cast_BeltConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_advanced_system_deflection(
            self: "BeltConnectionAdvancedSystemDeflection._Cast_BeltConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7312,
            )

            return self._parent._cast(_7312.CVTBeltConnectionAdvancedSystemDeflection)

        @property
        def belt_connection_advanced_system_deflection(
            self: "BeltConnectionAdvancedSystemDeflection._Cast_BeltConnectionAdvancedSystemDeflection",
        ) -> "BeltConnectionAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BeltConnectionAdvancedSystemDeflection._Cast_BeltConnectionAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "BeltConnectionAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2266.BeltConnection":
        """mastapy.system_model.connections_and_sockets.BeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6818.BeltConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BeltConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_system_deflection_results(
        self: Self,
    ) -> "List[_2697.BeltConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BeltConnectionSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BeltConnectionAdvancedSystemDeflection._Cast_BeltConnectionAdvancedSystemDeflection":
        return self._Cast_BeltConnectionAdvancedSystemDeflection(self)
