"""ParallelCoordinatesChartDefinition"""
from __future__ import annotations

from typing import TypeVar

from mastapy.utility_gui.charts import _1865
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARALLEL_COORDINATES_CHART_DEFINITION = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Charts", "ParallelCoordinatesChartDefinition"
)


__docformat__ = "restructuredtext en"
__all__ = ("ParallelCoordinatesChartDefinition",)


Self = TypeVar("Self", bound="ParallelCoordinatesChartDefinition")


class ParallelCoordinatesChartDefinition(_1865.TwoDChartDefinition):
    """ParallelCoordinatesChartDefinition

    This is a mastapy class.
    """

    TYPE = _PARALLEL_COORDINATES_CHART_DEFINITION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ParallelCoordinatesChartDefinition")

    class _Cast_ParallelCoordinatesChartDefinition:
        """Special nested class for casting ParallelCoordinatesChartDefinition to subclasses."""

        def __init__(
            self: "ParallelCoordinatesChartDefinition._Cast_ParallelCoordinatesChartDefinition",
            parent: "ParallelCoordinatesChartDefinition",
        ):
            self._parent = parent

        @property
        def two_d_chart_definition(
            self: "ParallelCoordinatesChartDefinition._Cast_ParallelCoordinatesChartDefinition",
        ):
            return self._parent._cast(_1865.TwoDChartDefinition)

        @property
        def nd_chart_definition(
            self: "ParallelCoordinatesChartDefinition._Cast_ParallelCoordinatesChartDefinition",
        ):
            from mastapy.utility_gui.charts import _1857

            return self._parent._cast(_1857.NDChartDefinition)

        @property
        def chart_definition(
            self: "ParallelCoordinatesChartDefinition._Cast_ParallelCoordinatesChartDefinition",
        ):
            from mastapy.utility.report import _1746

            return self._parent._cast(_1746.ChartDefinition)

        @property
        def parallel_coordinates_chart_definition(
            self: "ParallelCoordinatesChartDefinition._Cast_ParallelCoordinatesChartDefinition",
        ) -> "ParallelCoordinatesChartDefinition":
            return self._parent

        def __getattr__(
            self: "ParallelCoordinatesChartDefinition._Cast_ParallelCoordinatesChartDefinition",
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
        self: Self, instance_to_wrap: "ParallelCoordinatesChartDefinition.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ParallelCoordinatesChartDefinition._Cast_ParallelCoordinatesChartDefinition":
        return self._Cast_ParallelCoordinatesChartDefinition(self)
