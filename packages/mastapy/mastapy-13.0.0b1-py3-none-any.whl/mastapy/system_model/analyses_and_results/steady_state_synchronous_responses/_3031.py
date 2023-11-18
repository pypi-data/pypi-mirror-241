"""CylindricalPlanetGearSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3030,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "CylindricalPlanetGearSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2525


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="CylindricalPlanetGearSteadyStateSynchronousResponse")


class CylindricalPlanetGearSteadyStateSynchronousResponse(
    _3030.CylindricalGearSteadyStateSynchronousResponse
):
    """CylindricalPlanetGearSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalPlanetGearSteadyStateSynchronousResponse"
    )

    class _Cast_CylindricalPlanetGearSteadyStateSynchronousResponse:
        """Special nested class for casting CylindricalPlanetGearSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearSteadyStateSynchronousResponse._Cast_CylindricalPlanetGearSteadyStateSynchronousResponse",
            parent: "CylindricalPlanetGearSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_steady_state_synchronous_response(
            self: "CylindricalPlanetGearSteadyStateSynchronousResponse._Cast_CylindricalPlanetGearSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _3030.CylindricalGearSteadyStateSynchronousResponse
            )

        @property
        def gear_steady_state_synchronous_response(
            self: "CylindricalPlanetGearSteadyStateSynchronousResponse._Cast_CylindricalPlanetGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3042,
            )

            return self._parent._cast(_3042.GearSteadyStateSynchronousResponse)

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "CylindricalPlanetGearSteadyStateSynchronousResponse._Cast_CylindricalPlanetGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3059,
            )

            return self._parent._cast(
                _3059.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "CylindricalPlanetGearSteadyStateSynchronousResponse._Cast_CylindricalPlanetGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3006,
            )

            return self._parent._cast(_3006.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "CylindricalPlanetGearSteadyStateSynchronousResponse._Cast_CylindricalPlanetGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3061,
            )

            return self._parent._cast(_3061.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalPlanetGearSteadyStateSynchronousResponse._Cast_CylindricalPlanetGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalPlanetGearSteadyStateSynchronousResponse._Cast_CylindricalPlanetGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalPlanetGearSteadyStateSynchronousResponse._Cast_CylindricalPlanetGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalPlanetGearSteadyStateSynchronousResponse._Cast_CylindricalPlanetGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearSteadyStateSynchronousResponse._Cast_CylindricalPlanetGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response(
            self: "CylindricalPlanetGearSteadyStateSynchronousResponse._Cast_CylindricalPlanetGearSteadyStateSynchronousResponse",
        ) -> "CylindricalPlanetGearSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearSteadyStateSynchronousResponse._Cast_CylindricalPlanetGearSteadyStateSynchronousResponse",
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
        instance_to_wrap: "CylindricalPlanetGearSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2525.CylindricalPlanetGear":
        """mastapy.system_model.part_model.gears.CylindricalPlanetGear

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
    ) -> "CylindricalPlanetGearSteadyStateSynchronousResponse._Cast_CylindricalPlanetGearSteadyStateSynchronousResponse":
        return self._Cast_CylindricalPlanetGearSteadyStateSynchronousResponse(self)
