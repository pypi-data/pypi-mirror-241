"""ConceptCouplingPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4069
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "ConceptCouplingPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2579
    from mastapy.system_model.analyses_and_results.static_loads import _6838


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingPowerFlow",)


Self = TypeVar("Self", bound="ConceptCouplingPowerFlow")


class ConceptCouplingPowerFlow(_4069.CouplingPowerFlow):
    """ConceptCouplingPowerFlow

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptCouplingPowerFlow")

    class _Cast_ConceptCouplingPowerFlow:
        """Special nested class for casting ConceptCouplingPowerFlow to subclasses."""

        def __init__(
            self: "ConceptCouplingPowerFlow._Cast_ConceptCouplingPowerFlow",
            parent: "ConceptCouplingPowerFlow",
        ):
            self._parent = parent

        @property
        def coupling_power_flow(
            self: "ConceptCouplingPowerFlow._Cast_ConceptCouplingPowerFlow",
        ):
            return self._parent._cast(_4069.CouplingPowerFlow)

        @property
        def specialised_assembly_power_flow(
            self: "ConceptCouplingPowerFlow._Cast_ConceptCouplingPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4132

            return self._parent._cast(_4132.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "ConceptCouplingPowerFlow._Cast_ConceptCouplingPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4030

            return self._parent._cast(_4030.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(
            self: "ConceptCouplingPowerFlow._Cast_ConceptCouplingPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4111

            return self._parent._cast(_4111.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "ConceptCouplingPowerFlow._Cast_ConceptCouplingPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptCouplingPowerFlow._Cast_ConceptCouplingPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptCouplingPowerFlow._Cast_ConceptCouplingPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingPowerFlow._Cast_ConceptCouplingPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingPowerFlow._Cast_ConceptCouplingPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def concept_coupling_power_flow(
            self: "ConceptCouplingPowerFlow._Cast_ConceptCouplingPowerFlow",
        ) -> "ConceptCouplingPowerFlow":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingPowerFlow._Cast_ConceptCouplingPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptCouplingPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2579.ConceptCoupling":
        """mastapy.system_model.part_model.couplings.ConceptCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6838.ConceptCouplingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingLoadCase

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
    ) -> "ConceptCouplingPowerFlow._Cast_ConceptCouplingPowerFlow":
        return self._Cast_ConceptCouplingPowerFlow(self)
