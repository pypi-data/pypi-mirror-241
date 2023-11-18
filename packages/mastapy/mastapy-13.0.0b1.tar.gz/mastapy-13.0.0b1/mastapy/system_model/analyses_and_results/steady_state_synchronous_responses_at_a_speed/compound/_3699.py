"""KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3665,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3568,
    )


__docformat__ = "restructuredtext en"
__all__ = (
    "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
)


Self = TypeVar(
    "Self",
    bound="KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
)


class KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed(
    _3665.ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
):
    """KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            return self._parent._cast(
                _3665.ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3691,
            )

            return self._parent._cast(
                _3691.GearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3697,
            )

            return self._parent._cast(
                _3697.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3667,
            )

            return self._parent._cast(
                _3667.ConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3702,
            )

            return self._parent._cast(
                _3702.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3705,
            )

            return self._parent._cast(
                _3705.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3568.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3568.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed(
            self
        )
