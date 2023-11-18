"""GearSetCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2949
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "GearSetCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2758


__docformat__ = "restructuredtext en"
__all__ = ("GearSetCompoundSystemDeflection",)


Self = TypeVar("Self", bound="GearSetCompoundSystemDeflection")


class GearSetCompoundSystemDeflection(
    _2949.SpecialisedAssemblyCompoundSystemDeflection
):
    """GearSetCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetCompoundSystemDeflection")

    class _Cast_GearSetCompoundSystemDeflection:
        """Special nested class for casting GearSetCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "GearSetCompoundSystemDeflection._Cast_GearSetCompoundSystemDeflection",
            parent: "GearSetCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_system_deflection(
            self: "GearSetCompoundSystemDeflection._Cast_GearSetCompoundSystemDeflection",
        ):
            return self._parent._cast(_2949.SpecialisedAssemblyCompoundSystemDeflection)

        @property
        def abstract_assembly_compound_system_deflection(
            self: "GearSetCompoundSystemDeflection._Cast_GearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2849,
            )

            return self._parent._cast(_2849.AbstractAssemblyCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "GearSetCompoundSystemDeflection._Cast_GearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2929,
            )

            return self._parent._cast(_2929.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "GearSetCompoundSystemDeflection._Cast_GearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearSetCompoundSystemDeflection._Cast_GearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSetCompoundSystemDeflection._Cast_GearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_system_deflection(
            self: "GearSetCompoundSystemDeflection._Cast_GearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2855,
            )

            return self._parent._cast(
                _2855.AGMAGleasonConicalGearSetCompoundSystemDeflection
            )

        @property
        def bevel_differential_gear_set_compound_system_deflection(
            self: "GearSetCompoundSystemDeflection._Cast_GearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2862,
            )

            return self._parent._cast(
                _2862.BevelDifferentialGearSetCompoundSystemDeflection
            )

        @property
        def bevel_gear_set_compound_system_deflection(
            self: "GearSetCompoundSystemDeflection._Cast_GearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2867,
            )

            return self._parent._cast(_2867.BevelGearSetCompoundSystemDeflection)

        @property
        def concept_gear_set_compound_system_deflection(
            self: "GearSetCompoundSystemDeflection._Cast_GearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2880,
            )

            return self._parent._cast(_2880.ConceptGearSetCompoundSystemDeflection)

        @property
        def conical_gear_set_compound_system_deflection(
            self: "GearSetCompoundSystemDeflection._Cast_GearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2883,
            )

            return self._parent._cast(_2883.ConicalGearSetCompoundSystemDeflection)

        @property
        def cylindrical_gear_set_compound_system_deflection(
            self: "GearSetCompoundSystemDeflection._Cast_GearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2898,
            )

            return self._parent._cast(_2898.CylindricalGearSetCompoundSystemDeflection)

        @property
        def face_gear_set_compound_system_deflection(
            self: "GearSetCompoundSystemDeflection._Cast_GearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2905,
            )

            return self._parent._cast(_2905.FaceGearSetCompoundSystemDeflection)

        @property
        def hypoid_gear_set_compound_system_deflection(
            self: "GearSetCompoundSystemDeflection._Cast_GearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2914,
            )

            return self._parent._cast(_2914.HypoidGearSetCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_system_deflection(
            self: "GearSetCompoundSystemDeflection._Cast_GearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2918,
            )

            return self._parent._cast(
                _2918.KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_system_deflection(
            self: "GearSetCompoundSystemDeflection._Cast_GearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2921,
            )

            return self._parent._cast(
                _2921.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_system_deflection(
            self: "GearSetCompoundSystemDeflection._Cast_GearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2924,
            )

            return self._parent._cast(
                _2924.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection
            )

        @property
        def planetary_gear_set_compound_system_deflection(
            self: "GearSetCompoundSystemDeflection._Cast_GearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2934,
            )

            return self._parent._cast(_2934.PlanetaryGearSetCompoundSystemDeflection)

        @property
        def spiral_bevel_gear_set_compound_system_deflection(
            self: "GearSetCompoundSystemDeflection._Cast_GearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2952,
            )

            return self._parent._cast(_2952.SpiralBevelGearSetCompoundSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_compound_system_deflection(
            self: "GearSetCompoundSystemDeflection._Cast_GearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2958,
            )

            return self._parent._cast(
                _2958.StraightBevelDiffGearSetCompoundSystemDeflection
            )

        @property
        def straight_bevel_gear_set_compound_system_deflection(
            self: "GearSetCompoundSystemDeflection._Cast_GearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2961,
            )

            return self._parent._cast(
                _2961.StraightBevelGearSetCompoundSystemDeflection
            )

        @property
        def worm_gear_set_compound_system_deflection(
            self: "GearSetCompoundSystemDeflection._Cast_GearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2976,
            )

            return self._parent._cast(_2976.WormGearSetCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_set_compound_system_deflection(
            self: "GearSetCompoundSystemDeflection._Cast_GearSetCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2979,
            )

            return self._parent._cast(_2979.ZerolBevelGearSetCompoundSystemDeflection)

        @property
        def gear_set_compound_system_deflection(
            self: "GearSetCompoundSystemDeflection._Cast_GearSetCompoundSystemDeflection",
        ) -> "GearSetCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "GearSetCompoundSystemDeflection._Cast_GearSetCompoundSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetCompoundSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self: Self) -> "List[_2758.GearSetSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.GearSetSystemDeflection]

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
    ) -> "List[_2758.GearSetSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.GearSetSystemDeflection]

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
    ) -> "GearSetCompoundSystemDeflection._Cast_GearSetCompoundSystemDeflection":
        return self._Cast_GearSetCompoundSystemDeflection(self)
