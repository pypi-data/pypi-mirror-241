"""ConicalGearSetCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5936
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "ConicalGearSetCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5711


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="ConicalGearSetCompoundHarmonicAnalysis")


class ConicalGearSetCompoundHarmonicAnalysis(_5936.GearSetCompoundHarmonicAnalysis):
    """ConicalGearSetCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearSetCompoundHarmonicAnalysis"
    )

    class _Cast_ConicalGearSetCompoundHarmonicAnalysis:
        """Special nested class for casting ConicalGearSetCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
            parent: "ConicalGearSetCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_compound_harmonic_analysis(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
        ):
            return self._parent._cast(_5936.GearSetCompoundHarmonicAnalysis)

        @property
        def specialised_assembly_compound_harmonic_analysis(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5974,
            )

            return self._parent._cast(_5974.SpecialisedAssemblyCompoundHarmonicAnalysis)

        @property
        def abstract_assembly_compound_harmonic_analysis(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5876,
            )

            return self._parent._cast(_5876.AbstractAssemblyCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5955,
            )

            return self._parent._cast(_5955.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_harmonic_analysis(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5882,
            )

            return self._parent._cast(
                _5882.AGMAGleasonConicalGearSetCompoundHarmonicAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_harmonic_analysis(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5889,
            )

            return self._parent._cast(
                _5889.BevelDifferentialGearSetCompoundHarmonicAnalysis
            )

        @property
        def bevel_gear_set_compound_harmonic_analysis(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5894,
            )

            return self._parent._cast(_5894.BevelGearSetCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_set_compound_harmonic_analysis(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5940,
            )

            return self._parent._cast(_5940.HypoidGearSetCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_harmonic_analysis(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5944,
            )

            return self._parent._cast(
                _5944.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_harmonic_analysis(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5947,
            )

            return self._parent._cast(
                _5947.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_harmonic_analysis(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5950,
            )

            return self._parent._cast(
                _5950.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_harmonic_analysis(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5977,
            )

            return self._parent._cast(_5977.SpiralBevelGearSetCompoundHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_harmonic_analysis(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5983,
            )

            return self._parent._cast(
                _5983.StraightBevelDiffGearSetCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_harmonic_analysis(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5986,
            )

            return self._parent._cast(
                _5986.StraightBevelGearSetCompoundHarmonicAnalysis
            )

        @property
        def zerol_bevel_gear_set_compound_harmonic_analysis(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6004,
            )

            return self._parent._cast(_6004.ZerolBevelGearSetCompoundHarmonicAnalysis)

        @property
        def conical_gear_set_compound_harmonic_analysis(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
        ) -> "ConicalGearSetCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "ConicalGearSetCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5711.ConicalGearSetHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ConicalGearSetHarmonicAnalysis]

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
    ) -> "List[_5711.ConicalGearSetHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ConicalGearSetHarmonicAnalysis]

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
    ) -> "ConicalGearSetCompoundHarmonicAnalysis._Cast_ConicalGearSetCompoundHarmonicAnalysis":
        return self._Cast_ConicalGearSetCompoundHarmonicAnalysis(self)
