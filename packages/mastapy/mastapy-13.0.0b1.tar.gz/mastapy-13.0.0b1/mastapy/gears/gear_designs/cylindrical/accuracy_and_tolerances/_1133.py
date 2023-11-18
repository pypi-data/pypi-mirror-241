"""AGMAISO13281B14AccuracyGrader"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1140
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMAISO13281B14_ACCURACY_GRADER = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.AccuracyAndTolerances",
    "AGMAISO13281B14AccuracyGrader",
)


__docformat__ = "restructuredtext en"
__all__ = ("AGMAISO13281B14AccuracyGrader",)


Self = TypeVar("Self", bound="AGMAISO13281B14AccuracyGrader")


class AGMAISO13281B14AccuracyGrader(_1140.ISO132812013AccuracyGrader):
    """AGMAISO13281B14AccuracyGrader

    This is a mastapy class.
    """

    TYPE = _AGMAISO13281B14_ACCURACY_GRADER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAISO13281B14AccuracyGrader")

    class _Cast_AGMAISO13281B14AccuracyGrader:
        """Special nested class for casting AGMAISO13281B14AccuracyGrader to subclasses."""

        def __init__(
            self: "AGMAISO13281B14AccuracyGrader._Cast_AGMAISO13281B14AccuracyGrader",
            parent: "AGMAISO13281B14AccuracyGrader",
        ):
            self._parent = parent

        @property
        def iso132812013_accuracy_grader(
            self: "AGMAISO13281B14AccuracyGrader._Cast_AGMAISO13281B14AccuracyGrader",
        ):
            return self._parent._cast(_1140.ISO132812013AccuracyGrader)

        @property
        def iso1328_accuracy_grader_common(
            self: "AGMAISO13281B14AccuracyGrader._Cast_AGMAISO13281B14AccuracyGrader",
        ):
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
                _1141,
            )

            return self._parent._cast(_1141.ISO1328AccuracyGraderCommon)

        @property
        def cylindrical_accuracy_grader_with_profile_form_and_slope(
            self: "AGMAISO13281B14AccuracyGrader._Cast_AGMAISO13281B14AccuracyGrader",
        ):
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
                _1135,
            )

            return self._parent._cast(
                _1135.CylindricalAccuracyGraderWithProfileFormAndSlope
            )

        @property
        def cylindrical_accuracy_grader(
            self: "AGMAISO13281B14AccuracyGrader._Cast_AGMAISO13281B14AccuracyGrader",
        ):
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
                _1134,
            )

            return self._parent._cast(_1134.CylindricalAccuracyGrader)

        @property
        def agmaiso13281b14_accuracy_grader(
            self: "AGMAISO13281B14AccuracyGrader._Cast_AGMAISO13281B14AccuracyGrader",
        ) -> "AGMAISO13281B14AccuracyGrader":
            return self._parent

        def __getattr__(
            self: "AGMAISO13281B14AccuracyGrader._Cast_AGMAISO13281B14AccuracyGrader",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMAISO13281B14AccuracyGrader.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAISO13281B14AccuracyGrader._Cast_AGMAISO13281B14AccuracyGrader":
        return self._Cast_AGMAISO13281B14AccuracyGrader(self)
