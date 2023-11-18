"""SpecialisedAssemblyCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2849
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "SpecialisedAssemblyCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2804


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCompoundSystemDeflection",)


Self = TypeVar("Self", bound="SpecialisedAssemblyCompoundSystemDeflection")


class SpecialisedAssemblyCompoundSystemDeflection(
    _2849.AbstractAssemblyCompoundSystemDeflection
):
    """SpecialisedAssemblyCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyCompoundSystemDeflection"
    )

    class _Cast_SpecialisedAssemblyCompoundSystemDeflection:
        """Special nested class for casting SpecialisedAssemblyCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
            parent: "SpecialisedAssemblyCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def abstract_assembly_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ):
            return self._parent._cast(_2849.AbstractAssemblyCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2929,
            )

            return self._parent._cast(_2929.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2855,
            )

            return self._parent._cast(
                _2855.AGMAGleasonConicalGearSetCompoundSystemDeflection
            )

        @property
        def belt_drive_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2859,
            )

            return self._parent._cast(_2859.BeltDriveCompoundSystemDeflection)

        @property
        def bevel_differential_gear_set_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2862,
            )

            return self._parent._cast(
                _2862.BevelDifferentialGearSetCompoundSystemDeflection
            )

        @property
        def bevel_gear_set_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2867,
            )

            return self._parent._cast(_2867.BevelGearSetCompoundSystemDeflection)

        @property
        def bolted_joint_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2869,
            )

            return self._parent._cast(_2869.BoltedJointCompoundSystemDeflection)

        @property
        def clutch_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2870,
            )

            return self._parent._cast(_2870.ClutchCompoundSystemDeflection)

        @property
        def concept_coupling_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2875,
            )

            return self._parent._cast(_2875.ConceptCouplingCompoundSystemDeflection)

        @property
        def concept_gear_set_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2880,
            )

            return self._parent._cast(_2880.ConceptGearSetCompoundSystemDeflection)

        @property
        def conical_gear_set_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2883,
            )

            return self._parent._cast(_2883.ConicalGearSetCompoundSystemDeflection)

        @property
        def coupling_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2886,
            )

            return self._parent._cast(_2886.CouplingCompoundSystemDeflection)

        @property
        def cvt_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2890,
            )

            return self._parent._cast(_2890.CVTCompoundSystemDeflection)

        @property
        def cycloidal_assembly_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2892,
            )

            return self._parent._cast(_2892.CycloidalAssemblyCompoundSystemDeflection)

        @property
        def cylindrical_gear_set_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2898,
            )

            return self._parent._cast(_2898.CylindricalGearSetCompoundSystemDeflection)

        @property
        def face_gear_set_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2905,
            )

            return self._parent._cast(_2905.FaceGearSetCompoundSystemDeflection)

        @property
        def flexible_pin_assembly_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2907,
            )

            return self._parent._cast(_2907.FlexiblePinAssemblyCompoundSystemDeflection)

        @property
        def gear_set_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2910,
            )

            return self._parent._cast(_2910.GearSetCompoundSystemDeflection)

        @property
        def hypoid_gear_set_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2914,
            )

            return self._parent._cast(_2914.HypoidGearSetCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2918,
            )

            return self._parent._cast(
                _2918.KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2921,
            )

            return self._parent._cast(
                _2921.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2924,
            )

            return self._parent._cast(
                _2924.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2930,
            )

            return self._parent._cast(
                _2930.PartToPartShearCouplingCompoundSystemDeflection
            )

        @property
        def planetary_gear_set_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2934,
            )

            return self._parent._cast(_2934.PlanetaryGearSetCompoundSystemDeflection)

        @property
        def rolling_ring_assembly_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2941,
            )

            return self._parent._cast(_2941.RollingRingAssemblyCompoundSystemDeflection)

        @property
        def spiral_bevel_gear_set_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2952,
            )

            return self._parent._cast(_2952.SpiralBevelGearSetCompoundSystemDeflection)

        @property
        def spring_damper_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2953,
            )

            return self._parent._cast(_2953.SpringDamperCompoundSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2958,
            )

            return self._parent._cast(
                _2958.StraightBevelDiffGearSetCompoundSystemDeflection
            )

        @property
        def straight_bevel_gear_set_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2961,
            )

            return self._parent._cast(
                _2961.StraightBevelGearSetCompoundSystemDeflection
            )

        @property
        def synchroniser_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2964,
            )

            return self._parent._cast(_2964.SynchroniserCompoundSystemDeflection)

        @property
        def torque_converter_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2968,
            )

            return self._parent._cast(_2968.TorqueConverterCompoundSystemDeflection)

        @property
        def worm_gear_set_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2976,
            )

            return self._parent._cast(_2976.WormGearSetCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_set_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2979,
            )

            return self._parent._cast(_2979.ZerolBevelGearSetCompoundSystemDeflection)

        @property
        def specialised_assembly_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ) -> "SpecialisedAssemblyCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "SpecialisedAssemblyCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_2804.SpecialisedAssemblySystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.SpecialisedAssemblySystemDeflection]

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
    ) -> "List[_2804.SpecialisedAssemblySystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.SpecialisedAssemblySystemDeflection]

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
    ) -> "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection":
        return self._Cast_SpecialisedAssemblyCompoundSystemDeflection(self)
