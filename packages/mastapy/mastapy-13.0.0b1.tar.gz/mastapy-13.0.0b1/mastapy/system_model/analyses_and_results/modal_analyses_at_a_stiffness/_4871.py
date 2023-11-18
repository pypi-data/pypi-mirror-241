"""BevelGearModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4859,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "BevelGearModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2517


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="BevelGearModalAnalysisAtAStiffness")


class BevelGearModalAnalysisAtAStiffness(
    _4859.AGMAGleasonConicalGearModalAnalysisAtAStiffness
):
    """BevelGearModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearModalAnalysisAtAStiffness")

    class _Cast_BevelGearModalAnalysisAtAStiffness:
        """Special nested class for casting BevelGearModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "BevelGearModalAnalysisAtAStiffness._Cast_BevelGearModalAnalysisAtAStiffness",
            parent: "BevelGearModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_modal_analysis_at_a_stiffness(
            self: "BevelGearModalAnalysisAtAStiffness._Cast_BevelGearModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(
                _4859.AGMAGleasonConicalGearModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_modal_analysis_at_a_stiffness(
            self: "BevelGearModalAnalysisAtAStiffness._Cast_BevelGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4887,
            )

            return self._parent._cast(_4887.ConicalGearModalAnalysisAtAStiffness)

        @property
        def gear_modal_analysis_at_a_stiffness(
            self: "BevelGearModalAnalysisAtAStiffness._Cast_BevelGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4914,
            )

            return self._parent._cast(_4914.GearModalAnalysisAtAStiffness)

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "BevelGearModalAnalysisAtAStiffness._Cast_BevelGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4933,
            )

            return self._parent._cast(_4933.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "BevelGearModalAnalysisAtAStiffness._Cast_BevelGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4879,
            )

            return self._parent._cast(_4879.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "BevelGearModalAnalysisAtAStiffness._Cast_BevelGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4935,
            )

            return self._parent._cast(_4935.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "BevelGearModalAnalysisAtAStiffness._Cast_BevelGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelGearModalAnalysisAtAStiffness._Cast_BevelGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelGearModalAnalysisAtAStiffness._Cast_BevelGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearModalAnalysisAtAStiffness._Cast_BevelGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearModalAnalysisAtAStiffness._Cast_BevelGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_modal_analysis_at_a_stiffness(
            self: "BevelGearModalAnalysisAtAStiffness._Cast_BevelGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4866,
            )

            return self._parent._cast(
                _4866.BevelDifferentialGearModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_planet_gear_modal_analysis_at_a_stiffness(
            self: "BevelGearModalAnalysisAtAStiffness._Cast_BevelGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4868,
            )

            return self._parent._cast(
                _4868.BevelDifferentialPlanetGearModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_sun_gear_modal_analysis_at_a_stiffness(
            self: "BevelGearModalAnalysisAtAStiffness._Cast_BevelGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4869,
            )

            return self._parent._cast(
                _4869.BevelDifferentialSunGearModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_modal_analysis_at_a_stiffness(
            self: "BevelGearModalAnalysisAtAStiffness._Cast_BevelGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4956,
            )

            return self._parent._cast(_4956.SpiralBevelGearModalAnalysisAtAStiffness)

        @property
        def straight_bevel_diff_gear_modal_analysis_at_a_stiffness(
            self: "BevelGearModalAnalysisAtAStiffness._Cast_BevelGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4962,
            )

            return self._parent._cast(
                _4962.StraightBevelDiffGearModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_modal_analysis_at_a_stiffness(
            self: "BevelGearModalAnalysisAtAStiffness._Cast_BevelGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4965,
            )

            return self._parent._cast(_4965.StraightBevelGearModalAnalysisAtAStiffness)

        @property
        def straight_bevel_planet_gear_modal_analysis_at_a_stiffness(
            self: "BevelGearModalAnalysisAtAStiffness._Cast_BevelGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4967,
            )

            return self._parent._cast(
                _4967.StraightBevelPlanetGearModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_sun_gear_modal_analysis_at_a_stiffness(
            self: "BevelGearModalAnalysisAtAStiffness._Cast_BevelGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4968,
            )

            return self._parent._cast(
                _4968.StraightBevelSunGearModalAnalysisAtAStiffness
            )

        @property
        def zerol_bevel_gear_modal_analysis_at_a_stiffness(
            self: "BevelGearModalAnalysisAtAStiffness._Cast_BevelGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4983,
            )

            return self._parent._cast(_4983.ZerolBevelGearModalAnalysisAtAStiffness)

        @property
        def bevel_gear_modal_analysis_at_a_stiffness(
            self: "BevelGearModalAnalysisAtAStiffness._Cast_BevelGearModalAnalysisAtAStiffness",
        ) -> "BevelGearModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "BevelGearModalAnalysisAtAStiffness._Cast_BevelGearModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "BevelGearModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2517.BevelGear":
        """mastapy.system_model.part_model.gears.BevelGear

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
    ) -> "BevelGearModalAnalysisAtAStiffness._Cast_BevelGearModalAnalysisAtAStiffness":
        return self._Cast_BevelGearModalAnalysisAtAStiffness(self)
