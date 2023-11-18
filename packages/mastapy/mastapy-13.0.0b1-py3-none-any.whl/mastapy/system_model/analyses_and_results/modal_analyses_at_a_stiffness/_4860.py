"""AGMAGleasonConicalGearSetModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4888,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "AGMAGleasonConicalGearSetModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2512


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetModalAnalysisAtAStiffness")


class AGMAGleasonConicalGearSetModalAnalysisAtAStiffness(
    _4888.ConicalGearSetModalAnalysisAtAStiffness
):
    """AGMAGleasonConicalGearSetModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearSetModalAnalysisAtAStiffness"
    )

    class _Cast_AGMAGleasonConicalGearSetModalAnalysisAtAStiffness:
        """Special nested class for casting AGMAGleasonConicalGearSetModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearSetModalAnalysisAtAStiffness",
            parent: "AGMAGleasonConicalGearSetModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def conical_gear_set_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearSetModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(_4888.ConicalGearSetModalAnalysisAtAStiffness)

        @property
        def gear_set_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4915,
            )

            return self._parent._cast(_4915.GearSetModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4954,
            )

            return self._parent._cast(
                _4954.SpecialisedAssemblyModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4854,
            )

            return self._parent._cast(_4854.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4935,
            )

            return self._parent._cast(_4935.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4867,
            )

            return self._parent._cast(
                _4867.BevelDifferentialGearSetModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4872,
            )

            return self._parent._cast(_4872.BevelGearSetModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_set_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4919,
            )

            return self._parent._cast(_4919.HypoidGearSetModalAnalysisAtAStiffness)

        @property
        def spiral_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4957,
            )

            return self._parent._cast(_4957.SpiralBevelGearSetModalAnalysisAtAStiffness)

        @property
        def straight_bevel_diff_gear_set_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4963,
            )

            return self._parent._cast(
                _4963.StraightBevelDiffGearSetModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4966,
            )

            return self._parent._cast(
                _4966.StraightBevelGearSetModalAnalysisAtAStiffness
            )

        @property
        def zerol_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4984,
            )

            return self._parent._cast(_4984.ZerolBevelGearSetModalAnalysisAtAStiffness)

        @property
        def agma_gleason_conical_gear_set_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearSetModalAnalysisAtAStiffness",
        ) -> "AGMAGleasonConicalGearSetModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearSetModalAnalysisAtAStiffness",
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
        instance_to_wrap: "AGMAGleasonConicalGearSetModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2512.AGMAGleasonConicalGearSet":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearSetModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearSetModalAnalysisAtAStiffness":
        return self._Cast_AGMAGleasonConicalGearSetModalAnalysisAtAStiffness(self)
