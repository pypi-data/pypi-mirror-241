"""AbstractAssemblyCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5955
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "AbstractAssemblyCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5675


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="AbstractAssemblyCompoundHarmonicAnalysis")


class AbstractAssemblyCompoundHarmonicAnalysis(_5955.PartCompoundHarmonicAnalysis):
    """AbstractAssemblyCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractAssemblyCompoundHarmonicAnalysis"
    )

    class _Cast_AbstractAssemblyCompoundHarmonicAnalysis:
        """Special nested class for casting AbstractAssemblyCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
            parent: "AbstractAssemblyCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def part_compound_harmonic_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
        ):
            return self._parent._cast(_5955.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_harmonic_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5882,
            )

            return self._parent._cast(
                _5882.AGMAGleasonConicalGearSetCompoundHarmonicAnalysis
            )

        @property
        def assembly_compound_harmonic_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5883,
            )

            return self._parent._cast(_5883.AssemblyCompoundHarmonicAnalysis)

        @property
        def belt_drive_compound_harmonic_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5886,
            )

            return self._parent._cast(_5886.BeltDriveCompoundHarmonicAnalysis)

        @property
        def bevel_differential_gear_set_compound_harmonic_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5889,
            )

            return self._parent._cast(
                _5889.BevelDifferentialGearSetCompoundHarmonicAnalysis
            )

        @property
        def bevel_gear_set_compound_harmonic_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5894,
            )

            return self._parent._cast(_5894.BevelGearSetCompoundHarmonicAnalysis)

        @property
        def bolted_joint_compound_harmonic_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5896,
            )

            return self._parent._cast(_5896.BoltedJointCompoundHarmonicAnalysis)

        @property
        def clutch_compound_harmonic_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5897,
            )

            return self._parent._cast(_5897.ClutchCompoundHarmonicAnalysis)

        @property
        def concept_coupling_compound_harmonic_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5902,
            )

            return self._parent._cast(_5902.ConceptCouplingCompoundHarmonicAnalysis)

        @property
        def concept_gear_set_compound_harmonic_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5907,
            )

            return self._parent._cast(_5907.ConceptGearSetCompoundHarmonicAnalysis)

        @property
        def conical_gear_set_compound_harmonic_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5910,
            )

            return self._parent._cast(_5910.ConicalGearSetCompoundHarmonicAnalysis)

        @property
        def coupling_compound_harmonic_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5913,
            )

            return self._parent._cast(_5913.CouplingCompoundHarmonicAnalysis)

        @property
        def cvt_compound_harmonic_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5917,
            )

            return self._parent._cast(_5917.CVTCompoundHarmonicAnalysis)

        @property
        def cycloidal_assembly_compound_harmonic_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5919,
            )

            return self._parent._cast(_5919.CycloidalAssemblyCompoundHarmonicAnalysis)

        @property
        def cylindrical_gear_set_compound_harmonic_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5925,
            )

            return self._parent._cast(_5925.CylindricalGearSetCompoundHarmonicAnalysis)

        @property
        def face_gear_set_compound_harmonic_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5931,
            )

            return self._parent._cast(_5931.FaceGearSetCompoundHarmonicAnalysis)

        @property
        def flexible_pin_assembly_compound_harmonic_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5933,
            )

            return self._parent._cast(_5933.FlexiblePinAssemblyCompoundHarmonicAnalysis)

        @property
        def gear_set_compound_harmonic_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5936,
            )

            return self._parent._cast(_5936.GearSetCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_set_compound_harmonic_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5940,
            )

            return self._parent._cast(_5940.HypoidGearSetCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_harmonic_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5944,
            )

            return self._parent._cast(
                _5944.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_harmonic_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5947,
            )

            return self._parent._cast(
                _5947.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_harmonic_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5950,
            )

            return self._parent._cast(
                _5950.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis
            )

        @property
        def part_to_part_shear_coupling_compound_harmonic_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5956,
            )

            return self._parent._cast(
                _5956.PartToPartShearCouplingCompoundHarmonicAnalysis
            )

        @property
        def planetary_gear_set_compound_harmonic_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5960,
            )

            return self._parent._cast(_5960.PlanetaryGearSetCompoundHarmonicAnalysis)

        @property
        def rolling_ring_assembly_compound_harmonic_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5967,
            )

            return self._parent._cast(_5967.RollingRingAssemblyCompoundHarmonicAnalysis)

        @property
        def root_assembly_compound_harmonic_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5970,
            )

            return self._parent._cast(_5970.RootAssemblyCompoundHarmonicAnalysis)

        @property
        def specialised_assembly_compound_harmonic_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5974,
            )

            return self._parent._cast(_5974.SpecialisedAssemblyCompoundHarmonicAnalysis)

        @property
        def spiral_bevel_gear_set_compound_harmonic_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5977,
            )

            return self._parent._cast(_5977.SpiralBevelGearSetCompoundHarmonicAnalysis)

        @property
        def spring_damper_compound_harmonic_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5978,
            )

            return self._parent._cast(_5978.SpringDamperCompoundHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_harmonic_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5983,
            )

            return self._parent._cast(
                _5983.StraightBevelDiffGearSetCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_harmonic_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5986,
            )

            return self._parent._cast(
                _5986.StraightBevelGearSetCompoundHarmonicAnalysis
            )

        @property
        def synchroniser_compound_harmonic_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5989,
            )

            return self._parent._cast(_5989.SynchroniserCompoundHarmonicAnalysis)

        @property
        def torque_converter_compound_harmonic_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5993,
            )

            return self._parent._cast(_5993.TorqueConverterCompoundHarmonicAnalysis)

        @property
        def worm_gear_set_compound_harmonic_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6001,
            )

            return self._parent._cast(_6001.WormGearSetCompoundHarmonicAnalysis)

        @property
        def zerol_bevel_gear_set_compound_harmonic_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6004,
            )

            return self._parent._cast(_6004.ZerolBevelGearSetCompoundHarmonicAnalysis)

        @property
        def abstract_assembly_compound_harmonic_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
        ) -> "AbstractAssemblyCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "AbstractAssemblyCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5675.AbstractAssemblyHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.AbstractAssemblyHarmonicAnalysis]

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
    ) -> "List[_5675.AbstractAssemblyHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.AbstractAssemblyHarmonicAnalysis]

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
    ) -> "AbstractAssemblyCompoundHarmonicAnalysis._Cast_AbstractAssemblyCompoundHarmonicAnalysis":
        return self._Cast_AbstractAssemblyCompoundHarmonicAnalysis(self)
