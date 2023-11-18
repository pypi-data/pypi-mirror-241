"""BevelDifferentialPlanetGearModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4866,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "BevelDifferentialPlanetGearModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2515


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialPlanetGearModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="BevelDifferentialPlanetGearModalAnalysisAtAStiffness")


class BevelDifferentialPlanetGearModalAnalysisAtAStiffness(
    _4866.BevelDifferentialGearModalAnalysisAtAStiffness
):
    """BevelDifferentialPlanetGearModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialPlanetGearModalAnalysisAtAStiffness"
    )

    class _Cast_BevelDifferentialPlanetGearModalAnalysisAtAStiffness:
        """Special nested class for casting BevelDifferentialPlanetGearModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "BevelDifferentialPlanetGearModalAnalysisAtAStiffness._Cast_BevelDifferentialPlanetGearModalAnalysisAtAStiffness",
            parent: "BevelDifferentialPlanetGearModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialPlanetGearModalAnalysisAtAStiffness._Cast_BevelDifferentialPlanetGearModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(
                _4866.BevelDifferentialGearModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialPlanetGearModalAnalysisAtAStiffness._Cast_BevelDifferentialPlanetGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4871,
            )

            return self._parent._cast(_4871.BevelGearModalAnalysisAtAStiffness)

        @property
        def agma_gleason_conical_gear_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialPlanetGearModalAnalysisAtAStiffness._Cast_BevelDifferentialPlanetGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4859,
            )

            return self._parent._cast(
                _4859.AGMAGleasonConicalGearModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialPlanetGearModalAnalysisAtAStiffness._Cast_BevelDifferentialPlanetGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4887,
            )

            return self._parent._cast(_4887.ConicalGearModalAnalysisAtAStiffness)

        @property
        def gear_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialPlanetGearModalAnalysisAtAStiffness._Cast_BevelDifferentialPlanetGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4914,
            )

            return self._parent._cast(_4914.GearModalAnalysisAtAStiffness)

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialPlanetGearModalAnalysisAtAStiffness._Cast_BevelDifferentialPlanetGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4933,
            )

            return self._parent._cast(_4933.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialPlanetGearModalAnalysisAtAStiffness._Cast_BevelDifferentialPlanetGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4879,
            )

            return self._parent._cast(_4879.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialPlanetGearModalAnalysisAtAStiffness._Cast_BevelDifferentialPlanetGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4935,
            )

            return self._parent._cast(_4935.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialPlanetGearModalAnalysisAtAStiffness._Cast_BevelDifferentialPlanetGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialPlanetGearModalAnalysisAtAStiffness._Cast_BevelDifferentialPlanetGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialPlanetGearModalAnalysisAtAStiffness._Cast_BevelDifferentialPlanetGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialPlanetGearModalAnalysisAtAStiffness._Cast_BevelDifferentialPlanetGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialPlanetGearModalAnalysisAtAStiffness._Cast_BevelDifferentialPlanetGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialPlanetGearModalAnalysisAtAStiffness._Cast_BevelDifferentialPlanetGearModalAnalysisAtAStiffness",
        ) -> "BevelDifferentialPlanetGearModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialPlanetGearModalAnalysisAtAStiffness._Cast_BevelDifferentialPlanetGearModalAnalysisAtAStiffness",
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
        instance_to_wrap: "BevelDifferentialPlanetGearModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2515.BevelDifferentialPlanetGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear

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
    ) -> "BevelDifferentialPlanetGearModalAnalysisAtAStiffness._Cast_BevelDifferentialPlanetGearModalAnalysisAtAStiffness":
        return self._Cast_BevelDifferentialPlanetGearModalAnalysisAtAStiffness(self)
