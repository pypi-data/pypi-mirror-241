"""CustomReportDefinitionItem"""
from __future__ import annotations

from typing import TypeVar

from mastapy.utility.report import _1769
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_DEFINITION_ITEM = python_net_import(
    "SMT.MastaAPI.Utility.Report", "CustomReportDefinitionItem"
)


__docformat__ = "restructuredtext en"
__all__ = ("CustomReportDefinitionItem",)


Self = TypeVar("Self", bound="CustomReportDefinitionItem")


class CustomReportDefinitionItem(_1769.CustomReportNameableItem):
    """CustomReportDefinitionItem

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_DEFINITION_ITEM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomReportDefinitionItem")

    class _Cast_CustomReportDefinitionItem:
        """Special nested class for casting CustomReportDefinitionItem to subclasses."""

        def __init__(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
            parent: "CustomReportDefinitionItem",
        ):
            self._parent = parent

        @property
        def custom_report_nameable_item(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ):
            return self._parent._cast(_1769.CustomReportNameableItem)

        @property
        def custom_report_item(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ):
            from mastapy.utility.report import _1761

            return self._parent._cast(_1761.CustomReportItem)

        @property
        def ad_hoc_custom_table(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ):
            from mastapy.utility.report import _1740

            return self._parent._cast(_1740.AdHocCustomTable)

        @property
        def custom_chart(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ):
            from mastapy.utility.report import _1748

            return self._parent._cast(_1748.CustomChart)

        @property
        def custom_drawing(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ):
            from mastapy.utility.report import _1749

            return self._parent._cast(_1749.CustomDrawing)

        @property
        def custom_graphic(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ):
            from mastapy.utility.report import _1750

            return self._parent._cast(_1750.CustomGraphic)

        @property
        def custom_image(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ):
            from mastapy.utility.report import _1751

            return self._parent._cast(_1751.CustomImage)

        @property
        def custom_report_html_item(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ):
            from mastapy.utility.report import _1760

            return self._parent._cast(_1760.CustomReportHtmlItem)

        @property
        def custom_report_status_item(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ):
            from mastapy.utility.report import _1772

            return self._parent._cast(_1772.CustomReportStatusItem)

        @property
        def custom_report_text(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ):
            from mastapy.utility.report import _1775

            return self._parent._cast(_1775.CustomReportText)

        @property
        def custom_sub_report(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ):
            from mastapy.utility.report import _1777

            return self._parent._cast(_1777.CustomSubReport)

        @property
        def loaded_bearing_chart_reporter(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ):
            from mastapy.bearings.bearing_results import _1945

            return self._parent._cast(_1945.LoadedBearingChartReporter)

        @property
        def parametric_study_histogram(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4383,
            )

            return self._parent._cast(_4383.ParametricStudyHistogram)

        @property
        def custom_report_definition_item(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
        ) -> "CustomReportDefinitionItem":
            return self._parent

        def __getattr__(
            self: "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomReportDefinitionItem.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CustomReportDefinitionItem._Cast_CustomReportDefinitionItem":
        return self._Cast_CustomReportDefinitionItem(self)
