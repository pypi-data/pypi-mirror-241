"""BoltedJointPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4132
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "BoltedJointPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2441
    from mastapy.system_model.analyses_and_results.static_loads import _6828


__docformat__ = "restructuredtext en"
__all__ = ("BoltedJointPowerFlow",)


Self = TypeVar("Self", bound="BoltedJointPowerFlow")


class BoltedJointPowerFlow(_4132.SpecialisedAssemblyPowerFlow):
    """BoltedJointPowerFlow

    This is a mastapy class.
    """

    TYPE = _BOLTED_JOINT_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BoltedJointPowerFlow")

    class _Cast_BoltedJointPowerFlow:
        """Special nested class for casting BoltedJointPowerFlow to subclasses."""

        def __init__(
            self: "BoltedJointPowerFlow._Cast_BoltedJointPowerFlow",
            parent: "BoltedJointPowerFlow",
        ):
            self._parent = parent

        @property
        def specialised_assembly_power_flow(
            self: "BoltedJointPowerFlow._Cast_BoltedJointPowerFlow",
        ):
            return self._parent._cast(_4132.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "BoltedJointPowerFlow._Cast_BoltedJointPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4030

            return self._parent._cast(_4030.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(self: "BoltedJointPowerFlow._Cast_BoltedJointPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4111

            return self._parent._cast(_4111.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "BoltedJointPowerFlow._Cast_BoltedJointPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self: "BoltedJointPowerFlow._Cast_BoltedJointPowerFlow"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(self: "BoltedJointPowerFlow._Cast_BoltedJointPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BoltedJointPowerFlow._Cast_BoltedJointPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BoltedJointPowerFlow._Cast_BoltedJointPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bolted_joint_power_flow(
            self: "BoltedJointPowerFlow._Cast_BoltedJointPowerFlow",
        ) -> "BoltedJointPowerFlow":
            return self._parent

        def __getattr__(
            self: "BoltedJointPowerFlow._Cast_BoltedJointPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BoltedJointPowerFlow.TYPE"):
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
    def cast_to(self: Self) -> "BoltedJointPowerFlow._Cast_BoltedJointPowerFlow":
        return self._Cast_BoltedJointPowerFlow(self)
