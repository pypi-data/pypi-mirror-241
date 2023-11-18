"""SynchroniserSleeveModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4696
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "SynchroniserSleeveModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2604
    from mastapy.system_model.analyses_and_results.static_loads import _6968
    from mastapy.system_model.analyses_and_results.system_deflections import _2821


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserSleeveModalAnalysis",)


Self = TypeVar("Self", bound="SynchroniserSleeveModalAnalysis")


class SynchroniserSleeveModalAnalysis(_4696.SynchroniserPartModalAnalysis):
    """SynchroniserSleeveModalAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserSleeveModalAnalysis")

    class _Cast_SynchroniserSleeveModalAnalysis:
        """Special nested class for casting SynchroniserSleeveModalAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserSleeveModalAnalysis._Cast_SynchroniserSleeveModalAnalysis",
            parent: "SynchroniserSleeveModalAnalysis",
        ):
            self._parent = parent

        @property
        def synchroniser_part_modal_analysis(
            self: "SynchroniserSleeveModalAnalysis._Cast_SynchroniserSleeveModalAnalysis",
        ):
            return self._parent._cast(_4696.SynchroniserPartModalAnalysis)

        @property
        def coupling_half_modal_analysis(
            self: "SynchroniserSleeveModalAnalysis._Cast_SynchroniserSleeveModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4608

            return self._parent._cast(_4608.CouplingHalfModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "SynchroniserSleeveModalAnalysis._Cast_SynchroniserSleeveModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4655

            return self._parent._cast(_4655.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "SynchroniserSleeveModalAnalysis._Cast_SynchroniserSleeveModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4594

            return self._parent._cast(_4594.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "SynchroniserSleeveModalAnalysis._Cast_SynchroniserSleeveModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4659

            return self._parent._cast(_4659.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserSleeveModalAnalysis._Cast_SynchroniserSleeveModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserSleeveModalAnalysis._Cast_SynchroniserSleeveModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserSleeveModalAnalysis._Cast_SynchroniserSleeveModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserSleeveModalAnalysis._Cast_SynchroniserSleeveModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserSleeveModalAnalysis._Cast_SynchroniserSleeveModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def synchroniser_sleeve_modal_analysis(
            self: "SynchroniserSleeveModalAnalysis._Cast_SynchroniserSleeveModalAnalysis",
        ) -> "SynchroniserSleeveModalAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserSleeveModalAnalysis._Cast_SynchroniserSleeveModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SynchroniserSleeveModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2604.SynchroniserSleeve":
        """mastapy.system_model.part_model.couplings.SynchroniserSleeve

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6968.SynchroniserSleeveLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2821.SynchroniserSleeveSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.SynchroniserSleeveSystemDeflection

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
    ) -> "SynchroniserSleeveModalAnalysis._Cast_SynchroniserSleeveModalAnalysis":
        return self._Cast_SynchroniserSleeveModalAnalysis(self)
