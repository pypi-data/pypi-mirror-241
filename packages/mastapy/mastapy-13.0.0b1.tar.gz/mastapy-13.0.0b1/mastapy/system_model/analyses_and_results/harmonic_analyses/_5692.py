"""BevelGearHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5680
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "BevelGearHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2517
    from mastapy.system_model.analyses_and_results.system_deflections import _2706


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearHarmonicAnalysis",)


Self = TypeVar("Self", bound="BevelGearHarmonicAnalysis")


class BevelGearHarmonicAnalysis(_5680.AGMAGleasonConicalGearHarmonicAnalysis):
    """BevelGearHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearHarmonicAnalysis")

    class _Cast_BevelGearHarmonicAnalysis:
        """Special nested class for casting BevelGearHarmonicAnalysis to subclasses."""

        def __init__(
            self: "BevelGearHarmonicAnalysis._Cast_BevelGearHarmonicAnalysis",
            parent: "BevelGearHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_harmonic_analysis(
            self: "BevelGearHarmonicAnalysis._Cast_BevelGearHarmonicAnalysis",
        ):
            return self._parent._cast(_5680.AGMAGleasonConicalGearHarmonicAnalysis)

        @property
        def conical_gear_harmonic_analysis(
            self: "BevelGearHarmonicAnalysis._Cast_BevelGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5709,
            )

            return self._parent._cast(_5709.ConicalGearHarmonicAnalysis)

        @property
        def gear_harmonic_analysis(
            self: "BevelGearHarmonicAnalysis._Cast_BevelGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5750,
            )

            return self._parent._cast(_5750.GearHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "BevelGearHarmonicAnalysis._Cast_BevelGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5783,
            )

            return self._parent._cast(_5783.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "BevelGearHarmonicAnalysis._Cast_BevelGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5702,
            )

            return self._parent._cast(_5702.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "BevelGearHarmonicAnalysis._Cast_BevelGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5785,
            )

            return self._parent._cast(_5785.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelGearHarmonicAnalysis._Cast_BevelGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelGearHarmonicAnalysis._Cast_BevelGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelGearHarmonicAnalysis._Cast_BevelGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearHarmonicAnalysis._Cast_BevelGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearHarmonicAnalysis._Cast_BevelGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_harmonic_analysis(
            self: "BevelGearHarmonicAnalysis._Cast_BevelGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5687,
            )

            return self._parent._cast(_5687.BevelDifferentialGearHarmonicAnalysis)

        @property
        def bevel_differential_planet_gear_harmonic_analysis(
            self: "BevelGearHarmonicAnalysis._Cast_BevelGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5690,
            )

            return self._parent._cast(_5690.BevelDifferentialPlanetGearHarmonicAnalysis)

        @property
        def bevel_differential_sun_gear_harmonic_analysis(
            self: "BevelGearHarmonicAnalysis._Cast_BevelGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5691,
            )

            return self._parent._cast(_5691.BevelDifferentialSunGearHarmonicAnalysis)

        @property
        def spiral_bevel_gear_harmonic_analysis(
            self: "BevelGearHarmonicAnalysis._Cast_BevelGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5809,
            )

            return self._parent._cast(_5809.SpiralBevelGearHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_harmonic_analysis(
            self: "BevelGearHarmonicAnalysis._Cast_BevelGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5816,
            )

            return self._parent._cast(_5816.StraightBevelDiffGearHarmonicAnalysis)

        @property
        def straight_bevel_gear_harmonic_analysis(
            self: "BevelGearHarmonicAnalysis._Cast_BevelGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5819,
            )

            return self._parent._cast(_5819.StraightBevelGearHarmonicAnalysis)

        @property
        def straight_bevel_planet_gear_harmonic_analysis(
            self: "BevelGearHarmonicAnalysis._Cast_BevelGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5822,
            )

            return self._parent._cast(_5822.StraightBevelPlanetGearHarmonicAnalysis)

        @property
        def straight_bevel_sun_gear_harmonic_analysis(
            self: "BevelGearHarmonicAnalysis._Cast_BevelGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5823,
            )

            return self._parent._cast(_5823.StraightBevelSunGearHarmonicAnalysis)

        @property
        def zerol_bevel_gear_harmonic_analysis(
            self: "BevelGearHarmonicAnalysis._Cast_BevelGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5838,
            )

            return self._parent._cast(_5838.ZerolBevelGearHarmonicAnalysis)

        @property
        def bevel_gear_harmonic_analysis(
            self: "BevelGearHarmonicAnalysis._Cast_BevelGearHarmonicAnalysis",
        ) -> "BevelGearHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearHarmonicAnalysis._Cast_BevelGearHarmonicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2517.BevelGear":
        """mastapy.system_model.part_model.gears.BevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2706.BevelGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.BevelGearSystemDeflection

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
    ) -> "BevelGearHarmonicAnalysis._Cast_BevelGearHarmonicAnalysis":
        return self._Cast_BevelGearHarmonicAnalysis(self)
