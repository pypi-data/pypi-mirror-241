"""AGMAGleasonConicalGearSetStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3794
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "AGMAGleasonConicalGearSetStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2512


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetStabilityAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetStabilityAnalysis")


class AGMAGleasonConicalGearSetStabilityAnalysis(_3794.ConicalGearSetStabilityAnalysis):
    """AGMAGleasonConicalGearSetStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearSetStabilityAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearSetStabilityAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearSetStabilityAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis",
            parent: "AGMAGleasonConicalGearSetStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_set_stability_analysis(
            self: "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis",
        ):
            return self._parent._cast(_3794.ConicalGearSetStabilityAnalysis)

        @property
        def gear_set_stability_analysis(
            self: "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3822,
            )

            return self._parent._cast(_3822.GearSetStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(
            self: "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3861,
            )

            return self._parent._cast(_3861.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3761,
            )

            return self._parent._cast(_3761.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3842,
            )

            return self._parent._cast(_3842.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_stability_analysis(
            self: "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3773,
            )

            return self._parent._cast(_3773.BevelDifferentialGearSetStabilityAnalysis)

        @property
        def bevel_gear_set_stability_analysis(
            self: "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3778,
            )

            return self._parent._cast(_3778.BevelGearSetStabilityAnalysis)

        @property
        def hypoid_gear_set_stability_analysis(
            self: "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3826,
            )

            return self._parent._cast(_3826.HypoidGearSetStabilityAnalysis)

        @property
        def spiral_bevel_gear_set_stability_analysis(
            self: "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3863,
            )

            return self._parent._cast(_3863.SpiralBevelGearSetStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_set_stability_analysis(
            self: "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3872,
            )

            return self._parent._cast(_3872.StraightBevelDiffGearSetStabilityAnalysis)

        @property
        def straight_bevel_gear_set_stability_analysis(
            self: "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3875,
            )

            return self._parent._cast(_3875.StraightBevelGearSetStabilityAnalysis)

        @property
        def zerol_bevel_gear_set_stability_analysis(
            self: "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3893,
            )

            return self._parent._cast(_3893.ZerolBevelGearSetStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_set_stability_analysis(
            self: "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis",
        ) -> "AGMAGleasonConicalGearSetStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearSetStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2512.AGMAGleasonConicalGearSet":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearSetStabilityAnalysis._Cast_AGMAGleasonConicalGearSetStabilityAnalysis":
        return self._Cast_AGMAGleasonConicalGearSetStabilityAnalysis(self)
