"""KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3441,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2537
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3313,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3442,
        _3443,
    )


__docformat__ = "restructuredtext en"
__all__ = (
    "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
)


Self = TypeVar(
    "Self",
    bound="KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
)


class KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft(
    _3441.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
):
    """KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            return self._parent._cast(
                _3441.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3407,
            )

            return self._parent._cast(
                _3407.ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3433,
            )

            return self._parent._cast(
                _3433.GearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3471,
            )

            return self._parent._cast(
                _3471.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3373,
            )

            return self._parent._cast(
                _3373.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3452,
            )

            return self._parent._cast(
                _3452.PartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2537.KlingelnbergCycloPalloidHypoidGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2537.KlingelnbergCycloPalloidHypoidGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3313.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft]

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
    def klingelnberg_cyclo_palloid_hypoid_gears_compound_steady_state_synchronous_response_on_a_shaft(
        self: Self,
    ) -> "List[_3442.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidHypoidGearsCompoundSteadyStateSynchronousResponseOnAShaft
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_compound_steady_state_synchronous_response_on_a_shaft(
        self: Self,
    ) -> "List[_3443.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidHypoidMeshesCompoundSteadyStateSynchronousResponseOnAShaft
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3313.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft]

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
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft(
            self
        )
