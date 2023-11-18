"""CVTBeltConnectionCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5885
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "CVTBeltConnectionCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5717


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnectionCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="CVTBeltConnectionCompoundHarmonicAnalysis")


class CVTBeltConnectionCompoundHarmonicAnalysis(
    _5885.BeltConnectionCompoundHarmonicAnalysis
):
    """CVTBeltConnectionCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTBeltConnectionCompoundHarmonicAnalysis"
    )

    class _Cast_CVTBeltConnectionCompoundHarmonicAnalysis:
        """Special nested class for casting CVTBeltConnectionCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "CVTBeltConnectionCompoundHarmonicAnalysis._Cast_CVTBeltConnectionCompoundHarmonicAnalysis",
            parent: "CVTBeltConnectionCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def belt_connection_compound_harmonic_analysis(
            self: "CVTBeltConnectionCompoundHarmonicAnalysis._Cast_CVTBeltConnectionCompoundHarmonicAnalysis",
        ):
            return self._parent._cast(_5885.BeltConnectionCompoundHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis(
            self: "CVTBeltConnectionCompoundHarmonicAnalysis._Cast_CVTBeltConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5941,
            )

            return self._parent._cast(
                _5941.InterMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def connection_compound_harmonic_analysis(
            self: "CVTBeltConnectionCompoundHarmonicAnalysis._Cast_CVTBeltConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5911,
            )

            return self._parent._cast(_5911.ConnectionCompoundHarmonicAnalysis)

        @property
        def connection_compound_analysis(
            self: "CVTBeltConnectionCompoundHarmonicAnalysis._Cast_CVTBeltConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTBeltConnectionCompoundHarmonicAnalysis._Cast_CVTBeltConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTBeltConnectionCompoundHarmonicAnalysis._Cast_CVTBeltConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_compound_harmonic_analysis(
            self: "CVTBeltConnectionCompoundHarmonicAnalysis._Cast_CVTBeltConnectionCompoundHarmonicAnalysis",
        ) -> "CVTBeltConnectionCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTBeltConnectionCompoundHarmonicAnalysis._Cast_CVTBeltConnectionCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "CVTBeltConnectionCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5717.CVTBeltConnectionHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.CVTBeltConnectionHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5717.CVTBeltConnectionHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.CVTBeltConnectionHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CVTBeltConnectionCompoundHarmonicAnalysis._Cast_CVTBeltConnectionCompoundHarmonicAnalysis":
        return self._Cast_CVTBeltConnectionCompoundHarmonicAnalysis(self)
