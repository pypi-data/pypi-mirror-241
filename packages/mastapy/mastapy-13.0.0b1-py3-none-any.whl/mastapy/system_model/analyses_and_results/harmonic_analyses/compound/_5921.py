"""CycloidalDiscCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5877
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "CycloidalDiscCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2567
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5722


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="CycloidalDiscCompoundHarmonicAnalysis")


class CycloidalDiscCompoundHarmonicAnalysis(
    _5877.AbstractShaftCompoundHarmonicAnalysis
):
    """CycloidalDiscCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CycloidalDiscCompoundHarmonicAnalysis"
    )

    class _Cast_CycloidalDiscCompoundHarmonicAnalysis:
        """Special nested class for casting CycloidalDiscCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "CycloidalDiscCompoundHarmonicAnalysis._Cast_CycloidalDiscCompoundHarmonicAnalysis",
            parent: "CycloidalDiscCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_compound_harmonic_analysis(
            self: "CycloidalDiscCompoundHarmonicAnalysis._Cast_CycloidalDiscCompoundHarmonicAnalysis",
        ):
            return self._parent._cast(_5877.AbstractShaftCompoundHarmonicAnalysis)

        @property
        def abstract_shaft_or_housing_compound_harmonic_analysis(
            self: "CycloidalDiscCompoundHarmonicAnalysis._Cast_CycloidalDiscCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5878,
            )

            return self._parent._cast(
                _5878.AbstractShaftOrHousingCompoundHarmonicAnalysis
            )

        @property
        def component_compound_harmonic_analysis(
            self: "CycloidalDiscCompoundHarmonicAnalysis._Cast_CycloidalDiscCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5901,
            )

            return self._parent._cast(_5901.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "CycloidalDiscCompoundHarmonicAnalysis._Cast_CycloidalDiscCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5955,
            )

            return self._parent._cast(_5955.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "CycloidalDiscCompoundHarmonicAnalysis._Cast_CycloidalDiscCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscCompoundHarmonicAnalysis._Cast_CycloidalDiscCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCompoundHarmonicAnalysis._Cast_CycloidalDiscCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cycloidal_disc_compound_harmonic_analysis(
            self: "CycloidalDiscCompoundHarmonicAnalysis._Cast_CycloidalDiscCompoundHarmonicAnalysis",
        ) -> "CycloidalDiscCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCompoundHarmonicAnalysis._Cast_CycloidalDiscCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "CycloidalDiscCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2567.CycloidalDisc":
        """mastapy.system_model.part_model.cycloidal.CycloidalDisc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5722.CycloidalDiscHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.CycloidalDiscHarmonicAnalysis]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5722.CycloidalDiscHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.CycloidalDiscHarmonicAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscCompoundHarmonicAnalysis._Cast_CycloidalDiscCompoundHarmonicAnalysis":
        return self._Cast_CycloidalDiscCompoundHarmonicAnalysis(self)
