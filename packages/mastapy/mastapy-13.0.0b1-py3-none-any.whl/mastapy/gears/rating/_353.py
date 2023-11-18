"""AbstractGearSetRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.analysis import _1215
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_GEAR_SET_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating", "AbstractGearSetRating"
)

if TYPE_CHECKING:
    from mastapy.gears import _326
    from mastapy.gears.rating import _351, _352


__docformat__ = "restructuredtext en"
__all__ = ("AbstractGearSetRating",)


Self = TypeVar("Self", bound="AbstractGearSetRating")


class AbstractGearSetRating(_1215.AbstractGearSetAnalysis):
    """AbstractGearSetRating

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_GEAR_SET_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractGearSetRating")

    class _Cast_AbstractGearSetRating:
        """Special nested class for casting AbstractGearSetRating to subclasses."""

        def __init__(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
            parent: "AbstractGearSetRating",
        ):
            self._parent = parent

        @property
        def abstract_gear_set_analysis(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            return self._parent._cast(_1215.AbstractGearSetAnalysis)

        @property
        def gear_set_duty_cycle_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating import _360

            return self._parent._cast(_360.GearSetDutyCycleRating)

        @property
        def gear_set_rating(self: "AbstractGearSetRating._Cast_AbstractGearSetRating"):
            from mastapy.gears.rating import _361

            return self._parent._cast(_361.GearSetRating)

        @property
        def zerol_bevel_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.zerol_bevel import _369

            return self._parent._cast(_369.ZerolBevelGearSetRating)

        @property
        def worm_gear_set_duty_cycle_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.worm import _373

            return self._parent._cast(_373.WormGearSetDutyCycleRating)

        @property
        def worm_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.worm import _374

            return self._parent._cast(_374.WormGearSetRating)

        @property
        def straight_bevel_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.straight_bevel import _395

            return self._parent._cast(_395.StraightBevelGearSetRating)

        @property
        def straight_bevel_diff_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.straight_bevel_diff import _398

            return self._parent._cast(_398.StraightBevelDiffGearSetRating)

        @property
        def spiral_bevel_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.spiral_bevel import _402

            return self._parent._cast(_402.SpiralBevelGearSetRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _405

            return self._parent._cast(
                _405.KlingelnbergCycloPalloidSpiralBevelGearSetRating
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.klingelnberg_hypoid import _408

            return self._parent._cast(_408.KlingelnbergCycloPalloidHypoidGearSetRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.klingelnberg_conical import _411

            return self._parent._cast(_411.KlingelnbergCycloPalloidConicalGearSetRating)

        @property
        def hypoid_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.hypoid import _438

            return self._parent._cast(_438.HypoidGearSetRating)

        @property
        def face_gear_set_duty_cycle_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.face import _447

            return self._parent._cast(_447.FaceGearSetDutyCycleRating)

        @property
        def face_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.face import _448

            return self._parent._cast(_448.FaceGearSetRating)

        @property
        def cylindrical_gear_set_duty_cycle_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.cylindrical import _461

            return self._parent._cast(_461.CylindricalGearSetDutyCycleRating)

        @property
        def cylindrical_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.cylindrical import _462

            return self._parent._cast(_462.CylindricalGearSetRating)

        @property
        def reduced_cylindrical_gear_set_duty_cycle_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.cylindrical import _478

            return self._parent._cast(_478.ReducedCylindricalGearSetDutyCycleRating)

        @property
        def conical_gear_set_duty_cycle_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.conical import _539

            return self._parent._cast(_539.ConicalGearSetDutyCycleRating)

        @property
        def conical_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.conical import _540

            return self._parent._cast(_540.ConicalGearSetRating)

        @property
        def concept_gear_set_duty_cycle_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.concept import _550

            return self._parent._cast(_550.ConceptGearSetDutyCycleRating)

        @property
        def concept_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.concept import _551

            return self._parent._cast(_551.ConceptGearSetRating)

        @property
        def bevel_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.bevel import _554

            return self._parent._cast(_554.BevelGearSetRating)

        @property
        def agma_gleason_conical_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ):
            from mastapy.gears.rating.agma_gleason_conical import _565

            return self._parent._cast(_565.AGMAGleasonConicalGearSetRating)

        @property
        def abstract_gear_set_rating(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating",
        ) -> "AbstractGearSetRating":
            return self._parent

        def __getattr__(
            self: "AbstractGearSetRating._Cast_AbstractGearSetRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractGearSetRating.TYPE"):
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
    def normalized_safety_factor_for_fatigue_and_static(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalizedSafetyFactorForFatigueAndStatic

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
    def transmission_properties_gears(self: Self) -> "_326.GearSetDesignGroup":
        """mastapy.gears.GearSetDesignGroup

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransmissionPropertiesGears

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_mesh_ratings(self: Self) -> "List[_351.AbstractGearMeshRating]":
        """List[mastapy.gears.rating.AbstractGearMeshRating]

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
    def gear_ratings(self: Self) -> "List[_352.AbstractGearRating]":
        """List[mastapy.gears.rating.AbstractGearRating]

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
    def cast_to(self: Self) -> "AbstractGearSetRating._Cast_AbstractGearSetRating":
        return self._Cast_AbstractGearSetRating(self)
