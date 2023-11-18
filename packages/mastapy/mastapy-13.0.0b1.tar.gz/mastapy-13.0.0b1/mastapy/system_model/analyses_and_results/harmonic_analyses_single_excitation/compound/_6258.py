"""VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6213,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6129,
    )


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation"
)


class VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation(
    _6213.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
):
    """VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(
                _6213.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_compound_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6161,
            )

            return self._parent._cast(
                _6161.ComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6215,
            )

            return self._parent._cast(
                _6215.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def mass_disc_compound_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6211,
            )

            return self._parent._cast(
                _6211.MassDiscCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def measurement_component_compound_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6212,
            )

            return self._parent._cast(
                _6212.MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def point_load_compound_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6222,
            )

            return self._parent._cast(
                _6222.PointLoadCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def power_load_compound_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6223,
            )

            return self._parent._cast(
                _6223.PowerLoadCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def unbalanced_mass_compound_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6257,
            )

            return self._parent._cast(
                _6257.UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def virtual_component_compound_harmonic_analysis_of_single_excitation(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6129.VirtualComponentHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.VirtualComponentHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6129.VirtualComponentHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.VirtualComponentHarmonicAnalysisOfSingleExcitation]

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
    ) -> "VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation(
            self
        )
