"""KlingelnbergCycloPalloidHypoidGearRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.rating.klingelnberg_conical import _410
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.KlingelnbergHypoid",
    "KlingelnbergCycloPalloidHypoidGearRating",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.klingelnberg_hypoid import _975


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearRating",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearRating")


class KlingelnbergCycloPalloidHypoidGearRating(
    _410.KlingelnbergCycloPalloidConicalGearRating
):
    """KlingelnbergCycloPalloidHypoidGearRating

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_RATING
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidHypoidGearRating"
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearRating:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearRating to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearRating._Cast_KlingelnbergCycloPalloidHypoidGearRating",
            parent: "KlingelnbergCycloPalloidHypoidGearRating",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_rating(
            self: "KlingelnbergCycloPalloidHypoidGearRating._Cast_KlingelnbergCycloPalloidHypoidGearRating",
        ):
            return self._parent._cast(_410.KlingelnbergCycloPalloidConicalGearRating)

        @property
        def conical_gear_rating(
            self: "KlingelnbergCycloPalloidHypoidGearRating._Cast_KlingelnbergCycloPalloidHypoidGearRating",
        ):
            from mastapy.gears.rating.conical import _538

            return self._parent._cast(_538.ConicalGearRating)

        @property
        def gear_rating(
            self: "KlingelnbergCycloPalloidHypoidGearRating._Cast_KlingelnbergCycloPalloidHypoidGearRating",
        ):
            from mastapy.gears.rating import _359

            return self._parent._cast(_359.GearRating)

        @property
        def abstract_gear_rating(
            self: "KlingelnbergCycloPalloidHypoidGearRating._Cast_KlingelnbergCycloPalloidHypoidGearRating",
        ):
            from mastapy.gears.rating import _352

            return self._parent._cast(_352.AbstractGearRating)

        @property
        def abstract_gear_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearRating._Cast_KlingelnbergCycloPalloidHypoidGearRating",
        ):
            from mastapy.gears.analysis import _1213

            return self._parent._cast(_1213.AbstractGearAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_rating(
            self: "KlingelnbergCycloPalloidHypoidGearRating._Cast_KlingelnbergCycloPalloidHypoidGearRating",
        ) -> "KlingelnbergCycloPalloidHypoidGearRating":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearRating._Cast_KlingelnbergCycloPalloidHypoidGearRating",
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
        self: Self, instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearRating.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear(
        self: Self,
    ) -> "_975.KlingelnbergCycloPalloidHypoidGearDesign":
        """mastapy.gears.gear_designs.klingelnberg_hypoid.KlingelnbergCycloPalloidHypoidGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGear

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearRating._Cast_KlingelnbergCycloPalloidHypoidGearRating":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearRating(self)
