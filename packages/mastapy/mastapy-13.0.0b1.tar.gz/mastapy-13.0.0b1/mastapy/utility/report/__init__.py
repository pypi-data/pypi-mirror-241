"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1740 import AdHocCustomTable
    from ._1741 import AxisSettings
    from ._1742 import BlankRow
    from ._1743 import CadPageOrientation
    from ._1744 import CadPageSize
    from ._1745 import CadTableBorderType
    from ._1746 import ChartDefinition
    from ._1747 import SMTChartPointShape
    from ._1748 import CustomChart
    from ._1749 import CustomDrawing
    from ._1750 import CustomGraphic
    from ._1751 import CustomImage
    from ._1752 import CustomReport
    from ._1753 import CustomReportCadDrawing
    from ._1754 import CustomReportChart
    from ._1755 import CustomReportChartItem
    from ._1756 import CustomReportColumn
    from ._1757 import CustomReportColumns
    from ._1758 import CustomReportDefinitionItem
    from ._1759 import CustomReportHorizontalLine
    from ._1760 import CustomReportHtmlItem
    from ._1761 import CustomReportItem
    from ._1762 import CustomReportItemContainer
    from ._1763 import CustomReportItemContainerCollection
    from ._1764 import CustomReportItemContainerCollectionBase
    from ._1765 import CustomReportItemContainerCollectionItem
    from ._1766 import CustomReportKey
    from ._1767 import CustomReportMultiPropertyItem
    from ._1768 import CustomReportMultiPropertyItemBase
    from ._1769 import CustomReportNameableItem
    from ._1770 import CustomReportNamedItem
    from ._1771 import CustomReportPropertyItem
    from ._1772 import CustomReportStatusItem
    from ._1773 import CustomReportTab
    from ._1774 import CustomReportTabs
    from ._1775 import CustomReportText
    from ._1776 import CustomRow
    from ._1777 import CustomSubReport
    from ._1778 import CustomTable
    from ._1779 import DefinitionBooleanCheckOptions
    from ._1780 import DynamicCustomReportItem
    from ._1781 import FontStyle
    from ._1782 import FontWeight
    from ._1783 import HeadingSize
    from ._1784 import SimpleChartDefinition
    from ._1785 import UserTextRow
else:
    import_structure = {
        "_1740": ["AdHocCustomTable"],
        "_1741": ["AxisSettings"],
        "_1742": ["BlankRow"],
        "_1743": ["CadPageOrientation"],
        "_1744": ["CadPageSize"],
        "_1745": ["CadTableBorderType"],
        "_1746": ["ChartDefinition"],
        "_1747": ["SMTChartPointShape"],
        "_1748": ["CustomChart"],
        "_1749": ["CustomDrawing"],
        "_1750": ["CustomGraphic"],
        "_1751": ["CustomImage"],
        "_1752": ["CustomReport"],
        "_1753": ["CustomReportCadDrawing"],
        "_1754": ["CustomReportChart"],
        "_1755": ["CustomReportChartItem"],
        "_1756": ["CustomReportColumn"],
        "_1757": ["CustomReportColumns"],
        "_1758": ["CustomReportDefinitionItem"],
        "_1759": ["CustomReportHorizontalLine"],
        "_1760": ["CustomReportHtmlItem"],
        "_1761": ["CustomReportItem"],
        "_1762": ["CustomReportItemContainer"],
        "_1763": ["CustomReportItemContainerCollection"],
        "_1764": ["CustomReportItemContainerCollectionBase"],
        "_1765": ["CustomReportItemContainerCollectionItem"],
        "_1766": ["CustomReportKey"],
        "_1767": ["CustomReportMultiPropertyItem"],
        "_1768": ["CustomReportMultiPropertyItemBase"],
        "_1769": ["CustomReportNameableItem"],
        "_1770": ["CustomReportNamedItem"],
        "_1771": ["CustomReportPropertyItem"],
        "_1772": ["CustomReportStatusItem"],
        "_1773": ["CustomReportTab"],
        "_1774": ["CustomReportTabs"],
        "_1775": ["CustomReportText"],
        "_1776": ["CustomRow"],
        "_1777": ["CustomSubReport"],
        "_1778": ["CustomTable"],
        "_1779": ["DefinitionBooleanCheckOptions"],
        "_1780": ["DynamicCustomReportItem"],
        "_1781": ["FontStyle"],
        "_1782": ["FontWeight"],
        "_1783": ["HeadingSize"],
        "_1784": ["SimpleChartDefinition"],
        "_1785": ["UserTextRow"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AdHocCustomTable",
    "AxisSettings",
    "BlankRow",
    "CadPageOrientation",
    "CadPageSize",
    "CadTableBorderType",
    "ChartDefinition",
    "SMTChartPointShape",
    "CustomChart",
    "CustomDrawing",
    "CustomGraphic",
    "CustomImage",
    "CustomReport",
    "CustomReportCadDrawing",
    "CustomReportChart",
    "CustomReportChartItem",
    "CustomReportColumn",
    "CustomReportColumns",
    "CustomReportDefinitionItem",
    "CustomReportHorizontalLine",
    "CustomReportHtmlItem",
    "CustomReportItem",
    "CustomReportItemContainer",
    "CustomReportItemContainerCollection",
    "CustomReportItemContainerCollectionBase",
    "CustomReportItemContainerCollectionItem",
    "CustomReportKey",
    "CustomReportMultiPropertyItem",
    "CustomReportMultiPropertyItemBase",
    "CustomReportNameableItem",
    "CustomReportNamedItem",
    "CustomReportPropertyItem",
    "CustomReportStatusItem",
    "CustomReportTab",
    "CustomReportTabs",
    "CustomReportText",
    "CustomRow",
    "CustomSubReport",
    "CustomTable",
    "DefinitionBooleanCheckOptions",
    "DynamicCustomReportItem",
    "FontStyle",
    "FontWeight",
    "HeadingSize",
    "SimpleChartDefinition",
    "UserTextRow",
)
