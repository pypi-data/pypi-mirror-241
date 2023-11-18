"""GearMeshPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4097
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "GearMeshPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2311
    from mastapy.gears.rating import _358
    from mastapy.system_model.analyses_and_results.power_flows import _4151


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshPowerFlow",)


Self = TypeVar("Self", bound="GearMeshPowerFlow")


class GearMeshPowerFlow(_4097.InterMountableComponentConnectionPowerFlow):
    """GearMeshPowerFlow

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshPowerFlow")

    class _Cast_GearMeshPowerFlow:
        """Special nested class for casting GearMeshPowerFlow to subclasses."""

        def __init__(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
            parent: "GearMeshPowerFlow",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_power_flow(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
        ):
            return self._parent._cast(_4097.InterMountableComponentConnectionPowerFlow)

        @property
        def connection_power_flow(self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4065

            return self._parent._cast(_4065.ConnectionPowerFlow)

        @property
        def connection_static_load_analysis_case(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_power_flow(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4034

            return self._parent._cast(_4034.AGMAGleasonConicalGearMeshPowerFlow)

        @property
        def bevel_differential_gear_mesh_power_flow(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4041

            return self._parent._cast(_4041.BevelDifferentialGearMeshPowerFlow)

        @property
        def bevel_gear_mesh_power_flow(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4046

            return self._parent._cast(_4046.BevelGearMeshPowerFlow)

        @property
        def concept_gear_mesh_power_flow(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4059

            return self._parent._cast(_4059.ConceptGearMeshPowerFlow)

        @property
        def conical_gear_mesh_power_flow(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4062

            return self._parent._cast(_4062.ConicalGearMeshPowerFlow)

        @property
        def cylindrical_gear_mesh_power_flow(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4078

            return self._parent._cast(_4078.CylindricalGearMeshPowerFlow)

        @property
        def face_gear_mesh_power_flow(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4084

            return self._parent._cast(_4084.FaceGearMeshPowerFlow)

        @property
        def hypoid_gear_mesh_power_flow(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4094

            return self._parent._cast(_4094.HypoidGearMeshPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_power_flow(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4098

            return self._parent._cast(
                _4098.KlingelnbergCycloPalloidConicalGearMeshPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_power_flow(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4101

            return self._parent._cast(
                _4101.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_power_flow(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4104

            return self._parent._cast(
                _4104.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow
            )

        @property
        def spiral_bevel_gear_mesh_power_flow(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4133

            return self._parent._cast(_4133.SpiralBevelGearMeshPowerFlow)

        @property
        def straight_bevel_diff_gear_mesh_power_flow(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4139

            return self._parent._cast(_4139.StraightBevelDiffGearMeshPowerFlow)

        @property
        def straight_bevel_gear_mesh_power_flow(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4142

            return self._parent._cast(_4142.StraightBevelGearMeshPowerFlow)

        @property
        def worm_gear_mesh_power_flow(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4158

            return self._parent._cast(_4158.WormGearMeshPowerFlow)

        @property
        def zerol_bevel_gear_mesh_power_flow(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4161

            return self._parent._cast(_4161.ZerolBevelGearMeshPowerFlow)

        @property
        def gear_mesh_power_flow(
            self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow",
        ) -> "GearMeshPowerFlow":
            return self._parent

        def __getattr__(self: "GearMeshPowerFlow._Cast_GearMeshPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_a_tooth_passing_speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearAToothPassingSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_b_tooth_passing_speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearBToothPassingSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_passing_frequency(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothPassingFrequency

        if temp is None:
            return 0.0

        return temp

    @property
    def connection_design(self: Self) -> "_2311.GearMesh":
        """mastapy.system_model.connections_and_sockets.gears.GearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating(self: Self) -> "_358.GearMeshRating":
        """mastapy.gears.rating.GearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def tooth_passing_harmonics(self: Self) -> "List[_4151.ToothPassingHarmonic]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ToothPassingHarmonic]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothPassingHarmonics

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "GearMeshPowerFlow._Cast_GearMeshPowerFlow":
        return self._Cast_GearMeshPowerFlow(self)
