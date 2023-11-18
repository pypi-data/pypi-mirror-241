"""PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5024,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2587
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4937,
    )


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness",)


Self = TypeVar(
    "Self", bound="PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness"
)


class PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness(
    _5024.CouplingHalfCompoundModalAnalysisAtAStiffness
):
    """PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness",
    )

    class _Cast_PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness",
            parent: "PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_modal_analysis_at_a_stiffness(
            self: "PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(
                _5024.CouplingHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(
            self: "PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5062,
            )

            return self._parent._cast(
                _5062.MountableComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def component_compound_modal_analysis_at_a_stiffness(
            self: "PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5010,
            )

            return self._parent._cast(_5010.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5064,
            )

            return self._parent._cast(_5064.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis_at_a_stiffness(
            self: "PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness",
        ) -> "PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness",
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
        self: Self,
        instance_to_wrap: "PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2587.PartToPartShearCouplingHalf":
        """mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4937.PartToPartShearCouplingHalfModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.PartToPartShearCouplingHalfModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4937.PartToPartShearCouplingHalfModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.PartToPartShearCouplingHalfModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness":
        return self._Cast_PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness(
            self
        )
