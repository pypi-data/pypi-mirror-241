"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2617 import CompoundAnalysis
    from ._2618 import SingleAnalysis
    from ._2619 import AdvancedSystemDeflectionAnalysis
    from ._2620 import AdvancedSystemDeflectionSubAnalysis
    from ._2621 import AdvancedTimeSteppingAnalysisForModulation
    from ._2622 import CompoundParametricStudyToolAnalysis
    from ._2623 import CriticalSpeedAnalysis
    from ._2624 import DynamicAnalysis
    from ._2625 import DynamicModelAtAStiffnessAnalysis
    from ._2626 import DynamicModelForHarmonicAnalysis
    from ._2627 import DynamicModelForModalAnalysis
    from ._2628 import DynamicModelForStabilityAnalysis
    from ._2629 import DynamicModelForSteadyStateSynchronousResponseAnalysis
    from ._2630 import HarmonicAnalysis
    from ._2631 import HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation
    from ._2632 import HarmonicAnalysisOfSingleExcitationAnalysis
    from ._2633 import ModalAnalysis
    from ._2634 import ModalAnalysisAtASpeed
    from ._2635 import ModalAnalysisAtAStiffness
    from ._2636 import ModalAnalysisForHarmonicAnalysis
    from ._2637 import MultibodyDynamicsAnalysis
    from ._2638 import ParametricStudyToolAnalysis
    from ._2639 import PowerFlowAnalysis
    from ._2640 import StabilityAnalysis
    from ._2641 import SteadyStateSynchronousResponseAnalysis
    from ._2642 import SteadyStateSynchronousResponseAtASpeedAnalysis
    from ._2643 import SteadyStateSynchronousResponseOnAShaftAnalysis
    from ._2644 import SystemDeflectionAnalysis
    from ._2645 import TorsionalSystemDeflectionAnalysis
    from ._2646 import AnalysisCaseVariable
    from ._2647 import ConnectionAnalysis
    from ._2648 import Context
    from ._2649 import DesignEntityAnalysis
    from ._2650 import DesignEntityGroupAnalysis
    from ._2651 import DesignEntitySingleContextAnalysis
    from ._2655 import PartAnalysis
    from ._2656 import CompoundAdvancedSystemDeflectionAnalysis
    from ._2657 import CompoundAdvancedSystemDeflectionSubAnalysis
    from ._2658 import CompoundAdvancedTimeSteppingAnalysisForModulation
    from ._2659 import CompoundCriticalSpeedAnalysis
    from ._2660 import CompoundDynamicAnalysis
    from ._2661 import CompoundDynamicModelAtAStiffnessAnalysis
    from ._2662 import CompoundDynamicModelForHarmonicAnalysis
    from ._2663 import CompoundDynamicModelForModalAnalysis
    from ._2664 import CompoundDynamicModelForStabilityAnalysis
    from ._2665 import CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis
    from ._2666 import CompoundHarmonicAnalysis
    from ._2667 import (
        CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._2668 import CompoundHarmonicAnalysisOfSingleExcitationAnalysis
    from ._2669 import CompoundModalAnalysis
    from ._2670 import CompoundModalAnalysisAtASpeed
    from ._2671 import CompoundModalAnalysisAtAStiffness
    from ._2672 import CompoundModalAnalysisForHarmonicAnalysis
    from ._2673 import CompoundMultibodyDynamicsAnalysis
    from ._2674 import CompoundPowerFlowAnalysis
    from ._2675 import CompoundStabilityAnalysis
    from ._2676 import CompoundSteadyStateSynchronousResponseAnalysis
    from ._2677 import CompoundSteadyStateSynchronousResponseAtASpeedAnalysis
    from ._2678 import CompoundSteadyStateSynchronousResponseOnAShaftAnalysis
    from ._2679 import CompoundSystemDeflectionAnalysis
    from ._2680 import CompoundTorsionalSystemDeflectionAnalysis
    from ._2681 import TESetUpForDynamicAnalysisOptions
    from ._2682 import TimeOptions
else:
    import_structure = {
        "_2617": ["CompoundAnalysis"],
        "_2618": ["SingleAnalysis"],
        "_2619": ["AdvancedSystemDeflectionAnalysis"],
        "_2620": ["AdvancedSystemDeflectionSubAnalysis"],
        "_2621": ["AdvancedTimeSteppingAnalysisForModulation"],
        "_2622": ["CompoundParametricStudyToolAnalysis"],
        "_2623": ["CriticalSpeedAnalysis"],
        "_2624": ["DynamicAnalysis"],
        "_2625": ["DynamicModelAtAStiffnessAnalysis"],
        "_2626": ["DynamicModelForHarmonicAnalysis"],
        "_2627": ["DynamicModelForModalAnalysis"],
        "_2628": ["DynamicModelForStabilityAnalysis"],
        "_2629": ["DynamicModelForSteadyStateSynchronousResponseAnalysis"],
        "_2630": ["HarmonicAnalysis"],
        "_2631": ["HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation"],
        "_2632": ["HarmonicAnalysisOfSingleExcitationAnalysis"],
        "_2633": ["ModalAnalysis"],
        "_2634": ["ModalAnalysisAtASpeed"],
        "_2635": ["ModalAnalysisAtAStiffness"],
        "_2636": ["ModalAnalysisForHarmonicAnalysis"],
        "_2637": ["MultibodyDynamicsAnalysis"],
        "_2638": ["ParametricStudyToolAnalysis"],
        "_2639": ["PowerFlowAnalysis"],
        "_2640": ["StabilityAnalysis"],
        "_2641": ["SteadyStateSynchronousResponseAnalysis"],
        "_2642": ["SteadyStateSynchronousResponseAtASpeedAnalysis"],
        "_2643": ["SteadyStateSynchronousResponseOnAShaftAnalysis"],
        "_2644": ["SystemDeflectionAnalysis"],
        "_2645": ["TorsionalSystemDeflectionAnalysis"],
        "_2646": ["AnalysisCaseVariable"],
        "_2647": ["ConnectionAnalysis"],
        "_2648": ["Context"],
        "_2649": ["DesignEntityAnalysis"],
        "_2650": ["DesignEntityGroupAnalysis"],
        "_2651": ["DesignEntitySingleContextAnalysis"],
        "_2655": ["PartAnalysis"],
        "_2656": ["CompoundAdvancedSystemDeflectionAnalysis"],
        "_2657": ["CompoundAdvancedSystemDeflectionSubAnalysis"],
        "_2658": ["CompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_2659": ["CompoundCriticalSpeedAnalysis"],
        "_2660": ["CompoundDynamicAnalysis"],
        "_2661": ["CompoundDynamicModelAtAStiffnessAnalysis"],
        "_2662": ["CompoundDynamicModelForHarmonicAnalysis"],
        "_2663": ["CompoundDynamicModelForModalAnalysis"],
        "_2664": ["CompoundDynamicModelForStabilityAnalysis"],
        "_2665": ["CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis"],
        "_2666": ["CompoundHarmonicAnalysis"],
        "_2667": [
            "CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_2668": ["CompoundHarmonicAnalysisOfSingleExcitationAnalysis"],
        "_2669": ["CompoundModalAnalysis"],
        "_2670": ["CompoundModalAnalysisAtASpeed"],
        "_2671": ["CompoundModalAnalysisAtAStiffness"],
        "_2672": ["CompoundModalAnalysisForHarmonicAnalysis"],
        "_2673": ["CompoundMultibodyDynamicsAnalysis"],
        "_2674": ["CompoundPowerFlowAnalysis"],
        "_2675": ["CompoundStabilityAnalysis"],
        "_2676": ["CompoundSteadyStateSynchronousResponseAnalysis"],
        "_2677": ["CompoundSteadyStateSynchronousResponseAtASpeedAnalysis"],
        "_2678": ["CompoundSteadyStateSynchronousResponseOnAShaftAnalysis"],
        "_2679": ["CompoundSystemDeflectionAnalysis"],
        "_2680": ["CompoundTorsionalSystemDeflectionAnalysis"],
        "_2681": ["TESetUpForDynamicAnalysisOptions"],
        "_2682": ["TimeOptions"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CompoundAnalysis",
    "SingleAnalysis",
    "AdvancedSystemDeflectionAnalysis",
    "AdvancedSystemDeflectionSubAnalysis",
    "AdvancedTimeSteppingAnalysisForModulation",
    "CompoundParametricStudyToolAnalysis",
    "CriticalSpeedAnalysis",
    "DynamicAnalysis",
    "DynamicModelAtAStiffnessAnalysis",
    "DynamicModelForHarmonicAnalysis",
    "DynamicModelForModalAnalysis",
    "DynamicModelForStabilityAnalysis",
    "DynamicModelForSteadyStateSynchronousResponseAnalysis",
    "HarmonicAnalysis",
    "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
    "HarmonicAnalysisOfSingleExcitationAnalysis",
    "ModalAnalysis",
    "ModalAnalysisAtASpeed",
    "ModalAnalysisAtAStiffness",
    "ModalAnalysisForHarmonicAnalysis",
    "MultibodyDynamicsAnalysis",
    "ParametricStudyToolAnalysis",
    "PowerFlowAnalysis",
    "StabilityAnalysis",
    "SteadyStateSynchronousResponseAnalysis",
    "SteadyStateSynchronousResponseAtASpeedAnalysis",
    "SteadyStateSynchronousResponseOnAShaftAnalysis",
    "SystemDeflectionAnalysis",
    "TorsionalSystemDeflectionAnalysis",
    "AnalysisCaseVariable",
    "ConnectionAnalysis",
    "Context",
    "DesignEntityAnalysis",
    "DesignEntityGroupAnalysis",
    "DesignEntitySingleContextAnalysis",
    "PartAnalysis",
    "CompoundAdvancedSystemDeflectionAnalysis",
    "CompoundAdvancedSystemDeflectionSubAnalysis",
    "CompoundAdvancedTimeSteppingAnalysisForModulation",
    "CompoundCriticalSpeedAnalysis",
    "CompoundDynamicAnalysis",
    "CompoundDynamicModelAtAStiffnessAnalysis",
    "CompoundDynamicModelForHarmonicAnalysis",
    "CompoundDynamicModelForModalAnalysis",
    "CompoundDynamicModelForStabilityAnalysis",
    "CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis",
    "CompoundHarmonicAnalysis",
    "CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
    "CompoundHarmonicAnalysisOfSingleExcitationAnalysis",
    "CompoundModalAnalysis",
    "CompoundModalAnalysisAtASpeed",
    "CompoundModalAnalysisAtAStiffness",
    "CompoundModalAnalysisForHarmonicAnalysis",
    "CompoundMultibodyDynamicsAnalysis",
    "CompoundPowerFlowAnalysis",
    "CompoundStabilityAnalysis",
    "CompoundSteadyStateSynchronousResponseAnalysis",
    "CompoundSteadyStateSynchronousResponseAtASpeedAnalysis",
    "CompoundSteadyStateSynchronousResponseOnAShaftAnalysis",
    "CompoundSystemDeflectionAnalysis",
    "CompoundTorsionalSystemDeflectionAnalysis",
    "TESetUpForDynamicAnalysisOptions",
    "TimeOptions",
)
