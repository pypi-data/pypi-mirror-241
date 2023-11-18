"""SynchroniserSleeveSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2820
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "SynchroniserSleeveSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2604
    from mastapy.system_model.analyses_and_results.static_loads import _6968
    from mastapy.system_model.analyses_and_results.power_flows import _4150


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserSleeveSystemDeflection",)


Self = TypeVar("Self", bound="SynchroniserSleeveSystemDeflection")


class SynchroniserSleeveSystemDeflection(_2820.SynchroniserPartSystemDeflection):
    """SynchroniserSleeveSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserSleeveSystemDeflection")

    class _Cast_SynchroniserSleeveSystemDeflection:
        """Special nested class for casting SynchroniserSleeveSystemDeflection to subclasses."""

        def __init__(
            self: "SynchroniserSleeveSystemDeflection._Cast_SynchroniserSleeveSystemDeflection",
            parent: "SynchroniserSleeveSystemDeflection",
        ):
            self._parent = parent

        @property
        def synchroniser_part_system_deflection(
            self: "SynchroniserSleeveSystemDeflection._Cast_SynchroniserSleeveSystemDeflection",
        ):
            return self._parent._cast(_2820.SynchroniserPartSystemDeflection)

        @property
        def coupling_half_system_deflection(
            self: "SynchroniserSleeveSystemDeflection._Cast_SynchroniserSleeveSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2728,
            )

            return self._parent._cast(_2728.CouplingHalfSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "SynchroniserSleeveSystemDeflection._Cast_SynchroniserSleeveSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2780,
            )

            return self._parent._cast(_2780.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "SynchroniserSleeveSystemDeflection._Cast_SynchroniserSleeveSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2713,
            )

            return self._parent._cast(_2713.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "SynchroniserSleeveSystemDeflection._Cast_SynchroniserSleeveSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2783,
            )

            return self._parent._cast(_2783.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "SynchroniserSleeveSystemDeflection._Cast_SynchroniserSleeveSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserSleeveSystemDeflection._Cast_SynchroniserSleeveSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserSleeveSystemDeflection._Cast_SynchroniserSleeveSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserSleeveSystemDeflection._Cast_SynchroniserSleeveSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserSleeveSystemDeflection._Cast_SynchroniserSleeveSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserSleeveSystemDeflection._Cast_SynchroniserSleeveSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def synchroniser_sleeve_system_deflection(
            self: "SynchroniserSleeveSystemDeflection._Cast_SynchroniserSleeveSystemDeflection",
        ) -> "SynchroniserSleeveSystemDeflection":
            return self._parent

        def __getattr__(
            self: "SynchroniserSleeveSystemDeflection._Cast_SynchroniserSleeveSystemDeflection",
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
        self: Self, instance_to_wrap: "SynchroniserSleeveSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2604.SynchroniserSleeve":
        """mastapy.system_model.part_model.couplings.SynchroniserSleeve

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6968.SynchroniserSleeveLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4150.SynchroniserSleevePowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.SynchroniserSleevePowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SynchroniserSleeveSystemDeflection._Cast_SynchroniserSleeveSystemDeflection":
        return self._Cast_SynchroniserSleeveSystemDeflection(self)
