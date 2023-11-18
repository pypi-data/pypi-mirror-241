"""BevelDifferentialPlanetGearCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4175
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "BevelDifferentialPlanetGearCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4044


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialPlanetGearCompoundPowerFlow",)


Self = TypeVar("Self", bound="BevelDifferentialPlanetGearCompoundPowerFlow")


class BevelDifferentialPlanetGearCompoundPowerFlow(
    _4175.BevelDifferentialGearCompoundPowerFlow
):
    """BevelDifferentialPlanetGearCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialPlanetGearCompoundPowerFlow"
    )

    class _Cast_BevelDifferentialPlanetGearCompoundPowerFlow:
        """Special nested class for casting BevelDifferentialPlanetGearCompoundPowerFlow to subclasses."""

        def __init__(
            self: "BevelDifferentialPlanetGearCompoundPowerFlow._Cast_BevelDifferentialPlanetGearCompoundPowerFlow",
            parent: "BevelDifferentialPlanetGearCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_compound_power_flow(
            self: "BevelDifferentialPlanetGearCompoundPowerFlow._Cast_BevelDifferentialPlanetGearCompoundPowerFlow",
        ):
            return self._parent._cast(_4175.BevelDifferentialGearCompoundPowerFlow)

        @property
        def bevel_gear_compound_power_flow(
            self: "BevelDifferentialPlanetGearCompoundPowerFlow._Cast_BevelDifferentialPlanetGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4180,
            )

            return self._parent._cast(_4180.BevelGearCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_compound_power_flow(
            self: "BevelDifferentialPlanetGearCompoundPowerFlow._Cast_BevelDifferentialPlanetGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4168,
            )

            return self._parent._cast(_4168.AGMAGleasonConicalGearCompoundPowerFlow)

        @property
        def conical_gear_compound_power_flow(
            self: "BevelDifferentialPlanetGearCompoundPowerFlow._Cast_BevelDifferentialPlanetGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4196,
            )

            return self._parent._cast(_4196.ConicalGearCompoundPowerFlow)

        @property
        def gear_compound_power_flow(
            self: "BevelDifferentialPlanetGearCompoundPowerFlow._Cast_BevelDifferentialPlanetGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4222,
            )

            return self._parent._cast(_4222.GearCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "BevelDifferentialPlanetGearCompoundPowerFlow._Cast_BevelDifferentialPlanetGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4241,
            )

            return self._parent._cast(_4241.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "BevelDifferentialPlanetGearCompoundPowerFlow._Cast_BevelDifferentialPlanetGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4189,
            )

            return self._parent._cast(_4189.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "BevelDifferentialPlanetGearCompoundPowerFlow._Cast_BevelDifferentialPlanetGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4243,
            )

            return self._parent._cast(_4243.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialPlanetGearCompoundPowerFlow._Cast_BevelDifferentialPlanetGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialPlanetGearCompoundPowerFlow._Cast_BevelDifferentialPlanetGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialPlanetGearCompoundPowerFlow._Cast_BevelDifferentialPlanetGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_compound_power_flow(
            self: "BevelDifferentialPlanetGearCompoundPowerFlow._Cast_BevelDifferentialPlanetGearCompoundPowerFlow",
        ) -> "BevelDifferentialPlanetGearCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialPlanetGearCompoundPowerFlow._Cast_BevelDifferentialPlanetGearCompoundPowerFlow",
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
        self: Self,
        instance_to_wrap: "BevelDifferentialPlanetGearCompoundPowerFlow.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4044.BevelDifferentialPlanetGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.BevelDifferentialPlanetGearPowerFlow]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4044.BevelDifferentialPlanetGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.BevelDifferentialPlanetGearPowerFlow]

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
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialPlanetGearCompoundPowerFlow._Cast_BevelDifferentialPlanetGearCompoundPowerFlow":
        return self._Cast_BevelDifferentialPlanetGearCompoundPowerFlow(self)
