"""CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7106,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2267
    from mastapy.system_model.analyses_and_results.static_loads import _6834
    from mastapy.system_model.analyses_and_results.system_deflections import _2712


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation"
)


class CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation(
    _7106.ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
):
    """CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation",
            parent: "CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            return self._parent._cast(
                _7106.ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_shaft_to_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7006,
            )

            return self._parent._cast(
                _7006.AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_advanced_time_stepping_analysis_for_modulation(
            self: "CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7043,
            )

            return self._parent._cast(
                _7043.ConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_static_load_analysis_case(
            self: "CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_advanced_time_stepping_analysis_for_modulation(
            self: "CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7053,
            )

            return self._parent._cast(
                _7053.CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coaxial_connection_advanced_time_stepping_analysis_for_modulation(
            self: "CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2267.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6834.CoaxialConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CoaxialConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2712.CoaxialConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CoaxialConnectionSystemDeflection

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
    ) -> "CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation(
            self
        )
