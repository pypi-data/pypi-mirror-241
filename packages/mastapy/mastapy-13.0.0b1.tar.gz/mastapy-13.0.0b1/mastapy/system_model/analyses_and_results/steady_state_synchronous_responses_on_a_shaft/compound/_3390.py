"""BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3378,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3259,
    )


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
)


class BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft(
    _3378.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
):
    """BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            return self._parent._cast(
                _3378.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3406,
            )

            return self._parent._cast(
                _3406.ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3432,
            )

            return self._parent._cast(
                _3432.GearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3438,
            )

            return self._parent._cast(
                _3438.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3408,
            )

            return self._parent._cast(
                _3408.ConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_compound_analysis(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3385,
            )

            return self._parent._cast(
                _3385.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3473,
            )

            return self._parent._cast(
                _3473.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3479,
            )

            return self._parent._cast(
                _3479.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3482,
            )

            return self._parent._cast(
                _3482.StraightBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3500,
            )

            return self._parent._cast(
                _3500.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3259.BevelGearMeshSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.BevelGearMeshSteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3259.BevelGearMeshSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.BevelGearMeshSteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft(
            self
        )
