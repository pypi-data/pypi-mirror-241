"""CouplingPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4132
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "CouplingPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2581


__docformat__ = "restructuredtext en"
__all__ = ("CouplingPowerFlow",)


Self = TypeVar("Self", bound="CouplingPowerFlow")


class CouplingPowerFlow(_4132.SpecialisedAssemblyPowerFlow):
    """CouplingPowerFlow

    This is a mastapy class.
    """

    TYPE = _COUPLING_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingPowerFlow")

    class _Cast_CouplingPowerFlow:
        """Special nested class for casting CouplingPowerFlow to subclasses."""

        def __init__(
            self: "CouplingPowerFlow._Cast_CouplingPowerFlow",
            parent: "CouplingPowerFlow",
        ):
            self._parent = parent

        @property
        def specialised_assembly_power_flow(
            self: "CouplingPowerFlow._Cast_CouplingPowerFlow",
        ):
            return self._parent._cast(_4132.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "CouplingPowerFlow._Cast_CouplingPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4030

            return self._parent._cast(_4030.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(self: "CouplingPowerFlow._Cast_CouplingPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4111

            return self._parent._cast(_4111.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "CouplingPowerFlow._Cast_CouplingPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self: "CouplingPowerFlow._Cast_CouplingPowerFlow"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(self: "CouplingPowerFlow._Cast_CouplingPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingPowerFlow._Cast_CouplingPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self: "CouplingPowerFlow._Cast_CouplingPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def clutch_power_flow(self: "CouplingPowerFlow._Cast_CouplingPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4053

            return self._parent._cast(_4053.ClutchPowerFlow)

        @property
        def concept_coupling_power_flow(
            self: "CouplingPowerFlow._Cast_CouplingPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4058

            return self._parent._cast(_4058.ConceptCouplingPowerFlow)

        @property
        def part_to_part_shear_coupling_power_flow(
            self: "CouplingPowerFlow._Cast_CouplingPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4114

            return self._parent._cast(_4114.PartToPartShearCouplingPowerFlow)

        @property
        def spring_damper_power_flow(self: "CouplingPowerFlow._Cast_CouplingPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4138

            return self._parent._cast(_4138.SpringDamperPowerFlow)

        @property
        def torque_converter_power_flow(
            self: "CouplingPowerFlow._Cast_CouplingPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4153

            return self._parent._cast(_4153.TorqueConverterPowerFlow)

        @property
        def coupling_power_flow(
            self: "CouplingPowerFlow._Cast_CouplingPowerFlow",
        ) -> "CouplingPowerFlow":
            return self._parent

        def __getattr__(self: "CouplingPowerFlow._Cast_CouplingPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2581.Coupling":
        """mastapy.system_model.part_model.couplings.Coupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "CouplingPowerFlow._Cast_CouplingPowerFlow":
        return self._Cast_CouplingPowerFlow(self)
