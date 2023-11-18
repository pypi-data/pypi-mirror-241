"""ZerolBevelGearSetRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating.bevel import _554
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.ZerolBevel", "ZerolBevelGearSetRating"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.zerol_bevel import _952
    from mastapy.gears.rating.zerol_bevel import _368, _367


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearSetRating",)


Self = TypeVar("Self", bound="ZerolBevelGearSetRating")


class ZerolBevelGearSetRating(_554.BevelGearSetRating):
    """ZerolBevelGearSetRating

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ZerolBevelGearSetRating")

    class _Cast_ZerolBevelGearSetRating:
        """Special nested class for casting ZerolBevelGearSetRating to subclasses."""

        def __init__(
            self: "ZerolBevelGearSetRating._Cast_ZerolBevelGearSetRating",
            parent: "ZerolBevelGearSetRating",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_rating(
            self: "ZerolBevelGearSetRating._Cast_ZerolBevelGearSetRating",
        ):
            return self._parent._cast(_554.BevelGearSetRating)

        @property
        def agma_gleason_conical_gear_set_rating(
            self: "ZerolBevelGearSetRating._Cast_ZerolBevelGearSetRating",
        ):
            from mastapy.gears.rating.agma_gleason_conical import _565

            return self._parent._cast(_565.AGMAGleasonConicalGearSetRating)

        @property
        def conical_gear_set_rating(
            self: "ZerolBevelGearSetRating._Cast_ZerolBevelGearSetRating",
        ):
            from mastapy.gears.rating.conical import _540

            return self._parent._cast(_540.ConicalGearSetRating)

        @property
        def gear_set_rating(
            self: "ZerolBevelGearSetRating._Cast_ZerolBevelGearSetRating",
        ):
            from mastapy.gears.rating import _361

            return self._parent._cast(_361.GearSetRating)

        @property
        def abstract_gear_set_rating(
            self: "ZerolBevelGearSetRating._Cast_ZerolBevelGearSetRating",
        ):
            from mastapy.gears.rating import _353

            return self._parent._cast(_353.AbstractGearSetRating)

        @property
        def abstract_gear_set_analysis(
            self: "ZerolBevelGearSetRating._Cast_ZerolBevelGearSetRating",
        ):
            from mastapy.gears.analysis import _1215

            return self._parent._cast(_1215.AbstractGearSetAnalysis)

        @property
        def zerol_bevel_gear_set_rating(
            self: "ZerolBevelGearSetRating._Cast_ZerolBevelGearSetRating",
        ) -> "ZerolBevelGearSetRating":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearSetRating._Cast_ZerolBevelGearSetRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ZerolBevelGearSetRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def zerol_bevel_gear_set(self: Self) -> "_952.ZerolBevelGearSetDesign":
        """mastapy.gears.gear_designs.zerol_bevel.ZerolBevelGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def zerol_bevel_gear_ratings(self: Self) -> "List[_368.ZerolBevelGearRating]":
        """List[mastapy.gears.rating.zerol_bevel.ZerolBevelGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def zerol_bevel_mesh_ratings(self: Self) -> "List[_367.ZerolBevelGearMeshRating]":
        """List[mastapy.gears.rating.zerol_bevel.ZerolBevelGearMeshRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "ZerolBevelGearSetRating._Cast_ZerolBevelGearSetRating":
        return self._Cast_ZerolBevelGearSetRating(self)
