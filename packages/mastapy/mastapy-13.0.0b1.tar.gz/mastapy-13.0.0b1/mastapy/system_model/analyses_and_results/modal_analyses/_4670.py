"""RingPinsToDiscConnectionModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4639
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_TO_DISC_CONNECTION_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "RingPinsToDiscConnectionModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2339
    from mastapy.system_model.analyses_and_results.static_loads import _6942
    from mastapy.system_model.analyses_and_results.system_deflections import _2793


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsToDiscConnectionModalAnalysis",)


Self = TypeVar("Self", bound="RingPinsToDiscConnectionModalAnalysis")


class RingPinsToDiscConnectionModalAnalysis(
    _4639.InterMountableComponentConnectionModalAnalysis
):
    """RingPinsToDiscConnectionModalAnalysis

    This is a mastapy class.
    """

    TYPE = _RING_PINS_TO_DISC_CONNECTION_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RingPinsToDiscConnectionModalAnalysis"
    )

    class _Cast_RingPinsToDiscConnectionModalAnalysis:
        """Special nested class for casting RingPinsToDiscConnectionModalAnalysis to subclasses."""

        def __init__(
            self: "RingPinsToDiscConnectionModalAnalysis._Cast_RingPinsToDiscConnectionModalAnalysis",
            parent: "RingPinsToDiscConnectionModalAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_modal_analysis(
            self: "RingPinsToDiscConnectionModalAnalysis._Cast_RingPinsToDiscConnectionModalAnalysis",
        ):
            return self._parent._cast(
                _4639.InterMountableComponentConnectionModalAnalysis
            )

        @property
        def connection_modal_analysis(
            self: "RingPinsToDiscConnectionModalAnalysis._Cast_RingPinsToDiscConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4604

            return self._parent._cast(_4604.ConnectionModalAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "RingPinsToDiscConnectionModalAnalysis._Cast_RingPinsToDiscConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "RingPinsToDiscConnectionModalAnalysis._Cast_RingPinsToDiscConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "RingPinsToDiscConnectionModalAnalysis._Cast_RingPinsToDiscConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RingPinsToDiscConnectionModalAnalysis._Cast_RingPinsToDiscConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsToDiscConnectionModalAnalysis._Cast_RingPinsToDiscConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def ring_pins_to_disc_connection_modal_analysis(
            self: "RingPinsToDiscConnectionModalAnalysis._Cast_RingPinsToDiscConnectionModalAnalysis",
        ) -> "RingPinsToDiscConnectionModalAnalysis":
            return self._parent

        def __getattr__(
            self: "RingPinsToDiscConnectionModalAnalysis._Cast_RingPinsToDiscConnectionModalAnalysis",
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
        self: Self, instance_to_wrap: "RingPinsToDiscConnectionModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2339.RingPinsToDiscConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6942.RingPinsToDiscConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RingPinsToDiscConnectionLoadCase

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
    ) -> "_2793.RingPinsToDiscConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.RingPinsToDiscConnectionSystemDeflection

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
    ) -> "RingPinsToDiscConnectionModalAnalysis._Cast_RingPinsToDiscConnectionModalAnalysis":
        return self._Cast_RingPinsToDiscConnectionModalAnalysis(self)
