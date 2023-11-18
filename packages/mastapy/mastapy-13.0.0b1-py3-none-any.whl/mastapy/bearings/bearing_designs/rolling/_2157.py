"""MultiPointContactBallBearing"""
from __future__ import annotations

from typing import TypeVar

from mastapy.bearings.bearing_designs.rolling import _2138
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MULTI_POINT_CONTACT_BALL_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "MultiPointContactBallBearing"
)


__docformat__ = "restructuredtext en"
__all__ = ("MultiPointContactBallBearing",)


Self = TypeVar("Self", bound="MultiPointContactBallBearing")


class MultiPointContactBallBearing(_2138.BallBearing):
    """MultiPointContactBallBearing

    This is a mastapy class.
    """

    TYPE = _MULTI_POINT_CONTACT_BALL_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MultiPointContactBallBearing")

    class _Cast_MultiPointContactBallBearing:
        """Special nested class for casting MultiPointContactBallBearing to subclasses."""

        def __init__(
            self: "MultiPointContactBallBearing._Cast_MultiPointContactBallBearing",
            parent: "MultiPointContactBallBearing",
        ):
            self._parent = parent

        @property
        def ball_bearing(
            self: "MultiPointContactBallBearing._Cast_MultiPointContactBallBearing",
        ):
            return self._parent._cast(_2138.BallBearing)

        @property
        def rolling_bearing(
            self: "MultiPointContactBallBearing._Cast_MultiPointContactBallBearing",
        ):
            from mastapy.bearings.bearing_designs.rolling import _2163

            return self._parent._cast(_2163.RollingBearing)

        @property
        def detailed_bearing(
            self: "MultiPointContactBallBearing._Cast_MultiPointContactBallBearing",
        ):
            from mastapy.bearings.bearing_designs import _2129

            return self._parent._cast(_2129.DetailedBearing)

        @property
        def non_linear_bearing(
            self: "MultiPointContactBallBearing._Cast_MultiPointContactBallBearing",
        ):
            from mastapy.bearings.bearing_designs import _2132

            return self._parent._cast(_2132.NonLinearBearing)

        @property
        def bearing_design(
            self: "MultiPointContactBallBearing._Cast_MultiPointContactBallBearing",
        ):
            from mastapy.bearings.bearing_designs import _2128

            return self._parent._cast(_2128.BearingDesign)

        @property
        def four_point_contact_ball_bearing(
            self: "MultiPointContactBallBearing._Cast_MultiPointContactBallBearing",
        ):
            from mastapy.bearings.bearing_designs.rolling import _2152

            return self._parent._cast(_2152.FourPointContactBallBearing)

        @property
        def three_point_contact_ball_bearing(
            self: "MultiPointContactBallBearing._Cast_MultiPointContactBallBearing",
        ):
            from mastapy.bearings.bearing_designs.rolling import _2170

            return self._parent._cast(_2170.ThreePointContactBallBearing)

        @property
        def multi_point_contact_ball_bearing(
            self: "MultiPointContactBallBearing._Cast_MultiPointContactBallBearing",
        ) -> "MultiPointContactBallBearing":
            return self._parent

        def __getattr__(
            self: "MultiPointContactBallBearing._Cast_MultiPointContactBallBearing",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MultiPointContactBallBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "MultiPointContactBallBearing._Cast_MultiPointContactBallBearing":
        return self._Cast_MultiPointContactBallBearing(self)
