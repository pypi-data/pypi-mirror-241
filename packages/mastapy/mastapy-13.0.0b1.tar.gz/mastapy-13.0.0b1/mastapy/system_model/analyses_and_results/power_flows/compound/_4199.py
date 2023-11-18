"""ConnectionCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7536
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "ConnectionCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4065


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionCompoundPowerFlow",)


Self = TypeVar("Self", bound="ConnectionCompoundPowerFlow")


class ConnectionCompoundPowerFlow(_7536.ConnectionCompoundAnalysis):
    """ConnectionCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _CONNECTION_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectionCompoundPowerFlow")

    class _Cast_ConnectionCompoundPowerFlow:
        """Special nested class for casting ConnectionCompoundPowerFlow to subclasses."""

        def __init__(
            self: "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow",
            parent: "ConnectionCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def connection_compound_analysis(
            self: "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow",
        ):
            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_power_flow(
            self: "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4167,
            )

            return self._parent._cast(
                _4167.AbstractShaftToMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4169,
            )

            return self._parent._cast(_4169.AGMAGleasonConicalGearMeshCompoundPowerFlow)

        @property
        def belt_connection_compound_power_flow(
            self: "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4173,
            )

            return self._parent._cast(_4173.BeltConnectionCompoundPowerFlow)

        @property
        def bevel_differential_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4176,
            )

            return self._parent._cast(_4176.BevelDifferentialGearMeshCompoundPowerFlow)

        @property
        def bevel_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4181,
            )

            return self._parent._cast(_4181.BevelGearMeshCompoundPowerFlow)

        @property
        def clutch_connection_compound_power_flow(
            self: "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4186,
            )

            return self._parent._cast(_4186.ClutchConnectionCompoundPowerFlow)

        @property
        def coaxial_connection_compound_power_flow(
            self: "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4188,
            )

            return self._parent._cast(_4188.CoaxialConnectionCompoundPowerFlow)

        @property
        def concept_coupling_connection_compound_power_flow(
            self: "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4191,
            )

            return self._parent._cast(_4191.ConceptCouplingConnectionCompoundPowerFlow)

        @property
        def concept_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4194,
            )

            return self._parent._cast(_4194.ConceptGearMeshCompoundPowerFlow)

        @property
        def conical_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4197,
            )

            return self._parent._cast(_4197.ConicalGearMeshCompoundPowerFlow)

        @property
        def coupling_connection_compound_power_flow(
            self: "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4202,
            )

            return self._parent._cast(_4202.CouplingConnectionCompoundPowerFlow)

        @property
        def cvt_belt_connection_compound_power_flow(
            self: "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4204,
            )

            return self._parent._cast(_4204.CVTBeltConnectionCompoundPowerFlow)

        @property
        def cycloidal_disc_central_bearing_connection_compound_power_flow(
            self: "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4208,
            )

            return self._parent._cast(
                _4208.CycloidalDiscCentralBearingConnectionCompoundPowerFlow
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_power_flow(
            self: "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4210,
            )

            return self._parent._cast(
                _4210.CycloidalDiscPlanetaryBearingConnectionCompoundPowerFlow
            )

        @property
        def cylindrical_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4212,
            )

            return self._parent._cast(_4212.CylindricalGearMeshCompoundPowerFlow)

        @property
        def face_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4218,
            )

            return self._parent._cast(_4218.FaceGearMeshCompoundPowerFlow)

        @property
        def gear_mesh_compound_power_flow(
            self: "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4223,
            )

            return self._parent._cast(_4223.GearMeshCompoundPowerFlow)

        @property
        def hypoid_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4227,
            )

            return self._parent._cast(_4227.HypoidGearMeshCompoundPowerFlow)

        @property
        def inter_mountable_component_connection_compound_power_flow(
            self: "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4229,
            )

            return self._parent._cast(
                _4229.InterMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4231,
            )

            return self._parent._cast(
                _4231.KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4234,
            )

            return self._parent._cast(
                _4234.KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4237,
            )

            return self._parent._cast(
                _4237.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow
            )

        @property
        def part_to_part_shear_coupling_connection_compound_power_flow(
            self: "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4245,
            )

            return self._parent._cast(
                _4245.PartToPartShearCouplingConnectionCompoundPowerFlow
            )

        @property
        def planetary_connection_compound_power_flow(
            self: "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4247,
            )

            return self._parent._cast(_4247.PlanetaryConnectionCompoundPowerFlow)

        @property
        def ring_pins_to_disc_connection_compound_power_flow(
            self: "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4254,
            )

            return self._parent._cast(_4254.RingPinsToDiscConnectionCompoundPowerFlow)

        @property
        def rolling_ring_connection_compound_power_flow(
            self: "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4257,
            )

            return self._parent._cast(_4257.RollingRingConnectionCompoundPowerFlow)

        @property
        def shaft_to_mountable_component_connection_compound_power_flow(
            self: "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4261,
            )

            return self._parent._cast(
                _4261.ShaftToMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def spiral_bevel_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4264,
            )

            return self._parent._cast(_4264.SpiralBevelGearMeshCompoundPowerFlow)

        @property
        def spring_damper_connection_compound_power_flow(
            self: "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4267,
            )

            return self._parent._cast(_4267.SpringDamperConnectionCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4270,
            )

            return self._parent._cast(_4270.StraightBevelDiffGearMeshCompoundPowerFlow)

        @property
        def straight_bevel_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4273,
            )

            return self._parent._cast(_4273.StraightBevelGearMeshCompoundPowerFlow)

        @property
        def torque_converter_connection_compound_power_flow(
            self: "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4282,
            )

            return self._parent._cast(_4282.TorqueConverterConnectionCompoundPowerFlow)

        @property
        def worm_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4288,
            )

            return self._parent._cast(_4288.WormGearMeshCompoundPowerFlow)

        @property
        def zerol_bevel_gear_mesh_compound_power_flow(
            self: "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4291,
            )

            return self._parent._cast(_4291.ZerolBevelGearMeshCompoundPowerFlow)

        @property
        def connection_compound_power_flow(
            self: "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow",
        ) -> "ConnectionCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectionCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self: Self) -> "List[_4065.ConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ConnectionPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4065.ConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ConnectionPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConnectionCompoundPowerFlow._Cast_ConnectionCompoundPowerFlow":
        return self._Cast_ConnectionCompoundPowerFlow(self)
