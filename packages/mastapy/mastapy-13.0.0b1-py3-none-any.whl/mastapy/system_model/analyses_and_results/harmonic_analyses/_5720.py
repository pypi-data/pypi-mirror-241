"""CycloidalAssemblyHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5807
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_ASSEMBLY_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "CycloidalAssemblyHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2566
    from mastapy.system_model.analyses_and_results.static_loads import _6855
    from mastapy.system_model.analyses_and_results.system_deflections import _2733


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalAssemblyHarmonicAnalysis",)


Self = TypeVar("Self", bound="CycloidalAssemblyHarmonicAnalysis")


class CycloidalAssemblyHarmonicAnalysis(_5807.SpecialisedAssemblyHarmonicAnalysis):
    """CycloidalAssemblyHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_ASSEMBLY_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CycloidalAssemblyHarmonicAnalysis")

    class _Cast_CycloidalAssemblyHarmonicAnalysis:
        """Special nested class for casting CycloidalAssemblyHarmonicAnalysis to subclasses."""

        def __init__(
            self: "CycloidalAssemblyHarmonicAnalysis._Cast_CycloidalAssemblyHarmonicAnalysis",
            parent: "CycloidalAssemblyHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_harmonic_analysis(
            self: "CycloidalAssemblyHarmonicAnalysis._Cast_CycloidalAssemblyHarmonicAnalysis",
        ):
            return self._parent._cast(_5807.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(
            self: "CycloidalAssemblyHarmonicAnalysis._Cast_CycloidalAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5675,
            )

            return self._parent._cast(_5675.AbstractAssemblyHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "CycloidalAssemblyHarmonicAnalysis._Cast_CycloidalAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5785,
            )

            return self._parent._cast(_5785.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CycloidalAssemblyHarmonicAnalysis._Cast_CycloidalAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CycloidalAssemblyHarmonicAnalysis._Cast_CycloidalAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CycloidalAssemblyHarmonicAnalysis._Cast_CycloidalAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalAssemblyHarmonicAnalysis._Cast_CycloidalAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalAssemblyHarmonicAnalysis._Cast_CycloidalAssemblyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cycloidal_assembly_harmonic_analysis(
            self: "CycloidalAssemblyHarmonicAnalysis._Cast_CycloidalAssemblyHarmonicAnalysis",
        ) -> "CycloidalAssemblyHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalAssemblyHarmonicAnalysis._Cast_CycloidalAssemblyHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "CycloidalAssemblyHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2566.CycloidalAssembly":
        """mastapy.system_model.part_model.cycloidal.CycloidalAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6855.CycloidalAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalAssemblyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2733.CycloidalAssemblySystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CycloidalAssemblySystemDeflection

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
    ) -> "CycloidalAssemblyHarmonicAnalysis._Cast_CycloidalAssemblyHarmonicAnalysis":
        return self._Cast_CycloidalAssemblyHarmonicAnalysis(self)
