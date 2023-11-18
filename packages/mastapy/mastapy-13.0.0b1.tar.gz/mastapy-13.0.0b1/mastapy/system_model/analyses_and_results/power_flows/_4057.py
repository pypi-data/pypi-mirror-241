"""ConceptCouplingHalfPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4068
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_HALF_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "ConceptCouplingHalfPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2580
    from mastapy.system_model.analyses_and_results.static_loads import _6837


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingHalfPowerFlow",)


Self = TypeVar("Self", bound="ConceptCouplingHalfPowerFlow")


class ConceptCouplingHalfPowerFlow(_4068.CouplingHalfPowerFlow):
    """ConceptCouplingHalfPowerFlow

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_HALF_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptCouplingHalfPowerFlow")

    class _Cast_ConceptCouplingHalfPowerFlow:
        """Special nested class for casting ConceptCouplingHalfPowerFlow to subclasses."""

        def __init__(
            self: "ConceptCouplingHalfPowerFlow._Cast_ConceptCouplingHalfPowerFlow",
            parent: "ConceptCouplingHalfPowerFlow",
        ):
            self._parent = parent

        @property
        def coupling_half_power_flow(
            self: "ConceptCouplingHalfPowerFlow._Cast_ConceptCouplingHalfPowerFlow",
        ):
            return self._parent._cast(_4068.CouplingHalfPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "ConceptCouplingHalfPowerFlow._Cast_ConceptCouplingHalfPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4109

            return self._parent._cast(_4109.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "ConceptCouplingHalfPowerFlow._Cast_ConceptCouplingHalfPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4055

            return self._parent._cast(_4055.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "ConceptCouplingHalfPowerFlow._Cast_ConceptCouplingHalfPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4111

            return self._parent._cast(_4111.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "ConceptCouplingHalfPowerFlow._Cast_ConceptCouplingHalfPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptCouplingHalfPowerFlow._Cast_ConceptCouplingHalfPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptCouplingHalfPowerFlow._Cast_ConceptCouplingHalfPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingHalfPowerFlow._Cast_ConceptCouplingHalfPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingHalfPowerFlow._Cast_ConceptCouplingHalfPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def concept_coupling_half_power_flow(
            self: "ConceptCouplingHalfPowerFlow._Cast_ConceptCouplingHalfPowerFlow",
        ) -> "ConceptCouplingHalfPowerFlow":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingHalfPowerFlow._Cast_ConceptCouplingHalfPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptCouplingHalfPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2580.ConceptCouplingHalf":
        """mastapy.system_model.part_model.couplings.ConceptCouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6837.ConceptCouplingHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingHalfLoadCase

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
    ) -> "ConceptCouplingHalfPowerFlow._Cast_ConceptCouplingHalfPowerFlow":
        return self._Cast_ConceptCouplingHalfPowerFlow(self)
