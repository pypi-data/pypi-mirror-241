"""KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3962
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_COMPOUND_STABILITY_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
        "KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2317
    from mastapy.system_model.analyses_and_results.stability_analyses import _3832


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis"
)


class KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis(
    _3962.KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis
):
    """KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis",
            parent: "KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis",
        ):
            return self._parent._cast(
                _3962.KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis
            )

        @property
        def conical_gear_mesh_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3928,
            )

            return self._parent._cast(_3928.ConicalGearMeshCompoundStabilityAnalysis)

        @property
        def gear_mesh_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3954,
            )

            return self._parent._cast(_3954.GearMeshCompoundStabilityAnalysis)

        @property
        def inter_mountable_component_connection_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3960,
            )

            return self._parent._cast(
                _3960.InterMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def connection_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3930,
            )

            return self._parent._cast(_3930.ConnectionCompoundStabilityAnalysis)

        @property
        def connection_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_stability_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis",
        ) -> "KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2317.KlingelnbergCycloPalloidHypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2317.KlingelnbergCycloPalloidHypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh

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
    ) -> "List[_3832.KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis]

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
    ) -> "List[_3832.KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis]

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
    ) -> "KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis":
        return (
            self._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis(
                self
            )
        )
