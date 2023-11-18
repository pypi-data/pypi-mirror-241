"""GuideDxfModelModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "GuideDxfModelModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2453
    from mastapy.system_model.analyses_and_results.static_loads import _6894
    from mastapy.system_model.analyses_and_results.system_deflections import _2760


__docformat__ = "restructuredtext en"
__all__ = ("GuideDxfModelModalAnalysis",)


Self = TypeVar("Self", bound="GuideDxfModelModalAnalysis")


class GuideDxfModelModalAnalysis(_4594.ComponentModalAnalysis):
    """GuideDxfModelModalAnalysis

    This is a mastapy class.
    """

    TYPE = _GUIDE_DXF_MODEL_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GuideDxfModelModalAnalysis")

    class _Cast_GuideDxfModelModalAnalysis:
        """Special nested class for casting GuideDxfModelModalAnalysis to subclasses."""

        def __init__(
            self: "GuideDxfModelModalAnalysis._Cast_GuideDxfModelModalAnalysis",
            parent: "GuideDxfModelModalAnalysis",
        ):
            self._parent = parent

        @property
        def component_modal_analysis(
            self: "GuideDxfModelModalAnalysis._Cast_GuideDxfModelModalAnalysis",
        ):
            return self._parent._cast(_4594.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "GuideDxfModelModalAnalysis._Cast_GuideDxfModelModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4659

            return self._parent._cast(_4659.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "GuideDxfModelModalAnalysis._Cast_GuideDxfModelModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GuideDxfModelModalAnalysis._Cast_GuideDxfModelModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GuideDxfModelModalAnalysis._Cast_GuideDxfModelModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GuideDxfModelModalAnalysis._Cast_GuideDxfModelModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GuideDxfModelModalAnalysis._Cast_GuideDxfModelModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def guide_dxf_model_modal_analysis(
            self: "GuideDxfModelModalAnalysis._Cast_GuideDxfModelModalAnalysis",
        ) -> "GuideDxfModelModalAnalysis":
            return self._parent

        def __getattr__(
            self: "GuideDxfModelModalAnalysis._Cast_GuideDxfModelModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GuideDxfModelModalAnalysis.TYPE"):
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
    def system_deflection_results(self: Self) -> "_2760.GuideDxfModelSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.GuideDxfModelSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "GuideDxfModelModalAnalysis._Cast_GuideDxfModelModalAnalysis":
        return self._Cast_GuideDxfModelModalAnalysis(self)
