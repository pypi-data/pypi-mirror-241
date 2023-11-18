"""ExternalCADModelDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6299
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "ExternalCADModelDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2450
    from mastapy.system_model.analyses_and_results.static_loads import _6881


__docformat__ = "restructuredtext en"
__all__ = ("ExternalCADModelDynamicAnalysis",)


Self = TypeVar("Self", bound="ExternalCADModelDynamicAnalysis")


class ExternalCADModelDynamicAnalysis(_6299.ComponentDynamicAnalysis):
    """ExternalCADModelDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _EXTERNAL_CAD_MODEL_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ExternalCADModelDynamicAnalysis")

    class _Cast_ExternalCADModelDynamicAnalysis:
        """Special nested class for casting ExternalCADModelDynamicAnalysis to subclasses."""

        def __init__(
            self: "ExternalCADModelDynamicAnalysis._Cast_ExternalCADModelDynamicAnalysis",
            parent: "ExternalCADModelDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def component_dynamic_analysis(
            self: "ExternalCADModelDynamicAnalysis._Cast_ExternalCADModelDynamicAnalysis",
        ):
            return self._parent._cast(_6299.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "ExternalCADModelDynamicAnalysis._Cast_ExternalCADModelDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6355

            return self._parent._cast(_6355.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "ExternalCADModelDynamicAnalysis._Cast_ExternalCADModelDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ExternalCADModelDynamicAnalysis._Cast_ExternalCADModelDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ExternalCADModelDynamicAnalysis._Cast_ExternalCADModelDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ExternalCADModelDynamicAnalysis._Cast_ExternalCADModelDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ExternalCADModelDynamicAnalysis._Cast_ExternalCADModelDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ExternalCADModelDynamicAnalysis._Cast_ExternalCADModelDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def external_cad_model_dynamic_analysis(
            self: "ExternalCADModelDynamicAnalysis._Cast_ExternalCADModelDynamicAnalysis",
        ) -> "ExternalCADModelDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "ExternalCADModelDynamicAnalysis._Cast_ExternalCADModelDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ExternalCADModelDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2450.ExternalCADModel":
        """mastapy.system_model.part_model.ExternalCADModel

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6881.ExternalCADModelLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ExternalCADModelLoadCase

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
    ) -> "ExternalCADModelDynamicAnalysis._Cast_ExternalCADModelDynamicAnalysis":
        return self._Cast_ExternalCADModelDynamicAnalysis(self)
