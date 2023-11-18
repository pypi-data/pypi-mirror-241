"""TorqueConverterTurbineStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3799
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "TorqueConverterTurbineStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2608
    from mastapy.system_model.analyses_and_results.static_loads import _6973


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterTurbineStabilityAnalysis",)


Self = TypeVar("Self", bound="TorqueConverterTurbineStabilityAnalysis")


class TorqueConverterTurbineStabilityAnalysis(_3799.CouplingHalfStabilityAnalysis):
    """TorqueConverterTurbineStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterTurbineStabilityAnalysis"
    )

    class _Cast_TorqueConverterTurbineStabilityAnalysis:
        """Special nested class for casting TorqueConverterTurbineStabilityAnalysis to subclasses."""

        def __init__(
            self: "TorqueConverterTurbineStabilityAnalysis._Cast_TorqueConverterTurbineStabilityAnalysis",
            parent: "TorqueConverterTurbineStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_stability_analysis(
            self: "TorqueConverterTurbineStabilityAnalysis._Cast_TorqueConverterTurbineStabilityAnalysis",
        ):
            return self._parent._cast(_3799.CouplingHalfStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "TorqueConverterTurbineStabilityAnalysis._Cast_TorqueConverterTurbineStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3840,
            )

            return self._parent._cast(_3840.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "TorqueConverterTurbineStabilityAnalysis._Cast_TorqueConverterTurbineStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3786,
            )

            return self._parent._cast(_3786.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "TorqueConverterTurbineStabilityAnalysis._Cast_TorqueConverterTurbineStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3842,
            )

            return self._parent._cast(_3842.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "TorqueConverterTurbineStabilityAnalysis._Cast_TorqueConverterTurbineStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "TorqueConverterTurbineStabilityAnalysis._Cast_TorqueConverterTurbineStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterTurbineStabilityAnalysis._Cast_TorqueConverterTurbineStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterTurbineStabilityAnalysis._Cast_TorqueConverterTurbineStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterTurbineStabilityAnalysis._Cast_TorqueConverterTurbineStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def torque_converter_turbine_stability_analysis(
            self: "TorqueConverterTurbineStabilityAnalysis._Cast_TorqueConverterTurbineStabilityAnalysis",
        ) -> "TorqueConverterTurbineStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "TorqueConverterTurbineStabilityAnalysis._Cast_TorqueConverterTurbineStabilityAnalysis",
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
        self: Self, instance_to_wrap: "TorqueConverterTurbineStabilityAnalysis.TYPE"
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
    ) -> "TorqueConverterTurbineStabilityAnalysis._Cast_TorqueConverterTurbineStabilityAnalysis":
        return self._Cast_TorqueConverterTurbineStabilityAnalysis(self)
