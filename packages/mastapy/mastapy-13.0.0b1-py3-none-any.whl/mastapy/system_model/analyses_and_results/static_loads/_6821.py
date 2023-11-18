"""BevelDifferentialGearMeshLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6826
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "BevelDifferentialGearMeshLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2299


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearMeshLoadCase",)


Self = TypeVar("Self", bound="BevelDifferentialGearMeshLoadCase")


class BevelDifferentialGearMeshLoadCase(_6826.BevelGearMeshLoadCase):
    """BevelDifferentialGearMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_MESH_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelDifferentialGearMeshLoadCase")

    class _Cast_BevelDifferentialGearMeshLoadCase:
        """Special nested class for casting BevelDifferentialGearMeshLoadCase to subclasses."""

        def __init__(
            self: "BevelDifferentialGearMeshLoadCase._Cast_BevelDifferentialGearMeshLoadCase",
            parent: "BevelDifferentialGearMeshLoadCase",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_load_case(
            self: "BevelDifferentialGearMeshLoadCase._Cast_BevelDifferentialGearMeshLoadCase",
        ):
            return self._parent._cast(_6826.BevelGearMeshLoadCase)

        @property
        def agma_gleason_conical_gear_mesh_load_case(
            self: "BevelDifferentialGearMeshLoadCase._Cast_BevelDifferentialGearMeshLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6812

            return self._parent._cast(_6812.AGMAGleasonConicalGearMeshLoadCase)

        @property
        def conical_gear_mesh_load_case(
            self: "BevelDifferentialGearMeshLoadCase._Cast_BevelDifferentialGearMeshLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6844

            return self._parent._cast(_6844.ConicalGearMeshLoadCase)

        @property
        def gear_mesh_load_case(
            self: "BevelDifferentialGearMeshLoadCase._Cast_BevelDifferentialGearMeshLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6890

            return self._parent._cast(_6890.GearMeshLoadCase)

        @property
        def inter_mountable_component_connection_load_case(
            self: "BevelDifferentialGearMeshLoadCase._Cast_BevelDifferentialGearMeshLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6909

            return self._parent._cast(_6909.InterMountableComponentConnectionLoadCase)

        @property
        def connection_load_case(
            self: "BevelDifferentialGearMeshLoadCase._Cast_BevelDifferentialGearMeshLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6847

            return self._parent._cast(_6847.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "BevelDifferentialGearMeshLoadCase._Cast_BevelDifferentialGearMeshLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearMeshLoadCase._Cast_BevelDifferentialGearMeshLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearMeshLoadCase._Cast_BevelDifferentialGearMeshLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_load_case(
            self: "BevelDifferentialGearMeshLoadCase._Cast_BevelDifferentialGearMeshLoadCase",
        ) -> "BevelDifferentialGearMeshLoadCase":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearMeshLoadCase._Cast_BevelDifferentialGearMeshLoadCase",
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
        self: Self, instance_to_wrap: "BevelDifferentialGearMeshLoadCase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2299.BevelDifferentialGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh

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
    ) -> "BevelDifferentialGearMeshLoadCase._Cast_BevelDifferentialGearMeshLoadCase":
        return self._Cast_BevelDifferentialGearMeshLoadCase(self)
