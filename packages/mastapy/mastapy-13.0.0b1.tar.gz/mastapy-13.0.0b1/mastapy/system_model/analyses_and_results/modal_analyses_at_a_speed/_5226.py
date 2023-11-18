"""StraightBevelPlanetGearModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5221
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "StraightBevelPlanetGearModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2547


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGearModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="StraightBevelPlanetGearModalAnalysisAtASpeed")


class StraightBevelPlanetGearModalAnalysisAtASpeed(
    _5221.StraightBevelDiffGearModalAnalysisAtASpeed
):
    """StraightBevelPlanetGearModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelPlanetGearModalAnalysisAtASpeed"
    )

    class _Cast_StraightBevelPlanetGearModalAnalysisAtASpeed:
        """Special nested class for casting StraightBevelPlanetGearModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGearModalAnalysisAtASpeed._Cast_StraightBevelPlanetGearModalAnalysisAtASpeed",
            parent: "StraightBevelPlanetGearModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_modal_analysis_at_a_speed(
            self: "StraightBevelPlanetGearModalAnalysisAtASpeed._Cast_StraightBevelPlanetGearModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5221.StraightBevelDiffGearModalAnalysisAtASpeed)

        @property
        def bevel_gear_modal_analysis_at_a_speed(
            self: "StraightBevelPlanetGearModalAnalysisAtASpeed._Cast_StraightBevelPlanetGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5131,
            )

            return self._parent._cast(_5131.BevelGearModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_modal_analysis_at_a_speed(
            self: "StraightBevelPlanetGearModalAnalysisAtASpeed._Cast_StraightBevelPlanetGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5119,
            )

            return self._parent._cast(_5119.AGMAGleasonConicalGearModalAnalysisAtASpeed)

        @property
        def conical_gear_modal_analysis_at_a_speed(
            self: "StraightBevelPlanetGearModalAnalysisAtASpeed._Cast_StraightBevelPlanetGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5147,
            )

            return self._parent._cast(_5147.ConicalGearModalAnalysisAtASpeed)

        @property
        def gear_modal_analysis_at_a_speed(
            self: "StraightBevelPlanetGearModalAnalysisAtASpeed._Cast_StraightBevelPlanetGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5173,
            )

            return self._parent._cast(_5173.GearModalAnalysisAtASpeed)

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "StraightBevelPlanetGearModalAnalysisAtASpeed._Cast_StraightBevelPlanetGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5192,
            )

            return self._parent._cast(_5192.MountableComponentModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "StraightBevelPlanetGearModalAnalysisAtASpeed._Cast_StraightBevelPlanetGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5139,
            )

            return self._parent._cast(_5139.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "StraightBevelPlanetGearModalAnalysisAtASpeed._Cast_StraightBevelPlanetGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5194,
            )

            return self._parent._cast(_5194.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelPlanetGearModalAnalysisAtASpeed._Cast_StraightBevelPlanetGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelPlanetGearModalAnalysisAtASpeed._Cast_StraightBevelPlanetGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelPlanetGearModalAnalysisAtASpeed._Cast_StraightBevelPlanetGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelPlanetGearModalAnalysisAtASpeed._Cast_StraightBevelPlanetGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelPlanetGearModalAnalysisAtASpeed._Cast_StraightBevelPlanetGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_modal_analysis_at_a_speed(
            self: "StraightBevelPlanetGearModalAnalysisAtASpeed._Cast_StraightBevelPlanetGearModalAnalysisAtASpeed",
        ) -> "StraightBevelPlanetGearModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGearModalAnalysisAtASpeed._Cast_StraightBevelPlanetGearModalAnalysisAtASpeed",
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
        instance_to_wrap: "StraightBevelPlanetGearModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2547.StraightBevelPlanetGear":
        """mastapy.system_model.part_model.gears.StraightBevelPlanetGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelPlanetGearModalAnalysisAtASpeed._Cast_StraightBevelPlanetGearModalAnalysisAtASpeed":
        return self._Cast_StraightBevelPlanetGearModalAnalysisAtASpeed(self)
