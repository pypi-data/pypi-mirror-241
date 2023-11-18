"""GearMeshCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5941
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "GearMeshCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5752


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="GearMeshCompoundHarmonicAnalysis")


class GearMeshCompoundHarmonicAnalysis(
    _5941.InterMountableComponentConnectionCompoundHarmonicAnalysis
):
    """GearMeshCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshCompoundHarmonicAnalysis")

    class _Cast_GearMeshCompoundHarmonicAnalysis:
        """Special nested class for casting GearMeshCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
            parent: "GearMeshCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ):
            return self._parent._cast(
                _5941.InterMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def connection_compound_harmonic_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5911,
            )

            return self._parent._cast(_5911.ConnectionCompoundHarmonicAnalysis)

        @property
        def connection_compound_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_harmonic_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5881,
            )

            return self._parent._cast(
                _5881.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis
            )

        @property
        def bevel_differential_gear_mesh_compound_harmonic_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5888,
            )

            return self._parent._cast(
                _5888.BevelDifferentialGearMeshCompoundHarmonicAnalysis
            )

        @property
        def bevel_gear_mesh_compound_harmonic_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5893,
            )

            return self._parent._cast(_5893.BevelGearMeshCompoundHarmonicAnalysis)

        @property
        def concept_gear_mesh_compound_harmonic_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5906,
            )

            return self._parent._cast(_5906.ConceptGearMeshCompoundHarmonicAnalysis)

        @property
        def conical_gear_mesh_compound_harmonic_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5909,
            )

            return self._parent._cast(_5909.ConicalGearMeshCompoundHarmonicAnalysis)

        @property
        def cylindrical_gear_mesh_compound_harmonic_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5924,
            )

            return self._parent._cast(_5924.CylindricalGearMeshCompoundHarmonicAnalysis)

        @property
        def face_gear_mesh_compound_harmonic_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5930,
            )

            return self._parent._cast(_5930.FaceGearMeshCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_mesh_compound_harmonic_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5939,
            )

            return self._parent._cast(_5939.HypoidGearMeshCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_harmonic_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5943,
            )

            return self._parent._cast(
                _5943.KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_harmonic_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5946,
            )

            return self._parent._cast(
                _5946.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_harmonic_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5949,
            )

            return self._parent._cast(
                _5949.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_harmonic_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5976,
            )

            return self._parent._cast(_5976.SpiralBevelGearMeshCompoundHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_harmonic_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5982,
            )

            return self._parent._cast(
                _5982.StraightBevelDiffGearMeshCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_harmonic_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5985,
            )

            return self._parent._cast(
                _5985.StraightBevelGearMeshCompoundHarmonicAnalysis
            )

        @property
        def worm_gear_mesh_compound_harmonic_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6000,
            )

            return self._parent._cast(_6000.WormGearMeshCompoundHarmonicAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_harmonic_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6003,
            )

            return self._parent._cast(_6003.ZerolBevelGearMeshCompoundHarmonicAnalysis)

        @property
        def gear_mesh_compound_harmonic_analysis(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
        ) -> "GearMeshCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshCompoundHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self: Self) -> "List[_5752.GearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.GearMeshHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5752.GearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.GearMeshHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "GearMeshCompoundHarmonicAnalysis._Cast_GearMeshCompoundHarmonicAnalysis":
        return self._Cast_GearMeshCompoundHarmonicAnalysis(self)
