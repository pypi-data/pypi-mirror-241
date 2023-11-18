"""CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3709,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3540,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed"
)


class CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed(
    _3709.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
):
    """CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            return self._parent._cast(
                _3709.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3657,
            )

            return self._parent._cast(
                _3657.ComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3711,
            )

            return self._parent._cast(
                _3711.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_analysis(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def clutch_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3655,
            )

            return self._parent._cast(
                _3655.ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3660,
            )

            return self._parent._cast(
                _3660.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_pulley_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3674,
            )

            return self._parent._cast(
                _3674.CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3714,
            )

            return self._parent._cast(
                _3714.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def pulley_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3720,
            )

            return self._parent._cast(
                _3720.PulleyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3724,
            )

            return self._parent._cast(
                _3724.RollingRingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3736,
            )

            return self._parent._cast(
                _3736.SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3746,
            )

            return self._parent._cast(
                _3746.SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_part_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3747,
            )

            return self._parent._cast(
                _3747.SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_sleeve_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3748,
            )

            return self._parent._cast(
                _3748.SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_pump_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3751,
            )

            return self._parent._cast(
                _3751.TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_turbine_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3752,
            )

            return self._parent._cast(
                _3752.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3540.CouplingHalfSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.CouplingHalfSteadyStateSynchronousResponseAtASpeed]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3540.CouplingHalfSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.CouplingHalfSteadyStateSynchronousResponseAtASpeed]

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
    def cast_to(
        self: Self,
    ) -> "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed(
            self
        )
