"""CouplingHalfSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3059,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "CouplingHalfSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2582


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="CouplingHalfSteadyStateSynchronousResponse")


class CouplingHalfSteadyStateSynchronousResponse(
    _3059.MountableComponentSteadyStateSynchronousResponse
):
    """CouplingHalfSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingHalfSteadyStateSynchronousResponse"
    )

    class _Cast_CouplingHalfSteadyStateSynchronousResponse:
        """Special nested class for casting CouplingHalfSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
            parent: "CouplingHalfSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _3059.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3006,
            )

            return self._parent._cast(_3006.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3061,
            )

            return self._parent._cast(_3061.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def clutch_half_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3003,
            )

            return self._parent._cast(_3003.ClutchHalfSteadyStateSynchronousResponse)

        @property
        def concept_coupling_half_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3008,
            )

            return self._parent._cast(
                _3008.ConceptCouplingHalfSteadyStateSynchronousResponse
            )

        @property
        def cvt_pulley_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3022,
            )

            return self._parent._cast(_3022.CVTPulleySteadyStateSynchronousResponse)

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3063,
            )

            return self._parent._cast(
                _3063.PartToPartShearCouplingHalfSteadyStateSynchronousResponse
            )

        @property
        def pulley_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3070,
            )

            return self._parent._cast(_3070.PulleySteadyStateSynchronousResponse)

        @property
        def rolling_ring_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3075,
            )

            return self._parent._cast(_3075.RollingRingSteadyStateSynchronousResponse)

        @property
        def spring_damper_half_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3085,
            )

            return self._parent._cast(
                _3085.SpringDamperHalfSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_half_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3098,
            )

            return self._parent._cast(
                _3098.SynchroniserHalfSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_part_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3099,
            )

            return self._parent._cast(
                _3099.SynchroniserPartSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_sleeve_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3100,
            )

            return self._parent._cast(
                _3100.SynchroniserSleeveSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_pump_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3103,
            )

            return self._parent._cast(
                _3103.TorqueConverterPumpSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_turbine_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3105,
            )

            return self._parent._cast(
                _3105.TorqueConverterTurbineSteadyStateSynchronousResponse
            )

        @property
        def coupling_half_steady_state_synchronous_response(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
        ) -> "CouplingHalfSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse",
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
        self: Self, instance_to_wrap: "CouplingHalfSteadyStateSynchronousResponse.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2582.CouplingHalf":
        """mastapy.system_model.part_model.couplings.CouplingHalf

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
    ) -> "CouplingHalfSteadyStateSynchronousResponse._Cast_CouplingHalfSteadyStateSynchronousResponse":
        return self._Cast_CouplingHalfSteadyStateSynchronousResponse(self)
