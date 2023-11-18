"""PartToPartShearCouplingStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3800
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "PartToPartShearCouplingStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2586
    from mastapy.system_model.analyses_and_results.static_loads import _6929


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingStabilityAnalysis",)


Self = TypeVar("Self", bound="PartToPartShearCouplingStabilityAnalysis")


class PartToPartShearCouplingStabilityAnalysis(_3800.CouplingStabilityAnalysis):
    """PartToPartShearCouplingStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartToPartShearCouplingStabilityAnalysis"
    )

    class _Cast_PartToPartShearCouplingStabilityAnalysis:
        """Special nested class for casting PartToPartShearCouplingStabilityAnalysis to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingStabilityAnalysis._Cast_PartToPartShearCouplingStabilityAnalysis",
            parent: "PartToPartShearCouplingStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_stability_analysis(
            self: "PartToPartShearCouplingStabilityAnalysis._Cast_PartToPartShearCouplingStabilityAnalysis",
        ):
            return self._parent._cast(_3800.CouplingStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(
            self: "PartToPartShearCouplingStabilityAnalysis._Cast_PartToPartShearCouplingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3861,
            )

            return self._parent._cast(_3861.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "PartToPartShearCouplingStabilityAnalysis._Cast_PartToPartShearCouplingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3761,
            )

            return self._parent._cast(_3761.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "PartToPartShearCouplingStabilityAnalysis._Cast_PartToPartShearCouplingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3842,
            )

            return self._parent._cast(_3842.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PartToPartShearCouplingStabilityAnalysis._Cast_PartToPartShearCouplingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartToPartShearCouplingStabilityAnalysis._Cast_PartToPartShearCouplingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartToPartShearCouplingStabilityAnalysis._Cast_PartToPartShearCouplingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingStabilityAnalysis._Cast_PartToPartShearCouplingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingStabilityAnalysis._Cast_PartToPartShearCouplingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_stability_analysis(
            self: "PartToPartShearCouplingStabilityAnalysis._Cast_PartToPartShearCouplingStabilityAnalysis",
        ) -> "PartToPartShearCouplingStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingStabilityAnalysis._Cast_PartToPartShearCouplingStabilityAnalysis",
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
        self: Self, instance_to_wrap: "PartToPartShearCouplingStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2586.PartToPartShearCoupling":
        """mastapy.system_model.part_model.couplings.PartToPartShearCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6929.PartToPartShearCouplingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingLoadCase

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
    ) -> "PartToPartShearCouplingStabilityAnalysis._Cast_PartToPartShearCouplingStabilityAnalysis":
        return self._Cast_PartToPartShearCouplingStabilityAnalysis(self)
