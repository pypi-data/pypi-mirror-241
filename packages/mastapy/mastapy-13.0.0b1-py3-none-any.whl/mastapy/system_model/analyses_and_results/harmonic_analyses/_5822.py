"""StraightBevelPlanetGearHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5816
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "StraightBevelPlanetGearHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2547
    from mastapy.system_model.analyses_and_results.system_deflections import _2817


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGearHarmonicAnalysis",)


Self = TypeVar("Self", bound="StraightBevelPlanetGearHarmonicAnalysis")


class StraightBevelPlanetGearHarmonicAnalysis(
    _5816.StraightBevelDiffGearHarmonicAnalysis
):
    """StraightBevelPlanetGearHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelPlanetGearHarmonicAnalysis"
    )

    class _Cast_StraightBevelPlanetGearHarmonicAnalysis:
        """Special nested class for casting StraightBevelPlanetGearHarmonicAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGearHarmonicAnalysis._Cast_StraightBevelPlanetGearHarmonicAnalysis",
            parent: "StraightBevelPlanetGearHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_harmonic_analysis(
            self: "StraightBevelPlanetGearHarmonicAnalysis._Cast_StraightBevelPlanetGearHarmonicAnalysis",
        ):
            return self._parent._cast(_5816.StraightBevelDiffGearHarmonicAnalysis)

        @property
        def bevel_gear_harmonic_analysis(
            self: "StraightBevelPlanetGearHarmonicAnalysis._Cast_StraightBevelPlanetGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5692,
            )

            return self._parent._cast(_5692.BevelGearHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_harmonic_analysis(
            self: "StraightBevelPlanetGearHarmonicAnalysis._Cast_StraightBevelPlanetGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5680,
            )

            return self._parent._cast(_5680.AGMAGleasonConicalGearHarmonicAnalysis)

        @property
        def conical_gear_harmonic_analysis(
            self: "StraightBevelPlanetGearHarmonicAnalysis._Cast_StraightBevelPlanetGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5709,
            )

            return self._parent._cast(_5709.ConicalGearHarmonicAnalysis)

        @property
        def gear_harmonic_analysis(
            self: "StraightBevelPlanetGearHarmonicAnalysis._Cast_StraightBevelPlanetGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5750,
            )

            return self._parent._cast(_5750.GearHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "StraightBevelPlanetGearHarmonicAnalysis._Cast_StraightBevelPlanetGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5783,
            )

            return self._parent._cast(_5783.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "StraightBevelPlanetGearHarmonicAnalysis._Cast_StraightBevelPlanetGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5702,
            )

            return self._parent._cast(_5702.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "StraightBevelPlanetGearHarmonicAnalysis._Cast_StraightBevelPlanetGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5785,
            )

            return self._parent._cast(_5785.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelPlanetGearHarmonicAnalysis._Cast_StraightBevelPlanetGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelPlanetGearHarmonicAnalysis._Cast_StraightBevelPlanetGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelPlanetGearHarmonicAnalysis._Cast_StraightBevelPlanetGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelPlanetGearHarmonicAnalysis._Cast_StraightBevelPlanetGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelPlanetGearHarmonicAnalysis._Cast_StraightBevelPlanetGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_harmonic_analysis(
            self: "StraightBevelPlanetGearHarmonicAnalysis._Cast_StraightBevelPlanetGearHarmonicAnalysis",
        ) -> "StraightBevelPlanetGearHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGearHarmonicAnalysis._Cast_StraightBevelPlanetGearHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "StraightBevelPlanetGearHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2547.StraightBevelPlanetGear":
        """mastapy.system_model.part_model.gears.StraightBevelPlanetGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2817.StraightBevelPlanetGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.StraightBevelPlanetGearSystemDeflection

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
    ) -> "StraightBevelPlanetGearHarmonicAnalysis._Cast_StraightBevelPlanetGearHarmonicAnalysis":
        return self._Cast_StraightBevelPlanetGearHarmonicAnalysis(self)
