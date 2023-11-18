"""ConceptGearSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3042,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "ConceptGearSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2519
    from mastapy.system_model.analyses_and_results.static_loads import _6839


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="ConceptGearSteadyStateSynchronousResponse")


class ConceptGearSteadyStateSynchronousResponse(
    _3042.GearSteadyStateSynchronousResponse
):
    """ConceptGearSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptGearSteadyStateSynchronousResponse"
    )

    class _Cast_ConceptGearSteadyStateSynchronousResponse:
        """Special nested class for casting ConceptGearSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ConceptGearSteadyStateSynchronousResponse._Cast_ConceptGearSteadyStateSynchronousResponse",
            parent: "ConceptGearSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def gear_steady_state_synchronous_response(
            self: "ConceptGearSteadyStateSynchronousResponse._Cast_ConceptGearSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(_3042.GearSteadyStateSynchronousResponse)

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "ConceptGearSteadyStateSynchronousResponse._Cast_ConceptGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3059,
            )

            return self._parent._cast(
                _3059.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "ConceptGearSteadyStateSynchronousResponse._Cast_ConceptGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3006,
            )

            return self._parent._cast(_3006.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "ConceptGearSteadyStateSynchronousResponse._Cast_ConceptGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3061,
            )

            return self._parent._cast(_3061.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "ConceptGearSteadyStateSynchronousResponse._Cast_ConceptGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptGearSteadyStateSynchronousResponse._Cast_ConceptGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptGearSteadyStateSynchronousResponse._Cast_ConceptGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptGearSteadyStateSynchronousResponse._Cast_ConceptGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearSteadyStateSynchronousResponse._Cast_ConceptGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def concept_gear_steady_state_synchronous_response(
            self: "ConceptGearSteadyStateSynchronousResponse._Cast_ConceptGearSteadyStateSynchronousResponse",
        ) -> "ConceptGearSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ConceptGearSteadyStateSynchronousResponse._Cast_ConceptGearSteadyStateSynchronousResponse",
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
        self: Self, instance_to_wrap: "ConceptGearSteadyStateSynchronousResponse.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2519.ConceptGear":
        """mastapy.system_model.part_model.gears.ConceptGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6839.ConceptGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptGearSteadyStateSynchronousResponse._Cast_ConceptGearSteadyStateSynchronousResponse":
        return self._Cast_ConceptGearSteadyStateSynchronousResponse(self)
