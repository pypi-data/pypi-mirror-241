"""SpiralBevelGearCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4741
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "SpiralBevelGearCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2541
    from mastapy.system_model.analyses_and_results.modal_analyses import _4681


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearCompoundModalAnalysis",)


Self = TypeVar("Self", bound="SpiralBevelGearCompoundModalAnalysis")


class SpiralBevelGearCompoundModalAnalysis(_4741.BevelGearCompoundModalAnalysis):
    """SpiralBevelGearCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpiralBevelGearCompoundModalAnalysis")

    class _Cast_SpiralBevelGearCompoundModalAnalysis:
        """Special nested class for casting SpiralBevelGearCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "SpiralBevelGearCompoundModalAnalysis._Cast_SpiralBevelGearCompoundModalAnalysis",
            parent: "SpiralBevelGearCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_modal_analysis(
            self: "SpiralBevelGearCompoundModalAnalysis._Cast_SpiralBevelGearCompoundModalAnalysis",
        ):
            return self._parent._cast(_4741.BevelGearCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis(
            self: "SpiralBevelGearCompoundModalAnalysis._Cast_SpiralBevelGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4729,
            )

            return self._parent._cast(_4729.AGMAGleasonConicalGearCompoundModalAnalysis)

        @property
        def conical_gear_compound_modal_analysis(
            self: "SpiralBevelGearCompoundModalAnalysis._Cast_SpiralBevelGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4757,
            )

            return self._parent._cast(_4757.ConicalGearCompoundModalAnalysis)

        @property
        def gear_compound_modal_analysis(
            self: "SpiralBevelGearCompoundModalAnalysis._Cast_SpiralBevelGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4783,
            )

            return self._parent._cast(_4783.GearCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "SpiralBevelGearCompoundModalAnalysis._Cast_SpiralBevelGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4802,
            )

            return self._parent._cast(_4802.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "SpiralBevelGearCompoundModalAnalysis._Cast_SpiralBevelGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4750,
            )

            return self._parent._cast(_4750.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "SpiralBevelGearCompoundModalAnalysis._Cast_SpiralBevelGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4804,
            )

            return self._parent._cast(_4804.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "SpiralBevelGearCompoundModalAnalysis._Cast_SpiralBevelGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpiralBevelGearCompoundModalAnalysis._Cast_SpiralBevelGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearCompoundModalAnalysis._Cast_SpiralBevelGearCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_compound_modal_analysis(
            self: "SpiralBevelGearCompoundModalAnalysis._Cast_SpiralBevelGearCompoundModalAnalysis",
        ) -> "SpiralBevelGearCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearCompoundModalAnalysis._Cast_SpiralBevelGearCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "SpiralBevelGearCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2541.SpiralBevelGear":
        """mastapy.system_model.part_model.gears.SpiralBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4681.SpiralBevelGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.SpiralBevelGearModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4681.SpiralBevelGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.SpiralBevelGearModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearCompoundModalAnalysis._Cast_SpiralBevelGearCompoundModalAnalysis":
        return self._Cast_SpiralBevelGearCompoundModalAnalysis(self)
