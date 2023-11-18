"""KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4759
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_COMPOUND_MODAL_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
        "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4642


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis"
)


class KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis(
    _4759.ConicalGearSetCompoundModalAnalysis
):
    """KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_set_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis",
        ):
            return self._parent._cast(_4759.ConicalGearSetCompoundModalAnalysis)

        @property
        def gear_set_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4785,
            )

            return self._parent._cast(_4785.GearSetCompoundModalAnalysis)

        @property
        def specialised_assembly_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4823,
            )

            return self._parent._cast(_4823.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4725,
            )

            return self._parent._cast(_4725.AbstractAssemblyCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4804,
            )

            return self._parent._cast(_4804.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4796,
            )

            return self._parent._cast(
                _4796.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4799,
            )

            return self._parent._cast(
                _4799.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4642.KlingelnbergCycloPalloidConicalGearSetModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidConicalGearSetModalAnalysis]

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
    ) -> "List[_4642.KlingelnbergCycloPalloidConicalGearSetModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.KlingelnbergCycloPalloidConicalGearSetModalAnalysis]

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
    ) -> "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis":
        return self._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis(
            self
        )
