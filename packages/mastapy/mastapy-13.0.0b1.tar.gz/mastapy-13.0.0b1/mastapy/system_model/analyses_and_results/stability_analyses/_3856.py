"""RollingRingStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3799
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "RollingRingStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2594
    from mastapy.system_model.analyses_and_results.static_loads import _6945


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingStabilityAnalysis",)


Self = TypeVar("Self", bound="RollingRingStabilityAnalysis")


class RollingRingStabilityAnalysis(_3799.CouplingHalfStabilityAnalysis):
    """RollingRingStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollingRingStabilityAnalysis")

    class _Cast_RollingRingStabilityAnalysis:
        """Special nested class for casting RollingRingStabilityAnalysis to subclasses."""

        def __init__(
            self: "RollingRingStabilityAnalysis._Cast_RollingRingStabilityAnalysis",
            parent: "RollingRingStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_stability_analysis(
            self: "RollingRingStabilityAnalysis._Cast_RollingRingStabilityAnalysis",
        ):
            return self._parent._cast(_3799.CouplingHalfStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "RollingRingStabilityAnalysis._Cast_RollingRingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3840,
            )

            return self._parent._cast(_3840.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "RollingRingStabilityAnalysis._Cast_RollingRingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3786,
            )

            return self._parent._cast(_3786.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "RollingRingStabilityAnalysis._Cast_RollingRingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3842,
            )

            return self._parent._cast(_3842.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "RollingRingStabilityAnalysis._Cast_RollingRingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RollingRingStabilityAnalysis._Cast_RollingRingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RollingRingStabilityAnalysis._Cast_RollingRingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingStabilityAnalysis._Cast_RollingRingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingStabilityAnalysis._Cast_RollingRingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def rolling_ring_stability_analysis(
            self: "RollingRingStabilityAnalysis._Cast_RollingRingStabilityAnalysis",
        ) -> "RollingRingStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "RollingRingStabilityAnalysis._Cast_RollingRingStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RollingRingStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2594.RollingRing":
        """mastapy.system_model.part_model.couplings.RollingRing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6945.RollingRingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RollingRingLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[RollingRingStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.RollingRingStabilityAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "RollingRingStabilityAnalysis._Cast_RollingRingStabilityAnalysis":
        return self._Cast_RollingRingStabilityAnalysis(self)
