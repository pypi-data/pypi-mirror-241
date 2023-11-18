"""KlingelnbergCycloPalloidHypoidGearMesh"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets.gears import _2316
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears",
    "KlingelnbergCycloPalloidHypoidGearMesh",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.klingelnberg_hypoid import _976


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearMesh",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearMesh")


class KlingelnbergCycloPalloidHypoidGearMesh(
    _2316.KlingelnbergCycloPalloidConicalGearMesh
):
    """KlingelnbergCycloPalloidHypoidGearMesh

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidHypoidGearMesh"
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearMesh:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearMesh to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearMesh._Cast_KlingelnbergCycloPalloidHypoidGearMesh",
            parent: "KlingelnbergCycloPalloidHypoidGearMesh",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh(
            self: "KlingelnbergCycloPalloidHypoidGearMesh._Cast_KlingelnbergCycloPalloidHypoidGearMesh",
        ):
            return self._parent._cast(_2316.KlingelnbergCycloPalloidConicalGearMesh)

        @property
        def conical_gear_mesh(
            self: "KlingelnbergCycloPalloidHypoidGearMesh._Cast_KlingelnbergCycloPalloidHypoidGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2305

            return self._parent._cast(_2305.ConicalGearMesh)

        @property
        def gear_mesh(
            self: "KlingelnbergCycloPalloidHypoidGearMesh._Cast_KlingelnbergCycloPalloidHypoidGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2311

            return self._parent._cast(_2311.GearMesh)

        @property
        def inter_mountable_component_connection(
            self: "KlingelnbergCycloPalloidHypoidGearMesh._Cast_KlingelnbergCycloPalloidHypoidGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets import _2279

            return self._parent._cast(_2279.InterMountableComponentConnection)

        @property
        def connection(
            self: "KlingelnbergCycloPalloidHypoidGearMesh._Cast_KlingelnbergCycloPalloidHypoidGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets import _2270

            return self._parent._cast(_2270.Connection)

        @property
        def design_entity(
            self: "KlingelnbergCycloPalloidHypoidGearMesh._Cast_KlingelnbergCycloPalloidHypoidGearMesh",
        ):
            from mastapy.system_model import _2201

            return self._parent._cast(_2201.DesignEntity)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh(
            self: "KlingelnbergCycloPalloidHypoidGearMesh._Cast_KlingelnbergCycloPalloidHypoidGearMesh",
        ) -> "KlingelnbergCycloPalloidHypoidGearMesh":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearMesh._Cast_KlingelnbergCycloPalloidHypoidGearMesh",
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
        self: Self, instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearMesh.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_gear_mesh_design(
        self: Self,
    ) -> "_976.KlingelnbergCycloPalloidHypoidGearMeshDesign":
        """mastapy.gears.gear_designs.klingelnberg_hypoid.KlingelnbergCycloPalloidHypoidGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_mesh_design(
        self: Self,
    ) -> "_976.KlingelnbergCycloPalloidHypoidGearMeshDesign":
        """mastapy.gears.gear_designs.klingelnberg_hypoid.KlingelnbergCycloPalloidHypoidGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearMesh._Cast_KlingelnbergCycloPalloidHypoidGearMesh":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearMesh(self)
