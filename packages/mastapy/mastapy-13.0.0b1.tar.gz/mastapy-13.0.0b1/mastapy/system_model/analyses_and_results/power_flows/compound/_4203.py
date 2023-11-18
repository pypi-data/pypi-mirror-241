"""CouplingHalfCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4241
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "CouplingHalfCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4068


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundPowerFlow",)


Self = TypeVar("Self", bound="CouplingHalfCompoundPowerFlow")


class CouplingHalfCompoundPowerFlow(_4241.MountableComponentCompoundPowerFlow):
    """CouplingHalfCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfCompoundPowerFlow")

    class _Cast_CouplingHalfCompoundPowerFlow:
        """Special nested class for casting CouplingHalfCompoundPowerFlow to subclasses."""

        def __init__(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
            parent: "CouplingHalfCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ):
            return self._parent._cast(_4241.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4189,
            )

            return self._parent._cast(_4189.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4243,
            )

            return self._parent._cast(_4243.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def clutch_half_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4187,
            )

            return self._parent._cast(_4187.ClutchHalfCompoundPowerFlow)

        @property
        def concept_coupling_half_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4192,
            )

            return self._parent._cast(_4192.ConceptCouplingHalfCompoundPowerFlow)

        @property
        def cvt_pulley_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4206,
            )

            return self._parent._cast(_4206.CVTPulleyCompoundPowerFlow)

        @property
        def part_to_part_shear_coupling_half_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4246,
            )

            return self._parent._cast(
                _4246.PartToPartShearCouplingHalfCompoundPowerFlow
            )

        @property
        def pulley_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4252,
            )

            return self._parent._cast(_4252.PulleyCompoundPowerFlow)

        @property
        def rolling_ring_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4256,
            )

            return self._parent._cast(_4256.RollingRingCompoundPowerFlow)

        @property
        def spring_damper_half_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4268,
            )

            return self._parent._cast(_4268.SpringDamperHalfCompoundPowerFlow)

        @property
        def synchroniser_half_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4278,
            )

            return self._parent._cast(_4278.SynchroniserHalfCompoundPowerFlow)

        @property
        def synchroniser_part_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4279,
            )

            return self._parent._cast(_4279.SynchroniserPartCompoundPowerFlow)

        @property
        def synchroniser_sleeve_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4280,
            )

            return self._parent._cast(_4280.SynchroniserSleeveCompoundPowerFlow)

        @property
        def torque_converter_pump_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4283,
            )

            return self._parent._cast(_4283.TorqueConverterPumpCompoundPowerFlow)

        @property
        def torque_converter_turbine_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4284,
            )

            return self._parent._cast(_4284.TorqueConverterTurbineCompoundPowerFlow)

        @property
        def coupling_half_compound_power_flow(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
        ) -> "CouplingHalfCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingHalfCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_4068.CouplingHalfPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.CouplingHalfPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4068.CouplingHalfPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.CouplingHalfPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingHalfCompoundPowerFlow._Cast_CouplingHalfCompoundPowerFlow":
        return self._Cast_CouplingHalfCompoundPowerFlow(self)
