"""AGMAGleasonConicalGearMeshLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6844
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "AGMAGleasonConicalGearMeshLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2297


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshLoadCase",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearMeshLoadCase")


class AGMAGleasonConicalGearMeshLoadCase(_6844.ConicalGearMeshLoadCase):
    """AGMAGleasonConicalGearMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalGearMeshLoadCase")

    class _Cast_AGMAGleasonConicalGearMeshLoadCase:
        """Special nested class for casting AGMAGleasonConicalGearMeshLoadCase to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshLoadCase._Cast_AGMAGleasonConicalGearMeshLoadCase",
            parent: "AGMAGleasonConicalGearMeshLoadCase",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_load_case(
            self: "AGMAGleasonConicalGearMeshLoadCase._Cast_AGMAGleasonConicalGearMeshLoadCase",
        ):
            return self._parent._cast(_6844.ConicalGearMeshLoadCase)

        @property
        def gear_mesh_load_case(
            self: "AGMAGleasonConicalGearMeshLoadCase._Cast_AGMAGleasonConicalGearMeshLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6890

            return self._parent._cast(_6890.GearMeshLoadCase)

        @property
        def inter_mountable_component_connection_load_case(
            self: "AGMAGleasonConicalGearMeshLoadCase._Cast_AGMAGleasonConicalGearMeshLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6909

            return self._parent._cast(_6909.InterMountableComponentConnectionLoadCase)

        @property
        def connection_load_case(
            self: "AGMAGleasonConicalGearMeshLoadCase._Cast_AGMAGleasonConicalGearMeshLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6847

            return self._parent._cast(_6847.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "AGMAGleasonConicalGearMeshLoadCase._Cast_AGMAGleasonConicalGearMeshLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearMeshLoadCase._Cast_AGMAGleasonConicalGearMeshLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshLoadCase._Cast_AGMAGleasonConicalGearMeshLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_load_case(
            self: "AGMAGleasonConicalGearMeshLoadCase._Cast_AGMAGleasonConicalGearMeshLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6821

            return self._parent._cast(_6821.BevelDifferentialGearMeshLoadCase)

        @property
        def bevel_gear_mesh_load_case(
            self: "AGMAGleasonConicalGearMeshLoadCase._Cast_AGMAGleasonConicalGearMeshLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6826

            return self._parent._cast(_6826.BevelGearMeshLoadCase)

        @property
        def hypoid_gear_mesh_load_case(
            self: "AGMAGleasonConicalGearMeshLoadCase._Cast_AGMAGleasonConicalGearMeshLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6904

            return self._parent._cast(_6904.HypoidGearMeshLoadCase)

        @property
        def spiral_bevel_gear_mesh_load_case(
            self: "AGMAGleasonConicalGearMeshLoadCase._Cast_AGMAGleasonConicalGearMeshLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6952

            return self._parent._cast(_6952.SpiralBevelGearMeshLoadCase)

        @property
        def straight_bevel_diff_gear_mesh_load_case(
            self: "AGMAGleasonConicalGearMeshLoadCase._Cast_AGMAGleasonConicalGearMeshLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6958

            return self._parent._cast(_6958.StraightBevelDiffGearMeshLoadCase)

        @property
        def straight_bevel_gear_mesh_load_case(
            self: "AGMAGleasonConicalGearMeshLoadCase._Cast_AGMAGleasonConicalGearMeshLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6961

            return self._parent._cast(_6961.StraightBevelGearMeshLoadCase)

        @property
        def zerol_bevel_gear_mesh_load_case(
            self: "AGMAGleasonConicalGearMeshLoadCase._Cast_AGMAGleasonConicalGearMeshLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6984

            return self._parent._cast(_6984.ZerolBevelGearMeshLoadCase)

        @property
        def agma_gleason_conical_gear_mesh_load_case(
            self: "AGMAGleasonConicalGearMeshLoadCase._Cast_AGMAGleasonConicalGearMeshLoadCase",
        ) -> "AGMAGleasonConicalGearMeshLoadCase":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshLoadCase._Cast_AGMAGleasonConicalGearMeshLoadCase",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearMeshLoadCase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2297.AGMAGleasonConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh

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
    ) -> "AGMAGleasonConicalGearMeshLoadCase._Cast_AGMAGleasonConicalGearMeshLoadCase":
        return self._Cast_AGMAGleasonConicalGearMeshLoadCase(self)
