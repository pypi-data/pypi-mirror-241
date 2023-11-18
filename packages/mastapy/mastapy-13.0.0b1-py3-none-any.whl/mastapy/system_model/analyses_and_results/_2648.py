"""Context"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONTEXT = python_net_import("SMT.MastaAPI.SystemModel.AnalysesAndResults", "Context")

if TYPE_CHECKING:
    from mastapy.utility import _1581
    from mastapy.system_model import _2198


__docformat__ = "restructuredtext en"
__all__ = ("Context",)


Self = TypeVar("Self", bound="Context")


class Context(_0.APIBase):
    """Context

    This is a mastapy class.
    """

    TYPE = _CONTEXT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Context")

    class _Cast_Context:
        """Special nested class for casting Context to subclasses."""

        def __init__(self: "Context._Cast_Context", parent: "Context"):
            self._parent = parent

        @property
        def system_deflection(self: "Context._Cast_Context"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2823,
            )

            return self._parent._cast(_2823.SystemDeflection)

        @property
        def torsional_system_deflection(self: "Context._Cast_Context"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2830,
            )

            return self._parent._cast(_2830.TorsionalSystemDeflection)

        @property
        def dynamic_model_for_steady_state_synchronous_response(
            self: "Context._Cast_Context",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3033,
            )

            return self._parent._cast(
                _3033.DynamicModelForSteadyStateSynchronousResponse
            )

        @property
        def steady_state_synchronous_response(self: "Context._Cast_Context"):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3087,
            )

            return self._parent._cast(_3087.SteadyStateSynchronousResponse)

        @property
        def steady_state_synchronous_response_on_a_shaft(self: "Context._Cast_Context"):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3348,
            )

            return self._parent._cast(_3348.SteadyStateSynchronousResponseOnAShaft)

        @property
        def steady_state_synchronous_response_at_a_speed(self: "Context._Cast_Context"):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3607,
            )

            return self._parent._cast(_3607.SteadyStateSynchronousResponseAtASpeed)

        @property
        def dynamic_model_for_stability_analysis(self: "Context._Cast_Context"):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3814,
            )

            return self._parent._cast(_3814.DynamicModelForStabilityAnalysis)

        @property
        def stability_analysis(self: "Context._Cast_Context"):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3868,
            )

            return self._parent._cast(_3868.StabilityAnalysis)

        @property
        def power_flow(self: "Context._Cast_Context"):
            from mastapy.system_model.analyses_and_results.power_flows import _4119

            return self._parent._cast(_4119.PowerFlow)

        @property
        def parametric_study_static_load(self: "Context._Cast_Context"):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4384,
            )

            return self._parent._cast(_4384.ParametricStudyStaticLoad)

        @property
        def parametric_study_tool(self: "Context._Cast_Context"):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4385,
            )

            return self._parent._cast(_4385.ParametricStudyTool)

        @property
        def dynamic_model_for_modal_analysis(self: "Context._Cast_Context"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4622

            return self._parent._cast(_4622.DynamicModelForModalAnalysis)

        @property
        def modal_analysis(self: "Context._Cast_Context"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4651

            return self._parent._cast(_4651.ModalAnalysis)

        @property
        def dynamic_model_at_a_stiffness(self: "Context._Cast_Context"):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4906,
            )

            return self._parent._cast(_4906.DynamicModelAtAStiffness)

        @property
        def modal_analysis_at_a_stiffness(self: "Context._Cast_Context"):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4932,
            )

            return self._parent._cast(_4932.ModalAnalysisAtAStiffness)

        @property
        def modal_analysis_at_a_speed(self: "Context._Cast_Context"):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5191,
            )

            return self._parent._cast(_5191.ModalAnalysisAtASpeed)

        @property
        def multibody_dynamics_analysis(self: "Context._Cast_Context"):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5462

            return self._parent._cast(_5462.MultibodyDynamicsAnalysis)

        @property
        def dynamic_model_for_harmonic_analysis(self: "Context._Cast_Context"):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5729,
            )

            return self._parent._cast(_5729.DynamicModelForHarmonicAnalysis)

        @property
        def harmonic_analysis(self: "Context._Cast_Context"):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5758,
            )

            return self._parent._cast(_5758.HarmonicAnalysis)

        @property
        def harmonic_analysis_for_advanced_time_stepping_analysis_for_modulation(
            self: "Context._Cast_Context",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5762,
            )

            return self._parent._cast(
                _5762.HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def harmonic_analysis_with_varying_stiffness_static_load_case(
            self: "Context._Cast_Context",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5767,
            )

            return self._parent._cast(
                _5767.HarmonicAnalysisWithVaryingStiffnessStaticLoadCase
            )

        @property
        def harmonic_analysis_of_single_excitation(self: "Context._Cast_Context"):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6067,
            )

            return self._parent._cast(_6067.HarmonicAnalysisOfSingleExcitation)

        @property
        def modal_analysis_for_harmonic_analysis(self: "Context._Cast_Context"):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6083,
            )

            return self._parent._cast(_6083.ModalAnalysisForHarmonicAnalysis)

        @property
        def dynamic_analysis(self: "Context._Cast_Context"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6326

            return self._parent._cast(_6326.DynamicAnalysis)

        @property
        def critical_speed_analysis(self: "Context._Cast_Context"):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6580,
            )

            return self._parent._cast(_6580.CriticalSpeedAnalysis)

        @property
        def load_case(self: "Context._Cast_Context"):
            from mastapy.system_model.analyses_and_results.static_loads import _6801

            return self._parent._cast(_6801.LoadCase)

        @property
        def static_load_case(self: "Context._Cast_Context"):
            from mastapy.system_model.analyses_and_results.static_loads import _6802

            return self._parent._cast(_6802.StaticLoadCase)

        @property
        def time_series_load_case(self: "Context._Cast_Context"):
            from mastapy.system_model.analyses_and_results.static_loads import _6803

            return self._parent._cast(_6803.TimeSeriesLoadCase)

        @property
        def advanced_time_stepping_analysis_for_modulation_static_load_case(
            self: "Context._Cast_Context",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6809

            return self._parent._cast(
                _6809.AdvancedTimeSteppingAnalysisForModulationStaticLoadCase
            )

        @property
        def advanced_time_stepping_analysis_for_modulation(
            self: "Context._Cast_Context",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7007,
            )

            return self._parent._cast(_7007.AdvancedTimeSteppingAnalysisForModulation)

        @property
        def advanced_system_deflection(self: "Context._Cast_Context"):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7271,
            )

            return self._parent._cast(_7271.AdvancedSystemDeflection)

        @property
        def advanced_system_deflection_sub_analysis(self: "Context._Cast_Context"):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7273,
            )

            return self._parent._cast(_7273.AdvancedSystemDeflectionSubAnalysis)

        @property
        def analysis_case(self: "Context._Cast_Context"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7532

            return self._parent._cast(_7532.AnalysisCase)

        @property
        def compound_analysis_case(self: "Context._Cast_Context"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.CompoundAnalysisCase)

        @property
        def fe_analysis(self: "Context._Cast_Context"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.FEAnalysis)

        @property
        def static_load_analysis_case(self: "Context._Cast_Context"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.StaticLoadAnalysisCase)

        @property
        def time_series_load_analysis_case(self: "Context._Cast_Context"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.TimeSeriesLoadAnalysisCase)

        @property
        def context(self: "Context._Cast_Context") -> "Context":
            return self._parent

        def __getattr__(self: "Context._Cast_Context", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Context.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def comment(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Comment

        if temp is None:
            return ""

        return temp

    @comment.setter
    @enforce_parameter_types
    def comment(self: Self, value: "str"):
        self.wrapped.Comment = str(value) if value is not None else ""

    @property
    def name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: Self, value: "str"):
        self.wrapped.Name = str(value) if value is not None else ""

    @property
    def save_history_information(self: Self) -> "_1581.FileHistoryItem":
        """mastapy.utility.FileHistoryItem

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SaveHistoryInformation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def design_properties(self: Self) -> "_2198.Design":
        """mastapy.system_model.Design

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DesignProperties

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(self: Self) -> "Context._Cast_Context":
        return self._Cast_Context(self)
