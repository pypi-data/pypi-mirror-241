"""InterMountableComponentConnectionCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4760
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "InterMountableComponentConnectionCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4639


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionCompoundModalAnalysis",)


Self = TypeVar("Self", bound="InterMountableComponentConnectionCompoundModalAnalysis")


class InterMountableComponentConnectionCompoundModalAnalysis(
    _4760.ConnectionCompoundModalAnalysis
):
    """InterMountableComponentConnectionCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionCompoundModalAnalysis",
    )

    class _Cast_InterMountableComponentConnectionCompoundModalAnalysis:
        """Special nested class for casting InterMountableComponentConnectionCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
            parent: "InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            return self._parent._cast(_4760.ConnectionCompoundModalAnalysis)

        @property
        def connection_compound_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4730,
            )

            return self._parent._cast(
                _4730.AGMAGleasonConicalGearMeshCompoundModalAnalysis
            )

        @property
        def belt_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4734,
            )

            return self._parent._cast(_4734.BeltConnectionCompoundModalAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4737,
            )

            return self._parent._cast(
                _4737.BevelDifferentialGearMeshCompoundModalAnalysis
            )

        @property
        def bevel_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4742,
            )

            return self._parent._cast(_4742.BevelGearMeshCompoundModalAnalysis)

        @property
        def clutch_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4747,
            )

            return self._parent._cast(_4747.ClutchConnectionCompoundModalAnalysis)

        @property
        def concept_coupling_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4752,
            )

            return self._parent._cast(
                _4752.ConceptCouplingConnectionCompoundModalAnalysis
            )

        @property
        def concept_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4755,
            )

            return self._parent._cast(_4755.ConceptGearMeshCompoundModalAnalysis)

        @property
        def conical_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4758,
            )

            return self._parent._cast(_4758.ConicalGearMeshCompoundModalAnalysis)

        @property
        def coupling_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4763,
            )

            return self._parent._cast(_4763.CouplingConnectionCompoundModalAnalysis)

        @property
        def cvt_belt_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4765,
            )

            return self._parent._cast(_4765.CVTBeltConnectionCompoundModalAnalysis)

        @property
        def cylindrical_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4773,
            )

            return self._parent._cast(_4773.CylindricalGearMeshCompoundModalAnalysis)

        @property
        def face_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4779,
            )

            return self._parent._cast(_4779.FaceGearMeshCompoundModalAnalysis)

        @property
        def gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4784,
            )

            return self._parent._cast(_4784.GearMeshCompoundModalAnalysis)

        @property
        def hypoid_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4788,
            )

            return self._parent._cast(_4788.HypoidGearMeshCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4792,
            )

            return self._parent._cast(
                _4792.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4795,
            )

            return self._parent._cast(
                _4795.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4798,
            )

            return self._parent._cast(
                _4798.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4806,
            )

            return self._parent._cast(
                _4806.PartToPartShearCouplingConnectionCompoundModalAnalysis
            )

        @property
        def ring_pins_to_disc_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4815,
            )

            return self._parent._cast(
                _4815.RingPinsToDiscConnectionCompoundModalAnalysis
            )

        @property
        def rolling_ring_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4818,
            )

            return self._parent._cast(_4818.RollingRingConnectionCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4825,
            )

            return self._parent._cast(_4825.SpiralBevelGearMeshCompoundModalAnalysis)

        @property
        def spring_damper_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4828,
            )

            return self._parent._cast(_4828.SpringDamperConnectionCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4831,
            )

            return self._parent._cast(
                _4831.StraightBevelDiffGearMeshCompoundModalAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4834,
            )

            return self._parent._cast(_4834.StraightBevelGearMeshCompoundModalAnalysis)

        @property
        def torque_converter_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4843,
            )

            return self._parent._cast(
                _4843.TorqueConverterConnectionCompoundModalAnalysis
            )

        @property
        def worm_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4849,
            )

            return self._parent._cast(_4849.WormGearMeshCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4852,
            )

            return self._parent._cast(_4852.ZerolBevelGearMeshCompoundModalAnalysis)

        @property
        def inter_mountable_component_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "InterMountableComponentConnectionCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
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
        instance_to_wrap: "InterMountableComponentConnectionCompoundModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4639.InterMountableComponentConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.InterMountableComponentConnectionModalAnalysis]

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
    ) -> "List[_4639.InterMountableComponentConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.InterMountableComponentConnectionModalAnalysis]

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
    ) -> "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis":
        return self._Cast_InterMountableComponentConnectionCompoundModalAnalysis(self)
