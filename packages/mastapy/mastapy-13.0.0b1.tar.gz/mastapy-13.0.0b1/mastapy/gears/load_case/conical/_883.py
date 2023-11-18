"""ConicalGearLoadCase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.load_case import _871
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.Gears.LoadCase.Conical", "ConicalGearLoadCase"
)


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearLoadCase",)


Self = TypeVar("Self", bound="ConicalGearLoadCase")


class ConicalGearLoadCase(_871.GearLoadCaseBase):
    """ConicalGearLoadCase

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearLoadCase")

    class _Cast_ConicalGearLoadCase:
        """Special nested class for casting ConicalGearLoadCase to subclasses."""

        def __init__(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
            parent: "ConicalGearLoadCase",
        ):
            self._parent = parent

        @property
        def gear_load_case_base(self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase"):
            return self._parent._cast(_871.GearLoadCaseBase)

        @property
        def gear_design_analysis(self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase"):
            from mastapy.gears.analysis import _1216

            return self._parent._cast(_1216.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ):
            from mastapy.gears.analysis import _1213

            return self._parent._cast(_1213.AbstractGearAnalysis)

        @property
        def bevel_load_case(self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase"):
            from mastapy.gears.load_case.bevel import _889

            return self._parent._cast(_889.BevelLoadCase)

        @property
        def conical_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "ConicalGearLoadCase":
            return self._parent

        def __getattr__(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ConicalGearLoadCase._Cast_ConicalGearLoadCase":
        return self._Cast_ConicalGearLoadCase(self)
