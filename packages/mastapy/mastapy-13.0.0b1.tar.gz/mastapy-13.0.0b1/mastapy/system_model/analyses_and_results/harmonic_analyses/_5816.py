"""StraightBevelDiffGearHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5692
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "StraightBevelDiffGearHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2543
    from mastapy.system_model.analyses_and_results.static_loads import _6957
    from mastapy.system_model.analyses_and_results.system_deflections import _2813


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearHarmonicAnalysis",)


Self = TypeVar("Self", bound="StraightBevelDiffGearHarmonicAnalysis")


class StraightBevelDiffGearHarmonicAnalysis(_5692.BevelGearHarmonicAnalysis):
    """StraightBevelDiffGearHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearHarmonicAnalysis"
    )

    class _Cast_StraightBevelDiffGearHarmonicAnalysis:
        """Special nested class for casting StraightBevelDiffGearHarmonicAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearHarmonicAnalysis._Cast_StraightBevelDiffGearHarmonicAnalysis",
            parent: "StraightBevelDiffGearHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_harmonic_analysis(
            self: "StraightBevelDiffGearHarmonicAnalysis._Cast_StraightBevelDiffGearHarmonicAnalysis",
        ):
            return self._parent._cast(_5692.BevelGearHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_harmonic_analysis(
            self: "StraightBevelDiffGearHarmonicAnalysis._Cast_StraightBevelDiffGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5680,
            )

            return self._parent._cast(_5680.AGMAGleasonConicalGearHarmonicAnalysis)

        @property
        def conical_gear_harmonic_analysis(
            self: "StraightBevelDiffGearHarmonicAnalysis._Cast_StraightBevelDiffGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5709,
            )

            return self._parent._cast(_5709.ConicalGearHarmonicAnalysis)

        @property
        def gear_harmonic_analysis(
            self: "StraightBevelDiffGearHarmonicAnalysis._Cast_StraightBevelDiffGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5750,
            )

            return self._parent._cast(_5750.GearHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "StraightBevelDiffGearHarmonicAnalysis._Cast_StraightBevelDiffGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5783,
            )

            return self._parent._cast(_5783.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "StraightBevelDiffGearHarmonicAnalysis._Cast_StraightBevelDiffGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5702,
            )

            return self._parent._cast(_5702.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "StraightBevelDiffGearHarmonicAnalysis._Cast_StraightBevelDiffGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5785,
            )

            return self._parent._cast(_5785.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelDiffGearHarmonicAnalysis._Cast_StraightBevelDiffGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelDiffGearHarmonicAnalysis._Cast_StraightBevelDiffGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelDiffGearHarmonicAnalysis._Cast_StraightBevelDiffGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearHarmonicAnalysis._Cast_StraightBevelDiffGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearHarmonicAnalysis._Cast_StraightBevelDiffGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_harmonic_analysis(
            self: "StraightBevelDiffGearHarmonicAnalysis._Cast_StraightBevelDiffGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5822,
            )

            return self._parent._cast(_5822.StraightBevelPlanetGearHarmonicAnalysis)

        @property
        def straight_bevel_sun_gear_harmonic_analysis(
            self: "StraightBevelDiffGearHarmonicAnalysis._Cast_StraightBevelDiffGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5823,
            )

            return self._parent._cast(_5823.StraightBevelSunGearHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_harmonic_analysis(
            self: "StraightBevelDiffGearHarmonicAnalysis._Cast_StraightBevelDiffGearHarmonicAnalysis",
        ) -> "StraightBevelDiffGearHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearHarmonicAnalysis._Cast_StraightBevelDiffGearHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "StraightBevelDiffGearHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2543.StraightBevelDiffGear":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6957.StraightBevelDiffGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2813.StraightBevelDiffGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.StraightBevelDiffGearSystemDeflection

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
    ) -> "StraightBevelDiffGearHarmonicAnalysis._Cast_StraightBevelDiffGearHarmonicAnalysis":
        return self._Cast_StraightBevelDiffGearHarmonicAnalysis(self)
