"""AGMAGleasonConicalGearSetRating"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.rating.conical import _540
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.AGMAGleasonConical", "AGMAGleasonConicalGearSetRating"
)


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetRating",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetRating")


class AGMAGleasonConicalGearSetRating(_540.ConicalGearSetRating):
    """AGMAGleasonConicalGearSetRating

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalGearSetRating")

    class _Cast_AGMAGleasonConicalGearSetRating:
        """Special nested class for casting AGMAGleasonConicalGearSetRating to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetRating._Cast_AGMAGleasonConicalGearSetRating",
            parent: "AGMAGleasonConicalGearSetRating",
        ):
            self._parent = parent

        @property
        def conical_gear_set_rating(
            self: "AGMAGleasonConicalGearSetRating._Cast_AGMAGleasonConicalGearSetRating",
        ):
            return self._parent._cast(_540.ConicalGearSetRating)

        @property
        def gear_set_rating(
            self: "AGMAGleasonConicalGearSetRating._Cast_AGMAGleasonConicalGearSetRating",
        ):
            from mastapy.gears.rating import _361

            return self._parent._cast(_361.GearSetRating)

        @property
        def abstract_gear_set_rating(
            self: "AGMAGleasonConicalGearSetRating._Cast_AGMAGleasonConicalGearSetRating",
        ):
            from mastapy.gears.rating import _353

            return self._parent._cast(_353.AbstractGearSetRating)

        @property
        def abstract_gear_set_analysis(
            self: "AGMAGleasonConicalGearSetRating._Cast_AGMAGleasonConicalGearSetRating",
        ):
            from mastapy.gears.analysis import _1215

            return self._parent._cast(_1215.AbstractGearSetAnalysis)

        @property
        def zerol_bevel_gear_set_rating(
            self: "AGMAGleasonConicalGearSetRating._Cast_AGMAGleasonConicalGearSetRating",
        ):
            from mastapy.gears.rating.zerol_bevel import _369

            return self._parent._cast(_369.ZerolBevelGearSetRating)

        @property
        def straight_bevel_gear_set_rating(
            self: "AGMAGleasonConicalGearSetRating._Cast_AGMAGleasonConicalGearSetRating",
        ):
            from mastapy.gears.rating.straight_bevel import _395

            return self._parent._cast(_395.StraightBevelGearSetRating)

        @property
        def spiral_bevel_gear_set_rating(
            self: "AGMAGleasonConicalGearSetRating._Cast_AGMAGleasonConicalGearSetRating",
        ):
            from mastapy.gears.rating.spiral_bevel import _402

            return self._parent._cast(_402.SpiralBevelGearSetRating)

        @property
        def hypoid_gear_set_rating(
            self: "AGMAGleasonConicalGearSetRating._Cast_AGMAGleasonConicalGearSetRating",
        ):
            from mastapy.gears.rating.hypoid import _438

            return self._parent._cast(_438.HypoidGearSetRating)

        @property
        def bevel_gear_set_rating(
            self: "AGMAGleasonConicalGearSetRating._Cast_AGMAGleasonConicalGearSetRating",
        ):
            from mastapy.gears.rating.bevel import _554

            return self._parent._cast(_554.BevelGearSetRating)

        @property
        def agma_gleason_conical_gear_set_rating(
            self: "AGMAGleasonConicalGearSetRating._Cast_AGMAGleasonConicalGearSetRating",
        ) -> "AGMAGleasonConicalGearSetRating":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetRating._Cast_AGMAGleasonConicalGearSetRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMAGleasonConicalGearSetRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearSetRating._Cast_AGMAGleasonConicalGearSetRating":
        return self._Cast_AGMAGleasonConicalGearSetRating(self)
