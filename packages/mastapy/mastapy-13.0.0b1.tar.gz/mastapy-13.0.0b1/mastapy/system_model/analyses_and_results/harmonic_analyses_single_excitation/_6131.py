"""WormGearMeshHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6064,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MESH_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "WormGearMeshHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2327
    from mastapy.system_model.analyses_and_results.static_loads import _6981


__docformat__ = "restructuredtext en"
__all__ = ("WormGearMeshHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="WormGearMeshHarmonicAnalysisOfSingleExcitation")


class WormGearMeshHarmonicAnalysisOfSingleExcitation(
    _6064.GearMeshHarmonicAnalysisOfSingleExcitation
):
    """WormGearMeshHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_MESH_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_WormGearMeshHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_WormGearMeshHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting WormGearMeshHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "WormGearMeshHarmonicAnalysisOfSingleExcitation._Cast_WormGearMeshHarmonicAnalysisOfSingleExcitation",
            parent: "WormGearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def gear_mesh_harmonic_analysis_of_single_excitation(
            self: "WormGearMeshHarmonicAnalysisOfSingleExcitation._Cast_WormGearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(_6064.GearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def inter_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "WormGearMeshHarmonicAnalysisOfSingleExcitation._Cast_WormGearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6071,
            )

            return self._parent._cast(
                _6071.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_harmonic_analysis_of_single_excitation(
            self: "WormGearMeshHarmonicAnalysisOfSingleExcitation._Cast_WormGearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6040,
            )

            return self._parent._cast(
                _6040.ConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_static_load_analysis_case(
            self: "WormGearMeshHarmonicAnalysisOfSingleExcitation._Cast_WormGearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "WormGearMeshHarmonicAnalysisOfSingleExcitation._Cast_WormGearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "WormGearMeshHarmonicAnalysisOfSingleExcitation._Cast_WormGearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "WormGearMeshHarmonicAnalysisOfSingleExcitation._Cast_WormGearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearMeshHarmonicAnalysisOfSingleExcitation._Cast_WormGearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def worm_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "WormGearMeshHarmonicAnalysisOfSingleExcitation._Cast_WormGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "WormGearMeshHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "WormGearMeshHarmonicAnalysisOfSingleExcitation._Cast_WormGearMeshHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "WormGearMeshHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def connection_load_case(self: Self) -> "_6981.WormGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.WormGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "WormGearMeshHarmonicAnalysisOfSingleExcitation._Cast_WormGearMeshHarmonicAnalysisOfSingleExcitation":
        return self._Cast_WormGearMeshHarmonicAnalysisOfSingleExcitation(self)
