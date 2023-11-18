"""CycloidalDiscCentralBearingConnectionModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4593
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "CycloidalDiscCentralBearingConnectionModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2333
    from mastapy.system_model.analyses_and_results.system_deflections import _2734


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnectionModalAnalysis",)


Self = TypeVar("Self", bound="CycloidalDiscCentralBearingConnectionModalAnalysis")


class CycloidalDiscCentralBearingConnectionModalAnalysis(
    _4593.CoaxialConnectionModalAnalysis
):
    """CycloidalDiscCentralBearingConnectionModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CycloidalDiscCentralBearingConnectionModalAnalysis"
    )

    class _Cast_CycloidalDiscCentralBearingConnectionModalAnalysis:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionModalAnalysis to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysis._Cast_CycloidalDiscCentralBearingConnectionModalAnalysis",
            parent: "CycloidalDiscCentralBearingConnectionModalAnalysis",
        ):
            self._parent = parent

        @property
        def coaxial_connection_modal_analysis(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysis._Cast_CycloidalDiscCentralBearingConnectionModalAnalysis",
        ):
            return self._parent._cast(_4593.CoaxialConnectionModalAnalysis)

        @property
        def shaft_to_mountable_component_connection_modal_analysis(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysis._Cast_CycloidalDiscCentralBearingConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4678

            return self._parent._cast(
                _4678.ShaftToMountableComponentConnectionModalAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_modal_analysis(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysis._Cast_CycloidalDiscCentralBearingConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4572

            return self._parent._cast(
                _4572.AbstractShaftToMountableComponentConnectionModalAnalysis
            )

        @property
        def connection_modal_analysis(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysis._Cast_CycloidalDiscCentralBearingConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4604

            return self._parent._cast(_4604.ConnectionModalAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysis._Cast_CycloidalDiscCentralBearingConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysis._Cast_CycloidalDiscCentralBearingConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysis._Cast_CycloidalDiscCentralBearingConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysis._Cast_CycloidalDiscCentralBearingConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysis._Cast_CycloidalDiscCentralBearingConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_modal_analysis(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysis._Cast_CycloidalDiscCentralBearingConnectionModalAnalysis",
        ) -> "CycloidalDiscCentralBearingConnectionModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionModalAnalysis._Cast_CycloidalDiscCentralBearingConnectionModalAnalysis",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2333.CycloidalDiscCentralBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscCentralBearingConnection

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
    ) -> "_2734.CycloidalDiscCentralBearingConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CycloidalDiscCentralBearingConnectionSystemDeflection

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
    ) -> "CycloidalDiscCentralBearingConnectionModalAnalysis._Cast_CycloidalDiscCentralBearingConnectionModalAnalysis":
        return self._Cast_CycloidalDiscCentralBearingConnectionModalAnalysis(self)
