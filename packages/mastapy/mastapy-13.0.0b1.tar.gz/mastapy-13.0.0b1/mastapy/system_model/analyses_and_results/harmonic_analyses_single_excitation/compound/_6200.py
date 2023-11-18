"""HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6142,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2533
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6070,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6198,
        _6199,
    )


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation")


class HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation(
    _6142.AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
):
    """HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(
                _6142.AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6170,
            )

            return self._parent._cast(
                _6170.ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6196,
            )

            return self._parent._cast(
                _6196.GearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def specialised_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6234,
            )

            return self._parent._cast(
                _6234.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6136,
            )

            return self._parent._cast(
                _6136.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6215,
            )

            return self._parent._cast(
                _6215.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def hypoid_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2533.HypoidGearSet":
        """mastapy.system_model.part_model.gears.HypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2533.HypoidGearSet":
        """mastapy.system_model.part_model.gears.HypoidGearSet

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
    ) -> "List[_6070.HypoidGearSetHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.HypoidGearSetHarmonicAnalysisOfSingleExcitation]

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
    def hypoid_gears_compound_harmonic_analysis_of_single_excitation(
        self: Self,
    ) -> "List[_6198.HypoidGearCompoundHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.HypoidGearCompoundHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearsCompoundHarmonicAnalysisOfSingleExcitation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_meshes_compound_harmonic_analysis_of_single_excitation(
        self: Self,
    ) -> "List[_6199.HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidMeshesCompoundHarmonicAnalysisOfSingleExcitation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6070.HypoidGearSetHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.HypoidGearSetHarmonicAnalysisOfSingleExcitation]

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
    ) -> "HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation(self)
