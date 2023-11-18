"""GuideDxfModelDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6299
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "GuideDxfModelDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2453
    from mastapy.system_model.analyses_and_results.static_loads import _6894


__docformat__ = "restructuredtext en"
__all__ = ("GuideDxfModelDynamicAnalysis",)


Self = TypeVar("Self", bound="GuideDxfModelDynamicAnalysis")


class GuideDxfModelDynamicAnalysis(_6299.ComponentDynamicAnalysis):
    """GuideDxfModelDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _GUIDE_DXF_MODEL_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GuideDxfModelDynamicAnalysis")

    class _Cast_GuideDxfModelDynamicAnalysis:
        """Special nested class for casting GuideDxfModelDynamicAnalysis to subclasses."""

        def __init__(
            self: "GuideDxfModelDynamicAnalysis._Cast_GuideDxfModelDynamicAnalysis",
            parent: "GuideDxfModelDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def component_dynamic_analysis(
            self: "GuideDxfModelDynamicAnalysis._Cast_GuideDxfModelDynamicAnalysis",
        ):
            return self._parent._cast(_6299.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "GuideDxfModelDynamicAnalysis._Cast_GuideDxfModelDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6355

            return self._parent._cast(_6355.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "GuideDxfModelDynamicAnalysis._Cast_GuideDxfModelDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "GuideDxfModelDynamicAnalysis._Cast_GuideDxfModelDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GuideDxfModelDynamicAnalysis._Cast_GuideDxfModelDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GuideDxfModelDynamicAnalysis._Cast_GuideDxfModelDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GuideDxfModelDynamicAnalysis._Cast_GuideDxfModelDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GuideDxfModelDynamicAnalysis._Cast_GuideDxfModelDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def guide_dxf_model_dynamic_analysis(
            self: "GuideDxfModelDynamicAnalysis._Cast_GuideDxfModelDynamicAnalysis",
        ) -> "GuideDxfModelDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "GuideDxfModelDynamicAnalysis._Cast_GuideDxfModelDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GuideDxfModelDynamicAnalysis.TYPE"):
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
    ) -> "GuideDxfModelDynamicAnalysis._Cast_GuideDxfModelDynamicAnalysis":
        return self._Cast_GuideDxfModelDynamicAnalysis(self)
