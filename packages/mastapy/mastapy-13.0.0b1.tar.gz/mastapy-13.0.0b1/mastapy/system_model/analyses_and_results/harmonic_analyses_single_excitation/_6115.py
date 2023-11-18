"""StraightBevelGearHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6021,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "StraightBevelGearHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2545
    from mastapy.system_model.analyses_and_results.static_loads import _6960


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="StraightBevelGearHarmonicAnalysisOfSingleExcitation")


class StraightBevelGearHarmonicAnalysisOfSingleExcitation(
    _6021.BevelGearHarmonicAnalysisOfSingleExcitation
):
    """StraightBevelGearHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelGearHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_StraightBevelGearHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting StraightBevelGearHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "StraightBevelGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelGearHarmonicAnalysisOfSingleExcitation",
            parent: "StraightBevelGearHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def bevel_gear_harmonic_analysis_of_single_excitation(
            self: "StraightBevelGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelGearHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(_6021.BevelGearHarmonicAnalysisOfSingleExcitation)

        @property
        def agma_gleason_conical_gear_harmonic_analysis_of_single_excitation(
            self: "StraightBevelGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6009,
            )

            return self._parent._cast(
                _6009.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_harmonic_analysis_of_single_excitation(
            self: "StraightBevelGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6037,
            )

            return self._parent._cast(
                _6037.ConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_harmonic_analysis_of_single_excitation(
            self: "StraightBevelGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6063,
            )

            return self._parent._cast(_6063.GearHarmonicAnalysisOfSingleExcitation)

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "StraightBevelGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6084,
            )

            return self._parent._cast(
                _6084.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "StraightBevelGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6030,
            )

            return self._parent._cast(_6030.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "StraightBevelGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6086,
            )

            return self._parent._cast(_6086.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelGearHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "StraightBevelGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelGearHarmonicAnalysisOfSingleExcitation",
        ) -> "StraightBevelGearHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelGearHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "StraightBevelGearHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2545.StraightBevelGear":
        """mastapy.system_model.part_model.gears.StraightBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6960.StraightBevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearLoadCase

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
    ) -> "StraightBevelGearHarmonicAnalysisOfSingleExcitation._Cast_StraightBevelGearHarmonicAnalysisOfSingleExcitation":
        return self._Cast_StraightBevelGearHarmonicAnalysisOfSingleExcitation(self)
