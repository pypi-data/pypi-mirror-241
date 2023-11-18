"""ConceptCouplingConnectionHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5714
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ConceptCouplingConnectionHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2342
    from mastapy.system_model.analyses_and_results.static_loads import _6836
    from mastapy.system_model.analyses_and_results.system_deflections import _2715


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingConnectionHarmonicAnalysis",)


Self = TypeVar("Self", bound="ConceptCouplingConnectionHarmonicAnalysis")


class ConceptCouplingConnectionHarmonicAnalysis(
    _5714.CouplingConnectionHarmonicAnalysis
):
    """ConceptCouplingConnectionHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_CONNECTION_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingConnectionHarmonicAnalysis"
    )

    class _Cast_ConceptCouplingConnectionHarmonicAnalysis:
        """Special nested class for casting ConceptCouplingConnectionHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ConceptCouplingConnectionHarmonicAnalysis._Cast_ConceptCouplingConnectionHarmonicAnalysis",
            parent: "ConceptCouplingConnectionHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_harmonic_analysis(
            self: "ConceptCouplingConnectionHarmonicAnalysis._Cast_ConceptCouplingConnectionHarmonicAnalysis",
        ):
            return self._parent._cast(_5714.CouplingConnectionHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_harmonic_analysis(
            self: "ConceptCouplingConnectionHarmonicAnalysis._Cast_ConceptCouplingConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5771,
            )

            return self._parent._cast(
                _5771.InterMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def connection_harmonic_analysis(
            self: "ConceptCouplingConnectionHarmonicAnalysis._Cast_ConceptCouplingConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5712,
            )

            return self._parent._cast(_5712.ConnectionHarmonicAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "ConceptCouplingConnectionHarmonicAnalysis._Cast_ConceptCouplingConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConceptCouplingConnectionHarmonicAnalysis._Cast_ConceptCouplingConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConceptCouplingConnectionHarmonicAnalysis._Cast_ConceptCouplingConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2647

            return self._parent._cast(_2647.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingConnectionHarmonicAnalysis._Cast_ConceptCouplingConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingConnectionHarmonicAnalysis._Cast_ConceptCouplingConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def concept_coupling_connection_harmonic_analysis(
            self: "ConceptCouplingConnectionHarmonicAnalysis._Cast_ConceptCouplingConnectionHarmonicAnalysis",
        ) -> "ConceptCouplingConnectionHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingConnectionHarmonicAnalysis._Cast_ConceptCouplingConnectionHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "ConceptCouplingConnectionHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2342.ConceptCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6836.ConceptCouplingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2715.ConceptCouplingConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ConceptCouplingConnectionSystemDeflection

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
    ) -> "ConceptCouplingConnectionHarmonicAnalysis._Cast_ConceptCouplingConnectionHarmonicAnalysis":
        return self._Cast_ConceptCouplingConnectionHarmonicAnalysis(self)
