"""TorqueConverterTurbineModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4892,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "TorqueConverterTurbineModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2608
    from mastapy.system_model.analyses_and_results.static_loads import _6973


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterTurbineModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="TorqueConverterTurbineModalAnalysisAtAStiffness")


class TorqueConverterTurbineModalAnalysisAtAStiffness(
    _4892.CouplingHalfModalAnalysisAtAStiffness
):
    """TorqueConverterTurbineModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterTurbineModalAnalysisAtAStiffness"
    )

    class _Cast_TorqueConverterTurbineModalAnalysisAtAStiffness:
        """Special nested class for casting TorqueConverterTurbineModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "TorqueConverterTurbineModalAnalysisAtAStiffness._Cast_TorqueConverterTurbineModalAnalysisAtAStiffness",
            parent: "TorqueConverterTurbineModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def coupling_half_modal_analysis_at_a_stiffness(
            self: "TorqueConverterTurbineModalAnalysisAtAStiffness._Cast_TorqueConverterTurbineModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(_4892.CouplingHalfModalAnalysisAtAStiffness)

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "TorqueConverterTurbineModalAnalysisAtAStiffness._Cast_TorqueConverterTurbineModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4933,
            )

            return self._parent._cast(_4933.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "TorqueConverterTurbineModalAnalysisAtAStiffness._Cast_TorqueConverterTurbineModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4879,
            )

            return self._parent._cast(_4879.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "TorqueConverterTurbineModalAnalysisAtAStiffness._Cast_TorqueConverterTurbineModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4935,
            )

            return self._parent._cast(_4935.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "TorqueConverterTurbineModalAnalysisAtAStiffness._Cast_TorqueConverterTurbineModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "TorqueConverterTurbineModalAnalysisAtAStiffness._Cast_TorqueConverterTurbineModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterTurbineModalAnalysisAtAStiffness._Cast_TorqueConverterTurbineModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterTurbineModalAnalysisAtAStiffness._Cast_TorqueConverterTurbineModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterTurbineModalAnalysisAtAStiffness._Cast_TorqueConverterTurbineModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def torque_converter_turbine_modal_analysis_at_a_stiffness(
            self: "TorqueConverterTurbineModalAnalysisAtAStiffness._Cast_TorqueConverterTurbineModalAnalysisAtAStiffness",
        ) -> "TorqueConverterTurbineModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "TorqueConverterTurbineModalAnalysisAtAStiffness._Cast_TorqueConverterTurbineModalAnalysisAtAStiffness",
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
        instance_to_wrap: "TorqueConverterTurbineModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2608.TorqueConverterTurbine":
        """mastapy.system_model.part_model.couplings.TorqueConverterTurbine

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6973.TorqueConverterTurbineLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterTurbineLoadCase

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
    ) -> "TorqueConverterTurbineModalAnalysisAtAStiffness._Cast_TorqueConverterTurbineModalAnalysisAtAStiffness":
        return self._Cast_TorqueConverterTurbineModalAnalysisAtAStiffness(self)
