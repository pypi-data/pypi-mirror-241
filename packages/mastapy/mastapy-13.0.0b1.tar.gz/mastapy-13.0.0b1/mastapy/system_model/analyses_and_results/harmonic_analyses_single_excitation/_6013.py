"""BearingHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6041,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "BearingHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2437
    from mastapy.system_model.analyses_and_results.static_loads import _6817


__docformat__ = "restructuredtext en"
__all__ = ("BearingHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="BearingHarmonicAnalysisOfSingleExcitation")


class BearingHarmonicAnalysisOfSingleExcitation(
    _6041.ConnectorHarmonicAnalysisOfSingleExcitation
):
    """BearingHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _BEARING_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BearingHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_BearingHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting BearingHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "BearingHarmonicAnalysisOfSingleExcitation._Cast_BearingHarmonicAnalysisOfSingleExcitation",
            parent: "BearingHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def connector_harmonic_analysis_of_single_excitation(
            self: "BearingHarmonicAnalysisOfSingleExcitation._Cast_BearingHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(_6041.ConnectorHarmonicAnalysisOfSingleExcitation)

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "BearingHarmonicAnalysisOfSingleExcitation._Cast_BearingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6084,
            )

            return self._parent._cast(
                _6084.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "BearingHarmonicAnalysisOfSingleExcitation._Cast_BearingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6030,
            )

            return self._parent._cast(_6030.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "BearingHarmonicAnalysisOfSingleExcitation._Cast_BearingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6086,
            )

            return self._parent._cast(_6086.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "BearingHarmonicAnalysisOfSingleExcitation._Cast_BearingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BearingHarmonicAnalysisOfSingleExcitation._Cast_BearingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BearingHarmonicAnalysisOfSingleExcitation._Cast_BearingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BearingHarmonicAnalysisOfSingleExcitation._Cast_BearingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BearingHarmonicAnalysisOfSingleExcitation._Cast_BearingHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def bearing_harmonic_analysis_of_single_excitation(
            self: "BearingHarmonicAnalysisOfSingleExcitation._Cast_BearingHarmonicAnalysisOfSingleExcitation",
        ) -> "BearingHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "BearingHarmonicAnalysisOfSingleExcitation._Cast_BearingHarmonicAnalysisOfSingleExcitation",
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
        self: Self, instance_to_wrap: "BearingHarmonicAnalysisOfSingleExcitation.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2437.Bearing":
        """mastapy.system_model.part_model.Bearing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6817.BearingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BearingLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[BearingHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.BearingHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BearingHarmonicAnalysisOfSingleExcitation._Cast_BearingHarmonicAnalysisOfSingleExcitation":
        return self._Cast_BearingHarmonicAnalysisOfSingleExcitation(self)
