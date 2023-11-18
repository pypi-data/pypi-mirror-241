"""LoadedBallBearingResults"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor, conversion
from mastapy.bearings.bearing_results.rolling import _2031
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_BALL_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedBallBearingResults"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _1970, _2073


__docformat__ = "restructuredtext en"
__all__ = ("LoadedBallBearingResults",)


Self = TypeVar("Self", bound="LoadedBallBearingResults")


class LoadedBallBearingResults(_2031.LoadedRollingBearingResults):
    """LoadedBallBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_BALL_BEARING_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedBallBearingResults")

    class _Cast_LoadedBallBearingResults:
        """Special nested class for casting LoadedBallBearingResults to subclasses."""

        def __init__(
            self: "LoadedBallBearingResults._Cast_LoadedBallBearingResults",
            parent: "LoadedBallBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_rolling_bearing_results(
            self: "LoadedBallBearingResults._Cast_LoadedBallBearingResults",
        ):
            return self._parent._cast(_2031.LoadedRollingBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedBallBearingResults._Cast_LoadedBallBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1952

            return self._parent._cast(_1952.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedBallBearingResults._Cast_LoadedBallBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1955

            return self._parent._cast(_1955.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedBallBearingResults._Cast_LoadedBallBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1947

            return self._parent._cast(_1947.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedBallBearingResults._Cast_LoadedBallBearingResults",
        ):
            from mastapy.bearings import _1873

            return self._parent._cast(_1873.BearingLoadCaseResultsLightweight)

        @property
        def loaded_angular_contact_ball_bearing_results(
            self: "LoadedBallBearingResults._Cast_LoadedBallBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _1981

            return self._parent._cast(_1981.LoadedAngularContactBallBearingResults)

        @property
        def loaded_angular_contact_thrust_ball_bearing_results(
            self: "LoadedBallBearingResults._Cast_LoadedBallBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _1984

            return self._parent._cast(
                _1984.LoadedAngularContactThrustBallBearingResults
            )

        @property
        def loaded_deep_groove_ball_bearing_results(
            self: "LoadedBallBearingResults._Cast_LoadedBallBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2010

            return self._parent._cast(_2010.LoadedDeepGrooveBallBearingResults)

        @property
        def loaded_four_point_contact_ball_bearing_results(
            self: "LoadedBallBearingResults._Cast_LoadedBallBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2015

            return self._parent._cast(_2015.LoadedFourPointContactBallBearingResults)

        @property
        def loaded_self_aligning_ball_bearing_results(
            self: "LoadedBallBearingResults._Cast_LoadedBallBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2034

            return self._parent._cast(_2034.LoadedSelfAligningBallBearingResults)

        @property
        def loaded_three_point_contact_ball_bearing_results(
            self: "LoadedBallBearingResults._Cast_LoadedBallBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2049

            return self._parent._cast(_2049.LoadedThreePointContactBallBearingResults)

        @property
        def loaded_thrust_ball_bearing_results(
            self: "LoadedBallBearingResults._Cast_LoadedBallBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2052

            return self._parent._cast(_2052.LoadedThrustBallBearingResults)

        @property
        def loaded_ball_bearing_results(
            self: "LoadedBallBearingResults._Cast_LoadedBallBearingResults",
        ) -> "LoadedBallBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedBallBearingResults._Cast_LoadedBallBearingResults", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedBallBearingResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def friction_model_for_gyroscopic_moment(
        self: Self,
    ) -> "_1970.FrictionModelForGyroscopicMoment":
        """mastapy.bearings.bearing_results.rolling.FrictionModelForGyroscopicMoment

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FrictionModelForGyroscopicMoment

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Bearings.BearingResults.Rolling.FrictionModelForGyroscopicMoment",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.bearings.bearing_results.rolling._1970",
            "FrictionModelForGyroscopicMoment",
        )(value)

    @property
    def smearing_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SmearingSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def use_element_contact_angles_for_angular_velocities(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UseElementContactAnglesForAngularVelocities

        if temp is None:
            return False

        return temp

    @property
    def track_truncation(self: Self) -> "_2073.TrackTruncationSafetyFactorResults":
        """mastapy.bearings.bearing_results.rolling.TrackTruncationSafetyFactorResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TrackTruncation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedBallBearingResults._Cast_LoadedBallBearingResults":
        return self._Cast_LoadedBallBearingResults(self)
