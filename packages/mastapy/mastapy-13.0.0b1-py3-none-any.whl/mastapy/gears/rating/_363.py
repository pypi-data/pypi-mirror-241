"""MeshDutyCycleRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.gears.rating import _351
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MESH_DUTY_CYCLE_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating", "MeshDutyCycleRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating import _356


__docformat__ = "restructuredtext en"
__all__ = ("MeshDutyCycleRating",)


Self = TypeVar("Self", bound="MeshDutyCycleRating")


class MeshDutyCycleRating(_351.AbstractGearMeshRating):
    """MeshDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _MESH_DUTY_CYCLE_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MeshDutyCycleRating")

    class _Cast_MeshDutyCycleRating:
        """Special nested class for casting MeshDutyCycleRating to subclasses."""

        def __init__(
            self: "MeshDutyCycleRating._Cast_MeshDutyCycleRating",
            parent: "MeshDutyCycleRating",
        ):
            self._parent = parent

        @property
        def abstract_gear_mesh_rating(
            self: "MeshDutyCycleRating._Cast_MeshDutyCycleRating",
        ):
            return self._parent._cast(_351.AbstractGearMeshRating)

        @property
        def abstract_gear_mesh_analysis(
            self: "MeshDutyCycleRating._Cast_MeshDutyCycleRating",
        ):
            from mastapy.gears.analysis import _1214

            return self._parent._cast(_1214.AbstractGearMeshAnalysis)

        @property
        def worm_mesh_duty_cycle_rating(
            self: "MeshDutyCycleRating._Cast_MeshDutyCycleRating",
        ):
            from mastapy.gears.rating.worm import _375

            return self._parent._cast(_375.WormMeshDutyCycleRating)

        @property
        def face_gear_mesh_duty_cycle_rating(
            self: "MeshDutyCycleRating._Cast_MeshDutyCycleRating",
        ):
            from mastapy.gears.rating.face import _444

            return self._parent._cast(_444.FaceGearMeshDutyCycleRating)

        @property
        def cylindrical_mesh_duty_cycle_rating(
            self: "MeshDutyCycleRating._Cast_MeshDutyCycleRating",
        ):
            from mastapy.gears.rating.cylindrical import _464

            return self._parent._cast(_464.CylindricalMeshDutyCycleRating)

        @property
        def conical_mesh_duty_cycle_rating(
            self: "MeshDutyCycleRating._Cast_MeshDutyCycleRating",
        ):
            from mastapy.gears.rating.conical import _542

            return self._parent._cast(_542.ConicalMeshDutyCycleRating)

        @property
        def concept_gear_mesh_duty_cycle_rating(
            self: "MeshDutyCycleRating._Cast_MeshDutyCycleRating",
        ):
            from mastapy.gears.rating.concept import _547

            return self._parent._cast(_547.ConceptGearMeshDutyCycleRating)

        @property
        def mesh_duty_cycle_rating(
            self: "MeshDutyCycleRating._Cast_MeshDutyCycleRating",
        ) -> "MeshDutyCycleRating":
            return self._parent

        def __getattr__(
            self: "MeshDutyCycleRating._Cast_MeshDutyCycleRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MeshDutyCycleRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def energy_loss(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EnergyLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_efficiency(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshEfficiency

        if temp is None:
            return 0.0

        return temp

    @property
    def total_energy(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalEnergy

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_duty_cycle_ratings(self: Self) -> "List[_356.GearDutyCycleRating]":
        """List[mastapy.gears.rating.GearDutyCycleRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearDutyCycleRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "MeshDutyCycleRating._Cast_MeshDutyCycleRating":
        return self._Cast_MeshDutyCycleRating(self)
