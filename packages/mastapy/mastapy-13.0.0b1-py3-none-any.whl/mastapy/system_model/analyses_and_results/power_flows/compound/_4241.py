"""MountableComponentCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4189
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "MountableComponentCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4109


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentCompoundPowerFlow",)


Self = TypeVar("Self", bound="MountableComponentCompoundPowerFlow")


class MountableComponentCompoundPowerFlow(_4189.ComponentCompoundPowerFlow):
    """MountableComponentCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MountableComponentCompoundPowerFlow")

    class _Cast_MountableComponentCompoundPowerFlow:
        """Special nested class for casting MountableComponentCompoundPowerFlow to subclasses."""

        def __init__(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
            parent: "MountableComponentCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def component_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            return self._parent._cast(_4189.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4243,
            )

            return self._parent._cast(_4243.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4168,
            )

            return self._parent._cast(_4168.AGMAGleasonConicalGearCompoundPowerFlow)

        @property
        def bearing_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4172,
            )

            return self._parent._cast(_4172.BearingCompoundPowerFlow)

        @property
        def bevel_differential_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4175,
            )

            return self._parent._cast(_4175.BevelDifferentialGearCompoundPowerFlow)

        @property
        def bevel_differential_planet_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4178,
            )

            return self._parent._cast(
                _4178.BevelDifferentialPlanetGearCompoundPowerFlow
            )

        @property
        def bevel_differential_sun_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4179,
            )

            return self._parent._cast(_4179.BevelDifferentialSunGearCompoundPowerFlow)

        @property
        def bevel_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4180,
            )

            return self._parent._cast(_4180.BevelGearCompoundPowerFlow)

        @property
        def clutch_half_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4187,
            )

            return self._parent._cast(_4187.ClutchHalfCompoundPowerFlow)

        @property
        def concept_coupling_half_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4192,
            )

            return self._parent._cast(_4192.ConceptCouplingHalfCompoundPowerFlow)

        @property
        def concept_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4193,
            )

            return self._parent._cast(_4193.ConceptGearCompoundPowerFlow)

        @property
        def conical_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4196,
            )

            return self._parent._cast(_4196.ConicalGearCompoundPowerFlow)

        @property
        def connector_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4200,
            )

            return self._parent._cast(_4200.ConnectorCompoundPowerFlow)

        @property
        def coupling_half_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4203,
            )

            return self._parent._cast(_4203.CouplingHalfCompoundPowerFlow)

        @property
        def cvt_pulley_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4206,
            )

            return self._parent._cast(_4206.CVTPulleyCompoundPowerFlow)

        @property
        def cylindrical_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4211,
            )

            return self._parent._cast(_4211.CylindricalGearCompoundPowerFlow)

        @property
        def cylindrical_planet_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4214,
            )

            return self._parent._cast(_4214.CylindricalPlanetGearCompoundPowerFlow)

        @property
        def face_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4217,
            )

            return self._parent._cast(_4217.FaceGearCompoundPowerFlow)

        @property
        def gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4222,
            )

            return self._parent._cast(_4222.GearCompoundPowerFlow)

        @property
        def hypoid_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4226,
            )

            return self._parent._cast(_4226.HypoidGearCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4230,
            )

            return self._parent._cast(
                _4230.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4233,
            )

            return self._parent._cast(
                _4233.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4236,
            )

            return self._parent._cast(
                _4236.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow
            )

        @property
        def mass_disc_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4239,
            )

            return self._parent._cast(_4239.MassDiscCompoundPowerFlow)

        @property
        def measurement_component_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4240,
            )

            return self._parent._cast(_4240.MeasurementComponentCompoundPowerFlow)

        @property
        def oil_seal_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4242,
            )

            return self._parent._cast(_4242.OilSealCompoundPowerFlow)

        @property
        def part_to_part_shear_coupling_half_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4246,
            )

            return self._parent._cast(
                _4246.PartToPartShearCouplingHalfCompoundPowerFlow
            )

        @property
        def planet_carrier_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4249,
            )

            return self._parent._cast(_4249.PlanetCarrierCompoundPowerFlow)

        @property
        def point_load_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4250,
            )

            return self._parent._cast(_4250.PointLoadCompoundPowerFlow)

        @property
        def power_load_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4251,
            )

            return self._parent._cast(_4251.PowerLoadCompoundPowerFlow)

        @property
        def pulley_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4252,
            )

            return self._parent._cast(_4252.PulleyCompoundPowerFlow)

        @property
        def ring_pins_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4253,
            )

            return self._parent._cast(_4253.RingPinsCompoundPowerFlow)

        @property
        def rolling_ring_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4256,
            )

            return self._parent._cast(_4256.RollingRingCompoundPowerFlow)

        @property
        def shaft_hub_connection_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4260,
            )

            return self._parent._cast(_4260.ShaftHubConnectionCompoundPowerFlow)

        @property
        def spiral_bevel_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4263,
            )

            return self._parent._cast(_4263.SpiralBevelGearCompoundPowerFlow)

        @property
        def spring_damper_half_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4268,
            )

            return self._parent._cast(_4268.SpringDamperHalfCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4269,
            )

            return self._parent._cast(_4269.StraightBevelDiffGearCompoundPowerFlow)

        @property
        def straight_bevel_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4272,
            )

            return self._parent._cast(_4272.StraightBevelGearCompoundPowerFlow)

        @property
        def straight_bevel_planet_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4275,
            )

            return self._parent._cast(_4275.StraightBevelPlanetGearCompoundPowerFlow)

        @property
        def straight_bevel_sun_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4276,
            )

            return self._parent._cast(_4276.StraightBevelSunGearCompoundPowerFlow)

        @property
        def synchroniser_half_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4278,
            )

            return self._parent._cast(_4278.SynchroniserHalfCompoundPowerFlow)

        @property
        def synchroniser_part_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4279,
            )

            return self._parent._cast(_4279.SynchroniserPartCompoundPowerFlow)

        @property
        def synchroniser_sleeve_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4280,
            )

            return self._parent._cast(_4280.SynchroniserSleeveCompoundPowerFlow)

        @property
        def torque_converter_pump_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4283,
            )

            return self._parent._cast(_4283.TorqueConverterPumpCompoundPowerFlow)

        @property
        def torque_converter_turbine_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4284,
            )

            return self._parent._cast(_4284.TorqueConverterTurbineCompoundPowerFlow)

        @property
        def unbalanced_mass_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4285,
            )

            return self._parent._cast(_4285.UnbalancedMassCompoundPowerFlow)

        @property
        def virtual_component_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4286,
            )

            return self._parent._cast(_4286.VirtualComponentCompoundPowerFlow)

        @property
        def worm_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4287,
            )

            return self._parent._cast(_4287.WormGearCompoundPowerFlow)

        @property
        def zerol_bevel_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4290,
            )

            return self._parent._cast(_4290.ZerolBevelGearCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "MountableComponentCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "MountableComponentCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4109.MountableComponentPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.MountableComponentPowerFlow]

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
    ) -> "List[_4109.MountableComponentPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.MountableComponentPowerFlow]

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
    ) -> (
        "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow"
    ):
        return self._Cast_MountableComponentCompoundPowerFlow(self)
