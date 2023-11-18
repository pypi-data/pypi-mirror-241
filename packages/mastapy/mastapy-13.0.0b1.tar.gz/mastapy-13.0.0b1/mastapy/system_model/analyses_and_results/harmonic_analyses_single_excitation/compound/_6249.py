"""SynchroniserCompoundHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6234,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "SynchroniserCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2600
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6121,
    )


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="SynchroniserCompoundHarmonicAnalysisOfSingleExcitation")


class SynchroniserCompoundHarmonicAnalysisOfSingleExcitation(
    _6234.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation
):
    """SynchroniserCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SynchroniserCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_SynchroniserCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting SynchroniserCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "SynchroniserCompoundHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "SynchroniserCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "SynchroniserCompoundHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(
                _6234.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "SynchroniserCompoundHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6136,
            )

            return self._parent._cast(
                _6136.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "SynchroniserCompoundHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6215,
            )

            return self._parent._cast(
                _6215.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "SynchroniserCompoundHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserCompoundHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserCompoundHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def synchroniser_compound_harmonic_analysis_of_single_excitation(
            self: "SynchroniserCompoundHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "SynchroniserCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "SynchroniserCompoundHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "SynchroniserCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2600.Synchroniser":
        """mastapy.system_model.part_model.couplings.Synchroniser

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2600.Synchroniser":
        """mastapy.system_model.part_model.couplings.Synchroniser

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_6121.SynchroniserHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.SynchroniserHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6121.SynchroniserHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.SynchroniserHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SynchroniserCompoundHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_SynchroniserCompoundHarmonicAnalysisOfSingleExcitation(self)
