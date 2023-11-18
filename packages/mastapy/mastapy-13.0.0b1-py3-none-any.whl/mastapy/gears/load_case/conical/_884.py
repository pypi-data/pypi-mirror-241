"""ConicalGearSetLoadCase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.load_case import _872
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.Gears.LoadCase.Conical", "ConicalGearSetLoadCase"
)


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetLoadCase",)


Self = TypeVar("Self", bound="ConicalGearSetLoadCase")


class ConicalGearSetLoadCase(_872.GearSetLoadCaseBase):
    """ConicalGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearSetLoadCase")

    class _Cast_ConicalGearSetLoadCase:
        """Special nested class for casting ConicalGearSetLoadCase to subclasses."""

        def __init__(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
            parent: "ConicalGearSetLoadCase",
        ):
            self._parent = parent

        @property
        def gear_set_load_case_base(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ):
            return self._parent._cast(_872.GearSetLoadCaseBase)

        @property
        def gear_set_design_analysis(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ):
            from mastapy.gears.analysis import _1224

            return self._parent._cast(_1224.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ):
            from mastapy.gears.analysis import _1215

            return self._parent._cast(_1215.AbstractGearSetAnalysis)

        @property
        def bevel_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ):
            from mastapy.gears.load_case.bevel import _891

            return self._parent._cast(_891.BevelSetLoadCase)

        @property
        def conical_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "ConicalGearSetLoadCase":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearSetLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase":
        return self._Cast_ConicalGearSetLoadCase(self)
