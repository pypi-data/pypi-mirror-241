"""SpringDamperSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3282,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "SpringDamperSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2598
    from mastapy.system_model.analyses_and_results.static_loads import _6956


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="SpringDamperSteadyStateSynchronousResponseOnAShaft")


class SpringDamperSteadyStateSynchronousResponseOnAShaft(
    _3282.CouplingSteadyStateSynchronousResponseOnAShaft
):
    """SpringDamperSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpringDamperSteadyStateSynchronousResponseOnAShaft"
    )

    class _Cast_SpringDamperSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting SpringDamperSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "SpringDamperSteadyStateSynchronousResponseOnAShaft._Cast_SpringDamperSteadyStateSynchronousResponseOnAShaft",
            parent: "SpringDamperSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def coupling_steady_state_synchronous_response_on_a_shaft(
            self: "SpringDamperSteadyStateSynchronousResponseOnAShaft._Cast_SpringDamperSteadyStateSynchronousResponseOnAShaft",
        ):
            return self._parent._cast(
                _3282.CouplingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def specialised_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "SpringDamperSteadyStateSynchronousResponseOnAShaft._Cast_SpringDamperSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3341,
            )

            return self._parent._cast(
                _3341.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "SpringDamperSteadyStateSynchronousResponseOnAShaft._Cast_SpringDamperSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3243,
            )

            return self._parent._cast(
                _3243.AbstractAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "SpringDamperSteadyStateSynchronousResponseOnAShaft._Cast_SpringDamperSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3322,
            )

            return self._parent._cast(_3322.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "SpringDamperSteadyStateSynchronousResponseOnAShaft._Cast_SpringDamperSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpringDamperSteadyStateSynchronousResponseOnAShaft._Cast_SpringDamperSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpringDamperSteadyStateSynchronousResponseOnAShaft._Cast_SpringDamperSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperSteadyStateSynchronousResponseOnAShaft._Cast_SpringDamperSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperSteadyStateSynchronousResponseOnAShaft._Cast_SpringDamperSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def spring_damper_steady_state_synchronous_response_on_a_shaft(
            self: "SpringDamperSteadyStateSynchronousResponseOnAShaft._Cast_SpringDamperSteadyStateSynchronousResponseOnAShaft",
        ) -> "SpringDamperSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "SpringDamperSteadyStateSynchronousResponseOnAShaft._Cast_SpringDamperSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "SpringDamperSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2598.SpringDamper":
        """mastapy.system_model.part_model.couplings.SpringDamper

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6956.SpringDamperLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpringDamperLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpringDamperSteadyStateSynchronousResponseOnAShaft._Cast_SpringDamperSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_SpringDamperSteadyStateSynchronousResponseOnAShaft(self)
