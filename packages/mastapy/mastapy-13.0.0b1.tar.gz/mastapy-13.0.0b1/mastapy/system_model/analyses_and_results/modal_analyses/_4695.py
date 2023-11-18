"""SynchroniserModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4679
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "SynchroniserModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2600
    from mastapy.system_model.analyses_and_results.static_loads import _6966
    from mastapy.system_model.analyses_and_results.system_deflections import _2822


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserModalAnalysis",)


Self = TypeVar("Self", bound="SynchroniserModalAnalysis")


class SynchroniserModalAnalysis(_4679.SpecialisedAssemblyModalAnalysis):
    """SynchroniserModalAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserModalAnalysis")

    class _Cast_SynchroniserModalAnalysis:
        """Special nested class for casting SynchroniserModalAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserModalAnalysis._Cast_SynchroniserModalAnalysis",
            parent: "SynchroniserModalAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_modal_analysis(
            self: "SynchroniserModalAnalysis._Cast_SynchroniserModalAnalysis",
        ):
            return self._parent._cast(_4679.SpecialisedAssemblyModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "SynchroniserModalAnalysis._Cast_SynchroniserModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4569

            return self._parent._cast(_4569.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(
            self: "SynchroniserModalAnalysis._Cast_SynchroniserModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4659

            return self._parent._cast(_4659.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserModalAnalysis._Cast_SynchroniserModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserModalAnalysis._Cast_SynchroniserModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserModalAnalysis._Cast_SynchroniserModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserModalAnalysis._Cast_SynchroniserModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserModalAnalysis._Cast_SynchroniserModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def synchroniser_modal_analysis(
            self: "SynchroniserModalAnalysis._Cast_SynchroniserModalAnalysis",
        ) -> "SynchroniserModalAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserModalAnalysis._Cast_SynchroniserModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SynchroniserModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2600.Synchroniser":
        """mastapy.system_model.part_model.couplings.Synchroniser

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6966.SynchroniserLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2822.SynchroniserSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.SynchroniserSystemDeflection

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
    ) -> "SynchroniserModalAnalysis._Cast_SynchroniserModalAnalysis":
        return self._Cast_SynchroniserModalAnalysis(self)
