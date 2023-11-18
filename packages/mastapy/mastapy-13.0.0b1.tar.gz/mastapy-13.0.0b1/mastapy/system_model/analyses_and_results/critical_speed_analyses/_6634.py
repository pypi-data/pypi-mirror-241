"""RollingRingAssemblyCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6641
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "RollingRingAssemblyCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2595
    from mastapy.system_model.analyses_and_results.static_loads import _6943


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingAssemblyCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="RollingRingAssemblyCriticalSpeedAnalysis")


class RollingRingAssemblyCriticalSpeedAnalysis(
    _6641.SpecialisedAssemblyCriticalSpeedAnalysis
):
    """RollingRingAssemblyCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_ASSEMBLY_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RollingRingAssemblyCriticalSpeedAnalysis"
    )

    class _Cast_RollingRingAssemblyCriticalSpeedAnalysis:
        """Special nested class for casting RollingRingAssemblyCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "RollingRingAssemblyCriticalSpeedAnalysis._Cast_RollingRingAssemblyCriticalSpeedAnalysis",
            parent: "RollingRingAssemblyCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_critical_speed_analysis(
            self: "RollingRingAssemblyCriticalSpeedAnalysis._Cast_RollingRingAssemblyCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6641.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "RollingRingAssemblyCriticalSpeedAnalysis._Cast_RollingRingAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6540,
            )

            return self._parent._cast(_6540.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "RollingRingAssemblyCriticalSpeedAnalysis._Cast_RollingRingAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6622,
            )

            return self._parent._cast(_6622.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "RollingRingAssemblyCriticalSpeedAnalysis._Cast_RollingRingAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RollingRingAssemblyCriticalSpeedAnalysis._Cast_RollingRingAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RollingRingAssemblyCriticalSpeedAnalysis._Cast_RollingRingAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingAssemblyCriticalSpeedAnalysis._Cast_RollingRingAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingAssemblyCriticalSpeedAnalysis._Cast_RollingRingAssemblyCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def rolling_ring_assembly_critical_speed_analysis(
            self: "RollingRingAssemblyCriticalSpeedAnalysis._Cast_RollingRingAssemblyCriticalSpeedAnalysis",
        ) -> "RollingRingAssemblyCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "RollingRingAssemblyCriticalSpeedAnalysis._Cast_RollingRingAssemblyCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "RollingRingAssemblyCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2595.RollingRingAssembly":
        """mastapy.system_model.part_model.couplings.RollingRingAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6943.RollingRingAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RollingRingAssemblyLoadCase

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
    ) -> "RollingRingAssemblyCriticalSpeedAnalysis._Cast_RollingRingAssemblyCriticalSpeedAnalysis":
        return self._Cast_RollingRingAssemblyCriticalSpeedAnalysis(self)
