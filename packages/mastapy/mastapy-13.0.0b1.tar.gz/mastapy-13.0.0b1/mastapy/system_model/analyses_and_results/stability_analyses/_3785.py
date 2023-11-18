"""CoaxialConnectionStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3860
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "CoaxialConnectionStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2267
    from mastapy.system_model.analyses_and_results.static_loads import _6834


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnectionStabilityAnalysis",)


Self = TypeVar("Self", bound="CoaxialConnectionStabilityAnalysis")


class CoaxialConnectionStabilityAnalysis(
    _3860.ShaftToMountableComponentConnectionStabilityAnalysis
):
    """CoaxialConnectionStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CoaxialConnectionStabilityAnalysis")

    class _Cast_CoaxialConnectionStabilityAnalysis:
        """Special nested class for casting CoaxialConnectionStabilityAnalysis to subclasses."""

        def __init__(
            self: "CoaxialConnectionStabilityAnalysis._Cast_CoaxialConnectionStabilityAnalysis",
            parent: "CoaxialConnectionStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_stability_analysis(
            self: "CoaxialConnectionStabilityAnalysis._Cast_CoaxialConnectionStabilityAnalysis",
        ):
            return self._parent._cast(
                _3860.ShaftToMountableComponentConnectionStabilityAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_stability_analysis(
            self: "CoaxialConnectionStabilityAnalysis._Cast_CoaxialConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3764,
            )

            return self._parent._cast(
                _3764.AbstractShaftToMountableComponentConnectionStabilityAnalysis
            )

        @property
        def connection_stability_analysis(
            self: "CoaxialConnectionStabilityAnalysis._Cast_CoaxialConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3796,
            )

            return self._parent._cast(_3796.ConnectionStabilityAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CoaxialConnectionStabilityAnalysis._Cast_CoaxialConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CoaxialConnectionStabilityAnalysis._Cast_CoaxialConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CoaxialConnectionStabilityAnalysis._Cast_CoaxialConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CoaxialConnectionStabilityAnalysis._Cast_CoaxialConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CoaxialConnectionStabilityAnalysis._Cast_CoaxialConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_stability_analysis(
            self: "CoaxialConnectionStabilityAnalysis._Cast_CoaxialConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3806,
            )

            return self._parent._cast(
                _3806.CycloidalDiscCentralBearingConnectionStabilityAnalysis
            )

        @property
        def coaxial_connection_stability_analysis(
            self: "CoaxialConnectionStabilityAnalysis._Cast_CoaxialConnectionStabilityAnalysis",
        ) -> "CoaxialConnectionStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CoaxialConnectionStabilityAnalysis._Cast_CoaxialConnectionStabilityAnalysis",
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
        self: Self, instance_to_wrap: "CoaxialConnectionStabilityAnalysis.TYPE"
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
    def cast_to(
        self: Self,
    ) -> "CoaxialConnectionStabilityAnalysis._Cast_CoaxialConnectionStabilityAnalysis":
        return self._Cast_CoaxialConnectionStabilityAnalysis(self)
