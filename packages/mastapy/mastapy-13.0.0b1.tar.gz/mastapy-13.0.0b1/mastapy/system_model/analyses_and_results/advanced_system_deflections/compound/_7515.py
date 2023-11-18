"""StraightBevelSunGearCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7508,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "StraightBevelSunGearCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7385,
    )


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelSunGearCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="StraightBevelSunGearCompoundAdvancedSystemDeflection")


class StraightBevelSunGearCompoundAdvancedSystemDeflection(
    _7508.StraightBevelDiffGearCompoundAdvancedSystemDeflection
):
    """StraightBevelSunGearCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelSunGearCompoundAdvancedSystemDeflection"
    )

    class _Cast_StraightBevelSunGearCompoundAdvancedSystemDeflection:
        """Special nested class for casting StraightBevelSunGearCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "StraightBevelSunGearCompoundAdvancedSystemDeflection._Cast_StraightBevelSunGearCompoundAdvancedSystemDeflection",
            parent: "StraightBevelSunGearCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_compound_advanced_system_deflection(
            self: "StraightBevelSunGearCompoundAdvancedSystemDeflection._Cast_StraightBevelSunGearCompoundAdvancedSystemDeflection",
        ):
            return self._parent._cast(
                _7508.StraightBevelDiffGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_gear_compound_advanced_system_deflection(
            self: "StraightBevelSunGearCompoundAdvancedSystemDeflection._Cast_StraightBevelSunGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7419,
            )

            return self._parent._cast(_7419.BevelGearCompoundAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_compound_advanced_system_deflection(
            self: "StraightBevelSunGearCompoundAdvancedSystemDeflection._Cast_StraightBevelSunGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7407,
            )

            return self._parent._cast(
                _7407.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_compound_advanced_system_deflection(
            self: "StraightBevelSunGearCompoundAdvancedSystemDeflection._Cast_StraightBevelSunGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7435,
            )

            return self._parent._cast(_7435.ConicalGearCompoundAdvancedSystemDeflection)

        @property
        def gear_compound_advanced_system_deflection(
            self: "StraightBevelSunGearCompoundAdvancedSystemDeflection._Cast_StraightBevelSunGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7461,
            )

            return self._parent._cast(_7461.GearCompoundAdvancedSystemDeflection)

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "StraightBevelSunGearCompoundAdvancedSystemDeflection._Cast_StraightBevelSunGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7480,
            )

            return self._parent._cast(
                _7480.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "StraightBevelSunGearCompoundAdvancedSystemDeflection._Cast_StraightBevelSunGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7428,
            )

            return self._parent._cast(_7428.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "StraightBevelSunGearCompoundAdvancedSystemDeflection._Cast_StraightBevelSunGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7482,
            )

            return self._parent._cast(_7482.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "StraightBevelSunGearCompoundAdvancedSystemDeflection._Cast_StraightBevelSunGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelSunGearCompoundAdvancedSystemDeflection._Cast_StraightBevelSunGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelSunGearCompoundAdvancedSystemDeflection._Cast_StraightBevelSunGearCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def straight_bevel_sun_gear_compound_advanced_system_deflection(
            self: "StraightBevelSunGearCompoundAdvancedSystemDeflection._Cast_StraightBevelSunGearCompoundAdvancedSystemDeflection",
        ) -> "StraightBevelSunGearCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "StraightBevelSunGearCompoundAdvancedSystemDeflection._Cast_StraightBevelSunGearCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "StraightBevelSunGearCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_7385.StraightBevelSunGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.StraightBevelSunGearAdvancedSystemDeflection]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7385.StraightBevelSunGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.StraightBevelSunGearAdvancedSystemDeflection]

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
    ) -> "StraightBevelSunGearCompoundAdvancedSystemDeflection._Cast_StraightBevelSunGearCompoundAdvancedSystemDeflection":
        return self._Cast_StraightBevelSunGearCompoundAdvancedSystemDeflection(self)
