"""RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6201,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_TO_DISC_CONNECTION_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2339
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6097,
    )


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation"
)


class RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation(
    _6201.InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
):
    """RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _RING_PINS_TO_DISC_CONNECTION_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(
            self: "RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(
                _6201.InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_compound_harmonic_analysis_of_single_excitation(
            self: "RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6171,
            )

            return self._parent._cast(
                _6171.ConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_compound_analysis(
            self: "RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def ring_pins_to_disc_connection_compound_harmonic_analysis_of_single_excitation(
            self: "RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2339.RingPinsToDiscConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_6097.RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6097.RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation(
            self
        )
