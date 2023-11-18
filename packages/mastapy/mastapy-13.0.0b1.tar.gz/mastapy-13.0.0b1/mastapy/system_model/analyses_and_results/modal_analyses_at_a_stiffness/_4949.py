"""RollingRingModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4892,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "RollingRingModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2594
    from mastapy.system_model.analyses_and_results.static_loads import _6945


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="RollingRingModalAnalysisAtAStiffness")


class RollingRingModalAnalysisAtAStiffness(_4892.CouplingHalfModalAnalysisAtAStiffness):
    """RollingRingModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollingRingModalAnalysisAtAStiffness")

    class _Cast_RollingRingModalAnalysisAtAStiffness:
        """Special nested class for casting RollingRingModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "RollingRingModalAnalysisAtAStiffness._Cast_RollingRingModalAnalysisAtAStiffness",
            parent: "RollingRingModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def coupling_half_modal_analysis_at_a_stiffness(
            self: "RollingRingModalAnalysisAtAStiffness._Cast_RollingRingModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(_4892.CouplingHalfModalAnalysisAtAStiffness)

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "RollingRingModalAnalysisAtAStiffness._Cast_RollingRingModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4933,
            )

            return self._parent._cast(_4933.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "RollingRingModalAnalysisAtAStiffness._Cast_RollingRingModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4879,
            )

            return self._parent._cast(_4879.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "RollingRingModalAnalysisAtAStiffness._Cast_RollingRingModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4935,
            )

            return self._parent._cast(_4935.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "RollingRingModalAnalysisAtAStiffness._Cast_RollingRingModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RollingRingModalAnalysisAtAStiffness._Cast_RollingRingModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RollingRingModalAnalysisAtAStiffness._Cast_RollingRingModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingModalAnalysisAtAStiffness._Cast_RollingRingModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingModalAnalysisAtAStiffness._Cast_RollingRingModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def rolling_ring_modal_analysis_at_a_stiffness(
            self: "RollingRingModalAnalysisAtAStiffness._Cast_RollingRingModalAnalysisAtAStiffness",
        ) -> "RollingRingModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "RollingRingModalAnalysisAtAStiffness._Cast_RollingRingModalAnalysisAtAStiffness",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "RollingRingModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2594.RollingRing":
        """mastapy.system_model.part_model.couplings.RollingRing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6945.RollingRingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RollingRingLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[RollingRingModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.RollingRingModalAnalysisAtAStiffness]

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
    ) -> "RollingRingModalAnalysisAtAStiffness._Cast_RollingRingModalAnalysisAtAStiffness":
        return self._Cast_RollingRingModalAnalysisAtAStiffness(self)
