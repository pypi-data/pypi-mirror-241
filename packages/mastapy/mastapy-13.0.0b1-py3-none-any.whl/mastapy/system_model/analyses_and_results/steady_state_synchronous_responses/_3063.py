"""PartToPartShearCouplingHalfSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3019,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "PartToPartShearCouplingHalfSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2587
    from mastapy.system_model.analyses_and_results.static_loads import _6928


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingHalfSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self", bound="PartToPartShearCouplingHalfSteadyStateSynchronousResponse"
)


class PartToPartShearCouplingHalfSteadyStateSynchronousResponse(
    _3019.CouplingHalfSteadyStateSynchronousResponse
):
    """PartToPartShearCouplingHalfSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponse",
    )

    class _Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponse:
        """Special nested class for casting PartToPartShearCouplingHalfSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingHalfSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponse",
            parent: "PartToPartShearCouplingHalfSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def coupling_half_steady_state_synchronous_response(
            self: "PartToPartShearCouplingHalfSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(_3019.CouplingHalfSteadyStateSynchronousResponse)

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "PartToPartShearCouplingHalfSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3059,
            )

            return self._parent._cast(
                _3059.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "PartToPartShearCouplingHalfSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3006,
            )

            return self._parent._cast(_3006.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "PartToPartShearCouplingHalfSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3061,
            )

            return self._parent._cast(_3061.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "PartToPartShearCouplingHalfSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartToPartShearCouplingHalfSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartToPartShearCouplingHalfSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingHalfSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingHalfSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response(
            self: "PartToPartShearCouplingHalfSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponse",
        ) -> "PartToPartShearCouplingHalfSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingHalfSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponse",
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
        instance_to_wrap: "PartToPartShearCouplingHalfSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2587.PartToPartShearCouplingHalf":
        """mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6928.PartToPartShearCouplingHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingHalfLoadCase

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
    ) -> "PartToPartShearCouplingHalfSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponse":
        return self._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponse(
            self
        )
