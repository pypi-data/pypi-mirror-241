"""CylindricalPlanetGearCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3161,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "CylindricalPlanetGearCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3031,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearCompoundSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self", bound="CylindricalPlanetGearCompoundSteadyStateSynchronousResponse"
)


class CylindricalPlanetGearCompoundSteadyStateSynchronousResponse(
    _3161.CylindricalGearCompoundSteadyStateSynchronousResponse
):
    """CylindricalPlanetGearCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting CylindricalPlanetGearCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponse._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponse",
            parent: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_compound_steady_state_synchronous_response(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponse._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _3161.CylindricalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_compound_steady_state_synchronous_response(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponse._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3172,
            )

            return self._parent._cast(_3172.GearCompoundSteadyStateSynchronousResponse)

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponse._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3191,
            )

            return self._parent._cast(
                _3191.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponse._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3139,
            )

            return self._parent._cast(
                _3139.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponse._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3193,
            )

            return self._parent._cast(_3193.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponse._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponse._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponse._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_compound_steady_state_synchronous_response(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponse._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponse",
        ) -> "CylindricalPlanetGearCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponse._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "CylindricalPlanetGearCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3031.CylindricalPlanetGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.CylindricalPlanetGearSteadyStateSynchronousResponse]

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
    ) -> "List[_3031.CylindricalPlanetGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.CylindricalPlanetGearSteadyStateSynchronousResponse]

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
    ) -> "CylindricalPlanetGearCompoundSteadyStateSynchronousResponse._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponse":
        return self._Cast_CylindricalPlanetGearCompoundSteadyStateSynchronousResponse(
            self
        )
