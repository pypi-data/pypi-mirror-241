"""AbstractShaftHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5678
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "AbstractShaftHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2433
    from mastapy.system_model.analyses_and_results.system_deflections import _2685


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftHarmonicAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftHarmonicAnalysis")


class AbstractShaftHarmonicAnalysis(_5678.AbstractShaftOrHousingHarmonicAnalysis):
    """AbstractShaftHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractShaftHarmonicAnalysis")

    class _Cast_AbstractShaftHarmonicAnalysis:
        """Special nested class for casting AbstractShaftHarmonicAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftHarmonicAnalysis._Cast_AbstractShaftHarmonicAnalysis",
            parent: "AbstractShaftHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_harmonic_analysis(
            self: "AbstractShaftHarmonicAnalysis._Cast_AbstractShaftHarmonicAnalysis",
        ):
            return self._parent._cast(_5678.AbstractShaftOrHousingHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "AbstractShaftHarmonicAnalysis._Cast_AbstractShaftHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5702,
            )

            return self._parent._cast(_5702.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "AbstractShaftHarmonicAnalysis._Cast_AbstractShaftHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5785,
            )

            return self._parent._cast(_5785.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftHarmonicAnalysis._Cast_AbstractShaftHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftHarmonicAnalysis._Cast_AbstractShaftHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftHarmonicAnalysis._Cast_AbstractShaftHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftHarmonicAnalysis._Cast_AbstractShaftHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftHarmonicAnalysis._Cast_AbstractShaftHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cycloidal_disc_harmonic_analysis(
            self: "AbstractShaftHarmonicAnalysis._Cast_AbstractShaftHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5722,
            )

            return self._parent._cast(_5722.CycloidalDiscHarmonicAnalysis)

        @property
        def shaft_harmonic_analysis(
            self: "AbstractShaftHarmonicAnalysis._Cast_AbstractShaftHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5803,
            )

            return self._parent._cast(_5803.ShaftHarmonicAnalysis)

        @property
        def abstract_shaft_harmonic_analysis(
            self: "AbstractShaftHarmonicAnalysis._Cast_AbstractShaftHarmonicAnalysis",
        ) -> "AbstractShaftHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftHarmonicAnalysis._Cast_AbstractShaftHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractShaftHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2433.AbstractShaft":
        """mastapy.system_model.part_model.AbstractShaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2685.AbstractShaftSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.AbstractShaftSystemDeflection

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
    ) -> "AbstractShaftHarmonicAnalysis._Cast_AbstractShaftHarmonicAnalysis":
        return self._Cast_AbstractShaftHarmonicAnalysis(self)
