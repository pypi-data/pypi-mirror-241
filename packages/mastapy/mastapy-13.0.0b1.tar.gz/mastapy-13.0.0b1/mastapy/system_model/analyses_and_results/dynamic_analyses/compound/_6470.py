"""InterMountableComponentConnectionCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6440
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "InterMountableComponentConnectionCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6341


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="InterMountableComponentConnectionCompoundDynamicAnalysis")


class InterMountableComponentConnectionCompoundDynamicAnalysis(
    _6440.ConnectionCompoundDynamicAnalysis
):
    """InterMountableComponentConnectionCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
    )

    class _Cast_InterMountableComponentConnectionCompoundDynamicAnalysis:
        """Special nested class for casting InterMountableComponentConnectionCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
            parent: "InterMountableComponentConnectionCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def connection_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ):
            return self._parent._cast(_6440.ConnectionCompoundDynamicAnalysis)

        @property
        def connection_compound_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6410,
            )

            return self._parent._cast(
                _6410.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis
            )

        @property
        def belt_connection_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6414,
            )

            return self._parent._cast(_6414.BeltConnectionCompoundDynamicAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6417,
            )

            return self._parent._cast(
                _6417.BevelDifferentialGearMeshCompoundDynamicAnalysis
            )

        @property
        def bevel_gear_mesh_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6422,
            )

            return self._parent._cast(_6422.BevelGearMeshCompoundDynamicAnalysis)

        @property
        def clutch_connection_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6427,
            )

            return self._parent._cast(_6427.ClutchConnectionCompoundDynamicAnalysis)

        @property
        def concept_coupling_connection_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6432,
            )

            return self._parent._cast(
                _6432.ConceptCouplingConnectionCompoundDynamicAnalysis
            )

        @property
        def concept_gear_mesh_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6435,
            )

            return self._parent._cast(_6435.ConceptGearMeshCompoundDynamicAnalysis)

        @property
        def conical_gear_mesh_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6438,
            )

            return self._parent._cast(_6438.ConicalGearMeshCompoundDynamicAnalysis)

        @property
        def coupling_connection_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6443,
            )

            return self._parent._cast(_6443.CouplingConnectionCompoundDynamicAnalysis)

        @property
        def cvt_belt_connection_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6445,
            )

            return self._parent._cast(_6445.CVTBeltConnectionCompoundDynamicAnalysis)

        @property
        def cylindrical_gear_mesh_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6453,
            )

            return self._parent._cast(_6453.CylindricalGearMeshCompoundDynamicAnalysis)

        @property
        def face_gear_mesh_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6459,
            )

            return self._parent._cast(_6459.FaceGearMeshCompoundDynamicAnalysis)

        @property
        def gear_mesh_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6464,
            )

            return self._parent._cast(_6464.GearMeshCompoundDynamicAnalysis)

        @property
        def hypoid_gear_mesh_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6468,
            )

            return self._parent._cast(_6468.HypoidGearMeshCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6472,
            )

            return self._parent._cast(
                _6472.KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6475,
            )

            return self._parent._cast(
                _6475.KlingelnbergCycloPalloidHypoidGearMeshCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6478,
            )

            return self._parent._cast(
                _6478.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundDynamicAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6486,
            )

            return self._parent._cast(
                _6486.PartToPartShearCouplingConnectionCompoundDynamicAnalysis
            )

        @property
        def ring_pins_to_disc_connection_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6495,
            )

            return self._parent._cast(
                _6495.RingPinsToDiscConnectionCompoundDynamicAnalysis
            )

        @property
        def rolling_ring_connection_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6498,
            )

            return self._parent._cast(
                _6498.RollingRingConnectionCompoundDynamicAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6505,
            )

            return self._parent._cast(_6505.SpiralBevelGearMeshCompoundDynamicAnalysis)

        @property
        def spring_damper_connection_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6508,
            )

            return self._parent._cast(
                _6508.SpringDamperConnectionCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6511,
            )

            return self._parent._cast(
                _6511.StraightBevelDiffGearMeshCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6514,
            )

            return self._parent._cast(
                _6514.StraightBevelGearMeshCompoundDynamicAnalysis
            )

        @property
        def torque_converter_connection_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6523,
            )

            return self._parent._cast(
                _6523.TorqueConverterConnectionCompoundDynamicAnalysis
            )

        @property
        def worm_gear_mesh_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6529,
            )

            return self._parent._cast(_6529.WormGearMeshCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6532,
            )

            return self._parent._cast(_6532.ZerolBevelGearMeshCompoundDynamicAnalysis)

        @property
        def inter_mountable_component_connection_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "InterMountableComponentConnectionCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
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
        instance_to_wrap: "InterMountableComponentConnectionCompoundDynamicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6341.InterMountableComponentConnectionDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.InterMountableComponentConnectionDynamicAnalysis]

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
    ) -> "List[_6341.InterMountableComponentConnectionDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.InterMountableComponentConnectionDynamicAnalysis]

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
    ) -> "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis":
        return self._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis(self)
