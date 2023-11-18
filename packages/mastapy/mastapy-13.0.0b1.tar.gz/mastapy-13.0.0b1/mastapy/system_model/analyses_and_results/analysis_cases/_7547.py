"""StaticLoadAnalysisCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7532
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STATIC_LOAD_ANALYSIS_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases",
    "StaticLoadAnalysisCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import _6802


__docformat__ = "restructuredtext en"
__all__ = ("StaticLoadAnalysisCase",)


Self = TypeVar("Self", bound="StaticLoadAnalysisCase")


class StaticLoadAnalysisCase(_7532.AnalysisCase):
    """StaticLoadAnalysisCase

    This is a mastapy class.
    """

    TYPE = _STATIC_LOAD_ANALYSIS_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StaticLoadAnalysisCase")

    class _Cast_StaticLoadAnalysisCase:
        """Special nested class for casting StaticLoadAnalysisCase to subclasses."""

        def __init__(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
            parent: "StaticLoadAnalysisCase",
        ):
            self._parent = parent

        @property
        def analysis_case(self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase"):
            return self._parent._cast(_7532.AnalysisCase)

        @property
        def context(self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase"):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.Context)

        @property
        def system_deflection(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2823,
            )

            return self._parent._cast(_2823.SystemDeflection)

        @property
        def torsional_system_deflection(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2830,
            )

            return self._parent._cast(_2830.TorsionalSystemDeflection)

        @property
        def dynamic_model_for_steady_state_synchronous_response(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3033,
            )

            return self._parent._cast(
                _3033.DynamicModelForSteadyStateSynchronousResponse
            )

        @property
        def steady_state_synchronous_response(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3087,
            )

            return self._parent._cast(_3087.SteadyStateSynchronousResponse)

        @property
        def steady_state_synchronous_response_on_a_shaft(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3348,
            )

            return self._parent._cast(_3348.SteadyStateSynchronousResponseOnAShaft)

        @property
        def steady_state_synchronous_response_at_a_speed(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3607,
            )

            return self._parent._cast(_3607.SteadyStateSynchronousResponseAtASpeed)

        @property
        def dynamic_model_for_stability_analysis(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3814,
            )

            return self._parent._cast(_3814.DynamicModelForStabilityAnalysis)

        @property
        def stability_analysis(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3868,
            )

            return self._parent._cast(_3868.StabilityAnalysis)

        @property
        def power_flow(self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4119

            return self._parent._cast(_4119.PowerFlow)

        @property
        def dynamic_model_for_modal_analysis(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4622

            return self._parent._cast(_4622.DynamicModelForModalAnalysis)

        @property
        def modal_analysis(self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4651

            return self._parent._cast(_4651.ModalAnalysis)

        @property
        def dynamic_model_at_a_stiffness(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4906,
            )

            return self._parent._cast(_4906.DynamicModelAtAStiffness)

        @property
        def modal_analysis_at_a_stiffness(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4932,
            )

            return self._parent._cast(_4932.ModalAnalysisAtAStiffness)

        @property
        def modal_analysis_at_a_speed(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5191,
            )

            return self._parent._cast(_5191.ModalAnalysisAtASpeed)

        @property
        def dynamic_model_for_harmonic_analysis(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5729,
            )

            return self._parent._cast(_5729.DynamicModelForHarmonicAnalysis)

        @property
        def harmonic_analysis(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5758,
            )

            return self._parent._cast(_5758.HarmonicAnalysis)

        @property
        def harmonic_analysis_for_advanced_time_stepping_analysis_for_modulation(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5762,
            )

            return self._parent._cast(
                _5762.HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def harmonic_analysis_of_single_excitation(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6067,
            )

            return self._parent._cast(_6067.HarmonicAnalysisOfSingleExcitation)

        @property
        def modal_analysis_for_harmonic_analysis(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6083,
            )

            return self._parent._cast(_6083.ModalAnalysisForHarmonicAnalysis)

        @property
        def dynamic_analysis(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6326

            return self._parent._cast(_6326.DynamicAnalysis)

        @property
        def critical_speed_analysis(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6580,
            )

            return self._parent._cast(_6580.CriticalSpeedAnalysis)

        @property
        def advanced_time_stepping_analysis_for_modulation(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7007,
            )

            return self._parent._cast(_7007.AdvancedTimeSteppingAnalysisForModulation)

        @property
        def advanced_system_deflection(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7271,
            )

            return self._parent._cast(_7271.AdvancedSystemDeflection)

        @property
        def advanced_system_deflection_sub_analysis(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7273,
            )

            return self._parent._cast(_7273.AdvancedSystemDeflectionSubAnalysis)

        @property
        def compound_analysis_case(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.CompoundAnalysisCase)

        @property
        def fe_analysis(self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.FEAnalysis)

        @property
        def static_load_analysis_case(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase",
        ) -> "StaticLoadAnalysisCase":
            return self._parent

        def __getattr__(
            self: "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StaticLoadAnalysisCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def load_case(self: Self) -> "_6802.StaticLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "StaticLoadAnalysisCase._Cast_StaticLoadAnalysisCase":
        return self._Cast_StaticLoadAnalysisCase(self)
