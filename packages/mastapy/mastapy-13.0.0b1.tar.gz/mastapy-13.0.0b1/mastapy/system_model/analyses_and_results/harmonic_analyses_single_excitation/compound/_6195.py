"""GearMeshCompoundHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6201,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6064,
    )


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="GearMeshCompoundHarmonicAnalysisOfSingleExcitation")


class GearMeshCompoundHarmonicAnalysisOfSingleExcitation(
    _6201.InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
):
    """GearMeshCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting GearMeshCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(
                _6201.InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_compound_harmonic_analysis_of_single_excitation(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6171,
            )

            return self._parent._cast(
                _6171.ConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_compound_analysis(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6141,
            )

            return self._parent._cast(
                _6141.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6148,
            )

            return self._parent._cast(
                _6148.BevelDifferentialGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6153,
            )

            return self._parent._cast(
                _6153.BevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6166,
            )

            return self._parent._cast(
                _6166.ConceptGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6169,
            )

            return self._parent._cast(
                _6169.ConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6184,
            )

            return self._parent._cast(
                _6184.CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6190,
            )

            return self._parent._cast(
                _6190.FaceGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6199,
            )

            return self._parent._cast(
                _6199.HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6203,
            )

            return self._parent._cast(
                _6203.KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6206,
            )

            return self._parent._cast(
                _6206.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6209,
            )

            return self._parent._cast(
                _6209.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6236,
            )

            return self._parent._cast(
                _6236.SpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6242,
            )

            return self._parent._cast(
                _6242.StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6245,
            )

            return self._parent._cast(
                _6245.StraightBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6260,
            )

            return self._parent._cast(
                _6260.WormGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6263,
            )

            return self._parent._cast(
                _6263.ZerolBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "GearMeshCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "GearMeshCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6064.GearMeshHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.GearMeshHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6064.GearMeshHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.GearMeshHarmonicAnalysisOfSingleExcitation]

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
    ) -> "GearMeshCompoundHarmonicAnalysisOfSingleExcitation._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_GearMeshCompoundHarmonicAnalysisOfSingleExcitation(self)
