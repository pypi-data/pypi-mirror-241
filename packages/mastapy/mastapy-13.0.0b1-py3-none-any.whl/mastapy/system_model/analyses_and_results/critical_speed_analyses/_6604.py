"""GuideDxfModelCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6565
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "GuideDxfModelCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2453
    from mastapy.system_model.analyses_and_results.static_loads import _6894


__docformat__ = "restructuredtext en"
__all__ = ("GuideDxfModelCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="GuideDxfModelCriticalSpeedAnalysis")


class GuideDxfModelCriticalSpeedAnalysis(_6565.ComponentCriticalSpeedAnalysis):
    """GuideDxfModelCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _GUIDE_DXF_MODEL_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GuideDxfModelCriticalSpeedAnalysis")

    class _Cast_GuideDxfModelCriticalSpeedAnalysis:
        """Special nested class for casting GuideDxfModelCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "GuideDxfModelCriticalSpeedAnalysis._Cast_GuideDxfModelCriticalSpeedAnalysis",
            parent: "GuideDxfModelCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def component_critical_speed_analysis(
            self: "GuideDxfModelCriticalSpeedAnalysis._Cast_GuideDxfModelCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6565.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "GuideDxfModelCriticalSpeedAnalysis._Cast_GuideDxfModelCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6622,
            )

            return self._parent._cast(_6622.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "GuideDxfModelCriticalSpeedAnalysis._Cast_GuideDxfModelCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GuideDxfModelCriticalSpeedAnalysis._Cast_GuideDxfModelCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GuideDxfModelCriticalSpeedAnalysis._Cast_GuideDxfModelCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GuideDxfModelCriticalSpeedAnalysis._Cast_GuideDxfModelCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GuideDxfModelCriticalSpeedAnalysis._Cast_GuideDxfModelCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def guide_dxf_model_critical_speed_analysis(
            self: "GuideDxfModelCriticalSpeedAnalysis._Cast_GuideDxfModelCriticalSpeedAnalysis",
        ) -> "GuideDxfModelCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "GuideDxfModelCriticalSpeedAnalysis._Cast_GuideDxfModelCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "GuideDxfModelCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2453.GuideDxfModel":
        """mastapy.system_model.part_model.GuideDxfModel

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6894.GuideDxfModelLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.GuideDxfModelLoadCase

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
    ) -> "GuideDxfModelCriticalSpeedAnalysis._Cast_GuideDxfModelCriticalSpeedAnalysis":
        return self._Cast_GuideDxfModelCriticalSpeedAnalysis(self)
