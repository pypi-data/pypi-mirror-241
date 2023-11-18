"""FaceGearSetRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating import _361
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Face", "FaceGearSetRating"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.face import _993
    from mastapy.gears.rating.face import _446, _445


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearSetRating",)


Self = TypeVar("Self", bound="FaceGearSetRating")


class FaceGearSetRating(_361.GearSetRating):
    """FaceGearSetRating

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearSetRating")

    class _Cast_FaceGearSetRating:
        """Special nested class for casting FaceGearSetRating to subclasses."""

        def __init__(
            self: "FaceGearSetRating._Cast_FaceGearSetRating",
            parent: "FaceGearSetRating",
        ):
            self._parent = parent

        @property
        def gear_set_rating(self: "FaceGearSetRating._Cast_FaceGearSetRating"):
            return self._parent._cast(_361.GearSetRating)

        @property
        def abstract_gear_set_rating(self: "FaceGearSetRating._Cast_FaceGearSetRating"):
            from mastapy.gears.rating import _353

            return self._parent._cast(_353.AbstractGearSetRating)

        @property
        def abstract_gear_set_analysis(
            self: "FaceGearSetRating._Cast_FaceGearSetRating",
        ):
            from mastapy.gears.analysis import _1215

            return self._parent._cast(_1215.AbstractGearSetAnalysis)

        @property
        def face_gear_set_rating(
            self: "FaceGearSetRating._Cast_FaceGearSetRating",
        ) -> "FaceGearSetRating":
            return self._parent

        def __getattr__(self: "FaceGearSetRating._Cast_FaceGearSetRating", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearSetRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return ""

        return temp

    @property
    def face_gear_set(self: Self) -> "_993.FaceGearSetDesign":
        """mastapy.gears.gear_designs.face.FaceGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_ratings(self: Self) -> "List[_446.FaceGearRating]":
        """List[mastapy.gears.rating.face.FaceGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_gear_ratings(self: Self) -> "List[_446.FaceGearRating]":
        """List[mastapy.gears.rating.face.FaceGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gear_mesh_ratings(self: Self) -> "List[_445.FaceGearMeshRating]":
        """List[mastapy.gears.rating.face.FaceGearMeshRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_mesh_ratings(self: Self) -> "List[_445.FaceGearMeshRating]":
        """List[mastapy.gears.rating.face.FaceGearMeshRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "FaceGearSetRating._Cast_FaceGearSetRating":
        return self._Cast_FaceGearSetRating(self)
