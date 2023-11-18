"""ConicalGearMeshCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4223
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "ConicalGearMeshCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4062


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshCompoundPowerFlow",)


Self = TypeVar("Self", bound="ConicalGearMeshCompoundPowerFlow")


class ConicalGearMeshCompoundPowerFlow(_4223.GearMeshCompoundPowerFlow):
    """ConicalGearMeshCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearMeshCompoundPowerFlow")

    class _Cast_ConicalGearMeshCompoundPowerFlow:
        """Special nested class for casting ConicalGearMeshCompoundPowerFlow to subclasses."""

        def __init__(
            self: "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow",
            parent: "ConicalGearMeshCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def gear_mesh_compound_power_flow(
            self: "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow",
        ):
            return self._parent._cast(_4223.GearMeshCompoundPowerFlow)

        @property
        def inter_mountable_component_connection_compound_power_flow(
            self: "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4229,
            )

            return self._parent._cast(
                _4229.InterMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def connection_compound_power_flow(
            self: "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4199,
            )

            return self._parent._cast(_4199.ConnectionCompoundPowerFlow)

        @property
        def connection_compound_analysis(
            self: "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_power_flow(
            self: "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4169,
            )

            return self._parent._cast(_4169.AGMAGleasonConicalGearMeshCompoundPowerFlow)

        @property
        def bevel_differential_gear_mesh_compound_power_flow(
            self: "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4176,
            )

            return self._parent._cast(_4176.BevelDifferentialGearMeshCompoundPowerFlow)

        @property
        def bevel_gear_mesh_compound_power_flow(
            self: "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4181,
            )

            return self._parent._cast(_4181.BevelGearMeshCompoundPowerFlow)

        @property
        def hypoid_gear_mesh_compound_power_flow(
            self: "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4227,
            )

            return self._parent._cast(_4227.HypoidGearMeshCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_power_flow(
            self: "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4231,
            )

            return self._parent._cast(
                _4231.KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_power_flow(
            self: "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4234,
            )

            return self._parent._cast(
                _4234.KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_power_flow(
            self: "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4237,
            )

            return self._parent._cast(
                _4237.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow
            )

        @property
        def spiral_bevel_gear_mesh_compound_power_flow(
            self: "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4264,
            )

            return self._parent._cast(_4264.SpiralBevelGearMeshCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_mesh_compound_power_flow(
            self: "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4270,
            )

            return self._parent._cast(_4270.StraightBevelDiffGearMeshCompoundPowerFlow)

        @property
        def straight_bevel_gear_mesh_compound_power_flow(
            self: "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4273,
            )

            return self._parent._cast(_4273.StraightBevelGearMeshCompoundPowerFlow)

        @property
        def zerol_bevel_gear_mesh_compound_power_flow(
            self: "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4291,
            )

            return self._parent._cast(_4291.ZerolBevelGearMeshCompoundPowerFlow)

        @property
        def conical_gear_mesh_compound_power_flow(
            self: "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow",
        ) -> "ConicalGearMeshCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearMeshCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self: Self) -> "List[_4062.ConicalGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ConicalGearMeshPowerFlow]

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
    ) -> "List[_4062.ConicalGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ConicalGearMeshPowerFlow]

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
    ) -> "ConicalGearMeshCompoundPowerFlow._Cast_ConicalGearMeshCompoundPowerFlow":
        return self._Cast_ConicalGearMeshCompoundPowerFlow(self)
