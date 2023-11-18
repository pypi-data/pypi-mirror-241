"""BeltDriveSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3080,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "BeltDriveSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2574
    from mastapy.system_model.analyses_and_results.static_loads import _6819


__docformat__ = "restructuredtext en"
__all__ = ("BeltDriveSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="BeltDriveSteadyStateSynchronousResponse")


class BeltDriveSteadyStateSynchronousResponse(
    _3080.SpecialisedAssemblySteadyStateSynchronousResponse
):
    """BeltDriveSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BeltDriveSteadyStateSynchronousResponse"
    )

    class _Cast_BeltDriveSteadyStateSynchronousResponse:
        """Special nested class for casting BeltDriveSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "BeltDriveSteadyStateSynchronousResponse._Cast_BeltDriveSteadyStateSynchronousResponse",
            parent: "BeltDriveSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def specialised_assembly_steady_state_synchronous_response(
            self: "BeltDriveSteadyStateSynchronousResponse._Cast_BeltDriveSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _3080.SpecialisedAssemblySteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_steady_state_synchronous_response(
            self: "BeltDriveSteadyStateSynchronousResponse._Cast_BeltDriveSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2981,
            )

            return self._parent._cast(
                _2981.AbstractAssemblySteadyStateSynchronousResponse
            )

        @property
        def part_steady_state_synchronous_response(
            self: "BeltDriveSteadyStateSynchronousResponse._Cast_BeltDriveSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3061,
            )

            return self._parent._cast(_3061.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "BeltDriveSteadyStateSynchronousResponse._Cast_BeltDriveSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BeltDriveSteadyStateSynchronousResponse._Cast_BeltDriveSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BeltDriveSteadyStateSynchronousResponse._Cast_BeltDriveSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BeltDriveSteadyStateSynchronousResponse._Cast_BeltDriveSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltDriveSteadyStateSynchronousResponse._Cast_BeltDriveSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cvt_steady_state_synchronous_response(
            self: "BeltDriveSteadyStateSynchronousResponse._Cast_BeltDriveSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3023,
            )

            return self._parent._cast(_3023.CVTSteadyStateSynchronousResponse)

        @property
        def belt_drive_steady_state_synchronous_response(
            self: "BeltDriveSteadyStateSynchronousResponse._Cast_BeltDriveSteadyStateSynchronousResponse",
        ) -> "BeltDriveSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "BeltDriveSteadyStateSynchronousResponse._Cast_BeltDriveSteadyStateSynchronousResponse",
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
        self: Self, instance_to_wrap: "BeltDriveSteadyStateSynchronousResponse.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2574.BeltDrive":
        """mastapy.system_model.part_model.couplings.BeltDrive

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6819.BeltDriveLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BeltDriveLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BeltDriveSteadyStateSynchronousResponse._Cast_BeltDriveSteadyStateSynchronousResponse":
        return self._Cast_BeltDriveSteadyStateSynchronousResponse(self)
