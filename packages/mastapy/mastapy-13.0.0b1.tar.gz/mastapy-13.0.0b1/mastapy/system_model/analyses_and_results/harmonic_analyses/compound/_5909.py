"""ConicalGearMeshCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5935
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "ConicalGearMeshCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5710


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="ConicalGearMeshCompoundHarmonicAnalysis")


class ConicalGearMeshCompoundHarmonicAnalysis(_5935.GearMeshCompoundHarmonicAnalysis):
    """ConicalGearMeshCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearMeshCompoundHarmonicAnalysis"
    )

    class _Cast_ConicalGearMeshCompoundHarmonicAnalysis:
        """Special nested class for casting ConicalGearMeshCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis",
            parent: "ConicalGearMeshCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_compound_harmonic_analysis(
            self: "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis",
        ):
            return self._parent._cast(_5935.GearMeshCompoundHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis(
            self: "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5941,
            )

            return self._parent._cast(
                _5941.InterMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def connection_compound_harmonic_analysis(
            self: "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5911,
            )

            return self._parent._cast(_5911.ConnectionCompoundHarmonicAnalysis)

        @property
        def connection_compound_analysis(
            self: "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_harmonic_analysis(
            self: "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5881,
            )

            return self._parent._cast(
                _5881.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis
            )

        @property
        def bevel_differential_gear_mesh_compound_harmonic_analysis(
            self: "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5888,
            )

            return self._parent._cast(
                _5888.BevelDifferentialGearMeshCompoundHarmonicAnalysis
            )

        @property
        def bevel_gear_mesh_compound_harmonic_analysis(
            self: "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5893,
            )

            return self._parent._cast(_5893.BevelGearMeshCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_mesh_compound_harmonic_analysis(
            self: "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5939,
            )

            return self._parent._cast(_5939.HypoidGearMeshCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_harmonic_analysis(
            self: "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5943,
            )

            return self._parent._cast(
                _5943.KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_harmonic_analysis(
            self: "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5946,
            )

            return self._parent._cast(
                _5946.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_harmonic_analysis(
            self: "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5949,
            )

            return self._parent._cast(
                _5949.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_harmonic_analysis(
            self: "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5976,
            )

            return self._parent._cast(_5976.SpiralBevelGearMeshCompoundHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_harmonic_analysis(
            self: "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5982,
            )

            return self._parent._cast(
                _5982.StraightBevelDiffGearMeshCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_harmonic_analysis(
            self: "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5985,
            )

            return self._parent._cast(
                _5985.StraightBevelGearMeshCompoundHarmonicAnalysis
            )

        @property
        def zerol_bevel_gear_mesh_compound_harmonic_analysis(
            self: "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6003,
            )

            return self._parent._cast(_6003.ZerolBevelGearMeshCompoundHarmonicAnalysis)

        @property
        def conical_gear_mesh_compound_harmonic_analysis(
            self: "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "ConicalGearMeshCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "ConicalGearMeshCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planetaries(self: Self) -> "List[ConicalGearMeshCompoundHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.compound.ConicalGearMeshCompoundHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5710.ConicalGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ConicalGearMeshHarmonicAnalysis]

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
    ) -> "List[_5710.ConicalGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ConicalGearMeshHarmonicAnalysis]

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
    ) -> "ConicalGearMeshCompoundHarmonicAnalysis._Cast_ConicalGearMeshCompoundHarmonicAnalysis":
        return self._Cast_ConicalGearMeshCompoundHarmonicAnalysis(self)
