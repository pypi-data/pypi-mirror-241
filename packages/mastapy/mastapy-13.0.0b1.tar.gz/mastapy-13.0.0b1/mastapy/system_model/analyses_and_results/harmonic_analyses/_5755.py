"""GearSetHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5807
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "GearSetHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2530
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5750, _5752
    from mastapy.system_model.analyses_and_results.system_deflections import _2758


__docformat__ = "restructuredtext en"
__all__ = ("GearSetHarmonicAnalysis",)


Self = TypeVar("Self", bound="GearSetHarmonicAnalysis")


class GearSetHarmonicAnalysis(_5807.SpecialisedAssemblyHarmonicAnalysis):
    """GearSetHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetHarmonicAnalysis")

    class _Cast_GearSetHarmonicAnalysis:
        """Special nested class for casting GearSetHarmonicAnalysis to subclasses."""

        def __init__(
            self: "GearSetHarmonicAnalysis._Cast_GearSetHarmonicAnalysis",
            parent: "GearSetHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_harmonic_analysis(
            self: "GearSetHarmonicAnalysis._Cast_GearSetHarmonicAnalysis",
        ):
            return self._parent._cast(_5807.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(
            self: "GearSetHarmonicAnalysis._Cast_GearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5675,
            )

            return self._parent._cast(_5675.AbstractAssemblyHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "GearSetHarmonicAnalysis._Cast_GearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5785,
            )

            return self._parent._cast(_5785.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "GearSetHarmonicAnalysis._Cast_GearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GearSetHarmonicAnalysis._Cast_GearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GearSetHarmonicAnalysis._Cast_GearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearSetHarmonicAnalysis._Cast_GearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSetHarmonicAnalysis._Cast_GearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis(
            self: "GearSetHarmonicAnalysis._Cast_GearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5682,
            )

            return self._parent._cast(_5682.AGMAGleasonConicalGearSetHarmonicAnalysis)

        @property
        def bevel_differential_gear_set_harmonic_analysis(
            self: "GearSetHarmonicAnalysis._Cast_GearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5689,
            )

            return self._parent._cast(_5689.BevelDifferentialGearSetHarmonicAnalysis)

        @property
        def bevel_gear_set_harmonic_analysis(
            self: "GearSetHarmonicAnalysis._Cast_GearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5694,
            )

            return self._parent._cast(_5694.BevelGearSetHarmonicAnalysis)

        @property
        def concept_gear_set_harmonic_analysis(
            self: "GearSetHarmonicAnalysis._Cast_GearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5708,
            )

            return self._parent._cast(_5708.ConceptGearSetHarmonicAnalysis)

        @property
        def conical_gear_set_harmonic_analysis(
            self: "GearSetHarmonicAnalysis._Cast_GearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5711,
            )

            return self._parent._cast(_5711.ConicalGearSetHarmonicAnalysis)

        @property
        def cylindrical_gear_set_harmonic_analysis(
            self: "GearSetHarmonicAnalysis._Cast_GearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5726,
            )

            return self._parent._cast(_5726.CylindricalGearSetHarmonicAnalysis)

        @property
        def face_gear_set_harmonic_analysis(
            self: "GearSetHarmonicAnalysis._Cast_GearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5746,
            )

            return self._parent._cast(_5746.FaceGearSetHarmonicAnalysis)

        @property
        def hypoid_gear_set_harmonic_analysis(
            self: "GearSetHarmonicAnalysis._Cast_GearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5770,
            )

            return self._parent._cast(_5770.HypoidGearSetHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis(
            self: "GearSetHarmonicAnalysis._Cast_GearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5774,
            )

            return self._parent._cast(
                _5774.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_harmonic_analysis(
            self: "GearSetHarmonicAnalysis._Cast_GearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5777,
            )

            return self._parent._cast(
                _5777.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_harmonic_analysis(
            self: "GearSetHarmonicAnalysis._Cast_GearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5780,
            )

            return self._parent._cast(
                _5780.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis
            )

        @property
        def planetary_gear_set_harmonic_analysis(
            self: "GearSetHarmonicAnalysis._Cast_GearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5791,
            )

            return self._parent._cast(_5791.PlanetaryGearSetHarmonicAnalysis)

        @property
        def spiral_bevel_gear_set_harmonic_analysis(
            self: "GearSetHarmonicAnalysis._Cast_GearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5811,
            )

            return self._parent._cast(_5811.SpiralBevelGearSetHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_set_harmonic_analysis(
            self: "GearSetHarmonicAnalysis._Cast_GearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5818,
            )

            return self._parent._cast(_5818.StraightBevelDiffGearSetHarmonicAnalysis)

        @property
        def straight_bevel_gear_set_harmonic_analysis(
            self: "GearSetHarmonicAnalysis._Cast_GearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5821,
            )

            return self._parent._cast(_5821.StraightBevelGearSetHarmonicAnalysis)

        @property
        def worm_gear_set_harmonic_analysis(
            self: "GearSetHarmonicAnalysis._Cast_GearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5837,
            )

            return self._parent._cast(_5837.WormGearSetHarmonicAnalysis)

        @property
        def zerol_bevel_gear_set_harmonic_analysis(
            self: "GearSetHarmonicAnalysis._Cast_GearSetHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5840,
            )

            return self._parent._cast(_5840.ZerolBevelGearSetHarmonicAnalysis)

        @property
        def gear_set_harmonic_analysis(
            self: "GearSetHarmonicAnalysis._Cast_GearSetHarmonicAnalysis",
        ) -> "GearSetHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "GearSetHarmonicAnalysis._Cast_GearSetHarmonicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2530.GearSet":
        """mastapy.system_model.part_model.gears.GearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears_harmonic_analysis(self: Self) -> "List[_5750.GearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.GearHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearsHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_harmonic_analysis(self: Self) -> "List[_5752.GearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.GearMeshHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshesHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def system_deflection_results(self: Self) -> "_2758.GearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.GearSetSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "GearSetHarmonicAnalysis._Cast_GearSetHarmonicAnalysis":
        return self._Cast_GearSetHarmonicAnalysis(self)
