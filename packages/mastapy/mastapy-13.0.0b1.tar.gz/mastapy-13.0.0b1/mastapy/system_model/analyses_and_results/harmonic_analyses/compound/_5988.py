"""StraightBevelSunGearCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5981
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "StraightBevelSunGearCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5823


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelSunGearCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="StraightBevelSunGearCompoundHarmonicAnalysis")


class StraightBevelSunGearCompoundHarmonicAnalysis(
    _5981.StraightBevelDiffGearCompoundHarmonicAnalysis
):
    """StraightBevelSunGearCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelSunGearCompoundHarmonicAnalysis"
    )

    class _Cast_StraightBevelSunGearCompoundHarmonicAnalysis:
        """Special nested class for casting StraightBevelSunGearCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelSunGearCompoundHarmonicAnalysis._Cast_StraightBevelSunGearCompoundHarmonicAnalysis",
            parent: "StraightBevelSunGearCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_compound_harmonic_analysis(
            self: "StraightBevelSunGearCompoundHarmonicAnalysis._Cast_StraightBevelSunGearCompoundHarmonicAnalysis",
        ):
            return self._parent._cast(
                _5981.StraightBevelDiffGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_gear_compound_harmonic_analysis(
            self: "StraightBevelSunGearCompoundHarmonicAnalysis._Cast_StraightBevelSunGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5892,
            )

            return self._parent._cast(_5892.BevelGearCompoundHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_compound_harmonic_analysis(
            self: "StraightBevelSunGearCompoundHarmonicAnalysis._Cast_StraightBevelSunGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5880,
            )

            return self._parent._cast(
                _5880.AGMAGleasonConicalGearCompoundHarmonicAnalysis
            )

        @property
        def conical_gear_compound_harmonic_analysis(
            self: "StraightBevelSunGearCompoundHarmonicAnalysis._Cast_StraightBevelSunGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5908,
            )

            return self._parent._cast(_5908.ConicalGearCompoundHarmonicAnalysis)

        @property
        def gear_compound_harmonic_analysis(
            self: "StraightBevelSunGearCompoundHarmonicAnalysis._Cast_StraightBevelSunGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5934,
            )

            return self._parent._cast(_5934.GearCompoundHarmonicAnalysis)

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "StraightBevelSunGearCompoundHarmonicAnalysis._Cast_StraightBevelSunGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5953,
            )

            return self._parent._cast(_5953.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "StraightBevelSunGearCompoundHarmonicAnalysis._Cast_StraightBevelSunGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5901,
            )

            return self._parent._cast(_5901.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "StraightBevelSunGearCompoundHarmonicAnalysis._Cast_StraightBevelSunGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5955,
            )

            return self._parent._cast(_5955.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "StraightBevelSunGearCompoundHarmonicAnalysis._Cast_StraightBevelSunGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelSunGearCompoundHarmonicAnalysis._Cast_StraightBevelSunGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelSunGearCompoundHarmonicAnalysis._Cast_StraightBevelSunGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def straight_bevel_sun_gear_compound_harmonic_analysis(
            self: "StraightBevelSunGearCompoundHarmonicAnalysis._Cast_StraightBevelSunGearCompoundHarmonicAnalysis",
        ) -> "StraightBevelSunGearCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelSunGearCompoundHarmonicAnalysis._Cast_StraightBevelSunGearCompoundHarmonicAnalysis",
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
        instance_to_wrap: "StraightBevelSunGearCompoundHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5823.StraightBevelSunGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.StraightBevelSunGearHarmonicAnalysis]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5823.StraightBevelSunGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.StraightBevelSunGearHarmonicAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "StraightBevelSunGearCompoundHarmonicAnalysis._Cast_StraightBevelSunGearCompoundHarmonicAnalysis":
        return self._Cast_StraightBevelSunGearCompoundHarmonicAnalysis(self)
