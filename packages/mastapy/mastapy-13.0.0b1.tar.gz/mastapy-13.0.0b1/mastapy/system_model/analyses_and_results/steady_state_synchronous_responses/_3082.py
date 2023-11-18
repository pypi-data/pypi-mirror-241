"""SpiralBevelGearSetSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _2998,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "SpiralBevelGearSetSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2542
    from mastapy.system_model.analyses_and_results.static_loads import _6953
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3083,
        _3081,
    )


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearSetSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="SpiralBevelGearSetSteadyStateSynchronousResponse")


class SpiralBevelGearSetSteadyStateSynchronousResponse(
    _2998.BevelGearSetSteadyStateSynchronousResponse
):
    """SpiralBevelGearSetSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearSetSteadyStateSynchronousResponse"
    )

    class _Cast_SpiralBevelGearSetSteadyStateSynchronousResponse:
        """Special nested class for casting SpiralBevelGearSetSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "SpiralBevelGearSetSteadyStateSynchronousResponse._Cast_SpiralBevelGearSetSteadyStateSynchronousResponse",
            parent: "SpiralBevelGearSetSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_steady_state_synchronous_response(
            self: "SpiralBevelGearSetSteadyStateSynchronousResponse._Cast_SpiralBevelGearSetSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(_2998.BevelGearSetSteadyStateSynchronousResponse)

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response(
            self: "SpiralBevelGearSetSteadyStateSynchronousResponse._Cast_SpiralBevelGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2986,
            )

            return self._parent._cast(
                _2986.AGMAGleasonConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_set_steady_state_synchronous_response(
            self: "SpiralBevelGearSetSteadyStateSynchronousResponse._Cast_SpiralBevelGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3014,
            )

            return self._parent._cast(
                _3014.ConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def gear_set_steady_state_synchronous_response(
            self: "SpiralBevelGearSetSteadyStateSynchronousResponse._Cast_SpiralBevelGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3041,
            )

            return self._parent._cast(_3041.GearSetSteadyStateSynchronousResponse)

        @property
        def specialised_assembly_steady_state_synchronous_response(
            self: "SpiralBevelGearSetSteadyStateSynchronousResponse._Cast_SpiralBevelGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3080,
            )

            return self._parent._cast(
                _3080.SpecialisedAssemblySteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_steady_state_synchronous_response(
            self: "SpiralBevelGearSetSteadyStateSynchronousResponse._Cast_SpiralBevelGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2981,
            )

            return self._parent._cast(
                _2981.AbstractAssemblySteadyStateSynchronousResponse
            )

        @property
        def part_steady_state_synchronous_response(
            self: "SpiralBevelGearSetSteadyStateSynchronousResponse._Cast_SpiralBevelGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3061,
            )

            return self._parent._cast(_3061.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "SpiralBevelGearSetSteadyStateSynchronousResponse._Cast_SpiralBevelGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpiralBevelGearSetSteadyStateSynchronousResponse._Cast_SpiralBevelGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpiralBevelGearSetSteadyStateSynchronousResponse._Cast_SpiralBevelGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearSetSteadyStateSynchronousResponse._Cast_SpiralBevelGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearSetSteadyStateSynchronousResponse._Cast_SpiralBevelGearSetSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response(
            self: "SpiralBevelGearSetSteadyStateSynchronousResponse._Cast_SpiralBevelGearSetSteadyStateSynchronousResponse",
        ) -> "SpiralBevelGearSetSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearSetSteadyStateSynchronousResponse._Cast_SpiralBevelGearSetSteadyStateSynchronousResponse",
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
        instance_to_wrap: "SpiralBevelGearSetSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2542.SpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.SpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6953.SpiralBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def spiral_bevel_gears_steady_state_synchronous_response(
        self: Self,
    ) -> "List[_3083.SpiralBevelGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.SpiralBevelGearSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelGearsSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spiral_bevel_meshes_steady_state_synchronous_response(
        self: Self,
    ) -> "List[_3081.SpiralBevelGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.SpiralBevelGearMeshSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelMeshesSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearSetSteadyStateSynchronousResponse._Cast_SpiralBevelGearSetSteadyStateSynchronousResponse":
        return self._Cast_SpiralBevelGearSetSteadyStateSynchronousResponse(self)
