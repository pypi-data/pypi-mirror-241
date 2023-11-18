"""InterMountableComponentConnectionModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4889,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "InterMountableComponentConnectionModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2279


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionModalAnalysisAtAStiffness",)


Self = TypeVar(
    "Self", bound="InterMountableComponentConnectionModalAnalysisAtAStiffness"
)


class InterMountableComponentConnectionModalAnalysisAtAStiffness(
    _4889.ConnectionModalAnalysisAtAStiffness
):
    """InterMountableComponentConnectionModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
    )

    class _Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness:
        """Special nested class for casting InterMountableComponentConnectionModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
            parent: "InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def connection_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(_4889.ConnectionModalAnalysisAtAStiffness)

        @property
        def connection_static_load_analysis_case(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4858,
            )

            return self._parent._cast(
                _4858.AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness
            )

        @property
        def belt_connection_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4863,
            )

            return self._parent._cast(_4863.BeltConnectionModalAnalysisAtAStiffness)

        @property
        def bevel_differential_gear_mesh_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4865,
            )

            return self._parent._cast(
                _4865.BevelDifferentialGearMeshModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4870,
            )

            return self._parent._cast(_4870.BevelGearMeshModalAnalysisAtAStiffness)

        @property
        def clutch_connection_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4875,
            )

            return self._parent._cast(_4875.ClutchConnectionModalAnalysisAtAStiffness)

        @property
        def concept_coupling_connection_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4880,
            )

            return self._parent._cast(
                _4880.ConceptCouplingConnectionModalAnalysisAtAStiffness
            )

        @property
        def concept_gear_mesh_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4883,
            )

            return self._parent._cast(_4883.ConceptGearMeshModalAnalysisAtAStiffness)

        @property
        def conical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4886,
            )

            return self._parent._cast(_4886.ConicalGearMeshModalAnalysisAtAStiffness)

        @property
        def coupling_connection_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4891,
            )

            return self._parent._cast(_4891.CouplingConnectionModalAnalysisAtAStiffness)

        @property
        def cvt_belt_connection_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4894,
            )

            return self._parent._cast(_4894.CVTBeltConnectionModalAnalysisAtAStiffness)

        @property
        def cylindrical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4901,
            )

            return self._parent._cast(
                _4901.CylindricalGearMeshModalAnalysisAtAStiffness
            )

        @property
        def face_gear_mesh_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4908,
            )

            return self._parent._cast(_4908.FaceGearMeshModalAnalysisAtAStiffness)

        @property
        def gear_mesh_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4913,
            )

            return self._parent._cast(_4913.GearMeshModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_mesh_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4917,
            )

            return self._parent._cast(_4917.HypoidGearMeshModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4921,
            )

            return self._parent._cast(
                _4921.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4924,
            )

            return self._parent._cast(
                _4924.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4927,
            )

            return self._parent._cast(
                _4927.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtAStiffness
            )

        @property
        def part_to_part_shear_coupling_connection_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4936,
            )

            return self._parent._cast(
                _4936.PartToPartShearCouplingConnectionModalAnalysisAtAStiffness
            )

        @property
        def ring_pins_to_disc_connection_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4946,
            )

            return self._parent._cast(
                _4946.RingPinsToDiscConnectionModalAnalysisAtAStiffness
            )

        @property
        def rolling_ring_connection_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4948,
            )

            return self._parent._cast(
                _4948.RollingRingConnectionModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4955,
            )

            return self._parent._cast(
                _4955.SpiralBevelGearMeshModalAnalysisAtAStiffness
            )

        @property
        def spring_damper_connection_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4958,
            )

            return self._parent._cast(
                _4958.SpringDamperConnectionModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4961,
            )

            return self._parent._cast(
                _4961.StraightBevelDiffGearMeshModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4964,
            )

            return self._parent._cast(
                _4964.StraightBevelGearMeshModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_connection_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4973,
            )

            return self._parent._cast(
                _4973.TorqueConverterConnectionModalAnalysisAtAStiffness
            )

        @property
        def worm_gear_mesh_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4979,
            )

            return self._parent._cast(_4979.WormGearMeshModalAnalysisAtAStiffness)

        @property
        def zerol_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4982,
            )

            return self._parent._cast(_4982.ZerolBevelGearMeshModalAnalysisAtAStiffness)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
        ) -> "InterMountableComponentConnectionModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness",
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
        instance_to_wrap: "InterMountableComponentConnectionModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2279.InterMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.InterMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "InterMountableComponentConnectionModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness":
        return self._Cast_InterMountableComponentConnectionModalAnalysisAtAStiffness(
            self
        )
