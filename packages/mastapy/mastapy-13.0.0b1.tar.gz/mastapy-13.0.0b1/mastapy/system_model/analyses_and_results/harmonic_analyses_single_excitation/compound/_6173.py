"""CouplingCompoundHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6234,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "CouplingCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6044,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CouplingCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="CouplingCompoundHarmonicAnalysisOfSingleExcitation")


class CouplingCompoundHarmonicAnalysisOfSingleExcitation(
    _6234.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation
):
    """CouplingCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _COUPLING_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingCompoundHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_CouplingCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting CouplingCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "CouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "CouplingCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "CouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(
                _6234.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "CouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6136,
            )

            return self._parent._cast(
                _6136.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "CouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6215,
            )

            return self._parent._cast(
                _6215.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "CouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def clutch_compound_harmonic_analysis_of_single_excitation(
            self: "CouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6157,
            )

            return self._parent._cast(
                _6157.ClutchCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_compound_harmonic_analysis_of_single_excitation(
            self: "CouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6162,
            )

            return self._parent._cast(
                _6162.ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_compound_harmonic_analysis_of_single_excitation(
            self: "CouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6216,
            )

            return self._parent._cast(
                _6216.PartToPartShearCouplingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_compound_harmonic_analysis_of_single_excitation(
            self: "CouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6238,
            )

            return self._parent._cast(
                _6238.SpringDamperCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_compound_harmonic_analysis_of_single_excitation(
            self: "CouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6253,
            )

            return self._parent._cast(
                _6253.TorqueConverterCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_compound_harmonic_analysis_of_single_excitation(
            self: "CouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "CouplingCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "CouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "CouplingCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6044.CouplingHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.CouplingHarmonicAnalysisOfSingleExcitation]

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
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_6044.CouplingHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.CouplingHarmonicAnalysisOfSingleExcitation]

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
    def cast_to(
        self: Self,
    ) -> "CouplingCompoundHarmonicAnalysisOfSingleExcitation._Cast_CouplingCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_CouplingCompoundHarmonicAnalysisOfSingleExcitation(self)
