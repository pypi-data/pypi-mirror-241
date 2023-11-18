"""CylindricalGearPlasticMaterialDatabase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.materials import _590
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_PLASTIC_MATERIAL_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.Materials", "CylindricalGearPlasticMaterialDatabase"
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearPlasticMaterialDatabase",)


Self = TypeVar("Self", bound="CylindricalGearPlasticMaterialDatabase")


class CylindricalGearPlasticMaterialDatabase(
    _590.CylindricalGearMaterialDatabase["_601.PlasticCylindricalGearMaterial"]
):
    """CylindricalGearPlasticMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_PLASTIC_MATERIAL_DATABASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearPlasticMaterialDatabase"
    )

    class _Cast_CylindricalGearPlasticMaterialDatabase:
        """Special nested class for casting CylindricalGearPlasticMaterialDatabase to subclasses."""

        def __init__(
            self: "CylindricalGearPlasticMaterialDatabase._Cast_CylindricalGearPlasticMaterialDatabase",
            parent: "CylindricalGearPlasticMaterialDatabase",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_material_database(
            self: "CylindricalGearPlasticMaterialDatabase._Cast_CylindricalGearPlasticMaterialDatabase",
        ):
            return self._parent._cast(_590.CylindricalGearMaterialDatabase)

        @property
        def material_database(
            self: "CylindricalGearPlasticMaterialDatabase._Cast_CylindricalGearPlasticMaterialDatabase",
        ):
            from mastapy.materials import _268

            return self._parent._cast(_268.MaterialDatabase)

        @property
        def named_database(
            self: "CylindricalGearPlasticMaterialDatabase._Cast_CylindricalGearPlasticMaterialDatabase",
        ):
            from mastapy.utility.databases import _1826

            return self._parent._cast(_1826.NamedDatabase)

        @property
        def sql_database(
            self: "CylindricalGearPlasticMaterialDatabase._Cast_CylindricalGearPlasticMaterialDatabase",
        ):
            pass

            from mastapy.utility.databases import _1829

            return self._parent._cast(_1829.SQLDatabase)

        @property
        def database(
            self: "CylindricalGearPlasticMaterialDatabase._Cast_CylindricalGearPlasticMaterialDatabase",
        ):
            pass

            from mastapy.utility.databases import _1822

            return self._parent._cast(_1822.Database)

        @property
        def cylindrical_gear_plastic_material_database(
            self: "CylindricalGearPlasticMaterialDatabase._Cast_CylindricalGearPlasticMaterialDatabase",
        ) -> "CylindricalGearPlasticMaterialDatabase":
            return self._parent

        def __getattr__(
            self: "CylindricalGearPlasticMaterialDatabase._Cast_CylindricalGearPlasticMaterialDatabase",
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
        self: Self, instance_to_wrap: "CylindricalGearPlasticMaterialDatabase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearPlasticMaterialDatabase._Cast_CylindricalGearPlasticMaterialDatabase":
        return self._Cast_CylindricalGearPlasticMaterialDatabase(self)
