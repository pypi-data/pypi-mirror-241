"""CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7215,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7047,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation"
)


class CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7215.MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            return self._parent._cast(
                _7215.MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7163,
            )

            return self._parent._cast(
                _7163.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7217,
            )

            return self._parent._cast(
                _7217.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_analysis(
            self: "CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def clutch_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7161,
            )

            return self._parent._cast(
                _7161.ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7166,
            )

            return self._parent._cast(
                _7166.ConceptCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_pulley_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7180,
            )

            return self._parent._cast(
                _7180.CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7220,
            )

            return self._parent._cast(
                _7220.PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def pulley_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7226,
            )

            return self._parent._cast(
                _7226.PulleyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7230,
            )

            return self._parent._cast(
                _7230.RollingRingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7242,
            )

            return self._parent._cast(
                _7242.SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7252,
            )

            return self._parent._cast(
                _7252.SynchroniserHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7253,
            )

            return self._parent._cast(
                _7253.SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_sleeve_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7254,
            )

            return self._parent._cast(
                _7254.SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_pump_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7257,
            )

            return self._parent._cast(
                _7257.TorqueConverterPumpCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_turbine_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7258,
            )

            return self._parent._cast(
                _7258.TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7047.CouplingHalfAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.CouplingHalfAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_7047.CouplingHalfAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.CouplingHalfAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
