"""CustomReportMultiPropertyItem"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Generic

from mastapy.utility.report import _1768
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_MULTI_PROPERTY_ITEM = python_net_import(
    "SMT.MastaAPI.Utility.Report", "CustomReportMultiPropertyItem"
)

if TYPE_CHECKING:
    from mastapy.utility.report import _1771


__docformat__ = "restructuredtext en"
__all__ = ("CustomReportMultiPropertyItem",)


Self = TypeVar("Self", bound="CustomReportMultiPropertyItem")
TItem = TypeVar("TItem", bound="_1771.CustomReportPropertyItem")


class CustomReportMultiPropertyItem(
    _1768.CustomReportMultiPropertyItemBase, Generic[TItem]
):
    """CustomReportMultiPropertyItem

    This is a mastapy class.

    Generic Types:
        TItem
    """

    TYPE = _CUSTOM_REPORT_MULTI_PROPERTY_ITEM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomReportMultiPropertyItem")

    class _Cast_CustomReportMultiPropertyItem:
        """Special nested class for casting CustomReportMultiPropertyItem to subclasses."""

        def __init__(
            self: "CustomReportMultiPropertyItem._Cast_CustomReportMultiPropertyItem",
            parent: "CustomReportMultiPropertyItem",
        ):
            self._parent = parent

        @property
        def custom_report_multi_property_item_base(
            self: "CustomReportMultiPropertyItem._Cast_CustomReportMultiPropertyItem",
        ):
            return self._parent._cast(_1768.CustomReportMultiPropertyItemBase)

        @property
        def custom_report_nameable_item(
            self: "CustomReportMultiPropertyItem._Cast_CustomReportMultiPropertyItem",
        ):
            from mastapy.utility.report import _1769

            return self._parent._cast(_1769.CustomReportNameableItem)

        @property
        def custom_report_item(
            self: "CustomReportMultiPropertyItem._Cast_CustomReportMultiPropertyItem",
        ):
            from mastapy.utility.report import _1761

            return self._parent._cast(_1761.CustomReportItem)

        @property
        def shaft_damage_results_table_and_chart(
            self: "CustomReportMultiPropertyItem._Cast_CustomReportMultiPropertyItem",
        ):
            from mastapy.shafts import _20

            return self._parent._cast(_20.ShaftDamageResultsTableAndChart)

        @property
        def cylindrical_gear_table_with_mg_charts(
            self: "CustomReportMultiPropertyItem._Cast_CustomReportMultiPropertyItem",
        ):
            from mastapy.gears.gear_designs.cylindrical import _1033

            return self._parent._cast(_1033.CylindricalGearTableWithMGCharts)

        @property
        def custom_report_chart(
            self: "CustomReportMultiPropertyItem._Cast_CustomReportMultiPropertyItem",
        ):
            from mastapy.utility.report import _1754

            return self._parent._cast(_1754.CustomReportChart)

        @property
        def custom_table(
            self: "CustomReportMultiPropertyItem._Cast_CustomReportMultiPropertyItem",
        ):
            from mastapy.utility.report import _1778

            return self._parent._cast(_1778.CustomTable)

        @property
        def custom_line_chart(
            self: "CustomReportMultiPropertyItem._Cast_CustomReportMultiPropertyItem",
        ):
            from mastapy.utility_gui.charts import _1852

            return self._parent._cast(_1852.CustomLineChart)

        @property
        def custom_table_and_chart(
            self: "CustomReportMultiPropertyItem._Cast_CustomReportMultiPropertyItem",
        ):
            from mastapy.utility_gui.charts import _1853

            return self._parent._cast(_1853.CustomTableAndChart)

        @property
        def loaded_ball_element_chart_reporter(
            self: "CustomReportMultiPropertyItem._Cast_CustomReportMultiPropertyItem",
        ):
            from mastapy.bearings.bearing_results import _1944

            return self._parent._cast(_1944.LoadedBallElementChartReporter)

        @property
        def loaded_bearing_temperature_chart(
            self: "CustomReportMultiPropertyItem._Cast_CustomReportMultiPropertyItem",
        ):
            from mastapy.bearings.bearing_results import _1948

            return self._parent._cast(_1948.LoadedBearingTemperatureChart)

        @property
        def loaded_roller_element_chart_reporter(
            self: "CustomReportMultiPropertyItem._Cast_CustomReportMultiPropertyItem",
        ):
            from mastapy.bearings.bearing_results import _1956

            return self._parent._cast(_1956.LoadedRollerElementChartReporter)

        @property
        def shaft_system_deflection_sections_report(
            self: "CustomReportMultiPropertyItem._Cast_CustomReportMultiPropertyItem",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.reporting import (
                _2847,
            )

            return self._parent._cast(_2847.ShaftSystemDeflectionSectionsReport)

        @property
        def campbell_diagram_report(
            self: "CustomReportMultiPropertyItem._Cast_CustomReportMultiPropertyItem",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
                _4714,
            )

            return self._parent._cast(_4714.CampbellDiagramReport)

        @property
        def per_mode_results_report(
            self: "CustomReportMultiPropertyItem._Cast_CustomReportMultiPropertyItem",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
                _4718,
            )

            return self._parent._cast(_4718.PerModeResultsReport)

        @property
        def custom_report_multi_property_item(
            self: "CustomReportMultiPropertyItem._Cast_CustomReportMultiPropertyItem",
        ) -> "CustomReportMultiPropertyItem":
            return self._parent

        def __getattr__(
            self: "CustomReportMultiPropertyItem._Cast_CustomReportMultiPropertyItem",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomReportMultiPropertyItem.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CustomReportMultiPropertyItem._Cast_CustomReportMultiPropertyItem":
        return self._Cast_CustomReportMultiPropertyItem(self)
