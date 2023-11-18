"""CylindricalGearSetDutyCycleRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating import _360
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_DUTY_CYCLE_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical", "CylindricalGearSetDutyCycleRating"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1026
    from mastapy.gears.rating.cylindrical.optimisation import _499
    from mastapy.gears.rating.cylindrical import _478, _464


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetDutyCycleRating",)


Self = TypeVar("Self", bound="CylindricalGearSetDutyCycleRating")


class CylindricalGearSetDutyCycleRating(_360.GearSetDutyCycleRating):
    """CylindricalGearSetDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_DUTY_CYCLE_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearSetDutyCycleRating")

    class _Cast_CylindricalGearSetDutyCycleRating:
        """Special nested class for casting CylindricalGearSetDutyCycleRating to subclasses."""

        def __init__(
            self: "CylindricalGearSetDutyCycleRating._Cast_CylindricalGearSetDutyCycleRating",
            parent: "CylindricalGearSetDutyCycleRating",
        ):
            self._parent = parent

        @property
        def gear_set_duty_cycle_rating(
            self: "CylindricalGearSetDutyCycleRating._Cast_CylindricalGearSetDutyCycleRating",
        ):
            return self._parent._cast(_360.GearSetDutyCycleRating)

        @property
        def abstract_gear_set_rating(
            self: "CylindricalGearSetDutyCycleRating._Cast_CylindricalGearSetDutyCycleRating",
        ):
            from mastapy.gears.rating import _353

            return self._parent._cast(_353.AbstractGearSetRating)

        @property
        def abstract_gear_set_analysis(
            self: "CylindricalGearSetDutyCycleRating._Cast_CylindricalGearSetDutyCycleRating",
        ):
            from mastapy.gears.analysis import _1215

            return self._parent._cast(_1215.AbstractGearSetAnalysis)

        @property
        def reduced_cylindrical_gear_set_duty_cycle_rating(
            self: "CylindricalGearSetDutyCycleRating._Cast_CylindricalGearSetDutyCycleRating",
        ):
            return self._parent._cast(_478.ReducedCylindricalGearSetDutyCycleRating)

        @property
        def cylindrical_gear_set_duty_cycle_rating(
            self: "CylindricalGearSetDutyCycleRating._Cast_CylindricalGearSetDutyCycleRating",
        ) -> "CylindricalGearSetDutyCycleRating":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSetDutyCycleRating._Cast_CylindricalGearSetDutyCycleRating",
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
        self: Self, instance_to_wrap: "CylindricalGearSetDutyCycleRating.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cylindrical_gear_set(self: Self) -> "_1026.CylindricalGearSetDesign":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def optimisations(self: Self) -> "_499.CylindricalGearSetRatingOptimisationHelper":
        """mastapy.gears.rating.cylindrical.optimisation.CylindricalGearSetRatingOptimisationHelper

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Optimisations

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def reduced_equivalent_duty_cycle(
        self: Self,
    ) -> "_478.ReducedCylindricalGearSetDutyCycleRating":
        """mastapy.gears.rating.cylindrical.ReducedCylindricalGearSetDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReducedEquivalentDutyCycle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_mesh_duty_cycle_ratings(
        self: Self,
    ) -> "List[_464.CylindricalMeshDutyCycleRating]":
        """List[mastapy.gears.rating.cylindrical.CylindricalMeshDutyCycleRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearMeshDutyCycleRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_mesh_duty_cycle_ratings(
        self: Self,
    ) -> "List[_464.CylindricalMeshDutyCycleRating]":
        """List[mastapy.gears.rating.cylindrical.CylindricalMeshDutyCycleRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMeshDutyCycleRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def quick_optimise_for_safety_factor_and_contact_ratio_with_face_width(self: Self):
        """Method does not return."""
        self.wrapped.QuickOptimiseForSafetyFactorAndContactRatioWithFaceWidth()

    def set_profile_shift_to_maximum_safety_factor_fatigue_and_static(self: Self):
        """Method does not return."""
        self.wrapped.SetProfileShiftToMaximumSafetyFactorFatigueAndStatic()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearSetDutyCycleRating._Cast_CylindricalGearSetDutyCycleRating":
        return self._Cast_CylindricalGearSetDutyCycleRating(self)
