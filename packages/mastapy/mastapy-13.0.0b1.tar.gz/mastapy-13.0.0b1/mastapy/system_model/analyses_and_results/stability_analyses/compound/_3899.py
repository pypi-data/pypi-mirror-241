"""AGMAGleasonConicalGearCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3927
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "AGMAGleasonConicalGearCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3767


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearCompoundStabilityAnalysis")


class AGMAGleasonConicalGearCompoundStabilityAnalysis(
    _3927.ConicalGearCompoundStabilityAnalysis
):
    """AGMAGleasonConicalGearCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
            parent: "AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_compound_stability_analysis(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ):
            return self._parent._cast(_3927.ConicalGearCompoundStabilityAnalysis)

        @property
        def gear_compound_stability_analysis(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3953,
            )

            return self._parent._cast(_3953.GearCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3972,
            )

            return self._parent._cast(_3972.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3920,
            )

            return self._parent._cast(_3920.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3974,
            )

            return self._parent._cast(_3974.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_compound_stability_analysis(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3906,
            )

            return self._parent._cast(
                _3906.BevelDifferentialGearCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_stability_analysis(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3909,
            )

            return self._parent._cast(
                _3909.BevelDifferentialPlanetGearCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_stability_analysis(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3910,
            )

            return self._parent._cast(
                _3910.BevelDifferentialSunGearCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_compound_stability_analysis(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3911,
            )

            return self._parent._cast(_3911.BevelGearCompoundStabilityAnalysis)

        @property
        def hypoid_gear_compound_stability_analysis(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3957,
            )

            return self._parent._cast(_3957.HypoidGearCompoundStabilityAnalysis)

        @property
        def spiral_bevel_gear_compound_stability_analysis(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3994,
            )

            return self._parent._cast(_3994.SpiralBevelGearCompoundStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_compound_stability_analysis(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4000,
            )

            return self._parent._cast(
                _4000.StraightBevelDiffGearCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_compound_stability_analysis(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4003,
            )

            return self._parent._cast(_4003.StraightBevelGearCompoundStabilityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_stability_analysis(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4006,
            )

            return self._parent._cast(
                _4006.StraightBevelPlanetGearCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_stability_analysis(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4007,
            )

            return self._parent._cast(
                _4007.StraightBevelSunGearCompoundStabilityAnalysis
            )

        @property
        def zerol_bevel_gear_compound_stability_analysis(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4021,
            )

            return self._parent._cast(_4021.ZerolBevelGearCompoundStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_stability_analysis(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
        ) -> "AGMAGleasonConicalGearCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis",
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
        instance_to_wrap: "AGMAGleasonConicalGearCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3767.AGMAGleasonConicalGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.AGMAGleasonConicalGearStabilityAnalysis]

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
    ) -> "List[_3767.AGMAGleasonConicalGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.AGMAGleasonConicalGearStabilityAnalysis]

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
    ) -> "AGMAGleasonConicalGearCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis":
        return self._Cast_AGMAGleasonConicalGearCompoundStabilityAnalysis(self)
