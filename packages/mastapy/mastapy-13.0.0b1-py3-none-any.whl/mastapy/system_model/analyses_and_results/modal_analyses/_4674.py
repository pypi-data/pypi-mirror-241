"""RootAssemblyModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4576
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "RootAssemblyModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2472
    from mastapy.system_model.analyses_and_results.modal_analyses import _4651
    from mastapy.system_model.analyses_and_results.system_deflections import _2798


__docformat__ = "restructuredtext en"
__all__ = ("RootAssemblyModalAnalysis",)


Self = TypeVar("Self", bound="RootAssemblyModalAnalysis")


class RootAssemblyModalAnalysis(_4576.AssemblyModalAnalysis):
    """RootAssemblyModalAnalysis

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RootAssemblyModalAnalysis")

    class _Cast_RootAssemblyModalAnalysis:
        """Special nested class for casting RootAssemblyModalAnalysis to subclasses."""

        def __init__(
            self: "RootAssemblyModalAnalysis._Cast_RootAssemblyModalAnalysis",
            parent: "RootAssemblyModalAnalysis",
        ):
            self._parent = parent

        @property
        def assembly_modal_analysis(
            self: "RootAssemblyModalAnalysis._Cast_RootAssemblyModalAnalysis",
        ):
            return self._parent._cast(_4576.AssemblyModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "RootAssemblyModalAnalysis._Cast_RootAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4569

            return self._parent._cast(_4569.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(
            self: "RootAssemblyModalAnalysis._Cast_RootAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4659

            return self._parent._cast(_4659.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "RootAssemblyModalAnalysis._Cast_RootAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RootAssemblyModalAnalysis._Cast_RootAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RootAssemblyModalAnalysis._Cast_RootAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RootAssemblyModalAnalysis._Cast_RootAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RootAssemblyModalAnalysis._Cast_RootAssemblyModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def root_assembly_modal_analysis(
            self: "RootAssemblyModalAnalysis._Cast_RootAssemblyModalAnalysis",
        ) -> "RootAssemblyModalAnalysis":
            return self._parent

        def __getattr__(
            self: "RootAssemblyModalAnalysis._Cast_RootAssemblyModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RootAssemblyModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2472.RootAssembly":
        """mastapy.system_model.part_model.RootAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def modal_analysis_inputs(self: Self) -> "_4651.ModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ModalAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModalAnalysisInputs

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2798.RootAssemblySystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.RootAssemblySystemDeflection

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
    ) -> "RootAssemblyModalAnalysis._Cast_RootAssemblyModalAnalysis":
        return self._Cast_RootAssemblyModalAnalysis(self)
