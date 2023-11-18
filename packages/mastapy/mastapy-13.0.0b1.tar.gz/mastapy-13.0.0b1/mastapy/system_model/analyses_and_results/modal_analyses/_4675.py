"""ShaftHubConnectionModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4605
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_HUB_CONNECTION_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "ShaftHubConnectionModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2596
    from mastapy.system_model.analyses_and_results.static_loads import _6947
    from mastapy.system_model.analyses_and_results.system_deflections import _2799


__docformat__ = "restructuredtext en"
__all__ = ("ShaftHubConnectionModalAnalysis",)


Self = TypeVar("Self", bound="ShaftHubConnectionModalAnalysis")


class ShaftHubConnectionModalAnalysis(_4605.ConnectorModalAnalysis):
    """ShaftHubConnectionModalAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_HUB_CONNECTION_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftHubConnectionModalAnalysis")

    class _Cast_ShaftHubConnectionModalAnalysis:
        """Special nested class for casting ShaftHubConnectionModalAnalysis to subclasses."""

        def __init__(
            self: "ShaftHubConnectionModalAnalysis._Cast_ShaftHubConnectionModalAnalysis",
            parent: "ShaftHubConnectionModalAnalysis",
        ):
            self._parent = parent

        @property
        def connector_modal_analysis(
            self: "ShaftHubConnectionModalAnalysis._Cast_ShaftHubConnectionModalAnalysis",
        ):
            return self._parent._cast(_4605.ConnectorModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "ShaftHubConnectionModalAnalysis._Cast_ShaftHubConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4655

            return self._parent._cast(_4655.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "ShaftHubConnectionModalAnalysis._Cast_ShaftHubConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4594

            return self._parent._cast(_4594.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "ShaftHubConnectionModalAnalysis._Cast_ShaftHubConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4659

            return self._parent._cast(_4659.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ShaftHubConnectionModalAnalysis._Cast_ShaftHubConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ShaftHubConnectionModalAnalysis._Cast_ShaftHubConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ShaftHubConnectionModalAnalysis._Cast_ShaftHubConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftHubConnectionModalAnalysis._Cast_ShaftHubConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftHubConnectionModalAnalysis._Cast_ShaftHubConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def shaft_hub_connection_modal_analysis(
            self: "ShaftHubConnectionModalAnalysis._Cast_ShaftHubConnectionModalAnalysis",
        ) -> "ShaftHubConnectionModalAnalysis":
            return self._parent

        def __getattr__(
            self: "ShaftHubConnectionModalAnalysis._Cast_ShaftHubConnectionModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftHubConnectionModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2596.ShaftHubConnection":
        """mastapy.system_model.part_model.couplings.ShaftHubConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6947.ShaftHubConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ShaftHubConnectionLoadCase

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
    ) -> "_2799.ShaftHubConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ShaftHubConnectionSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ShaftHubConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ShaftHubConnectionModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ShaftHubConnectionModalAnalysis._Cast_ShaftHubConnectionModalAnalysis":
        return self._Cast_ShaftHubConnectionModalAnalysis(self)
