"""PulleyHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5715
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PULLEY_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "PulleyHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2588
    from mastapy.system_model.analyses_and_results.static_loads import _6938
    from mastapy.system_model.analyses_and_results.system_deflections import _2791


__docformat__ = "restructuredtext en"
__all__ = ("PulleyHarmonicAnalysis",)


Self = TypeVar("Self", bound="PulleyHarmonicAnalysis")


class PulleyHarmonicAnalysis(_5715.CouplingHalfHarmonicAnalysis):
    """PulleyHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _PULLEY_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PulleyHarmonicAnalysis")

    class _Cast_PulleyHarmonicAnalysis:
        """Special nested class for casting PulleyHarmonicAnalysis to subclasses."""

        def __init__(
            self: "PulleyHarmonicAnalysis._Cast_PulleyHarmonicAnalysis",
            parent: "PulleyHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_harmonic_analysis(
            self: "PulleyHarmonicAnalysis._Cast_PulleyHarmonicAnalysis",
        ):
            return self._parent._cast(_5715.CouplingHalfHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "PulleyHarmonicAnalysis._Cast_PulleyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5783,
            )

            return self._parent._cast(_5783.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "PulleyHarmonicAnalysis._Cast_PulleyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5702,
            )

            return self._parent._cast(_5702.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "PulleyHarmonicAnalysis._Cast_PulleyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5785,
            )

            return self._parent._cast(_5785.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PulleyHarmonicAnalysis._Cast_PulleyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PulleyHarmonicAnalysis._Cast_PulleyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(self: "PulleyHarmonicAnalysis._Cast_PulleyHarmonicAnalysis"):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PulleyHarmonicAnalysis._Cast_PulleyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PulleyHarmonicAnalysis._Cast_PulleyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cvt_pulley_harmonic_analysis(
            self: "PulleyHarmonicAnalysis._Cast_PulleyHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5719,
            )

            return self._parent._cast(_5719.CVTPulleyHarmonicAnalysis)

        @property
        def pulley_harmonic_analysis(
            self: "PulleyHarmonicAnalysis._Cast_PulleyHarmonicAnalysis",
        ) -> "PulleyHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "PulleyHarmonicAnalysis._Cast_PulleyHarmonicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PulleyHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2588.Pulley":
        """mastapy.system_model.part_model.couplings.Pulley

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6938.PulleyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PulleyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2791.PulleySystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.PulleySystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "PulleyHarmonicAnalysis._Cast_PulleyHarmonicAnalysis":
        return self._Cast_PulleyHarmonicAnalysis(self)
