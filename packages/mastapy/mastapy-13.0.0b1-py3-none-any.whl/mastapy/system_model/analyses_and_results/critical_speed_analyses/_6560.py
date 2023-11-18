"""BoltedJointCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6641
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "BoltedJointCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2441
    from mastapy.system_model.analyses_and_results.static_loads import _6828


__docformat__ = "restructuredtext en"
__all__ = ("BoltedJointCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="BoltedJointCriticalSpeedAnalysis")


class BoltedJointCriticalSpeedAnalysis(_6641.SpecialisedAssemblyCriticalSpeedAnalysis):
    """BoltedJointCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _BOLTED_JOINT_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BoltedJointCriticalSpeedAnalysis")

    class _Cast_BoltedJointCriticalSpeedAnalysis:
        """Special nested class for casting BoltedJointCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "BoltedJointCriticalSpeedAnalysis._Cast_BoltedJointCriticalSpeedAnalysis",
            parent: "BoltedJointCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_critical_speed_analysis(
            self: "BoltedJointCriticalSpeedAnalysis._Cast_BoltedJointCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6641.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "BoltedJointCriticalSpeedAnalysis._Cast_BoltedJointCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6540,
            )

            return self._parent._cast(_6540.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "BoltedJointCriticalSpeedAnalysis._Cast_BoltedJointCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6622,
            )

            return self._parent._cast(_6622.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BoltedJointCriticalSpeedAnalysis._Cast_BoltedJointCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BoltedJointCriticalSpeedAnalysis._Cast_BoltedJointCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BoltedJointCriticalSpeedAnalysis._Cast_BoltedJointCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BoltedJointCriticalSpeedAnalysis._Cast_BoltedJointCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BoltedJointCriticalSpeedAnalysis._Cast_BoltedJointCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bolted_joint_critical_speed_analysis(
            self: "BoltedJointCriticalSpeedAnalysis._Cast_BoltedJointCriticalSpeedAnalysis",
        ) -> "BoltedJointCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "BoltedJointCriticalSpeedAnalysis._Cast_BoltedJointCriticalSpeedAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BoltedJointCriticalSpeedAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2441.BoltedJoint":
        """mastapy.system_model.part_model.BoltedJoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6828.BoltedJointLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BoltedJointLoadCase

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
    ) -> "BoltedJointCriticalSpeedAnalysis._Cast_BoltedJointCriticalSpeedAnalysis":
        return self._Cast_BoltedJointCriticalSpeedAnalysis(self)
