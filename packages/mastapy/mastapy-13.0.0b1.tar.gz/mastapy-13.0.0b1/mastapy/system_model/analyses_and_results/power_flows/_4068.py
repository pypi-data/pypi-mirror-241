"""CouplingHalfPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4109
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "CouplingHalfPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2582


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfPowerFlow",)


Self = TypeVar("Self", bound="CouplingHalfPowerFlow")


class CouplingHalfPowerFlow(_4109.MountableComponentPowerFlow):
    """CouplingHalfPowerFlow

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfPowerFlow")

    class _Cast_CouplingHalfPowerFlow:
        """Special nested class for casting CouplingHalfPowerFlow to subclasses."""

        def __init__(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
            parent: "CouplingHalfPowerFlow",
        ):
            self._parent = parent

        @property
        def mountable_component_power_flow(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
        ):
            return self._parent._cast(_4109.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4055

            return self._parent._cast(_4055.ComponentPowerFlow)

        @property
        def part_power_flow(self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4111

            return self._parent._cast(_4111.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def clutch_half_power_flow(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4052

            return self._parent._cast(_4052.ClutchHalfPowerFlow)

        @property
        def concept_coupling_half_power_flow(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4057

            return self._parent._cast(_4057.ConceptCouplingHalfPowerFlow)

        @property
        def cvt_pulley_power_flow(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4072

            return self._parent._cast(_4072.CVTPulleyPowerFlow)

        @property
        def part_to_part_shear_coupling_half_power_flow(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4113

            return self._parent._cast(_4113.PartToPartShearCouplingHalfPowerFlow)

        @property
        def pulley_power_flow(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4122

            return self._parent._cast(_4122.PulleyPowerFlow)

        @property
        def rolling_ring_power_flow(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4127

            return self._parent._cast(_4127.RollingRingPowerFlow)

        @property
        def spring_damper_half_power_flow(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.SpringDamperHalfPowerFlow)

        @property
        def synchroniser_half_power_flow(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4147

            return self._parent._cast(_4147.SynchroniserHalfPowerFlow)

        @property
        def synchroniser_part_power_flow(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4148

            return self._parent._cast(_4148.SynchroniserPartPowerFlow)

        @property
        def synchroniser_sleeve_power_flow(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4150

            return self._parent._cast(_4150.SynchroniserSleevePowerFlow)

        @property
        def torque_converter_pump_power_flow(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4154

            return self._parent._cast(_4154.TorqueConverterPumpPowerFlow)

        @property
        def torque_converter_turbine_power_flow(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4155

            return self._parent._cast(_4155.TorqueConverterTurbinePowerFlow)

        @property
        def coupling_half_power_flow(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow",
        ) -> "CouplingHalfPowerFlow":
            return self._parent

        def __getattr__(
            self: "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingHalfPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2582.CouplingHalf":
        """mastapy.system_model.part_model.couplings.CouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow":
        return self._Cast_CouplingHalfPowerFlow(self)
