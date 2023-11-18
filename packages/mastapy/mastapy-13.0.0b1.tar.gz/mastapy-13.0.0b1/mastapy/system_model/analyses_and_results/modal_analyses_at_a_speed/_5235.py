"""TorqueConverterTurbineModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5152
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "TorqueConverterTurbineModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2608
    from mastapy.system_model.analyses_and_results.static_loads import _6973


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterTurbineModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="TorqueConverterTurbineModalAnalysisAtASpeed")


class TorqueConverterTurbineModalAnalysisAtASpeed(
    _5152.CouplingHalfModalAnalysisAtASpeed
):
    """TorqueConverterTurbineModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterTurbineModalAnalysisAtASpeed"
    )

    class _Cast_TorqueConverterTurbineModalAnalysisAtASpeed:
        """Special nested class for casting TorqueConverterTurbineModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "TorqueConverterTurbineModalAnalysisAtASpeed._Cast_TorqueConverterTurbineModalAnalysisAtASpeed",
            parent: "TorqueConverterTurbineModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_half_modal_analysis_at_a_speed(
            self: "TorqueConverterTurbineModalAnalysisAtASpeed._Cast_TorqueConverterTurbineModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5152.CouplingHalfModalAnalysisAtASpeed)

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "TorqueConverterTurbineModalAnalysisAtASpeed._Cast_TorqueConverterTurbineModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5192,
            )

            return self._parent._cast(_5192.MountableComponentModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "TorqueConverterTurbineModalAnalysisAtASpeed._Cast_TorqueConverterTurbineModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5139,
            )

            return self._parent._cast(_5139.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "TorqueConverterTurbineModalAnalysisAtASpeed._Cast_TorqueConverterTurbineModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5194,
            )

            return self._parent._cast(_5194.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "TorqueConverterTurbineModalAnalysisAtASpeed._Cast_TorqueConverterTurbineModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "TorqueConverterTurbineModalAnalysisAtASpeed._Cast_TorqueConverterTurbineModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterTurbineModalAnalysisAtASpeed._Cast_TorqueConverterTurbineModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterTurbineModalAnalysisAtASpeed._Cast_TorqueConverterTurbineModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterTurbineModalAnalysisAtASpeed._Cast_TorqueConverterTurbineModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def torque_converter_turbine_modal_analysis_at_a_speed(
            self: "TorqueConverterTurbineModalAnalysisAtASpeed._Cast_TorqueConverterTurbineModalAnalysisAtASpeed",
        ) -> "TorqueConverterTurbineModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "TorqueConverterTurbineModalAnalysisAtASpeed._Cast_TorqueConverterTurbineModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "TorqueConverterTurbineModalAnalysisAtASpeed.TYPE"
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
    ) -> "TorqueConverterTurbineModalAnalysisAtASpeed._Cast_TorqueConverterTurbineModalAnalysisAtASpeed":
        return self._Cast_TorqueConverterTurbineModalAnalysisAtASpeed(self)
