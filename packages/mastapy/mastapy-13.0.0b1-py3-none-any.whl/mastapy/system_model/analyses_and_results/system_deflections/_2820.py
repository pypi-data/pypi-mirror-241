"""SynchroniserPartSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2728
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "SynchroniserPartSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2603
    from mastapy.system_model.analyses_and_results.power_flows import _4148


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartSystemDeflection",)


Self = TypeVar("Self", bound="SynchroniserPartSystemDeflection")


class SynchroniserPartSystemDeflection(_2728.CouplingHalfSystemDeflection):
    """SynchroniserPartSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserPartSystemDeflection")

    class _Cast_SynchroniserPartSystemDeflection:
        """Special nested class for casting SynchroniserPartSystemDeflection to subclasses."""

        def __init__(
            self: "SynchroniserPartSystemDeflection._Cast_SynchroniserPartSystemDeflection",
            parent: "SynchroniserPartSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_half_system_deflection(
            self: "SynchroniserPartSystemDeflection._Cast_SynchroniserPartSystemDeflection",
        ):
            return self._parent._cast(_2728.CouplingHalfSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "SynchroniserPartSystemDeflection._Cast_SynchroniserPartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2780,
            )

            return self._parent._cast(_2780.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "SynchroniserPartSystemDeflection._Cast_SynchroniserPartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2713,
            )

            return self._parent._cast(_2713.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "SynchroniserPartSystemDeflection._Cast_SynchroniserPartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2783,
            )

            return self._parent._cast(_2783.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "SynchroniserPartSystemDeflection._Cast_SynchroniserPartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserPartSystemDeflection._Cast_SynchroniserPartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserPartSystemDeflection._Cast_SynchroniserPartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserPartSystemDeflection._Cast_SynchroniserPartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserPartSystemDeflection._Cast_SynchroniserPartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartSystemDeflection._Cast_SynchroniserPartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def synchroniser_half_system_deflection(
            self: "SynchroniserPartSystemDeflection._Cast_SynchroniserPartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2819,
            )

            return self._parent._cast(_2819.SynchroniserHalfSystemDeflection)

        @property
        def synchroniser_sleeve_system_deflection(
            self: "SynchroniserPartSystemDeflection._Cast_SynchroniserPartSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2821,
            )

            return self._parent._cast(_2821.SynchroniserSleeveSystemDeflection)

        @property
        def synchroniser_part_system_deflection(
            self: "SynchroniserPartSystemDeflection._Cast_SynchroniserPartSystemDeflection",
        ) -> "SynchroniserPartSystemDeflection":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartSystemDeflection._Cast_SynchroniserPartSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SynchroniserPartSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2603.SynchroniserPart":
        """mastapy.system_model.part_model.couplings.SynchroniserPart

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4148.SynchroniserPartPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.SynchroniserPartPowerFlow

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
    ) -> "SynchroniserPartSystemDeflection._Cast_SynchroniserPartSystemDeflection":
        return self._Cast_SynchroniserPartSystemDeflection(self)
