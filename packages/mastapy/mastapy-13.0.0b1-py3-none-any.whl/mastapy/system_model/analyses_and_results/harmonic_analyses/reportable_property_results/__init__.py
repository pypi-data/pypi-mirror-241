"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5851 import AbstractSingleWhineAnalysisResultsPropertyAccessor
    from ._5852 import DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic
    from ._5853 import DataPointForResponseOfANodeAtAFrequencyToAHarmonic
    from ._5854 import FEPartHarmonicAnalysisResultsPropertyAccessor
    from ._5855 import FEPartSingleWhineAnalysisResultsPropertyAccessor
    from ._5856 import HarmonicAnalysisCombinedForMultipleSurfacesWithinAHarmonic
    from ._5857 import HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic
    from ._5858 import HarmonicAnalysisResultsBrokenDownByGroupsWithinAHarmonic
    from ._5859 import HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic
    from ._5860 import HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic
    from ._5861 import HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic
    from ._5862 import HarmonicAnalysisResultsPropertyAccessor
    from ._5863 import ResultsForMultipleOrders
    from ._5864 import ResultsForMultipleOrdersForFESurface
    from ._5865 import ResultsForMultipleOrdersForGroups
    from ._5866 import ResultsForOrder
    from ._5867 import ResultsForOrderIncludingGroups
    from ._5868 import ResultsForOrderIncludingNodes
    from ._5869 import ResultsForOrderIncludingSurfaces
    from ._5870 import ResultsForResponseOfAComponentOrSurfaceInAHarmonic
    from ._5871 import ResultsForResponseOfANodeOnAHarmonic
    from ._5872 import ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic
    from ._5873 import RootAssemblyHarmonicAnalysisResultsPropertyAccessor
    from ._5874 import RootAssemblySingleWhineAnalysisResultsPropertyAccessor
    from ._5875 import SingleWhineAnalysisResultsPropertyAccessor
else:
    import_structure = {
        "_5851": ["AbstractSingleWhineAnalysisResultsPropertyAccessor"],
        "_5852": ["DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic"],
        "_5853": ["DataPointForResponseOfANodeAtAFrequencyToAHarmonic"],
        "_5854": ["FEPartHarmonicAnalysisResultsPropertyAccessor"],
        "_5855": ["FEPartSingleWhineAnalysisResultsPropertyAccessor"],
        "_5856": ["HarmonicAnalysisCombinedForMultipleSurfacesWithinAHarmonic"],
        "_5857": ["HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic"],
        "_5858": ["HarmonicAnalysisResultsBrokenDownByGroupsWithinAHarmonic"],
        "_5859": ["HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic"],
        "_5860": ["HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic"],
        "_5861": ["HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic"],
        "_5862": ["HarmonicAnalysisResultsPropertyAccessor"],
        "_5863": ["ResultsForMultipleOrders"],
        "_5864": ["ResultsForMultipleOrdersForFESurface"],
        "_5865": ["ResultsForMultipleOrdersForGroups"],
        "_5866": ["ResultsForOrder"],
        "_5867": ["ResultsForOrderIncludingGroups"],
        "_5868": ["ResultsForOrderIncludingNodes"],
        "_5869": ["ResultsForOrderIncludingSurfaces"],
        "_5870": ["ResultsForResponseOfAComponentOrSurfaceInAHarmonic"],
        "_5871": ["ResultsForResponseOfANodeOnAHarmonic"],
        "_5872": ["ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic"],
        "_5873": ["RootAssemblyHarmonicAnalysisResultsPropertyAccessor"],
        "_5874": ["RootAssemblySingleWhineAnalysisResultsPropertyAccessor"],
        "_5875": ["SingleWhineAnalysisResultsPropertyAccessor"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractSingleWhineAnalysisResultsPropertyAccessor",
    "DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic",
    "DataPointForResponseOfANodeAtAFrequencyToAHarmonic",
    "FEPartHarmonicAnalysisResultsPropertyAccessor",
    "FEPartSingleWhineAnalysisResultsPropertyAccessor",
    "HarmonicAnalysisCombinedForMultipleSurfacesWithinAHarmonic",
    "HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic",
    "HarmonicAnalysisResultsBrokenDownByGroupsWithinAHarmonic",
    "HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic",
    "HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic",
    "HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic",
    "HarmonicAnalysisResultsPropertyAccessor",
    "ResultsForMultipleOrders",
    "ResultsForMultipleOrdersForFESurface",
    "ResultsForMultipleOrdersForGroups",
    "ResultsForOrder",
    "ResultsForOrderIncludingGroups",
    "ResultsForOrderIncludingNodes",
    "ResultsForOrderIncludingSurfaces",
    "ResultsForResponseOfAComponentOrSurfaceInAHarmonic",
    "ResultsForResponseOfANodeOnAHarmonic",
    "ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic",
    "RootAssemblyHarmonicAnalysisResultsPropertyAccessor",
    "RootAssemblySingleWhineAnalysisResultsPropertyAccessor",
    "SingleWhineAnalysisResultsPropertyAccessor",
)
