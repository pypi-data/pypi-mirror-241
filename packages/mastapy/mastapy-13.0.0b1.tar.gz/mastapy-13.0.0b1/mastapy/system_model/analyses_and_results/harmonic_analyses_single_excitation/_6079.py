"""KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6073,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2318
    from mastapy.system_model.analyses_and_results.static_loads import _6917


__docformat__ = "restructuredtext en"
__all__ = (
    "KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation",
)


Self = TypeVar(
    "Self",
    bound="KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation",
)


class KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation(
    _6073.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysisOfSingleExcitation
):
    """KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(
                _6073.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6038,
            )

            return self._parent._cast(
                _6038.ConicalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_mesh_harmonic_analysis_of_single_excitation(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6064,
            )

            return self._parent._cast(_6064.GearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def inter_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6071,
            )

            return self._parent._cast(
                _6071.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_harmonic_analysis_of_single_excitation(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6040,
            )

            return self._parent._cast(
                _6040.ConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2318.KlingelnbergCycloPalloidSpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(
        self: Self,
    ) -> "_6917.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase

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
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation(
            self
        )
