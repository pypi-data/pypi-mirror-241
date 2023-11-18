"""AGMAGleasonConicalGearSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2724
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "AGMAGleasonConicalGearSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2511
    from mastapy.system_model.analyses_and_results.power_flows import _4035


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSystemDeflection",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSystemDeflection")


class AGMAGleasonConicalGearSystemDeflection(_2724.ConicalGearSystemDeflection):
    """AGMAGleasonConicalGearSystemDeflection

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearSystemDeflection"
    )

    class _Cast_AGMAGleasonConicalGearSystemDeflection:
        """Special nested class for casting AGMAGleasonConicalGearSystemDeflection to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
            parent: "AGMAGleasonConicalGearSystemDeflection",
        ):
            self._parent = parent

        @property
        def conical_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            return self._parent._cast(_2724.ConicalGearSystemDeflection)

        @property
        def gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2759,
            )

            return self._parent._cast(_2759.GearSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2780,
            )

            return self._parent._cast(_2780.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2713,
            )

            return self._parent._cast(_2713.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2783,
            )

            return self._parent._cast(_2783.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2701,
            )

            return self._parent._cast(_2701.BevelDifferentialGearSystemDeflection)

        @property
        def bevel_differential_planet_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2702,
            )

            return self._parent._cast(_2702.BevelDifferentialPlanetGearSystemDeflection)

        @property
        def bevel_differential_sun_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2703,
            )

            return self._parent._cast(_2703.BevelDifferentialSunGearSystemDeflection)

        @property
        def bevel_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2706,
            )

            return self._parent._cast(_2706.BevelGearSystemDeflection)

        @property
        def hypoid_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2763,
            )

            return self._parent._cast(_2763.HypoidGearSystemDeflection)

        @property
        def spiral_bevel_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2807,
            )

            return self._parent._cast(_2807.SpiralBevelGearSystemDeflection)

        @property
        def straight_bevel_diff_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2813,
            )

            return self._parent._cast(_2813.StraightBevelDiffGearSystemDeflection)

        @property
        def straight_bevel_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2816,
            )

            return self._parent._cast(_2816.StraightBevelGearSystemDeflection)

        @property
        def straight_bevel_planet_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2817,
            )

            return self._parent._cast(_2817.StraightBevelPlanetGearSystemDeflection)

        @property
        def straight_bevel_sun_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2818,
            )

            return self._parent._cast(_2818.StraightBevelSunGearSystemDeflection)

        @property
        def zerol_bevel_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2839,
            )

            return self._parent._cast(_2839.ZerolBevelGearSystemDeflection)

        @property
        def agma_gleason_conical_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "AGMAGleasonConicalGearSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2511.AGMAGleasonConicalGear":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4035.AGMAGleasonConicalGearPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.AGMAGleasonConicalGearPowerFlow

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
    ) -> "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection":
        return self._Cast_AGMAGleasonConicalGearSystemDeflection(self)
