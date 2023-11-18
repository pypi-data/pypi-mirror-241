"""BevelGearMeshCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3900
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "BevelGearMeshCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3777


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="BevelGearMeshCompoundStabilityAnalysis")


class BevelGearMeshCompoundStabilityAnalysis(
    _3900.AGMAGleasonConicalGearMeshCompoundStabilityAnalysis
):
    """BevelGearMeshCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearMeshCompoundStabilityAnalysis"
    )

    class _Cast_BevelGearMeshCompoundStabilityAnalysis:
        """Special nested class for casting BevelGearMeshCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "BevelGearMeshCompoundStabilityAnalysis._Cast_BevelGearMeshCompoundStabilityAnalysis",
            parent: "BevelGearMeshCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_compound_stability_analysis(
            self: "BevelGearMeshCompoundStabilityAnalysis._Cast_BevelGearMeshCompoundStabilityAnalysis",
        ):
            return self._parent._cast(
                _3900.AGMAGleasonConicalGearMeshCompoundStabilityAnalysis
            )

        @property
        def conical_gear_mesh_compound_stability_analysis(
            self: "BevelGearMeshCompoundStabilityAnalysis._Cast_BevelGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3928,
            )

            return self._parent._cast(_3928.ConicalGearMeshCompoundStabilityAnalysis)

        @property
        def gear_mesh_compound_stability_analysis(
            self: "BevelGearMeshCompoundStabilityAnalysis._Cast_BevelGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3954,
            )

            return self._parent._cast(_3954.GearMeshCompoundStabilityAnalysis)

        @property
        def inter_mountable_component_connection_compound_stability_analysis(
            self: "BevelGearMeshCompoundStabilityAnalysis._Cast_BevelGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3960,
            )

            return self._parent._cast(
                _3960.InterMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def connection_compound_stability_analysis(
            self: "BevelGearMeshCompoundStabilityAnalysis._Cast_BevelGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3930,
            )

            return self._parent._cast(_3930.ConnectionCompoundStabilityAnalysis)

        @property
        def connection_compound_analysis(
            self: "BevelGearMeshCompoundStabilityAnalysis._Cast_BevelGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearMeshCompoundStabilityAnalysis._Cast_BevelGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshCompoundStabilityAnalysis._Cast_BevelGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_stability_analysis(
            self: "BevelGearMeshCompoundStabilityAnalysis._Cast_BevelGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3907,
            )

            return self._parent._cast(
                _3907.BevelDifferentialGearMeshCompoundStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_stability_analysis(
            self: "BevelGearMeshCompoundStabilityAnalysis._Cast_BevelGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3995,
            )

            return self._parent._cast(
                _3995.SpiralBevelGearMeshCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_stability_analysis(
            self: "BevelGearMeshCompoundStabilityAnalysis._Cast_BevelGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4001,
            )

            return self._parent._cast(
                _4001.StraightBevelDiffGearMeshCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_stability_analysis(
            self: "BevelGearMeshCompoundStabilityAnalysis._Cast_BevelGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4004,
            )

            return self._parent._cast(
                _4004.StraightBevelGearMeshCompoundStabilityAnalysis
            )

        @property
        def zerol_bevel_gear_mesh_compound_stability_analysis(
            self: "BevelGearMeshCompoundStabilityAnalysis._Cast_BevelGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4022,
            )

            return self._parent._cast(_4022.ZerolBevelGearMeshCompoundStabilityAnalysis)

        @property
        def bevel_gear_mesh_compound_stability_analysis(
            self: "BevelGearMeshCompoundStabilityAnalysis._Cast_BevelGearMeshCompoundStabilityAnalysis",
        ) -> "BevelGearMeshCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshCompoundStabilityAnalysis._Cast_BevelGearMeshCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "BevelGearMeshCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3777.BevelGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.BevelGearMeshStabilityAnalysis]

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
    ) -> "List[_3777.BevelGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.BevelGearMeshStabilityAnalysis]

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
    ) -> "BevelGearMeshCompoundStabilityAnalysis._Cast_BevelGearMeshCompoundStabilityAnalysis":
        return self._Cast_BevelGearMeshCompoundStabilityAnalysis(self)
