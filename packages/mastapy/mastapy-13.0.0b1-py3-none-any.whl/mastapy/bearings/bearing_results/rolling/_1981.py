"""LoadedAngularContactBallBearingResults"""
from __future__ import annotations

from typing import TypeVar

from mastapy.bearings.bearing_results.rolling import _2000
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ANGULAR_CONTACT_BALL_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedAngularContactBallBearingResults",
)


__docformat__ = "restructuredtext en"
__all__ = ("LoadedAngularContactBallBearingResults",)


Self = TypeVar("Self", bound="LoadedAngularContactBallBearingResults")


class LoadedAngularContactBallBearingResults(_2000.LoadedBallBearingResults):
    """LoadedAngularContactBallBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_ANGULAR_CONTACT_BALL_BEARING_RESULTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedAngularContactBallBearingResults"
    )

    class _Cast_LoadedAngularContactBallBearingResults:
        """Special nested class for casting LoadedAngularContactBallBearingResults to subclasses."""

        def __init__(
            self: "LoadedAngularContactBallBearingResults._Cast_LoadedAngularContactBallBearingResults",
            parent: "LoadedAngularContactBallBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_ball_bearing_results(
            self: "LoadedAngularContactBallBearingResults._Cast_LoadedAngularContactBallBearingResults",
        ):
            return self._parent._cast(_2000.LoadedBallBearingResults)

        @property
        def loaded_rolling_bearing_results(
            self: "LoadedAngularContactBallBearingResults._Cast_LoadedAngularContactBallBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2031

            return self._parent._cast(_2031.LoadedRollingBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedAngularContactBallBearingResults._Cast_LoadedAngularContactBallBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1952

            return self._parent._cast(_1952.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedAngularContactBallBearingResults._Cast_LoadedAngularContactBallBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1955

            return self._parent._cast(_1955.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedAngularContactBallBearingResults._Cast_LoadedAngularContactBallBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1947

            return self._parent._cast(_1947.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedAngularContactBallBearingResults._Cast_LoadedAngularContactBallBearingResults",
        ):
            from mastapy.bearings import _1873

            return self._parent._cast(_1873.BearingLoadCaseResultsLightweight)

        @property
        def loaded_angular_contact_thrust_ball_bearing_results(
            self: "LoadedAngularContactBallBearingResults._Cast_LoadedAngularContactBallBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _1984

            return self._parent._cast(
                _1984.LoadedAngularContactThrustBallBearingResults
            )

        @property
        def loaded_angular_contact_ball_bearing_results(
            self: "LoadedAngularContactBallBearingResults._Cast_LoadedAngularContactBallBearingResults",
        ) -> "LoadedAngularContactBallBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedAngularContactBallBearingResults._Cast_LoadedAngularContactBallBearingResults",
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
        self: Self, instance_to_wrap: "LoadedAngularContactBallBearingResults.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedAngularContactBallBearingResults._Cast_LoadedAngularContactBallBearingResults":
        return self._Cast_LoadedAngularContactBallBearingResults(self)
