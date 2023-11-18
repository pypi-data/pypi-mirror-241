"""BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3256,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2516


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft"
)


class BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft(
    _3256.BevelDifferentialGearSteadyStateSynchronousResponseOnAShaft
):
    """BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft",
            parent: "BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft",
        ):
            return self._parent._cast(
                _3256.BevelDifferentialGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3261,
            )

            return self._parent._cast(
                _3261.BevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3249,
            )

            return self._parent._cast(
                _3249.AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3277,
            )

            return self._parent._cast(
                _3277.ConicalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3303,
            )

            return self._parent._cast(_3303.GearSteadyStateSynchronousResponseOnAShaft)

        @property
        def mountable_component_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3320,
            )

            return self._parent._cast(
                _3320.MountableComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3268,
            )

            return self._parent._cast(
                _3268.ComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3322,
            )

            return self._parent._cast(_3322.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2516.BevelDifferentialSunGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialSunGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft":
        return (
            self._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft(
                self
            )
        )
