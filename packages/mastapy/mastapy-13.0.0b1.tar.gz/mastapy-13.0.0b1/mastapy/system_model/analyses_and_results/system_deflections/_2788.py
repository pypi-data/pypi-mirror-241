"""PlanetCarrierSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2780
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "PlanetCarrierSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2467
    from mastapy.system_model.analyses_and_results.static_loads import _6933
    from mastapy.system_model.analyses_and_results.power_flows import _4117
    from mastapy.system_model.analyses_and_results.system_deflections.reporting import (
        _2844,
    )


__docformat__ = "restructuredtext en"
__all__ = ("PlanetCarrierSystemDeflection",)


Self = TypeVar("Self", bound="PlanetCarrierSystemDeflection")


class PlanetCarrierSystemDeflection(_2780.MountableComponentSystemDeflection):
    """PlanetCarrierSystemDeflection

    This is a mastapy class.
    """

    TYPE = _PLANET_CARRIER_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetCarrierSystemDeflection")

    class _Cast_PlanetCarrierSystemDeflection:
        """Special nested class for casting PlanetCarrierSystemDeflection to subclasses."""

        def __init__(
            self: "PlanetCarrierSystemDeflection._Cast_PlanetCarrierSystemDeflection",
            parent: "PlanetCarrierSystemDeflection",
        ):
            self._parent = parent

        @property
        def mountable_component_system_deflection(
            self: "PlanetCarrierSystemDeflection._Cast_PlanetCarrierSystemDeflection",
        ):
            return self._parent._cast(_2780.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "PlanetCarrierSystemDeflection._Cast_PlanetCarrierSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2713,
            )

            return self._parent._cast(_2713.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "PlanetCarrierSystemDeflection._Cast_PlanetCarrierSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2783,
            )

            return self._parent._cast(_2783.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "PlanetCarrierSystemDeflection._Cast_PlanetCarrierSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PlanetCarrierSystemDeflection._Cast_PlanetCarrierSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetCarrierSystemDeflection._Cast_PlanetCarrierSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetCarrierSystemDeflection._Cast_PlanetCarrierSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetCarrierSystemDeflection._Cast_PlanetCarrierSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetCarrierSystemDeflection._Cast_PlanetCarrierSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def planet_carrier_system_deflection(
            self: "PlanetCarrierSystemDeflection._Cast_PlanetCarrierSystemDeflection",
        ) -> "PlanetCarrierSystemDeflection":
            return self._parent

        def __getattr__(
            self: "PlanetCarrierSystemDeflection._Cast_PlanetCarrierSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlanetCarrierSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2467.PlanetCarrier":
        """mastapy.system_model.part_model.PlanetCarrier

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6933.PlanetCarrierLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PlanetCarrierLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4117.PlanetCarrierPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.PlanetCarrierPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def windup(self: Self) -> "List[_2844.PlanetCarrierWindup]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.reporting.PlanetCarrierWindup]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Windup

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "PlanetCarrierSystemDeflection._Cast_PlanetCarrierSystemDeflection":
        return self._Cast_PlanetCarrierSystemDeflection(self)
