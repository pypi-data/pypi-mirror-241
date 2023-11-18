"""FEPartModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4856,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_PART_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "FEPartModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2451
    from mastapy.system_model.analyses_and_results.static_loads import _6885


__docformat__ = "restructuredtext en"
__all__ = ("FEPartModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="FEPartModalAnalysisAtAStiffness")


class FEPartModalAnalysisAtAStiffness(
    _4856.AbstractShaftOrHousingModalAnalysisAtAStiffness
):
    """FEPartModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _FE_PART_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEPartModalAnalysisAtAStiffness")

    class _Cast_FEPartModalAnalysisAtAStiffness:
        """Special nested class for casting FEPartModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "FEPartModalAnalysisAtAStiffness._Cast_FEPartModalAnalysisAtAStiffness",
            parent: "FEPartModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_modal_analysis_at_a_stiffness(
            self: "FEPartModalAnalysisAtAStiffness._Cast_FEPartModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(
                _4856.AbstractShaftOrHousingModalAnalysisAtAStiffness
            )

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "FEPartModalAnalysisAtAStiffness._Cast_FEPartModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4879,
            )

            return self._parent._cast(_4879.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "FEPartModalAnalysisAtAStiffness._Cast_FEPartModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4935,
            )

            return self._parent._cast(_4935.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "FEPartModalAnalysisAtAStiffness._Cast_FEPartModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FEPartModalAnalysisAtAStiffness._Cast_FEPartModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FEPartModalAnalysisAtAStiffness._Cast_FEPartModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FEPartModalAnalysisAtAStiffness._Cast_FEPartModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FEPartModalAnalysisAtAStiffness._Cast_FEPartModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def fe_part_modal_analysis_at_a_stiffness(
            self: "FEPartModalAnalysisAtAStiffness._Cast_FEPartModalAnalysisAtAStiffness",
        ) -> "FEPartModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "FEPartModalAnalysisAtAStiffness._Cast_FEPartModalAnalysisAtAStiffness",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEPartModalAnalysisAtAStiffness.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2451.FEPart":
        """mastapy.system_model.part_model.FEPart

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6885.FEPartLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FEPartLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[FEPartModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.FEPartModalAnalysisAtAStiffness]

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
    ) -> "FEPartModalAnalysisAtAStiffness._Cast_FEPartModalAnalysisAtAStiffness":
        return self._Cast_FEPartModalAnalysisAtAStiffness(self)
