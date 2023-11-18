"""PlanetaryGearSetCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4213
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "PlanetaryGearSetCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4116


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetCompoundPowerFlow",)


Self = TypeVar("Self", bound="PlanetaryGearSetCompoundPowerFlow")


class PlanetaryGearSetCompoundPowerFlow(_4213.CylindricalGearSetCompoundPowerFlow):
    """PlanetaryGearSetCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetaryGearSetCompoundPowerFlow")

    class _Cast_PlanetaryGearSetCompoundPowerFlow:
        """Special nested class for casting PlanetaryGearSetCompoundPowerFlow to subclasses."""

        def __init__(
            self: "PlanetaryGearSetCompoundPowerFlow._Cast_PlanetaryGearSetCompoundPowerFlow",
            parent: "PlanetaryGearSetCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_compound_power_flow(
            self: "PlanetaryGearSetCompoundPowerFlow._Cast_PlanetaryGearSetCompoundPowerFlow",
        ):
            return self._parent._cast(_4213.CylindricalGearSetCompoundPowerFlow)

        @property
        def gear_set_compound_power_flow(
            self: "PlanetaryGearSetCompoundPowerFlow._Cast_PlanetaryGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4224,
            )

            return self._parent._cast(_4224.GearSetCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(
            self: "PlanetaryGearSetCompoundPowerFlow._Cast_PlanetaryGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4262,
            )

            return self._parent._cast(_4262.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def abstract_assembly_compound_power_flow(
            self: "PlanetaryGearSetCompoundPowerFlow._Cast_PlanetaryGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4164,
            )

            return self._parent._cast(_4164.AbstractAssemblyCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "PlanetaryGearSetCompoundPowerFlow._Cast_PlanetaryGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4243,
            )

            return self._parent._cast(_4243.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "PlanetaryGearSetCompoundPowerFlow._Cast_PlanetaryGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetaryGearSetCompoundPowerFlow._Cast_PlanetaryGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetCompoundPowerFlow._Cast_PlanetaryGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def planetary_gear_set_compound_power_flow(
            self: "PlanetaryGearSetCompoundPowerFlow._Cast_PlanetaryGearSetCompoundPowerFlow",
        ) -> "PlanetaryGearSetCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetCompoundPowerFlow._Cast_PlanetaryGearSetCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "PlanetaryGearSetCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4116.PlanetaryGearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.PlanetaryGearSetPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(self: Self) -> "List[_4116.PlanetaryGearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.PlanetaryGearSetPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "PlanetaryGearSetCompoundPowerFlow._Cast_PlanetaryGearSetCompoundPowerFlow":
        return self._Cast_PlanetaryGearSetCompoundPowerFlow(self)
