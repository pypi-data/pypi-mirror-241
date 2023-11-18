"""GearMaterialDatabase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.databases import _1826
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MATERIAL_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.Materials", "GearMaterialDatabase"
)

if TYPE_CHECKING:
    from mastapy.gears.materials import _592


__docformat__ = "restructuredtext en"
__all__ = ("GearMaterialDatabase",)


Self = TypeVar("Self", bound="GearMaterialDatabase")
T = TypeVar("T", bound="_592.GearMaterial")


class GearMaterialDatabase(_1826.NamedDatabase[T]):
    """GearMaterialDatabase

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _GEAR_MATERIAL_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMaterialDatabase")

    class _Cast_GearMaterialDatabase:
        """Special nested class for casting GearMaterialDatabase to subclasses."""

        def __init__(
            self: "GearMaterialDatabase._Cast_GearMaterialDatabase",
            parent: "GearMaterialDatabase",
        ):
            self._parent = parent

        @property
        def named_database(self: "GearMaterialDatabase._Cast_GearMaterialDatabase"):
            return self._parent._cast(_1826.NamedDatabase)

        @property
        def sql_database(self: "GearMaterialDatabase._Cast_GearMaterialDatabase"):
            pass

            from mastapy.utility.databases import _1829

            return self._parent._cast(_1829.SQLDatabase)

        @property
        def database(self: "GearMaterialDatabase._Cast_GearMaterialDatabase"):
            pass

            from mastapy.utility.databases import _1822

            return self._parent._cast(_1822.Database)

        @property
        def bevel_gear_material_database(
            self: "GearMaterialDatabase._Cast_GearMaterialDatabase",
        ):
            from mastapy.gears.materials import _586

            return self._parent._cast(_586.BevelGearMaterialDatabase)

        @property
        def klingelnberg_conical_gear_material_database(
            self: "GearMaterialDatabase._Cast_GearMaterialDatabase",
        ):
            from mastapy.gears.materials import _598

            return self._parent._cast(_598.KlingelnbergConicalGearMaterialDatabase)

        @property
        def gear_material_database(
            self: "GearMaterialDatabase._Cast_GearMaterialDatabase",
        ) -> "GearMaterialDatabase":
            return self._parent

        def __getattr__(
            self: "GearMaterialDatabase._Cast_GearMaterialDatabase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMaterialDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "GearMaterialDatabase._Cast_GearMaterialDatabase":
        return self._Cast_GearMaterialDatabase(self)
