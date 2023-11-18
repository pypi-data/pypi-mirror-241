"""PlanetaryGearSetHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6054,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "PlanetaryGearSetHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2540


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="PlanetaryGearSetHarmonicAnalysisOfSingleExcitation")


class PlanetaryGearSetHarmonicAnalysisOfSingleExcitation(
    _6054.CylindricalGearSetHarmonicAnalysisOfSingleExcitation
):
    """PlanetaryGearSetHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryGearSetHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_PlanetaryGearSetHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting PlanetaryGearSetHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "PlanetaryGearSetHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetHarmonicAnalysisOfSingleExcitation",
            parent: "PlanetaryGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_harmonic_analysis_of_single_excitation(
            self: "PlanetaryGearSetHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(
                _6054.CylindricalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_set_harmonic_analysis_of_single_excitation(
            self: "PlanetaryGearSetHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6065,
            )

            return self._parent._cast(_6065.GearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(
            self: "PlanetaryGearSetHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6105,
            )

            return self._parent._cast(
                _6105.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(
            self: "PlanetaryGearSetHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6005,
            )

            return self._parent._cast(
                _6005.AbstractAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "PlanetaryGearSetHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6086,
            )

            return self._parent._cast(_6086.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "PlanetaryGearSetHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetaryGearSetHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetaryGearSetHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryGearSetHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.DesignEntityAnalysis)

        @property
        def planetary_gear_set_harmonic_analysis_of_single_excitation(
            self: "PlanetaryGearSetHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetHarmonicAnalysisOfSingleExcitation",
        ) -> "PlanetaryGearSetHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "PlanetaryGearSetHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2540.PlanetaryGearSet":
        """mastapy.system_model.part_model.gears.PlanetaryGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PlanetaryGearSetHarmonicAnalysisOfSingleExcitation._Cast_PlanetaryGearSetHarmonicAnalysisOfSingleExcitation":
        return self._Cast_PlanetaryGearSetHarmonicAnalysisOfSingleExcitation(self)
