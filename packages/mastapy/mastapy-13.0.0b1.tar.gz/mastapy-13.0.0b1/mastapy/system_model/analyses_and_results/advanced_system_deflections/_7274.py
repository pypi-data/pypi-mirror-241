"""AGMAGleasonConicalGearAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7302
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "AGMAGleasonConicalGearAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2511


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearAdvancedSystemDeflection")


class AGMAGleasonConicalGearAdvancedSystemDeflection(
    _7302.ConicalGearAdvancedSystemDeflection
):
    """AGMAGleasonConicalGearAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearAdvancedSystemDeflection"
    )

    class _Cast_AGMAGleasonConicalGearAdvancedSystemDeflection:
        """Special nested class for casting AGMAGleasonConicalGearAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearAdvancedSystemDeflection",
            parent: "AGMAGleasonConicalGearAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def conical_gear_advanced_system_deflection(
            self: "AGMAGleasonConicalGearAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7302.ConicalGearAdvancedSystemDeflection)

        @property
        def gear_advanced_system_deflection(
            self: "AGMAGleasonConicalGearAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7330,
            )

            return self._parent._cast(_7330.GearAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(
            self: "AGMAGleasonConicalGearAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7350,
            )

            return self._parent._cast(_7350.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "AGMAGleasonConicalGearAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7295,
            )

            return self._parent._cast(_7295.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "AGMAGleasonConicalGearAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7352,
            )

            return self._parent._cast(_7352.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_advanced_system_deflection(
            self: "AGMAGleasonConicalGearAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7281,
            )

            return self._parent._cast(
                _7281.BevelDifferentialGearAdvancedSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_advanced_system_deflection(
            self: "AGMAGleasonConicalGearAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7284,
            )

            return self._parent._cast(
                _7284.BevelDifferentialPlanetGearAdvancedSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_advanced_system_deflection(
            self: "AGMAGleasonConicalGearAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7285,
            )

            return self._parent._cast(
                _7285.BevelDifferentialSunGearAdvancedSystemDeflection
            )

        @property
        def bevel_gear_advanced_system_deflection(
            self: "AGMAGleasonConicalGearAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7286,
            )

            return self._parent._cast(_7286.BevelGearAdvancedSystemDeflection)

        @property
        def hypoid_gear_advanced_system_deflection(
            self: "AGMAGleasonConicalGearAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7334,
            )

            return self._parent._cast(_7334.HypoidGearAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_advanced_system_deflection(
            self: "AGMAGleasonConicalGearAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7372,
            )

            return self._parent._cast(_7372.SpiralBevelGearAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_advanced_system_deflection(
            self: "AGMAGleasonConicalGearAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7378,
            )

            return self._parent._cast(
                _7378.StraightBevelDiffGearAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_advanced_system_deflection(
            self: "AGMAGleasonConicalGearAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7381,
            )

            return self._parent._cast(_7381.StraightBevelGearAdvancedSystemDeflection)

        @property
        def straight_bevel_planet_gear_advanced_system_deflection(
            self: "AGMAGleasonConicalGearAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7384,
            )

            return self._parent._cast(
                _7384.StraightBevelPlanetGearAdvancedSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_advanced_system_deflection(
            self: "AGMAGleasonConicalGearAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7385,
            )

            return self._parent._cast(
                _7385.StraightBevelSunGearAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_advanced_system_deflection(
            self: "AGMAGleasonConicalGearAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7400,
            )

            return self._parent._cast(_7400.ZerolBevelGearAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_advanced_system_deflection(
            self: "AGMAGleasonConicalGearAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearAdvancedSystemDeflection",
        ) -> "AGMAGleasonConicalGearAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearAdvancedSystemDeflection",
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
        instance_to_wrap: "AGMAGleasonConicalGearAdvancedSystemDeflection.TYPE",
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
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearAdvancedSystemDeflection":
        return self._Cast_AGMAGleasonConicalGearAdvancedSystemDeflection(self)
