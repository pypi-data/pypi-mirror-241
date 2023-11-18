"""GearMeshCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3960
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "GearMeshCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3821


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="GearMeshCompoundStabilityAnalysis")


class GearMeshCompoundStabilityAnalysis(
    _3960.InterMountableComponentConnectionCompoundStabilityAnalysis
):
    """GearMeshCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshCompoundStabilityAnalysis")

    class _Cast_GearMeshCompoundStabilityAnalysis:
        """Special nested class for casting GearMeshCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
            parent: "GearMeshCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ):
            return self._parent._cast(
                _3960.InterMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def connection_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3930,
            )

            return self._parent._cast(_3930.ConnectionCompoundStabilityAnalysis)

        @property
        def connection_compound_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3900,
            )

            return self._parent._cast(
                _3900.AGMAGleasonConicalGearMeshCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3907,
            )

            return self._parent._cast(
                _3907.BevelDifferentialGearMeshCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3912,
            )

            return self._parent._cast(_3912.BevelGearMeshCompoundStabilityAnalysis)

        @property
        def concept_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3925,
            )

            return self._parent._cast(_3925.ConceptGearMeshCompoundStabilityAnalysis)

        @property
        def conical_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3928,
            )

            return self._parent._cast(_3928.ConicalGearMeshCompoundStabilityAnalysis)

        @property
        def cylindrical_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3943,
            )

            return self._parent._cast(
                _3943.CylindricalGearMeshCompoundStabilityAnalysis
            )

        @property
        def face_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3949,
            )

            return self._parent._cast(_3949.FaceGearMeshCompoundStabilityAnalysis)

        @property
        def hypoid_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3958,
            )

            return self._parent._cast(_3958.HypoidGearMeshCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3962,
            )

            return self._parent._cast(
                _3962.KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3965,
            )

            return self._parent._cast(
                _3965.KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3968,
            )

            return self._parent._cast(
                _3968.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3995,
            )

            return self._parent._cast(
                _3995.SpiralBevelGearMeshCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4001,
            )

            return self._parent._cast(
                _4001.StraightBevelDiffGearMeshCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4004,
            )

            return self._parent._cast(
                _4004.StraightBevelGearMeshCompoundStabilityAnalysis
            )

        @property
        def worm_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4019,
            )

            return self._parent._cast(_4019.WormGearMeshCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4022,
            )

            return self._parent._cast(_4022.ZerolBevelGearMeshCompoundStabilityAnalysis)

        @property
        def gear_mesh_compound_stability_analysis(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
        ) -> "GearMeshCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "GearMeshCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3821.GearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.GearMeshStabilityAnalysis]

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
    ) -> "List[_3821.GearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.GearMeshStabilityAnalysis]

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
    ) -> "GearMeshCompoundStabilityAnalysis._Cast_GearMeshCompoundStabilityAnalysis":
        return self._Cast_GearMeshCompoundStabilityAnalysis(self)
