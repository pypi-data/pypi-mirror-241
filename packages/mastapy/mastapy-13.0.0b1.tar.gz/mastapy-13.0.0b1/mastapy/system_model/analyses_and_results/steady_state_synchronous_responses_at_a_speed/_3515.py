"""BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3520,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2513
    from mastapy.system_model.analyses_and_results.static_loads import _6820


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed"
)


class BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed(
    _3520.BevelGearSteadyStateSynchronousResponseAtASpeed
):
    """BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed",
            parent: "BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed",
        ):
            return self._parent._cast(
                _3520.BevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3508,
            )

            return self._parent._cast(
                _3508.AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3536,
            )

            return self._parent._cast(
                _3536.ConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3562,
            )

            return self._parent._cast(_3562.GearSteadyStateSynchronousResponseAtASpeed)

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3579,
            )

            return self._parent._cast(
                _3579.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3527,
            )

            return self._parent._cast(
                _3527.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3581,
            )

            return self._parent._cast(_3581.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3516,
            )

            return self._parent._cast(
                _3516.BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3517,
            )

            return self._parent._cast(
                _3517.BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2513.BevelDifferentialGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6820.BevelDifferentialGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearLoadCase

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
    ) -> "BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed(
            self
        )
