"""AnalysisCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results import _2648
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANALYSIS_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases", "AnalysisCase"
)

if TYPE_CHECKING:
    from mastapy.utility import _1576
    from mastapy.system_model import _2201
    from mastapy.system_model.analyses_and_results import _2649


__docformat__ = "restructuredtext en"
__all__ = ("AnalysisCase",)


Self = TypeVar("Self", bound="AnalysisCase")


class AnalysisCase(_2648.Context):
    """AnalysisCase

    This is a mastapy class.
    """

    TYPE = _ANALYSIS_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AnalysisCase")

    class _Cast_AnalysisCase:
        """Special nested class for casting AnalysisCase to subclasses."""

        def __init__(self: "AnalysisCase._Cast_AnalysisCase", parent: "AnalysisCase"):
            self._parent = parent

        @property
        def context(self: "AnalysisCase._Cast_AnalysisCase"):
            return self._parent._cast(_2648.Context)

        @property
        def system_deflection(self: "AnalysisCase._Cast_AnalysisCase"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2823,
            )

            return self._parent._cast(_2823.SystemDeflection)

        @property
        def torsional_system_deflection(self: "AnalysisCase._Cast_AnalysisCase"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2830,
            )

            return self._parent._cast(_2830.TorsionalSystemDeflection)

        @property
        def dynamic_model_for_steady_state_synchronous_response(
            self: "AnalysisCase._Cast_AnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3033,
            )

            return self._parent._cast(
                _3033.DynamicModelForSteadyStateSynchronousResponse
            )

        @property
        def steady_state_synchronous_response(self: "AnalysisCase._Cast_AnalysisCase"):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3087,
            )

            return self._parent._cast(_3087.SteadyStateSynchronousResponse)

        @property
        def steady_state_synchronous_response_on_a_shaft(
            self: "AnalysisCase._Cast_AnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3348,
            )

            return self._parent._cast(_3348.SteadyStateSynchronousResponseOnAShaft)

        @property
        def steady_state_synchronous_response_at_a_speed(
            self: "AnalysisCase._Cast_AnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3607,
            )

            return self._parent._cast(_3607.SteadyStateSynchronousResponseAtASpeed)

        @property
        def dynamic_model_for_stability_analysis(
            self: "AnalysisCase._Cast_AnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3814,
            )

            return self._parent._cast(_3814.DynamicModelForStabilityAnalysis)

        @property
        def stability_analysis(self: "AnalysisCase._Cast_AnalysisCase"):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3868,
            )

            return self._parent._cast(_3868.StabilityAnalysis)

        @property
        def power_flow(self: "AnalysisCase._Cast_AnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4119

            return self._parent._cast(_4119.PowerFlow)

        @property
        def parametric_study_tool(self: "AnalysisCase._Cast_AnalysisCase"):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4385,
            )

            return self._parent._cast(_4385.ParametricStudyTool)

        @property
        def dynamic_model_for_modal_analysis(self: "AnalysisCase._Cast_AnalysisCase"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4622

            return self._parent._cast(_4622.DynamicModelForModalAnalysis)

        @property
        def modal_analysis(self: "AnalysisCase._Cast_AnalysisCase"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4651

            return self._parent._cast(_4651.ModalAnalysis)

        @property
        def dynamic_model_at_a_stiffness(self: "AnalysisCase._Cast_AnalysisCase"):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4906,
            )

            return self._parent._cast(_4906.DynamicModelAtAStiffness)

        @property
        def modal_analysis_at_a_stiffness(self: "AnalysisCase._Cast_AnalysisCase"):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4932,
            )

            return self._parent._cast(_4932.ModalAnalysisAtAStiffness)

        @property
        def modal_analysis_at_a_speed(self: "AnalysisCase._Cast_AnalysisCase"):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5191,
            )

            return self._parent._cast(_5191.ModalAnalysisAtASpeed)

        @property
        def multibody_dynamics_analysis(self: "AnalysisCase._Cast_AnalysisCase"):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5462

            return self._parent._cast(_5462.MultibodyDynamicsAnalysis)

        @property
        def dynamic_model_for_harmonic_analysis(
            self: "AnalysisCase._Cast_AnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5729,
            )

            return self._parent._cast(_5729.DynamicModelForHarmonicAnalysis)

        @property
        def harmonic_analysis(self: "AnalysisCase._Cast_AnalysisCase"):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5758,
            )

            return self._parent._cast(_5758.HarmonicAnalysis)

        @property
        def harmonic_analysis_for_advanced_time_stepping_analysis_for_modulation(
            self: "AnalysisCase._Cast_AnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5762,
            )

            return self._parent._cast(
                _5762.HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def harmonic_analysis_of_single_excitation(
            self: "AnalysisCase._Cast_AnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6067,
            )

            return self._parent._cast(_6067.HarmonicAnalysisOfSingleExcitation)

        @property
        def modal_analysis_for_harmonic_analysis(
            self: "AnalysisCase._Cast_AnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6083,
            )

            return self._parent._cast(_6083.ModalAnalysisForHarmonicAnalysis)

        @property
        def dynamic_analysis(self: "AnalysisCase._Cast_AnalysisCase"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6326

            return self._parent._cast(_6326.DynamicAnalysis)

        @property
        def critical_speed_analysis(self: "AnalysisCase._Cast_AnalysisCase"):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6580,
            )

            return self._parent._cast(_6580.CriticalSpeedAnalysis)

        @property
        def advanced_time_stepping_analysis_for_modulation(
            self: "AnalysisCase._Cast_AnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7007,
            )

            return self._parent._cast(_7007.AdvancedTimeSteppingAnalysisForModulation)

        @property
        def advanced_system_deflection(self: "AnalysisCase._Cast_AnalysisCase"):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7271,
            )

            return self._parent._cast(_7271.AdvancedSystemDeflection)

        @property
        def advanced_system_deflection_sub_analysis(
            self: "AnalysisCase._Cast_AnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7273,
            )

            return self._parent._cast(_7273.AdvancedSystemDeflectionSubAnalysis)

        @property
        def compound_analysis_case(self: "AnalysisCase._Cast_AnalysisCase"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.CompoundAnalysisCase)

        @property
        def fe_analysis(self: "AnalysisCase._Cast_AnalysisCase"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.FEAnalysis)

        @property
        def static_load_analysis_case(self: "AnalysisCase._Cast_AnalysisCase"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.StaticLoadAnalysisCase)

        @property
        def time_series_load_analysis_case(self: "AnalysisCase._Cast_AnalysisCase"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.TimeSeriesLoadAnalysisCase)

        @property
        def analysis_case(self: "AnalysisCase._Cast_AnalysisCase") -> "AnalysisCase":
            return self._parent

        def __getattr__(self: "AnalysisCase._Cast_AnalysisCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AnalysisCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def analysis_setup_time(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AnalysisSetupTime

        if temp is None:
            return 0.0

        return temp

    @property
    def load_case_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadCaseName

        if temp is None:
            return ""

        return temp

    @property
    def analysis_run_information(self: Self) -> "_1576.AnalysisRunInformation":
        """mastapy.utility.AnalysisRunInformation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AnalysisRunInformation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def results_ready(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResultsReady

        if temp is None:
            return False

        return temp

    @enforce_parameter_types
    def results_for(
        self: Self, design_entity: "_2201.DesignEntity"
    ) -> "_2649.DesignEntityAnalysis":
        """mastapy.system_model.analyses_and_results.DesignEntityAnalysis

        Args:
            design_entity (mastapy.system_model.DesignEntity)
        """
        method_result = self.wrapped.ResultsFor(
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def perform_analysis(self: Self):
        """Method does not return."""
        self.wrapped.PerformAnalysis()

    @property
    def cast_to(self: Self) -> "AnalysisCase._Cast_AnalysisCase":
        return self._Cast_AnalysisCase(self)
