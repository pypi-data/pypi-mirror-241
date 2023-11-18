"""StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3132,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2544
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3091,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3219,
        _3220,
    )


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self", bound="StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse"
)


class StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse(
    _3132.BevelGearSetCompoundSteadyStateSynchronousResponse
):
    """StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse",
            parent: "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response(
            self: "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _3132.BevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response(
            self: "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3120,
            )

            return self._parent._cast(
                _3120.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_set_compound_steady_state_synchronous_response(
            self: "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3148,
            )

            return self._parent._cast(
                _3148.ConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_set_compound_steady_state_synchronous_response(
            self: "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3174,
            )

            return self._parent._cast(
                _3174.GearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response(
            self: "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3212,
            )

            return self._parent._cast(
                _3212.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response(
            self: "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3114,
            )

            return self._parent._cast(
                _3114.AbstractAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3193,
            )

            return self._parent._cast(_3193.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response(
            self: "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2544.StraightBevelDiffGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2544.StraightBevelDiffGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3091.StraightBevelDiffGearSetSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.StraightBevelDiffGearSetSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_gears_compound_steady_state_synchronous_response(
        self: Self,
    ) -> "List[_3219.StraightBevelDiffGearCompoundSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound.StraightBevelDiffGearCompoundSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearsCompoundSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_meshes_compound_steady_state_synchronous_response(
        self: Self,
    ) -> "List[_3220.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.StraightBevelDiffMeshesCompoundSteadyStateSynchronousResponse
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3091.StraightBevelDiffGearSetSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.StraightBevelDiffGearSetSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse._Cast_StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse":
        return (
            self._Cast_StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse(
                self
            )
        )
