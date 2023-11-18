"""KlingelnbergCycloPalloidConicalGearMesh"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.connections_and_sockets.gears import _2305
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears",
    "KlingelnbergCycloPalloidConicalGearMesh",
)


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearMesh",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearMesh")


class KlingelnbergCycloPalloidConicalGearMesh(_2305.ConicalGearMesh):
    """KlingelnbergCycloPalloidConicalGearMesh

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidConicalGearMesh"
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearMesh:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearMesh to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearMesh._Cast_KlingelnbergCycloPalloidConicalGearMesh",
            parent: "KlingelnbergCycloPalloidConicalGearMesh",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh(
            self: "KlingelnbergCycloPalloidConicalGearMesh._Cast_KlingelnbergCycloPalloidConicalGearMesh",
        ):
            return self._parent._cast(_2305.ConicalGearMesh)

        @property
        def gear_mesh(
            self: "KlingelnbergCycloPalloidConicalGearMesh._Cast_KlingelnbergCycloPalloidConicalGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2311

            return self._parent._cast(_2311.GearMesh)

        @property
        def inter_mountable_component_connection(
            self: "KlingelnbergCycloPalloidConicalGearMesh._Cast_KlingelnbergCycloPalloidConicalGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets import _2279

            return self._parent._cast(_2279.InterMountableComponentConnection)

        @property
        def connection(
            self: "KlingelnbergCycloPalloidConicalGearMesh._Cast_KlingelnbergCycloPalloidConicalGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets import _2270

            return self._parent._cast(_2270.Connection)

        @property
        def design_entity(
            self: "KlingelnbergCycloPalloidConicalGearMesh._Cast_KlingelnbergCycloPalloidConicalGearMesh",
        ):
            from mastapy.system_model import _2201

            return self._parent._cast(_2201.DesignEntity)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh(
            self: "KlingelnbergCycloPalloidConicalGearMesh._Cast_KlingelnbergCycloPalloidConicalGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2317

            return self._parent._cast(_2317.KlingelnbergCycloPalloidHypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(
            self: "KlingelnbergCycloPalloidConicalGearMesh._Cast_KlingelnbergCycloPalloidConicalGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2318

            return self._parent._cast(_2318.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh(
            self: "KlingelnbergCycloPalloidConicalGearMesh._Cast_KlingelnbergCycloPalloidConicalGearMesh",
        ) -> "KlingelnbergCycloPalloidConicalGearMesh":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearMesh._Cast_KlingelnbergCycloPalloidConicalGearMesh",
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
        self: Self, instance_to_wrap: "KlingelnbergCycloPalloidConicalGearMesh.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearMesh._Cast_KlingelnbergCycloPalloidConicalGearMesh":
        return self._Cast_KlingelnbergCycloPalloidConicalGearMesh(self)
