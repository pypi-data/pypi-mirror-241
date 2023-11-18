"""GearSetCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4262
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "GearSetCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.gears.rating import _360
    from mastapy.system_model.analyses_and_results.power_flows import _4092


__docformat__ = "restructuredtext en"
__all__ = ("GearSetCompoundPowerFlow",)


Self = TypeVar("Self", bound="GearSetCompoundPowerFlow")


class GearSetCompoundPowerFlow(_4262.SpecialisedAssemblyCompoundPowerFlow):
    """GearSetCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetCompoundPowerFlow")

    class _Cast_GearSetCompoundPowerFlow:
        """Special nested class for casting GearSetCompoundPowerFlow to subclasses."""

        def __init__(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
            parent: "GearSetCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            return self._parent._cast(_4262.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def abstract_assembly_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4164,
            )

            return self._parent._cast(_4164.AbstractAssemblyCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4243,
            )

            return self._parent._cast(_4243.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4170,
            )

            return self._parent._cast(_4170.AGMAGleasonConicalGearSetCompoundPowerFlow)

        @property
        def bevel_differential_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4177,
            )

            return self._parent._cast(_4177.BevelDifferentialGearSetCompoundPowerFlow)

        @property
        def bevel_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4182,
            )

            return self._parent._cast(_4182.BevelGearSetCompoundPowerFlow)

        @property
        def concept_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4195,
            )

            return self._parent._cast(_4195.ConceptGearSetCompoundPowerFlow)

        @property
        def conical_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4198,
            )

            return self._parent._cast(_4198.ConicalGearSetCompoundPowerFlow)

        @property
        def cylindrical_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4213,
            )

            return self._parent._cast(_4213.CylindricalGearSetCompoundPowerFlow)

        @property
        def face_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4219,
            )

            return self._parent._cast(_4219.FaceGearSetCompoundPowerFlow)

        @property
        def hypoid_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4228,
            )

            return self._parent._cast(_4228.HypoidGearSetCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4232,
            )

            return self._parent._cast(
                _4232.KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4235,
            )

            return self._parent._cast(
                _4235.KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4238,
            )

            return self._parent._cast(
                _4238.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow
            )

        @property
        def planetary_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4248,
            )

            return self._parent._cast(_4248.PlanetaryGearSetCompoundPowerFlow)

        @property
        def spiral_bevel_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4265,
            )

            return self._parent._cast(_4265.SpiralBevelGearSetCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4271,
            )

            return self._parent._cast(_4271.StraightBevelDiffGearSetCompoundPowerFlow)

        @property
        def straight_bevel_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4274,
            )

            return self._parent._cast(_4274.StraightBevelGearSetCompoundPowerFlow)

        @property
        def worm_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4289,
            )

            return self._parent._cast(_4289.WormGearSetCompoundPowerFlow)

        @property
        def zerol_bevel_gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4292,
            )

            return self._parent._cast(_4292.ZerolBevelGearSetCompoundPowerFlow)

        @property
        def gear_set_compound_power_flow(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow",
        ) -> "GearSetCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_set_duty_cycle_rating(self: Self) -> "_360.GearSetDutyCycleRating":
        """mastapy.gears.rating.GearSetDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSetDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases(self: Self) -> "List[_4092.GearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.GearSetPowerFlow]

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
    def assembly_analysis_cases_ready(self: Self) -> "List[_4092.GearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.GearSetPowerFlow]

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
    def cast_to(
        self: Self,
    ) -> "GearSetCompoundPowerFlow._Cast_GearSetCompoundPowerFlow":
        return self._Cast_GearSetCompoundPowerFlow(self)
