"""AbstractGearRating"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.analysis import _1213
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_GEAR_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating", "AbstractGearRating"
)


__docformat__ = "restructuredtext en"
__all__ = ("AbstractGearRating",)


Self = TypeVar("Self", bound="AbstractGearRating")


class AbstractGearRating(_1213.AbstractGearAnalysis):
    """AbstractGearRating

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_GEAR_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractGearRating")

    class _Cast_AbstractGearRating:
        """Special nested class for casting AbstractGearRating to subclasses."""

        def __init__(
            self: "AbstractGearRating._Cast_AbstractGearRating",
            parent: "AbstractGearRating",
        ):
            self._parent = parent

        @property
        def abstract_gear_analysis(self: "AbstractGearRating._Cast_AbstractGearRating"):
            return self._parent._cast(_1213.AbstractGearAnalysis)

        @property
        def gear_duty_cycle_rating(self: "AbstractGearRating._Cast_AbstractGearRating"):
            from mastapy.gears.rating import _356

            return self._parent._cast(_356.GearDutyCycleRating)

        @property
        def gear_rating(self: "AbstractGearRating._Cast_AbstractGearRating"):
            from mastapy.gears.rating import _359

            return self._parent._cast(_359.GearRating)

        @property
        def zerol_bevel_gear_rating(
            self: "AbstractGearRating._Cast_AbstractGearRating",
        ):
            from mastapy.gears.rating.zerol_bevel import _368

            return self._parent._cast(_368.ZerolBevelGearRating)

        @property
        def worm_gear_duty_cycle_rating(
            self: "AbstractGearRating._Cast_AbstractGearRating",
        ):
            from mastapy.gears.rating.worm import _370

            return self._parent._cast(_370.WormGearDutyCycleRating)

        @property
        def worm_gear_rating(self: "AbstractGearRating._Cast_AbstractGearRating"):
            from mastapy.gears.rating.worm import _372

            return self._parent._cast(_372.WormGearRating)

        @property
        def straight_bevel_gear_rating(
            self: "AbstractGearRating._Cast_AbstractGearRating",
        ):
            from mastapy.gears.rating.straight_bevel import _394

            return self._parent._cast(_394.StraightBevelGearRating)

        @property
        def straight_bevel_diff_gear_rating(
            self: "AbstractGearRating._Cast_AbstractGearRating",
        ):
            from mastapy.gears.rating.straight_bevel_diff import _397

            return self._parent._cast(_397.StraightBevelDiffGearRating)

        @property
        def spiral_bevel_gear_rating(
            self: "AbstractGearRating._Cast_AbstractGearRating",
        ):
            from mastapy.gears.rating.spiral_bevel import _401

            return self._parent._cast(_401.SpiralBevelGearRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_rating(
            self: "AbstractGearRating._Cast_AbstractGearRating",
        ):
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _404

            return self._parent._cast(
                _404.KlingelnbergCycloPalloidSpiralBevelGearRating
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_rating(
            self: "AbstractGearRating._Cast_AbstractGearRating",
        ):
            from mastapy.gears.rating.klingelnberg_hypoid import _407

            return self._parent._cast(_407.KlingelnbergCycloPalloidHypoidGearRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_rating(
            self: "AbstractGearRating._Cast_AbstractGearRating",
        ):
            from mastapy.gears.rating.klingelnberg_conical import _410

            return self._parent._cast(_410.KlingelnbergCycloPalloidConicalGearRating)

        @property
        def hypoid_gear_rating(self: "AbstractGearRating._Cast_AbstractGearRating"):
            from mastapy.gears.rating.hypoid import _437

            return self._parent._cast(_437.HypoidGearRating)

        @property
        def face_gear_duty_cycle_rating(
            self: "AbstractGearRating._Cast_AbstractGearRating",
        ):
            from mastapy.gears.rating.face import _443

            return self._parent._cast(_443.FaceGearDutyCycleRating)

        @property
        def face_gear_rating(self: "AbstractGearRating._Cast_AbstractGearRating"):
            from mastapy.gears.rating.face import _446

            return self._parent._cast(_446.FaceGearRating)

        @property
        def cylindrical_gear_duty_cycle_rating(
            self: "AbstractGearRating._Cast_AbstractGearRating",
        ):
            from mastapy.gears.rating.cylindrical import _453

            return self._parent._cast(_453.CylindricalGearDutyCycleRating)

        @property
        def cylindrical_gear_rating(
            self: "AbstractGearRating._Cast_AbstractGearRating",
        ):
            from mastapy.gears.rating.cylindrical import _458

            return self._parent._cast(_458.CylindricalGearRating)

        @property
        def conical_gear_duty_cycle_rating(
            self: "AbstractGearRating._Cast_AbstractGearRating",
        ):
            from mastapy.gears.rating.conical import _536

            return self._parent._cast(_536.ConicalGearDutyCycleRating)

        @property
        def conical_gear_rating(self: "AbstractGearRating._Cast_AbstractGearRating"):
            from mastapy.gears.rating.conical import _538

            return self._parent._cast(_538.ConicalGearRating)

        @property
        def concept_gear_duty_cycle_rating(
            self: "AbstractGearRating._Cast_AbstractGearRating",
        ):
            from mastapy.gears.rating.concept import _546

            return self._parent._cast(_546.ConceptGearDutyCycleRating)

        @property
        def concept_gear_rating(self: "AbstractGearRating._Cast_AbstractGearRating"):
            from mastapy.gears.rating.concept import _549

            return self._parent._cast(_549.ConceptGearRating)

        @property
        def bevel_gear_rating(self: "AbstractGearRating._Cast_AbstractGearRating"):
            from mastapy.gears.rating.bevel import _553

            return self._parent._cast(_553.BevelGearRating)

        @property
        def agma_gleason_conical_gear_rating(
            self: "AbstractGearRating._Cast_AbstractGearRating",
        ):
            from mastapy.gears.rating.agma_gleason_conical import _564

            return self._parent._cast(_564.AGMAGleasonConicalGearRating)

        @property
        def abstract_gear_rating(
            self: "AbstractGearRating._Cast_AbstractGearRating",
        ) -> "AbstractGearRating":
            return self._parent

        def __getattr__(self: "AbstractGearRating._Cast_AbstractGearRating", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractGearRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bending_safety_factor_for_fatigue(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BendingSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def bending_safety_factor_for_static(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BendingSafetyFactorForStatic

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_safety_factor_for_fatigue(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_safety_factor_for_static(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactSafetyFactorForStatic

        if temp is None:
            return 0.0

        return temp

    @property
    def cycles_to_fail(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CyclesToFail

        if temp is None:
            return 0.0

        return temp

    @property
    def cycles_to_fail_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CyclesToFailBending

        if temp is None:
            return 0.0

        return temp

    @property
    def cycles_to_fail_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CyclesToFailContact

        if temp is None:
            return 0.0

        return temp

    @property
    def damage_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DamageBending

        if temp is None:
            return 0.0

        return temp

    @property
    def damage_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DamageContact

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_reliability_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearReliabilityBending

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_reliability_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearReliabilityContact

        if temp is None:
            return 0.0

        return temp

    @property
    def normalized_bending_safety_factor_for_fatigue(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalizedBendingSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def normalized_bending_safety_factor_for_static(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalizedBendingSafetyFactorForStatic

        if temp is None:
            return 0.0

        return temp

    @property
    def normalized_contact_safety_factor_for_fatigue(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalizedContactSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def normalized_contact_safety_factor_for_static(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalizedContactSafetyFactorForStatic

        if temp is None:
            return 0.0

        return temp

    @property
    def normalized_safety_factor_for_fatigue(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalizedSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def normalized_safety_factor_for_static(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalizedSafetyFactorForStatic

        if temp is None:
            return 0.0

        return temp

    @property
    def time_to_fail(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TimeToFail

        if temp is None:
            return 0.0

        return temp

    @property
    def time_to_fail_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TimeToFailBending

        if temp is None:
            return 0.0

        return temp

    @property
    def time_to_fail_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TimeToFailContact

        if temp is None:
            return 0.0

        return temp

    @property
    def total_gear_reliability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalGearReliability

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "AbstractGearRating._Cast_AbstractGearRating":
        return self._Cast_AbstractGearRating(self)
