"""LoadedAxialThrustCylindricalRollerBearingRow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling import _2023
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_AXIAL_THRUST_CYLINDRICAL_ROLLER_BEARING_ROW = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedAxialThrustCylindricalRollerBearingRow",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _1992


__docformat__ = "restructuredtext en"
__all__ = ("LoadedAxialThrustCylindricalRollerBearingRow",)


Self = TypeVar("Self", bound="LoadedAxialThrustCylindricalRollerBearingRow")


class LoadedAxialThrustCylindricalRollerBearingRow(
    _2023.LoadedNonBarrelRollerBearingRow
):
    """LoadedAxialThrustCylindricalRollerBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_AXIAL_THRUST_CYLINDRICAL_ROLLER_BEARING_ROW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedAxialThrustCylindricalRollerBearingRow"
    )

    class _Cast_LoadedAxialThrustCylindricalRollerBearingRow:
        """Special nested class for casting LoadedAxialThrustCylindricalRollerBearingRow to subclasses."""

        def __init__(
            self: "LoadedAxialThrustCylindricalRollerBearingRow._Cast_LoadedAxialThrustCylindricalRollerBearingRow",
            parent: "LoadedAxialThrustCylindricalRollerBearingRow",
        ):
            self._parent = parent

        @property
        def loaded_non_barrel_roller_bearing_row(
            self: "LoadedAxialThrustCylindricalRollerBearingRow._Cast_LoadedAxialThrustCylindricalRollerBearingRow",
        ):
            return self._parent._cast(_2023.LoadedNonBarrelRollerBearingRow)

        @property
        def loaded_roller_bearing_row(
            self: "LoadedAxialThrustCylindricalRollerBearingRow._Cast_LoadedAxialThrustCylindricalRollerBearingRow",
        ):
            from mastapy.bearings.bearing_results.rolling import _2028

            return self._parent._cast(_2028.LoadedRollerBearingRow)

        @property
        def loaded_rolling_bearing_row(
            self: "LoadedAxialThrustCylindricalRollerBearingRow._Cast_LoadedAxialThrustCylindricalRollerBearingRow",
        ):
            from mastapy.bearings.bearing_results.rolling import _2032

            return self._parent._cast(_2032.LoadedRollingBearingRow)

        @property
        def loaded_axial_thrust_needle_roller_bearing_row(
            self: "LoadedAxialThrustCylindricalRollerBearingRow._Cast_LoadedAxialThrustCylindricalRollerBearingRow",
        ):
            from mastapy.bearings.bearing_results.rolling import _1996

            return self._parent._cast(_1996.LoadedAxialThrustNeedleRollerBearingRow)

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_row(
            self: "LoadedAxialThrustCylindricalRollerBearingRow._Cast_LoadedAxialThrustCylindricalRollerBearingRow",
        ) -> "LoadedAxialThrustCylindricalRollerBearingRow":
            return self._parent

        def __getattr__(
            self: "LoadedAxialThrustCylindricalRollerBearingRow._Cast_LoadedAxialThrustCylindricalRollerBearingRow",
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
        self: Self,
        instance_to_wrap: "LoadedAxialThrustCylindricalRollerBearingRow.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def loaded_bearing(
        self: Self,
    ) -> "_1992.LoadedAxialThrustCylindricalRollerBearingResults":
        """mastapy.bearings.bearing_results.rolling.LoadedAxialThrustCylindricalRollerBearingResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadedBearing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedAxialThrustCylindricalRollerBearingRow._Cast_LoadedAxialThrustCylindricalRollerBearingRow":
        return self._Cast_LoadedAxialThrustCylindricalRollerBearingRow(self)
