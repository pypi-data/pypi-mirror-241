"""StraightBevelGearMeshCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4181
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_MESH_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "StraightBevelGearMeshCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2325
    from mastapy.system_model.analyses_and_results.power_flows import _4142


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearMeshCompoundPowerFlow",)


Self = TypeVar("Self", bound="StraightBevelGearMeshCompoundPowerFlow")


class StraightBevelGearMeshCompoundPowerFlow(_4181.BevelGearMeshCompoundPowerFlow):
    """StraightBevelGearMeshCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_MESH_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelGearMeshCompoundPowerFlow"
    )

    class _Cast_StraightBevelGearMeshCompoundPowerFlow:
        """Special nested class for casting StraightBevelGearMeshCompoundPowerFlow to subclasses."""

        def __init__(
            self: "StraightBevelGearMeshCompoundPowerFlow._Cast_StraightBevelGearMeshCompoundPowerFlow",
            parent: "StraightBevelGearMeshCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_power_flow(
            self: "StraightBevelGearMeshCompoundPowerFlow._Cast_StraightBevelGearMeshCompoundPowerFlow",
        ):
            return self._parent._cast(_4181.BevelGearMeshCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_mesh_compound_power_flow(
            self: "StraightBevelGearMeshCompoundPowerFlow._Cast_StraightBevelGearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4169,
            )

            return self._parent._cast(_4169.AGMAGleasonConicalGearMeshCompoundPowerFlow)

        @property
        def conical_gear_mesh_compound_power_flow(
            self: "StraightBevelGearMeshCompoundPowerFlow._Cast_StraightBevelGearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4197,
            )

            return self._parent._cast(_4197.ConicalGearMeshCompoundPowerFlow)

        @property
        def gear_mesh_compound_power_flow(
            self: "StraightBevelGearMeshCompoundPowerFlow._Cast_StraightBevelGearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4223,
            )

            return self._parent._cast(_4223.GearMeshCompoundPowerFlow)

        @property
        def inter_mountable_component_connection_compound_power_flow(
            self: "StraightBevelGearMeshCompoundPowerFlow._Cast_StraightBevelGearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4229,
            )

            return self._parent._cast(
                _4229.InterMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def connection_compound_power_flow(
            self: "StraightBevelGearMeshCompoundPowerFlow._Cast_StraightBevelGearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4199,
            )

            return self._parent._cast(_4199.ConnectionCompoundPowerFlow)

        @property
        def connection_compound_analysis(
            self: "StraightBevelGearMeshCompoundPowerFlow._Cast_StraightBevelGearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelGearMeshCompoundPowerFlow._Cast_StraightBevelGearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearMeshCompoundPowerFlow._Cast_StraightBevelGearMeshCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_mesh_compound_power_flow(
            self: "StraightBevelGearMeshCompoundPowerFlow._Cast_StraightBevelGearMeshCompoundPowerFlow",
        ) -> "StraightBevelGearMeshCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearMeshCompoundPowerFlow._Cast_StraightBevelGearMeshCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "StraightBevelGearMeshCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2325.StraightBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2325.StraightBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4142.StraightBevelGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.StraightBevelGearMeshPowerFlow]

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
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4142.StraightBevelGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.StraightBevelGearMeshPowerFlow]

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
    def cast_to(
        self: Self,
    ) -> "StraightBevelGearMeshCompoundPowerFlow._Cast_StraightBevelGearMeshCompoundPowerFlow":
        return self._Cast_StraightBevelGearMeshCompoundPowerFlow(self)
