"""PowerLoadStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3888
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "PowerLoadStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2470
    from mastapy.system_model.analyses_and_results.static_loads import _6937


__docformat__ = "restructuredtext en"
__all__ = ("PowerLoadStabilityAnalysis",)


Self = TypeVar("Self", bound="PowerLoadStabilityAnalysis")


class PowerLoadStabilityAnalysis(_3888.VirtualComponentStabilityAnalysis):
    """PowerLoadStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _POWER_LOAD_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PowerLoadStabilityAnalysis")

    class _Cast_PowerLoadStabilityAnalysis:
        """Special nested class for casting PowerLoadStabilityAnalysis to subclasses."""

        def __init__(
            self: "PowerLoadStabilityAnalysis._Cast_PowerLoadStabilityAnalysis",
            parent: "PowerLoadStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_stability_analysis(
            self: "PowerLoadStabilityAnalysis._Cast_PowerLoadStabilityAnalysis",
        ):
            return self._parent._cast(_3888.VirtualComponentStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "PowerLoadStabilityAnalysis._Cast_PowerLoadStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3840,
            )

            return self._parent._cast(_3840.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "PowerLoadStabilityAnalysis._Cast_PowerLoadStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3786,
            )

            return self._parent._cast(_3786.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "PowerLoadStabilityAnalysis._Cast_PowerLoadStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3842,
            )

            return self._parent._cast(_3842.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PowerLoadStabilityAnalysis._Cast_PowerLoadStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PowerLoadStabilityAnalysis._Cast_PowerLoadStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PowerLoadStabilityAnalysis._Cast_PowerLoadStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PowerLoadStabilityAnalysis._Cast_PowerLoadStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PowerLoadStabilityAnalysis._Cast_PowerLoadStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def power_load_stability_analysis(
            self: "PowerLoadStabilityAnalysis._Cast_PowerLoadStabilityAnalysis",
        ) -> "PowerLoadStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "PowerLoadStabilityAnalysis._Cast_PowerLoadStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PowerLoadStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2470.PowerLoad":
        """mastapy.system_model.part_model.PowerLoad

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6937.PowerLoadLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PowerLoadLoadCase

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
    ) -> "PowerLoadStabilityAnalysis._Cast_PowerLoadStabilityAnalysis":
        return self._Cast_PowerLoadStabilityAnalysis(self)
