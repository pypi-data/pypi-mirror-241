"""LoadedCylindricalRollerBearingResults"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling import _2022
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_CYLINDRICAL_ROLLER_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedCylindricalRollerBearingResults",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2062


__docformat__ = "restructuredtext en"
__all__ = ("LoadedCylindricalRollerBearingResults",)


Self = TypeVar("Self", bound="LoadedCylindricalRollerBearingResults")


class LoadedCylindricalRollerBearingResults(_2022.LoadedNonBarrelRollerBearingResults):
    """LoadedCylindricalRollerBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_CYLINDRICAL_ROLLER_BEARING_RESULTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedCylindricalRollerBearingResults"
    )

    class _Cast_LoadedCylindricalRollerBearingResults:
        """Special nested class for casting LoadedCylindricalRollerBearingResults to subclasses."""

        def __init__(
            self: "LoadedCylindricalRollerBearingResults._Cast_LoadedCylindricalRollerBearingResults",
            parent: "LoadedCylindricalRollerBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_non_barrel_roller_bearing_results(
            self: "LoadedCylindricalRollerBearingResults._Cast_LoadedCylindricalRollerBearingResults",
        ):
            return self._parent._cast(_2022.LoadedNonBarrelRollerBearingResults)

        @property
        def loaded_roller_bearing_results(
            self: "LoadedCylindricalRollerBearingResults._Cast_LoadedCylindricalRollerBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2027

            return self._parent._cast(_2027.LoadedRollerBearingResults)

        @property
        def loaded_rolling_bearing_results(
            self: "LoadedCylindricalRollerBearingResults._Cast_LoadedCylindricalRollerBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2031

            return self._parent._cast(_2031.LoadedRollingBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedCylindricalRollerBearingResults._Cast_LoadedCylindricalRollerBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1952

            return self._parent._cast(_1952.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedCylindricalRollerBearingResults._Cast_LoadedCylindricalRollerBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1955

            return self._parent._cast(_1955.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedCylindricalRollerBearingResults._Cast_LoadedCylindricalRollerBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1947

            return self._parent._cast(_1947.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedCylindricalRollerBearingResults._Cast_LoadedCylindricalRollerBearingResults",
        ):
            from mastapy.bearings import _1873

            return self._parent._cast(_1873.BearingLoadCaseResultsLightweight)

        @property
        def loaded_needle_roller_bearing_results(
            self: "LoadedCylindricalRollerBearingResults._Cast_LoadedCylindricalRollerBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2019

            return self._parent._cast(_2019.LoadedNeedleRollerBearingResults)

        @property
        def loaded_cylindrical_roller_bearing_results(
            self: "LoadedCylindricalRollerBearingResults._Cast_LoadedCylindricalRollerBearingResults",
        ) -> "LoadedCylindricalRollerBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedCylindricalRollerBearingResults._Cast_LoadedCylindricalRollerBearingResults",
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
        self: Self, instance_to_wrap: "LoadedCylindricalRollerBearingResults.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def permissible_continuous_axial_load(
        self: Self,
    ) -> "_2062.PermissibleContinuousAxialLoadResults":
        """mastapy.bearings.bearing_results.rolling.PermissibleContinuousAxialLoadResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleContinuousAxialLoad

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedCylindricalRollerBearingResults._Cast_LoadedCylindricalRollerBearingResults":
        return self._Cast_LoadedCylindricalRollerBearingResults(self)
