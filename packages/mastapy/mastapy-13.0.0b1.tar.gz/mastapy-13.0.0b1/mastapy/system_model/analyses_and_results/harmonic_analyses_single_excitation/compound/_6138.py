"""AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6161,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6007,
    )


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation"
)


class AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation(
    _6161.ComponentCompoundHarmonicAnalysisOfSingleExcitation
):
    """AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def component_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(
                _6161.ComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6215,
            )

            return self._parent._cast(
                _6215.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6137,
            )

            return self._parent._cast(
                _6137.AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6181,
            )

            return self._parent._cast(
                _6181.CycloidalDiscCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def fe_part_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6192,
            )

            return self._parent._cast(
                _6192.FEPartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6231,
            )

            return self._parent._cast(
                _6231.ShaftCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_or_housing_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6007.AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6007.AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation":
        return (
            self._Cast_AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation(
                self
            )
        )
