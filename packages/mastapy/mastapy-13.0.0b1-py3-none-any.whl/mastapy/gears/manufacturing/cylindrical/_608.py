"""CylindricalCutterDatabase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.databases import _1826
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_CUTTER_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical", "CylindricalCutterDatabase"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.cutters import _711


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalCutterDatabase",)


Self = TypeVar("Self", bound="CylindricalCutterDatabase")
T = TypeVar("T", bound="_711.CylindricalGearRealCutterDesign")


class CylindricalCutterDatabase(_1826.NamedDatabase[T]):
    """CylindricalCutterDatabase

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _CYLINDRICAL_CUTTER_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalCutterDatabase")

    class _Cast_CylindricalCutterDatabase:
        """Special nested class for casting CylindricalCutterDatabase to subclasses."""

        def __init__(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
            parent: "CylindricalCutterDatabase",
        ):
            self._parent = parent

        @property
        def named_database(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
        ):
            return self._parent._cast(_1826.NamedDatabase)

        @property
        def sql_database(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
        ):
            pass

            from mastapy.utility.databases import _1829

            return self._parent._cast(_1829.SQLDatabase)

        @property
        def database(self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase"):
            pass

            from mastapy.utility.databases import _1822

            return self._parent._cast(_1822.Database)

        @property
        def cylindrical_hob_database(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
        ):
            from mastapy.gears.manufacturing.cylindrical import _613

            return self._parent._cast(_613.CylindricalHobDatabase)

        @property
        def cylindrical_shaper_database(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
        ):
            from mastapy.gears.manufacturing.cylindrical import _624

            return self._parent._cast(_624.CylindricalShaperDatabase)

        @property
        def cylindrical_formed_wheel_grinder_database(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
        ):
            from mastapy.gears.manufacturing.cylindrical.cutters import _703

            return self._parent._cast(_703.CylindricalFormedWheelGrinderDatabase)

        @property
        def cylindrical_gear_plunge_shaver_database(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
        ):
            from mastapy.gears.manufacturing.cylindrical.cutters import _709

            return self._parent._cast(_709.CylindricalGearPlungeShaverDatabase)

        @property
        def cylindrical_gear_shaver_database(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
        ):
            from mastapy.gears.manufacturing.cylindrical.cutters import _714

            return self._parent._cast(_714.CylindricalGearShaverDatabase)

        @property
        def cylindrical_worm_grinder_database(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
        ):
            from mastapy.gears.manufacturing.cylindrical.cutters import _715

            return self._parent._cast(_715.CylindricalWormGrinderDatabase)

        @property
        def cylindrical_cutter_database(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase",
        ) -> "CylindricalCutterDatabase":
            return self._parent

        def __getattr__(
            self: "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalCutterDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalCutterDatabase._Cast_CylindricalCutterDatabase":
        return self._Cast_CylindricalCutterDatabase(self)
