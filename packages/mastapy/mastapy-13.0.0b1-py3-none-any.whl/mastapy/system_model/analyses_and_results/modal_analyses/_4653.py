"""ModalAnalysisDrawStyle"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results.dynamic_analyses import _6327
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MODAL_ANALYSIS_DRAW_STYLE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "ModalAnalysisDrawStyle",
)


__docformat__ = "restructuredtext en"
__all__ = ("ModalAnalysisDrawStyle",)


Self = TypeVar("Self", bound="ModalAnalysisDrawStyle")


class ModalAnalysisDrawStyle(_6327.DynamicAnalysisDrawStyle):
    """ModalAnalysisDrawStyle

    This is a mastapy class.
    """

    TYPE = _MODAL_ANALYSIS_DRAW_STYLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ModalAnalysisDrawStyle")

    class _Cast_ModalAnalysisDrawStyle:
        """Special nested class for casting ModalAnalysisDrawStyle to subclasses."""

        def __init__(
            self: "ModalAnalysisDrawStyle._Cast_ModalAnalysisDrawStyle",
            parent: "ModalAnalysisDrawStyle",
        ):
            self._parent = parent

        @property
        def dynamic_analysis_draw_style(
            self: "ModalAnalysisDrawStyle._Cast_ModalAnalysisDrawStyle",
        ):
            return self._parent._cast(_6327.DynamicAnalysisDrawStyle)

        @property
        def contour_draw_style(
            self: "ModalAnalysisDrawStyle._Cast_ModalAnalysisDrawStyle",
        ):
            from mastapy.system_model.drawing import _2244

            return self._parent._cast(_2244.ContourDrawStyle)

        @property
        def draw_style_base(
            self: "ModalAnalysisDrawStyle._Cast_ModalAnalysisDrawStyle",
        ):
            from mastapy.geometry import _306

            return self._parent._cast(_306.DrawStyleBase)

        @property
        def modal_analysis_draw_style(
            self: "ModalAnalysisDrawStyle._Cast_ModalAnalysisDrawStyle",
        ) -> "ModalAnalysisDrawStyle":
            return self._parent

        def __getattr__(
            self: "ModalAnalysisDrawStyle._Cast_ModalAnalysisDrawStyle", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ModalAnalysisDrawStyle.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ModalAnalysisDrawStyle._Cast_ModalAnalysisDrawStyle":
        return self._Cast_ModalAnalysisDrawStyle(self)
