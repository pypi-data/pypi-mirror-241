"""AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7305
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_ADVANCED_SYSTEM_DEFLECTION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
        "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2263


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",)


Self = TypeVar(
    "Self", bound="AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection"
)


class AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection(
    _7305.ConnectionAdvancedSystemDeflection
):
    """AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",
            parent: "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def connection_advanced_system_deflection(
            self: "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7305.ConnectionAdvancedSystemDeflection)

        @property
        def connection_static_load_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def coaxial_connection_advanced_system_deflection(
            self: "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7294,
            )

            return self._parent._cast(_7294.CoaxialConnectionAdvancedSystemDeflection)

        @property
        def cycloidal_disc_central_bearing_connection_advanced_system_deflection(
            self: "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7316,
            )

            return self._parent._cast(
                _7316.CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_advanced_system_deflection(
            self: "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7317,
            )

            return self._parent._cast(
                _7317.CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection
            )

        @property
        def planetary_connection_advanced_system_deflection(
            self: "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7356,
            )

            return self._parent._cast(_7356.PlanetaryConnectionAdvancedSystemDeflection)

        @property
        def shaft_to_mountable_component_connection_advanced_system_deflection(
            self: "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7370,
            )

            return self._parent._cast(
                _7370.ShaftToMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def abstract_shaft_to_mountable_component_connection_advanced_system_deflection(
            self: "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2263.AbstractShaftToMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.AbstractShaftToMountableComponentConnection

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
    ) -> "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection":
        return self._Cast_AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection(
            self
        )
