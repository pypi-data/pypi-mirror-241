"""MassDiscModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4703
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MASS_DISC_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses", "MassDiscModalAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2460
    from mastapy.system_model.analyses_and_results.static_loads import _6919
    from mastapy.system_model.analyses_and_results.system_deflections import _2777


__docformat__ = "restructuredtext en"
__all__ = ("MassDiscModalAnalysis",)


Self = TypeVar("Self", bound="MassDiscModalAnalysis")


class MassDiscModalAnalysis(_4703.VirtualComponentModalAnalysis):
    """MassDiscModalAnalysis

    This is a mastapy class.
    """

    TYPE = _MASS_DISC_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MassDiscModalAnalysis")

    class _Cast_MassDiscModalAnalysis:
        """Special nested class for casting MassDiscModalAnalysis to subclasses."""

        def __init__(
            self: "MassDiscModalAnalysis._Cast_MassDiscModalAnalysis",
            parent: "MassDiscModalAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_modal_analysis(
            self: "MassDiscModalAnalysis._Cast_MassDiscModalAnalysis",
        ):
            return self._parent._cast(_4703.VirtualComponentModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "MassDiscModalAnalysis._Cast_MassDiscModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4655

            return self._parent._cast(_4655.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "MassDiscModalAnalysis._Cast_MassDiscModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4594

            return self._parent._cast(_4594.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "MassDiscModalAnalysis._Cast_MassDiscModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4659

            return self._parent._cast(_4659.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "MassDiscModalAnalysis._Cast_MassDiscModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MassDiscModalAnalysis._Cast_MassDiscModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(self: "MassDiscModalAnalysis._Cast_MassDiscModalAnalysis"):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MassDiscModalAnalysis._Cast_MassDiscModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MassDiscModalAnalysis._Cast_MassDiscModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def mass_disc_modal_analysis(
            self: "MassDiscModalAnalysis._Cast_MassDiscModalAnalysis",
        ) -> "MassDiscModalAnalysis":
            return self._parent

        def __getattr__(
            self: "MassDiscModalAnalysis._Cast_MassDiscModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MassDiscModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2460.MassDisc":
        """mastapy.system_model.part_model.MassDisc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6919.MassDiscLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.MassDiscLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2777.MassDiscSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.MassDiscSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[MassDiscModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.MassDiscModalAnalysis]

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
    def cast_to(self: Self) -> "MassDiscModalAnalysis._Cast_MassDiscModalAnalysis":
        return self._Cast_MassDiscModalAnalysis(self)
