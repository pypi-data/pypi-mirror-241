"""RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6071,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_TO_DISC_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
        "RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2339
    from mastapy.system_model.analyses_and_results.static_loads import _6942


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation"
)


class RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation(
    _6071.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
):
    """RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _RING_PINS_TO_DISC_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation._Cast_RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation",
            parent: "RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation._Cast_RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(
                _6071.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_harmonic_analysis_of_single_excitation(
            self: "RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation._Cast_RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6040,
            )

            return self._parent._cast(
                _6040.ConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_static_load_analysis_case(
            self: "RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation._Cast_RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation._Cast_RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation._Cast_RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation._Cast_RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation._Cast_RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def ring_pins_to_disc_connection_harmonic_analysis_of_single_excitation(
            self: "RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation._Cast_RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation",
        ) -> "RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation._Cast_RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation.TYPE",
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
    def cast_to(
        self: Self,
    ) -> "RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation._Cast_RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation":
        return self._Cast_RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation(
            self
        )
