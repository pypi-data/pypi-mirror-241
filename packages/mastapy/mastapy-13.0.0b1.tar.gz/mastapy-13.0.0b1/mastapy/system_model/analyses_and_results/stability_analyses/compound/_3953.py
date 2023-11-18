"""GearCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3972
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "GearCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3823


__docformat__ = "restructuredtext en"
__all__ = ("GearCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="GearCompoundStabilityAnalysis")


class GearCompoundStabilityAnalysis(_3972.MountableComponentCompoundStabilityAnalysis):
    """GearCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearCompoundStabilityAnalysis")

    class _Cast_GearCompoundStabilityAnalysis:
        """Special nested class for casting GearCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
            parent: "GearCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            return self._parent._cast(_3972.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3920,
            )

            return self._parent._cast(_3920.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3974,
            )

            return self._parent._cast(_3974.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3899,
            )

            return self._parent._cast(
                _3899.AGMAGleasonConicalGearCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3906,
            )

            return self._parent._cast(
                _3906.BevelDifferentialGearCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3909,
            )

            return self._parent._cast(
                _3909.BevelDifferentialPlanetGearCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3910,
            )

            return self._parent._cast(
                _3910.BevelDifferentialSunGearCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3911,
            )

            return self._parent._cast(_3911.BevelGearCompoundStabilityAnalysis)

        @property
        def concept_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3924,
            )

            return self._parent._cast(_3924.ConceptGearCompoundStabilityAnalysis)

        @property
        def conical_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3927,
            )

            return self._parent._cast(_3927.ConicalGearCompoundStabilityAnalysis)

        @property
        def cylindrical_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3942,
            )

            return self._parent._cast(_3942.CylindricalGearCompoundStabilityAnalysis)

        @property
        def cylindrical_planet_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3945,
            )

            return self._parent._cast(
                _3945.CylindricalPlanetGearCompoundStabilityAnalysis
            )

        @property
        def face_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3948,
            )

            return self._parent._cast(_3948.FaceGearCompoundStabilityAnalysis)

        @property
        def hypoid_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3957,
            )

            return self._parent._cast(_3957.HypoidGearCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3961,
            )

            return self._parent._cast(
                _3961.KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3964,
            )

            return self._parent._cast(
                _3964.KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3967,
            )

            return self._parent._cast(
                _3967.KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3994,
            )

            return self._parent._cast(_3994.SpiralBevelGearCompoundStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4000,
            )

            return self._parent._cast(
                _4000.StraightBevelDiffGearCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4003,
            )

            return self._parent._cast(_4003.StraightBevelGearCompoundStabilityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4006,
            )

            return self._parent._cast(
                _4006.StraightBevelPlanetGearCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4007,
            )

            return self._parent._cast(
                _4007.StraightBevelSunGearCompoundStabilityAnalysis
            )

        @property
        def worm_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4018,
            )

            return self._parent._cast(_4018.WormGearCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4021,
            )

            return self._parent._cast(_4021.ZerolBevelGearCompoundStabilityAnalysis)

        @property
        def gear_compound_stability_analysis(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
        ) -> "GearCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearCompoundStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_3823.GearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.GearStabilityAnalysis]

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
    ) -> "List[_3823.GearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.GearStabilityAnalysis]

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
    ) -> "GearCompoundStabilityAnalysis._Cast_GearCompoundStabilityAnalysis":
        return self._Cast_GearCompoundStabilityAnalysis(self)
