"""CycloidalDiscHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6006,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "CycloidalDiscHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2567
    from mastapy.system_model.analyses_and_results.static_loads import _6857


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="CycloidalDiscHarmonicAnalysisOfSingleExcitation")


class CycloidalDiscHarmonicAnalysisOfSingleExcitation(
    _6006.AbstractShaftHarmonicAnalysisOfSingleExcitation
):
    """CycloidalDiscHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CycloidalDiscHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_CycloidalDiscHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting CycloidalDiscHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "CycloidalDiscHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscHarmonicAnalysisOfSingleExcitation",
            parent: "CycloidalDiscHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def abstract_shaft_harmonic_analysis_of_single_excitation(
            self: "CycloidalDiscHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(
                _6006.AbstractShaftHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_or_housing_harmonic_analysis_of_single_excitation(
            self: "CycloidalDiscHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6007,
            )

            return self._parent._cast(
                _6007.AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "CycloidalDiscHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6030,
            )

            return self._parent._cast(_6030.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "CycloidalDiscHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6086,
            )

            return self._parent._cast(_6086.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "CycloidalDiscHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CycloidalDiscHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CycloidalDiscHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cycloidal_disc_harmonic_analysis_of_single_excitation(
            self: "CycloidalDiscHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscHarmonicAnalysisOfSingleExcitation",
        ) -> "CycloidalDiscHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "CycloidalDiscHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2567.CycloidalDisc":
        """mastapy.system_model.part_model.cycloidal.CycloidalDisc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6857.CycloidalDiscLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscHarmonicAnalysisOfSingleExcitation":
        return self._Cast_CycloidalDiscHarmonicAnalysisOfSingleExcitation(self)
