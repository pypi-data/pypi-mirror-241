"""SynchroniserAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7107,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "SynchroniserAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2600
    from mastapy.system_model.analyses_and_results.static_loads import _6966
    from mastapy.system_model.analyses_and_results.system_deflections import _2822


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="SynchroniserAdvancedTimeSteppingAnalysisForModulation")


class SynchroniserAdvancedTimeSteppingAnalysisForModulation(
    _7107.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
):
    """SynchroniserAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserAdvancedTimeSteppingAnalysisForModulation"
    )

    class _Cast_SynchroniserAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting SynchroniserAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "SynchroniserAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserAdvancedTimeSteppingAnalysisForModulation",
            parent: "SynchroniserAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def specialised_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "SynchroniserAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserAdvancedTimeSteppingAnalysisForModulation",
        ):
            return self._parent._cast(
                _7107.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "SynchroniserAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7003,
            )

            return self._parent._cast(
                _7003.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "SynchroniserAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7088,
            )

            return self._parent._cast(
                _7088.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def synchroniser_advanced_time_stepping_analysis_for_modulation(
            self: "SynchroniserAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserAdvancedTimeSteppingAnalysisForModulation",
        ) -> "SynchroniserAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "SynchroniserAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserAdvancedTimeSteppingAnalysisForModulation",
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
        self: Self,
        instance_to_wrap: "SynchroniserAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2600.Synchroniser":
        """mastapy.system_model.part_model.couplings.Synchroniser

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6966.SynchroniserLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2822.SynchroniserSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.SynchroniserSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SynchroniserAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_SynchroniserAdvancedTimeSteppingAnalysisForModulation(self)
