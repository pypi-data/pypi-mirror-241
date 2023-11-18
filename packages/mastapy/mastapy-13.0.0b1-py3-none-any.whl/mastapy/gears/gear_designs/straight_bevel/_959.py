"""StraightBevelGearDesign"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.gear_designs.bevel import _1178
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.StraightBevel", "StraightBevelGearDesign"
)


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearDesign",)


Self = TypeVar("Self", bound="StraightBevelGearDesign")


class StraightBevelGearDesign(_1178.BevelGearDesign):
    """StraightBevelGearDesign

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelGearDesign")

    class _Cast_StraightBevelGearDesign:
        """Special nested class for casting StraightBevelGearDesign to subclasses."""

        def __init__(
            self: "StraightBevelGearDesign._Cast_StraightBevelGearDesign",
            parent: "StraightBevelGearDesign",
        ):
            self._parent = parent

        @property
        def bevel_gear_design(
            self: "StraightBevelGearDesign._Cast_StraightBevelGearDesign",
        ):
            return self._parent._cast(_1178.BevelGearDesign)

        @property
        def agma_gleason_conical_gear_design(
            self: "StraightBevelGearDesign._Cast_StraightBevelGearDesign",
        ):
            from mastapy.gears.gear_designs.agma_gleason_conical import _1191

            return self._parent._cast(_1191.AGMAGleasonConicalGearDesign)

        @property
        def conical_gear_design(
            self: "StraightBevelGearDesign._Cast_StraightBevelGearDesign",
        ):
            from mastapy.gears.gear_designs.conical import _1152

            return self._parent._cast(_1152.ConicalGearDesign)

        @property
        def gear_design(self: "StraightBevelGearDesign._Cast_StraightBevelGearDesign"):
            from mastapy.gears.gear_designs import _945

            return self._parent._cast(_945.GearDesign)

        @property
        def gear_design_component(
            self: "StraightBevelGearDesign._Cast_StraightBevelGearDesign",
        ):
            from mastapy.gears.gear_designs import _946

            return self._parent._cast(_946.GearDesignComponent)

        @property
        def straight_bevel_gear_design(
            self: "StraightBevelGearDesign._Cast_StraightBevelGearDesign",
        ) -> "StraightBevelGearDesign":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearDesign._Cast_StraightBevelGearDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelGearDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "StraightBevelGearDesign._Cast_StraightBevelGearDesign":
        return self._Cast_StraightBevelGearDesign(self)
