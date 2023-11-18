"""PlanetCarrierModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4933,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "PlanetCarrierModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2467
    from mastapy.system_model.analyses_and_results.static_loads import _6933


__docformat__ = "restructuredtext en"
__all__ = ("PlanetCarrierModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="PlanetCarrierModalAnalysisAtAStiffness")


class PlanetCarrierModalAnalysisAtAStiffness(
    _4933.MountableComponentModalAnalysisAtAStiffness
):
    """PlanetCarrierModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _PLANET_CARRIER_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetCarrierModalAnalysisAtAStiffness"
    )

    class _Cast_PlanetCarrierModalAnalysisAtAStiffness:
        """Special nested class for casting PlanetCarrierModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "PlanetCarrierModalAnalysisAtAStiffness._Cast_PlanetCarrierModalAnalysisAtAStiffness",
            parent: "PlanetCarrierModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "PlanetCarrierModalAnalysisAtAStiffness._Cast_PlanetCarrierModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(_4933.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "PlanetCarrierModalAnalysisAtAStiffness._Cast_PlanetCarrierModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4879,
            )

            return self._parent._cast(_4879.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "PlanetCarrierModalAnalysisAtAStiffness._Cast_PlanetCarrierModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4935,
            )

            return self._parent._cast(_4935.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "PlanetCarrierModalAnalysisAtAStiffness._Cast_PlanetCarrierModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetCarrierModalAnalysisAtAStiffness._Cast_PlanetCarrierModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetCarrierModalAnalysisAtAStiffness._Cast_PlanetCarrierModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetCarrierModalAnalysisAtAStiffness._Cast_PlanetCarrierModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetCarrierModalAnalysisAtAStiffness._Cast_PlanetCarrierModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def planet_carrier_modal_analysis_at_a_stiffness(
            self: "PlanetCarrierModalAnalysisAtAStiffness._Cast_PlanetCarrierModalAnalysisAtAStiffness",
        ) -> "PlanetCarrierModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "PlanetCarrierModalAnalysisAtAStiffness._Cast_PlanetCarrierModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "PlanetCarrierModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2467.PlanetCarrier":
        """mastapy.system_model.part_model.PlanetCarrier

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6933.PlanetCarrierLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PlanetCarrierLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PlanetCarrierModalAnalysisAtAStiffness._Cast_PlanetCarrierModalAnalysisAtAStiffness":
        return self._Cast_PlanetCarrierModalAnalysisAtAStiffness(self)
