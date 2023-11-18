"""SynchroniserPartAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7047,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "SynchroniserPartAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2603
    from mastapy.system_model.analyses_and_results.system_deflections import _2820


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="SynchroniserPartAdvancedTimeSteppingAnalysisForModulation"
)


class SynchroniserPartAdvancedTimeSteppingAnalysisForModulation(
    _7047.CouplingHalfAdvancedTimeSteppingAnalysisForModulation
):
    """SynchroniserPartAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SynchroniserPartAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_SynchroniserPartAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting SynchroniserPartAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "SynchroniserPartAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserPartAdvancedTimeSteppingAnalysisForModulation",
            parent: "SynchroniserPartAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def coupling_half_advanced_time_stepping_analysis_for_modulation(
            self: "SynchroniserPartAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserPartAdvancedTimeSteppingAnalysisForModulation",
        ):
            return self._parent._cast(
                _7047.CouplingHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(
            self: "SynchroniserPartAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserPartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7086,
            )

            return self._parent._cast(
                _7086.MountableComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "SynchroniserPartAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserPartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7033,
            )

            return self._parent._cast(
                _7033.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "SynchroniserPartAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserPartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7088,
            )

            return self._parent._cast(
                _7088.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserPartAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserPartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserPartAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserPartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserPartAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserPartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserPartAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserPartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserPartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def synchroniser_half_advanced_time_stepping_analysis_for_modulation(
            self: "SynchroniserPartAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserPartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7123,
            )

            return self._parent._cast(
                _7123.SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_sleeve_advanced_time_stepping_analysis_for_modulation(
            self: "SynchroniserPartAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserPartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7125,
            )

            return self._parent._cast(
                _7125.SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_part_advanced_time_stepping_analysis_for_modulation(
            self: "SynchroniserPartAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserPartAdvancedTimeSteppingAnalysisForModulation",
        ) -> "SynchroniserPartAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserPartAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "SynchroniserPartAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2603.SynchroniserPart":
        """mastapy.system_model.part_model.couplings.SynchroniserPart

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2820.SynchroniserPartSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.SynchroniserPartSystemDeflection

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
    ) -> "SynchroniserPartAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserPartAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_SynchroniserPartAdvancedTimeSteppingAnalysisForModulation(
            self
        )
