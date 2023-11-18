"""StraightBevelSunGearSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2813
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "StraightBevelSunGearSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2548
    from mastapy.system_model.analyses_and_results.power_flows import _4146


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelSunGearSystemDeflection",)


Self = TypeVar("Self", bound="StraightBevelSunGearSystemDeflection")


class StraightBevelSunGearSystemDeflection(_2813.StraightBevelDiffGearSystemDeflection):
    """StraightBevelSunGearSystemDeflection

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelSunGearSystemDeflection")

    class _Cast_StraightBevelSunGearSystemDeflection:
        """Special nested class for casting StraightBevelSunGearSystemDeflection to subclasses."""

        def __init__(
            self: "StraightBevelSunGearSystemDeflection._Cast_StraightBevelSunGearSystemDeflection",
            parent: "StraightBevelSunGearSystemDeflection",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_system_deflection(
            self: "StraightBevelSunGearSystemDeflection._Cast_StraightBevelSunGearSystemDeflection",
        ):
            return self._parent._cast(_2813.StraightBevelDiffGearSystemDeflection)

        @property
        def bevel_gear_system_deflection(
            self: "StraightBevelSunGearSystemDeflection._Cast_StraightBevelSunGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2706,
            )

            return self._parent._cast(_2706.BevelGearSystemDeflection)

        @property
        def agma_gleason_conical_gear_system_deflection(
            self: "StraightBevelSunGearSystemDeflection._Cast_StraightBevelSunGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2689,
            )

            return self._parent._cast(_2689.AGMAGleasonConicalGearSystemDeflection)

        @property
        def conical_gear_system_deflection(
            self: "StraightBevelSunGearSystemDeflection._Cast_StraightBevelSunGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2724,
            )

            return self._parent._cast(_2724.ConicalGearSystemDeflection)

        @property
        def gear_system_deflection(
            self: "StraightBevelSunGearSystemDeflection._Cast_StraightBevelSunGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2759,
            )

            return self._parent._cast(_2759.GearSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "StraightBevelSunGearSystemDeflection._Cast_StraightBevelSunGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2780,
            )

            return self._parent._cast(_2780.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "StraightBevelSunGearSystemDeflection._Cast_StraightBevelSunGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2713,
            )

            return self._parent._cast(_2713.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "StraightBevelSunGearSystemDeflection._Cast_StraightBevelSunGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2783,
            )

            return self._parent._cast(_2783.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "StraightBevelSunGearSystemDeflection._Cast_StraightBevelSunGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelSunGearSystemDeflection._Cast_StraightBevelSunGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelSunGearSystemDeflection._Cast_StraightBevelSunGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelSunGearSystemDeflection._Cast_StraightBevelSunGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelSunGearSystemDeflection._Cast_StraightBevelSunGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelSunGearSystemDeflection._Cast_StraightBevelSunGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def straight_bevel_sun_gear_system_deflection(
            self: "StraightBevelSunGearSystemDeflection._Cast_StraightBevelSunGearSystemDeflection",
        ) -> "StraightBevelSunGearSystemDeflection":
            return self._parent

        def __getattr__(
            self: "StraightBevelSunGearSystemDeflection._Cast_StraightBevelSunGearSystemDeflection",
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
        self: Self, instance_to_wrap: "StraightBevelSunGearSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2548.StraightBevelSunGear":
        """mastapy.system_model.part_model.gears.StraightBevelSunGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4146.StraightBevelSunGearPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.StraightBevelSunGearPowerFlow

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
    ) -> "StraightBevelSunGearSystemDeflection._Cast_StraightBevelSunGearSystemDeflection":
        return self._Cast_StraightBevelSunGearSystemDeflection(self)
