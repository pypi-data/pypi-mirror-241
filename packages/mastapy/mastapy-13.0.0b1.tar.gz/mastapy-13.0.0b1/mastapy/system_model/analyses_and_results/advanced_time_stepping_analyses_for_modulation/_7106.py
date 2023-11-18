"""ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7006,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2293
    from mastapy.system_model.analyses_and_results.system_deflections import _2803


__docformat__ = "restructuredtext en"
__all__ = (
    "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
)


Self = TypeVar(
    "Self",
    bound="ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
)


class ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation(
    _7006.AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
):
    """ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
            parent: "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            return self._parent._cast(
                _7006.AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_advanced_time_stepping_analysis_for_modulation(
            self: "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7043,
            )

            return self._parent._cast(
                _7043.ConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_static_load_analysis_case(
            self: "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def coaxial_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7032,
            )

            return self._parent._cast(
                _7032.CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_disc_central_bearing_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7053,
            )

            return self._parent._cast(
                _7053.CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planetary_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7092,
            )

            return self._parent._cast(
                _7092.PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_to_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2293.ShaftToMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2803.ShaftToMountableComponentConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ShaftToMountableComponentConnectionSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation(
            self
        )
