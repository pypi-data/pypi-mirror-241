"""PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3495,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2470
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3330,
    )


__docformat__ = "restructuredtext en"
__all__ = ("PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft")


class PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft(
    _3495.VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft
):
    """PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _POWER_LOAD_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            return self._parent._cast(
                _3495.VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3450,
            )

            return self._parent._cast(
                _3450.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3398,
            )

            return self._parent._cast(
                _3398.ComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3452,
            )

            return self._parent._cast(
                _3452.PartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_analysis(
            self: "PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def power_load_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
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
    ) -> "List[_3330.PowerLoadSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.PowerLoadSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3330.PowerLoadSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.PowerLoadSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft(self)
