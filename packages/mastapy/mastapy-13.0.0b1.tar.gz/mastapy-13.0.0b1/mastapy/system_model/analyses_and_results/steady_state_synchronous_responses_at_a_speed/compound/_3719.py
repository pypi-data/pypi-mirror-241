"""PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3754,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2470
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3589,
    )


__docformat__ = "restructuredtext en"
__all__ = ("PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed")


class PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed(
    _3754.VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed
):
    """PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _POWER_LOAD_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            return self._parent._cast(
                _3754.VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3709,
            )

            return self._parent._cast(
                _3709.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_compound_steady_state_synchronous_response_at_a_speed(
            self: "PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3657,
            )

            return self._parent._cast(
                _3657.ComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3711,
            )

            return self._parent._cast(
                _3711.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_analysis(
            self: "PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def power_load_compound_steady_state_synchronous_response_at_a_speed(
            self: "PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2470.PowerLoad":
        """mastapy.system_model.part_model.PowerLoad

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
    ) -> "List[_3589.PowerLoadSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.PowerLoadSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "List[_3589.PowerLoadSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.PowerLoadSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed(self)
