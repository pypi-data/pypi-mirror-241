"""SynchroniserPartStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3799
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "SynchroniserPartStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2603


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartStabilityAnalysis",)


Self = TypeVar("Self", bound="SynchroniserPartStabilityAnalysis")


class SynchroniserPartStabilityAnalysis(_3799.CouplingHalfStabilityAnalysis):
    """SynchroniserPartStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserPartStabilityAnalysis")

    class _Cast_SynchroniserPartStabilityAnalysis:
        """Special nested class for casting SynchroniserPartStabilityAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserPartStabilityAnalysis._Cast_SynchroniserPartStabilityAnalysis",
            parent: "SynchroniserPartStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_stability_analysis(
            self: "SynchroniserPartStabilityAnalysis._Cast_SynchroniserPartStabilityAnalysis",
        ):
            return self._parent._cast(_3799.CouplingHalfStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "SynchroniserPartStabilityAnalysis._Cast_SynchroniserPartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3840,
            )

            return self._parent._cast(_3840.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "SynchroniserPartStabilityAnalysis._Cast_SynchroniserPartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3786,
            )

            return self._parent._cast(_3786.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "SynchroniserPartStabilityAnalysis._Cast_SynchroniserPartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3842,
            )

            return self._parent._cast(_3842.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserPartStabilityAnalysis._Cast_SynchroniserPartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserPartStabilityAnalysis._Cast_SynchroniserPartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserPartStabilityAnalysis._Cast_SynchroniserPartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserPartStabilityAnalysis._Cast_SynchroniserPartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartStabilityAnalysis._Cast_SynchroniserPartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def synchroniser_half_stability_analysis(
            self: "SynchroniserPartStabilityAnalysis._Cast_SynchroniserPartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3879,
            )

            return self._parent._cast(_3879.SynchroniserHalfStabilityAnalysis)

        @property
        def synchroniser_sleeve_stability_analysis(
            self: "SynchroniserPartStabilityAnalysis._Cast_SynchroniserPartStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3881,
            )

            return self._parent._cast(_3881.SynchroniserSleeveStabilityAnalysis)

        @property
        def synchroniser_part_stability_analysis(
            self: "SynchroniserPartStabilityAnalysis._Cast_SynchroniserPartStabilityAnalysis",
        ) -> "SynchroniserPartStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartStabilityAnalysis._Cast_SynchroniserPartStabilityAnalysis",
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
        self: Self, instance_to_wrap: "SynchroniserPartStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2603.SynchroniserPart":
        """mastapy.system_model.part_model.couplings.SynchroniserPart

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
    ) -> "SynchroniserPartStabilityAnalysis._Cast_SynchroniserPartStabilityAnalysis":
        return self._Cast_SynchroniserPartStabilityAnalysis(self)
