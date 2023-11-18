"""OilSealHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6041,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OIL_SEAL_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "OilSealHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2464
    from mastapy.system_model.analyses_and_results.static_loads import _6924


__docformat__ = "restructuredtext en"
__all__ = ("OilSealHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="OilSealHarmonicAnalysisOfSingleExcitation")


class OilSealHarmonicAnalysisOfSingleExcitation(
    _6041.ConnectorHarmonicAnalysisOfSingleExcitation
):
    """OilSealHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _OIL_SEAL_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_OilSealHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_OilSealHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting OilSealHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "OilSealHarmonicAnalysisOfSingleExcitation._Cast_OilSealHarmonicAnalysisOfSingleExcitation",
            parent: "OilSealHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def connector_harmonic_analysis_of_single_excitation(
            self: "OilSealHarmonicAnalysisOfSingleExcitation._Cast_OilSealHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(_6041.ConnectorHarmonicAnalysisOfSingleExcitation)

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "OilSealHarmonicAnalysisOfSingleExcitation._Cast_OilSealHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6084,
            )

            return self._parent._cast(
                _6084.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "OilSealHarmonicAnalysisOfSingleExcitation._Cast_OilSealHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6030,
            )

            return self._parent._cast(_6030.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "OilSealHarmonicAnalysisOfSingleExcitation._Cast_OilSealHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6086,
            )

            return self._parent._cast(_6086.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "OilSealHarmonicAnalysisOfSingleExcitation._Cast_OilSealHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "OilSealHarmonicAnalysisOfSingleExcitation._Cast_OilSealHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "OilSealHarmonicAnalysisOfSingleExcitation._Cast_OilSealHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "OilSealHarmonicAnalysisOfSingleExcitation._Cast_OilSealHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "OilSealHarmonicAnalysisOfSingleExcitation._Cast_OilSealHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def oil_seal_harmonic_analysis_of_single_excitation(
            self: "OilSealHarmonicAnalysisOfSingleExcitation._Cast_OilSealHarmonicAnalysisOfSingleExcitation",
        ) -> "OilSealHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "OilSealHarmonicAnalysisOfSingleExcitation._Cast_OilSealHarmonicAnalysisOfSingleExcitation",
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
        self: Self, instance_to_wrap: "OilSealHarmonicAnalysisOfSingleExcitation.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2464.OilSeal":
        """mastapy.system_model.part_model.OilSeal

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6924.OilSealLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.OilSealLoadCase

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
    ) -> "OilSealHarmonicAnalysisOfSingleExcitation._Cast_OilSealHarmonicAnalysisOfSingleExcitation":
        return self._Cast_OilSealHarmonicAnalysisOfSingleExcitation(self)
