"""BevelGearRating"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.rating.agma_gleason_conical import _564
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Bevel", "BevelGearRating"
)


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearRating",)


Self = TypeVar("Self", bound="BevelGearRating")


class BevelGearRating(_564.AGMAGleasonConicalGearRating):
    """BevelGearRating

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearRating")

    class _Cast_BevelGearRating:
        """Special nested class for casting BevelGearRating to subclasses."""

        def __init__(
            self: "BevelGearRating._Cast_BevelGearRating", parent: "BevelGearRating"
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_rating(
            self: "BevelGearRating._Cast_BevelGearRating",
        ):
            return self._parent._cast(_564.AGMAGleasonConicalGearRating)

        @property
        def conical_gear_rating(self: "BevelGearRating._Cast_BevelGearRating"):
            from mastapy.gears.rating.conical import _538

            return self._parent._cast(_538.ConicalGearRating)

        @property
        def gear_rating(self: "BevelGearRating._Cast_BevelGearRating"):
            from mastapy.gears.rating import _359

            return self._parent._cast(_359.GearRating)

        @property
        def abstract_gear_rating(self: "BevelGearRating._Cast_BevelGearRating"):
            from mastapy.gears.rating import _352

            return self._parent._cast(_352.AbstractGearRating)

        @property
        def abstract_gear_analysis(self: "BevelGearRating._Cast_BevelGearRating"):
            from mastapy.gears.analysis import _1213

            return self._parent._cast(_1213.AbstractGearAnalysis)

        @property
        def zerol_bevel_gear_rating(self: "BevelGearRating._Cast_BevelGearRating"):
            from mastapy.gears.rating.zerol_bevel import _368

            return self._parent._cast(_368.ZerolBevelGearRating)

        @property
        def straight_bevel_gear_rating(self: "BevelGearRating._Cast_BevelGearRating"):
            from mastapy.gears.rating.straight_bevel import _394

            return self._parent._cast(_394.StraightBevelGearRating)

        @property
        def spiral_bevel_gear_rating(self: "BevelGearRating._Cast_BevelGearRating"):
            from mastapy.gears.rating.spiral_bevel import _401

            return self._parent._cast(_401.SpiralBevelGearRating)

        @property
        def bevel_gear_rating(
            self: "BevelGearRating._Cast_BevelGearRating",
        ) -> "BevelGearRating":
            return self._parent

        def __getattr__(self: "BevelGearRating._Cast_BevelGearRating", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "BevelGearRating._Cast_BevelGearRating":
        return self._Cast_BevelGearRating(self)
