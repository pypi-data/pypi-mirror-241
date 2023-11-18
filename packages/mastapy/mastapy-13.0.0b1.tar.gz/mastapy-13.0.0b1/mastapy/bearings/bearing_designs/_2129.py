"""DetailedBearing"""
from __future__ import annotations

from typing import TypeVar

from mastapy.bearings.bearing_designs import _2132
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DETAILED_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns", "DetailedBearing"
)


__docformat__ = "restructuredtext en"
__all__ = ("DetailedBearing",)


Self = TypeVar("Self", bound="DetailedBearing")


class DetailedBearing(_2132.NonLinearBearing):
    """DetailedBearing

    This is a mastapy class.
    """

    TYPE = _DETAILED_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DetailedBearing")

    class _Cast_DetailedBearing:
        """Special nested class for casting DetailedBearing to subclasses."""

        def __init__(
            self: "DetailedBearing._Cast_DetailedBearing", parent: "DetailedBearing"
        ):
            self._parent = parent

        @property
        def non_linear_bearing(self: "DetailedBearing._Cast_DetailedBearing"):
            return self._parent._cast(_2132.NonLinearBearing)

        @property
        def bearing_design(self: "DetailedBearing._Cast_DetailedBearing"):
            from mastapy.bearings.bearing_designs import _2128

            return self._parent._cast(_2128.BearingDesign)

        @property
        def angular_contact_ball_bearing(self: "DetailedBearing._Cast_DetailedBearing"):
            from mastapy.bearings.bearing_designs.rolling import _2133

            return self._parent._cast(_2133.AngularContactBallBearing)

        @property
        def angular_contact_thrust_ball_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ):
            from mastapy.bearings.bearing_designs.rolling import _2134

            return self._parent._cast(_2134.AngularContactThrustBallBearing)

        @property
        def asymmetric_spherical_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ):
            from mastapy.bearings.bearing_designs.rolling import _2135

            return self._parent._cast(_2135.AsymmetricSphericalRollerBearing)

        @property
        def axial_thrust_cylindrical_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ):
            from mastapy.bearings.bearing_designs.rolling import _2136

            return self._parent._cast(_2136.AxialThrustCylindricalRollerBearing)

        @property
        def axial_thrust_needle_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ):
            from mastapy.bearings.bearing_designs.rolling import _2137

            return self._parent._cast(_2137.AxialThrustNeedleRollerBearing)

        @property
        def ball_bearing(self: "DetailedBearing._Cast_DetailedBearing"):
            from mastapy.bearings.bearing_designs.rolling import _2138

            return self._parent._cast(_2138.BallBearing)

        @property
        def barrel_roller_bearing(self: "DetailedBearing._Cast_DetailedBearing"):
            from mastapy.bearings.bearing_designs.rolling import _2140

            return self._parent._cast(_2140.BarrelRollerBearing)

        @property
        def crossed_roller_bearing(self: "DetailedBearing._Cast_DetailedBearing"):
            from mastapy.bearings.bearing_designs.rolling import _2146

            return self._parent._cast(_2146.CrossedRollerBearing)

        @property
        def cylindrical_roller_bearing(self: "DetailedBearing._Cast_DetailedBearing"):
            from mastapy.bearings.bearing_designs.rolling import _2147

            return self._parent._cast(_2147.CylindricalRollerBearing)

        @property
        def deep_groove_ball_bearing(self: "DetailedBearing._Cast_DetailedBearing"):
            from mastapy.bearings.bearing_designs.rolling import _2148

            return self._parent._cast(_2148.DeepGrooveBallBearing)

        @property
        def four_point_contact_ball_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ):
            from mastapy.bearings.bearing_designs.rolling import _2152

            return self._parent._cast(_2152.FourPointContactBallBearing)

        @property
        def multi_point_contact_ball_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ):
            from mastapy.bearings.bearing_designs.rolling import _2157

            return self._parent._cast(_2157.MultiPointContactBallBearing)

        @property
        def needle_roller_bearing(self: "DetailedBearing._Cast_DetailedBearing"):
            from mastapy.bearings.bearing_designs.rolling import _2158

            return self._parent._cast(_2158.NeedleRollerBearing)

        @property
        def non_barrel_roller_bearing(self: "DetailedBearing._Cast_DetailedBearing"):
            from mastapy.bearings.bearing_designs.rolling import _2159

            return self._parent._cast(_2159.NonBarrelRollerBearing)

        @property
        def roller_bearing(self: "DetailedBearing._Cast_DetailedBearing"):
            from mastapy.bearings.bearing_designs.rolling import _2160

            return self._parent._cast(_2160.RollerBearing)

        @property
        def rolling_bearing(self: "DetailedBearing._Cast_DetailedBearing"):
            from mastapy.bearings.bearing_designs.rolling import _2163

            return self._parent._cast(_2163.RollingBearing)

        @property
        def self_aligning_ball_bearing(self: "DetailedBearing._Cast_DetailedBearing"):
            from mastapy.bearings.bearing_designs.rolling import _2164

            return self._parent._cast(_2164.SelfAligningBallBearing)

        @property
        def spherical_roller_bearing(self: "DetailedBearing._Cast_DetailedBearing"):
            from mastapy.bearings.bearing_designs.rolling import _2167

            return self._parent._cast(_2167.SphericalRollerBearing)

        @property
        def spherical_roller_thrust_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ):
            from mastapy.bearings.bearing_designs.rolling import _2168

            return self._parent._cast(_2168.SphericalRollerThrustBearing)

        @property
        def taper_roller_bearing(self: "DetailedBearing._Cast_DetailedBearing"):
            from mastapy.bearings.bearing_designs.rolling import _2169

            return self._parent._cast(_2169.TaperRollerBearing)

        @property
        def three_point_contact_ball_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ):
            from mastapy.bearings.bearing_designs.rolling import _2170

            return self._parent._cast(_2170.ThreePointContactBallBearing)

        @property
        def thrust_ball_bearing(self: "DetailedBearing._Cast_DetailedBearing"):
            from mastapy.bearings.bearing_designs.rolling import _2171

            return self._parent._cast(_2171.ThrustBallBearing)

        @property
        def toroidal_roller_bearing(self: "DetailedBearing._Cast_DetailedBearing"):
            from mastapy.bearings.bearing_designs.rolling import _2172

            return self._parent._cast(_2172.ToroidalRollerBearing)

        @property
        def pad_fluid_film_bearing(self: "DetailedBearing._Cast_DetailedBearing"):
            from mastapy.bearings.bearing_designs.fluid_film import _2185

            return self._parent._cast(_2185.PadFluidFilmBearing)

        @property
        def plain_grease_filled_journal_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ):
            from mastapy.bearings.bearing_designs.fluid_film import _2187

            return self._parent._cast(_2187.PlainGreaseFilledJournalBearing)

        @property
        def plain_journal_bearing(self: "DetailedBearing._Cast_DetailedBearing"):
            from mastapy.bearings.bearing_designs.fluid_film import _2189

            return self._parent._cast(_2189.PlainJournalBearing)

        @property
        def plain_oil_fed_journal_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ):
            from mastapy.bearings.bearing_designs.fluid_film import _2191

            return self._parent._cast(_2191.PlainOilFedJournalBearing)

        @property
        def tilting_pad_journal_bearing(self: "DetailedBearing._Cast_DetailedBearing"):
            from mastapy.bearings.bearing_designs.fluid_film import _2192

            return self._parent._cast(_2192.TiltingPadJournalBearing)

        @property
        def tilting_pad_thrust_bearing(self: "DetailedBearing._Cast_DetailedBearing"):
            from mastapy.bearings.bearing_designs.fluid_film import _2193

            return self._parent._cast(_2193.TiltingPadThrustBearing)

        @property
        def detailed_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "DetailedBearing":
            return self._parent

        def __getattr__(self: "DetailedBearing._Cast_DetailedBearing", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DetailedBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "DetailedBearing._Cast_DetailedBearing":
        return self._Cast_DetailedBearing(self)
