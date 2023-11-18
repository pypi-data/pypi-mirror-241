"""ISO1328AccuracyGraderCommon"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1135
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO1328_ACCURACY_GRADER_COMMON = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.AccuracyAndTolerances",
    "ISO1328AccuracyGraderCommon",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1143


__docformat__ = "restructuredtext en"
__all__ = ("ISO1328AccuracyGraderCommon",)


Self = TypeVar("Self", bound="ISO1328AccuracyGraderCommon")


class ISO1328AccuracyGraderCommon(
    _1135.CylindricalAccuracyGraderWithProfileFormAndSlope
):
    """ISO1328AccuracyGraderCommon

    This is a mastapy class.
    """

    TYPE = _ISO1328_ACCURACY_GRADER_COMMON
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ISO1328AccuracyGraderCommon")

    class _Cast_ISO1328AccuracyGraderCommon:
        """Special nested class for casting ISO1328AccuracyGraderCommon to subclasses."""

        def __init__(
            self: "ISO1328AccuracyGraderCommon._Cast_ISO1328AccuracyGraderCommon",
            parent: "ISO1328AccuracyGraderCommon",
        ):
            self._parent = parent

        @property
        def cylindrical_accuracy_grader_with_profile_form_and_slope(
            self: "ISO1328AccuracyGraderCommon._Cast_ISO1328AccuracyGraderCommon",
        ):
            return self._parent._cast(
                _1135.CylindricalAccuracyGraderWithProfileFormAndSlope
            )

        @property
        def cylindrical_accuracy_grader(
            self: "ISO1328AccuracyGraderCommon._Cast_ISO1328AccuracyGraderCommon",
        ):
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
                _1134,
            )

            return self._parent._cast(_1134.CylindricalAccuracyGrader)

        @property
        def agmaiso13281b14_accuracy_grader(
            self: "ISO1328AccuracyGraderCommon._Cast_ISO1328AccuracyGraderCommon",
        ):
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
                _1133,
            )

            return self._parent._cast(_1133.AGMAISO13281B14AccuracyGrader)

        @property
        def iso132811995_accuracy_grader(
            self: "ISO1328AccuracyGraderCommon._Cast_ISO1328AccuracyGraderCommon",
        ):
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
                _1139,
            )

            return self._parent._cast(_1139.ISO132811995AccuracyGrader)

        @property
        def iso132812013_accuracy_grader(
            self: "ISO1328AccuracyGraderCommon._Cast_ISO1328AccuracyGraderCommon",
        ):
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
                _1140,
            )

            return self._parent._cast(_1140.ISO132812013AccuracyGrader)

        @property
        def iso1328_accuracy_grader_common(
            self: "ISO1328AccuracyGraderCommon._Cast_ISO1328AccuracyGraderCommon",
        ) -> "ISO1328AccuracyGraderCommon":
            return self._parent

        def __getattr__(
            self: "ISO1328AccuracyGraderCommon._Cast_ISO1328AccuracyGraderCommon",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ISO1328AccuracyGraderCommon.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def base_pitch_deviation(self: Self) -> "_1143.OverridableTolerance":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.OverridableTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasePitchDeviation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def toothto_tooth_radial_composite_deviation(
        self: Self,
    ) -> "_1143.OverridableTolerance":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.OverridableTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothtoToothRadialCompositeDeviation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def total_radial_composite_deviation(self: Self) -> "_1143.OverridableTolerance":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.OverridableTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalRadialCompositeDeviation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ISO1328AccuracyGraderCommon._Cast_ISO1328AccuracyGraderCommon":
        return self._Cast_ISO1328AccuracyGraderCommon(self)
