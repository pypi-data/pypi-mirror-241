"""StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5262,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2544
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5222,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5349,
        _5350,
    )


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed")


class StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed(
    _5262.BevelGearSetCompoundModalAnalysisAtASpeed
):
    """StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed"
    )

    class _Cast_StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed:
        """Special nested class for casting StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed",
            parent: "StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5262.BevelGearSetCompoundModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5250,
            )

            return self._parent._cast(
                _5250.AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5278,
            )

            return self._parent._cast(_5278.ConicalGearSetCompoundModalAnalysisAtASpeed)

        @property
        def gear_set_compound_modal_analysis_at_a_speed(
            self: "StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5304,
            )

            return self._parent._cast(_5304.GearSetCompoundModalAnalysisAtASpeed)

        @property
        def specialised_assembly_compound_modal_analysis_at_a_speed(
            self: "StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5342,
            )

            return self._parent._cast(
                _5342.SpecialisedAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_speed(
            self: "StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5244,
            )

            return self._parent._cast(
                _5244.AbstractAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5323,
            )

            return self._parent._cast(_5323.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis_at_a_speed(
            self: "StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed",
        ) -> "StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed.TYPE",
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
    ) -> "List[_5222.StraightBevelDiffGearSetModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.StraightBevelDiffGearSetModalAnalysisAtASpeed]

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
    def straight_bevel_diff_gears_compound_modal_analysis_at_a_speed(
        self: Self,
    ) -> "List[_5349.StraightBevelDiffGearCompoundModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound.StraightBevelDiffGearCompoundModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearsCompoundModalAnalysisAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_meshes_compound_modal_analysis_at_a_speed(
        self: Self,
    ) -> "List[_5350.StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound.StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffMeshesCompoundModalAnalysisAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5222.StraightBevelDiffGearSetModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.StraightBevelDiffGearSetModalAnalysisAtASpeed]

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
    ) -> "StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed":
        return self._Cast_StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed(self)
