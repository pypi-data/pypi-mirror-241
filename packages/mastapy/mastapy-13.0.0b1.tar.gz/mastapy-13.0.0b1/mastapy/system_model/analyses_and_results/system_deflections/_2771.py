"""KlingelnbergCycloPalloidHypoidGearSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2768
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "KlingelnbergCycloPalloidHypoidGearSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2536
    from mastapy.gears.rating.klingelnberg_hypoid import _407
    from mastapy.system_model.analyses_and_results.static_loads import _6913
    from mastapy.system_model.analyses_and_results.power_flows import _4102


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearSystemDeflection",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearSystemDeflection")


class KlingelnbergCycloPalloidHypoidGearSystemDeflection(
    _2768.KlingelnbergCycloPalloidConicalGearSystemDeflection
):
    """KlingelnbergCycloPalloidHypoidGearSystemDeflection

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidHypoidGearSystemDeflection"
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearSystemDeflection:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearSystemDeflection to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSystemDeflection",
            parent: "KlingelnbergCycloPalloidHypoidGearSystemDeflection",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSystemDeflection",
        ):
            return self._parent._cast(
                _2768.KlingelnbergCycloPalloidConicalGearSystemDeflection
            )

        @property
        def conical_gear_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2724,
            )

            return self._parent._cast(_2724.ConicalGearSystemDeflection)

        @property
        def gear_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2759,
            )

            return self._parent._cast(_2759.GearSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2780,
            )

            return self._parent._cast(_2780.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2713,
            )

            return self._parent._cast(_2713.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2783,
            )

            return self._parent._cast(_2783.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSystemDeflection",
        ) -> "KlingelnbergCycloPalloidHypoidGearSystemDeflection":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSystemDeflection",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2536.KlingelnbergCycloPalloidHypoidGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(
        self: Self,
    ) -> "_407.KlingelnbergCycloPalloidHypoidGearRating":
        """mastapy.gears.rating.klingelnberg_hypoid.KlingelnbergCycloPalloidHypoidGearRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(
        self: Self,
    ) -> "_6913.KlingelnbergCycloPalloidHypoidGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(
        self: Self,
    ) -> "_4102.KlingelnbergCycloPalloidHypoidGearPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidHypoidGearPowerFlow

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
    ) -> "KlingelnbergCycloPalloidHypoidGearSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSystemDeflection":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearSystemDeflection(self)
