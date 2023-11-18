"""FlankMicroGeometry"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from PIL.Image import Image

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLANK_MICRO_GEOMETRY = python_net_import(
    "SMT.MastaAPI.Gears.MicroGeometry", "FlankMicroGeometry"
)

if TYPE_CHECKING:
    from mastapy.gears import _334
    from mastapy.gears.gear_designs import _945
    from mastapy.utility.scripting import _1739


__docformat__ = "restructuredtext en"
__all__ = ("FlankMicroGeometry",)


Self = TypeVar("Self", bound="FlankMicroGeometry")


class FlankMicroGeometry(_0.APIBase):
    """FlankMicroGeometry

    This is a mastapy class.
    """

    TYPE = _FLANK_MICRO_GEOMETRY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FlankMicroGeometry")

    class _Cast_FlankMicroGeometry:
        """Special nested class for casting FlankMicroGeometry to subclasses."""

        def __init__(
            self: "FlankMicroGeometry._Cast_FlankMicroGeometry",
            parent: "FlankMicroGeometry",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_flank_micro_geometry(
            self: "FlankMicroGeometry._Cast_FlankMicroGeometry",
        ):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1093

            return self._parent._cast(_1093.CylindricalGearFlankMicroGeometry)

        @property
        def conical_gear_flank_micro_geometry(
            self: "FlankMicroGeometry._Cast_FlankMicroGeometry",
        ):
            from mastapy.gears.gear_designs.conical.micro_geometry import _1171

            return self._parent._cast(_1171.ConicalGearFlankMicroGeometry)

        @property
        def flank_micro_geometry(
            self: "FlankMicroGeometry._Cast_FlankMicroGeometry",
        ) -> "FlankMicroGeometry":
            return self._parent

        def __getattr__(self: "FlankMicroGeometry._Cast_FlankMicroGeometry", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FlankMicroGeometry.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def micro_geometry_input_type(self: Self) -> "_334.MicroGeometryInputTypes":
        """mastapy.gears.MicroGeometryInputTypes"""
        temp = self.wrapped.MicroGeometryInputType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.MicroGeometryInputTypes"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears._334", "MicroGeometryInputTypes"
        )(value)

    @micro_geometry_input_type.setter
    @enforce_parameter_types
    def micro_geometry_input_type(self: Self, value: "_334.MicroGeometryInputTypes"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.MicroGeometryInputTypes"
        )
        self.wrapped.MicroGeometryInputType = value

    @property
    def modification_chart(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModificationChart

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def gear_design(self: Self) -> "_945.GearDesign":
        """mastapy.gears.gear_designs.GearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def user_specified_data(self: Self) -> "_1739.UserSpecifiedData":
        """mastapy.utility.scripting.UserSpecifiedData

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UserSpecifiedData

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "FlankMicroGeometry._Cast_FlankMicroGeometry":
        return self._Cast_FlankMicroGeometry(self)
