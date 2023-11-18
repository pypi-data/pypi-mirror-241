"""ConicalGearMeshPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4090
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "ConicalGearMeshPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2305


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshPowerFlow",)


Self = TypeVar("Self", bound="ConicalGearMeshPowerFlow")


class ConicalGearMeshPowerFlow(_4090.GearMeshPowerFlow):
    """ConicalGearMeshPowerFlow

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearMeshPowerFlow")

    class _Cast_ConicalGearMeshPowerFlow:
        """Special nested class for casting ConicalGearMeshPowerFlow to subclasses."""

        def __init__(
            self: "ConicalGearMeshPowerFlow._Cast_ConicalGearMeshPowerFlow",
            parent: "ConicalGearMeshPowerFlow",
        ):
            self._parent = parent

        @property
        def gear_mesh_power_flow(
            self: "ConicalGearMeshPowerFlow._Cast_ConicalGearMeshPowerFlow",
        ):
            return self._parent._cast(_4090.GearMeshPowerFlow)

        @property
        def inter_mountable_component_connection_power_flow(
            self: "ConicalGearMeshPowerFlow._Cast_ConicalGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4097

            return self._parent._cast(_4097.InterMountableComponentConnectionPowerFlow)

        @property
        def connection_power_flow(
            self: "ConicalGearMeshPowerFlow._Cast_ConicalGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4065

            return self._parent._cast(_4065.ConnectionPowerFlow)

        @property
        def connection_static_load_analysis_case(
            self: "ConicalGearMeshPowerFlow._Cast_ConicalGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConicalGearMeshPowerFlow._Cast_ConicalGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConicalGearMeshPowerFlow._Cast_ConicalGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearMeshPowerFlow._Cast_ConicalGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearMeshPowerFlow._Cast_ConicalGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_power_flow(
            self: "ConicalGearMeshPowerFlow._Cast_ConicalGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4034

            return self._parent._cast(_4034.AGMAGleasonConicalGearMeshPowerFlow)

        @property
        def bevel_differential_gear_mesh_power_flow(
            self: "ConicalGearMeshPowerFlow._Cast_ConicalGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4041

            return self._parent._cast(_4041.BevelDifferentialGearMeshPowerFlow)

        @property
        def bevel_gear_mesh_power_flow(
            self: "ConicalGearMeshPowerFlow._Cast_ConicalGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4046

            return self._parent._cast(_4046.BevelGearMeshPowerFlow)

        @property
        def hypoid_gear_mesh_power_flow(
            self: "ConicalGearMeshPowerFlow._Cast_ConicalGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4094

            return self._parent._cast(_4094.HypoidGearMeshPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_power_flow(
            self: "ConicalGearMeshPowerFlow._Cast_ConicalGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4098

            return self._parent._cast(
                _4098.KlingelnbergCycloPalloidConicalGearMeshPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_power_flow(
            self: "ConicalGearMeshPowerFlow._Cast_ConicalGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4101

            return self._parent._cast(
                _4101.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_power_flow(
            self: "ConicalGearMeshPowerFlow._Cast_ConicalGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4104

            return self._parent._cast(
                _4104.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow
            )

        @property
        def spiral_bevel_gear_mesh_power_flow(
            self: "ConicalGearMeshPowerFlow._Cast_ConicalGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4133

            return self._parent._cast(_4133.SpiralBevelGearMeshPowerFlow)

        @property
        def straight_bevel_diff_gear_mesh_power_flow(
            self: "ConicalGearMeshPowerFlow._Cast_ConicalGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4139

            return self._parent._cast(_4139.StraightBevelDiffGearMeshPowerFlow)

        @property
        def straight_bevel_gear_mesh_power_flow(
            self: "ConicalGearMeshPowerFlow._Cast_ConicalGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4142

            return self._parent._cast(_4142.StraightBevelGearMeshPowerFlow)

        @property
        def zerol_bevel_gear_mesh_power_flow(
            self: "ConicalGearMeshPowerFlow._Cast_ConicalGearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4161

            return self._parent._cast(_4161.ZerolBevelGearMeshPowerFlow)

        @property
        def conical_gear_mesh_power_flow(
            self: "ConicalGearMeshPowerFlow._Cast_ConicalGearMeshPowerFlow",
        ) -> "ConicalGearMeshPowerFlow":
            return self._parent

        def __getattr__(
            self: "ConicalGearMeshPowerFlow._Cast_ConicalGearMeshPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearMeshPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2305.ConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh

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
    ) -> "ConicalGearMeshPowerFlow._Cast_ConicalGearMeshPowerFlow":
        return self._Cast_ConicalGearMeshPowerFlow(self)
