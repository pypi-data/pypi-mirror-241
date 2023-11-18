"""ZerolBevelGearMeshRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating.bevel import _552
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MESH_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.ZerolBevel", "ZerolBevelGearMeshRating"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.zerol_bevel import _951
    from mastapy.gears.rating.zerol_bevel import _368


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearMeshRating",)


Self = TypeVar("Self", bound="ZerolBevelGearMeshRating")


class ZerolBevelGearMeshRating(_552.BevelGearMeshRating):
    """ZerolBevelGearMeshRating

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_MESH_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ZerolBevelGearMeshRating")

    class _Cast_ZerolBevelGearMeshRating:
        """Special nested class for casting ZerolBevelGearMeshRating to subclasses."""

        def __init__(
            self: "ZerolBevelGearMeshRating._Cast_ZerolBevelGearMeshRating",
            parent: "ZerolBevelGearMeshRating",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_rating(
            self: "ZerolBevelGearMeshRating._Cast_ZerolBevelGearMeshRating",
        ):
            return self._parent._cast(_552.BevelGearMeshRating)

        @property
        def agma_gleason_conical_gear_mesh_rating(
            self: "ZerolBevelGearMeshRating._Cast_ZerolBevelGearMeshRating",
        ):
            from mastapy.gears.rating.agma_gleason_conical import _563

            return self._parent._cast(_563.AGMAGleasonConicalGearMeshRating)

        @property
        def conical_gear_mesh_rating(
            self: "ZerolBevelGearMeshRating._Cast_ZerolBevelGearMeshRating",
        ):
            from mastapy.gears.rating.conical import _537

            return self._parent._cast(_537.ConicalGearMeshRating)

        @property
        def gear_mesh_rating(
            self: "ZerolBevelGearMeshRating._Cast_ZerolBevelGearMeshRating",
        ):
            from mastapy.gears.rating import _358

            return self._parent._cast(_358.GearMeshRating)

        @property
        def abstract_gear_mesh_rating(
            self: "ZerolBevelGearMeshRating._Cast_ZerolBevelGearMeshRating",
        ):
            from mastapy.gears.rating import _351

            return self._parent._cast(_351.AbstractGearMeshRating)

        @property
        def abstract_gear_mesh_analysis(
            self: "ZerolBevelGearMeshRating._Cast_ZerolBevelGearMeshRating",
        ):
            from mastapy.gears.analysis import _1214

            return self._parent._cast(_1214.AbstractGearMeshAnalysis)

        @property
        def zerol_bevel_gear_mesh_rating(
            self: "ZerolBevelGearMeshRating._Cast_ZerolBevelGearMeshRating",
        ) -> "ZerolBevelGearMeshRating":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearMeshRating._Cast_ZerolBevelGearMeshRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ZerolBevelGearMeshRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def zerol_bevel_gear_mesh(self: Self) -> "_951.ZerolBevelGearMeshDesign":
        """mastapy.gears.gear_designs.zerol_bevel.ZerolBevelGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGearMesh

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
    def cast_to(
        self: Self,
    ) -> "ZerolBevelGearMeshRating._Cast_ZerolBevelGearMeshRating":
        return self._Cast_ZerolBevelGearMeshRating(self)
