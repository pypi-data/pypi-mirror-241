"""CylindricalGearSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3042,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "CylindricalGearSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2523
    from mastapy.system_model.analyses_and_results.static_loads import _6859


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="CylindricalGearSteadyStateSynchronousResponse")


class CylindricalGearSteadyStateSynchronousResponse(
    _3042.GearSteadyStateSynchronousResponse
):
    """CylindricalGearSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearSteadyStateSynchronousResponse"
    )

    class _Cast_CylindricalGearSteadyStateSynchronousResponse:
        """Special nested class for casting CylindricalGearSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "CylindricalGearSteadyStateSynchronousResponse._Cast_CylindricalGearSteadyStateSynchronousResponse",
            parent: "CylindricalGearSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def gear_steady_state_synchronous_response(
            self: "CylindricalGearSteadyStateSynchronousResponse._Cast_CylindricalGearSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(_3042.GearSteadyStateSynchronousResponse)

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "CylindricalGearSteadyStateSynchronousResponse._Cast_CylindricalGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3059,
            )

            return self._parent._cast(
                _3059.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "CylindricalGearSteadyStateSynchronousResponse._Cast_CylindricalGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3006,
            )

            return self._parent._cast(_3006.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "CylindricalGearSteadyStateSynchronousResponse._Cast_CylindricalGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3061,
            )

            return self._parent._cast(_3061.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalGearSteadyStateSynchronousResponse._Cast_CylindricalGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalGearSteadyStateSynchronousResponse._Cast_CylindricalGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalGearSteadyStateSynchronousResponse._Cast_CylindricalGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearSteadyStateSynchronousResponse._Cast_CylindricalGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearSteadyStateSynchronousResponse._Cast_CylindricalGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response(
            self: "CylindricalGearSteadyStateSynchronousResponse._Cast_CylindricalGearSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3031,
            )

            return self._parent._cast(
                _3031.CylindricalPlanetGearSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_steady_state_synchronous_response(
            self: "CylindricalGearSteadyStateSynchronousResponse._Cast_CylindricalGearSteadyStateSynchronousResponse",
        ) -> "CylindricalGearSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSteadyStateSynchronousResponse._Cast_CylindricalGearSteadyStateSynchronousResponse",
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
        instance_to_wrap: "CylindricalGearSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2523.CylindricalGear":
        """mastapy.system_model.part_model.gears.CylindricalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6859.CylindricalGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(
        self: Self,
    ) -> "List[CylindricalGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.CylindricalGearSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearSteadyStateSynchronousResponse._Cast_CylindricalGearSteadyStateSynchronousResponse":
        return self._Cast_CylindricalGearSteadyStateSynchronousResponse(self)
