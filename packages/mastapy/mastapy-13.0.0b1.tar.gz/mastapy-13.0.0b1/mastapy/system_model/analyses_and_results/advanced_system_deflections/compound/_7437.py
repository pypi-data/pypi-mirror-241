"""ConicalGearSetCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7463,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "ConicalGearSetCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.conical import _539
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7304,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="ConicalGearSetCompoundAdvancedSystemDeflection")


class ConicalGearSetCompoundAdvancedSystemDeflection(
    _7463.GearSetCompoundAdvancedSystemDeflection
):
    """ConicalGearSetCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearSetCompoundAdvancedSystemDeflection"
    )

    class _Cast_ConicalGearSetCompoundAdvancedSystemDeflection:
        """Special nested class for casting ConicalGearSetCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
            parent: "ConicalGearSetCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_set_compound_advanced_system_deflection(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7463.GearSetCompoundAdvancedSystemDeflection)

        @property
        def specialised_assembly_compound_advanced_system_deflection(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7501,
            )

            return self._parent._cast(
                _7501.SpecialisedAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_assembly_compound_advanced_system_deflection(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7403,
            )

            return self._parent._cast(
                _7403.AbstractAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def part_compound_advanced_system_deflection(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7482,
            )

            return self._parent._cast(_7482.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_advanced_system_deflection(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7409,
            )

            return self._parent._cast(
                _7409.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_gear_set_compound_advanced_system_deflection(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7416,
            )

            return self._parent._cast(
                _7416.BevelDifferentialGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_gear_set_compound_advanced_system_deflection(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7421,
            )

            return self._parent._cast(
                _7421.BevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def hypoid_gear_set_compound_advanced_system_deflection(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7467,
            )

            return self._parent._cast(
                _7467.HypoidGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_advanced_system_deflection(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7471,
            )

            return self._parent._cast(
                _7471.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_advanced_system_deflection(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7474,
            )

            return self._parent._cast(
                _7474.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_advanced_system_deflection(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7477,
            )

            return self._parent._cast(
                _7477.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_set_compound_advanced_system_deflection(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7504,
            )

            return self._parent._cast(
                _7504.SpiralBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_set_compound_advanced_system_deflection(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7510,
            )

            return self._parent._cast(
                _7510.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_set_compound_advanced_system_deflection(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7513,
            )

            return self._parent._cast(
                _7513.StraightBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_set_compound_advanced_system_deflection(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7531,
            )

            return self._parent._cast(
                _7531.ZerolBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_set_compound_advanced_system_deflection(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "ConicalGearSetCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "ConicalGearSetCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_duty_cycle_rating(self: Self) -> "_539.ConicalGearSetDutyCycleRating":
        """mastapy.gears.rating.conical.ConicalGearSetDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def conical_gear_duty_cycle_rating(
        self: Self,
    ) -> "_539.ConicalGearSetDutyCycleRating":
        """mastapy.gears.rating.conical.ConicalGearSetDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_7304.ConicalGearSetAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ConicalGearSetAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_7304.ConicalGearSetAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ConicalGearSetAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearSetCompoundAdvancedSystemDeflection._Cast_ConicalGearSetCompoundAdvancedSystemDeflection":
        return self._Cast_ConicalGearSetCompoundAdvancedSystemDeflection(self)
