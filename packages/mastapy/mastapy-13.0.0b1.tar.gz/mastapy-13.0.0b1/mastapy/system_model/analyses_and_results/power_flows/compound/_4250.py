"""PointLoadCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4286
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "PointLoadCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2469
    from mastapy.system_model.analyses_and_results.power_flows import _4118


__docformat__ = "restructuredtext en"
__all__ = ("PointLoadCompoundPowerFlow",)


Self = TypeVar("Self", bound="PointLoadCompoundPowerFlow")


class PointLoadCompoundPowerFlow(_4286.VirtualComponentCompoundPowerFlow):
    """PointLoadCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _POINT_LOAD_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PointLoadCompoundPowerFlow")

    class _Cast_PointLoadCompoundPowerFlow:
        """Special nested class for casting PointLoadCompoundPowerFlow to subclasses."""

        def __init__(
            self: "PointLoadCompoundPowerFlow._Cast_PointLoadCompoundPowerFlow",
            parent: "PointLoadCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_power_flow(
            self: "PointLoadCompoundPowerFlow._Cast_PointLoadCompoundPowerFlow",
        ):
            return self._parent._cast(_4286.VirtualComponentCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "PointLoadCompoundPowerFlow._Cast_PointLoadCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4241,
            )

            return self._parent._cast(_4241.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "PointLoadCompoundPowerFlow._Cast_PointLoadCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4189,
            )

            return self._parent._cast(_4189.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "PointLoadCompoundPowerFlow._Cast_PointLoadCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4243,
            )

            return self._parent._cast(_4243.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "PointLoadCompoundPowerFlow._Cast_PointLoadCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PointLoadCompoundPowerFlow._Cast_PointLoadCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PointLoadCompoundPowerFlow._Cast_PointLoadCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def point_load_compound_power_flow(
            self: "PointLoadCompoundPowerFlow._Cast_PointLoadCompoundPowerFlow",
        ) -> "PointLoadCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "PointLoadCompoundPowerFlow._Cast_PointLoadCompoundPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PointLoadCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2469.PointLoad":
        """mastapy.system_model.part_model.PointLoad

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(self: Self) -> "List[_4118.PointLoadPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.PointLoadPowerFlow]

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
    def component_analysis_cases(self: Self) -> "List[_4118.PointLoadPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.PointLoadPowerFlow]

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
    ) -> "PointLoadCompoundPowerFlow._Cast_PointLoadCompoundPowerFlow":
        return self._Cast_PointLoadCompoundPowerFlow(self)
