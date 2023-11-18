"""FlexiblePinAssemblyCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6770,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "FlexiblePinAssemblyCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2452
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6600


__docformat__ = "restructuredtext en"
__all__ = ("FlexiblePinAssemblyCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="FlexiblePinAssemblyCompoundCriticalSpeedAnalysis")


class FlexiblePinAssemblyCompoundCriticalSpeedAnalysis(
    _6770.SpecialisedAssemblyCompoundCriticalSpeedAnalysis
):
    """FlexiblePinAssemblyCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ASSEMBLY_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FlexiblePinAssemblyCompoundCriticalSpeedAnalysis"
    )

    class _Cast_FlexiblePinAssemblyCompoundCriticalSpeedAnalysis:
        """Special nested class for casting FlexiblePinAssemblyCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "FlexiblePinAssemblyCompoundCriticalSpeedAnalysis._Cast_FlexiblePinAssemblyCompoundCriticalSpeedAnalysis",
            parent: "FlexiblePinAssemblyCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_critical_speed_analysis(
            self: "FlexiblePinAssemblyCompoundCriticalSpeedAnalysis._Cast_FlexiblePinAssemblyCompoundCriticalSpeedAnalysis",
        ):
            return self._parent._cast(
                _6770.SpecialisedAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def abstract_assembly_compound_critical_speed_analysis(
            self: "FlexiblePinAssemblyCompoundCriticalSpeedAnalysis._Cast_FlexiblePinAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6672,
            )

            return self._parent._cast(
                _6672.AbstractAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def part_compound_critical_speed_analysis(
            self: "FlexiblePinAssemblyCompoundCriticalSpeedAnalysis._Cast_FlexiblePinAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6751,
            )

            return self._parent._cast(_6751.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "FlexiblePinAssemblyCompoundCriticalSpeedAnalysis._Cast_FlexiblePinAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "FlexiblePinAssemblyCompoundCriticalSpeedAnalysis._Cast_FlexiblePinAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "FlexiblePinAssemblyCompoundCriticalSpeedAnalysis._Cast_FlexiblePinAssemblyCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def flexible_pin_assembly_compound_critical_speed_analysis(
            self: "FlexiblePinAssemblyCompoundCriticalSpeedAnalysis._Cast_FlexiblePinAssemblyCompoundCriticalSpeedAnalysis",
        ) -> "FlexiblePinAssemblyCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "FlexiblePinAssemblyCompoundCriticalSpeedAnalysis._Cast_FlexiblePinAssemblyCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "FlexiblePinAssemblyCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2452.FlexiblePinAssembly":
        """mastapy.system_model.part_model.FlexiblePinAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2452.FlexiblePinAssembly":
        """mastapy.system_model.part_model.FlexiblePinAssembly

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
    ) -> "List[_6600.FlexiblePinAssemblyCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.FlexiblePinAssemblyCriticalSpeedAnalysis]

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
    ) -> "List[_6600.FlexiblePinAssemblyCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.FlexiblePinAssemblyCriticalSpeedAnalysis]

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
    ) -> "FlexiblePinAssemblyCompoundCriticalSpeedAnalysis._Cast_FlexiblePinAssemblyCompoundCriticalSpeedAnalysis":
        return self._Cast_FlexiblePinAssemblyCompoundCriticalSpeedAnalysis(self)
