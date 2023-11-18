"""StraightBevelGearCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3911
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "StraightBevelGearCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2545
    from mastapy.system_model.analyses_and_results.stability_analyses import _3876


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="StraightBevelGearCompoundStabilityAnalysis")


class StraightBevelGearCompoundStabilityAnalysis(
    _3911.BevelGearCompoundStabilityAnalysis
):
    """StraightBevelGearCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelGearCompoundStabilityAnalysis"
    )

    class _Cast_StraightBevelGearCompoundStabilityAnalysis:
        """Special nested class for casting StraightBevelGearCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelGearCompoundStabilityAnalysis._Cast_StraightBevelGearCompoundStabilityAnalysis",
            parent: "StraightBevelGearCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_stability_analysis(
            self: "StraightBevelGearCompoundStabilityAnalysis._Cast_StraightBevelGearCompoundStabilityAnalysis",
        ):
            return self._parent._cast(_3911.BevelGearCompoundStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_stability_analysis(
            self: "StraightBevelGearCompoundStabilityAnalysis._Cast_StraightBevelGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3899,
            )

            return self._parent._cast(
                _3899.AGMAGleasonConicalGearCompoundStabilityAnalysis
            )

        @property
        def conical_gear_compound_stability_analysis(
            self: "StraightBevelGearCompoundStabilityAnalysis._Cast_StraightBevelGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3927,
            )

            return self._parent._cast(_3927.ConicalGearCompoundStabilityAnalysis)

        @property
        def gear_compound_stability_analysis(
            self: "StraightBevelGearCompoundStabilityAnalysis._Cast_StraightBevelGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3953,
            )

            return self._parent._cast(_3953.GearCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(
            self: "StraightBevelGearCompoundStabilityAnalysis._Cast_StraightBevelGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3972,
            )

            return self._parent._cast(_3972.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "StraightBevelGearCompoundStabilityAnalysis._Cast_StraightBevelGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3920,
            )

            return self._parent._cast(_3920.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "StraightBevelGearCompoundStabilityAnalysis._Cast_StraightBevelGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3974,
            )

            return self._parent._cast(_3974.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "StraightBevelGearCompoundStabilityAnalysis._Cast_StraightBevelGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelGearCompoundStabilityAnalysis._Cast_StraightBevelGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearCompoundStabilityAnalysis._Cast_StraightBevelGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_compound_stability_analysis(
            self: "StraightBevelGearCompoundStabilityAnalysis._Cast_StraightBevelGearCompoundStabilityAnalysis",
        ) -> "StraightBevelGearCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearCompoundStabilityAnalysis._Cast_StraightBevelGearCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "StraightBevelGearCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2545.StraightBevelGear":
        """mastapy.system_model.part_model.gears.StraightBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3876.StraightBevelGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.StraightBevelGearStabilityAnalysis]

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
    ) -> "List[_3876.StraightBevelGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.StraightBevelGearStabilityAnalysis]

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
    ) -> "StraightBevelGearCompoundStabilityAnalysis._Cast_StraightBevelGearCompoundStabilityAnalysis":
        return self._Cast_StraightBevelGearCompoundStabilityAnalysis(self)
