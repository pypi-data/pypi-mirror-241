"""LoadedNonLinearBearingResults"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.bearings.bearing_results import _1947
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_NON_LINEAR_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults", "LoadedNonLinearBearingResults"
)

if TYPE_CHECKING:
    from mastapy.materials.efficiency import _300, _301


__docformat__ = "restructuredtext en"
__all__ = ("LoadedNonLinearBearingResults",)


Self = TypeVar("Self", bound="LoadedNonLinearBearingResults")


class LoadedNonLinearBearingResults(_1947.LoadedBearingResults):
    """LoadedNonLinearBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_NON_LINEAR_BEARING_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedNonLinearBearingResults")

    class _Cast_LoadedNonLinearBearingResults:
        """Special nested class for casting LoadedNonLinearBearingResults to subclasses."""

        def __init__(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
            parent: "LoadedNonLinearBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            return self._parent._cast(_1947.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings import _1873

            return self._parent._cast(_1873.BearingLoadCaseResultsLightweight)

        @property
        def loaded_concept_axial_clearance_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1949

            return self._parent._cast(_1949.LoadedConceptAxialClearanceBearingResults)

        @property
        def loaded_concept_clearance_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1950

            return self._parent._cast(_1950.LoadedConceptClearanceBearingResults)

        @property
        def loaded_concept_radial_clearance_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1951

            return self._parent._cast(_1951.LoadedConceptRadialClearanceBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1952

            return self._parent._cast(_1952.LoadedDetailedBearingResults)

        @property
        def loaded_angular_contact_ball_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _1981

            return self._parent._cast(_1981.LoadedAngularContactBallBearingResults)

        @property
        def loaded_angular_contact_thrust_ball_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _1984

            return self._parent._cast(
                _1984.LoadedAngularContactThrustBallBearingResults
            )

        @property
        def loaded_asymmetric_spherical_roller_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _1987

            return self._parent._cast(
                _1987.LoadedAsymmetricSphericalRollerBearingResults
            )

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _1992

            return self._parent._cast(
                _1992.LoadedAxialThrustCylindricalRollerBearingResults
            )

        @property
        def loaded_axial_thrust_needle_roller_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _1995

            return self._parent._cast(_1995.LoadedAxialThrustNeedleRollerBearingResults)

        @property
        def loaded_ball_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2000

            return self._parent._cast(_2000.LoadedBallBearingResults)

        @property
        def loaded_crossed_roller_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2003

            return self._parent._cast(_2003.LoadedCrossedRollerBearingResults)

        @property
        def loaded_cylindrical_roller_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2007

            return self._parent._cast(_2007.LoadedCylindricalRollerBearingResults)

        @property
        def loaded_deep_groove_ball_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2010

            return self._parent._cast(_2010.LoadedDeepGrooveBallBearingResults)

        @property
        def loaded_four_point_contact_ball_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2015

            return self._parent._cast(_2015.LoadedFourPointContactBallBearingResults)

        @property
        def loaded_needle_roller_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2019

            return self._parent._cast(_2019.LoadedNeedleRollerBearingResults)

        @property
        def loaded_non_barrel_roller_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2022

            return self._parent._cast(_2022.LoadedNonBarrelRollerBearingResults)

        @property
        def loaded_roller_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2027

            return self._parent._cast(_2027.LoadedRollerBearingResults)

        @property
        def loaded_rolling_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2031

            return self._parent._cast(_2031.LoadedRollingBearingResults)

        @property
        def loaded_self_aligning_ball_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2034

            return self._parent._cast(_2034.LoadedSelfAligningBallBearingResults)

        @property
        def loaded_spherical_roller_radial_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2038

            return self._parent._cast(_2038.LoadedSphericalRollerRadialBearingResults)

        @property
        def loaded_spherical_roller_thrust_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2041

            return self._parent._cast(_2041.LoadedSphericalRollerThrustBearingResults)

        @property
        def loaded_taper_roller_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2046

            return self._parent._cast(_2046.LoadedTaperRollerBearingResults)

        @property
        def loaded_three_point_contact_ball_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2049

            return self._parent._cast(_2049.LoadedThreePointContactBallBearingResults)

        @property
        def loaded_thrust_ball_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2052

            return self._parent._cast(_2052.LoadedThrustBallBearingResults)

        @property
        def loaded_toroidal_roller_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2055

            return self._parent._cast(_2055.LoadedToroidalRollerBearingResults)

        @property
        def loaded_fluid_film_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.fluid_film import _2117

            return self._parent._cast(_2117.LoadedFluidFilmBearingResults)

        @property
        def loaded_grease_filled_journal_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.fluid_film import _2118

            return self._parent._cast(_2118.LoadedGreaseFilledJournalBearingResults)

        @property
        def loaded_pad_fluid_film_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.fluid_film import _2119

            return self._parent._cast(_2119.LoadedPadFluidFilmBearingResults)

        @property
        def loaded_plain_journal_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.fluid_film import _2120

            return self._parent._cast(_2120.LoadedPlainJournalBearingResults)

        @property
        def loaded_plain_oil_fed_journal_bearing(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.fluid_film import _2122

            return self._parent._cast(_2122.LoadedPlainOilFedJournalBearing)

        @property
        def loaded_tilting_pad_journal_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.fluid_film import _2125

            return self._parent._cast(_2125.LoadedTiltingPadJournalBearingResults)

        @property
        def loaded_tilting_pad_thrust_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ):
            from mastapy.bearings.bearing_results.fluid_film import _2126

            return self._parent._cast(_2126.LoadedTiltingPadThrustBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "LoadedNonLinearBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedNonLinearBearingResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def power_loss(self: Self) -> "_300.PowerLoss":
        """mastapy.materials.efficiency.PowerLoss

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLoss

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def resistive_torque(self: Self) -> "_301.ResistiveTorque":
        """mastapy.materials.efficiency.ResistiveTorque

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResistiveTorque

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults":
        return self._Cast_LoadedNonLinearBearingResults(self)
