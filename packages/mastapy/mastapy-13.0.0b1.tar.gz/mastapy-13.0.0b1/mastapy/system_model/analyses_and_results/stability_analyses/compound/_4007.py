"""StraightBevelSunGearCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _4000
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "StraightBevelSunGearCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3878


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelSunGearCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="StraightBevelSunGearCompoundStabilityAnalysis")


class StraightBevelSunGearCompoundStabilityAnalysis(
    _4000.StraightBevelDiffGearCompoundStabilityAnalysis
):
    """StraightBevelSunGearCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelSunGearCompoundStabilityAnalysis"
    )

    class _Cast_StraightBevelSunGearCompoundStabilityAnalysis:
        """Special nested class for casting StraightBevelSunGearCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelSunGearCompoundStabilityAnalysis._Cast_StraightBevelSunGearCompoundStabilityAnalysis",
            parent: "StraightBevelSunGearCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_compound_stability_analysis(
            self: "StraightBevelSunGearCompoundStabilityAnalysis._Cast_StraightBevelSunGearCompoundStabilityAnalysis",
        ):
            return self._parent._cast(
                _4000.StraightBevelDiffGearCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_compound_stability_analysis(
            self: "StraightBevelSunGearCompoundStabilityAnalysis._Cast_StraightBevelSunGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3911,
            )

            return self._parent._cast(_3911.BevelGearCompoundStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_stability_analysis(
            self: "StraightBevelSunGearCompoundStabilityAnalysis._Cast_StraightBevelSunGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3899,
            )

            return self._parent._cast(
                _3899.AGMAGleasonConicalGearCompoundStabilityAnalysis
            )

        @property
        def conical_gear_compound_stability_analysis(
            self: "StraightBevelSunGearCompoundStabilityAnalysis._Cast_StraightBevelSunGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3927,
            )

            return self._parent._cast(_3927.ConicalGearCompoundStabilityAnalysis)

        @property
        def gear_compound_stability_analysis(
            self: "StraightBevelSunGearCompoundStabilityAnalysis._Cast_StraightBevelSunGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3953,
            )

            return self._parent._cast(_3953.GearCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(
            self: "StraightBevelSunGearCompoundStabilityAnalysis._Cast_StraightBevelSunGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3972,
            )

            return self._parent._cast(_3972.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "StraightBevelSunGearCompoundStabilityAnalysis._Cast_StraightBevelSunGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3920,
            )

            return self._parent._cast(_3920.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "StraightBevelSunGearCompoundStabilityAnalysis._Cast_StraightBevelSunGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3974,
            )

            return self._parent._cast(_3974.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "StraightBevelSunGearCompoundStabilityAnalysis._Cast_StraightBevelSunGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelSunGearCompoundStabilityAnalysis._Cast_StraightBevelSunGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelSunGearCompoundStabilityAnalysis._Cast_StraightBevelSunGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def straight_bevel_sun_gear_compound_stability_analysis(
            self: "StraightBevelSunGearCompoundStabilityAnalysis._Cast_StraightBevelSunGearCompoundStabilityAnalysis",
        ) -> "StraightBevelSunGearCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelSunGearCompoundStabilityAnalysis._Cast_StraightBevelSunGearCompoundStabilityAnalysis",
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
        instance_to_wrap: "StraightBevelSunGearCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3878.StraightBevelSunGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.StraightBevelSunGearStabilityAnalysis]

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
    ) -> "List[_3878.StraightBevelSunGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.StraightBevelSunGearStabilityAnalysis]

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
    ) -> "StraightBevelSunGearCompoundStabilityAnalysis._Cast_StraightBevelSunGearCompoundStabilityAnalysis":
        return self._Cast_StraightBevelSunGearCompoundStabilityAnalysis(self)
