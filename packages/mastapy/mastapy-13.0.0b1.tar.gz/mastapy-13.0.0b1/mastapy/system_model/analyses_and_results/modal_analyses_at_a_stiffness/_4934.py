"""OilSealModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4890,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OIL_SEAL_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "OilSealModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2464
    from mastapy.system_model.analyses_and_results.static_loads import _6924


__docformat__ = "restructuredtext en"
__all__ = ("OilSealModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="OilSealModalAnalysisAtAStiffness")


class OilSealModalAnalysisAtAStiffness(_4890.ConnectorModalAnalysisAtAStiffness):
    """OilSealModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _OIL_SEAL_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OilSealModalAnalysisAtAStiffness")

    class _Cast_OilSealModalAnalysisAtAStiffness:
        """Special nested class for casting OilSealModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "OilSealModalAnalysisAtAStiffness._Cast_OilSealModalAnalysisAtAStiffness",
            parent: "OilSealModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def connector_modal_analysis_at_a_stiffness(
            self: "OilSealModalAnalysisAtAStiffness._Cast_OilSealModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(_4890.ConnectorModalAnalysisAtAStiffness)

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "OilSealModalAnalysisAtAStiffness._Cast_OilSealModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4933,
            )

            return self._parent._cast(_4933.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "OilSealModalAnalysisAtAStiffness._Cast_OilSealModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4879,
            )

            return self._parent._cast(_4879.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "OilSealModalAnalysisAtAStiffness._Cast_OilSealModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4935,
            )

            return self._parent._cast(_4935.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "OilSealModalAnalysisAtAStiffness._Cast_OilSealModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "OilSealModalAnalysisAtAStiffness._Cast_OilSealModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "OilSealModalAnalysisAtAStiffness._Cast_OilSealModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "OilSealModalAnalysisAtAStiffness._Cast_OilSealModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "OilSealModalAnalysisAtAStiffness._Cast_OilSealModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def oil_seal_modal_analysis_at_a_stiffness(
            self: "OilSealModalAnalysisAtAStiffness._Cast_OilSealModalAnalysisAtAStiffness",
        ) -> "OilSealModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "OilSealModalAnalysisAtAStiffness._Cast_OilSealModalAnalysisAtAStiffness",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "OilSealModalAnalysisAtAStiffness.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2464.OilSeal":
        """mastapy.system_model.part_model.OilSeal

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6924.OilSealLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.OilSealLoadCase

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
    ) -> "OilSealModalAnalysisAtAStiffness._Cast_OilSealModalAnalysisAtAStiffness":
        return self._Cast_OilSealModalAnalysisAtAStiffness(self)
