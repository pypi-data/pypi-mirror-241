"""MountableComponentInnerSocket"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.connections_and_sockets import _2282
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_INNER_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "MountableComponentInnerSocket"
)


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentInnerSocket",)


Self = TypeVar("Self", bound="MountableComponentInnerSocket")


class MountableComponentInnerSocket(_2282.MountableComponentSocket):
    """MountableComponentInnerSocket

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_INNER_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MountableComponentInnerSocket")

    class _Cast_MountableComponentInnerSocket:
        """Special nested class for casting MountableComponentInnerSocket to subclasses."""

        def __init__(
            self: "MountableComponentInnerSocket._Cast_MountableComponentInnerSocket",
            parent: "MountableComponentInnerSocket",
        ):
            self._parent = parent

        @property
        def mountable_component_socket(
            self: "MountableComponentInnerSocket._Cast_MountableComponentInnerSocket",
        ):
            return self._parent._cast(_2282.MountableComponentSocket)

        @property
        def cylindrical_socket(
            self: "MountableComponentInnerSocket._Cast_MountableComponentInnerSocket",
        ):
            from mastapy.system_model.connections_and_sockets import _2274

            return self._parent._cast(_2274.CylindricalSocket)

        @property
        def socket(
            self: "MountableComponentInnerSocket._Cast_MountableComponentInnerSocket",
        ):
            from mastapy.system_model.connections_and_sockets import _2294

            return self._parent._cast(_2294.Socket)

        @property
        def bearing_inner_socket(
            self: "MountableComponentInnerSocket._Cast_MountableComponentInnerSocket",
        ):
            from mastapy.system_model.connections_and_sockets import _2264

            return self._parent._cast(_2264.BearingInnerSocket)

        @property
        def mountable_component_inner_socket(
            self: "MountableComponentInnerSocket._Cast_MountableComponentInnerSocket",
        ) -> "MountableComponentInnerSocket":
            return self._parent

        def __getattr__(
            self: "MountableComponentInnerSocket._Cast_MountableComponentInnerSocket",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MountableComponentInnerSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "MountableComponentInnerSocket._Cast_MountableComponentInnerSocket":
        return self._Cast_MountableComponentInnerSocket(self)
