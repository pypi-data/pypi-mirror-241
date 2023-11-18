"""CylindricalPlanetGearAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7318
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "CylindricalPlanetGearAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2525


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="CylindricalPlanetGearAdvancedSystemDeflection")


class CylindricalPlanetGearAdvancedSystemDeflection(
    _7318.CylindricalGearAdvancedSystemDeflection
):
    """CylindricalPlanetGearAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalPlanetGearAdvancedSystemDeflection"
    )

    class _Cast_CylindricalPlanetGearAdvancedSystemDeflection:
        """Special nested class for casting CylindricalPlanetGearAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearAdvancedSystemDeflection._Cast_CylindricalPlanetGearAdvancedSystemDeflection",
            parent: "CylindricalPlanetGearAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_advanced_system_deflection(
            self: "CylindricalPlanetGearAdvancedSystemDeflection._Cast_CylindricalPlanetGearAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7318.CylindricalGearAdvancedSystemDeflection)

        @property
        def gear_advanced_system_deflection(
            self: "CylindricalPlanetGearAdvancedSystemDeflection._Cast_CylindricalPlanetGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7330,
            )

            return self._parent._cast(_7330.GearAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(
            self: "CylindricalPlanetGearAdvancedSystemDeflection._Cast_CylindricalPlanetGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7350,
            )

            return self._parent._cast(_7350.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "CylindricalPlanetGearAdvancedSystemDeflection._Cast_CylindricalPlanetGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7295,
            )

            return self._parent._cast(_7295.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "CylindricalPlanetGearAdvancedSystemDeflection._Cast_CylindricalPlanetGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7352,
            )

            return self._parent._cast(_7352.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalPlanetGearAdvancedSystemDeflection._Cast_CylindricalPlanetGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalPlanetGearAdvancedSystemDeflection._Cast_CylindricalPlanetGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalPlanetGearAdvancedSystemDeflection._Cast_CylindricalPlanetGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalPlanetGearAdvancedSystemDeflection._Cast_CylindricalPlanetGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearAdvancedSystemDeflection._Cast_CylindricalPlanetGearAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_advanced_system_deflection(
            self: "CylindricalPlanetGearAdvancedSystemDeflection._Cast_CylindricalPlanetGearAdvancedSystemDeflection",
        ) -> "CylindricalPlanetGearAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearAdvancedSystemDeflection._Cast_CylindricalPlanetGearAdvancedSystemDeflection",
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
        instance_to_wrap: "CylindricalPlanetGearAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2525.CylindricalPlanetGear":
        """mastapy.system_model.part_model.gears.CylindricalPlanetGear

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
    ) -> "CylindricalPlanetGearAdvancedSystemDeflection._Cast_CylindricalPlanetGearAdvancedSystemDeflection":
        return self._Cast_CylindricalPlanetGearAdvancedSystemDeflection(self)
