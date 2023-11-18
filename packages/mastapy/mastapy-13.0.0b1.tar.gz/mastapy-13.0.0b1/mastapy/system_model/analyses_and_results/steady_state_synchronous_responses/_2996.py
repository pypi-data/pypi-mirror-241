"""BevelDifferentialSunGearSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _2994,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "BevelDifferentialSunGearSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2516


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialSunGearSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="BevelDifferentialSunGearSteadyStateSynchronousResponse")


class BevelDifferentialSunGearSteadyStateSynchronousResponse(
    _2994.BevelDifferentialGearSteadyStateSynchronousResponse
):
    """BevelDifferentialSunGearSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialSunGearSteadyStateSynchronousResponse",
    )

    class _Cast_BevelDifferentialSunGearSteadyStateSynchronousResponse:
        """Special nested class for casting BevelDifferentialSunGearSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponse._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponse",
            parent: "BevelDifferentialSunGearSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_steady_state_synchronous_response(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponse._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _2994.BevelDifferentialGearSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_steady_state_synchronous_response(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponse._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2999,
            )

            return self._parent._cast(_2999.BevelGearSteadyStateSynchronousResponse)

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponse._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2987,
            )

            return self._parent._cast(
                _2987.AGMAGleasonConicalGearSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_steady_state_synchronous_response(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponse._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3015,
            )

            return self._parent._cast(_3015.ConicalGearSteadyStateSynchronousResponse)

        @property
        def gear_steady_state_synchronous_response(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponse._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3042,
            )

            return self._parent._cast(_3042.GearSteadyStateSynchronousResponse)

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponse._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3059,
            )

            return self._parent._cast(
                _3059.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponse._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3006,
            )

            return self._parent._cast(_3006.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponse._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3061,
            )

            return self._parent._cast(_3061.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponse._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponse._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponse._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponse._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponse._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponse._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponse",
        ) -> "BevelDifferentialSunGearSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialSunGearSteadyStateSynchronousResponse._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponse",
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
        instance_to_wrap: "BevelDifferentialSunGearSteadyStateSynchronousResponse.TYPE",
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
    ) -> "BevelDifferentialSunGearSteadyStateSynchronousResponse._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponse":
        return self._Cast_BevelDifferentialSunGearSteadyStateSynchronousResponse(self)
