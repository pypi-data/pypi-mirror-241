"""SynchroniserSleeveHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6122,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "SynchroniserSleeveHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2604
    from mastapy.system_model.analyses_and_results.static_loads import _6968


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserSleeveHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="SynchroniserSleeveHarmonicAnalysisOfSingleExcitation")


class SynchroniserSleeveHarmonicAnalysisOfSingleExcitation(
    _6122.SynchroniserPartHarmonicAnalysisOfSingleExcitation
):
    """SynchroniserSleeveHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserSleeveHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_SynchroniserSleeveHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting SynchroniserSleeveHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "SynchroniserSleeveHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserSleeveHarmonicAnalysisOfSingleExcitation",
            parent: "SynchroniserSleeveHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def synchroniser_part_harmonic_analysis_of_single_excitation(
            self: "SynchroniserSleeveHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserSleeveHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(
                _6122.SynchroniserPartHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_half_harmonic_analysis_of_single_excitation(
            self: "SynchroniserSleeveHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserSleeveHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6043,
            )

            return self._parent._cast(
                _6043.CouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "SynchroniserSleeveHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserSleeveHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6084,
            )

            return self._parent._cast(
                _6084.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "SynchroniserSleeveHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserSleeveHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6030,
            )

            return self._parent._cast(_6030.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "SynchroniserSleeveHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserSleeveHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6086,
            )

            return self._parent._cast(_6086.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserSleeveHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserSleeveHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserSleeveHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserSleeveHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserSleeveHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserSleeveHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserSleeveHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserSleeveHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserSleeveHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserSleeveHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def synchroniser_sleeve_harmonic_analysis_of_single_excitation(
            self: "SynchroniserSleeveHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserSleeveHarmonicAnalysisOfSingleExcitation",
        ) -> "SynchroniserSleeveHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "SynchroniserSleeveHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserSleeveHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "SynchroniserSleeveHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2604.SynchroniserSleeve":
        """mastapy.system_model.part_model.couplings.SynchroniserSleeve

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6968.SynchroniserSleeveLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SynchroniserSleeveHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserSleeveHarmonicAnalysisOfSingleExcitation":
        return self._Cast_SynchroniserSleeveHarmonicAnalysisOfSingleExcitation(self)
