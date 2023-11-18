"""AGMAGleasonConicalGearMeshHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5710
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "AGMAGleasonConicalGearMeshHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2297
    from mastapy.system_model.analyses_and_results.system_deflections import _2687


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshHarmonicAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearMeshHarmonicAnalysis")


class AGMAGleasonConicalGearMeshHarmonicAnalysis(_5710.ConicalGearMeshHarmonicAnalysis):
    """AGMAGleasonConicalGearMeshHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearMeshHarmonicAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis",
            parent: "AGMAGleasonConicalGearMeshHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_harmonic_analysis(
            self: "AGMAGleasonConicalGearMeshHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis",
        ):
            return self._parent._cast(_5710.ConicalGearMeshHarmonicAnalysis)

        @property
        def gear_mesh_harmonic_analysis(
            self: "AGMAGleasonConicalGearMeshHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5752,
            )

            return self._parent._cast(_5752.GearMeshHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_harmonic_analysis(
            self: "AGMAGleasonConicalGearMeshHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5771,
            )

            return self._parent._cast(
                _5771.InterMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def connection_harmonic_analysis(
            self: "AGMAGleasonConicalGearMeshHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5712,
            )

            return self._parent._cast(_5712.ConnectionHarmonicAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "AGMAGleasonConicalGearMeshHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "AGMAGleasonConicalGearMeshHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AGMAGleasonConicalGearMeshHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearMeshHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_harmonic_analysis(
            self: "AGMAGleasonConicalGearMeshHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5688,
            )

            return self._parent._cast(_5688.BevelDifferentialGearMeshHarmonicAnalysis)

        @property
        def bevel_gear_mesh_harmonic_analysis(
            self: "AGMAGleasonConicalGearMeshHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5693,
            )

            return self._parent._cast(_5693.BevelGearMeshHarmonicAnalysis)

        @property
        def hypoid_gear_mesh_harmonic_analysis(
            self: "AGMAGleasonConicalGearMeshHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5769,
            )

            return self._parent._cast(_5769.HypoidGearMeshHarmonicAnalysis)

        @property
        def spiral_bevel_gear_mesh_harmonic_analysis(
            self: "AGMAGleasonConicalGearMeshHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5810,
            )

            return self._parent._cast(_5810.SpiralBevelGearMeshHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_harmonic_analysis(
            self: "AGMAGleasonConicalGearMeshHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5817,
            )

            return self._parent._cast(_5817.StraightBevelDiffGearMeshHarmonicAnalysis)

        @property
        def straight_bevel_gear_mesh_harmonic_analysis(
            self: "AGMAGleasonConicalGearMeshHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5820,
            )

            return self._parent._cast(_5820.StraightBevelGearMeshHarmonicAnalysis)

        @property
        def zerol_bevel_gear_mesh_harmonic_analysis(
            self: "AGMAGleasonConicalGearMeshHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5839,
            )

            return self._parent._cast(_5839.ZerolBevelGearMeshHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_harmonic_analysis(
            self: "AGMAGleasonConicalGearMeshHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis",
        ) -> "AGMAGleasonConicalGearMeshHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearMeshHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2297.AGMAGleasonConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2687.AGMAGleasonConicalGearMeshSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearMeshSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearMeshHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis":
        return self._Cast_AGMAGleasonConicalGearMeshHarmonicAnalysis(self)
