"""ExternalCADModelSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3006,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "ExternalCADModelSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2450
    from mastapy.system_model.analyses_and_results.static_loads import _6881


__docformat__ = "restructuredtext en"
__all__ = ("ExternalCADModelSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="ExternalCADModelSteadyStateSynchronousResponse")


class ExternalCADModelSteadyStateSynchronousResponse(
    _3006.ComponentSteadyStateSynchronousResponse
):
    """ExternalCADModelSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _EXTERNAL_CAD_MODEL_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ExternalCADModelSteadyStateSynchronousResponse"
    )

    class _Cast_ExternalCADModelSteadyStateSynchronousResponse:
        """Special nested class for casting ExternalCADModelSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ExternalCADModelSteadyStateSynchronousResponse._Cast_ExternalCADModelSteadyStateSynchronousResponse",
            parent: "ExternalCADModelSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def component_steady_state_synchronous_response(
            self: "ExternalCADModelSteadyStateSynchronousResponse._Cast_ExternalCADModelSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(_3006.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "ExternalCADModelSteadyStateSynchronousResponse._Cast_ExternalCADModelSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3061,
            )

            return self._parent._cast(_3061.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "ExternalCADModelSteadyStateSynchronousResponse._Cast_ExternalCADModelSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ExternalCADModelSteadyStateSynchronousResponse._Cast_ExternalCADModelSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ExternalCADModelSteadyStateSynchronousResponse._Cast_ExternalCADModelSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ExternalCADModelSteadyStateSynchronousResponse._Cast_ExternalCADModelSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ExternalCADModelSteadyStateSynchronousResponse._Cast_ExternalCADModelSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def external_cad_model_steady_state_synchronous_response(
            self: "ExternalCADModelSteadyStateSynchronousResponse._Cast_ExternalCADModelSteadyStateSynchronousResponse",
        ) -> "ExternalCADModelSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ExternalCADModelSteadyStateSynchronousResponse._Cast_ExternalCADModelSteadyStateSynchronousResponse",
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
        instance_to_wrap: "ExternalCADModelSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2450.ExternalCADModel":
        """mastapy.system_model.part_model.ExternalCADModel

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6881.ExternalCADModelLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ExternalCADModelLoadCase

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
    ) -> "ExternalCADModelSteadyStateSynchronousResponse._Cast_ExternalCADModelSteadyStateSynchronousResponse":
        return self._Cast_ExternalCADModelSteadyStateSynchronousResponse(self)
