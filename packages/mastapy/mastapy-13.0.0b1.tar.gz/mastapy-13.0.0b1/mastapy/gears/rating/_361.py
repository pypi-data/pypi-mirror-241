"""GearSetRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.gears.rating import _353
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_RATING = python_net_import("SMT.MastaAPI.Gears.Rating", "GearSetRating")

if TYPE_CHECKING:
    from mastapy.materials import _265
    from mastapy.gears.rating import _358, _359


__docformat__ = "restructuredtext en"
__all__ = ("GearSetRating",)


Self = TypeVar("Self", bound="GearSetRating")


class GearSetRating(_353.AbstractGearSetRating):
    """GearSetRating

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetRating")

    class _Cast_GearSetRating:
        """Special nested class for casting GearSetRating to subclasses."""

        def __init__(
            self: "GearSetRating._Cast_GearSetRating", parent: "GearSetRating"
        ):
            self._parent = parent

        @property
        def abstract_gear_set_rating(self: "GearSetRating._Cast_GearSetRating"):
            return self._parent._cast(_353.AbstractGearSetRating)

        @property
        def abstract_gear_set_analysis(self: "GearSetRating._Cast_GearSetRating"):
            from mastapy.gears.analysis import _1215

            return self._parent._cast(_1215.AbstractGearSetAnalysis)

        @property
        def zerol_bevel_gear_set_rating(self: "GearSetRating._Cast_GearSetRating"):
            from mastapy.gears.rating.zerol_bevel import _369

            return self._parent._cast(_369.ZerolBevelGearSetRating)

        @property
        def worm_gear_set_rating(self: "GearSetRating._Cast_GearSetRating"):
            from mastapy.gears.rating.worm import _374

            return self._parent._cast(_374.WormGearSetRating)

        @property
        def straight_bevel_gear_set_rating(self: "GearSetRating._Cast_GearSetRating"):
            from mastapy.gears.rating.straight_bevel import _395

            return self._parent._cast(_395.StraightBevelGearSetRating)

        @property
        def straight_bevel_diff_gear_set_rating(
            self: "GearSetRating._Cast_GearSetRating",
        ):
            from mastapy.gears.rating.straight_bevel_diff import _398

            return self._parent._cast(_398.StraightBevelDiffGearSetRating)

        @property
        def spiral_bevel_gear_set_rating(self: "GearSetRating._Cast_GearSetRating"):
            from mastapy.gears.rating.spiral_bevel import _402

            return self._parent._cast(_402.SpiralBevelGearSetRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_rating(
            self: "GearSetRating._Cast_GearSetRating",
        ):
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _405

            return self._parent._cast(
                _405.KlingelnbergCycloPalloidSpiralBevelGearSetRating
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_rating(
            self: "GearSetRating._Cast_GearSetRating",
        ):
            from mastapy.gears.rating.klingelnberg_hypoid import _408

            return self._parent._cast(_408.KlingelnbergCycloPalloidHypoidGearSetRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_rating(
            self: "GearSetRating._Cast_GearSetRating",
        ):
            from mastapy.gears.rating.klingelnberg_conical import _411

            return self._parent._cast(_411.KlingelnbergCycloPalloidConicalGearSetRating)

        @property
        def hypoid_gear_set_rating(self: "GearSetRating._Cast_GearSetRating"):
            from mastapy.gears.rating.hypoid import _438

            return self._parent._cast(_438.HypoidGearSetRating)

        @property
        def face_gear_set_rating(self: "GearSetRating._Cast_GearSetRating"):
            from mastapy.gears.rating.face import _448

            return self._parent._cast(_448.FaceGearSetRating)

        @property
        def cylindrical_gear_set_rating(self: "GearSetRating._Cast_GearSetRating"):
            from mastapy.gears.rating.cylindrical import _462

            return self._parent._cast(_462.CylindricalGearSetRating)

        @property
        def conical_gear_set_rating(self: "GearSetRating._Cast_GearSetRating"):
            from mastapy.gears.rating.conical import _540

            return self._parent._cast(_540.ConicalGearSetRating)

        @property
        def concept_gear_set_rating(self: "GearSetRating._Cast_GearSetRating"):
            from mastapy.gears.rating.concept import _551

            return self._parent._cast(_551.ConceptGearSetRating)

        @property
        def bevel_gear_set_rating(self: "GearSetRating._Cast_GearSetRating"):
            from mastapy.gears.rating.bevel import _554

            return self._parent._cast(_554.BevelGearSetRating)

        @property
        def agma_gleason_conical_gear_set_rating(
            self: "GearSetRating._Cast_GearSetRating",
        ):
            from mastapy.gears.rating.agma_gleason_conical import _565

            return self._parent._cast(_565.AGMAGleasonConicalGearSetRating)

        @property
        def gear_set_rating(
            self: "GearSetRating._Cast_GearSetRating",
        ) -> "GearSetRating":
            return self._parent

        def __getattr__(self: "GearSetRating._Cast_GearSetRating", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: Self, value: "str"):
        self.wrapped.Name = str(value) if value is not None else ""

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
    def total_gear_set_reliability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalGearSetReliability

        if temp is None:
            return 0.0

        return temp

    @property
    def lubrication_detail(self: Self) -> "_265.LubricationDetail":
        """mastapy.materials.LubricationDetail

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LubricationDetail

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_mesh_ratings(self: Self) -> "List[_358.GearMeshRating]":
        """List[mastapy.gears.rating.GearMeshRating]

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
    def gear_ratings(self: Self) -> "List[_359.GearRating]":
        """List[mastapy.gears.rating.GearRating]

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
    def cast_to(self: Self) -> "GearSetRating._Cast_GearSetRating":
        return self._Cast_GearSetRating(self)
