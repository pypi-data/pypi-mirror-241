"""PartToPartShearCouplingConnectionCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5914
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_CONNECTION_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "PartToPartShearCouplingConnectionCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2346
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5786


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingConnectionCompoundHarmonicAnalysis",)


Self = TypeVar(
    "Self", bound="PartToPartShearCouplingConnectionCompoundHarmonicAnalysis"
)


class PartToPartShearCouplingConnectionCompoundHarmonicAnalysis(
    _5914.CouplingConnectionCompoundHarmonicAnalysis
):
    """PartToPartShearCouplingConnectionCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_CONNECTION_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PartToPartShearCouplingConnectionCompoundHarmonicAnalysis",
    )

    class _Cast_PartToPartShearCouplingConnectionCompoundHarmonicAnalysis:
        """Special nested class for casting PartToPartShearCouplingConnectionCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingConnectionCompoundHarmonicAnalysis._Cast_PartToPartShearCouplingConnectionCompoundHarmonicAnalysis",
            parent: "PartToPartShearCouplingConnectionCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_harmonic_analysis(
            self: "PartToPartShearCouplingConnectionCompoundHarmonicAnalysis._Cast_PartToPartShearCouplingConnectionCompoundHarmonicAnalysis",
        ):
            return self._parent._cast(_5914.CouplingConnectionCompoundHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis(
            self: "PartToPartShearCouplingConnectionCompoundHarmonicAnalysis._Cast_PartToPartShearCouplingConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5941,
            )

            return self._parent._cast(
                _5941.InterMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def connection_compound_harmonic_analysis(
            self: "PartToPartShearCouplingConnectionCompoundHarmonicAnalysis._Cast_PartToPartShearCouplingConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5911,
            )

            return self._parent._cast(_5911.ConnectionCompoundHarmonicAnalysis)

        @property
        def connection_compound_analysis(
            self: "PartToPartShearCouplingConnectionCompoundHarmonicAnalysis._Cast_PartToPartShearCouplingConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartToPartShearCouplingConnectionCompoundHarmonicAnalysis._Cast_PartToPartShearCouplingConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingConnectionCompoundHarmonicAnalysis._Cast_PartToPartShearCouplingConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_connection_compound_harmonic_analysis(
            self: "PartToPartShearCouplingConnectionCompoundHarmonicAnalysis._Cast_PartToPartShearCouplingConnectionCompoundHarmonicAnalysis",
        ) -> "PartToPartShearCouplingConnectionCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingConnectionCompoundHarmonicAnalysis._Cast_PartToPartShearCouplingConnectionCompoundHarmonicAnalysis",
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
        instance_to_wrap: "PartToPartShearCouplingConnectionCompoundHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2346.PartToPartShearCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2346.PartToPartShearCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5786.PartToPartShearCouplingConnectionHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.PartToPartShearCouplingConnectionHarmonicAnalysis]

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
    ) -> "List[_5786.PartToPartShearCouplingConnectionHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.PartToPartShearCouplingConnectionHarmonicAnalysis]

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
    ) -> "PartToPartShearCouplingConnectionCompoundHarmonicAnalysis._Cast_PartToPartShearCouplingConnectionCompoundHarmonicAnalysis":
        return self._Cast_PartToPartShearCouplingConnectionCompoundHarmonicAnalysis(
            self
        )
