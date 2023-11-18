"""StraightBevelGearSetCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5262,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "StraightBevelGearSetCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2546
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5225,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5352,
        _5353,
    )


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearSetCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="StraightBevelGearSetCompoundModalAnalysisAtASpeed")


class StraightBevelGearSetCompoundModalAnalysisAtASpeed(
    _5262.BevelGearSetCompoundModalAnalysisAtASpeed
):
    """StraightBevelGearSetCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelGearSetCompoundModalAnalysisAtASpeed"
    )

    class _Cast_StraightBevelGearSetCompoundModalAnalysisAtASpeed:
        """Special nested class for casting StraightBevelGearSetCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "StraightBevelGearSetCompoundModalAnalysisAtASpeed._Cast_StraightBevelGearSetCompoundModalAnalysisAtASpeed",
            parent: "StraightBevelGearSetCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "StraightBevelGearSetCompoundModalAnalysisAtASpeed._Cast_StraightBevelGearSetCompoundModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5262.BevelGearSetCompoundModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "StraightBevelGearSetCompoundModalAnalysisAtASpeed._Cast_StraightBevelGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5250,
            )

            return self._parent._cast(
                _5250.AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "StraightBevelGearSetCompoundModalAnalysisAtASpeed._Cast_StraightBevelGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5278,
            )

            return self._parent._cast(_5278.ConicalGearSetCompoundModalAnalysisAtASpeed)

        @property
        def gear_set_compound_modal_analysis_at_a_speed(
            self: "StraightBevelGearSetCompoundModalAnalysisAtASpeed._Cast_StraightBevelGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5304,
            )

            return self._parent._cast(_5304.GearSetCompoundModalAnalysisAtASpeed)

        @property
        def specialised_assembly_compound_modal_analysis_at_a_speed(
            self: "StraightBevelGearSetCompoundModalAnalysisAtASpeed._Cast_StraightBevelGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5342,
            )

            return self._parent._cast(
                _5342.SpecialisedAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_speed(
            self: "StraightBevelGearSetCompoundModalAnalysisAtASpeed._Cast_StraightBevelGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5244,
            )

            return self._parent._cast(
                _5244.AbstractAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "StraightBevelGearSetCompoundModalAnalysisAtASpeed._Cast_StraightBevelGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5323,
            )

            return self._parent._cast(_5323.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "StraightBevelGearSetCompoundModalAnalysisAtASpeed._Cast_StraightBevelGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelGearSetCompoundModalAnalysisAtASpeed._Cast_StraightBevelGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearSetCompoundModalAnalysisAtASpeed._Cast_StraightBevelGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "StraightBevelGearSetCompoundModalAnalysisAtASpeed._Cast_StraightBevelGearSetCompoundModalAnalysisAtASpeed",
        ) -> "StraightBevelGearSetCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearSetCompoundModalAnalysisAtASpeed._Cast_StraightBevelGearSetCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "StraightBevelGearSetCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2546.StraightBevelGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2546.StraightBevelGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelGearSet

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
    ) -> "List[_5225.StraightBevelGearSetModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.StraightBevelGearSetModalAnalysisAtASpeed]

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
    def straight_bevel_gears_compound_modal_analysis_at_a_speed(
        self: Self,
    ) -> "List[_5352.StraightBevelGearCompoundModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound.StraightBevelGearCompoundModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelGearsCompoundModalAnalysisAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_meshes_compound_modal_analysis_at_a_speed(
        self: Self,
    ) -> "List[_5353.StraightBevelGearMeshCompoundModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound.StraightBevelGearMeshCompoundModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelMeshesCompoundModalAnalysisAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5225.StraightBevelGearSetModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.StraightBevelGearSetModalAnalysisAtASpeed]

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
    ) -> "StraightBevelGearSetCompoundModalAnalysisAtASpeed._Cast_StraightBevelGearSetCompoundModalAnalysisAtASpeed":
        return self._Cast_StraightBevelGearSetCompoundModalAnalysisAtASpeed(self)
