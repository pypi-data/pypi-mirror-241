"""RingPinsModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4655
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses", "RingPinsModalAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2568
    from mastapy.system_model.analyses_and_results.static_loads import _6941
    from mastapy.system_model.analyses_and_results.system_deflections import _2792


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsModalAnalysis",)


Self = TypeVar("Self", bound="RingPinsModalAnalysis")


class RingPinsModalAnalysis(_4655.MountableComponentModalAnalysis):
    """RingPinsModalAnalysis

    This is a mastapy class.
    """

    TYPE = _RING_PINS_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RingPinsModalAnalysis")

    class _Cast_RingPinsModalAnalysis:
        """Special nested class for casting RingPinsModalAnalysis to subclasses."""

        def __init__(
            self: "RingPinsModalAnalysis._Cast_RingPinsModalAnalysis",
            parent: "RingPinsModalAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_modal_analysis(
            self: "RingPinsModalAnalysis._Cast_RingPinsModalAnalysis",
        ):
            return self._parent._cast(_4655.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "RingPinsModalAnalysis._Cast_RingPinsModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4594

            return self._parent._cast(_4594.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "RingPinsModalAnalysis._Cast_RingPinsModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4659

            return self._parent._cast(_4659.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "RingPinsModalAnalysis._Cast_RingPinsModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RingPinsModalAnalysis._Cast_RingPinsModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(self: "RingPinsModalAnalysis._Cast_RingPinsModalAnalysis"):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RingPinsModalAnalysis._Cast_RingPinsModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsModalAnalysis._Cast_RingPinsModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def ring_pins_modal_analysis(
            self: "RingPinsModalAnalysis._Cast_RingPinsModalAnalysis",
        ) -> "RingPinsModalAnalysis":
            return self._parent

        def __getattr__(
            self: "RingPinsModalAnalysis._Cast_RingPinsModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RingPinsModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2568.RingPins":
        """mastapy.system_model.part_model.cycloidal.RingPins

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6941.RingPinsLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RingPinsLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2792.RingPinsSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.RingPinsSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "RingPinsModalAnalysis._Cast_RingPinsModalAnalysis":
        return self._Cast_RingPinsModalAnalysis(self)
