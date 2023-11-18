"""KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5146
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_MODAL_ANALYSIS_AT_A_SPEED = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
        "KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2316


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed"
)


class KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed(
    _5146.ConicalGearMeshModalAnalysisAtASpeed
):
    """KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed",
            parent: "KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5146.ConicalGearMeshModalAnalysisAtASpeed)

        @property
        def gear_mesh_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5172,
            )

            return self._parent._cast(_5172.GearMeshModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5179,
            )

            return self._parent._cast(
                _5179.InterMountableComponentConnectionModalAnalysisAtASpeed
            )

        @property
        def connection_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5149,
            )

            return self._parent._cast(_5149.ConnectionModalAnalysisAtASpeed)

        @property
        def connection_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5183,
            )

            return self._parent._cast(
                _5183.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5186,
            )

            return self._parent._cast(
                _5186.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed",
        ) -> "KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2316.KlingelnbergCycloPalloidConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh

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
    ) -> "KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed":
        return self._Cast_KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed(
            self
        )
