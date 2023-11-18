"""SynchroniserPartModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4608
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "SynchroniserPartModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2603
    from mastapy.system_model.analyses_and_results.system_deflections import _2820


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartModalAnalysis",)


Self = TypeVar("Self", bound="SynchroniserPartModalAnalysis")


class SynchroniserPartModalAnalysis(_4608.CouplingHalfModalAnalysis):
    """SynchroniserPartModalAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserPartModalAnalysis")

    class _Cast_SynchroniserPartModalAnalysis:
        """Special nested class for casting SynchroniserPartModalAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserPartModalAnalysis._Cast_SynchroniserPartModalAnalysis",
            parent: "SynchroniserPartModalAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_modal_analysis(
            self: "SynchroniserPartModalAnalysis._Cast_SynchroniserPartModalAnalysis",
        ):
            return self._parent._cast(_4608.CouplingHalfModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "SynchroniserPartModalAnalysis._Cast_SynchroniserPartModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4655

            return self._parent._cast(_4655.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "SynchroniserPartModalAnalysis._Cast_SynchroniserPartModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4594

            return self._parent._cast(_4594.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "SynchroniserPartModalAnalysis._Cast_SynchroniserPartModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4659

            return self._parent._cast(_4659.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserPartModalAnalysis._Cast_SynchroniserPartModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserPartModalAnalysis._Cast_SynchroniserPartModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserPartModalAnalysis._Cast_SynchroniserPartModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserPartModalAnalysis._Cast_SynchroniserPartModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartModalAnalysis._Cast_SynchroniserPartModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def synchroniser_half_modal_analysis(
            self: "SynchroniserPartModalAnalysis._Cast_SynchroniserPartModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4694

            return self._parent._cast(_4694.SynchroniserHalfModalAnalysis)

        @property
        def synchroniser_sleeve_modal_analysis(
            self: "SynchroniserPartModalAnalysis._Cast_SynchroniserPartModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4697

            return self._parent._cast(_4697.SynchroniserSleeveModalAnalysis)

        @property
        def synchroniser_part_modal_analysis(
            self: "SynchroniserPartModalAnalysis._Cast_SynchroniserPartModalAnalysis",
        ) -> "SynchroniserPartModalAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartModalAnalysis._Cast_SynchroniserPartModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SynchroniserPartModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2603.SynchroniserPart":
        """mastapy.system_model.part_model.couplings.SynchroniserPart

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2820.SynchroniserPartSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.SynchroniserPartSystemDeflection

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
    ) -> "SynchroniserPartModalAnalysis._Cast_SynchroniserPartModalAnalysis":
        return self._Cast_SynchroniserPartModalAnalysis(self)
