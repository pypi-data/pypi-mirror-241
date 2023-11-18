"""BevelDifferentialGearSetModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5132
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "BevelDifferentialGearSetModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2514
    from mastapy.system_model.analyses_and_results.static_loads import _6822
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5126,
        _5125,
    )


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearSetModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="BevelDifferentialGearSetModalAnalysisAtASpeed")


class BevelDifferentialGearSetModalAnalysisAtASpeed(
    _5132.BevelGearSetModalAnalysisAtASpeed
):
    """BevelDifferentialGearSetModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearSetModalAnalysisAtASpeed"
    )

    class _Cast_BevelDifferentialGearSetModalAnalysisAtASpeed:
        """Special nested class for casting BevelDifferentialGearSetModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "BevelDifferentialGearSetModalAnalysisAtASpeed._Cast_BevelDifferentialGearSetModalAnalysisAtASpeed",
            parent: "BevelDifferentialGearSetModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_modal_analysis_at_a_speed(
            self: "BevelDifferentialGearSetModalAnalysisAtASpeed._Cast_BevelDifferentialGearSetModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5132.BevelGearSetModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_set_modal_analysis_at_a_speed(
            self: "BevelDifferentialGearSetModalAnalysisAtASpeed._Cast_BevelDifferentialGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5120,
            )

            return self._parent._cast(
                _5120.AGMAGleasonConicalGearSetModalAnalysisAtASpeed
            )

        @property
        def conical_gear_set_modal_analysis_at_a_speed(
            self: "BevelDifferentialGearSetModalAnalysisAtASpeed._Cast_BevelDifferentialGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5148,
            )

            return self._parent._cast(_5148.ConicalGearSetModalAnalysisAtASpeed)

        @property
        def gear_set_modal_analysis_at_a_speed(
            self: "BevelDifferentialGearSetModalAnalysisAtASpeed._Cast_BevelDifferentialGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5174,
            )

            return self._parent._cast(_5174.GearSetModalAnalysisAtASpeed)

        @property
        def specialised_assembly_modal_analysis_at_a_speed(
            self: "BevelDifferentialGearSetModalAnalysisAtASpeed._Cast_BevelDifferentialGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5213,
            )

            return self._parent._cast(_5213.SpecialisedAssemblyModalAnalysisAtASpeed)

        @property
        def abstract_assembly_modal_analysis_at_a_speed(
            self: "BevelDifferentialGearSetModalAnalysisAtASpeed._Cast_BevelDifferentialGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5114,
            )

            return self._parent._cast(_5114.AbstractAssemblyModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "BevelDifferentialGearSetModalAnalysisAtASpeed._Cast_BevelDifferentialGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5194,
            )

            return self._parent._cast(_5194.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialGearSetModalAnalysisAtASpeed._Cast_BevelDifferentialGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialGearSetModalAnalysisAtASpeed._Cast_BevelDifferentialGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialGearSetModalAnalysisAtASpeed._Cast_BevelDifferentialGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearSetModalAnalysisAtASpeed._Cast_BevelDifferentialGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearSetModalAnalysisAtASpeed._Cast_BevelDifferentialGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_modal_analysis_at_a_speed(
            self: "BevelDifferentialGearSetModalAnalysisAtASpeed._Cast_BevelDifferentialGearSetModalAnalysisAtASpeed",
        ) -> "BevelDifferentialGearSetModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearSetModalAnalysisAtASpeed._Cast_BevelDifferentialGearSetModalAnalysisAtASpeed",
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
        instance_to_wrap: "BevelDifferentialGearSetModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2514.BevelDifferentialGearSet":
        """mastapy.system_model.part_model.gears.BevelDifferentialGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6822.BevelDifferentialGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_differential_gears_modal_analysis_at_a_speed(
        self: Self,
    ) -> "List[_5126.BevelDifferentialGearModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.BevelDifferentialGearModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialGearsModalAnalysisAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_differential_meshes_modal_analysis_at_a_speed(
        self: Self,
    ) -> "List[_5125.BevelDifferentialGearMeshModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.BevelDifferentialGearMeshModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialMeshesModalAnalysisAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialGearSetModalAnalysisAtASpeed._Cast_BevelDifferentialGearSetModalAnalysisAtASpeed":
        return self._Cast_BevelDifferentialGearSetModalAnalysisAtASpeed(self)
