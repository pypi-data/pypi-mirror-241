"""ConceptCouplingModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5153
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "ConceptCouplingModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2579
    from mastapy.system_model.analyses_and_results.static_loads import _6838


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="ConceptCouplingModalAnalysisAtASpeed")


class ConceptCouplingModalAnalysisAtASpeed(_5153.CouplingModalAnalysisAtASpeed):
    """ConceptCouplingModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptCouplingModalAnalysisAtASpeed")

    class _Cast_ConceptCouplingModalAnalysisAtASpeed:
        """Special nested class for casting ConceptCouplingModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "ConceptCouplingModalAnalysisAtASpeed._Cast_ConceptCouplingModalAnalysisAtASpeed",
            parent: "ConceptCouplingModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_modal_analysis_at_a_speed(
            self: "ConceptCouplingModalAnalysisAtASpeed._Cast_ConceptCouplingModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5153.CouplingModalAnalysisAtASpeed)

        @property
        def specialised_assembly_modal_analysis_at_a_speed(
            self: "ConceptCouplingModalAnalysisAtASpeed._Cast_ConceptCouplingModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5213,
            )

            return self._parent._cast(_5213.SpecialisedAssemblyModalAnalysisAtASpeed)

        @property
        def abstract_assembly_modal_analysis_at_a_speed(
            self: "ConceptCouplingModalAnalysisAtASpeed._Cast_ConceptCouplingModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5114,
            )

            return self._parent._cast(_5114.AbstractAssemblyModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "ConceptCouplingModalAnalysisAtASpeed._Cast_ConceptCouplingModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5194,
            )

            return self._parent._cast(_5194.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "ConceptCouplingModalAnalysisAtASpeed._Cast_ConceptCouplingModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptCouplingModalAnalysisAtASpeed._Cast_ConceptCouplingModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptCouplingModalAnalysisAtASpeed._Cast_ConceptCouplingModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingModalAnalysisAtASpeed._Cast_ConceptCouplingModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingModalAnalysisAtASpeed._Cast_ConceptCouplingModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def concept_coupling_modal_analysis_at_a_speed(
            self: "ConceptCouplingModalAnalysisAtASpeed._Cast_ConceptCouplingModalAnalysisAtASpeed",
        ) -> "ConceptCouplingModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingModalAnalysisAtASpeed._Cast_ConceptCouplingModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "ConceptCouplingModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2579.ConceptCoupling":
        """mastapy.system_model.part_model.couplings.ConceptCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6838.ConceptCouplingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingLoadCase

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
    ) -> "ConceptCouplingModalAnalysisAtASpeed._Cast_ConceptCouplingModalAnalysisAtASpeed":
        return self._Cast_ConceptCouplingModalAnalysisAtASpeed(self)
