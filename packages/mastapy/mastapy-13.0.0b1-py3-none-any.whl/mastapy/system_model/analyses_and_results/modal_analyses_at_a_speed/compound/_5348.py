"""SpringDamperHalfCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5283,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HALF_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "SpringDamperHalfCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2599
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5218,
    )


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperHalfCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="SpringDamperHalfCompoundModalAnalysisAtASpeed")


class SpringDamperHalfCompoundModalAnalysisAtASpeed(
    _5283.CouplingHalfCompoundModalAnalysisAtASpeed
):
    """SpringDamperHalfCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_HALF_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpringDamperHalfCompoundModalAnalysisAtASpeed"
    )

    class _Cast_SpringDamperHalfCompoundModalAnalysisAtASpeed:
        """Special nested class for casting SpringDamperHalfCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "SpringDamperHalfCompoundModalAnalysisAtASpeed._Cast_SpringDamperHalfCompoundModalAnalysisAtASpeed",
            parent: "SpringDamperHalfCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_modal_analysis_at_a_speed(
            self: "SpringDamperHalfCompoundModalAnalysisAtASpeed._Cast_SpringDamperHalfCompoundModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5283.CouplingHalfCompoundModalAnalysisAtASpeed)

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(
            self: "SpringDamperHalfCompoundModalAnalysisAtASpeed._Cast_SpringDamperHalfCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5321,
            )

            return self._parent._cast(
                _5321.MountableComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "SpringDamperHalfCompoundModalAnalysisAtASpeed._Cast_SpringDamperHalfCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5269,
            )

            return self._parent._cast(_5269.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "SpringDamperHalfCompoundModalAnalysisAtASpeed._Cast_SpringDamperHalfCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5323,
            )

            return self._parent._cast(_5323.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "SpringDamperHalfCompoundModalAnalysisAtASpeed._Cast_SpringDamperHalfCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpringDamperHalfCompoundModalAnalysisAtASpeed._Cast_SpringDamperHalfCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperHalfCompoundModalAnalysisAtASpeed._Cast_SpringDamperHalfCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def spring_damper_half_compound_modal_analysis_at_a_speed(
            self: "SpringDamperHalfCompoundModalAnalysisAtASpeed._Cast_SpringDamperHalfCompoundModalAnalysisAtASpeed",
        ) -> "SpringDamperHalfCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "SpringDamperHalfCompoundModalAnalysisAtASpeed._Cast_SpringDamperHalfCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "SpringDamperHalfCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2599.SpringDamperHalf":
        """mastapy.system_model.part_model.couplings.SpringDamperHalf

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
    ) -> "List[_5218.SpringDamperHalfModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.SpringDamperHalfModalAnalysisAtASpeed]

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
    ) -> "List[_5218.SpringDamperHalfModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.SpringDamperHalfModalAnalysisAtASpeed]

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
    ) -> "SpringDamperHalfCompoundModalAnalysisAtASpeed._Cast_SpringDamperHalfCompoundModalAnalysisAtASpeed":
        return self._Cast_SpringDamperHalfCompoundModalAnalysisAtASpeed(self)
