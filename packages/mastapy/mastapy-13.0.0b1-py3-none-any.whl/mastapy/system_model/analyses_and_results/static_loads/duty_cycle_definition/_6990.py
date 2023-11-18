"""ForceInputOptions"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
    _6995,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FORCE_INPUT_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.DutyCycleDefinition",
    "ForceInputOptions",
)


__docformat__ = "restructuredtext en"
__all__ = ("ForceInputOptions",)


Self = TypeVar("Self", bound="ForceInputOptions")


class ForceInputOptions(_6995.PointLoadInputOptions):
    """ForceInputOptions

    This is a mastapy class.
    """

    TYPE = _FORCE_INPUT_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ForceInputOptions")

    class _Cast_ForceInputOptions:
        """Special nested class for casting ForceInputOptions to subclasses."""

        def __init__(
            self: "ForceInputOptions._Cast_ForceInputOptions",
            parent: "ForceInputOptions",
        ):
            self._parent = parent

        @property
        def point_load_input_options(self: "ForceInputOptions._Cast_ForceInputOptions"):
            return self._parent._cast(_6995.PointLoadInputOptions)

        @property
        def column_input_options(self: "ForceInputOptions._Cast_ForceInputOptions"):
            from mastapy.utility_gui import _1845

            return self._parent._cast(_1845.ColumnInputOptions)

        @property
        def force_input_options(
            self: "ForceInputOptions._Cast_ForceInputOptions",
        ) -> "ForceInputOptions":
            return self._parent

        def __getattr__(self: "ForceInputOptions._Cast_ForceInputOptions", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ForceInputOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ForceInputOptions._Cast_ForceInputOptions":
        return self._Cast_ForceInputOptions(self)
