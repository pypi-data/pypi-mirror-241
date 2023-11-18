"""KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5019,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4923,
    )


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness",)


Self = TypeVar(
    "Self",
    bound="KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness",
)


class KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness(
    _5019.ConicalGearSetCompoundModalAnalysisAtAStiffness
):
    """KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness",
            parent: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def conical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(
                _5019.ConicalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def gear_set_compound_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5045,
            )

            return self._parent._cast(_5045.GearSetCompoundModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_compound_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5083,
            )

            return self._parent._cast(
                _5083.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4985,
            )

            return self._parent._cast(
                _4985.AbstractAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5064,
            )

            return self._parent._cast(_5064.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5056,
            )

            return self._parent._cast(
                _5056.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5059,
            )

            return self._parent._cast(
                _5059.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4923.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4923.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness":
        return self._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness(
            self
        )
