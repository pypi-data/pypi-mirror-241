"""CustomReportMultiPropertyItemBase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.utility.report import _1769
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_MULTI_PROPERTY_ITEM_BASE = python_net_import(
    "SMT.MastaAPI.Utility.Report", "CustomReportMultiPropertyItemBase"
)


__docformat__ = "restructuredtext en"
__all__ = ("CustomReportMultiPropertyItemBase",)


Self = TypeVar("Self", bound="CustomReportMultiPropertyItemBase")


class CustomReportMultiPropertyItemBase(_1769.CustomReportNameableItem):
    """CustomReportMultiPropertyItemBase

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_MULTI_PROPERTY_ITEM_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomReportMultiPropertyItemBase")

    class _Cast_CustomReportMultiPropertyItemBase:
        """Special nested class for casting CustomReportMultiPropertyItemBase to subclasses."""

        def __init__(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
            parent: "CustomReportMultiPropertyItemBase",
        ):
            self._parent = parent

        @property
        def custom_report_nameable_item(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ):
            return self._parent._cast(_1769.CustomReportNameableItem)

        @property
        def custom_report_item(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ):
            from mastapy.utility.report import _1761

            return self._parent._cast(_1761.CustomReportItem)

        @property
        def shaft_damage_results_table_and_chart(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ):
            from mastapy.shafts import _20

            return self._parent._cast(_20.ShaftDamageResultsTableAndChart)

        @property
        def cylindrical_gear_table_with_mg_charts(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ):
            from mastapy.gears.gear_designs.cylindrical import _1033

            return self._parent._cast(_1033.CylindricalGearTableWithMGCharts)

        @property
        def custom_report_chart(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ):
            from mastapy.utility.report import _1754

            return self._parent._cast(_1754.CustomReportChart)

        @property
        def custom_report_multi_property_item(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ):
            from mastapy.utility.report import _1767

            return self._parent._cast(_1767.CustomReportMultiPropertyItem)

        @property
        def custom_table(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ):
            from mastapy.utility.report import _1778

            return self._parent._cast(_1778.CustomTable)

        @property
        def custom_line_chart(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ):
            from mastapy.utility_gui.charts import _1852

            return self._parent._cast(_1852.CustomLineChart)

        @property
        def custom_table_and_chart(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ):
            from mastapy.utility_gui.charts import _1853

            return self._parent._cast(_1853.CustomTableAndChart)

        @property
        def loaded_ball_element_chart_reporter(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ):
            from mastapy.bearings.bearing_results import _1944

            return self._parent._cast(_1944.LoadedBallElementChartReporter)

        @property
        def loaded_bearing_temperature_chart(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ):
            from mastapy.bearings.bearing_results import _1948

            return self._parent._cast(_1948.LoadedBearingTemperatureChart)

        @property
        def loaded_roller_element_chart_reporter(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ):
            from mastapy.bearings.bearing_results import _1956

            return self._parent._cast(_1956.LoadedRollerElementChartReporter)

        @property
        def shaft_system_deflection_sections_report(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.reporting import (
                _2847,
            )

            return self._parent._cast(_2847.ShaftSystemDeflectionSectionsReport)

        @property
        def campbell_diagram_report(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
                _4714,
            )

            return self._parent._cast(_4714.CampbellDiagramReport)

        @property
        def per_mode_results_report(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
                _4718,
            )

            return self._parent._cast(_4718.PerModeResultsReport)

        @property
        def custom_report_multi_property_item_base(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
        ) -> "CustomReportMultiPropertyItemBase":
            return self._parent

        def __getattr__(
            self: "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "CustomReportMultiPropertyItemBase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CustomReportMultiPropertyItemBase._Cast_CustomReportMultiPropertyItemBase":
        return self._Cast_CustomReportMultiPropertyItemBase(self)
