"""Quaternion"""
from __future__ import annotations

from typing import TypeVar

from mastapy.math_utility import _1523
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_QUATERNION = python_net_import("SMT.MastaAPI.MathUtility", "Quaternion")


__docformat__ = "restructuredtext en"
__all__ = ("Quaternion",)


Self = TypeVar("Self", bound="Quaternion")


class Quaternion(_1523.RealVector):
    """Quaternion

    This is a mastapy class.
    """

    TYPE = _QUATERNION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Quaternion")

    class _Cast_Quaternion:
        """Special nested class for casting Quaternion to subclasses."""

        def __init__(self: "Quaternion._Cast_Quaternion", parent: "Quaternion"):
            self._parent = parent

        @property
        def real_vector(self: "Quaternion._Cast_Quaternion"):
            return self._parent._cast(_1523.RealVector)

        @property
        def real_matrix(self: "Quaternion._Cast_Quaternion"):
            from mastapy.math_utility import _1522

            return self._parent._cast(_1522.RealMatrix)

        @property
        def generic_matrix(self: "Quaternion._Cast_Quaternion"):
            pass

            from mastapy.math_utility import _1511

            return self._parent._cast(_1511.GenericMatrix)

        @property
        def quaternion(self: "Quaternion._Cast_Quaternion") -> "Quaternion":
            return self._parent

        def __getattr__(self: "Quaternion._Cast_Quaternion", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Quaternion.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "Quaternion._Cast_Quaternion":
        return self._Cast_Quaternion(self)
