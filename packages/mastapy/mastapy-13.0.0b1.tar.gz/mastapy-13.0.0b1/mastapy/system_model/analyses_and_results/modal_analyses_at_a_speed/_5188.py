"""KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5182
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_MODAL_ANALYSIS_AT_A_SPEED = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
        "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2539
    from mastapy.system_model.analyses_and_results.static_loads import _6918
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5187,
        _5186,
    )


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed"
)


class KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed(
    _5182.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed
):
    """KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed",
        ):
            return self._parent._cast(
                _5182.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed
            )

        @property
        def conical_gear_set_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5148,
            )

            return self._parent._cast(_5148.ConicalGearSetModalAnalysisAtASpeed)

        @property
        def gear_set_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5174,
            )

            return self._parent._cast(_5174.GearSetModalAnalysisAtASpeed)

        @property
        def specialised_assembly_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5213,
            )

            return self._parent._cast(_5213.SpecialisedAssemblyModalAnalysisAtASpeed)

        @property
        def abstract_assembly_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5114,
            )

            return self._parent._cast(_5114.AbstractAssemblyModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5194,
            )

            return self._parent._cast(_5194.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(
        self: Self,
    ) -> "_2539.KlingelnbergCycloPalloidSpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(
        self: Self,
    ) -> "_6918.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gears_modal_analysis_at_a_speed(
        self: Self,
    ) -> "List[_5187.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearsModalAnalysisAtASpeed
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_meshes_modal_analysis_at_a_speed(
        self: Self,
    ) -> "List[_5186.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshesModalAnalysisAtASpeed
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed":
        return (
            self._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed(
                self
            )
        )
