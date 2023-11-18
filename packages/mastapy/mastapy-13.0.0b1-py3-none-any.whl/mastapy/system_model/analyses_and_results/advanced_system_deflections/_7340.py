"""KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7304
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
        "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2535


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection"
)


class KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection(
    _7304.ConicalGearSetAdvancedSystemDeflection
):
    """KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
            parent: "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def conical_gear_set_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7304.ConicalGearSetAdvancedSystemDeflection)

        @property
        def gear_set_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7332,
            )

            return self._parent._cast(_7332.GearSetAdvancedSystemDeflection)

        @property
        def specialised_assembly_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7371,
            )

            return self._parent._cast(_7371.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7267,
            )

            return self._parent._cast(_7267.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7352,
            )

            return self._parent._cast(_7352.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7343,
            )

            return self._parent._cast(
                _7343.KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7346,
            )

            return self._parent._cast(
                _7346.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
        ) -> "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2535.KlingelnbergCycloPalloidConicalGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection":
        return (
            self._Cast_KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection(
                self
            )
        )
