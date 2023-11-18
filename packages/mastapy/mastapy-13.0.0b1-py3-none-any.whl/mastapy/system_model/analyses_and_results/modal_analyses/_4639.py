"""InterMountableComponentConnectionModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4604
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "InterMountableComponentConnectionModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2279
    from mastapy.system_model.analyses_and_results.system_deflections import _2765


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionModalAnalysis",)


Self = TypeVar("Self", bound="InterMountableComponentConnectionModalAnalysis")


class InterMountableComponentConnectionModalAnalysis(_4604.ConnectionModalAnalysis):
    """InterMountableComponentConnectionModalAnalysis

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_InterMountableComponentConnectionModalAnalysis"
    )

    class _Cast_InterMountableComponentConnectionModalAnalysis:
        """Special nested class for casting InterMountableComponentConnectionModalAnalysis to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
            parent: "InterMountableComponentConnectionModalAnalysis",
        ):
            self._parent = parent

        @property
        def connection_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            return self._parent._cast(_4604.ConnectionModalAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4573

            return self._parent._cast(_4573.AGMAGleasonConicalGearMeshModalAnalysis)

        @property
        def belt_connection_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4578

            return self._parent._cast(_4578.BeltConnectionModalAnalysis)

        @property
        def bevel_differential_gear_mesh_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4580

            return self._parent._cast(_4580.BevelDifferentialGearMeshModalAnalysis)

        @property
        def bevel_gear_mesh_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4585

            return self._parent._cast(_4585.BevelGearMeshModalAnalysis)

        @property
        def clutch_connection_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4590

            return self._parent._cast(_4590.ClutchConnectionModalAnalysis)

        @property
        def concept_coupling_connection_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4595

            return self._parent._cast(_4595.ConceptCouplingConnectionModalAnalysis)

        @property
        def concept_gear_mesh_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4598

            return self._parent._cast(_4598.ConceptGearMeshModalAnalysis)

        @property
        def conical_gear_mesh_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4601

            return self._parent._cast(_4601.ConicalGearMeshModalAnalysis)

        @property
        def coupling_connection_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4607

            return self._parent._cast(_4607.CouplingConnectionModalAnalysis)

        @property
        def cvt_belt_connection_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4610

            return self._parent._cast(_4610.CVTBeltConnectionModalAnalysis)

        @property
        def cylindrical_gear_mesh_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4617

            return self._parent._cast(_4617.CylindricalGearMeshModalAnalysis)

        @property
        def face_gear_mesh_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4626

            return self._parent._cast(_4626.FaceGearMeshModalAnalysis)

        @property
        def gear_mesh_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4632

            return self._parent._cast(_4632.GearMeshModalAnalysis)

        @property
        def hypoid_gear_mesh_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4636

            return self._parent._cast(_4636.HypoidGearMeshModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4640

            return self._parent._cast(
                _4640.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4643

            return self._parent._cast(
                _4643.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4646

            return self._parent._cast(
                _4646.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4660

            return self._parent._cast(
                _4660.PartToPartShearCouplingConnectionModalAnalysis
            )

        @property
        def ring_pins_to_disc_connection_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4670

            return self._parent._cast(_4670.RingPinsToDiscConnectionModalAnalysis)

        @property
        def rolling_ring_connection_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4672

            return self._parent._cast(_4672.RollingRingConnectionModalAnalysis)

        @property
        def spiral_bevel_gear_mesh_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4680

            return self._parent._cast(_4680.SpiralBevelGearMeshModalAnalysis)

        @property
        def spring_damper_connection_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4683

            return self._parent._cast(_4683.SpringDamperConnectionModalAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4686

            return self._parent._cast(_4686.StraightBevelDiffGearMeshModalAnalysis)

        @property
        def straight_bevel_gear_mesh_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4689

            return self._parent._cast(_4689.StraightBevelGearMeshModalAnalysis)

        @property
        def torque_converter_connection_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4698

            return self._parent._cast(_4698.TorqueConverterConnectionModalAnalysis)

        @property
        def worm_gear_mesh_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4707

            return self._parent._cast(_4707.WormGearMeshModalAnalysis)

        @property
        def zerol_bevel_gear_mesh_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4710

            return self._parent._cast(_4710.ZerolBevelGearMeshModalAnalysis)

        @property
        def inter_mountable_component_connection_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ) -> "InterMountableComponentConnectionModalAnalysis":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
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
        instance_to_wrap: "InterMountableComponentConnectionModalAnalysis.TYPE",
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
    def system_deflection_results(
        self: Self,
    ) -> "_2765.InterMountableComponentConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.InterMountableComponentConnectionSystemDeflection

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
    ) -> "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis":
        return self._Cast_InterMountableComponentConnectionModalAnalysis(self)
