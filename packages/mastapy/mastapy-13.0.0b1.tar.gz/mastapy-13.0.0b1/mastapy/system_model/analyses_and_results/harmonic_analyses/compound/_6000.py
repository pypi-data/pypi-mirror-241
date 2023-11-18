"""WormGearMeshCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5935
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "WormGearMeshCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2327
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5836


__docformat__ = "restructuredtext en"
__all__ = ("WormGearMeshCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="WormGearMeshCompoundHarmonicAnalysis")


class WormGearMeshCompoundHarmonicAnalysis(_5935.GearMeshCompoundHarmonicAnalysis):
    """WormGearMeshCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearMeshCompoundHarmonicAnalysis")

    class _Cast_WormGearMeshCompoundHarmonicAnalysis:
        """Special nested class for casting WormGearMeshCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "WormGearMeshCompoundHarmonicAnalysis._Cast_WormGearMeshCompoundHarmonicAnalysis",
            parent: "WormGearMeshCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_compound_harmonic_analysis(
            self: "WormGearMeshCompoundHarmonicAnalysis._Cast_WormGearMeshCompoundHarmonicAnalysis",
        ):
            return self._parent._cast(_5935.GearMeshCompoundHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis(
            self: "WormGearMeshCompoundHarmonicAnalysis._Cast_WormGearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5941,
            )

            return self._parent._cast(
                _5941.InterMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def connection_compound_harmonic_analysis(
            self: "WormGearMeshCompoundHarmonicAnalysis._Cast_WormGearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5911,
            )

            return self._parent._cast(_5911.ConnectionCompoundHarmonicAnalysis)

        @property
        def connection_compound_analysis(
            self: "WormGearMeshCompoundHarmonicAnalysis._Cast_WormGearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "WormGearMeshCompoundHarmonicAnalysis._Cast_WormGearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearMeshCompoundHarmonicAnalysis._Cast_WormGearMeshCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def worm_gear_mesh_compound_harmonic_analysis(
            self: "WormGearMeshCompoundHarmonicAnalysis._Cast_WormGearMeshCompoundHarmonicAnalysis",
        ) -> "WormGearMeshCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "WormGearMeshCompoundHarmonicAnalysis._Cast_WormGearMeshCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "WormGearMeshCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2327.WormGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.WormGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2327.WormGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.WormGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5836.WormGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.WormGearMeshHarmonicAnalysis]

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
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5836.WormGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.WormGearMeshHarmonicAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "WormGearMeshCompoundHarmonicAnalysis._Cast_WormGearMeshCompoundHarmonicAnalysis":
        return self._Cast_WormGearMeshCompoundHarmonicAnalysis(self)
