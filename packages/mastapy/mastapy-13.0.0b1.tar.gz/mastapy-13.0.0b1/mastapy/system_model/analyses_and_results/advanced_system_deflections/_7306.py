"""ConnectorAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7350
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "ConnectorAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2445


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="ConnectorAdvancedSystemDeflection")


class ConnectorAdvancedSystemDeflection(
    _7350.MountableComponentAdvancedSystemDeflection
):
    """ConnectorAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectorAdvancedSystemDeflection")

    class _Cast_ConnectorAdvancedSystemDeflection:
        """Special nested class for casting ConnectorAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
            parent: "ConnectorAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def mountable_component_advanced_system_deflection(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7350.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7295,
            )

            return self._parent._cast(_7295.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7352,
            )

            return self._parent._cast(_7352.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bearing_advanced_system_deflection(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7278,
            )

            return self._parent._cast(_7278.BearingAdvancedSystemDeflection)

        @property
        def oil_seal_advanced_system_deflection(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7351,
            )

            return self._parent._cast(_7351.OilSealAdvancedSystemDeflection)

        @property
        def shaft_hub_connection_advanced_system_deflection(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7369,
            )

            return self._parent._cast(_7369.ShaftHubConnectionAdvancedSystemDeflection)

        @property
        def connector_advanced_system_deflection(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
        ) -> "ConnectorAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "ConnectorAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2445.Connector":
        """mastapy.system_model.part_model.Connector

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection":
        return self._Cast_ConnectorAdvancedSystemDeflection(self)
