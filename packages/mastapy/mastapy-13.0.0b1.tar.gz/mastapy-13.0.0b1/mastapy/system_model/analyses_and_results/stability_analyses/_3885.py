"""TorqueConverterStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3800
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "TorqueConverterStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2605
    from mastapy.system_model.analyses_and_results.static_loads import _6971


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterStabilityAnalysis",)


Self = TypeVar("Self", bound="TorqueConverterStabilityAnalysis")


class TorqueConverterStabilityAnalysis(_3800.CouplingStabilityAnalysis):
    """TorqueConverterStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TorqueConverterStabilityAnalysis")

    class _Cast_TorqueConverterStabilityAnalysis:
        """Special nested class for casting TorqueConverterStabilityAnalysis to subclasses."""

        def __init__(
            self: "TorqueConverterStabilityAnalysis._Cast_TorqueConverterStabilityAnalysis",
            parent: "TorqueConverterStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_stability_analysis(
            self: "TorqueConverterStabilityAnalysis._Cast_TorqueConverterStabilityAnalysis",
        ):
            return self._parent._cast(_3800.CouplingStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(
            self: "TorqueConverterStabilityAnalysis._Cast_TorqueConverterStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3861,
            )

            return self._parent._cast(_3861.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "TorqueConverterStabilityAnalysis._Cast_TorqueConverterStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3761,
            )

            return self._parent._cast(_3761.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "TorqueConverterStabilityAnalysis._Cast_TorqueConverterStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3842,
            )

            return self._parent._cast(_3842.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "TorqueConverterStabilityAnalysis._Cast_TorqueConverterStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "TorqueConverterStabilityAnalysis._Cast_TorqueConverterStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterStabilityAnalysis._Cast_TorqueConverterStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterStabilityAnalysis._Cast_TorqueConverterStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterStabilityAnalysis._Cast_TorqueConverterStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def torque_converter_stability_analysis(
            self: "TorqueConverterStabilityAnalysis._Cast_TorqueConverterStabilityAnalysis",
        ) -> "TorqueConverterStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "TorqueConverterStabilityAnalysis._Cast_TorqueConverterStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TorqueConverterStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2605.TorqueConverter":
        """mastapy.system_model.part_model.couplings.TorqueConverter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6971.TorqueConverterLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "TorqueConverterStabilityAnalysis._Cast_TorqueConverterStabilityAnalysis":
        return self._Cast_TorqueConverterStabilityAnalysis(self)
