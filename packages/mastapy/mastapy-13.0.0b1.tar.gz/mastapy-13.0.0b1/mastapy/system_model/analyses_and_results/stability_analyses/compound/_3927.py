"""ConicalGearCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3953
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "ConicalGearCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3795


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="ConicalGearCompoundStabilityAnalysis")


class ConicalGearCompoundStabilityAnalysis(_3953.GearCompoundStabilityAnalysis):
    """ConicalGearCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearCompoundStabilityAnalysis")

    class _Cast_ConicalGearCompoundStabilityAnalysis:
        """Special nested class for casting ConicalGearCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearCompoundStabilityAnalysis._Cast_ConicalGearCompoundStabilityAnalysis",
            parent: "ConicalGearCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def gear_compound_stability_analysis(
            self: "ConicalGearCompoundStabilityAnalysis._Cast_ConicalGearCompoundStabilityAnalysis",
        ):
            return self._parent._cast(_3953.GearCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(
            self: "ConicalGearCompoundStabilityAnalysis._Cast_ConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3972,
            )

            return self._parent._cast(_3972.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "ConicalGearCompoundStabilityAnalysis._Cast_ConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3920,
            )

            return self._parent._cast(_3920.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "ConicalGearCompoundStabilityAnalysis._Cast_ConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3974,
            )

            return self._parent._cast(_3974.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "ConicalGearCompoundStabilityAnalysis._Cast_ConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearCompoundStabilityAnalysis._Cast_ConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearCompoundStabilityAnalysis._Cast_ConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_stability_analysis(
            self: "ConicalGearCompoundStabilityAnalysis._Cast_ConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3899,
            )

            return self._parent._cast(
                _3899.AGMAGleasonConicalGearCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_gear_compound_stability_analysis(
            self: "ConicalGearCompoundStabilityAnalysis._Cast_ConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3906,
            )

            return self._parent._cast(
                _3906.BevelDifferentialGearCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_stability_analysis(
            self: "ConicalGearCompoundStabilityAnalysis._Cast_ConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3909,
            )

            return self._parent._cast(
                _3909.BevelDifferentialPlanetGearCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_stability_analysis(
            self: "ConicalGearCompoundStabilityAnalysis._Cast_ConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3910,
            )

            return self._parent._cast(
                _3910.BevelDifferentialSunGearCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_compound_stability_analysis(
            self: "ConicalGearCompoundStabilityAnalysis._Cast_ConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3911,
            )

            return self._parent._cast(_3911.BevelGearCompoundStabilityAnalysis)

        @property
        def hypoid_gear_compound_stability_analysis(
            self: "ConicalGearCompoundStabilityAnalysis._Cast_ConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3957,
            )

            return self._parent._cast(_3957.HypoidGearCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_stability_analysis(
            self: "ConicalGearCompoundStabilityAnalysis._Cast_ConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3961,
            )

            return self._parent._cast(
                _3961.KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_stability_analysis(
            self: "ConicalGearCompoundStabilityAnalysis._Cast_ConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3964,
            )

            return self._parent._cast(
                _3964.KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_stability_analysis(
            self: "ConicalGearCompoundStabilityAnalysis._Cast_ConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3967,
            )

            return self._parent._cast(
                _3967.KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_compound_stability_analysis(
            self: "ConicalGearCompoundStabilityAnalysis._Cast_ConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3994,
            )

            return self._parent._cast(_3994.SpiralBevelGearCompoundStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_compound_stability_analysis(
            self: "ConicalGearCompoundStabilityAnalysis._Cast_ConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4000,
            )

            return self._parent._cast(
                _4000.StraightBevelDiffGearCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_compound_stability_analysis(
            self: "ConicalGearCompoundStabilityAnalysis._Cast_ConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4003,
            )

            return self._parent._cast(_4003.StraightBevelGearCompoundStabilityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_stability_analysis(
            self: "ConicalGearCompoundStabilityAnalysis._Cast_ConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4006,
            )

            return self._parent._cast(
                _4006.StraightBevelPlanetGearCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_stability_analysis(
            self: "ConicalGearCompoundStabilityAnalysis._Cast_ConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4007,
            )

            return self._parent._cast(
                _4007.StraightBevelSunGearCompoundStabilityAnalysis
            )

        @property
        def zerol_bevel_gear_compound_stability_analysis(
            self: "ConicalGearCompoundStabilityAnalysis._Cast_ConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4021,
            )

            return self._parent._cast(_4021.ZerolBevelGearCompoundStabilityAnalysis)

        @property
        def conical_gear_compound_stability_analysis(
            self: "ConicalGearCompoundStabilityAnalysis._Cast_ConicalGearCompoundStabilityAnalysis",
        ) -> "ConicalGearCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearCompoundStabilityAnalysis._Cast_ConicalGearCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "ConicalGearCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planetaries(self: Self) -> "List[ConicalGearCompoundStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.compound.ConicalGearCompoundStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3795.ConicalGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ConicalGearStabilityAnalysis]

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
    ) -> "List[_3795.ConicalGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ConicalGearStabilityAnalysis]

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
    ) -> "ConicalGearCompoundStabilityAnalysis._Cast_ConicalGearCompoundStabilityAnalysis":
        return self._Cast_ConicalGearCompoundStabilityAnalysis(self)
