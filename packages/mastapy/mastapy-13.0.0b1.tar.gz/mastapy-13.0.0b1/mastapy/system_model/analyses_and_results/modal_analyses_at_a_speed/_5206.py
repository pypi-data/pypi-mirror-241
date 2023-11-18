"""RollingRingAssemblyModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5213
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "RollingRingAssemblyModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2595
    from mastapy.system_model.analyses_and_results.static_loads import _6943


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingAssemblyModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="RollingRingAssemblyModalAnalysisAtASpeed")


class RollingRingAssemblyModalAnalysisAtASpeed(
    _5213.SpecialisedAssemblyModalAnalysisAtASpeed
):
    """RollingRingAssemblyModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_ASSEMBLY_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RollingRingAssemblyModalAnalysisAtASpeed"
    )

    class _Cast_RollingRingAssemblyModalAnalysisAtASpeed:
        """Special nested class for casting RollingRingAssemblyModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "RollingRingAssemblyModalAnalysisAtASpeed._Cast_RollingRingAssemblyModalAnalysisAtASpeed",
            parent: "RollingRingAssemblyModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def specialised_assembly_modal_analysis_at_a_speed(
            self: "RollingRingAssemblyModalAnalysisAtASpeed._Cast_RollingRingAssemblyModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5213.SpecialisedAssemblyModalAnalysisAtASpeed)

        @property
        def abstract_assembly_modal_analysis_at_a_speed(
            self: "RollingRingAssemblyModalAnalysisAtASpeed._Cast_RollingRingAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5114,
            )

            return self._parent._cast(_5114.AbstractAssemblyModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "RollingRingAssemblyModalAnalysisAtASpeed._Cast_RollingRingAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5194,
            )

            return self._parent._cast(_5194.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "RollingRingAssemblyModalAnalysisAtASpeed._Cast_RollingRingAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RollingRingAssemblyModalAnalysisAtASpeed._Cast_RollingRingAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RollingRingAssemblyModalAnalysisAtASpeed._Cast_RollingRingAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingAssemblyModalAnalysisAtASpeed._Cast_RollingRingAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingAssemblyModalAnalysisAtASpeed._Cast_RollingRingAssemblyModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def rolling_ring_assembly_modal_analysis_at_a_speed(
            self: "RollingRingAssemblyModalAnalysisAtASpeed._Cast_RollingRingAssemblyModalAnalysisAtASpeed",
        ) -> "RollingRingAssemblyModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "RollingRingAssemblyModalAnalysisAtASpeed._Cast_RollingRingAssemblyModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "RollingRingAssemblyModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2595.RollingRingAssembly":
        """mastapy.system_model.part_model.couplings.RollingRingAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6943.RollingRingAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RollingRingAssemblyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "RollingRingAssemblyModalAnalysisAtASpeed._Cast_RollingRingAssemblyModalAnalysisAtASpeed":
        return self._Cast_RollingRingAssemblyModalAnalysisAtASpeed(self)
