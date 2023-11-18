"""ConceptGearSetRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating import _361
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Concept", "ConceptGearSetRating"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.concept import _1176
    from mastapy.gears.rating.concept import _549, _548


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearSetRating",)


Self = TypeVar("Self", bound="ConceptGearSetRating")


class ConceptGearSetRating(_361.GearSetRating):
    """ConceptGearSetRating

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptGearSetRating")

    class _Cast_ConceptGearSetRating:
        """Special nested class for casting ConceptGearSetRating to subclasses."""

        def __init__(
            self: "ConceptGearSetRating._Cast_ConceptGearSetRating",
            parent: "ConceptGearSetRating",
        ):
            self._parent = parent

        @property
        def gear_set_rating(self: "ConceptGearSetRating._Cast_ConceptGearSetRating"):
            return self._parent._cast(_361.GearSetRating)

        @property
        def abstract_gear_set_rating(
            self: "ConceptGearSetRating._Cast_ConceptGearSetRating",
        ):
            from mastapy.gears.rating import _353

            return self._parent._cast(_353.AbstractGearSetRating)

        @property
        def abstract_gear_set_analysis(
            self: "ConceptGearSetRating._Cast_ConceptGearSetRating",
        ):
            from mastapy.gears.analysis import _1215

            return self._parent._cast(_1215.AbstractGearSetAnalysis)

        @property
        def concept_gear_set_rating(
            self: "ConceptGearSetRating._Cast_ConceptGearSetRating",
        ) -> "ConceptGearSetRating":
            return self._parent

        def __getattr__(
            self: "ConceptGearSetRating._Cast_ConceptGearSetRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptGearSetRating.TYPE"):
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
    def concept_gear_set(self: Self) -> "_1176.ConceptGearSetDesign":
        """mastapy.gears.gear_designs.concept.ConceptGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_ratings(self: Self) -> "List[_549.ConceptGearRating]":
        """List[mastapy.gears.rating.concept.ConceptGearRating]

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
    def concept_gear_ratings(self: Self) -> "List[_549.ConceptGearRating]":
        """List[mastapy.gears.rating.concept.ConceptGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gear_mesh_ratings(self: Self) -> "List[_548.ConceptGearMeshRating]":
        """List[mastapy.gears.rating.concept.ConceptGearMeshRating]

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
    def concept_mesh_ratings(self: Self) -> "List[_548.ConceptGearMeshRating]":
        """List[mastapy.gears.rating.concept.ConceptGearMeshRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "ConceptGearSetRating._Cast_ConceptGearSetRating":
        return self._Cast_ConceptGearSetRating(self)
