"""ClutchCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6709,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "ClutchCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2576
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6562


__docformat__ = "restructuredtext en"
__all__ = ("ClutchCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="ClutchCompoundCriticalSpeedAnalysis")


class ClutchCompoundCriticalSpeedAnalysis(_6709.CouplingCompoundCriticalSpeedAnalysis):
    """ClutchCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CLUTCH_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClutchCompoundCriticalSpeedAnalysis")

    class _Cast_ClutchCompoundCriticalSpeedAnalysis:
        """Special nested class for casting ClutchCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "ClutchCompoundCriticalSpeedAnalysis._Cast_ClutchCompoundCriticalSpeedAnalysis",
            parent: "ClutchCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_compound_critical_speed_analysis(
            self: "ClutchCompoundCriticalSpeedAnalysis._Cast_ClutchCompoundCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6709.CouplingCompoundCriticalSpeedAnalysis)

        @property
        def specialised_assembly_compound_critical_speed_analysis(
            self: "ClutchCompoundCriticalSpeedAnalysis._Cast_ClutchCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6770,
            )

            return self._parent._cast(
                _6770.SpecialisedAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def abstract_assembly_compound_critical_speed_analysis(
            self: "ClutchCompoundCriticalSpeedAnalysis._Cast_ClutchCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6672,
            )

            return self._parent._cast(
                _6672.AbstractAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def part_compound_critical_speed_analysis(
            self: "ClutchCompoundCriticalSpeedAnalysis._Cast_ClutchCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6751,
            )

            return self._parent._cast(_6751.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "ClutchCompoundCriticalSpeedAnalysis._Cast_ClutchCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ClutchCompoundCriticalSpeedAnalysis._Cast_ClutchCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchCompoundCriticalSpeedAnalysis._Cast_ClutchCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def clutch_compound_critical_speed_analysis(
            self: "ClutchCompoundCriticalSpeedAnalysis._Cast_ClutchCompoundCriticalSpeedAnalysis",
        ) -> "ClutchCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "ClutchCompoundCriticalSpeedAnalysis._Cast_ClutchCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "ClutchCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2576.Clutch":
        """mastapy.system_model.part_model.couplings.Clutch

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2576.Clutch":
        """mastapy.system_model.part_model.couplings.Clutch

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_6562.ClutchCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ClutchCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6562.ClutchCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ClutchCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> (
        "ClutchCompoundCriticalSpeedAnalysis._Cast_ClutchCompoundCriticalSpeedAnalysis"
    ):
        return self._Cast_ClutchCompoundCriticalSpeedAnalysis(self)
