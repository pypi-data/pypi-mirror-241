"""ConicalGearMeshCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5585
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "ConicalGearMeshCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5408


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="ConicalGearMeshCompoundMultibodyDynamicsAnalysis")


class ConicalGearMeshCompoundMultibodyDynamicsAnalysis(
    _5585.GearMeshCompoundMultibodyDynamicsAnalysis
):
    """ConicalGearMeshCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearMeshCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_ConicalGearMeshCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting ConicalGearMeshCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_ConicalGearMeshCompoundMultibodyDynamicsAnalysis",
            parent: "ConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_ConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5585.GearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "ConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_ConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5591,
            )

            return self._parent._cast(
                _5591.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def connection_compound_multibody_dynamics_analysis(
            self: "ConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_ConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5561,
            )

            return self._parent._cast(_5561.ConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def connection_compound_analysis(
            self: "ConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_ConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_ConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_ConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_ConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5531,
            )

            return self._parent._cast(
                _5531.AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_ConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5538,
            )

            return self._parent._cast(
                _5538.BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_ConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5543,
            )

            return self._parent._cast(
                _5543.BevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def hypoid_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_ConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5589,
            )

            return self._parent._cast(
                _5589.HypoidGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_ConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5593,
            )

            return self._parent._cast(
                _5593.KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_ConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5596,
            )

            return self._parent._cast(
                _5596.KlingelnbergCycloPalloidHypoidGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_ConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5599,
            )

            return self._parent._cast(
                _5599.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_ConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5626,
            )

            return self._parent._cast(
                _5626.SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_ConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5632,
            )

            return self._parent._cast(
                _5632.StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_ConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5635,
            )

            return self._parent._cast(
                _5635.StraightBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_ConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5653,
            )

            return self._parent._cast(
                _5653.ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_ConicalGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "ConicalGearMeshCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_ConicalGearMeshCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "ConicalGearMeshCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planetaries(
        self: Self,
    ) -> "List[ConicalGearMeshCompoundMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ConicalGearMeshCompoundMultibodyDynamicsAnalysis]

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
    ) -> "List[_5408.ConicalGearMeshMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ConicalGearMeshMultibodyDynamicsAnalysis]

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
    ) -> "List[_5408.ConicalGearMeshMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ConicalGearMeshMultibodyDynamicsAnalysis]

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
    ) -> "ConicalGearMeshCompoundMultibodyDynamicsAnalysis._Cast_ConicalGearMeshCompoundMultibodyDynamicsAnalysis":
        return self._Cast_ConicalGearMeshCompoundMultibodyDynamicsAnalysis(self)
