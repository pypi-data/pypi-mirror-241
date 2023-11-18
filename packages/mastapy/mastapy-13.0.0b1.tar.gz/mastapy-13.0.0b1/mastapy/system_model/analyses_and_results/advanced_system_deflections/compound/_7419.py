"""BevelGearCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7407,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "BevelGearCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7286,
    )


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="BevelGearCompoundAdvancedSystemDeflection")


class BevelGearCompoundAdvancedSystemDeflection(
    _7407.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection
):
    """BevelGearCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearCompoundAdvancedSystemDeflection"
    )

    class _Cast_BevelGearCompoundAdvancedSystemDeflection:
        """Special nested class for casting BevelGearCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "BevelGearCompoundAdvancedSystemDeflection._Cast_BevelGearCompoundAdvancedSystemDeflection",
            parent: "BevelGearCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_compound_advanced_system_deflection(
            self: "BevelGearCompoundAdvancedSystemDeflection._Cast_BevelGearCompoundAdvancedSystemDeflection",
        ):
            return self._parent._cast(
                _7407.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_compound_advanced_system_deflection(
            self: "BevelGearCompoundAdvancedSystemDeflection._Cast_BevelGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7435,
            )

            return self._parent._cast(_7435.ConicalGearCompoundAdvancedSystemDeflection)

        @property
        def gear_compound_advanced_system_deflection(
            self: "BevelGearCompoundAdvancedSystemDeflection._Cast_BevelGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7461,
            )

            return self._parent._cast(_7461.GearCompoundAdvancedSystemDeflection)

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "BevelGearCompoundAdvancedSystemDeflection._Cast_BevelGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7480,
            )

            return self._parent._cast(
                _7480.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "BevelGearCompoundAdvancedSystemDeflection._Cast_BevelGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7428,
            )

            return self._parent._cast(_7428.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "BevelGearCompoundAdvancedSystemDeflection._Cast_BevelGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7482,
            )

            return self._parent._cast(_7482.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "BevelGearCompoundAdvancedSystemDeflection._Cast_BevelGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearCompoundAdvancedSystemDeflection._Cast_BevelGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearCompoundAdvancedSystemDeflection._Cast_BevelGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_compound_advanced_system_deflection(
            self: "BevelGearCompoundAdvancedSystemDeflection._Cast_BevelGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7414,
            )

            return self._parent._cast(
                _7414.BevelDifferentialGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_compound_advanced_system_deflection(
            self: "BevelGearCompoundAdvancedSystemDeflection._Cast_BevelGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7417,
            )

            return self._parent._cast(
                _7417.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_compound_advanced_system_deflection(
            self: "BevelGearCompoundAdvancedSystemDeflection._Cast_BevelGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7418,
            )

            return self._parent._cast(
                _7418.BevelDifferentialSunGearCompoundAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_compound_advanced_system_deflection(
            self: "BevelGearCompoundAdvancedSystemDeflection._Cast_BevelGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7502,
            )

            return self._parent._cast(
                _7502.SpiralBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_compound_advanced_system_deflection(
            self: "BevelGearCompoundAdvancedSystemDeflection._Cast_BevelGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7508,
            )

            return self._parent._cast(
                _7508.StraightBevelDiffGearCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_compound_advanced_system_deflection(
            self: "BevelGearCompoundAdvancedSystemDeflection._Cast_BevelGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7511,
            )

            return self._parent._cast(
                _7511.StraightBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_planet_gear_compound_advanced_system_deflection(
            self: "BevelGearCompoundAdvancedSystemDeflection._Cast_BevelGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7514,
            )

            return self._parent._cast(
                _7514.StraightBevelPlanetGearCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_compound_advanced_system_deflection(
            self: "BevelGearCompoundAdvancedSystemDeflection._Cast_BevelGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7515,
            )

            return self._parent._cast(
                _7515.StraightBevelSunGearCompoundAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_compound_advanced_system_deflection(
            self: "BevelGearCompoundAdvancedSystemDeflection._Cast_BevelGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7529,
            )

            return self._parent._cast(
                _7529.ZerolBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_gear_compound_advanced_system_deflection(
            self: "BevelGearCompoundAdvancedSystemDeflection._Cast_BevelGearCompoundAdvancedSystemDeflection",
        ) -> "BevelGearCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BevelGearCompoundAdvancedSystemDeflection._Cast_BevelGearCompoundAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "BevelGearCompoundAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7286.BevelGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.BevelGearAdvancedSystemDeflection]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_7286.BevelGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.BevelGearAdvancedSystemDeflection]

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
    def cast_to(
        self: Self,
    ) -> "BevelGearCompoundAdvancedSystemDeflection._Cast_BevelGearCompoundAdvancedSystemDeflection":
        return self._Cast_BevelGearCompoundAdvancedSystemDeflection(self)
