"""RollingRingDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6313
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "RollingRingDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2594
    from mastapy.system_model.analyses_and_results.static_loads import _6945


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingDynamicAnalysis",)


Self = TypeVar("Self", bound="RollingRingDynamicAnalysis")


class RollingRingDynamicAnalysis(_6313.CouplingHalfDynamicAnalysis):
    """RollingRingDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollingRingDynamicAnalysis")

    class _Cast_RollingRingDynamicAnalysis:
        """Special nested class for casting RollingRingDynamicAnalysis to subclasses."""

        def __init__(
            self: "RollingRingDynamicAnalysis._Cast_RollingRingDynamicAnalysis",
            parent: "RollingRingDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_dynamic_analysis(
            self: "RollingRingDynamicAnalysis._Cast_RollingRingDynamicAnalysis",
        ):
            return self._parent._cast(_6313.CouplingHalfDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "RollingRingDynamicAnalysis._Cast_RollingRingDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6353

            return self._parent._cast(_6353.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "RollingRingDynamicAnalysis._Cast_RollingRingDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6299

            return self._parent._cast(_6299.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "RollingRingDynamicAnalysis._Cast_RollingRingDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6355

            return self._parent._cast(_6355.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "RollingRingDynamicAnalysis._Cast_RollingRingDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "RollingRingDynamicAnalysis._Cast_RollingRingDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RollingRingDynamicAnalysis._Cast_RollingRingDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RollingRingDynamicAnalysis._Cast_RollingRingDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingDynamicAnalysis._Cast_RollingRingDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingDynamicAnalysis._Cast_RollingRingDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def rolling_ring_dynamic_analysis(
            self: "RollingRingDynamicAnalysis._Cast_RollingRingDynamicAnalysis",
        ) -> "RollingRingDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "RollingRingDynamicAnalysis._Cast_RollingRingDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RollingRingDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2594.RollingRing":
        """mastapy.system_model.part_model.couplings.RollingRing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6945.RollingRingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RollingRingLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[RollingRingDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.RollingRingDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "RollingRingDynamicAnalysis._Cast_RollingRingDynamicAnalysis":
        return self._Cast_RollingRingDynamicAnalysis(self)
