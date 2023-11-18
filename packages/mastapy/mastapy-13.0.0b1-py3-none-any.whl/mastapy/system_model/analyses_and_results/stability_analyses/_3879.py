"""SynchroniserHalfStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3880
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "SynchroniserHalfStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2602
    from mastapy.system_model.analyses_and_results.static_loads import _6965


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserHalfStabilityAnalysis",)


Self = TypeVar("Self", bound="SynchroniserHalfStabilityAnalysis")


class SynchroniserHalfStabilityAnalysis(_3880.SynchroniserPartStabilityAnalysis):
    """SynchroniserHalfStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_HALF_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserHalfStabilityAnalysis")

    class _Cast_SynchroniserHalfStabilityAnalysis:
        """Special nested class for casting SynchroniserHalfStabilityAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserHalfStabilityAnalysis._Cast_SynchroniserHalfStabilityAnalysis",
            parent: "SynchroniserHalfStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def synchroniser_part_stability_analysis(
            self: "SynchroniserHalfStabilityAnalysis._Cast_SynchroniserHalfStabilityAnalysis",
        ):
            return self._parent._cast(_3880.SynchroniserPartStabilityAnalysis)

        @property
        def coupling_half_stability_analysis(
            self: "SynchroniserHalfStabilityAnalysis._Cast_SynchroniserHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3799,
            )

            return self._parent._cast(_3799.CouplingHalfStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "SynchroniserHalfStabilityAnalysis._Cast_SynchroniserHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3840,
            )

            return self._parent._cast(_3840.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "SynchroniserHalfStabilityAnalysis._Cast_SynchroniserHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3786,
            )

            return self._parent._cast(_3786.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "SynchroniserHalfStabilityAnalysis._Cast_SynchroniserHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3842,
            )

            return self._parent._cast(_3842.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserHalfStabilityAnalysis._Cast_SynchroniserHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserHalfStabilityAnalysis._Cast_SynchroniserHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserHalfStabilityAnalysis._Cast_SynchroniserHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserHalfStabilityAnalysis._Cast_SynchroniserHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserHalfStabilityAnalysis._Cast_SynchroniserHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def synchroniser_half_stability_analysis(
            self: "SynchroniserHalfStabilityAnalysis._Cast_SynchroniserHalfStabilityAnalysis",
        ) -> "SynchroniserHalfStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserHalfStabilityAnalysis._Cast_SynchroniserHalfStabilityAnalysis",
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
        self: Self, instance_to_wrap: "SynchroniserHalfStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2602.SynchroniserHalf":
        """mastapy.system_model.part_model.couplings.SynchroniserHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6965.SynchroniserHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserHalfLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SynchroniserHalfStabilityAnalysis._Cast_SynchroniserHalfStabilityAnalysis":
        return self._Cast_SynchroniserHalfStabilityAnalysis(self)
