"""CylindricalShaperDatabase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.manufacturing.cylindrical import _608
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_SHAPER_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical", "CylindricalShaperDatabase"
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalShaperDatabase",)


Self = TypeVar("Self", bound="CylindricalShaperDatabase")


class CylindricalShaperDatabase(
    _608.CylindricalCutterDatabase["_712.CylindricalGearShaper"]
):
    """CylindricalShaperDatabase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_SHAPER_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalShaperDatabase")

    class _Cast_CylindricalShaperDatabase:
        """Special nested class for casting CylindricalShaperDatabase to subclasses."""

        def __init__(
            self: "CylindricalShaperDatabase._Cast_CylindricalShaperDatabase",
            parent: "CylindricalShaperDatabase",
        ):
            self._parent = parent

        @property
        def cylindrical_cutter_database(
            self: "CylindricalShaperDatabase._Cast_CylindricalShaperDatabase",
        ):
            return self._parent._cast(_608.CylindricalCutterDatabase)

        @property
        def named_database(
            self: "CylindricalShaperDatabase._Cast_CylindricalShaperDatabase",
        ):
            from mastapy.utility.databases import _1826

            return self._parent._cast(_1826.NamedDatabase)

        @property
        def sql_database(
            self: "CylindricalShaperDatabase._Cast_CylindricalShaperDatabase",
        ):
            pass

            from mastapy.utility.databases import _1829

            return self._parent._cast(_1829.SQLDatabase)

        @property
        def database(self: "CylindricalShaperDatabase._Cast_CylindricalShaperDatabase"):
            pass

            from mastapy.utility.databases import _1822

            return self._parent._cast(_1822.Database)

        @property
        def cylindrical_shaper_database(
            self: "CylindricalShaperDatabase._Cast_CylindricalShaperDatabase",
        ) -> "CylindricalShaperDatabase":
            return self._parent

        def __getattr__(
            self: "CylindricalShaperDatabase._Cast_CylindricalShaperDatabase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalShaperDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalShaperDatabase._Cast_CylindricalShaperDatabase":
        return self._Cast_CylindricalShaperDatabase(self)
